from itertools import product, permutations
from math import factorial,comb
from collections import Counter

def formula(n,q):
 out=Counter()
 for a in range(n+1):
  for b in range(n-a+1):
   for c in range(n-a-b+1):
    d=n-a-b-c; r=a+b; s=a+c
    if r==0 or s==0:continue
    mult=factorial(n)//(factorial(a)*factorial(b)*factorial(c)*factorial(d))
    for t in range(min(b,c)+1):
     u=a+t
     if not u:continue
     fall=factorial(b)//factorial(b-t)
     x=mult*comb(c,t)*fall*(a+t)**(b-t)*r**(c-t)*(r*s)**d*q**(b+c+2*d-t)
     out[r,s,u]+=x
 return out

def base(n):
 funs=list(product(range(n),repeat=n))
 idem=[f for f in funs if all(f[f[i]]==f[i] for i in range(n))]
 out=Counter(); cumul=Counter()
 for f in idem:
  R=set(f)
  for h in idem:
   S=set(h)
   p=tuple(h[f[i]] for i in range(n))
   if all(p[p[i]]==p[i] for i in range(n)):
    u=len(set(p)); t=len(set(p)-R)
    out[len(R),len(S),u,t]+=1
    cumul[len(R),len(S),u,t]+=1
 return idem,out

def group_perms(m):
 perms=list(permutations(range(m)))
 ident=tuple(range(m)); ix={p:i for i,p in enumerate(perms)}; e=ix[ident]
 table=[[ix[tuple(p[q[i]] for i in range(m))] for q in perms] for p in perms]
 return list(range(len(perms))),e,table

def cyclic_group(q):
 return list(range(q)), 0, [[(i+j)%q for j in range(q)] for i in range(q)]

def actual(n,group):
 elems,ident,mul=group
 idemf,_=base(n); pairs=[]
 for f in idemf:
  R=set(f)
  for free in product(elems,repeat=n-len(R)):
   labels=iter(free); v=tuple(ident if i in R else next(labels) for i in range(n))
   pairs.append((f,v,len(R)))
 count=Counter()
 for f,g,r in pairs:
  for h,k,s in pairs:
   p=tuple(h[f[i]] for i in range(n))
   if not all(p[p[i]]==p[i] for i in range(n)):continue
   u=len(set(p))
   if all(mul[k[f[x]]][g[x]]==ident for x in set(p)):
    count[r,s,u]+=1
 return count,len(pairs)

if __name__=='__main__':
 for n in range(1,11):
  # Polynomial in group order: the top coefficient must be n at degree 2n-2.
  coeff=Counter()
  for a in range(n+1):
   for b in range(n-a+1):
    for c in range(n-a-b+1):
     d=n-a-b-c; r=a+b; s=a+c
     if not (r and s): continue
     m=factorial(n)//(factorial(a)*factorial(b)*factorial(c)*factorial(d))
     for t in range(min(b,c)+1):
      if not (a+t):continue
      k=m*comb(c,t)*(factorial(b)//factorial(b-t))*(a+t)**(b-t)*r**(c-t)*(r*s)**d
      coeff[b+c+2*d-t]+=k
  assert max(coeff)==2*n-2 and coeff[2*n-2]==n,(n,coeff)
 print('asymptotic leading-coefficient checks n=1..10 PASS')
 for n in (1,2,3,4):
  idem,by=base(n)
  for q in (1,2,3,6):
   expected=Counter()
   for (r,s,u,t),ct in by.items():expected[r,s,u]+=ct*q**(2*n-r-s-t)
   f=formula(n,q)
   assert f==expected,(n,q,expected-f,f-expected)
   print('base',n,q,'maps',len(idem),'total',sum(f.values()),'strata',len(f))
 for n,q in ((2,2),(3,2),(4,2)):
  gp=group_perms(2); out,np=actual(n,gp)
  assert out==formula(n,2),(n,out-formula(n,2),formula(n,2)-out)
  print('C2 actual',n,'idempotents',np,'ordered product idempotent pairs',sum(out.values()),'PASS')
 for n in (2,3):
  gp=group_perms(3);out,np=actual(n,gp)
  assert out==formula(n,6),(n,out-formula(n,6),formula(n,6)-out)
  print('S3 actual',n,'idempotents',np,'ordered product idempotent pairs',sum(out.values()),'PASS')

 out,np=actual(3,cyclic_group(6))
 assert out==formula(3,6)
 print('C6 actual',3,'idempotents',np,'ordered product idempotent pairs',sum(out.values()),'PASS')
 print('VERIFY_OK_GROUP_WREATH_SKEW_IDEMPOTENCE')
