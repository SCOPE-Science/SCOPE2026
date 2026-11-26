"""Exact arithmetic checks for the characteristic-five Barth sextic.

No external Python modules are required. This script enumerates all points of
P^3(F5) and P^3(F25) in canonical projective charts. It also checks the six
singular-point orbit representatives and their nondegenerate local Hessians.
"""
from collections import Counter
from itertools import product

P=5
VARS=4

def add_poly(f,g):
    h=f.copy()
    for e,c in g.items():
        v=(h.get(e,0)+c)%P
        if v:h[e]=v
        else:h.pop(e,None)
    return h

def scale_poly(f,c):
    return {e:(v*c)%P for e,v in f.items() if (v*c)%P}

def mul_poly(f,g):
    h={}
    for e,c in f.items():
        for t,d in g.items():
            key=tuple(a+b for a,b in zip(e,t))
            h[key]=(h.get(key,0)+c*d)%P
    return {e:c for e,c in h.items() if c}

def diff(f,j):
    h={}
    for e,c in f.items():
        if e[j]:
            t=list(e);t[j]-=1
            d=c*e[j]%P
            if d:h[tuple(t)]=d
    return h

def eval5(f,point):
    return sum(c*__import__('math').prod(pow(v,n,P) for v,n in zip(point,e)) for e,c in f.items())%P

zero=(0,0,0,0)
var=[{tuple(int(i==j) for i in range(VARS)):1} for j in range(VARS)]
x,y,z,w=var
x2,y2,z2,w2=[mul_poly(t,t) for t in var]
S=add_poly(add_poly(x2,y2),z2)
K=add_poly(S,scale_poly(w2,-1))
F=add_poly(mul_poly(mul_poly(add_poly(x2,y2),add_poly(y2,z2)),add_poly(z2,x2)),scale_poly(mul_poly(mul_poly(K,K),w2),-2))
G=[diff(F,j) for j in range(4)]
H=[[diff(G[i],j) for j in range(4)] for i in range(4)]

def determinant3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
           -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
           +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))%5

reps={
    'infinity_axis':((1,0,0,0),0,4,3),
    'infinity_two_plus_one_minus':((1,1,2,0),0,4,12),
    'affine_one_plus':((1,0,0,1),3,1,6),
    'affine_two_plus_one_minus':((1,1,2,1),3,1,24),
    'affine_two_minus':((2,2,0,1),3,4,12),
    'affine_three_plus':((1,1,1,1),3,4,8),
}
for name,(p,chart,expected,count) in reps.items():
    assert eval5(F,p)==0 and all(eval5(g,p)==0 for g in G),name
    inds=[k for k in range(4) if k!=chart]
    localH=[[eval5(H[i][j],p) for j in inds] for i in inds]
    assert determinant3(localH)==expected, (name,localH)
print('node type sizes:',{k:v[3] for k,v in reps.items()})

# The disjoint charts below contain 5^3+5^2+5+1=156 points.
points=[]; nodes=[]
for chart in range(4):
    for trailing in product(range(5),repeat=3-chart):
        pt=(0,)*chart+(1,)+trailing
        if eval5(F,pt)==0:
            points.append(pt)
            if all(eval5(g,pt)==0 for g in G):nodes.append(pt)
assert len(points)==91 and len(nodes)==65
assert sum(v[3] for v in reps.values())==len(nodes)
assert Counter('infinity' if p[3]==0 else 'affine' for p in nodes)=={'affine':50,'infinity':15}
print('F5:',{'projective_points':156,'surface_points':len(points),'nodes':len(nodes),'smooth_points':len(points)-len(nodes)})

# Independent direct finite-field point counts in two degree-two extensions.
def field25(n):
    assert n in (2,3) # both are nonsquares mod 5
    q=25
    add=[[((a%5+b%5)%5)+5*((a//5+b//5)%5) for b in range(q)] for a in range(q)]
    neg=[(-a%5)+5*(-(a//5)%5) for a in range(q)]
    sub=[[add[a][neg[b]] for b in range(q)] for a in range(q)]
    mul=[[((a%5)*(b%5)+n*(a//5)*(b//5))%5+5*(((a%5)*(b//5)+(a//5)*(b%5))%5) for b in range(q)] for a in range(q)]
    sq=[mul[a][a] for a in range(q)]
    def on(x,y,z,w):
        a,b,c,d=sq[x],sq[y],sq[z],sq[w]
        p=mul[mul[add[a][b]][add[b][c]]][add[c][a]]
        k=sub[add[add[a][b]][c]][d]
        return p==mul[2][mul[mul[k][k]][d]]
    strata=Counter()
    for x,y,z in product(range(q),repeat=3):
        if on(x,y,z,1):strata['w=1']+=1
    for x,y in product(range(q),repeat=2):
        if on(x,y,1,0):strata['w=0,z=1']+=1
    for x in range(q):
        if on(x,1,0,0):strata['w=z=0,y=1']+=1
    if on(1,0,0,0):strata['axis']+=1
    assert dict(strata)=={'w=1':1510,'w=0,z=1':137,'w=z=0,y=1':3,'axis':1}
    assert sum(strata.values())==1651
    print('F25 with t^2=',n,':',dict(sorted(strata.items())),'total:',sum(strata.values()))
for n in (2,3):field25(n)

# This is a consistency check, not a substitute for the cohomological proof.
def formula(n):return 1+5**(2*n)+5**n*(27+14*(-1)**n)
assert [formula(n) for n in range(1,4)]==[91,1651,17251]
print('zeta point-count formula:',[formula(n) for n in (1,2,3)])
print('VERIFY_OK')
