from protorpc import messages
from protorpc import message_types

from CompanyUpdate import CompanyUpdate

class MessageNone(messages.Message):
    inti = messages.StringField(1)

class CompanyList(messages.Message):
    code = messages.IntegerField(1)
    data = messages.MessageField(CompanyUpdate, 2, repeated = True)