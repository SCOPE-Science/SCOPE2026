#!/usr/bin/env python3
"""Exact combinatorial, algebraic and finite-field checks for a 12-conic configuration.
Only Python's standard library is required.
"""
import collections
import itertools
import math

# Z[L] represented by low-to-high coefficient tuples.
def normpoly(a):
    a = list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return tuple(a)
def plus(a,b):
    return normpoly(tuple((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                          for i in range(max(len(a),len(b)))))
def neg(a): return tuple(-v for v in a)
def mult(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return normpoly(tuple(c))
Z=(0,); O=(1,); L=(0,1)
# Z[omega]/(omega^2+omega+1) with coefficients from Z[L]
def e(a,b=Z): return (a,b)
def ea(x,y):return (plus(x[0],y[0]),plus(x[1],y[1]))
def en(x):return (neg(x[0]),neg(x[1]))
def es(x,y):return ea(x,en(y))
def em(x,y):
    a,b=x;c,d=y
    bc=mult(b,d)
    return (plus(mult(a,c),neg(bc)),
            plus(plus(mult(a,d),mult(b,c)),neg(bc)))
def econj(x):return (plus(x[0],neg(x[1])),neg(x[1]))
def enorm(x):
    n=em(x,econj(x))
    assert n[1]==Z
    return n[0]
def det3(rows):
    out=e(Z)
    for perm in itertools.permutations(range(3)):
        v=e(O)
        for i in range(3):v=em(v,rows[i][perm[i]])
        inv=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        out=ea(out,en(v) if inv%2 else v)
    return out
def div_monic(f,g):
    a=list(f); g=list(g)
    if len(a)<len(g):return (f,False)
    assert g[-1]==1
    while len(a)>=len(g):
        c=a[-1]
        for i in range(len(g)):
            a[len(a)-len(g)+i]-=c*g[i]
        while len(a)>1 and a[-1]==0:a.pop()
    return (tuple(a),not any(a))
# build Hesse dual flex-tangent coordinates: (1,eta^2,L eta) cyclic,
# where eta runs through the three cube roots of one.
roots=[e(O),e(Z,O),e(neg(O),neg(O))]
pts=[]
for r in roots:
    r2=em(r,r)
    lr=em(e(L),r)
    pts.extend([[e(O),r2,lr],[lr,e(O),r2],[r2,lr,e(O)]])
factors=[L,(-1,1),(1,1,1),(2,1),(4,-2,1)]
max_residual=0
for tri in itertools.combinations(range(9),3):
    f=enorm(det3([pts[i] for i in tri]))
    assert f!=Z
    # exact division, returning quotient when remainder zero
    for g in factors:
        while len(f)>=len(g):
            a=list(f);b=list(g);quo=[0]*(len(a)-len(b)+1)
            while len(a)>=len(b):
                c=a[-1];p=len(a)-len(b);quo[p]=c
                for k,v in enumerate(b):a[p+k]-=c*v
                while len(a)>1 and a[-1]==0:a.pop()
            if all(x==0 for x in a):f=normpoly(tuple(quo))
            else:break
    assert len(f)==1 and abs(f[0]) in (1,3,9,27), (tri,f)
    max_residual=max(max_residual,abs(f[0]))
print('HESSE_DUAL_NO_EXTRA_TRIPLE_DETERMINANT_FACTORS',84,max_residual)

# The affine plane of order three and the conic indexing objects.
V=tuple(itertools.product(range(3),repeat=2))
Vidx={v:i for i,v in enumerate(V)}
Lines=[]
for a,b in V:
    if (a,b)==(0,0):continue
    for c in range(3):
        s=frozenset(v for v in V if (a*v[0]+b*v[1])%3==c)
        if s not in Lines:Lines.append(s)
Lidx={l:i for i,l in enumerate(Lines)}
Pairs=[(i,j) for i in range(12) for j in range(i+1,12) if not (Lines[i]&Lines[j])]
Pairsidx={p:i for i,p in enumerate(Pairs)}
I=[(i,v) for i in range(12) for v in range(9) if V[v] not in Lines[i]]
J=[(i,j) for i,j in itertools.permutations(range(12),2) if not (Lines[i]&Lines[j])]
assert (len(V),len(Lines),len(Pairs),len(I),len(J))==(9,12,12,72,24)

def cycles(mapping,universe):
    seen=set();out=[]
    for start in universe:
        if start in seen:continue
        cur=start;r=0
        while cur not in seen:
            seen.add(cur);r+=1;cur=mapping[cur]
        assert cur==start
        out.append(r)
    return tuple(sorted(out))

def signature(M,t):
    a,b,c,d=M
    fv={x:((a*x[0]+b*x[1]+t[0])%3,(c*x[0]+d*x[1]+t[1])%3) for x in V}
    fl={i:Lidx[frozenset(fv[v] for v in l)] for i,l in enumerate(Lines)}
    fp={x:tuple(sorted((fl[x[0]],fl[x[1]]))) for x in Pairs}
    fi={x:(fl[x[0]],Vidx[fv[V[x[1]]]]) for x in I}
    fj={x:(fl[x[0]],fl[x[1]]) for x in J}
    return (cycles(fv,V),cycles(fl,range(12)),cycles(fp,Pairs),cycles(fi,I),cycles(fj,J))

def fix(cycle,n):return sum(c for c in cycle if n%c==0)
def count(sig,Q,n):
    v,l,u,i,j=sig
    return (Q**n+1)*fix(l,n)+fix(v,n)+fix(u,n)-fix(i,n)-fix(j,n)
def formula(sig):
    v,l,u,i,j=sig
    return (fix(l,1),fix(l,1)+fix(v,1)+fix(u,1)-fix(i,1)-fix(j,1))
GL=[m for m in itertools.product(range(3),repeat=4) if (m[0]*m[3]-m[1]*m[2])%3]
profiles=collections.defaultdict(list)
for m in GL:
    for t in V:profiles[signature(m,t)].append((m,t))
assert len(profiles)==10
profile_counts=collections.Counter((len(reps),math.lcm(*sig[0],*sig[1]),formula(sig))
                                    for sig,reps in profiles.items())
expected={(1,1,(12,-63)),(36,2,(4,-1)),(9,2,(4,9)),
          (24,3,(3,-3)),(48,3,(0,0)),(8,3,(3,0)),
          (54,4,(0,1)),(72,6,(1,3)),(72,6,(1,2)),(108,8,(0,1))}
assert set(profile_counts)==expected,(set(profile_counts)^expected)
print('AFFINE_CLASSES_OK',sum(map(len,profiles.values())),len(profiles))
# Conjugacy is slightly finer: the two order-eight classes share a signature.
def mm(A,B):
    a,b,c,d=A;e,f,g,h=B
    return ((a*e+b*g)%3,(a*f+b*h)%3,(c*e+d*g)%3,(c*f+d*h)%3)
def mv(A,v):
    a,b,c,d=A
    return ((a*v[0]+b*v[1])%3,(c*v[0]+d*v[1])%3)
def gc(x,y):
    A,t=x;B,u=y
    w=mv(A,u)
    return (mm(A,B),((w[0]+t[0])%3,(w[1]+t[1])%3))
def gi(x):
    A,t=x;a,b,c,d=A
    idet=pow((a*d-b*c)%3,-1,3)
    B=((d*idet)%3,(-b*idet)%3,(-c*idet)%3,(a*idet)%3)
    u=mv(B,t)
    return (B,((-u[0])%3,(-u[1])%3))
remain={(m,t) for m in GL for t in V}
class_sizes=[]
while remain:
    x=next(iter(remain))
    cl={gc(gc(y,x),gi(y)) for y in ((m,t) for m in GL for t in V)}
    class_sizes.append(len(cl))
    remain-=cl
assert sorted(class_sizes)==[1,8,9,24,36,48,54,54,54,72,72]
print('AGL_CONJUGACY_CLASSES_OK',len(class_sizes))

def curve_count(p,a,b):
    assert (4*a**3+27*b*b)%p
    n=1+sum(1 for x in range(p) for y in range(p) if (y*y-x**3-a*x-b)%p==0)
    j=1728*4*a**3*pow((4*a**3+27*b*b)%p,-1,p)%p
    return n,j
assert curve_count(5,3,2)==(5,4)
assert curve_count(7,1,3)==(6,5)
# order-eight Frobenius: trace 1 and determinant 5=2 mod 3
s8=signature((0,1,1,1),(0,0))
assert all([s8[0]==(1,8),s8[1]==(4,8),s8[2]==(4,8),
            s8[3]==(8,)*9,s8[4]==(8,)*3])
for n in range(1,17):
    target=1 if n%4 else ((4*5**n+9) if n%8 else (12*5**n-63))
    assert count(s8,5,n)==target
print('F5_UNIQUE_RATIONAL_POINT_OK',count(s8,5,1))
# Frobenius on E[3] at p=7 has nontrivial unipotent form; choose torsor
# class not in (M-I)V, corresponding to non-3-divisible rational P.
s3=signature((0,1,2,2),(0,1))
assert s3[0]==(3,3,3) and s3[1]==(3,3,3,3)
assert count(s3,7,1)==0 and count(s3,7,3)==12*7**3-63
print('F7_POINT_FREE_CONFIGURATION_OK',count(s3,7,1))
print('CHILEAN_ARITHMETIC_CERTIFICATE_OK')
