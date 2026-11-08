"""Exact rational checks for relaxed alternating projections on two principal lines."""
from fractions import Fraction as Q
from math import isqrt

def mat_mul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def trans(a): return [[a[j][i] for j in range(2)] for i in range(2)]

def det(a): return a[0][0]*a[1][1]-a[0][1]*a[1][0]

def block(c, s, omega):
    return [[1-omega*s*s, Q(0)], [omega*c*s, 1-omega]]

def gram_defect(b):
    g=mat_mul(trans(b),b)
    return [[int(i==j)-g[i][j] for j in range(2)] for i in range(2)]

def is_psd(m):
    return m[0][0]>=0 and m[1][1]>=0 and det(m)>=0

def check(c,s):
    assert c*c+s*s==1 and c>0 and s>0
    w_safe=(2+c)/(1+c)
    w_asym=2/(2-c*c)
    count=0
    for k in range(-10,41):
        for denom in [5,7,11,17]:
            w=Q(k,denom)
            b=block(c,s,w)
            g=gram_defect(b)
            assert g[0][0]==w*s*s*(2-w)
            assert g[0][1]==-w*c*s*(1-w)
            assert g[1][1]==w*(2-w)
            assert det(g)==w*w*s*s*((2-w)**2-c*c*(1-w)**2)
            assert is_psd(g)==(Q(0)<=w<=w_safe)
            assert b[0][0]**2+b[1][0]**2==c*c+s*s*(w-1)**2
            count+=1
    for w in [w_safe,w_asym,Q(1),Q(0),Q(2),w_safe+Q(1,1000),w_safe-Q(1,1000)]:
        assert is_psd(gram_defect(block(c,s,w)))==(Q(0)<=w<=w_safe)
        count+=1
    assert (w_asym>w_safe)==(c**3+2*c*c-2>0)
    return count

n=0
for i,j,k in [(3,4,5),(5,12,13),(8,15,17),(7,24,25),(20,21,29),(9,40,41),(11,60,61),(16,63,65),(33,56,65),(28,45,53),(48,55,73),(65,72,97)]:
    for a,b in [(Q(i,k),Q(j,k)),(Q(j,k),Q(i,k))]:
        n+=check(a,b)
print(f'PASS: {n} exact rational checks across 24 principal-angle instances.')
