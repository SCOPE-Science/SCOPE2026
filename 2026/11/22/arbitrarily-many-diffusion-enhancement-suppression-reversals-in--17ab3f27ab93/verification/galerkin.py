import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import spsolve

def calculate(N=65,k=25,w=50,eps=.015,t=2):
  D=1.; nu=t/2; ks=list(range(-N,N+1)); width=len(ks); ids={n:i for i,n in enumerate(ks)}
  f={1:np.sqrt(2.)/2,-1:np.sqrt(2.)/2,k:np.sqrt(2*w)/2,-k:np.sqrt(2*w)/2}
  rows=[];cols=[];data=[];rt=[];ct=[];dt=[]
  for sidx,s in enumerate([1,-1]):
    for n in ks:
      i=sidx*width+ids[n]
      rows += [i,i];cols += [i,(1-sidx)*width+ids[n]];data += [-D*n*n-nu,nu]
      rt += [i,i];ct += [i,(1-sidx)*width+ids[n]];dt += [-D*n*n-nu,nu]
      for l,coeff in f.items():
        m=n-l
        if m in ids:
          j=sidx*width+ids[m]
          rows.append(i);cols.append(j);data.append(-eps*s*1j*n*coeff)
          rt.append(i);ct.append(j);dt.append(eps*s*1j*m*coeff)
  size=2*width
  M=sp.coo_matrix((data,(rows,cols)),shape=(size,size)).tolil()
  n0=ids[0];M[n0,:]=0;M[n0,n0]=1;M[n0,width+n0]=1
  rhs=np.zeros(size,dtype=complex);rhs[n0]=1
  p=spsolve(M.tocsr(),rhs)
  B=sp.coo_matrix((dt,(rt,ct)),shape=(size,size)).tolil()
  B[n0,:]=0;B[n0,n0]=1;B[n0,width+n0]=1
  rhs2=np.zeros(size,dtype=complex)
  for idx,s in enumerate([1,-1]):
    for l,c in f.items(): rhs2[idx*width+ids[l]]=eps*s*c
  chi=spsolve((-B).tocsr(),rhs2)
  # evaluate on grid via Fourier direct matrix
  x=np.arange(1024)*2*np.pi/1024
  ex=np.exp(1j*np.outer(ks,x));
  dens=np.array([np.real(p[idx*width:(idx+1)*width] @ ex)/(2*np.pi) for idx in range(2)])
  c=np.array([np.real(chi[idx*width:(idx+1)*width] @ ex) for idx in range(2)])
  cp=np.array([np.real((1j*np.array(ks)*chi[idx*width:(idx+1)*width]) @ ex) for idx in range(2)])
  h=(2*np.pi/1024)
  diff=D*np.sum(dens*(1+cp)**2)*h+nu/2*np.sum(dens*(c[::-1]-c)**2)*h
  v=eps*np.sum(dens*np.array([1,-1])[:,None]*(np.sqrt(2)*np.cos(x)+np.sqrt(2*w)*np.cos(k*x)))*h
  pred=((t-1)/(t+1)**2+w*(t-k*k)/(t+k*k)**2)
  return float(diff-1),float(eps**2*pred),float(v)
if __name__=='__main__':
 for t in [0.5,2,25,1250]:
  print(t,calculate(t=t))
