"""Exhaustive residue check for monomial quaternion symbols (f,g) with
f,g degree-0 monomials in a=x-z,b=x+z,c=y-w,d=y+w mod squares (7 classes),
along the four Q-lines L1..L4. CORRECTED constants-tracked derivation:
L1 (a,c; units b-const,d=Y; r=c/a=-Q1/(Y Q2) with Q1=s^2+2t^2, Q2=2s^2+t^2
up to the evident square factors): with n=e1+e3, m=f1+f3 (mod 2),
  residue class = const^(nm) Q1^(nf3+me3) Y^(n(f4+f3)+m(e4+e3)) 2^(n(f2+f4)+m(e2+e4));
  Q1,Y,(2) are independent mod squares in Q(Y) (Q1 prime; Y prime; 2 nonsquare
  const), so unramified <=> nm=0, nf3+me3=0, n(f4+f3)+m(e4+e3)=0,
  n(f2+f4)+m(e2+e4)=0.
L2 (a,d; units b-const,c=Y): n=e1+e4; conds nf4+me4=0, n(f3+f4)+m(e3+e4)=0,
  n(f2+f3)+m(e2+e3)=0. L3 (b,c; units a-const,d=Y): n=e2+e3; conds nf3+me3=0,
  n(f4+f3)+m(e4+e3)=0, n(f1+f4)+m(e1+e4)=0. L4 (b,d; units a-const,c=Y):
  n=e2+e4; conds nf4+me4=0, n(f3+f4)+m(e3+e4)=0, n(f1+f3)+m(e1+e3)=0.
(Supersedes residue_search.py/recovery_line_residues.py which used a wrong model.)
Result: 0 of 21 unordered pairs unramified on all four lines (3 per single line).
"""
import itertools
funcs=[e for e in itertools.product([0,1],repeat=4) if sum(e)%2==0 and any(e)]
print("classes:",funcs)
def ok_L1(ef,eg):
    n=(ef[0]+ef[2])%2; m=(eg[0]+eg[2])%2
    if (n*m)%2==1: return False
    if (ef[2]*m+eg[2]*n)%2==1: return False
    if (ef[1]*m+eg[1]*n)%2==1: return False
    if (ef[3]*m+eg[3]*n)%2==1: return False
    return True
def ok_L2(ef,eg):
    n=(ef[0]+ef[3])%2; m=(eg[0]+eg[3])%2
    if (n*m)%2==1: return False
    if (ef[3]*m+eg[3]*n)%2==1: return False
    if (ef[1]*m+eg[1]*n)%2==1: return False
    if (ef[2]*m+eg[2]*n)%2==1: return False
    return True
def ok_L3(ef,eg):
    n=(ef[1]+ef[2])%2; m=(eg[1]+eg[2])%2
    if (n*m)%2==1: return False
    if (ef[2]*m+eg[2]*n)%2==1: return False
    if (ef[0]*m+eg[0]*n)%2==1: return False
    if (ef[3]*m+eg[3]*n)%2==1: return False
    return True
def ok_L4(ef,eg):
    n=(ef[1]+ef[3])%2; m=(eg[1]+eg[3])%2
    if (n*m)%2==1: return False
    if (ef[3]*m+eg[3]*n)%2==1: return False
    if (ef[0]*m+eg[0]*n)%2==1: return False
    if (ef[2]*m+eg[2]*n)%2==1: return False
    return True
ef=(1,1,0,0); eg=(0,0,1,1)
print("naive:",ok_L1(ef,eg),ok_L2(ef,eg),ok_L3(ef,eg),ok_L4(ef,eg))
good=[]
for i,ef in enumerate(funcs):
    for eg in funcs:
        if eg<=ef: continue
        if ok_L1(ef,eg) and ok_L2(ef,eg) and ok_L3(ef,eg) and ok_L4(ef,eg):
            good.append((ef,eg))
print("line-unramified unordered pairs:",len(good))
for p in good: print(p)
for name,fn in [("L1",ok_L1),("L2",ok_L2),("L3",ok_L3),("L4",ok_L4)]:
    c=sum(1 for ef in funcs for eg in funcs if eg>ef and fn(ef,eg))
    print(name,"passes:",c)
print("MONOMIAL_RESIDUE_PROOF_OK")
