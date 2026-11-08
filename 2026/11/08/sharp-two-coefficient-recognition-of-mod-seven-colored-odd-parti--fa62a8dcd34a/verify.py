#!/usr/bin/env python3
"""Independent exact-integer verification for the colored-odd-partition mod-7 classification."""
from math import gcd

P = 7
TABLE = {
 1: [1,1,2,3,5,0,4,1,1,2,0,0,0,3],
 2: [1,2,4,1,0,3,5,1,2,0,1,1,0,0],
 3: [1,3,0,2,4,5,0,1,0,0,2,0,5,1],
 4: [1,4,4,0,0,6,5,0,4,1,2,0,0,5],
 5: [1,5,2,3,0,4,0,2,0,2,3,1,4,0],
 6: [1,6,1,5,3,3,5,1,2,2,0,3,3,5],
 7: [1,0,1,0,2,0,3,1,5,1,0,2,4,3],
}
EXPECTED = {1:5, 3:2, 4:4, 5:6, 7:3}

def exact_via_log_derivative(k,N):
    # F=f_2^(k-1)/f_1^k; qF'/F=sum_{m>=1}(k*sigma(m)-2(k-1)*[2|m]*sigma(m/2))q^m.
    def sigma(n):
        return sum(d for d in range(1,n+1) if n%d==0)
    w = [0]+[k*sigma(m)-(2*(k-1)*sigma(m//2) if m%2==0 else 0) for m in range(1,N+1)]
    a=[1]+[0]*N
    for n in range(1,N+1):
        acc=sum(w[m]*a[n-m] for m in range(1,n+1))
        assert acc%n==0,('nonintegral coefficient',k,n)
        a[n]=acc//n
    return a

def product_dp(k,N):
    # Direct colored-part multiplicities: one choice for even m, k choices for odd m.
    a = [1]+[0]*N
    for m in range(1,N+1):
        for _ in range(1 if m%2==0 else k):
            for n in range(m,N+1):
                a[n] = (a[n]+a[n-m])%P
    return a

def verify():
    comparisons=0
    for k in range(1,8):
        a=product_dp(k,13)
        b=[v%P for v in exact_via_log_derivative(k,13)]
        assert a==b==TABLE[k],(k,a,b)
        comparisons+=14
        both=[r for r in range(7) if a[r]==a[r+7]==0]
        assert both==([EXPECTED[k]] if k in EXPECTED else []), (k,both)
    # Color shift from characteristic-seven Freshman's dream.
    for k in range(1,78):
        N=27
        direct=product_dp(k+7,N)
        base=product_dp(k,N)
        d7=product_dp(1,N)  # not used as D; below build D(q^7)=[product(1+q^(7m))]
        d=[1]+[0]*N
        for m in range(7,N+1,7):
            for n in range(N,m-1,-1): d[n]=(d[n]+d[n-m])%P
        predicted=[sum(base[n-j]*d[j] for j in range(n+1))%P for n in range(N+1)]
        assert direct==predicted,(k,direct,predicted)
        comparisons+=N+1
    assert TABLE[3][6]==0 and TABLE[3][13]==1
    print('VERIFY_OK canonical_k=7 canonical_coefficients=98 color_shift_k=77 color_shift_coefficients=2156 total_exact_mod7_checks=%d first_two_classification=complete sharp_first_sample_counterexample=(k=3,r=6)'%comparisons)
    print('ELIGIBLE_MOD_7 '+repr([(0,3),(1,5),(3,2),(4,4),(5,6)]))
    for k in range(1,8):
        print('ROW k=%d initial_zero=%s both_zero=%s coefficients=%s'%(k,[r for r in range(7) if TABLE[k][r]==0],[r for r in range(7) if TABLE[k][r]==TABLE[k][r+7]==0],TABLE[k]))
if __name__=='__main__': verify()
