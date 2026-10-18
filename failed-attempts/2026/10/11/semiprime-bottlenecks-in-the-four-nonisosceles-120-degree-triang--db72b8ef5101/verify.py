import math

def omega(n):
    assert n>=1
    c=0; p=2
    while p*p<=n:
        while n%p==0:
            c+=1; n//=p
        p += 1 if p==2 else 2
    if n>1: c+=1
    return c

def isprime(n):
    if n<2:return False
    if n%2==0:return n==2
    p=3
    while p*p<=n:
        if n%p==0:return False
        p+=2
    return True

triples=[]
for a in range(1,90):
  for b in range(1,90):
    if math.gcd(a,b)!=1: continue
    s=a*a+a*b+b*b
    c=math.isqrt(s)
    if c*c==s and math.gcd(math.gcd(a,b),c)==1:
      triples.append((a,b,c))
      assert omega(a+b)>=2
      for lam in range(1,25):
        N18=3*lam*lam*(a+2*b)*(a+b)
        assert omega(N18)>=4
        N19=lam*lam*(2*a+b)*(a+b)
        assert omega(N19)>=3
        if (lam*lam)%b==0:
          N20=(lam*lam//b)*(a+b)
          assert omega(N20)>=2
          assert (omega(N20)==2) == (lam*lam==b and omega(a+b)==2)
        N21=lam*lam*(a+2*b)*(2*a+b)
        assert omega(N21)>=2
        rhs=(lam==1 and isprime(a+2*b) and isprime(2*a+b))
        assert (omega(N21)==2)==rhs
        if rhs:
          assert a+2*b != 2*a+b
          assert min(a+2*b,2*a+b)>=5

assert 19*19==5*5+5*16+16*16
assert (4*4*(5+16))//16==21 and omega(21)==2
assert 7*7==3*3+3*5+5*5
assert (3+2*5)*(2*3+5)==143 and omega(143)==2
print('VERIFY_OK primitive_triples',len(triples),'lambda_range=1..24')
