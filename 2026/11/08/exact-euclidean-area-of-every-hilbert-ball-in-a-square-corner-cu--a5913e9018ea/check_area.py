"""Independent polygon-clipping checks for Hilbert ball Euclidean areas.

Uses only the Python standard library. All radius parameters refer to the
unhalved Hilbert cross-ratio distance on the open square (-1,1)^2.
"""
import math
import random


def exact_area(u, v, radius):
    t = math.tanh(radius/2)
    base = 4*t*t*(1-u*u)*(1-v*v)/((1-t*t*u*u)*(1-t*t*v*v))
    cuts = 0.0
    for i in (-1, 1):
        for j in (-1, 1):
            a, b = i*u, j*v
            cuts += (t*t*(1-t*t)/2)*(a-b)**2 * (1-a*b-abs(a-b)) / ((1+t*a)**2*(1+t*b)**2)
    return base - cuts


def clipped_polygon(u, v, radius):
    q = math.exp(radius)
    facets = [(1, 0, 1), (-1, 0, 1), (0, 1, 1), (0, -1, 1)]
    vals = [c + a*u + b*v for a,b,c in facets]
    polygon = [(-1.,-1.),(1.,-1.),(1.,1.),(-1.,1.)]
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            a,b,c = facets[i]
            d,e,f = facets[j]
            A = a/vals[i]-q*d/vals[j]
            B = b/vals[i]-q*e/vals[j]
            C = c/vals[i]-q*f/vals[j]
            out = []
            for k in range(len(polygon)):
                p, r = polygon[k], polygon[(k+1)%len(polygon)]
                fp = A*p[0]+B*p[1]+C
                fr = A*r[0]+B*r[1]+C
                inside_p = fp <= 0.
                inside_r = fr <= 0.
                if inside_p:
                    out.append(p)
                if inside_p != inside_r:
                    lam = fp/(fp-fr)
                    out.append((p[0]+lam*(r[0]-p[0]),p[1]+lam*(r[1]-p[1])))
            polygon = out
    return polygon


def poly_area(P):
    return abs(sum(P[i][0]*P[(i+1)%len(P)][1]-P[i][1]*P[(i+1)%len(P)][0] for i in range(len(P))))/2



def direct_cross_ratio(c, y):
    roots=[]
    for i in range(2):
        delta=y[i]-c[i]
        if delta:
            roots += [(1-c[i])/delta,(-1-c[i])/delta]
    positive=min(z for z in roots if z>1)
    negative=max(z for z in roots if z<0)
    return math.log(positive/(positive-1)*(1-negative)/(-negative))


def facet_ratio_distance(c, y):
    ratios=[]
    for i in range(2):
        ratios += [(1+y[i])/(1+c[i]),(1-y[i])/(1-c[i])]
    return math.log(max(ratios)/min(ratios))

def main():
    rng=random.Random(123401)
    n=0
    for _ in range(150):
        c=(rng.uniform(-0.9,0.9),rng.uniform(-0.9,0.9))
        y=(rng.uniform(-0.9,0.9),rng.uniform(-0.9,0.9))
        assert abs(direct_cross_ratio(c,y)-facet_ratio_distance(c,y))<3e-13
    for radius in (0.13, 0.6, 1.5, 3.3, 6.0):
        t = math.tanh(radius/2)
        assert abs(exact_area(0,0,radius)-4*t*t)<2e-13
        for k in range(70):
            u,v=(rng.uniform(-0.98,0.98),rng.uniform(-0.98,0.98))
            formula = exact_area(u,v,radius)
            polygon = clipped_polygon(u,v,radius)
            geom = poly_area(polygon)
            assert abs(formula-geom) < 2e-9*max(1,geom), (radius,u,v,formula,geom)
            assert 0 < formula < 4*t*t
            n+=1
        for eps in (.002,.004):
            exact_deficit = 4*t*t-exact_area(eps,0,radius)
            coefficient = 6*t*t*(1-t*t)
            assert abs(exact_deficit/eps**2-coefficient) < max(.01,coefficient*.06)
    # Vertex repetition in a clipping implementation may occur at coincident edges;
    # the distinct-point count is used for combinatorial checks.
    def vertices(P):
        distinct=[]
        for x in P:
            if not any(math.dist(x,y)<1e-8 for y in distinct):
                distinct.append(x)
        return distinct
    assert len(vertices(clipped_polygon(0,0,1.1)))==4
    assert len(vertices(clipped_polygon(.2,0,1.1)))==8
    assert len(vertices(clipped_polygon(.2,.2,1.1)))==6
    assert len(vertices(clipped_polygon(.2,.1,1.1)))==8
    print('HILBERT_SQUARE_EUCLIDEAN_AREA_OK',n)

if __name__=='__main__':
    main()
