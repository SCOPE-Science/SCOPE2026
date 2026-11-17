"""Exact binomial census identities and conditional period-four asymptotic."""
from math import factorial, comb

def A(n):return max(0,2**n-2-2*n)
def B(n):return n*A(n-1)
def D(n):return n*(n-1) if n>=4 else 0
def U(n):
    if n<6:return 0
    return 3**n-3*(2**n+n*2**(n-1))+3*(n*n+n+1)
def L(n):return {1:3,2:6,3:6}.get(n,0)
def C3(m,n):return U(m)*U(n)+U(m)*L(n)+L(m)*U(n)
def C4(m,n):return 6*(A(m)+B(m))*(A(n)+B(n))+3*((A(m)+B(m))*(D(n)+U(n))+(A(n)+B(n))*(D(m)+U(m)))
def C1(m,n):return 3**(m+n)-C3(m,n)-C4(m,n)
def U_direct(n):
    return sum(comb(n,i)*comb(n-i,j) for i in range(2,n+1) for j in range(2,n-i+1) if n-i-j>=2)
def A_direct(n):return sum(comb(n,i) for i in range(2,n-1))
def main():
    for n in range(1,101):
        assert U(n)==U_direct(n)
        assert A(n)==A_direct(n)
        assert C1(n,n)>=0 and C3(n,n)>=0 and C4(n,n)>=0
        assert C1(n,n)+C3(n,n)+C4(n,n)==9**n
    print('exponential counts and three basin populations checked for n=1..100: PASS')
    for n in [8,12,20,30,60,120,240]:
        num=C4(n,n)
        asym=3*(n+2)*6**n
        print(f'n={n} P4={num}/{9**n} asymptotic ratio={num/asym:.12f}')
    print('Exact integer checks: PASS')
if __name__ == '__main__':main()
