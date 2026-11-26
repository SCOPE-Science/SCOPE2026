from math import gcd

def seq(k,lim):
 a=[0,1]
 for n in range(2,lim+1):
  a.append(sum(a[max(0,n-2-(n%k)):n]))
 return a

def order(c,m):
 assert gcd(c,m)==1
 v=c % m; d=1
 while v!=1:
  v=v*c % m; d+=1
 return d

def theorem(k,M):
 temp=M;a=b=0
 while temp%2==0:a+=1;temp//=2
 while temp%3==0:b+=1;temp//=3
 m=temp
 if k==2:
  h=M//(3**b)
  T=2*order(3,h) if h>1 else 1
  N3=2*(b+1) if b else 0
  N=max((2 if h>1 else 0),N3)
 else:
  c=3*2**(k-2)
  T=k*order(c,m) if m>1 else 1
  N3=0 if b==0 else (k*b if k>=4 else 3*(b+1))
  if a==0:N2=0
  elif k==3:
   N2=3 if a==1 else 3*(a-1)+1
  elif a<=k-4:
   N2=a+2
  else:
   q=(a-(k-4)+(k-2)-1)//(k-2)
   r=a-1-(k-4)-(q-1)*(k-2)
   N2=k*q+r+1
  N=max(N2,N3,(2 if k>=4 else 3) if m>1 else 0)
 return N,T

def test():
 for k in range(2,17):
  for M in range(2,151):
   N,T=theorem(k,M)
   z=seq(k,N+5*T+5)
   if any((z[n]-z[n+T])%M for n in range(N,len(z)-T)):
    print('not period',k,M,N,T,next(n for n in range(N,len(z)-T) if (z[n]-z[n+T])%M));return
   if N>0 and all((z[n]-z[n+T])%M==0 for n in range(N-1,len(z)-T)):
    print('not minimal N',k,M,N,T);return
   # least T: all divisors
   for d in range(1,T):
    if T%d==0 and all((z[n]-z[n+d])%M==0 for n in range(N+3*T,N+4*T)):
     print('not minimal T',k,M,N,T,d);return
 print('ALL CHECKS PASSED', 15*149)
if __name__=='__main__':test()
