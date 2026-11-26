from fractions import Fraction
from itertools import product
from math import prod

ASSERTS=0

def check(cond,msg):
    global ASSERTS
    ASSERTS += 1
    if not cond:
        raise AssertionError(msg)

def omega(n):
    c=0; d=2
    while d*d<=n:
        while n%d==0:
            c+=1; n//=d
        d += 1 if d==2 else 2
    if n>1: c+=1
    return c

def criterion(fr):
    p,q=fr.numerator,fr.denominator
    if p==1:
        return True
    if p & (p-1):
        return False
    a=p.bit_length()-1
    # reduced fraction with power-of-two numerator has odd denominator
    return q%2==1 and omega(q)>=a

def all_posets(n):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    for states in product((0,1,2), repeat=len(pairs)):
        # 0 incomparable, 1 i<j, 2 j<i
        le=[[False]*n for _ in range(n)]
        for i in range(n): le[i][i]=True
        for (i,j),s in zip(pairs,states):
            if s==1: le[i][j]=True
            elif s==2: le[j][i]=True
        ok=True
        for i in range(n):
            for j in range(n):
                if not le[i][j]: continue
                for k in range(n):
                    if le[j][k] and not le[i][k]:
                        ok=False; break
                if not ok: break
            if not ok: break
        if ok:
            yield le

def upsets(le):
    n=len(le); out=[]
    for mask in range(1<<n):
        ok=True
        for i in range(n):
            if mask>>i & 1:
                for j in range(n):
                    if le[i][j] and not (mask>>j & 1):
                        ok=False; break
            if not ok: break
        if ok: out.append(mask)
    return out

def down_closure(le,mask):
    n=len(le); d=0
    for x in range(n):
        for y in range(n):
            if (mask>>y)&1 and le[x][y]:
                d |= 1<<x; break
    return d

def components(le):
    n=len(le); seen=set(); comps=[]
    for s in range(n):
        if s in seen: continue
        stack=[s]; seen.add(s); comp=[]
        while stack:
            x=stack.pop(); comp.append(x)
            for y in range(n):
                if y not in seen and x!=y and (le[x][y] or le[y][x]):
                    seen.add(y); stack.append(y)
        comps.append(comp)
    return comps

def restrict(le,inds):
    return [[le[i][j] for j in inds] for i in inds]

expected_counts={1:1,2:3,3:19,4:219,5:4231}
value_sets={}
total=0
for n in range(1,6):
    cnt=0; vals=set()
    for le in all_posets(n):
        cnt+=1; total+=1
        ups=upsets(le); size=len(ups); full=(1<<n)-1
        em=[]
        for U in ups:
            neg=full ^ down_closure(le,U)
            check(neg in ups, f'negation not upset n={n}')
            if U | neg == full:
                em.append(U)
        c=len(components(le))
        check(len(em)==2**c, f'center size mismatch n={n} em={len(em)} c={c}')
        fr=Fraction(len(em),size)
        check(criterion(fr), f'criterion necessity fails {fr} n={n}')
        # product decomposition by connected components
        ns=[]
        for comp in components(le):
            ni=len(upsets(restrict(le,comp)))
            check(ni>=2,'factor too small')
            ns.append(ni)
        check(size==prod(ns), f'upset product size mismatch n={n}')
        check(fr==prod((Fraction(2,ni) for ni in ns), start=Fraction(1,1)), f'product degree mismatch {fr} {ns}')
        vals.add(fr)
    check(cnt==expected_counts[n], f'labelled poset count mismatch n={n} got {cnt}')
    value_sets[n]=vals

# Exact arithmetic equivalence of the two spectrum descriptions over a substantial finite box.
for r in range(1,5):
    for ns in product(range(2,13), repeat=r):
        fr=prod((Fraction(2,k) for k in ns), start=Fraction(1,1))
        check(criterion(fr), f'product value rejected {fr} from {ns}')

# Converse construction for every reduced rational p/q in a finite box satisfying the criterion.
def prime_factors(n):
    fs=[]; d=2
    while d*d<=n:
        while n%d==0:
            fs.append(d); n//=d
        d += 1 if d==2 else 2
    if n>1: fs.append(n)
    return fs

for q in range(1,151):
    for a in range(0,7):
        p=1<<a
        fr=Fraction(p,q)
        if fr>1 or fr.numerator!=p: # only already reduced p/q in stated form
            continue
        if criterion(fr):
            if p==1:
                ns=[2*q]
            else:
                fs=prime_factors(q)
                check(len(fs)>=a, 'omega condition inconsistency')
                # group odd prime factors into exactly a integers >=3
                groups=[fs[i] for i in range(a)]
                for j,f in enumerate(fs[a:]): groups[j%a]*=f
                ns=groups
            got=prod((Fraction(2,k) for k in ns), start=Fraction(1,1))
            check(got==fr, f'converse construction failed {fr} via {ns}')

# Selected membership/nonmembership regression values.
for s in ['1','2/3','1/2','4/9','2/5','1/3','4/15','8/27','16/81']:
    check(criterion(Fraction(s)),f'expected member {s}')
for s in ['4/5','8/15','8/21','16/45','3/4','6/7']:
    check(not criterion(Fraction(s)),f'expected nonmember {s}')

print('VERIFY_OK', ASSERTS, 'exact assertions;', total, 'labelled posets checked')
for n in range(1,6):
    print('n=',n,'degree_values=',','.join(str(x) for x in sorted(value_sets[n], reverse=True)))
