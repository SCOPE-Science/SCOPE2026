"""Independent GF(4) direct check for rank-one idempotent sum fibers in M_2."""
import itertools,collections
Q=4

def mul(a,b):
    o=0
    for i in range(2):
        for j in range(2):
            if (a>>i)&1 and (b>>j)&1: o^=1<<(i+j)
    if o&8:o^=14 # t^3=t*t^2=t*(t+1)=1
    if o&4:o^=7 # t^2=t+1
    return o

def rank(A):
    a,b,c,d=A
    if mul(a,d)^mul(b,c):return 2
    return 1 if any(A) else 0

def fiber(A):
    a,b,c,d=A
    if a^d:return 0
    r=rank(A)
    if r==0:return 20
    if r==1:return 8
    if b==c==0 and a==d:return 20 if a==1 else 0
    # non-scalar trace-zero M over a perfect characteristic-two field:
    # one eigenline, eigenvalue lambda=(det M)^(2).
    det=mul(a,d)^mul(b,c)
    lam=mul(det,det)
    return 8 if lam==1 else 4

p=[]
for u in itertools.product(range(Q),repeat=2):
    if not any(u) or next(a for a in u if a)!=1:continue
    for v in itertools.product(range(Q),repeat=2):
        if mul(u[0],v[0])^mul(u[1],v[1])==1:
            p.append(tuple(mul(u[i],v[j]) for i in range(2) for j in range(2)))
obs=collections.Counter(tuple(a^b for a,b in zip(x,y)) for x in p for y in p)
for A in itertools.product(range(Q),repeat=4):
    assert obs.get(A,0)==fiber(A),(A,obs.get(A,0),fiber(A))
print('GF4 n=2 PASS: 20 rank-one idempotents, 400 ordered pairs, 256 targets, fiber distribution',dict(sorted(collections.Counter(obs.values()).items())))
print('GF4_RANK_ONE_IDEMPOTENT_SUM_PASS')
