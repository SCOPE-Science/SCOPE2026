from functools import lru_cache
from fractions import Fraction
from math import factorial

def graph(n,cyclic=False):
 v=2*n
 ed=[(i,i+n) for i in range(n)]
 ed += [(i,i+1) for i in range(n-1)]
 if cyclic: ed.append((n-1,0))
 return v,ed

def greedy_expectation(n,cyclic=False):
 N,E=graph(n,cyclic)
 @lru_cache(None)
 def solve(mask):
  possible=[(a,b) for (a,b) in E if mask&(1<<a) and mask&(1<<b)]
  if not possible:return Fraction(0)
  return 1+sum((solve(mask^(1<<a)^(1<<b)) for (a,b) in possible),Fraction(0))/len(possible)
 ans=solve((1<<N)-1)
 return ans,solve.cache_info().currsize

def closed_f(n):
 f=[Fraction(0)]
 for i in range(1,n+1):f.append(1+Fraction(4*sum(f[:i-1])+2*f[i-1],2*i-1))
 return f
f=closed_f(20)
for n in range(1,10):
 e,num=greedy_expectation(n)
 assert e==f[n]
 print('comb',n,str(e),'states',num)
for n in range(3,11):
 e,num=greedy_expectation(n,True)
 wanted=1+(f[n-1]+f[n-2])/2
 assert e==wanted,(n,e,wanted)
 print('sunlet',n,str(e),'states',num)
print('PASS independent rational dynamic recursion for 19 graphs')
