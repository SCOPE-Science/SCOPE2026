from eisen import *
# lambda=(1-w), lambda^3 = -3-6w (verify)
lam=(1,-1)
lam2=emul(lam,lam); lam3=emul(lam2,lam)
print("lam^2=",e2str(lam2),"N=",enorm(lam2))
print("lam^3=",e2str(lam3),"N=",enorm(lam3))
def is_lam3_clean(pi):
    return edivides(lam3, esub(pi, ONE))
primes=enum_primary_primes(5000)
clean=[(pi,N) for pi,N in primes if is_lam3_clean(pi)]
print("n eligible:",len(primes),"n lam3-clean:",len(clean))
for pi,N in clean[:40]: print(e2str(pi),N)
