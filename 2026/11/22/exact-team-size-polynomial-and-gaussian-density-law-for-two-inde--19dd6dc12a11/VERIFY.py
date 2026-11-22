"""Cross-checking finite tests of two-rectangle team-size polynomial.
Standard-library only; no external packages.
"""
from collections import Counter
from itertools import combinations
from math import comb, factorial

def weighted_formula(m,n):
    # Polynomials are represented as dicts degree -> integer coefficient.
    def plus(a,b,sgn=1):
        c=Counter(a)
        for k,v in b.items(): c[k]+=sgn*v
        return {k:v for k,v in c.items() if v}
    def power(items,m):
        out={0:1}
        for _ in range(m):
            nxt=Counter()
            for k,v in out.items():
                for e in items:nxt[k+e]+=v
            out=dict(nxt)
        return out
    def IE(vals):
        # exact rows using ALL len(vals) distinct nonzero patterns, plus zero
        from itertools import combinations
        ans={}
        for z in range(len(vals)+1):
            for sel in combinations(vals,z):
                ans=plus(ans,power((0,)+sel,m),(-1)**(len(vals)-z))
        return ans
    ans={0:1}
    for A in range(1,1<<n):
        ans=plus(ans,IE([A.bit_count()]))
    for A in range(1,1<<n):
        for B in range(A+1,1<<n):
            ans=plus(ans,IE([A.bit_count(),B.bit_count()]))
            if (A&B)!=A and (A&B)!=B:
                ans=plus(ans,IE([A.bit_count(),B.bit_count(),(A|B).bit_count()]))
    return dict(sorted(ans.items()))

def independent_coverage(m,n):
    rectangles=[0]
    for rowmask in range(1,1<<m):
        for colmask in range(1,1<<n):
            mask=sum(1<<(i*n+j) for i in range(m) for j in range(n)
                     if (rowmask>>i)&1 and (colmask>>j)&1)
            rectangles.append(mask)
    # enumerate every union of at most 2 rectangles
    matrices={a|b for j,a in enumerate(rectangles) for b in rectangles[j:]}
    return dict(sorted(Counter(v.bit_count() for v in matrices).items()))

def main():
    cases=0
    for m in range(1,6):
        for n in range(1,6):
            got=weighted_formula(m,n)
            ex=independent_coverage(m,n)
            assert got==ex,(m,n,got,ex)
            assert got==weighted_formula(n,m),('transpose',m,n)
            cases+=1
    assert sum(weighted_formula(3,3).values())==356
    assert sum(weighted_formula(4,4).values())==1+225+8550
    print('VERIFY_OK 25_rectangular_cases, complete_two_rectangle_unions, transpose, OEIS_small_rank_counts')
    print('3x3:',weighted_formula(3,3))
    print('4x4:',weighted_formula(4,4))
if __name__=='__main__':main()

# Optional additional checks, based on the independent multinomial intersection census.
def weighted_via_intersections(m,n):
    from math import factorial
    from collections import Counter
    def op(a,b,sign=1):
        z=Counter(a)
        for k,v in b.items(): z[k]+=sign*v
        return {k:v for k,v in z.items() if v}
    def power(exponents):
        q={0:1}
        for _ in range(m):
            t=Counter()
            for k,v in q.items():
                for e in exponents:t[k+e]+=v
            q=dict(t)
        return q
    def d(vals):
        from itertools import combinations
        ret={}
        for k in range(len(vals)+1):
            for sub in combinations(vals,k):
                ret=op(ret,power((0,)+sub),(-1)**(len(vals)-k))
        return ret
    w={0:1}
    for a in range(1,n+1):w=op(w,{k:v*comb(n,a) for k,v in d([a]).items()})
    pairs=Counter();triples=Counter()
    for a in range(1,n+1):
        for b in range(1,n+1):
            for c in range(max(0,a+b-n),min(a,b)+1):
                if a==b==c:continue
                ways=factorial(n)//(factorial(c)*factorial(a-c)*factorial(b-c)*factorial(n-a-b+c))
                for k,v in d([a,b]).items():pairs[k]+=ways*v
                if c<a and c<b:
                    for k,v in d([a,b,a+b-c]).items():triples[k]+=ways*v
    assert all(v%2==0 for v in pairs.values())
    assert all(v%2==0 for v in triples.values())
    w=op(w,{k:v//2 for k,v in pairs.items()})
    w=op(w,{k:v//2 for k,v in triples.items()})
    return dict(sorted(w.items()))

def test_independent_inclusions_and_moments():
    from itertools import product
    from fractions import Fraction
    for m in range(1,6):
        for n in range(1,6):
            assert weighted_via_intersections(m,n)==weighted_formula(m,n), (m,n)
    for N in range(1,5):
        sumh=sumh2=0
        for rowcodes in product(range(4),repeat=N):
            for colcodes in product(range(4),repeat=N):
                ones=sum(1 for u in rowcodes for v in colcodes if (u&v)!=0)
                sumh+=ones
                sumh2+=ones*ones
        den=16**N
        mean=Fraction(sumh,den*N*N)
        var=Fraction(sumh2,den*N**4)-mean**2
        assert mean==Fraction(7,16),(N,mean)
        assert var==Fraction(38*N+25,256*N*N),(N,var)
    print('WEIGHTED_MULTINOMIAL_OK 25_rectangular_cases; FACTOR_MOMENTS_OK N=1..4')

if __name__=='__main__':test_independent_inclusions_and_moments()

def test_generic_unique_representations():
    from itertools import product
    from collections import Counter
    N=4
    all_outputs=Counter()
    generic_outputs=Counter()
    for rows in product(range(4),repeat=N):
        row_event=set(rows)==set(range(4))
        for cols in product(range(4),repeat=N):
            mat=sum(1<<(i*N+j) for i,u in enumerate(rows) for j,v in enumerate(cols) if (u&v))
            all_outputs[mat]+=1
            if row_event and (1 in cols) and (2 in cols):
                generic_outputs[mat]+=1
    assert generic_outputs and all(v==2 for v in generic_outputs.values())
    assert all(all_outputs[k]==2 for k in generic_outputs)
    print('GENERIC_FACTOR_UNIQUENESS_OK',len(generic_outputs),'matrices order 4')

if __name__=='__main__':test_generic_unique_representations()
