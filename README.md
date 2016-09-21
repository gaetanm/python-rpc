# Project_2: RPC client/server over HTTP

## Examples

### Server

`$> python http_rpc_server.py`

### Client

```
Client.time(self) -> int
Client.ram(self) -> int, int
Client.hdd(self) -> int, int
Client.add(self, a, b) -> int
Client.sub(self, a, b) -> int
Client.json_to_xml(self, json_string) -> xml_string
```