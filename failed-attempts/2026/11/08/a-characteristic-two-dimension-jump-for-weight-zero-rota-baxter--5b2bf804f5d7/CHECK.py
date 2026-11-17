from itertools import product

def gaussian(n,k,q):
    if k<0 or k>n:return 0
    if k==0:return 1
    v=1
    for j in range(k):
        v=v*(q**(n-j)-1)//1
    d=1
    for j in range(k):d*=q**(k-j)-1
    return v//d

def gl(k,q):
    x=1
    for i in range(k):x*=q**k-q**i
    return x

def expected(n,q):
    total=0
    for k in range(n//2+1):
        total+=gaussian(n,k,q)*gaussian(n-k,k,q)*gl(k,q)*q**(n if q%2==0 else n-k)
    return total

def is_RB(P,n,q):
    d=n+1
    basis=[tuple(1 if i==j else 0 for i in range(d)) for j in range(d)]
    # RB bilinear so only basis pairs necessary (because P is linear and products are bilinear)
    def mul(a,b):
        out=[0]*d
        out[0]=a[0]*b[0]%q
        for i in range(1,d):out[i]=(a[0]*b[i]+a[i]*b[0])%q
        return out
    def apply(a):return [sum(P[i][j]*a[j] for j in range(d))%q for i in range(d)]
    PB=[apply(x) for x in basis]
    for i in range(d):
        for j in range(d):
            a,b=mul(PB[i],PB[j]),apply([(c+d)%q for c,d in zip(mul(basis[i],PB[j]),mul(PB[i],basis[j]))])
            if a!=b:return False
    return True

def run():
  for n,q in [(1,2),(1,3),(2,2),(2,3),(3,2)]:
    d=n+1
    c=0; bad=0
    for flat in product(range(q),repeat=d*d):
        P=[flat[i*d:(i+1)*d] for i in range(d)]
        L=[[P[i][j] for j in range(1,d)] for i in range(1,d)]
        L2zero=all(sum(L[i][k]*L[k][j] for k in range(n))%q==0 for i in range(n) for j in range(n))
        Lvzero=all(sum(L[i][k]*P[k+1][0] for k in range(n))%q==0 for i in range(n))
        predicted=all(P[0][j]==0 for j in range(d)) and L2zero and (q%2==0 or Lvzero)
        actual=is_RB(P,n,q)
        c+=actual;bad+=(predicted!=actual)
    ex=expected(n,q)
    print('n=',n,'q=',q,'actual=',c,'formula=',ex,'mismatches=',bad,flush=True)
    assert c==ex and bad==0
if __name__=='__main__':run()
