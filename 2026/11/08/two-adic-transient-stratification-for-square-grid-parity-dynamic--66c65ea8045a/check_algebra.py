"""Independent GF(2) polynomial and truncated-ring checks for the square-grid theorem."""

def poly_mul(a,b):
    r=0
    while b:
        if b&1:r^=a
        a<<=1;b>>=1
    return r

def poly_gcd(a,b):
    while b:
        k=a.bit_length()-b.bit_length()
        while k>=0:
            a^=b<<k
            k=a.bit_length()-b.bit_length()
        a,b=b,a
    return a

def derivative(a):
    out=0
    for i in range(1,a.bit_length(),2):
        if (a>>i)&1:out|=1<<(i-1)
    return out

def fibonacci_poly(n):
    f0,f1=1,2 # polynomials p_0=1, p_1=x
    if n==0:return f0
    for j in range(2,n+1):f0,f1=f1,(f1<<1)^f0
    return f1

def mul_matrix(P,e):
    # P rows GF2: coefficient of input x^i y^j in output z*x^i y^j.
    rows=[0]*(e*e)
    for j in range(e):
        for i in range(e):
            col=j*e+i
            if i+1<e:rows[j*e+i+1]^=1<<col
            if j+1<e:rows[(j+1)*e+i]^=1<<col
    return rows

def rank(rows):
    pivot={}
    for x in rows:
        while x:
            i=x.bit_length()-1
            if i in pivot:x^=pivot[i]
            else:pivot[i]=x;break
    return len(pivot)

def prod(A,B):
    out=[]
    for v in A:
        x=0
        while v:
            l=v&-v;x^=B[l.bit_length()-1];v-=l
        out.append(x)
    return out

def main():
    checks=0
    for n in range(2,130):
        h=(n+1)&-(n+1);u=(n+1)//h
        f=fibonacci_poly(n)
        fodd=fibonacci_poly(u-1)
        assert fodd&1==1
        assert all(((fodd>>j)&1)==0 for j in range(1,fodd.bit_length(),2))
        g=sum(((fodd>>(2*j))&1)<<j for j in range(fodd.bit_length()//2+1))
        assert poly_gcd(g,derivative(g))==1
        q=1
        for _ in range(2*h):q=poly_mul(q,g)
        assert f==q<<(h-1),(n,h,u)
        checks+=3
    print('PASS polynomial multiplicity and squarefreeness checks:',checks,'comparisons through n=129')
    t=0
    for h in [2,4,8,16]:
        for e in [h,h-1]:
            N=e*e
            A=mul_matrix(None,e)
            P=[1<<i for i in range(N)]
            for k in range(h+1):
                got=rank(P)
                expect=(e*(h-k) if e==h else ((e*e if k==0 else (h-2)*max(h-k,0))))
                assert got==expect,(h,e,k,got,expect)
                P=prod(A,P)
                t+=1
    print('PASS two-variable multiplication Jordan ranks:',t,'comparisons through h=16')
    print('ALL PASS')
if __name__=='__main__':main()
