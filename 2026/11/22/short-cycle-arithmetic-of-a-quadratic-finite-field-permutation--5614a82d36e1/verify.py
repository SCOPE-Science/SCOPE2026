"""Exact integer resultants and finite-field checks for short cycles."""
from math import gcd

PHI={8:[1,0,0,0,1],12:[1,0,-1,0,1],15:[1,-1,0,1,-1,1,0,-1,1]}
RES={8:{1:32,3:36,5:16,7:4},12:{1:16,5:25,7:16,11:1},15:{1:256,4:361,11:121,14:1}}


def determinant_exact(a):
    a=[r[:] for r in a]; n=len(a); prev=1; sign=1
    for k in range(n-1):
        pivotrow=next((r for r in range(k,n) if a[r][k]),None)
        if pivotrow is None:return 0
        if pivotrow!=k:
            a[k],a[pivotrow]=a[pivotrow],a[k]; sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numer=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numer%prev==0
                a[i][j]=numer//prev
            a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]


def resultant(f,g):
    m=len(f)-1; n=len(g)-1
    fh=f[::-1]; gh=g[::-1]
    mat=[]
    for i in range(n):
        mat.append([0]*i+fh+[0]*(n-i-1))
    for i in range(m):
        mat.append([0]*i+gh+[0]*(m-i-1))
    assert len(mat)==m+n and all(len(r)==m+n for r in mat)
    return determinant_exact(mat)


def trim(f):
    while len(f)>1 and f[-1]==0:f.pop()
    return f


def mod_poly(f,p):
    return trim([v%p for v in f])


def divmod_poly(a,b,p):
    a=mod_poly(a,p); b=mod_poly(b,p)
    if b==[0]:raise ZeroDivisionError
    quot=[0]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        t=len(a)-len(b); c=a[-1]*pow(b[-1],-1,p)%p
        quot[t]=c
        for i in range(len(b)):a[i+t]=(a[i+t]-c*b[i])%p
        trim(a)
    return trim(quot),a


def gcd_poly(a,b,p):
    a=mod_poly(a,p);b=mod_poly(b,p)
    while b!=[0]:
        _,r=divmod_poly(a,b,p);a,b=b,r
    if a!=[0]:
        u=pow(a[-1],-1,p);a=mod_poly([t*u for t in a],p)
    return a


def x_power_plus_x_minus_two(e):
    g=[-2]+[0]*e;g[1]+=1;g[e]+=1;return g


def verify_resultants():
    count=0
    for d in RES:
        for r,absolute in RES[d].items():
            assert abs(resultant(PHI[d],x_power_plus_x_minus_two(r)))==absolute,(d,r)
            count+=1
    for d,r,p in [(8,3,3),(12,5,5),(15,11,11),(15,4,19)]:
        g=gcd_poly(PHI[d],x_power_plus_x_minus_two(r),p)
        assert len(g)-1==2,(d,r,p,g)
        count+=1
    return count


def verify_prime_power_resonance():
    count=0
    for p in (3,5,7,11,13,17,19,23,29,31,37,41):
        for f in (1,2,3,4):
            q=p**f
            for d in (8,12,15):
                if d%p==0:continue
                target=2 if (f%2==1 and (d,p) in ((8,3),(12,5),(15,11),(15,19))) else 0
                assert len(gcd_poly(PHI[d],x_power_plus_x_minus_two(q%d),p))-1==target,(p,f,d)
                count+=1
    return count


def verify_prime_fields():
    fields=(3,5,7,11,13,17,19,23,29,31,37,41)
    n=0
    for p in fields:
        delta=next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)
        got={8:0,12:0,15:0}
        total_points=0
        for z in range(1,p):
            x,y=1,0
            period=None
            for k in range(1,p*p):
                x,y=(x+z*y)%p,(y+delta*z*x)%p
                if x==1 and y==0:
                    period=k;break
            assert period is not None and (p*p-1)%period==0
            assert period not in [2,3,4,5,6,7,9,10,11,13,14]
            if period in got:got[period]+=1
            total_points +=p*p-1
            n+=1
        predicted={8:2 if p==3 else 0,12:2 if p==5 else 0,15:2 if p in (11,19) else 0}
        assert got==predicted,(p,got,predicted)
        prod=1
        for z in range(p):prod=prod*(1-delta*z*z)%p
        assert prod==4%p
        assert (p*p+(p-1))+total_points==p**3
    return n

if __name__=='__main__':
    a=verify_resultants();b=verify_prime_fields();c=verify_prime_power_resonance()
    print('PASS: %d exact resultants/characteristic certificates, %d prime-field nonzero fibers, %d prime-power spectral checks' % (a,b,c))
