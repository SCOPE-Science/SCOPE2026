from itertools import permutations
from fractions import Fraction
import sympy as s
from itertools import combinations

def partitions(vals):
    if not vals:
        yield ()
        return
    a=vals[0]
    for b in vals[1:]:
        rest=[v for v in vals if v not in (a,b)]
        for tail in partitions(rest):
            yield ((a,b),)+tail
PARTS=tuple(partitions(tuple(range(6))))
assert len(PARTS)==15

def det3(A):
    (a,b,c),(d,e,f),(g,h,i)=A
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def coeff_pair(a,b): return (1,-(a+b),a*b)

def determinants(roots):
    return tuple(det3([coeff_pair(roots[a],roots[b]) for a,b in p]) for p in PARTS)

def h(roots):
    ans=1
    for x in determinants(roots):ans*=x
    return ans
special=(-3,-2,-1,1,2,3)
other=(0,1,2,3,4,7)
D1=determinants(special)
D2=determinants(other)
print('partitions',len(PARTS),'zero special',sum(d==0 for d in D1),'zero other',sum(d==0 for d in D2),'H(other)',h(other))
print('special partitions',[p for p,d in zip(PARTS,D1) if d==0])
print('first few determinants',D2[:5]);
# all permutations: H is symmetric in root ordering
for roots in [special,other]:
 h0=h(roots)
 for p in permutations(roots):
    assert h(p)==h0
print('all 720 root permutation symmetries verified on 2 samples')
# exact check of the Möbius stabilizer of a six-point divisor
# test Mobius automorphisms of explicit special sextic
S=list(special)
auto=[]
for dst in permutations(S,3):
 M=s.Matrix([[x,1,-y*x,-y] for x,y in zip(S[:3],dst)])
 ns=M.nullspace()
 if len(ns)!=1:continue
 a,b,c,d=ns[0]
 if a*d-b*c==0:continue
 mapped=[]
 for x in S:
  if c*x+d==0: break
  mapped.append(s.cancel((a*x+b)/(c*x+d)))
 else:
  if set(mapped)==set(S):auto.append(tuple(mapped))
assert len(auto)==2
print('Mobius stabilizer special sextic',auto)
# explicit elliptic fibration with six I2 fibers
x,t=s.symbols('x t')
r1=5*(t*t-1);r2=-8*(t*t-4);r3=3*(t*t-9)
assert s.expand(r1+r2+r3)==0
Q1=(2*r1+r2)/3; Q2=(r2-r1)/3;Q3=-(r1+2*r2)/3
assert s.expand(Q1+Q2+Q3)==0
assert s.expand(Q1-Q2-r1)==s.expand(Q2-Q3-r2)==s.expand(Q3-Q1-r3)==0
f=s.expand((x-Q1)*(x-Q2)*(x-Q3))
A=s.expand(Q1*Q2+Q2*Q3+Q3*Q1);B=s.expand(-Q1*Q2*Q3)
assert s.expand(f-(x**3+A*x+B))==0
D=s.factor(4*A**3+27*B**2)
assert s.expand(D+14400*((t*t-1)*(t*t-4)*(t*t-9))**2)==0
for u in special:
 assert A.subs(t,u)!=0 and B.subs(t,u)!=0
print('example Weierstrass discriminant:',D)

# Nonalternation and simple vanishing of the determinant product.
assert h((0,0,1,2,3,4)) != 0
zero_partition = [i for i,d in enumerate(D1) if d == 0]
assert len(zero_partition) == 1
changed = list(special);changed[0] += 1
assert determinants(changed)[zero_partition[0]] != 0
assert h(tuple(z+3 for z in other)) == h(other)
assert h(tuple(2*z for z in other)) == 2**45*h(other)
print('VERIFY_OK')
