#!/usr/bin/env python3
"""Independent capped-denumerant verification for adjacent odd intervals."""

def counts(gen, N, cap):
 out=[0]*(N+1);out[0]=1
 for g in gen:
  for v in range(g,N+1):
   out[v]=min(cap,out[v]+out[v-g])
 return out

def exceptional(a,p):
 if p==0:return {4*a+3}
 if p==1:return set(range(8*a,8*a+7,2))
 k=2*a-2*p+1
 return {2*(2*a+1)+2*s for s in (k,k+1) if a+1<=s<=2*a}

def run():
 checked=0; diffs=0; odd_end=0
 for a in range(4,151):
  b=2*a+1; N=20*a+100; cap=(a+1)//2+2
  minus=counts(range(b,4*a+2,2),N,cap)
  plus=counts(range(b,4*a+4,2),N,cap)
  for p in range((a+1)//2+1):
   actual={n for n in range(N+1) if minus[n]<=p<plus[n]}
   expected=exceptional(a,p)
   assert actual==expected,(a,p,actual,expected)
   checked+=1;diffs+=len(actual)
   if a%2 and p==(a+1)//2 and p>=2:assert len(actual)==1;odd_end+=1
 print('ODD_INTERVAL_THRESHOLD_EXCEPTIONS_OK','a=4..150','instances',checked,'total_differences',diffs,'odd_endpoint_cases',odd_end)
 for a in (4,5,11,30):
  for p in (0,1,2,(a+1)//2):
   print('SAMPLE',a,p,sorted(exceptional(a,p)))
if __name__=='__main__':run()
