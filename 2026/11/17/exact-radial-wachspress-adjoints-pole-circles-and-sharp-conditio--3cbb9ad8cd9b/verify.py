"""Independent direct finite checks of exact Wachspress product formula.
Python 3 standard library only. Analytic argument covers all n; these finite checks do not.
"""
import math

checks = 0
for n in range(3, 36):
    c = math.cos(math.pi/n)
    normals = [(math.cos(2*math.pi*j/n), math.sin(2*math.pi*j/n)) for j in range(n)]
    vertices = [(math.cos((2*j-1)*math.pi/n), math.sin((2*j-1)*math.pi/n)) for j in range(n)]
    roots = [c/math.cos(math.pi*k/n) for k in range(2, (n-1)//2+1)]
    assert len(roots) == (n-3)//2
    for t in range(20):
        r = 0.01 + 0.68 * t / 19
        angle = 0.137 + t*0.417
        x, y = r*math.cos(angle),r*math.sin(angle)
        ell = [c - a*x-b*y for a,b in normals]
        weights = []
        for j in range(n):
            w = 1.0
            for k in range(n):
                if k != j and k != (j-1)%n:
                    w *= ell[k]
            weights.append(w)
        q = sum(weights)
        factor = n*c**(n-2)
        for k in range(2,(n-1)//2+1):
            factor *= 1 - math.cos(math.pi*k/n)**2/c**2*r*r
        assert math.isclose(q, factor,rel_tol=5e-11,abs_tol=2e-13),(n,t,'factorization')
        assert math.isclose(sum(weights[j]*vertices[j][0] for j in range(n)),x*q,rel_tol=2e-10,abs_tol=3e-13),(n,t,'precision x')
        assert math.isclose(sum(weights[j]*vertices[j][1] for j in range(n)),y*q,rel_tol=2e-10,abs_tol=3e-13),(n,t,'precision y')
        checks+=3
    q_vert = n*n/(2**n*math.sin(math.pi/n)**2)
    q_r = n*c**(n-2)
    for k in range(2,(n-1)//2+1):
        q_r *= 1 - (math.cos(math.pi*k/n)/c)**2
    assert math.isclose(q_vert,q_r,rel_tol=5e-9,abs_tol=5e-13),(n,'vertex')
    checks+=1
    for k in range(2,(n-1)//2+1):
        theta = math.pi*k/n
        radius = c/math.cos(theta)
        x,y = radius*math.cos(theta),radius*math.sin(theta)
        for idx in (0,k):
            a,b=normals[idx]
            assert abs(c-a*x-b*y) < 1e-12
            checks+=1
    if n>=5:
        assert roots[0]>1 and all(roots[i]<roots[i+1] for i in range(len(roots)-1))
        checks+=1
print('PASS:',checks,'finite standard-library checks for n=3..35')
