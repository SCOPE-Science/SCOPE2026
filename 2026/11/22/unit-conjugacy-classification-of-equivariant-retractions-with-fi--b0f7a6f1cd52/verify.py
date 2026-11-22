"""Finite independent enumeration of equivariant retraction orbit profiles."""
from itertools import product, permutations
from collections import defaultdict
from math import factorial, comb


def make_cyclic(k):
    els=tuple(range(k))
    return els,0,lambda a,b:(a+b)%k,lambda a:(-a)%k, (1,)


def make_s3():
    els=tuple(permutations(range(3)))
    one=tuple(range(3))
    mul=lambda a,b:tuple(a[b[i]] for i in range(3))
    inv=lambda a:tuple(a.index(i) for i in range(3))
    return els,one,mul,inv,((1,0,2),(1,2,0))


def enumerate_idempotents(a,b,els,one):
    for f in product(range(a),repeat=a):
        if any(f[f[i]] != f[i] for i in range(a)):
            continue
        opts=[('F',i,None) for i in range(a)]+[('R',j,g) for j in range(b) for g in els]
        for r in product(opts,repeat=b):
            if any((f[z[1]]!=z[1] if z[0]=='F' else r[z[1]]!=('R',z[1],one)) for z in r):
                continue
            yield f,r


def profile(e,a,b,one):
    f,r=e
    fixed=[]
    for i in range(a):
        if f[i]==i:
            fixed.append((sum(v==i for v in f),sum(z[0]=='F' and z[1]==i for z in r)))
    free=[]
    for j in range(b):
        if r[j]==('R',j,one):
            free.append(sum(z[0]=='R' and z[1]==j for z in r))
    return tuple(sorted(fixed)),tuple(sorted(free))


def orbit_cardinality(profile,a,b,m):
    fixed,free=profile
    fm=defaultdict(int)
    rm=defaultdict(int)
    for s,t in fixed: fm[s,t]+=1
    for c in free: rm[c]+=1
    den=1
    for (s,t),num in fm.items():den*=factorial(num)*(factorial(s-1)*factorial(t))**num
    for c,num in rm.items():den*=factorial(num)*factorial(c-1)**num
    numerator=factorial(a)*factorial(b)*m**sum(c-1 for c in free)
    assert numerator%den==0
    return numerator//den


def conjugate(e,a,b,u,one,mul,inv):
    f,r=e; p,s,k=u
    pin=[p.index(i) for i in range(a)]
    sin=[s.index(j) for j in range(b)]
    ff=tuple(p[f[pin[i]]] for i in range(a))
    rr=[]
    for j in range(b):
        old=sin[j]
        typ,tar,g=r[old]
        if typ=='F':rr.append(('F',p[tar],None))
        else:rr.append(('R',s[tar],mul(mul(inv(k[old]),g),k[tar])))
    return ff,tuple(rr)


def generators(a,b,els,one,groupgens):
    pf=tuple(range(a));sr=tuple(range(b));sh=(one,)*b
    for i in range(a-1):
        pp=list(pf);pp[i],pp[i+1]=pp[i+1],pp[i];yield tuple(pp),sr,sh
    for j in range(b-1):
        ss=list(sr);ss[j],ss[j+1]=ss[j+1],ss[j];yield pf,tuple(ss),sh
    for j in range(b):
        for g in groupgens:
            kk=list(sh);kk[j]=g;yield pf,sr,tuple(kk)


def expected_profiles(a,b):
    # Independent coefficient extraction from the two infinite Euler products:
    # partitions into mixed blocks (s,t) and free-root blocks (0,c).
    types=[(s,t) for s in range(1,a+1) for t in range(b+1)] + [(0,c) for c in range(1,b+1)]
    found=set()
    def visit(i,aa,bb,fixed,free):
        if i==len(types):
            if aa==bb==0:found.add((tuple(sorted(fixed)),tuple(sorted(free))))
            return
        s,t=types[i]
        for k in range(min(aa//s if s else b+1, bb//t if t else a+1)+1):
            if k*s>aa or k*t>bb:continue
            visit(i+1,aa-k*s,bb-k*t,fixed+([(s,t)]*k if s else []),free+([t]*k if not s else []))
    visit(0,a,b,[],[])
    return found


def labeled_count_formula(a,b,m):
    return sum(comb(a,k)*comb(b,l)*(k**(a-k))*((k+m*l)**(b-l))
               for k in range(a+1) for l in range(b+1))


def test_case(a,b,group,orbit_check=True):
    els,one,mul,inv,groupgens=group
    obj=list(enumerate_idempotents(a,b,els,one))
    buckets=defaultdict(set)
    for e in obj:buckets[profile(e,a,b,one)].add(e)
    assert sum(len(t) for t in buckets.values())==len(obj)
    assert set(buckets)==expected_profiles(a,b),(a,b,set(buckets)^expected_profiles(a,b))
    assert len(obj)==labeled_count_formula(a,b,len(els)),(a,b,len(els),len(obj))
    for prof, bucket in buckets.items():
        assert len(bucket)==orbit_cardinality(prof,a,b,len(els)),(a,b,len(els),prof,len(bucket))
    if orbit_check:
        units=list(generators(a,b,els,one,groupgens))
        for prof,bucket in buckets.items():
            seen={next(iter(bucket))}
            todo=list(seen)
            while todo:
                e=todo.pop()
                for u in units:
                    d=conjugate(e,a,b,u,one,mul,inv)
                    assert d in bucket,(a,b,prof,e,u,d)
                    if d not in seen:seen.add(d);todo.append(d)
            assert seen==bucket,(a,b,len(els),prof,len(seen),len(bucket))
    return len(obj),len(buckets)

if __name__=='__main__':
    tests=0
    for m in (2,3):
        g=make_cyclic(m)
        for a in range(0,4):
            for b in range(0,4):
                if a==b==0:continue
                if a+b*m>9:continue
                total,nclasses=test_case(a,b,g,True)
                print(f'C_{m} a={a} b={b} idempotents={total} orbit_classes={nclasses}')
                tests+=1
    g=make_s3()
    for a,b in ((0,1),(0,2),(1,1),(1,2),(2,1),(2,2)):
        total,nclasses=test_case(a,b,g,True)
        print(f'S3 a={a} b={b} idempotents={total} orbit_classes={nclasses}')
        tests+=1
    print(f'GSET_RETRACTION_UNIT_ORBITS_VERIFIED cases={tests}')
