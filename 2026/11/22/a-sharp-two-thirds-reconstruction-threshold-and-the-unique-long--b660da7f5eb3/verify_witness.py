"""Independent periodic-word constructive-witness verification."""
from collections import Counter

def spectrum(n,k,a,r):
    marks={a,a+r}
    return Counter(''.join('1' if i in marks else '0' for i in range(t,t+k)) for t in range(n-k+1))

cases=0
for n in range(5,121):
  for k in range(3,(2*n+1)//3+1):
    r=n-k+1
    lo=max(0,n-2*r)
    hi=min(r-1,n-r-1)
    assert hi-lo>=1,(n,k,r,lo,hi)
    witness=spectrum(n,k,lo,r)
    for a in range(lo,hi+1):
      assert 0<=a<a+r<n and a+2*r>=n,(n,k,a,r)
      assert spectrum(n,k,a,r)==witness,(n,k,a,r)
    cases+=1
print(f'PASS: {cases} complete periodic-witness families (n=5..120), every a in admissible interval')
for n in range(5,100):
    assert (2*n+1)//3+1 > (n+1)/2
print('PASS: threshold lies within near-half theorem regime for n=5..99')
