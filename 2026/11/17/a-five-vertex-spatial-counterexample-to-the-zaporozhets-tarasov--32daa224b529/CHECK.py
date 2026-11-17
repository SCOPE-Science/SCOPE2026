"""Exact, standalone certificate for the five-vertex mean-distance reversal."""
from fractions import Fraction as Q

L = Q(1000)
e = Q(1, 100)
P = [(Q(0),Q(0),e), (Q(0),Q(0),-e),
     (L,-Q(1),e/3), (L,Q(1),e/3), (L,Q(0),-e/3)]
faces = [(0,1,2),(0,1,3),(0,2,3),(1,2,4),(1,3,4),(2,3,4)]

def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def norm2(a):return dot(a,a)

# Every displayed triangle has all remaining vertices strictly to one side.
# A 3-polytope with five vertices has at most 2*5-4=6 facets.
for face in faces:
    a,b,c = (P[i] for i in face)
    n = cross(sub(b,a), sub(c,a))
    signs = [dot(n,sub(P[j],a)) for j in range(5) if j not in face]
    assert all(x>0 for x in signs) or all(x<0 for x in signs), (face,signs)
    assert all(x!=0 for x in signs)
assert len(faces)==6

# Exact squared doubled areas of all six facets.
areas4 = [norm2(cross(sub(P[b],P[a]),sub(P[c],P[a]))) for a,b,c in faces]
assert areas4[0] == 4*e*e*(L*L+1)
assert areas4[1] == areas4[0]
assert areas4[2] == 4*(L*L+4*e*e/9)
assert areas4[3] == L*L*(1+4*e*e/9)+4*e*e/9
assert areas4[4] == areas4[3]
assert areas4[5] == 16*e*e/9

# Volume slices: 4e*t - (10e/3)*t^2, integral 8e/9.
# The axial interior CDF is 9t^2/4-5t^3/4.
assert (4*e/Q(2) - (10*e/3)/3) == 8*e/9
assert (Q(9,4)-Q(5,4)) == 1
# Gini = 2 int_0^1 F(t)(1-F(t))dt.
# F coefficients in degree-indexed dictionary; exact polynomial integration.
def prod(a,b):
    ans={}
    for i,x in a.items():
        for j,y in b.items():ans[i+j]=ans.get(i+j,Q(0))+x*y
    return ans
def gint(F):
    sq=prod(F,F)
    return 2*(sum(v/Q(k+1) for k,v in F.items()) - sum(v/Q(k+1) for k,v in sq.items()))
gI = gint({2:Q(9,4),3:-Q(5,4)})
assert gI==Q(39,140)

# Elementary rational root isolations: all three displayed roots lie in (L,L+1).
for rad in [L*L+1,L*L+4*e*e/9,L*L*(1+4*e*e/9)+4*e*e/9]:
    assert L*L<rad<(L+1)*(L+1)

# Let A0=2e sqrt(L^2+1), A1=sqrt(L^2+4e^2/9)
#       +sqrt(L^2(1+4e^2/9)+4e^2/9), A2=2e/3.
# Their bounds imply alpha=2 A0/S and beta=(A1-A0)/S satisfy:
a0lo,a0hi=Q(20),Q(1001,50)
a1lo,a1hi=Q(2000),Q(2002)
a2=Q(1,150)
Slo,Shi=a0lo+a1lo+a2,a0hi+a1hi+a2
alow,ahigh=2*a0lo/Shi,2*a0hi/Slo
blow,bhigh=(a1lo-a0hi)/Shi,(a1hi-a0lo)/Slo
assert Q(19,1000)<alow<ahigh<Q(21,1000)
assert Q(979,1000)<blow<bhigh<Q(982,1000)

def g(a,b):
    return a+Q(2,3)*b-Q(2,3)*a*a-a*b-Q(2,5)*b*b

a,b=Q(19,1000),Q(979,1000)
# The partial derivatives are strictly negative throughout the parameter box.
assert 1-Q(4,3)*a-b<0
assert Q(2,3)-a-Q(4,5)*b<0
assert gint({1:a,2:b})==g(a,b)==Q(1347243,5000000)
# Transverse diameter bound: 2 sqrt(1+e^2)<2.001.
assert (2*Q(1)+Q(1,1000))**2>4*(1+e*e)
# Projection lemma: Delta >= L*gI and theta <= L*gB+D.
exact_margin = gI-g(a,b)-Q(2001,1000000)
assert exact_margin==Q(15579,2187500)>0
print('PASS: six supporting facets, exact cross products, exact interior Gini,')
print('rational surface CDF bounds, and certified strict mean-distance reversal.')
print('Certified Delta(K)-theta(K) >', L*exact_margin)
