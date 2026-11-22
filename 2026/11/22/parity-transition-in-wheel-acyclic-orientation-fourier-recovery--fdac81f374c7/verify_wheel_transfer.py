"""Independent two-state transfer calculation of wheel orientation Fourier coefficients."""

def multiply(a,b):
    return ((a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3]),
            (a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]))

def value(n,s):
    # Row-major 2-by-2 matrices, one spoke sign and one rim sign per vertex.
    p=(1,0,0,1); A=B=0
    for i in range(n):
        a=(s>>i)&1
        b=(s>>(n+i))&1
        A^=a; B^=b
        L=(2,1,1,2) if not b else (0,-1,1,0)
        D=(1,0,0,-1) if a else (1,0,0,1)
        T=multiply(D,L)
        p=multiply(p,(T[0][0],T[0][1],T[1][0],T[1][1]))
        p=(p[0][0],p[0][1],p[1][0],p[1][1])
    return p[0]+p[3] - (1+(-1)**A)*(1+(-1)**B)

def check(n):
    N=3**n-3
    assert value(n,0)==N
    assert sum(value(n,s)**2 for s in range(4**n)) == 4**n*N
    if n%2==0:
        for s in range(4**n):
            v=value(n,s)
            if s.bit_count()%2:assert v==0
            else:assert v%4==2
        b=((1<<n)-1)<<n
        a=0 if n%4==0 else 3
        assert value(n,a|b)==-2
    else:
        b=((1<<n)-1)<<n
        for a in range(1<<n):
            if a.bit_count()%2:assert value(n,b|a)==0
    return n,N

if __name__=='__main__':
    for n in range(3,9):
        print('TRANSFER_WHEEL',*check(n))
    print('TRANSFER_WHEEL_OK')
