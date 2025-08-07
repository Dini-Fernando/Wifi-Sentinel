import asyncio
from notificationapi_python_server_sdk import notificationapi

notificationapi.init(
  "am1ci5afjk0kn4yvcv9tdmnd01",
  "16nwh5jmkf8qc6rynxofw05jvxmgw0bxfanb71wcshbyq5f0wczyw7jhsb"
)

async def send_notification():
    await notificationapi.send({
      "type": "heads_up__a_new_device_has_joined_your_wifi",
      "to": {
         "email": "chamodifernando311@gmail.com",
         "number": "+94765551309"
      }
    })

