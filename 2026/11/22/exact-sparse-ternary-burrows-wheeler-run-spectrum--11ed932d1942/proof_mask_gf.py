import sympy as sp
from itertools import product
z,u=sp.symbols('z u');D=(1-z)*(1-z**2)*(1-z**3)
# bits A=1 B=2 C=4

def chains(prev=0):
 yield ()
 for nxt in range(1,8):
  if nxt!=prev and nxt & prev==prev:
   for rest in chains(nxt):
    yield (nxt,)+rest

def run_count(t):return 1+sum(x!=y for x,y in zip(t,t[1:]))

def emit(m,prev,b_gt_c):
 order=(4,1,2) if b_gt_c else (4,2,1)
 return ''.join(('1' if i==1 else '2') if i & prev ==0 else '0' for i in order if i&m)

def final(m,b_gt_c):
 # start at 1, then first2 then second2 if b>c, else reverse
 order=(4,1,2) if b_gt_c else (4,2,1) # The first marker-starting row starts with 1; the remaining two start with 2.
 return ''.join(('0' if i&m else ('2' if i in (4,2) else '1')) for i in order)

# The ordered marker-starting rows are C,A,B if b>c and C,B,A otherwise.

F={r:0 for r in range(2,8)}
ch=list(chains())
for chain in ch:
 b_gt_c=any(m&2 and not m&4 for m in chain)
 if not chain:
  t=final(0,False);F[run_count(t)]+=z**3;continue
 for states in product((0,1),repeat=len(chain)):
  out='';prev=0;weight=z**3
  for m,rep in zip(chain,states):
   k=m.bit_count();out+=emit(m,prev,b_gt_c)
   if rep:
    out+='0';weight*=z**(2*k)/(1-z**k)
   else:weight*=z**k
   prev=m
  out+=final(prev,b_gt_c)
  r=run_count(out)
  F[r]+=weight
print('chains',len(ch),'terms',sum(2**len(c) for c in ch))
for r,f in F.items():
 if f==0:continue
 poly=sp.cancel(f*D).expand()
 print('r',r,'num=',sp.factor(poly),'degree',sp.Poly(poly,z).degree(),'denominator?',sp.denom(poly))

expected={
 2:z**3*D,
 3:z**4*(1-z)**2*(2*z**3+3*z**2+4*z+2),
 4:z**4*(1-z)*(3*z**2+2*z+1),
 5:z**5*(1-z)*(2*z**3+3*z**2+4*z+2),
 6:z**6*(z**3+z**2+3*z+1),
}
for r in range(2,8):
 assert sp.cancel(F[r]*D-expected.get(r,0))==0, r
assert sp.cancel(sum(F.values())-z**3/(1-z)**3)==0
print('Exact symbolic denominator and all five numerator identities verified.')
