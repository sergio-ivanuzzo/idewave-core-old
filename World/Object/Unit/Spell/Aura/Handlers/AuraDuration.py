from World.WorldPacket.Constants.WorldOpCode import WorldOpCode
from Server.Connection.Connection import Connection
from Typings.Abstract.AbstractHandler import AbstractHandler


class AuraDuration(AbstractHandler):

    def __init__(self, **kwargs):
        self.data: bytes = kwargs.pop('data', bytes())
        self.connection: Connection = kwargs.pop('connection')

    async def process(self):
        response = b'\x00\xff\xff\xff\xff'
        return WorldOpCode.SMSG_UPDATE_AURA_DURATION, [response]