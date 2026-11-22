"""Reproduce finite diagnostics for an analytic symbolic-horseshoe construction.
Requires mpmath >=1.2. The analytic inequalities and Banach argument, not
these samples, prove the all-parameter and infinite-alphabet-size assertions.
"""
import mpmath as mp
mp.mp.dps=75

def example(A,B,v,N=5):
    a,b,v=mp.mpf(A),mp.mpf(B),mp.mpf(v)
    u=v/2
    h=4*(a+1)**2*v**2
    Bnd=a*v+abs(b)*mp.pi*h
    psi_w=v**2/(2*a*mp.pi*mp.sqrt(u*(1-v)))
    psi_y=abs(b)*v**2/(a*mp.pi)
    gy=2*(a+abs(b)*mp.pi)*Bnd
    q=max(psi_w+psi_y,gy)
    assert v<mp.mpf('0.5') and h<1 and abs(b)*h <mp.pi/4
    assert Bnd**2<=h and q<mp.mpf('0.3')
    lo=mp.floor(a/v+1)+1
    hi=mp.ceil(2*a/v-1)-1
    assert hi-lo+1>=N
    # Select separated odd/even-index phase bands, avoiding endpoints.
    ks=[int(lo)+j for j in range(N)]
    def inv(k,w,y):
        return a*mp.pi/(k*mp.pi+mp.asin(mp.sqrt(w))-b*y)
    intervals=[]
    for k in ks:
        vals=[inv(k,w,y) for w in (u,v) for y in (0,h)]
        mini,maxi=min(vals),max(vals)
        assert u<mini<=maxi<v
        intervals.append((mini,maxi))
        for w in [u, (u+v)/2, v]:
            for y in [0,h/3,h]:
                x=inv(k,w,y)
                f=mp.sin(a*mp.pi/x+b*y)**2
                assert abs(f-w)<mp.mpf('1e-55')
    for j in range(N-1):
        assert intervals[j+1][1]<intervals[j][0]
    # Approximate an orbit for a periodic code using truncated contractions.
    seq=[int(lo)+(i%N) for i in range(18)]
    x=[(u+v)/2]*19
    y=[h/4]*19
    y[0]=mp.mpf('0')
    for it in range(400):
        xx=[inv(seq[i],x[i+1],y[i]) for i in range(18)]+[x[-1]]
        yy=[mp.mpf('0')]+[mp.sin(b*mp.pi*y[i]+a*x[i])**2 for i in range(18)]
        dif=max([abs(xx[i]-x[i]) for i in range(18)]+[abs(yy[i]-y[i]) for i in range(19)])
        x,y=xx,yy
        if dif<mp.mpf('1e-65'): break
    assert dif<mp.mpf('1e-65')
    for i in range(16):
        assert abs(mp.sin(a*mp.pi/x[i]+b*y[i])**2-x[i+1])<mp.mpf('1e-55')
        assert abs(mp.sin(b*mp.pi*y[i]+a*x[i])**2-y[i+1])<mp.mpf('1e-55')
    print('a,b,v,N =',A,B,v,N)
    print('h =',mp.nstr(h,16),'contraction_upper =',mp.nstr(q,16))
    print('sample phase indices=',ks,'analytic band count >=',int(mp.floor(a/v))-3)
    print('inverse and forward diagnostic assertions PASS')

example('1','2','0.000001')
example('30','20','0.00000001')
print('All finite diagnostics PASS. Unbounded entropy is proved analytically, not enumerated.')
