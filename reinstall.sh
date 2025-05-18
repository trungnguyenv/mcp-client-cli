#!/usr/bin/env bash

uv build && uv tool install --reinstall dist/mcp_client_cli-1.0.4-py3-none-any.whl
