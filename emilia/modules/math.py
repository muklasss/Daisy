from typing import List
import requests
from telegram import Message, Update, Bot, MessageEntity
from telegram.ext import CommandHandler, run_async
from emilia import dispatcher
from emilia.modules.disable import DisableAbleCommandHandler
from emilia.modules.helper_funcs.alternate import send_message

@run_async
def cos(update, context):
    args = context.args
    message = update.effective_message
    message.reply_text(math.cos(int(args[0])))

@run_async
def sin(update, context):
    args = context.args
    message = update.effective_message
    message.reply_text(math.sin(int(args[0])))

@run_async
def tan(update, context):
    args = context.args
    message = update.effective_message
    message.reply_text(math.tan(int(args[0])))

@run_async
def arccos(update, context):
    args = context.args
    message = update.effective_message
    message.reply_text(math.acos(int(args[0])))

@run_async
def arcsin(update, context):
    args = context.args
    message = update.effective_message
    message.reply_text(math.asin(int(args[0])))

@run_async
def arctan(update, context):
    args = context.args
    message = update.effective_message
    message.reply_text(math.atan(int(args[0])))

@run_async
def abs(update, context):
    args = context.args
    message = update.effective_message
    message.reply_text(math.fabs(int(args[0])))

@run_async
def log(update, context):
    args = context.args
    message = update.effective_message
    message.reply_text(math.log(int(args[0])))

__help__ = """
Solves complex math problems using https://newton.now.sh
 
 - /cos: Cosine `/cos pi`
 - /sin: Sine `/sin 0`
 - /tan: Tangent `/tan 0`
 - /arccos: Inverse Cosine `/arccos 1`
 - /arcsin: Inverse Sine `/arcsin 0`
 - /arctan: Inverse Tangent `/arctan 0`
 - /abs: Absolute Value `/abs -1`
 - /log: Logarithm `/log 2l8`
__Keep in mind__: To find the tangent line of a function at a certain x value, send the request as c|f(x) where c is the given x value and f(x) is the function expression, the separator is a vertical bar '|'. See the table above for an example request.
To find the area under a function, send the request as c:d|f(x) where c is the starting x value, d is the ending x value, and f(x) is the function under which you want the curve between the two x values.
To compute fractions, enter expressions as numerator(over)denominator. For example, to process 2/4 you must send in your expression as 2(over)4. The result expression will be in standard math notation (1/2, 3/4).
"""




COS_HANDLER = DisableAbleCommandHandler("cos", cos, pass_args=True)
SIN_HANDLER = DisableAbleCommandHandler("sin", sin, pass_args=True)
TAN_HANDLER = DisableAbleCommandHandler("tan", tan, pass_args=True)
ARCCOS_HANDLER = DisableAbleCommandHandler("arccos", arccos, pass_args=True)
ARCSIN_HANDLER = DisableAbleCommandHandler("arcsin", arcsin, pass_args=True)
ARCTAN_HANDLER = DisableAbleCommandHandler("arctan", arctan, pass_args=True)
ABS_HANDLER = DisableAbleCommandHandler("abs", abs, pass_args=True)
LOG_HANDLER = DisableAbleCommandHandler("log", log, pass_args=True)


dispatcher.add_handler(COS_HANDLER)
dispatcher.add_handler(SIN_HANDLER)
dispatcher.add_handler(TAN_HANDLER)
dispatcher.add_handler(ARCCOS_HANDLER)
dispatcher.add_handler(ARCSIN_HANDLER)
dispatcher.add_handler(ARCTAN_HANDLER)
dispatcher.add_handler(ABS_HANDLER)
dispatcher.add_handler(LOG_HANDLER)

__mod_name__ = "Math"
__command_list__ = ["math","factor","derive","integrate","zeroes","tangent","area","cos","sin","tan","arccos","arcsin","arctan","abs","log"]
__handlers__ = [
    SIMPLIFY_HANDLER,FACTOR_HANDLER,DERIVE_HANDLER,INTEGRATE_HANDLER,ZEROES_HANDLER,TANGENT_HANDLER,AREA_HANDLER,AREA_HANDLER,COS_HANDLER,SIN_HANDLER,TAN_HANDLER,ARCCOS_HANDLER,ARCSIN_HANDLER,ARCTAN_HANDLER,ABS_HANDLER,LOG_HANDLER
]
