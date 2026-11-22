"""Exact bivariate polynomial identity certificate via interpolation."""

def det_bareiss(a):
    n=len(a)
    if n==0:return 1
    a=[r[:] for r in a]
    last=1
    sign=1
    for k in range(n-1):
        if a[k][k]==0:
            r=next((r for r in range(k+1,n) if a[r][k]),None)
            if r is None:return 0
            a[k],a[r]=a[r],a[k];sign=-sign
        piv=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                a[i][j]=(a[i][j]*piv - a[i][k]*a[k][j])//last
            a[i][k]=0
        last=piv
    return sign*a[n-1][n-1]

def mat(t,u):
    a=[[int(i==j) for j in range(16)] for i in range(16)]
    for s in range(16):
        for b in (0,1):
            w=s.bit_count()+b
            if w<=3:
                nxt=(2*s+b)&15
                a[s][nxt]-=t*u**(3-w)
    return a

def declared(t,u):
    return 1-t*u**3-t*t*u-t**4*u*u-2*t**5+t**7*u+t**10

if __name__=='__main__':
    n=0
    for t in range(17):
        for u in range(49):
            a=det_bareiss(mat(t,u))
            b=declared(t,u)
            assert a==b,(t,u,a,b)
            n+=1
    print('determinant_identity=PASS evaluations='+str(n))
    print('degree_bounds_t<=16,u<=48; 17x49 interpolation grid establishes identity')
