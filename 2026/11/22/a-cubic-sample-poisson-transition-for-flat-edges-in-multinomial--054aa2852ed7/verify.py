"""Finite exact checks for a critical equal-neighbor multinomial occupancy theorem.

Run: python3 verify.py
All operations in the structural checks use exact Python integer arithmetic.
The limiting theorem uses an analytic Fourier-local-limit argument, not finite tests.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, factorial, exp, log, lgamma, pi, sqrt

checks = 0

def assert_equal(a, b, context):
    global checks
    assert a == b, (context, a, b)
    checks += 1


def compositions(total, count):
    if count == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, count - 1):
                yield (first,) + rest


def ensemble(n, N):
    # Compute exact probabilities by enumerating all n-dimensional counts.
    den = n**N
    s = {"one": 0, "adjacent": 0, "disjoint": 0, "all": 0}
    for x in compositions(N, n):
        mult = factorial(N)
        denom = 1
        for v in x:
            denom *= factorial(v)
        mult //= denom
        s["all"] += mult
        if x[0] == x[1]:
            s["one"] += mult
        if x[0] == x[1] == x[2]:
            s["adjacent"] += mult
        if n >= 4 and x[0] == x[1] and x[2] == x[3]:
            s["disjoint"] += mult
    assert_equal(s["all"], den, ("total multinomial mass", n, N))
    return {k: Fraction(v, den) for k,v in s.items()}


def marg_single(n, N):
    num = sum(comb(N, 2*r)*comb(2*r, r)*(n-2)**(N-2*r)
              for r in range(N//2+1))
    return Fraction(num, n**N)


def marg_adjacent(n, N):
    num = sum(factorial(N)//(factorial(r)**3*factorial(N-3*r)) *
              (n-3)**(N-3*r) for r in range(N//3+1))
    return Fraction(num, n**N)


def marg_disjoint(n, N):
    num = 0
    for a in range(N//2+1):
        for b in range((N-2*a)//2+1):
            q = N-2*a-2*b
            num += factorial(N)//(factorial(a)**2*factorial(b)**2*factorial(q))*(n-4)**q
    return Fraction(num, n**N)


def det_int(a):
    # Leibniz formula, independent of the claimed cluster determinant.
    from itertools import permutations
    k=len(a)
    total=0
    for perm in permutations(range(k)):
        inv=sum(perm[i]>perm[j] for i in range(k) for j in range(i+1,k))
        val=(-1)**inv
        for i in range(k):val*=a[i][perm[i]]
        total+=val
    return total


def clusters(indices):
    out=[]
    for i in sorted(indices):
        if not out or i>out[-1][-1]+1:
            out.append([i])
        else:out[-1].append(i)
    return out


def prob_tie_asymptotic(n, c=1):
    # Stable finite-n binomial mixture: first choose how many balls land
    # in two selected cells, then ask for an equal split.
    N=int(c*n**3)
    p=2/n
    mean=N*p
    spread=sqrt(N*p*(1-p))
    lo=max(0,int(mean-13*spread)-2)
    hi=min(N,int(mean+13*spread)+2)
    ans=0.0
    for k in range(lo,hi+1):
        if k%2:continue
        logp=(lgamma(N+1)-lgamma(k+1)-lgamma(N-k+1)
              +k*log(p)+(N-k)*log(1-p))
        logsplit=lgamma(k+1)-2*lgamma(k//2+1)-k*log(2)
        ans+=exp(logp+logsplit)
    return ans


def main():
    for n in (4,5,6):
        for N in range(9):
            e=ensemble(n,N)
            assert_equal(e["one"],marg_single(n,N),("single",n,N))
            assert_equal(e["adjacent"],marg_adjacent(n,N),("adjacent",n,N))
            assert_equal(e["disjoint"],marg_disjoint(n,N),("disjoint",n,N))
    for n in (5,7,9):
        for k in range(1,5):
            for J in combinations(range(1,n),k):
                A=[[2 if i==j else -1 if abs(J[i]-J[j])==1 else 0
                    for j in range(k)] for i in range(k)]
                claimed=1
                for c in clusters(J):claimed*=len(c)+1
                assert_equal(det_int(A),claimed,("incidence determinant",n,J))
    # Gaussian scaling consistency checks: finite sample, not a proof.
    errors=[]
    for n in (15,25,40):
        p=prob_tie_asymptotic(n)
        value=2*sqrt(pi)*n*p
        errors.append(abs(value-1))
        assert 0.90<value<1.10,(n,value)
        global checks
        checks+=1
    assert errors[-1]<errors[0], errors
    checks+=1
    print(f"PASS {checks} exact/numeric assertions")
    print("Critical single-edge normalization errors:", errors)

if __name__ == '__main__':main()
