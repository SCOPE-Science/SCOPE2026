#!/usr/bin/env python3
"""Independent point-equation and complete line scan for the BKS octic over GF(343)."""
from collections import Counter

p,q=7,343
# F_343=F_7[v]/(v^3+v+1), a different field presentation.
def dec(x):return x%p,(x//p)%p,x//(p*p)
def enc(a,b,c):return a%p+p*(b%p)+p*p*(c%p)
def times(x,y):
    a,b,c=dec(x);d,e,f=dec(y)
    z0,z1,z2,z3,z4=a*d,a*e+b*d,a*f+b*e+c*d,b*f+c*e,c*f
    return enc(z0+6*z3,z1+6*z3+6*z4,z2+6*z4)
M=[[times(i,j) for j in range(q)] for i in range(q)]
A=[[enc(*( (u+v)%p for u,v in zip(dec(i),dec(j)))) for j in range(q)] for i in range(q)]
neg=[enc(*((-v)%p for v in dec(i))) for i in range(q)]
inv=[0]+[next(j for j in range(1,q) if M[i][j]==1) for i in range(1,q)]
def add(x,y):return A[x][y]
def sub(x,y):return A[x][neg[y]]
def mul(x,y):return M[x][y]
def power(x,e):
    t=1
    while e:
        if e&1:t=mul(t,x)
        x=mul(x,x);e>>=1
    return t

# Every affine point is tested against the homogeneous degree-eight equation.
pts=[]
for x in range(q):
    x7=power(x,7)
    for y in range(q):
        d=sub(mul(y,y),mul(2,x))
        if add(sub(power(y,8),add(x7,x)),power(d,4))==0:
            pts.append((x,y,1))
pts.append((1,0,0))
assert len(pts)==365,len(pts)

def normalize(line):
    k=next(x for x in line if x)
    return tuple(mul(x,inv[k]) for x in line)

def points_on_line(ell):
    a,b,c=ell
    return sum(1 for x,y,z in pts if add(add(mul(a,x),mul(b,y)),mul(c,z))==0)

lines=[(1,b,c) for b in range(q) for c in range(q)]
lines += [(0,1,c) for c in range(q)]
lines += [(0,0,1)]
assert len(lines)==q*q+q+1
spectrum=Counter();maxlines=[];examples={}
for ell in lines:
    r=points_on_line(ell)
    spectrum[r]+=1
    examples.setdefault(r,ell)
    assert r<=8
    if r==8:maxlines.append(ell)
assert dict(spectrum)=={0:48048,1:20000,2:46032,3:3528,4:21,5:28,8:336},spectrum

hits=Counter()
for a,b,c in maxlines:
    if b:
        for x in range(q):
            y=mul(neg[add(mul(a,x),c)],inv[b]);hits[x*q+y]+=1
        hits[q*q+mul(neg[a],inv[b])]+=1
    elif a:
        x=mul(neg[c],inv[a]);
        for y in range(q):hits[x*q+y]+=1
        hits[q*q+q]+=1
    else:
        for y in range(q+1):hits[q*q+y]+=1
hist=Counter(hits.values())
hist[0]=len(lines)-len(hits)
assert dict(hist)=={0:51633,1:19152,2:46872,8:336},hist
# Infinity on the curve is [1:0:0], so its incidence index is q^2.
curve_hist=Counter(hits[x*q+y] if z else hits[q*q] for x,y,z in pts)
assert dict(curve_hist)=={0:29,8:336},curve_hist
ground=[(x,y,z) for x,y,z in pts if x<p and y<p and z<p]
assert len(ground)==29
assert all(hits[x*q+y] == 0 if z else hits[q*q] == 0 for x,y,z in ground)
assert sum(k*v for k,v in spectrum.items())==365*344
assert sum(k*(k-1)//2*v for k,v in spectrum.items())==365*364//2
assert sum(k*v for k,v in hist.items())==336*344
assert sum(k*(k-1)//2*v for k,v in hist.items())==336*335//2
print('GF(343), irreducible v^3+v+1')
print('equation points',len(pts),'projective lines',len(lines))
print('line spectrum',sorted(spectrum.items()))
print('maximal secant incidence',sorted(hist.items()))
print('curve point incidence',sorted(curve_hist.items()))
print('uncovered exterior points',hist[0]-curve_hist[0])
print('sample lines',sorted(examples.items()))
print('DIRECT_VERIFY_OK')
