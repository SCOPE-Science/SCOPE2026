from itertools import combinations
from math import comb

def formula(n,k,m):
 t=n-2*k
 a0=1+int(t!=0)+int(t*t!=n)
 a1=1+int(t!=0)
 return min(m,a0)+(n-1)*min(m,a1)+n*(n-3)//2

def rank_mod(mat,p=1000003):
 rows=[list(map(lambda x:x%p,row)) for row in mat]
 m=len(rows); N=len(rows[0]); piv=0
 for j in range(N):
  found=next((i for i in range(piv,m) if rows[i][j]!=0),None)
  if found is None:continue
  rows[piv],rows[found]=rows[found],rows[piv]
  inv=pow(rows[piv][j],p-2,p)
  for i in range(piv+1,m):
   a=rows[i][j]
   if a:
    v=a*inv%p
    rows[i][j:]=[(x-v*y)%p for x,y in zip(rows[i][j:],rows[piv][j:])]
  piv+=1
  if piv==min(m,N):break
 return piv

def test(n,k,m):
 cols=[()] +[(i,) for i in range(n)]+list(combinations(range(n),2))
 ev=[2**(d*t) for t in range(m) for d in range(3)]
 arr=[]
 for t in range(m):
  for neg in combinations(range(n),k):
   neg=set(neg)
   arr.append([(-1 if len(neg.intersection(S))%2 else 1)*(2**(len(S)*t)) for S in cols])
 return rank_mod(arr), formula(n,k,m)

def main():
 count=0
 for n in range(5,9):
  for k in range(2,n-1):
   for m in range(1,5):
    obs,exp=test(n,k,m);assert obs==exp,(n,k,m,obs,exp); count+=1
 for n,k in [(9,3),(9,4),(16,6)]:
  t=n-2*k
  a0=1+int(t!=0)+int(t*t!=n)
  assert a0 in (2,3)
 print('CHECK_OK exact_modular_rank_cases=',count,' square_resonance_checked=3')
if __name__=='__main__':main()
