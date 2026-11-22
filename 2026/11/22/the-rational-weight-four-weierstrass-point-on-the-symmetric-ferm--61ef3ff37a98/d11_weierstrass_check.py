"""Exact rational Taylor certificate for the distinguished point of F_11/S_3.

Independent polynomial arithmetic with fractions, no nonstandard packages.
The precision 14 suffices to read the five pivot orders 1,3,5,11,13.
"""
from fractions import Fraction as Q

N = 14

def const(c):
    a = [Q(0) for _ in range(N)]
    a[0] = Q(c)
    return a

def power_t(j, c=1):
    a = const(0)
    if j < N:
        a[j] = Q(c)
    return a

def plus(a, b):
    return [x+y for x,y in zip(a,b)]

def minus(a, b):
    return [x-y for x,y in zip(a,b)]

def mul(a,b):
    out = const(0)
    for i,x in enumerate(a):
        if not x: continue
        for j,y in enumerate(b[:N-i]):
            if y: out[i+j] += x*y
    return out

def powpoly(a,k):
    r = const(1)
    for _ in range(k): r=mul(r,a)
    return r

def ord_lead(a):
    for j,c in enumerate(a):
        if c:
            return j,c
    return None

def determinant(square_rows):
    rows = [list(r) for r in square_rows]
    n = len(rows)
    out = Q(1)
    for col in range(n):
        pivot = next((i for i in range(col, n) if rows[i][col]), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            rows[col], rows[pivot] = rows[pivot], rows[col]
            out = -out
        scale = rows[col][col]
        out *= scale
        for i in range(col+1,n):
            factor = rows[i][col] / scale
            rows[i] = [u-factor*v for u,v in zip(rows[i],rows[col])]
    return out

def matrix_rank(rows):
    rows=[list(r) for r in rows]
    if not rows:return 0
    n=len(rows[0]);pivot=0
    for col in range(n):
        pos=next((r for r in range(pivot,len(rows)) if rows[r][col]),None)
        if pos is None:continue
        rows[pivot],rows[pos]=rows[pos],rows[pivot]
        v=rows[pivot][col]
        rows[pivot]=[x/v for x in rows[pivot]]
        for r in range(len(rows)):
            if r!=pivot and rows[r][col]:
                z=rows[r][col]
                rows[r]=[u-z*w for u,w in zip(rows[r],rows[pivot])]
        pivot+=1
        if pivot==len(rows):break
    return pivot

# On X=1, F_11 has local coordinates t=Z, y=Y with
# y(0)=-1, y^11+1+t^11=0. Truncated Hensel solution:
t=power_t(1)
y=minus(const(-1),power_t(11,Q(1,11)))
assert plus(plus(powpoly(y,11),const(1)),power_t(11))==const(0)
e1=plus(plus(const(1),y),t)
e2=plus(mul(y,plus(const(1),t)),t)
e3=mul(y,t)
K=minus(mul(e1,e2),e3)
assert ord_lead(K)==(11,Q(1,11))

# Five independent invariant canonical sections, after common unit
# Delta/f_y is removed. These are homogeneous symmetric degree-five forms.
sections=[mul(e2,e3),mul(powpoly(e1,3),e2),powpoly(e1,5),mul(e2,K),mul(powpoly(e1,2),K)]
orders=[ord_lead(v) for v in sections]
assert orders==[(1,Q(1)),(3,Q(-1)),(5,Q(1)),(11,Q(-1,11)),(13,Q(1,11))],orders
# These sections span all five dimensions by their distinct orders.
# Degree-two tame ramification converts upstairs 1,3,5,11,13 to
# downstairs differential vanishing orders 0,1,2,5,6.
assert [(r-1)//2 for r,c in orders]==[0,1,2,5,6]
assert [((r-1)//2)+1 for r,c in orders]==[1,2,3,6,7]

# Cross-check: entire standard degree-five symmetric monomial basis.
basis=[powpoly(e1,5),mul(powpoly(e1,3),e2),mul(e1,powpoly(e2,2)),mul(powpoly(e1,2),e3),mul(e2,e3)]
jet_rows=[[col[j] for col in basis] for j in range(N)]
rank_progress=[matrix_rank(jet_rows[:j+1]) for j in range(N)]
assert [j for j in range(N) if rank_progress[j]-(rank_progress[j-1] if j else 0)]==[1,3,5,11,13]
assert rank_progress[-1]==5
assert determinant([jet_rows[j] for j in [1,3,5,11,13]]) == Q(1,121)
# The Weierstrass semigroup has exactly these five gaps below 8.
generated={4*a+5*b+11*c for a in range(8) for b in range(8) for c in range(8)}
assert [i for i in range(1,20) if i not in generated]==[1,2,3,6,7]
assert sum(g-(j+1) for j,g in enumerate([1,2,3,6,7]))==4
print('PASS: five upstairs orders 1,3,5,11,13; gap sequence 1,2,3,6,7; weight 4.')
print('Exact leading coefficients:',[(j,str(c)) for j,c in orders])
print('Complete jet ranks 0..13:',rank_progress)
print('Exact pivot-jet determinant:',str(determinant([jet_rows[j] for j in [1,3,5,11,13]])))
