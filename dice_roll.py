from numpy import random
from message_log import MessageLog


def roll(diesize: int) -> int:
    result = random.randint(diesize)+1
    #MessageLog.add_message("1d" + str(diesize) + "  =  " + str(result))
    return result





