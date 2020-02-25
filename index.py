from proto import every, concat, some

matrix = []
finished = False
player = True


def initialize(dim: int = 0) -> list:
    temp = [[None for i in range(dim)] for j in range(dim)]
    return temp


matrix = initialize(3)


def check(lst):
    # first diagonal
    d1 = [lst[i][i] for i in range(len(lst))]
    diagonal1 = every(d1, lambda x: x is False) or every(
        d1, lambda x: x is True)

    # second diagonal
    d2 = [lst[i][len(lst)-i-1] for i in range(len(lst))]
    diagonal2 = every(d2, lambda x: x is False) or every(
        d2, lambda x: x is True)

    h = [every([c for c in row], lambda x:  x is False) for row in lst]
    horizontal = some(h, lambda x: x is True) or some(h, lambda x: x is True)

    collist = []
    for i in range(len(lst)):
        collist.append([lst[j][i] for j in range(len(lst[i]))])

    v = [every([c for c in row], lambda x:  x is False) for row in collist]
    vertical = some(v, lambda x: x is True) or some(v, lambda x: x is True)

    if horizontal or vertical or diagonal1 or diagonal2:
        return True
    else:
        return False


def repl(x):
    if x is not None:
        if x is True:
            return ' ✕  '
        else:
            return ' ◯  '
    else:
        return '    '


def mask(lst):
    data = ['|'.join([repl(c) for c in row]) for row in lst]

    print('\n──────────────\n'.join(data))


while finished is False:
    print(concat(' ', 'Player ', str(1 if player else 2), 'Insert pos:'))
    address = input()
    xy = address.split(',')
    isInRange = (
        int(xy[0])-1) < len(matrix) and (int(xy[1]) - 1) < len(matrix[0])
    isNotTaken = matrix[int(xy[0]) - 1][int(xy[1]) - 1] is None

    if every(xy, lambda x: x.isdigit() and isInRange and isNotTaken):
        matrix[int(xy[0]) - 1][int(xy[1]) - 1] = player
        mask(matrix)
        if check(matrix):
            finished = True
            print(concat(' ', 'Player ', str(1 if player else 2), 'won'))
            break
        player = not player
    else:
        print('Invalid address')
