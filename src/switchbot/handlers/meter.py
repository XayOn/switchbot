"""Notify."""
import asyncio
from aiojobs.aiohttp import spawn
import json
from aiohttp import web
from aioswitchbotmeter import DevScanner


async def all(request):
    return web.json_response([])


async def latest(request):
    return web.json_response(request.app['meter_storage'][-1])


async def start(request):

    async def scanner_async(request):
        scanner = DevScanner(request.rel_url.query.get('device', 'hci0'), int(request.rel_url.query.get('wait_time', 5)))
        async for result in scanner.scan():
            request.app['meter_storage'].append(result)

    await spawn(request, scanner_async(request))
    return web.json_response({'status': 'ok'})
