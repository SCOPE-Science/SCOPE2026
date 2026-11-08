"""Independent exact point-count certificate over F_(31^2).

The field is F_31[u]/(u^2+1). The direct fiber-product count and
Klein-four quotient trace identity are both checked.
"""
P=31; Q=P*P

def pair(x):return x%P,x//P
def mul(a,b):
 x,y=pair(a);z,w=pair(b)
 return (x*z-y*w)%P+P*((x*w+y*z)%P)
def power(a,n):
 r=1
 while n:
  if n&1:r=mul(r,a)
  a=mul(a,a);n>>=1
 return r

def chi(a):
 if a==0:return 0
 b=power(a,(Q-1)//2)
 assert b in (1,P-1)
 return 1 if b==1 else -1

# Precompute fourth powers and quadratic characters, ensuring all
# 961 field elements are treated without probabilistic sampling.
fourth=[power(x,4) for x in range(Q)]
character=[chi(x) for x in range(Q)]
def sub_scalar(x,a):return ((x%P-a)%P)+P*(x//P)

def count(a):
 e1=e2=h=2
 c=4
 for x4 in fourth:
  f=sub_scalar(x4,1);g=sub_scalar(x4,a);v=mul(f,g)
  y=character[f];z=character[g]
  e1+=1+y;e2+=1+z;h+=1+character[v]
  c+=(1+y)*(1+z)
 assert c==e1+e2+h-2*(Q+1)
 return (e1,e2,h,c)

if __name__=='__main__':
 assert len(set(fourth))==241  # fourth power residues including zero
 counts={a:count(a) for a in range(P) if a not in (0,1)}
 max_n=Q+1+2*5*P
 max_params=sorted(a for a,s in counts.items() if s[-1]==max_n)
 assert max_params==[14,20,30]
 for a in max_params:
  assert counts[a]==(1024,1024,1148,1272)
 assert all(counts[a][-1]<max_n for a in counts if a not in max_params)
 print('maximal genus-five coefficient parameters:',max_params)
 print('quotient counts at each:',(1024,1024,1148))
 print('point count over F_(31^2):',max_n)
 print('HOWE31_MAXIMAL_CERTIFICATE_PASS')
