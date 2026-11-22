from itertools import product

def direct(q,n):
    assert q in (3,5,7)
    sl=list(product(range(q),repeat=3))
    vec=list(product(range(q),repeat=2*n))
    zeros=(0,)*3
    counts=[0]*q
    for aa,bb,cc in sl:
      for dd,ee,ff in sl:
        # if [X,Y]=0: bracket h=b f' - c e', e=2(a e' - d b), f=2(d c - a f')
        if (bb*ff-cc*ee)%q or (2*(aa*ee-dd*bb))%q or (2*(dd*cc-aa*ff))%q: continue
        for u in vec:
          for v in vec:
            if any((aa*v[2*i]+bb*v[2*i+1]-dd*u[2*i]-ee*u[2*i+1])%q or (cc*v[2*i]-aa*v[2*i+1]-ff*u[2*i]+dd*u[2*i+1])%q for i in range(n)): continue
            z=sum(u[2*i]*v[2*i+1]-u[2*i+1]*v[2*i] for i in range(n))%q
            counts[z]+=q*q # free centers
    return counts

def symbolic(q,n):
  nnz=q**(2*n+1) * ((q**(2*n)-1)+(q+1)*(q*q-1)*(q**n-1))
  zz=q*q*(q**(2*n)+(q**(2*n)-1)*q**(2*n-1)+(q+1)*(q*q-1)*(q**(2*n)+(q**n-1)*q**(2*n-1))+q*q*(q*q-1)*q**(2*n))
  return [zz]+[nnz]*(q-1)
for q,n in [(3,1),(3,2),(5,1)]:
  a=direct(q,n); b=symbolic(q,n)
  print(q,n,a,b,a==b)
  assert a==b
print('SCHRO_CENTRAL_FIBERS_OK')
