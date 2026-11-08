#!/usr/bin/env python3
"""Exact, dependency-free verification of cyclic Radau IIA polynomial certificates.

This checks finite polynomial identities, coefficient signs, and exact rational
matrix entries. The all-dimension small-step and large-step arguments are
analytic and explained in RESULT.md; finite tests alone do not establish them.
"""
from fractions import Fraction as F
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
cert = json.loads((ROOT / 'certificate.json').read_text(encoding='utf-8'))
checks = 0

def require(cond, msg):
    global checks
    checks += 1
    if not cond: raise AssertionError(msg)

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def add(a,b):
    out=[F(0)]*max(len(a),len(b))
    for i,v in enumerate(a):out[i]+=v
    for i,v in enumerate(b):out[i]+=v
    return trim(out)

def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return trim(out)

def eval_poly(a,h):
    y=F(0)
    for x in reversed(a):y=y*h+x
    return y

# In powers of cyclic P, D=I-2h(P-I)/3+h^2(P-I)^2/6,
# U=I+h(P-I)/3, and R(h(P-I))=D^-1 U.
base_D={0:[F(1),F(2,3),F(1,6)],1:[F(0),-F(2,3),-F(1,3)],2:[F(0),F(0),F(1,6)]}
base_U={0:[F(1),-F(1,3)],1:[F(0),F(1,3)]}

def reduce_mod_n(poly_coeffs,n):
    ans=[[F(0)] for _ in range(n)]
    for j,coef in poly_coeffs.items():ans[j%n]=add(ans[j%n],coef)
    return ans

for n in range(2,7):
    dat=cert['records'][str(n)]
    d=[F(x) for x in dat['den']]
    nums=[[F(x) for x in p] for p in dat['nums']]
    require(len(nums)==n, f'wrong number of numerators: {n}')
    require(all(c>=0 for c in d) and d[0]>0,f'den positivity: {n}')
    DD=reduce_mod_n(base_D,n)
    UU=reduce_mod_n(base_U,n)
    for j in range(n):
        lhs=[F(0)]
        for k in range(n):lhs=add(lhs,mul(DD[k],nums[(j-k)%n]))
        rhs=mul(d,UU[j])
        require(trim(lhs)==trim(rhs),f'cyclic polynomial identity: n={n},j={j}')
        if n<=5:
            require(all(c>=0 for c in nums[j]) and any(c>0 for c in nums[j]), f'nonnegative coefficients n={n},j={j}')
    if n==6:
        for j in range(1,5):
            require(all(c>=0 for c in nums[j]) and any(c>0 for c in nums[j]),f'other cyclic entries: n=6,j={j}')
        require(nums[0]==[F(v) for v in [1296,3888,5400,4440,2280,664,26,-50,-5,5,1]],'diagonal sign certificate')
        require(nums[5]==[F(v) for v in [0,0,0,0,0,-12,36,90,60,15,1]],'six-cycle obstruction')
        # N0>0: on 0<h<=3, 5h^8+50h^7 <=585h^5<664h^5.
        require(F(5)*3**3+F(50)*3**2 < F(664),'diagonal small-h inequality')
        # For h>=3: h^10+5h^9-5h^8-50h^7
        # =h^7(h^3+5h^2-5h-50)>0, since cubic value at 3 is 7
        # and its derivative 3h^2+10h-5 is positive for h>=3.
        require(3**3+5*3**2-5*3-50>0 and 3*3**2+10*3-5>0,'diagonal large-h inequality')

# Recover the first negative off-diagonal coefficient from the scalar
# Radau IIA generating function R(z)=(1+z/3)/(1-2z/3+z^2/6).
a=[F(1)]
for k in range(1,7):
    v=F(1,3) if k==1 else F(0)
    v+=F(2,3)*a[k-1]
    if k>=2:v-=F(1,6)*a[k-2]
    a.append(v)
require(a[:6]==[F(1),F(1),F(1,2),F(1,6),F(1,36),-F(1,108)],'Taylor expansion')

# Solve the n=8 matrix exactly at three steps to demonstrate disconnected
# positive-step regions. A circulant's first column contains every entry.
def step_column(n,h):
    D=reduce_mod_n(base_D,n)
    U=reduce_mod_n(base_U,n)
    d=[eval_poly(v,h) for v in D]
    u=[eval_poly(v,h) for v in U]
    M=[[d[(i-j)%n] for j in range(n)]+[u[i]] for i in range(n)]
    for k in range(n):
        pivot=next((r for r in range(k,n) if M[r][k]!=0),None)
        require(pivot is not None,'nonsingular matrix')
        M[k],M[pivot]=M[pivot],M[k]
        v=M[k][k]
        M[k]=[q/v for q in M[k]]
        for i in range(n):
            if i==k:continue
            r=M[i][k]
            if r:M[i]=[M[i][j]-r*M[k][j] for j in range(n+1)]
    col=[M[i][n] for i in range(n)]
    for i in range(n):
        require(sum(d[(i-j)%n]*col[j] for j in range(n))==u[i],'rational solution residual')
    require(sum(col)==1,'mass conservation')
    return col

special={F(2):(7,F(11824,2058973)),F(4):(0,-F(5703833,339145563)),F(20):(0,F(127548251905668327,1666416340218976267))}
for h,(idx,expected) in special.items():
    col=step_column(8,h)
    require(min(col)==expected and col[idx]==expected,f'8-cycle exact minimum at h={h}')
    require((min(col)>0)==(h!=4),f'8-cycle sign at h={h}')

poly6=[-12,36,90,60,15,1]
lo=F(2086088,10000000)
hi=F(2086089,10000000)
require(eval_poly(poly6,lo)<0<eval_poly(poly6,hi),'six-cycle root isolating interval')
require(all(F(v)>0 for v in [36,180,180,60,5]),'six-cycle monotone derivative')

print(f'VERIFY_OK: {checks} exact assertions; cyclic n=2..6 coefficient identities; n=8 h=2,4,20 rational sign checks.')
print('Six-cycle unique positive recovery root lies in (0.2086088,0.2086089).')
print('Eight-cycle exact signed minima:',{str(h):str(v) for h,(_,v) in special.items()})
