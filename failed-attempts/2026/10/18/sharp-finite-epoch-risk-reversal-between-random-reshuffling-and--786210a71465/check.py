from fractions import Fraction as F
from itertools import product,permutations

def epoch(vals, r, eta, x, seq):
    for i in seq:
        x = r*x-eta*vals[i]
    return x

def enumerate_exact(n, K, lam, eta, b, x0):
    r=1-eta*lam
    plans={'RR':list(permutations(range(n))),'SGD':list(product(range(n),repeat=n))}
    out={}
    for name,choices in plans.items():
        cumulative=F(0,1)
        for seqs in product(choices,repeat=K):
            x=x0
            for seq in seqs:
                x=epoch(b,r,eta,x,seq)
            cumulative+=x*x
        out[name]=lam*cumulative/(2*len(choices)**K)
    sigma2=sum(v*v for v in b)/n
    W=sum(r**j for j in range(n));Q=sum(r**(2*j) for j in range(n))
    delta=(lam*eta*eta*sigma2/(2*(n-1)))*(Q-W*W)*sum((r**(2*n))**t for t in range(K))
    print(dict(n=n,K=K,r=str(r),rr=str(out['RR']),sgd=str(out['SGD']),delta_formula=str(delta),agree=out['RR']-out['SGD']==delta))
    assert out['RR']-out['SGD']==delta

enumerate_exact(3,2,F(1),F(1,2),(F(1),F(-2),F(1)),F(3,2))
enumerate_exact(3,2,F(1),F(3,2),(F(1),F(-2),F(1)),F(3,2))
enumerate_exact(3,2,F(1),F(1),(F(1),F(-2),F(1)),F(3,2))
enumerate_exact(4,1,F(2),F(3,4),(F(1),F(2),F(-1),F(-2)),F(1,3))

def multi_exact(lam, eta, offsets, x0, K):
    n=len(offsets);d=len(lam)
    opts={'RR':list(permutations(range(n))),'SGD':list(product(range(n),repeat=n))}
    loss={}
    for k,v in opts.items():
      accum=F(0)
      for ps in product(v, repeat=K):
        x=list(x0)
        for seq in ps:
          for i in seq:
            x=[(1-eta*lam[j])*x[j]-eta*offsets[i][j] for j in range(d)]
        accum+=sum(lam[j]*x[j]*x[j]/2 for j in range(d))
      loss[k]=accum/(len(v)**K)
    pred=F(0)
    for j,L in enumerate(lam):
      r=1-eta*L
      var=sum(offsets[i][j]**2 for i in range(n))/n
      Q=sum(r**(2*t) for t in range(n))
      W=sum(r**t for t in range(n))
      S=sum(r**(2*n*k) for k in range(K))
      pred+=eta**2*L*var*(Q-W*W)*S/(2*(n-1))
    print('MULTI',dict(RR=str(loss['RR']),SGD=str(loss['SGD']),delta=str(pred),agrees=loss['RR']-loss['SGD']==pred))
    assert loss['RR']-loss['SGD']==pred

multi_exact([F(1),F(3)],F(1,2),[(F(1),F(1)),(F(-2),F(0)),(F(1),F(-1))],[F(2),F(-1)],2)
multi_exact([F(1),F(3)],F(1,2),[(F(1),F(2)),(F(-2),F(0)),(F(1),F(-2))],[F(2),F(-1)],2)
