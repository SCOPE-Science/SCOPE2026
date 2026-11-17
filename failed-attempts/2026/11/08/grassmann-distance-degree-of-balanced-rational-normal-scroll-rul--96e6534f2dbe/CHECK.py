"""Exact finite-field witnesses for balanced-scroll Grassmann-distance degrees.

Run: python3 CHECK.py. Uses only Python's standard library. Mod-p gcd 1
with degree preservation certifies the corresponding rational gcd is 1.
The universal theorem and the Jacobian formula are proved separately.
"""
P = 1000003

def tr(a):
    a=[int(z)%P for z in a]
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def add(a,b,sign=1):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=sign*v
    return tr(c)

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]+=v*w
    return tr(c)

def scale(a,c):return tr([v*c for v in a])
def deriv(a):return tr([i*a[i] for i in range(1,len(a))] or [0])

def rem(a,b):
    a=tr(a);b=tr(b)
    if b==[0]:raise ZeroDivisionError()
    while a!=[0] and len(a)>=len(b):
        t=a[-1]*pow(b[-1],-1,P)%P
        d=len(a)-len(b)
        for i,v in enumerate(b):a[i+d]=(a[i+d]-t*v)%P
        a=tr(a)
    return a

def gcd(a,b):
    a=tr(a);b=tr(b)
    while b!=[0]:a,b=b,rem(a,b)
    return tr(scale(a,pow(a[-1],-1,P))) if a!=[0] else [0]

def det(a):
    a=[[z%P for z in row] for row in a];n=len(a);ans=1
    for i in range(n):
        piv=next((j for j in range(i,n) if a[j][i]),None)
        if piv is None:return 0
        if piv!=i:a[i],a[piv]=a[piv],a[i];ans=-ans
        z=a[i][i];ans=ans*z%P
        inv=pow(z,-1,P)
        for j in range(i+1,n):
            factor=a[j][i]*inv%P
            for k in range(i,n):a[j][k]=(a[j][k]-factor*a[i][k])%P
    return ans%P

def check(n,d):
    s=[0]*(2*n+1)
    for j in range(n+1):s[2*j]=1
    f=[0];ps=[]
    for i in range(1,d+1):
        a=[0]*(n+1)
        a[0]+=1;a[1]+=i+1;a[n-1]+=i*i+1;a[n]+=i+2
        a=tr(a);norm=sum(x*x for x in a)%P
        assert norm
        f=add(f,scale(mul(a,a),pow(norm,-1,P)))
        ps.append(a)
    h=add(mul(deriv(f),s),mul(f,deriv(s)),-1)
    assert len(h)-1==4*n-2,(n,d,len(h)-1)
    assert gcd(f,s)==[1]
    assert gcd(h,deriv(h))==[1]
    assert gcd(h,s)==[1]
    for a in ps: assert gcd(h,a)==[1]

def jac(n):
    # Tangent basis at u1=1, u2=2+t^n, modulo the constant shift f -> f+c*s.
    s=[0]*(2*n+1)
    for j in range(n+1):s[2*j]=1
    two=[0]*(n+1);two[0]=2;two[n]=1
    directions=[]
    for j in range(1,n+1):
        v=[0]*(j+1);v[j]=2;directions.append(v)
    inv5=pow(5,-1,P)
    for j in range(1,n):
        v=[0]*(j+1);v[j]=1
        directions.append(scale(mul(two,v),2*inv5))
    v=[0]*(n+1);v[0]=1;v[n]=-2
    directions.append(scale(mul(two,v),2*inv5))
    rows=[]
    for a in directions:
        # Reduce modulo s, which is monic of degree 2n.
        a=rem(a,s)
        rows.append(a+[0]*(2*n-len(a)))
    got=det(rows)
    expect=(-pow(4,n+1,P)*pow(pow(5,n,P),-1,P))%P
    assert got==expect,(n,got,expect)

if __name__=='__main__':
    for n in range(2,9):
        jac(n)
        for d in (2,3,4):check(n,d)
    print('BALANCED_SCROLL_GD_CERTIFICATE_OK: 21 exact modular witnesses; 7 Jacobian identities')
