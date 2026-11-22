"""Independent integer matrix and characteristic-polynomial tests of a one-loop deletion."""
from math import gcd

def build(m):
    n=1<<m
    a=[0]*n
    for v in range(n):
        for b in (0,1):
            u=((v<<1)&(n-1))|b
            a[v]^=1<<u
    a[0]^=1 # delete pre-existing loop 0->0
    return a

def compose(a,b):
    n=len(a);c=[]
    for r in a:
        out=0
        while r:
            t=r&-r;out^=b[t.bit_length()-1];r-=t
        c.append(out)
    return c

def rank(a):
    piv={}
    for x in a:
        while x:
            i=x.bit_length()-1
            if i in piv:x^=piv[i]
            else:piv[i]=x;break
    return len(piv)

def check_rank():
    for m in range(1,8):
        b=build(m);n=1<<m
        power=[1<<i for i in range(n)]
        for t in range(m+3):
            expected=(1<<(m-t))+t if t<=m else m+1
            assert rank(power)==expected,(m,t,rank(power),expected)
            power=compose(power,b)
        print('m',m,'ranks verified; recurrent rank',m+1)

def check_characteristic():
    import sympy as s
    z=s.Symbol('z')
    for m in range(1,5):
        b=build(m);n=1<<m
        mat=s.Matrix([[b[i]>>j&1 for j in range(n)]for i in range(n)])
        coeff=[int(c)%2 for c in mat.charpoly(z).all_coeffs()]
        expected=[1]+[0]*(n-(m+2))+[1]*(m+1) if n>m+1 else [1]*(m+2)
        # factor z^(n-m-1) * (z^(m+1)+...+1)
        expected=[1]*(m+2)+[0]*(n-m-1)
        assert coeff==expected,(m,coeff,expected)
        print('m',m,'charpoly verified')
if __name__=='__main__':
    check_rank();check_characteristic(); print('PASS linear rank and integer character polynomials')
