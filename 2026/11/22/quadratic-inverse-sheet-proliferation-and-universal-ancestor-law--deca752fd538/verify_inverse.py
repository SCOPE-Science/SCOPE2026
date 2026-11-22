"""Independent finite checks for the inverse-fiber theorem of the 2D logistic-sine cosine map.

Run: python3 verify_inverse.py
No dependencies beyond the Python standard library. The infinite conclusions are proved
analytically in RESULT.md; these computations only check finite instances.
"""
import math
import random

PI = math.pi

def inverse_scalar(target, amplitude, shift):
    """Enumerate all z in [-1,1] with cos(amplitude*sin(pi*z)+shift)=target."""
    assert -1 < target < 1 and amplitude > 0
    angle = math.acos(target)
    roots = []
    for sign in (-1, 1):
        offset = sign * angle - shift
        lo = (-amplitude - offset) / (2 * PI)
        hi = (amplitude - offset) / (2 * PI)
        for k in range(math.ceil(lo - 1e-12), math.floor(hi + 1e-12) + 1):
            s = (2 * PI * k + offset) / amplitude
            if abs(s) > 1 + 1e-10:
                continue
            s = max(-1.0, min(1.0, s))
            z = math.asin(s) / PI
            if abs(s) < 1e-12:
                roots += [-1.0, 0.0, 1.0]
            elif abs(abs(s) - 1.0) < 1e-12:
                roots.append(z)
            else:
                roots += [z, (1.0 if s > 0 else -1.0) - z]
    return roots

def inverse_plane(u, v, b, a, alpha1, alpha2):
    h = 4.0 / b
    ys = inverse_scalar(v, h, PI * a * u * (1 - u) + alpha2)
    out = []
    for y in ys:
        xs = inverse_scalar(u, PI * h, a * y * (1 - y) + alpha1)
        out.extend((x, y) for x in xs)
    return out

def forward(x, y, b, a, alpha1, alpha2):
    h = 4.0 / b
    u = math.cos(PI * h * math.sin(PI * x) + a * y * (1 - y) + alpha1)
    v = math.cos(PI * a * u * (1 - u) + h * math.sin(PI * y) + alpha2)
    return u, v

def check():
    rng = random.Random(1723)
    checked_roots = 0
    checked_cases = 0
    for b in (1.7, 1.0, .65, .3, .18):
        for _ in range(19):
            a = rng.uniform(-3, 3)
            alpha1 = rng.uniform(-12, 12)
            alpha2 = rng.uniform(-12, 12)
            u = rng.uniform(-.99, .99)
            v = rng.uniform(-.99, .99)
            pts = inverse_plane(u,v,b,a,alpha1,alpha2)
            assert pts
            h = 4/b
            # Uniform O(H) bound, intentionally conservative.
            assert abs(len(pts) - (16/PI)*h*h) <= 120*h + 200
            for x,y in pts:
                assert -1.000000001 <= x <= 1.000000001
                assert -1.000000001 <= y <= 1.000000001
                uu,vv=forward(x,y,b,a,alpha1,alpha2)
                assert abs(uu-u)<5e-10 and abs(vv-v)<5e-10,(b,u,v,x,y,uu,vv)
            checked_roots += len(pts)
            checked_cases +=1
    for b in (.8,.4,.2,.1):
        pts=inverse_plane(.241,.617,b,.71,.3,-.2)
        coeff=b*b*len(pts)
        assert abs(coeff - 256/PI)<120*b
        ex2=sum(x*x for x,y in pts)/len(pts)
        ey2=sum(y*y for x,y in pts)/len(pts)
        # Compare a low-order moment with numerical quadrature of the limiting density.
        # Use numerical quadrature as independent moment test.
        steps=100000
        integ=0.0
        for j in range(steps):
            z=-1.0+(2.0*j+1.0)/steps
            integ += z*z * (PI/4)*abs(math.cos(PI*z))*(2/steps)
        assert abs(ex2-integ)<.15
        assert abs(ey2-integ)<.15
        print('b=',b,'N=',len(pts),'b^2*N=',coeff,'E[x^2]=',ex2,'E[y^2]=',ey2,'limit=',integ)
    # Resonant scalar phase: sin(pi*z)=0 gives exactly the three source points
    # -1, 0, 1; cosine target is interior and phase branches remain distinct.
    t=math.cos(.47)
    roots=inverse_scalar(t,8.0,.47)
    assert any(abs(x+1)<1e-12 for x in roots)
    assert any(abs(x)<1e-12 for x in roots)
    assert any(abs(x-1)<1e-12 for x in roots)
    # Construct one interior output from a point on the critical x=1/2 line.
    b,a,alpha1,alpha2=.51,.71,.23,-.34
    u,v=forward(.5,.27,b,a,alpha1,alpha2)
    assert abs(u)<1 and abs(v)<1
    pts=inverse_plane(u,v,b,a,alpha1,alpha2)
    assert any(abs(x-.5)<1e-10 and abs(y-.27)<1e-10 for x,y in pts)
    print('PASS:',checked_cases,'finite parameter cases;',checked_roots,'directly verified inverse points; resonant and critical boundary checks')

if __name__=='__main__':
    check()
