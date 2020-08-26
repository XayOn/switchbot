"""Meter"""
from pathlib import Path
import asyncio
from aiojobs.aiohttp import spawn
import json
from aiohttp import web
from aioswitchbotmeter import DevScanner

ABSP = Path(__file__).parent.parent


async def all(request):
    """Return all stored meter values"""
    return web.json_response(request.app['meter_storage'].all())


async def latest(request):
    """Return latest meter reading"""
    return web.json_response(request.app['meter_storage'].latest())

async def start(request):
    """Start meter reading process for a given device and wait time."""
    async def scanner_async(request):
        scanner = DevScanner(request.rel_url.query.get('device', 'hci0'),
                             int(request.rel_url.query.get('wait_time', 5)))
        async for result in scanner.scan():
            request.app['meter_storage'].append(result)

    await spawn(request, scanner_async(request))
    return web.json_response({'status': 'ok'})

async def index(request):
    return web.FileResponse(str(ABSP / 'templates' / 'index.html'))
