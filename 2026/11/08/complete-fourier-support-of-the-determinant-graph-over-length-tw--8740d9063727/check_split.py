"""6-dimensional row-elimination Fourier verification for F_3[t]/(t^2)."""
import numpy as np

def run(b,c):
 # Ring elements a+t d, represented by (a,d) in F3^2; all arrays have shape 3^12.
 N=3
 v=np.indices((3,)*12,dtype=np.int16)
 u=[(v[2*j],v[2*j+1]) for j in range(3)]
 w=[(v[2*j+6],v[2*j+7]) for j in range(3)]
 def mul(a,z):return ((a[0]*z[0])%N,(a[0]*z[1]+a[1]*z[0])%N)
 def sub(a,z):return ((a[0]-z[0])%N,(a[1]-z[1])%N)
 cross=[sub(mul(u[1],w[2]),mul(u[2],w[1])),sub(mul(u[2],w[0]),mul(u[0],w[2])),sub(mul(u[0],w[1]),mul(u[1],w[0]))]
 f=np.ones(v.shape[1:],dtype=bool)
 for j in range(3):
  bc=mul(b,cross[j]);f &= (((bc[0]+c[j][0])%N)==0) & (((bc[1]+c[j][1])%N)==0)
 ft=(N**6)*np.fft.fftn(f.astype(float))
 nz=np.abs(ft)>1e-5
 # fft index for coefficient of variable u0 is - A_t; for u_t is - A_0.
 A0=[(-v[2*i+1])%3 for i in range(3)]
 B0=[(-v[2*i+7])%3 for i in range(3)]
 C0=[z[0]%3 for z in c]
 a,bv,d=A0;e,f1,g=B0;h,i,j=C0
 minors=[(a*f1-bv*e)%3,(a*g-d*e)%3,(bv*g-d*f1)%3,
 (a*i-bv*h)%3,(a*j-d*h)%3,(bv*j-d*i)%3,
 (e*i-f1*h)%3,(e*j-g*h)%3,(f1*j-g*i)%3]
 rank_le1=np.logical_and.reduce([x==0 for x in minors]); det=(a*(f1*j-g*i)-bv*(e*j-g*h)+d*(e*i-f1*h))%3
 if b[0]!=0:
  expect=rank_le1 | ((det!=0)& ((-pow(b[0],-3,3)*det)%3==1))
 else:
  # A reduction zero means fft freq of every residue-coefficient u_t is zero.
  expect=np.logical_and.reduce([a==0,bv==0,d==0,e==0,f1==0,g==0])
  if b[1]==0: expect &= all(z[0]==0 and z[1]==0 for z in c) & np.logical_and.reduce([v[2*i]==0 for i in (0,1,2,3,4,5)])
  else: expect &= all(z[0]==0 for z in c)
 print('ring F3[t]/t^2 b=',b,'c=',c,'nonzeros',nz.sum(),'pred',expect.sum(),'mismatch',np.count_nonzero(nz^expect))
 assert np.array_equal(nz,expect)

run((1,0),((0,0),(0,0),(1,0)))
run((1,0),((0,0),(0,0),(0,0)))
run((0,1),((0,0),(0,0),(0,1)))
print('SPLIT_CHAIN_EXACT_SUPPORT_CHECKS_OK')
