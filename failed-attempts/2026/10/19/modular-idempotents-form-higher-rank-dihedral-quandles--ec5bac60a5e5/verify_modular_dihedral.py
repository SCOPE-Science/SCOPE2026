"""Independent small-field tests for modular dihedral-quandle idempotents.

Run with Python 3: python verify_modular_dihedral.py
No third-party packages needed. This script provides finite checks, not a proof.
"""
from itertools import product


def subgroup(p):
    h = {1}
    while True:
        nxt = h | {(-a) % p for a in h} | {(2*a) % p for a in h}
        if nxt == h:
            return h
        h = nxt


def cyclic_mul(a, b, p):
    c = [0]*p
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    c[(i+j) % p] = (c[(i+j) % p] + x*y) % p
    return c


def modular_star(a, b, p):
    c = [0]*p
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    c[(2*j-i) % p] = (c[(2*j-i) % p] + x*y) % p
    return c


def exp_augmentation(v, p):
    one = [1]+[0]*(p-1)
    total = one[:]
    power = one[:]
    factorial = 1
    for j in range(1, p):
        power = cyclic_mul(power, v, p)
        factorial = factorial*j % p
        scale = pow(factorial, -1, p)
        total = [(x+scale*y)%p for x,y in zip(total,power)]
    return total


def kernel_rank_mod_p(A, p):
    a = [[x%p for x in row] for row in A]
    n = len(a)
    row = 0
    for col in range(n):
        pivot = next((i for i in range(row,n) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col],-1,p)
        a[row] = [(x*inv)%p for x in a[row]]
        for i in range(n):
            if i != row and a[i][col]:
                v = a[i][col]
                a[i] = [(x-v*y)%p for x,y in zip(a[i],a[row])]
        row += 1
    return n-row


def canonical_vectors(p):
    H = subgroup(p)
    seen = set()
    answer = []
    for a in range(1,p):
        if a in seen:
            continue
        C = {(a*h)%p for h in H}
        seen |= C
        v = [0]*p
        for g in C:
            v[g] = pow(g,-1,p)
        assert sum(v)%p == 0
        answer.append(v)
    return answer


def check_prime(p):
    matrix = [[int(i == j) - int(i == (-j)%p) - int(i == (2*j)%p)
               for j in range(p)] for i in range(p)]
    actual = kernel_rank_mod_p(matrix,p)
    expected = (p-1)//len(subgroup(p))
    assert actual == expected, (p,actual,expected)
    vs = canonical_vectors(p)
    assert len(vs) == expected
    for v in vs:
        assert modular_star(exp_augmentation(v,p),exp_augmentation(v,p),p) == exp_augmentation(v,p)
    if len(vs) > 1:
        left,right = vs[:2]
        EL = exp_augmentation(left,p)
        ER = exp_augmentation(right,p)
        target = exp_augmentation([(-x+2*y)%p for x,y in zip(left,right)],p)
        assert modular_star(EL,ER,p) == target
        assert sum(int(c!=0) for c in EL)>1, 'new nonbasis idempotent not witnessed'
    return expected


def brute_prime(p):
    idempotents = []
    for u in product(range(p),repeat=p):
        if modular_star(u,u,p) == list(u):
            idempotents.append(u)
    expected = 1+p**((p-1)//len(subgroup(p)))
    assert len(idempotents) == expected, (p,len(idempotents),expected)
    assert sum(1 for u in idempotents if any(u) and sum(u)%p==0) == 0
    assert sum(1 for u in idempotents if sum(int(c!=0) for c in u)==1) == p
    return len(idempotents)


# The arithmetic for F_9 = F_3[u]/(u^2+1), encoded as a+3b.
def add9(x,y):
    return (x%3+y%3)%3+3*((x//3+y//3)%3)

def mul9(x,y):
    a,b=x%3,x//3; c,d=y%3,y//3
    return (a*c+2*b*d)%3 + 3*((a*d+b*c)%3)

def brute_q9():
    add = [[add9(x,y) for y in range(9)] for x in range(9)]
    mul = [[mul9(x,y) for y in range(9)] for x in range(9)]
    idem=[]
    for u in product(range(9),repeat=3):
        v = [0,0,0]
        for a in range(3):
            for b in range(3):
                j = (2*b-a)%3
                v[j] = add[v[j]][mul[u[a]][u[b]]]
        if v == list(u):
            idem.append(u)
    assert len(idem)==10, len(idem)
    assert sum(1 for u in idem if any(u) and add[add[u[0]][u[1]]][u[2]]==0) == 0
    return len(idem)


if __name__ == '__main__':
    for p in [3,5,7,11,13,17,19,23,31,41,73]:
        dim = check_prime(p)
        print(f'prime={p}, subgroup_size={len(subgroup(p))}, linear_dimension={dim}')
    for p in [3,5]:
        print(f'exhaustive F_{p} algebra: {brute_prime(p)} idempotents')
    print(f'exhaustive F_9 algebra on R_3: {brute_q9()} idempotents')
    print('VERIFY_OK: 11 rank tests, 2 prime-field exhaustive tests, 1 extension-field exhaustive test, explicit positive-dimensional witnesses')
