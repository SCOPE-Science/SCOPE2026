"""Symbolic all-order moment identities for a two-temperature energy-exchange star."""
import sympy as S
m,r,T,d=S.symbols('m r T d',positive=True)
N=2*m
a=2*r/(1+2*r)
D=(1+2*r)**2*(N+2*r+1)
means={0:T,1:T+a*d,-1:T-a*d}
def M(s): return means[s]
def leaf2(s):
    var=T**2+2*T*s*a*d+(4*r/(1+2*r)-a*a+2/D)*d*d
    return S.expand(M(s)**2+var)
H2=2*T*T+(2*r/(1+2*r)+2*(r+1)/D)*d*d
def hleaf(s):return T*M(s)+d*d/((1+2*r)*(N+2*r+1))
def lp(s,t):return M(s)*M(t)+d*d/D
def check(label,expr):
    z=S.factor(expr)
    assert z==0,(label,z)
    print('SYMBOLIC_IDENTITY_PASSED',label)
check('hub_mean', m*((M(1)-M(0))/2+(M(-1)-M(0))/2))
for s in (1,-1):
    check('leaf_mean_'+str(s), (M(0)-M(s))/2+r*(T+s*d-M(s)))
check('hub_second',m*((leaf2(1)+2*hleaf(1)-2*H2)/3+(leaf2(-1)+2*hleaf(-1)-2*H2)/3))
for s in (1,-1):
    check('leaf_second_'+str(s),(H2+2*hleaf(s)-2*leaf2(s))/3+r*(2*(T+s*d)**2-leaf2(s)))
    other=-s
    sum_pairs=(m-1)*lp(s,s)+m*lp(s,other)
    check('hub_leaf_'+str(s),(H2+leaf2(s)+2*hleaf(s))/6-hleaf(s)+((sum_pairs)-(N-1)*hleaf(s))/2+r*((T+s*d)*T-hleaf(s)))
for s,t in [(1,1),(1,-1),(-1,-1)]:
    check('leaf_leaf_'+str(s)+'_'+str(t),(hleaf(s)+hleaf(t))/2 -(1+2*r)*lp(s,t)+r*((T+s*d)*M(t)+(T+t*d)*M(s)))
print('STAR_KMP_SYMBOLIC_ALL_SIZES_PASSED')
