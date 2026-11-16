"""Independent integer-arithmetic closed formula vs 3-term sums."""
from itertools import combinations_with_replacement
from collections import defaultdict
B=8192

def pow2_ge2(x):
    return int(x>=2 and x&(x-1)==0)

def two(n):
    if n<=0:return 0
    h=n//(n & -n)
    pos=int(n.bit_count()==2 or (n>=2 and n.bit_count()==1))
    neg=int((h+1)&h==0) # h = 2**d-1
    return pos+neg

def formula(d):
    if d<0:return formula(-d)
    if d==0:raise ValueError('zero has infinitely many noncancelling representations')
    v=(d & -d).bit_length()-1
    m=d>>v
    p=pow2_ge2(m-1)+pow2_ge2(m+1)
    return two((m-1)//2)+two((m+1)//2)+p+int(m==3)+(v>=1)*(p+int(m==1))+(v>=2)*int(m==1)
# Independently enumerate solutions for each D from generators bounded via largest term <=4D.
S=[0]+[z for j in range((4*B).bit_length()) for z in (-2**j,2**j)]
c=defaultdict(int)
for t in combinations_with_replacement(S,3):
    if any(t[i]==-t[j] for i in range(3) for j in range(i+1,3)):continue
    d=sum(t)
    if 0<d<=B:c[d]+=1
for d in range(1,B+1):
    if c[d]!=formula(d):raise AssertionError((d,c[d],formula(d)))
print('PASS formula / independent exhaustive sums', B, 'max',max(c.values()))
for d in (1,2,3,4,5,6,7,8,9,10,12,24,48):print(d, formula(d))
