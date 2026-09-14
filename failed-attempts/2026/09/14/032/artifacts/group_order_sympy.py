import sys
sys.path.insert(0, '.')
from sympy.combinatorics import Permutation
from sympy.combinatorics.perm_groups import PermutationGroup
u0=[1,2,3,0,5,6,4,8,7,10,9,11]
u1=[2,10,11,5,8,3,4,7,6,9,0,1]
n=12
def inv(p):
    q=[0]*n
    for i,v in enumerate(p): q[v]=i
    return q
def compose(a,b): return [a[b[i]] for i in range(n)]
uinf=inv(compose(u0,u1))
s0=Permutation(u0); s1=Permutation(u1); si=Permutation(uinf)
G=PermutationGroup(s0,s1)
print("order:",G.order())
print("is_transitive:",G.is_transitive())
print("is_primitive:",G.is_primitive())
print("is_symmetric:",G.is_symmetric)
print("is_alternating:",G.is_alternating)
