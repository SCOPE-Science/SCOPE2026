from itertools import product

checks = 0

def is_steiner(tab, n):
    global checks
    for a in range(n):
        if tab[a*n+a] != a:
            return False
        for b in range(n):
            if tab[a*n+b] != tab[b*n+a]:
                return False
            c = tab[a*n+b]
            if tab[a*n+c] != b:
                return False
    return True

def close(seed, op):
    global checks
    S=set(seed)
    while True:
        T=set(S)
        for a in S:
            for b in S:
                T.add(op(a,b))
        if T==S:
            return S
        S=T

# Exhaust every binary operation on three labeled points.
steiner=[]
for vals in product(range(3), repeat=9):
    if is_steiner(vals,3):
        steiner.append(vals)
assert len(steiner)==1; checks += 1
tab=steiner[0]
op3=lambda a,b:tab[a*3+b]
for a in range(3):
    assert close([a],op3)=={a}; checks += 1
for a in range(3):
    for b in range(3):
        if a!=b:
            assert close([a,b],op3)=={0,1,2}; checks += 1

# Fano Steiner quasigroup: the seven nonzero vectors of F_2^3.
pts=list(range(1,8))
def op7(a,b):
    return a if a==b else a^b
for a in pts:
    assert op7(a,a)==a; checks += 1
    for b in pts:
        assert op7(a,b)==op7(b,a); checks += 1
        assert op7(a,op7(a,b))==b; checks += 1

# Every pair closes to a 1- or 3-element subquasigroup.
for a in pts:
    for b in pts:
        c=close([a,b],op7)
        assert len(c)==(1 if a==b else 3); checks += 1

# Three independent Fano points generate all seven points.
assert close([1,2,4],op7)==set(pts); checks += 1

print(f"VERIFY_OK {checks} exact assertions")
