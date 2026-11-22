import numpy as np, itertools, math

def mask(n,e=.4,d=.4):
    u=np.empty(n)
    if n%2==0:
        m=n//2
        for j in range(m): u[j]=1-e+e*(2*j)/n;u[j+m]=1-e+e*(2*j+1)/n
    else:
        for j in range(n): u[j]=1-e+e*j/n
    r=np.sqrt(u)*np.exp(1j*np.array([d*2**j/2**n for j in range(n)]))
    return r,u

def obs(x,r):
    return np.abs(np.fft.fft(x))**2,np.abs(np.fft.fft(x*r))**2

def inverse(y0,y1,r,u):
    n=len(r); a=np.fft.ifft(y0);b=np.fft.ifft(y1);tol=1e-7*np.max(y0)
    if np.max(np.abs(y0))<1e-14:return np.zeros(n,complex), 'zero'
    nz=[k for k in range(1,n) if abs(a[k])>tol or abs(b[k])>tol]
    if not nz:
        j=int(np.argmin(abs(u-b[0].real/a[0].real)))
        xx=np.zeros(n,complex);xx[j]=np.sqrt(a[0].real)
        return xx,'one'
    if n%2==0 and nz==[n//2]:
        m=n//2;ratio=b[0].real/a[0].real
        pairs=[j for j in range(m) if u[j]-1e-8<=ratio<=u[j+m]+1e-8]
        if len(pairs)!=1:raise ValueError(('antipodal supports',n,ratio,pairs))
        j=pairs[0];k=j+m
        B=(b[0].real-u[j]*a[0].real)/(u[k]-u[j]);A=a[0].real-B
        # a[m]=2Re(z), b[m]=2Re(r[k]conj(r[j]) z) where z=x[k]conj(x[j])
        P=r[k]*np.conj(r[j]);ReZ=a[m].real/2
        ImZ=(P.real*ReZ-b[m].real/2)/P.imag
        z=ReZ+1j*ImZ
        xx=np.zeros(n,complex);xx[j]=np.sqrt(A);xx[k]=z/xx[j]
        return xx,'antipodal'
    k=next(k for k in nz if (2*k)%n!=0)
    ratio=b[k]/a[k]
    pairs=[(j,l) for j in range(n) for l in range(n) if j!=l and (j-l)%n==k]
    j,l=min(pairs,key=lambda jl:abs(r[jl[0]]*np.conj(r[jl[1]])-ratio))
    if abs(r[j]*np.conj(r[l])-ratio)>1e-7:raise ValueError(('non-antipodal support',n,ratio))
    B=(b[0].real-u[l]*a[0].real)/(u[j]-u[l]);A=a[0].real-B
    xx=np.zeros(n,complex);xx[l]=np.sqrt(A);xx[j]=a[k]/xx[l]
    return xx,'general'

rng=np.random.default_rng(12811)
count=0
for n in range(2,18):
  r,u=mask(n)
  for nnz in [0,1,2]:
    for supp in itertools.combinations(range(n),nnz):
       for _ in range(3):
          x=np.zeros(n,complex)
          for j in supp:
             amp=.5+rng.random()*2;phase=rng.random()*2*np.pi
             x[j]=amp*np.exp(1j*phase)
          y0,y1=obs(x,r)
          xr,c=inverse(y0,y1,r,u)
          if nnz:
             jj=supp[0];phase=x[jj]/xr[jj];err=np.max(abs(xr*phase-x))
             assert err<1e-7,(n,supp,c,err,x,xr)
          else:assert np.all(xr==0)
          count+=1
  # Structural verification: all oriented binary-power differences are unique.
  diffs={2**a-2**b for a in range(n) for b in range(n) if a!=b}
  assert len(diffs)==n*(n-1)
  if n%2==0:
    assert all(u[j]<u[j+n//2]<u[j+1] for j in range(n//2-1))
  assert all(abs(abs(z)**2-v)<1e-12 for z,v in zip(r,u))
  assert all((.5<=v<=1.0) for v in u)
print('PASS', count,'signal_reconstructions, n=2..17; all ordered binary differences distinct')
