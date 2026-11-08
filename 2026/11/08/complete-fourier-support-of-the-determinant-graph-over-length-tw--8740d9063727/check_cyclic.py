"""Numerical convolution Fourier-support checks on the 3x3 determinant graph.
Requires NumPy. Uses exact modular row elimination before a six-dimensional FFT;
this independent computation does not use stationary-phase or critical-point fibres.
"""
import numpy as np
from itertools import product

def verify(b,c):
 n=9
 x=np.indices((n,)*6,dtype=np.int16)
 u1,u2,u3,v1,v2,v3=x
 cross=[(u2*v3-u3*v2)%n,(u3*v1-u1*v3)%n,(u1*v2-u2*v1)%n]
 f=np.logical_and.reduce([((b * cross[i]+c[i])%n)==0 for i in range(3)]).astype(float)
 ft=np.fft.fftn(f)*n**3
 nz=np.abs(ft)>1e-5
 # use direct elementwise rank over F3
 ind=np.indices((n,)*6,dtype=np.int16).reshape(6,-1)
 a,bv,d,f1,g,h=(-ind)%3
 e0,e1,e2=[z%3 for z in c]
 minor=[(a*g-bv*f1)%3,(a*h-d*f1)%3,(bv*h-d*g)%3,
 (a*e1-bv*e0)%3,(a*e2-d*e0)%3,(bv*e2-d*e1)%3,
 (f1*e1-g*e0)%3,(f1*e2-h*e0)%3,(g*e2-h*e1)%3]
 r1=np.logical_and.reduce([v==0 for v in minor]); det=(a*(g*e2-h*e1)-bv*(f1*e2-h*e0)+d*(f1*e1-g*e0))%3
 if b%3:
  val=(-pow(b%3,-3,3)*det)%3
  expect=r1 | ((det!=0) & (val==1))
 elif b%9:
  expect=((ind%3)==0).all(axis=0) & all(z%3==0 for z in c)
 else:
  expect=(ind==0).all(axis=0)&all(z==0 for z in c)
 expect=expect.reshape((n,)*6)
 print('b,c',b,c,'support actual',nz.sum(),'predicted',expect.sum(),'mismatches',np.count_nonzero(nz^expect),'min positive',np.min(np.abs(ft)[nz]) if nz.any() else None)
 assert np.array_equal(nz,expect)

if __name__=='__main__':
 verify(1,(0,0,0))
 verify(1,(0,0,1))
 verify(3,(0,0,3))
 verify(0,(0,0,0))
 print('ALL_DETERMINANT_CHAIN_CHECKS_OK')
