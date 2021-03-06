from protorpc import messages
from protorpc import message_types

class MessageNone(messages.Message):
    inti = messages.StringField(1)

class AdditionalExpenseUpdate(messages.Message):
    token = messages.StringField(1, required = True) 
    quotationKey = messages.StringField(2)
    description = messages.StringField(3)
    price = messages.FloatField(4)
    comment = messages.StringField(5)
    entityKey = messages.StringField(6, required = True)