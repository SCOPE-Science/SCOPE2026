from pathlib import Path
ROOT = Path(__file__).resolve().parent
import time,itertools,collections
IRR={1:3,2:7,3:11,4:19,5:37,6:67}

def mul(a,b,k):
 mod=IRR[k];mask=(1<<k)-1;res=0
 while b:
  if b&1:res^=a
  b>>=1;a<<=1
  if a&(1<<k):a^=mod
 return res&mask

def power(a,n,k):
 r=1
 for _ in range(n):r=mul(r,a,k)
 return r

def affine(k,t,inf):
 if inf: return [0,0,0,1],[0,0,1,0]
 return [1,t,power(t,2,k),power(t,3,k)],[0,1,0,power(t,2,k)]

def space_null(rows):
 # independent pivots sorted row pivot least index
 piv={}
 for row in rows:
  while row:
   p=row.bit_length()-1
   if p not in piv:
    piv[p]=row;break
   row^=piv[p]
 free=[i for i in range(16) if i not in piv]
 bs=[]
 for i in free:
  vec=1<<i
  for p in sorted(piv):
   if (vec&piv[p]).bit_count()%2: vec^=1<<p
  assert all((vec & rr).bit_count()%2 == 0 for rr in rows)
  bs.append(vec)
 return bs

def sieve(k, bad):
 v=range(1<<k);points=[(x,False) for x in v]+[(0,True)]
 info=[affine(k,x,inf) for x,inf in points]
 nsub=0;rankdist=collections.Counter()
 for A,DA in info:
  for B,DB in info:
   coeff=[]
   for i in range(4):
    for j in range(4):
     coeff.append((mul(A[i],B[j],k),mul(DA[i],B[j],k),mul(A[i],DB[j],k)))
   rows=[]
   for ch in range(3):
    for shift in range(k):
     row=sum(((coeff[idx][ch]>>shift)&1)<<idx for idx in range(16))
     rows.append(row)
   basis=space_null(rows)
   rankdist[16-len(basis)]+=1
   if len(basis)>0:
    x=[0]
    for vec in basis:
     x += [a^vec for a in x]
    for a in x:bad[a]=1
    nsub+=1
 print(k,'positive nullspaces',nsub,'rank distribution',rankdist,'bad',sum(bad),'survivors',65536-sum(bad),flush=True)

if __name__=='__main__':
 st=time.time();bad=bytearray(1<<16)
 for k in range(1,7): sieve(k,bad)
 print('TOTAL_SMOOTH',65536-sum(bad))
 print('time',time.time()-st)
 with open(ROOT / "sieve_survivors.txt",'w') as f:f.write('\n'.join(str(i) for i in range(1,65536) if not bad[i]))
