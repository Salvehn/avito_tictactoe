from proto import every, concat, some

matrix = []
finished = False
player = True


def initialize(dim: int = 0) -> list:
    temp = [[None for i in range(dim)] for j in range(dim)]
    return temp


matrix = initialize(3)


def check(lst):

    diagonal1 = every([lst[i][i] for i in range(len(lst))],
                      lambda x: x is False or x is True)
    diagonal2 = every([lst[i][len(lst)-i-1]
                      for i in range(len(lst))], lambda x: x is False or x is True)
    horizontal = some([every([c for c in row], lambda x:  x is False)
                      for row in lst], lambda x: x is True) or some([every([c for c in row], lambda x:  x is True)
                                        for row in lst], lambda x: x is True)
    collist = []
    for i in range(len(lst)):
        collist.append([lst[j][i] for j in range(len(lst[i]))]  )

    vertical = some([every([c for c in row], lambda x:  x is False)
                      for row in collist], lambda x: x is True) or some([every([c for c in row], lambda x:  x is True)
                                        for row in collist], lambda x: x is True)

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
    print('\n'.join(['|'.join([repl(c) for c in row]) for row in lst]))


while finished is False:
    print(concat(' ', 'Player ', str(1 if player else 2), 'Insert pos:'))
    address = input()
    xy = address.split(',')
    isInRange = (int(x)-1) < len(matrix) and (int(x) - 1) < len(matrix[0])
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
