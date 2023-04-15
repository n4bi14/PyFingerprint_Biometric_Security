import os
import datetime
import logging
import asyncio
import aiocoap.resource as resource
import aiocoap
from time import sleep

# open the encrypted fingerprint data
with open("encrypted_fingerprint.txt", "rb") as key_file:
    encrypted_data = key_file.read()
    encrypted_data = str(encrypted_data)

        
class FingerResource(resource.Resource):
    """Example resource which supports the GET method. It uses asyncio.sleep to
    simulate a long-running operation, and thus forces the protocol to send
    empty ACK first. """

    def get_link_description(self):
        # Publish additional data in .well-known/core
        return dict(**super().get_link_description(), title="Hello World Request")

    async def render_get(self, request):
        await asyncio.sleep(3)

        payload = encrypted_data.encode('ascii')
        return aiocoap.Message(payload=payload)
    
# logging setup
logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)

async def main():
    # Resource tree creation
    root = resource.Site()

    root.add_resource(['.well-known', 'core'],
            resource.WKCResource(root.get_resources_as_linkheader))
    root.add_resource(['finger'], FingerResource())

    await aiocoap.Context.create_server_context(root, bind=("149.162.131.101", 5683))

    # Run forever
    await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
    asyncio.run(main())


