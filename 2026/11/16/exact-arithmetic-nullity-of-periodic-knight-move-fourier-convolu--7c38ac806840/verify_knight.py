"""Supplemental, exact finite-field checks of a knight-convolution nullity formula.
These finite checks supplement, but do not replace, the analytic proof.
Run: python3 verify_knight.py
"""
from math import gcd, lcm

MOVES = ((1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1))

def is_prime(p):
    if p < 2: return False
    if p % 2 == 0: return p == 2
    d = 3
    while d*d <= p:
        if p%d == 0: return False
        d += 2
    return True

def factors(n):
    a = []; d = 2
    while d*d <= n:
        if n%d==0:
            a.append(d)
            while n%d==0:n//=d
        d += 1
    if n>1:a.append(n)
    return a

def primitive_root(p):
    fs = factors(p-1)
    for g in range(2,p):
        if all(pow(g,(p-1)//q,p)!=1 for q in fs):return g
    raise AssertionError('No primitive root')

def expected(m,n):
    G=gcd(m,n);L=lcm(m,n)
    straight = (2*G if L%2==0 else 0) - (m%2==0) - (n%2==0)
    special = 2*sum((m%6==0,n%6==0,m%2==0 and n%3==0,m%3==0 and n%2==0))
    special += 8*(m%8==0 and n%8==0)
    return straight+special

def count_modp(m,n,p,g):
    a=pow(g,(p-1)//m,p); b=pow(g,(p-1)//n,p)
    aa=[pow(a,k,p) for k in range(m)]; bb=[pow(b,k,p) for k in range(n)]
    ans=0
    for k in range(m):
        ak=aa[k]; ax=aa[(2*k)%m]
        for t in range(n):
            bt=bb[t];by=bb[(2*t)%n]
            x=(ak+pow(ak,p-2,p))%p
            y=(bt+pow(bt,p-2,p))%p
            x2=(ax+pow(ax,p-2,p))%p
            y2=(by+pow(by,p-2,p))%p
            v=(x2*y + x*y2)%p
            ans+=(v==0)
    return ans

def main():
    cases=0
    for m in range(5,25):
        for n in range(5,25):
            L=lcm(m,n);p=L*((100003+L-1)//L)+1
            while not is_prime(p):p+=L
            g=primitive_root(p)
            observed=count_modp(m,n,p,g)
            predicted=expected(m,n)
            if observed != predicted:
                raise AssertionError((m,n,p,observed,predicted))
            cases+=1
    print(f'PASS: {cases} exact finite-field spectral-nullity checks (5<=m,n<=24)')
    for m,n,answer in ((5,5,0),(6,6,18),(8,8,22),(12,12,30),(24,24,62),(6,9,9),(5,6,3)):
        if expected(m,n)!=answer:raise AssertionError((m,n,expected(m,n),answer))
    print('PASS: seven boundary and resonance examples')

if __name__=='__main__':main()
