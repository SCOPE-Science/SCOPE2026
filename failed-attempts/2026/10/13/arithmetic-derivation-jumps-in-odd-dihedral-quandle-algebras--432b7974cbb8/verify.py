from math import gcd

def direct_dimension(n, p):
    if n % 2 == 0:
        raise ValueError('odd n only')
    pivots={}
    inv2=pow(2,-1,n)
    for i in range(n):
      for j in range(n):
        t=(2*j-i)%n
        for k in range(n):
          row={}
          for a,c in ((k*n+t,1), (((2*j-k)%n)*n+i,-1), (((k+i)*inv2%n)*n+j,-1)):
            row[a]=(row.get(a,0)+c)%p
            if not row[a]:del row[a]
          while row:
            c=min(row)
            if c not in pivots:
              a=row[c]
              ainv=pow(a,-1,p)
              pivots[c]={x:(y*ainv)%p for x,y in row.items()}
              break
            mult=row[c]
            pr=pivots[c]
            for x,y in pr.items():
              new=(row.get(x,0)-mult*y)%p
              if new:row[x]=new
              else:row.pop(x,None)
    return n*n-len(pivots)

def predicted(n,p):
    if n%2==0 or gcd(n,p)>1:raise ValueError('odd n, p prime to n only')
    if p==2:return 0
    seen=set([0]);dim=0
    for x in range(1,n):
      if x in seen:continue
      orbit=set();todo=[(x,1)];weights={};consistent=True
      while todo:
        a,w=todo.pop();w%=p
        if a in weights:
          if weights[a]!=w:consistent=False
          continue
        weights[a]=w;orbit.add(a)
        todo.append(((2*a)%n,(2*w)%p))
        todo.append(((-a)%n,(-w)%p))
      seen|=orbit
      dim+=int(consistent)
    return dim

if __name__=='__main__':
    tests=[(n,p) for n in [3,5,7,9,11,13,15] for p in [2,3,5,7,11,13] if n%p]
    for n,p in tests:
        a=direct_dimension(n,p)
        b=predicted(n,p)
        print(n,p,a,b,'OK' if a==b else 'ERROR',flush=True)
        assert a==b
    print('VERIFY_OK')

# Arithmetic centralizer/orbit closed formula, implemented independently of
# the breadth-first character-consistency predictor.
from math import lcm

def euler_phi(n):
    return sum(1 for j in range(1,n+1) if gcd(j,n)==1)

def divisor_formula(n,p):
    if n%2==0 or gcd(n,p)>1:raise ValueError('odd n with p coprime to n')
    if p==2:return 0
    total=0
    for m in range(2,n+1):
        if n%m:continue
        h=1
        t=2%m
        while t!=1:
            t=(2*t)%m
            h+=1
        subgroup={pow(2,k,m) for k in range(h)}
        minus_in=(-1)%m in subgroup
        orbit_size=h if minus_in else 2*h
        admissible=(p and ((2**(h//2)+1)%p==0 if minus_in else (2**h-1)%p==0))
        if admissible:total+=euler_phi(m)//orbit_size
    return total

def legendre_certificate_n11():
    n,p=11,3
    chi=[0]*n
    for a in range(1,n):chi[a]=1 if pow(a,(n-1)//2,n)==1 else -1
    assert chi[2]%3==2 and chi[10]%3==2
    for i in range(n):
      for j in range(n):
        t=(2*j-i)%n
        for k in range(n):
          lhs=chi[(k-t)%n]
          rhs=chi[(2*j-k-i)%n]+chi[((k+i)*pow(2,-1,n)-j)%n]
          assert (lhs-rhs)%p==0,(i,j,k,lhs,rhs)
    print('LEGENDRE_N11_P3_OK')

if __name__=='__main__':
    for n,p in tests:
        assert predicted(n,p)==divisor_formula(n,p),(n,p,predicted(n,p),divisor_formula(n,p))
    legendre_certificate_n11()
    print('ARITHMETIC_FORMULA_OK')
