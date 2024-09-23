import time
from random import randint
from logg import Logg

logger = Logg('robo2', 'robo2.json')


while True:
    random1 = randint(0,15)
    random2 = randint(1,10)

    if random1 > 11:
        random1 = 0
    if(random1<=4):
        print(logger.info('Mensagem de informacao!'))
    elif(random1>=5 and random1<=8):
        print(logger.warning('Mensagem de aviso!'))
    elif(random1>=9 and random1<=10):
        print(logger.error('Mensagem de erro!'))
    else:
        print(logger.critical('Mensagem critica!'))

    time.sleep(random2)