"""Reproduce three-node Fourier cluster leading-singular-value checks."""
import mpmath as mp
mp.mp.dps=75
count=0
for n in [1,2,3,5,9]:
  s0=2*n+1
  s2=n*(n+1)*(2*n+1)/3
  s4=n*(n+1)*(2*n+1)*(3*n*n+3*n-1)/15
  normres=mp.sqrt((mp.mpf(str(s4))-mp.mpf(str(s2))**2/s0)/s0)
  for tt in [-mp.mpf('0.7'),-mp.mpf('0.25'),mp.mpf('0'),mp.mpf('0.4'),mp.mpf('0.8')]:
    predicted=normres*(1-tt**2)/mp.sqrt(6+2*tt**2)
    for delta in [mp.mpf('0.008'),mp.mpf('0.004'),mp.mpf('0.002')]:
      xs=[-delta,tt*delta,delta]
      gram=mp.matrix(3,3)
      for i in range(3):
        for j in range(3):
          v=xs[j]-xs[i]
          gram[i,j]=mp.sin((n+mp.mpf('0.5'))*v)/(s0*mp.sin(v/2)) if i!=j else mp.mpf(1)
      eig,_=mp.eigsy(gram)
      sv=mp.sqrt(eig[0]); rel=abs(sv/(delta**2*predicted)-1)
      assert rel<mp.mpf('0.025'), (n,tt,delta,sv,rel)
      count+=1
for n in range(1,100):
  A=mp.mpf(n*(n+1)*(2*n-1)*(2*n+1)*(2*n+3))/45
  s0=2*n+1
  check=mp.mpf(n*(n+1)*(4*n*n+4*n-3))/45
  assert abs(A/s0-check)<mp.mpf('1e-55');count+=1
print('TRIPLE_CLUSTER_CHECKS_PASS',count)
# Apodized symmetric frequency samples: exact Gram from positive cosine weights.
for sample in [([(0,mp.mpf(1)),(-1,mp.mpf(2)),(1,mp.mpf(2)),(-3,mp.mpf(1)),(3,mp.mpf(1))]),
               ([(-2,mp.mpf(3)),(2,mp.mpf(3)),(-7,mp.mpf(2)),(7,mp.mpf(2))])]:
  sw=sum(w for _,w in sample); weights=[(k,w/sw) for k,w in sample]
  m2=sum(w*k*k for k,w in weights)
  m4=sum(w*k**4 for k,w in weights)
  for t in [mp.mpf('0'),mp.mpf('0.2'),mp.mpf('0.7')]:
    C=mp.sqrt(m4-m2*m2)*(1-t*t)/mp.sqrt(6+2*t*t)
    for delta in [mp.mpf('0.01'),mp.mpf('0.004')]:
      xs=[-delta,t*delta,delta]
      gram=mp.matrix([[sum(w*mp.exp(1j*k*(xs[j]-xs[i])) for k,w in weights) for j in range(3)] for i in range(3)])
      # Remove numerical imaginary rounding from Gram, which must be real under symmetry.
      gram=mp.matrix([[mp.re(gram[i,j]) for j in range(3)] for i in range(3)])
      ev,_=mp.eigsy(gram)
      assert abs(mp.sqrt(ev[0])/(C*delta*delta)-1)<mp.mpf('0.02')
      count+=1
print('APODIZED_CLUSTER_CHECKS_PASS',count)
