from proto import every, concat, some
import random

#initializes matrix
def initialize(dim: int = 0) -> list:
    temp = [[None for i in range(dim)] for j in range(dim)]
    return temp


# checks for winning pattern
def check(lst: list) -> bool:
    # first diagonal
    d1 = [lst[i][i] for i in range(len(lst))]
    diagonal1 = every(d1, lambda x: x is False) or every(
        d1, lambda x: x is True)


    # second diagonal
    d2 = [lst[i][len(lst)-i-1] for i in range(len(lst))]
    diagonal2 = every(d2, lambda x: x is False) or every(
        d2, lambda x: x is True)

    # horizontal pattern
    h = [every([c for c in row], lambda x:  x is False) or every([c for c in row], lambda x:  x is True)  for row in lst]
    horizontal = some(h, lambda x: x is True)

    collist = []
    for i in range(len(lst)):
        collist.append([lst[j][i] for j in range(len(lst[i]))])


    # vertical pattern
    v = [every([c for c in row], lambda x:  x is False) or every([c for c in row], lambda x:  x is True) for row in collist]
    vertical = some(v, lambda x: x is True)

    if horizontal or vertical or diagonal1 or diagonal2:
        return True
    else:
        return False


# masks boolean into circle or cross
def repl(x) -> str:
    if x is not None:
        if x is True:
            return ' ✕ '
        else:
            return ' ◯ '
    else:
        return '   '


# creates TicTacToe view
def mask(lst: list):
    data = ['┃'.join([repl(c) for c in row]) for row in lst]
    str = ['━━━' for c in lst]
    return ('\n'+('╋'.join(str))+'\n').join(data)


#converts input to addr
def addrToInd(xy: list) -> list:
    return [int(i) if i.isdigit() else -1 for i in xy]


# validates if address is in range
def isInRange(addr: list, matrix: list) -> bool:
    return ((addr[0]-1) < len(matrix) and (addr[1] - 1) < len(matrix[0])) and ((
            addr[0]-1) >=0 and (addr[1] - 1) >= 0 )


# validates if address wasnt taken
def isNotTaken(addr: list, matrix: list) -> bool:
    return matrix[addr[0] - 1][addr[1] - 1] is None


def start():
    option = ''
    options = {'Авто': 1, 'Ручной': 2, 'Полу': 3}
    while option not in options:
        print('Выберите режим: {}/{}/{}'.format(*options))
        option = input()
        if not option:
            option = 'Ручной'
        if options[option]:
            mode = options[option]


    print('Enter dimension: ')
    dim = input()
    if not dim:
        print('Matrix dimensions error, generating default 3x3 matrix')
        dim = 3
    dim = int(dim)
    matrix = initialize(dim)


    print('TicTacToe!\n')
    print(mask(matrix),'\n')

    finished = False
    player = True

    while finished is False:

        if mode == 2:
            print(concat(' ', 'Player ', str(1 if player else 2), 'Insert pos:'))
            address = input()
            xy = address.split(',')
            xy = addrToInd(xy)
        elif mode == 1:
            xy=[random.randint(0,int(dim)),random.randint(0,int(dim))]
        else:
            if player:
                print(concat(' ', 'Player ', str(1 if player else 2), 'Insert pos:'))
                address = input()
                xy = address.split(',')
                xy = addrToInd(xy)
            else:
                xy=[random.randint(0,int(dim)),random.randint(0,int(dim))]


        # validates all
        if isInRange(xy,matrix) and isNotTaken(xy,matrix):
            matrix[xy[0] - 1][xy[1] - 1] = player

            print(mask(matrix))

            # checks if there are still unused cells
            a = [every([c for c in row], lambda x: x is False or x is True) for row in matrix]
            available = every(a, lambda x: x is True)
            if available:
                print('Draw')
                break
                return
            if check(matrix):
                finished = True
                print(concat(' ', '\nPlayer', str(1 if player else 2), 'won!'))
                break
                return
            player = not player
        else:
            if mode == 2:
                print('Invalid address')
            else:
                if player:
                    print('Invalid address')

if __name__ == '__main__':
    start()
