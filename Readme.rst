SwitchBot JSON API
------------------

SwitchBot Meter json api. 

NOTE: This API does not download the device CSV, it just scans its current
status via ble each X seconds.

TODO: Documentation (it's 1AM, pushing in case of fire)
TODO: OpenAPI specs

Usage with httpie::

        http get http://host:port/start

        http get http://host:port/latest

        http get http://host:port/all
