"""Direct checks of bipyramid dihedral minimax formulas.
Run: python verify.py.  Uses only Python standard library."""
import math,random
random.seed(7301)
tests=0
for n in range(3,25):
    a=math.pi/n; s=math.sin(a); c=math.cos(a)
    def metric(hp,hm):
        # Explicit outward normals to triangular facets, via independent vector dot products.
        def u(sign,theta,h):
            k=c/h; den=math.hypot(1,k)
            return (math.cos(theta)/den, math.sin(theta)/den, sign*k/den)
        normals_p=[u(1,(2*j+1)*a,hp) for j in range(n)]
        normals_m=[u(-1,(2*j+1)*a,hm) for j in range(n)]
        def angle(x,y):
            dot=sum(v*w for v,w in zip(x,y))
            return math.acos(min(1,max(-1,-dot))) # pi-arccos(dot)=arccos(-dot)
        return max([angle(normals_p[j],normals_m[j]) for j in range(n)] +
                   [angle(normals_p[j],normals_p[(j+1)%n]) for j in range(n)] +
                   [angle(normals_m[j],normals_m[(j+1)%n]) for j in range(n)])
    phi_star=math.pi-2*math.atan(s)
    hstar=c/s
    assert abs(metric(hstar,hstar)-phi_star)<1e-12; tests+=1
    for k in range(100):
        hp=math.exp(random.uniform(-4,4));hm=math.exp(random.uniform(-4,4))
        thp=math.atan(c/hp);thm=math.atan(c/hm)
        expected=math.pi-min(thp+thm,2*math.asin(s*math.cos(thp)),2*math.asin(s*math.cos(thm)))
        actual=metric(hp,hm)
        assert abs(actual-expected)<1e-12,(n,hp,hm,actual,expected)
        assert actual>=phi_star-1e-12
        tests+=2
    dc=2*math.asin((math.sqrt(1+8*s*s)-1)/(4*s))
    for r in range(1,20):
        delta=(math.pi/2)*r/20
        m=math.atan(s*math.cos(delta/2)/(1+s*math.sin(delta/2)))
        kappa=2*m if delta<dc else 2*math.asin(s*math.cos(delta))
        assert m>0 and 0<dc<math.pi/2
        # analytic minimax: sample 400 parameter values and compare best sampled
        best=0
        for j in range(401):
            mtest=delta/2+(math.pi/2-delta)*j/400
            thp=mtest+delta/2;thm=mtest-delta/2
            if thm<=0 or thp>=math.pi/2:continue
            kt=min(thp+thm,2*math.asin(s*math.cos(thp)),2*math.asin(s*math.cos(thm)))
            best=max(best,kt)
            assert kt<=kappa+1e-12
            tests+=1
        assert 0<=kappa-best<0.01
        if delta<dc:
            assert m>delta/2 and m+delta/2<math.pi/2
            assert abs(2*m-2*math.asin(s*math.cos(m+delta/2)))<1e-12
        tests+=2
print('PASS',tests,'direct normal-vector and fixed-asymmetry assertions')
