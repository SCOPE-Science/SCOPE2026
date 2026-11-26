from itertools import product

checks = 0

def ok(cond, msg=''):
    global checks
    checks += 1
    assert cond, msg

# Enumerate all binary operations on {0,1,2}; retain exactly the Steiner-quasigroup tables.
steiner = []
for vals in product(range(3), repeat=9):
    def mul(a,b):
        return vals[3*a+b]
    if any(mul(a,a) != a for a in range(3)):
        continue
    if any(mul(a,b) != mul(b,a) for a in range(3) for b in range(3)):
        continue
    if any(mul(a,mul(a,b)) != b for a in range(3) for b in range(3)):
        continue
    steiner.append(vals)

ok(len(steiner) == 1, 'There should be one labeled Steiner quasigroup on three fixed labels.')
vals = steiner[0]
def mul(a,b): return vals[3*a+b]

expected = (
    0,2,1,
    2,1,0,
    1,0,2,
)
ok(vals == expected, 'Unexpected 3-element Steiner table.')

# One generator is closed; two distinct generators close after adjoining their product.
def closure(seed):
    s=set(seed)
    changed=True
    while changed:
        changed=False
        for a in tuple(s):
            for b in tuple(s):
                c=mul(a,b)
                if c not in s:
                    s.add(c); changed=True
    return s

for a in range(3):
    ok(closure({a}) == {a})
for a in range(3):
    for b in range(3):
        if a != b:
            ok(closure({a,b}) == {0,1,2})
            z=mul(a,b)
            ok(z not in {a,b})
            ok(mul(a,z) == b)
            ok(mul(b,z) == a)

# Symbolic multiplication on the three normal forms x,y,z=x*y is closed.
# 0=x, 1=y, 2=z. This checks every product of normal forms.
for a in range(3):
    for b in range(3):
        ok(mul(a,b) in {0,1,2})

print(f'VERIFY_OK {checks} exact assertions')
