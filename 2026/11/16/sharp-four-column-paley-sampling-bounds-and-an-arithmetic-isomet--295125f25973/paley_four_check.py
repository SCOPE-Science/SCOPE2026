"""Exact integer tests for four-column nonzero-quadratic-residue Fourier sampling.
Requires Python >=3.9 standard library only. All strict finite-order comparisons
are certified by integer principal minors and rational square-root bounds.
"""
from itertools import combinations
from math import isqrt

T = 10**9

def residues(p):
    return {k*k % p for k in range(1,p)}

def sign_matrix(p, cols, Q):
    return tuple(tuple(0 if i == j else (1 if (cols[i]-cols[j]) % p in Q else -1)
                       for j in range(4)) for i in range(4))

def is_star(S):
    return sorted(sum(S[i][j] == 1 for j in range(4) if j != i)
                  for i in range(4)) == [1,1,1,3]

def is_matching(S):
    return all(sum(S[i][j] == 1 for j in range(4) if j != i) == 1
               for i in range(4))

def is_independent(S):
    return all(S[i][j] == -1 for i,j in combinations(range(4),2))

def determinant(M):
    n=len(M)
    if n == 1: return M[0][0]
    if n == 2: return M[0][0]*M[1][1]-M[0][1]*M[1][0]
    return sum(((-1)**j)*M[0][j]*determinant([r[:j]+r[j+1:] for r in M[1:]])
               for j in range(n))

def has_positive_principal_minors(M):
    return all(determinant([row[:k] for row in M[:k]]) > 0 for k in range(1,5))

def exact_small(p, arith_thresh):
    Q=residues(p)
    hatsqrt=isqrt(p*T*T)  # exact rational floor(T*sqrt(p))
    counts = dict(star=0,matching=0,independent=0,other=0)
    distinct=set()
    for cols in combinations(range(p),4):
        S=sign_matrix(p,cols,Q)
        distinct.add(S)
        if is_star(S): counts['star']+=1
        else: counts['other']+=1
        if is_matching(S): counts['matching']+=1
        if is_independent(S): counts['independent']+=1
    # For every non-star sign pattern, certify H_true > rI.  With
    # H_hat=(pI-J+(hatsqrt/T)S)/(p-1), first certify H_hat > sI
    # where s=r+1/1000.  Then ||H_true-H_hat|| <=3/(T(p-1)) < 1/1000.
    # The multiplier 1000*T converts H_hat-sI to an integer matrix.
    checked=0
    for S in distinct:
        if is_star(S):continue
        M = [[1000*T*(p*(i==j)-1)+1000*hatsqrt*S[i][j]
              - arith_thresh*T*(p-1)*(i==j) for j in range(4)] for i in range(4)]
        assert has_positive_principal_minors(M), (p,S)
        checked+=1
    assert counts['star']>0 and counts['matching']>0 and counts['independent']==0
    # Exhibit the two configurations directly, also the extremal star:
    star={13:(0,1,3,9),17:(0,1,3,10)}[p]
    matching=(0,1,6,7)
    assert is_star(sign_matrix(p,star,Q))
    assert is_matching(sign_matrix(p,matching,Q))
    # Certified rational bounds for the explicit star eigenvalue alpha < r.
    # The inequalities below use only integer squaring and cross-multiplication.
    if p == 13:
        assert 18**2 < 25*p and 2500*p < 181**2
        # 18/5 < sqrt(13) < 181/50, and sqrt(14-sqrt(13)) > 321/100.
        assert (14*50-181)*10000 > 321**2*50
        # Hence alpha < (11 - 18/5 - 642/100)/12 = 98/1200 < 85/1000.
        assert 98*1000 < 85*1200
    else:
        assert 412**2 < 10000*p and 10000*p < 413**2
        # 412/100 < sqrt(17) < 413/100 and sqrt(18-sqrt(17)) > 372/100.
        assert (18*100-413)*10000 > 372**2*100
        # Hence alpha < (15 - 412/100 - 744/100)/16 = 344/1600 < 230/1000.
        assert 344*1000 < 230*1600
    print('CERTIFIED_EXCEPTION',p,'subsets',sum(1 for _ in combinations(range(p),4)),
          'sign_matrices',len(distinct),'nonstar_patterns',checked,'counts',counts,
          'r=',(arith_thresh-1)/1000)

if __name__ == '__main__':
    for p,a in [(13,86),(17,231)]: exact_small(p,a)
    for p in (29,37,41,53,61):
        Q=residues(p)
        # Check each edge of the Paley graph is in a four-clique and induced 2K2.
        for b in Q:
            common=[v for v in range(p) if v not in (0,b) and v in Q and (v-b)%p in Q]
            opposite=[v for v in range(p) if v not in (0,b) and v not in Q and (v-b)%p not in Q]
            assert len(common)==(p-5)//4
            assert len(opposite)==(p-1)//4
            assert any((x-y)%p in Q for x,y in combinations(common,2))
            assert any((x-y)%p in Q for x,y in combinations(opposite,2))
        print('CERTIFIED_LARGE',p,'edges_sampled',len(Q))
    # p=5: 4 of 5 normalized unit Fourier vectors in two rows:
    # full frame operator = 5/2 I, one deleted vector has unit norm,
    # eigenvalues of resulting 4-column Gram are {0,0,3/2,5/2}.
    print('PALEY_FOUR_EXTREMA_PASS small_primes=5,13,17 large_primes=29,37,41,53,61')
