import itertools
from copy import deepcopy


def permutations(n: int):
    x = ['0', '1']
    res = set()

    perm_rep = [list(p) for p in itertools.product(x, repeat=n)]
    for per in perm_rep:
        i = 0
        while i < n + 1:
            comb = deepcopy(per)
            comb.insert(i, '1111')
            res.add(''.join(comb))
            i += 1
    return res


if __name__ == '__main__':
    # Number of days
    x = int(input())
    if x < 4:
        print("Number of days must be greater than 4")
    else:
        res = permutations(x - 4)
        print(str(len(res))+'/'+str(pow(2, x)))
