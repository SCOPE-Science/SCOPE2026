"""Independent finite checks for uniform-word palindrome-center variance theorem.
Run: python3 verify.py (Python standard library only).
Finite checks supplement, but do not replace, the all-length forest proof.
"""
from fractions import Fraction
from itertools import product


def radii(n):
    result=[]
    for c2 in range(2*n-1):
        if c2 % 2 == 0:
            i = c2//2
            m = min(i,n-1-i)
            def pairs(r, i=i):
                return [(i-j,i+j) for j in range(1,r+1)]
        else:
            i = (c2+1)//2
            m = min(i,n-i)
            def pairs(r, i=i):
                return [(i-1-j,i+j) for j in range(r)]
        result.append((c2,m,pairs))
    return result


def union_is_forest(n,edges):
    parent=list(range(n))
    def root(a):
        while a!=parent[a]:
            a=parent[a]
        return a
    for a,b in edges:
        a,b=root(a),root(b)
        if a==b:
            return False
        parent[a]=b
    return True


def center_variance(m,q):
    t=Fraction(1,q)
    return (t-(2*m+1)*(1-t)*t**(m+1)-t**(2*m+2))/(1-t)**2


def theorem_variance(n,q):
    if n==1:
        return Fraction(0)
    k=n//2
    return 4*sum((center_variance(j,q) for j in range(1,k)),Fraction(0))+(1 if n%2==0 else 3)*center_variance(k,q)


def brute_variance(n,q):
    total=total_sq=0
    for word in product(range(q),repeat=n):
        count=sum(word[a:b+1]==word[a:b+1][::-1]
                  for a in range(n) for b in range(a+1,n))
        total+=count
        total_sq+=count*count
    denom=q**n
    return Fraction(total_sq,denom)-Fraction(total,denom)**2


def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c


def rational_coefficients(q,count):
    # q(q-1)z^2(1+z)(q+z^2) / [(1-z)^2(q-z^2)^2(q^2-z^2)]
    numerator=poly_mul([0,0,q*(q-1)],poly_mul([1,1],[q,0,1]))
    denominator=poly_mul(poly_mul([1,-2,1],poly_mul([q,0,-1],[q,0,-1])),[q*q,0,-1])
    result=[]
    for n in range(count):
        v=(numerator[n] if n<len(numerator) else 0)
        v-=sum(denominator[j]*result[n-j] for j in range(1,min(n+1,len(denominator))))
        result.append(Fraction(v,denominator[0]))
    return result


def main():
    forest_checks=0
    for n in range(2,17):
        centers=radii(n)
        for ci,mi,pi in centers:
            if mi==0: continue
            for cj,mj,pj in centers:
                if cj<=ci or mj==0: continue
                for r in range(1,mi+1):
                    for s in range(1,mj+1):
                        assert union_is_forest(n,pi(r)+pj(s)),(n,ci,cj,r,s)
                        forest_checks+=1
    variance_cases=0
    for q,nmax in [(2,12),(3,8),(4,7)]:
        for n in range(1,nmax+1):
            assert brute_variance(n,q)==theorem_variance(n,q),(q,n)
            variance_cases+=1
    gf_cases=0
    for q in range(2,8):
        coeffs=rational_coefficients(q,80)
        for n in range(1,80):
            assert coeffs[n]==theorem_variance(n,q),(q,n)
            gf_cases+=1
    # Pairwise independence need not extend to joint independence:
    # for length-three word, X0=X1, X0=X2, X1=X2 have joint probability 1/q^2.
    for q in range(2,6):
        assert Fraction(1,q*q) != Fraction(1,q**3)
    print('VERIFY_OK forest_checks=%d brute_variance_cases=%d gf_cases=%d' % (forest_checks,variance_cases,gf_cases))

if __name__=='__main__':
    main()
