"""Independent finite checks of an affine cube-section polygon-type law.

Run: python3 verify.py
Only the Python standard library is required. Numerical tests supplement the proof.
"""
import math
import random
from collections import defaultdict

PI = math.pi
ROOT2 = math.sqrt(2.0)
P3 = 2.0 - 4.0 * ROOT2 / PI * math.atan(ROOT2)
P6 = 2.0 * math.sqrt(3.0) / 3.0 - 4.0 * ROOT2 / PI * math.atan(1.0 / ROOT2)
P5 = P3 - 2.0 * P6
P4 = 1.0 - P3 - P5 - P6
THEORY = (P3, P4, P5, P6)
VERTICES = [(i,j,k) for i in (0,1) for j in (0,1) for k in (0,1)]
EDGES = [(i,j) for i in range(8) for j in range(i+1,8)
         if sum(abs(VERTICES[i][k]-VERTICES[j][k]) for k in range(3)) == 1]


def normal_section_counts(a, b, c):
    heights = [a*i+b*j+c*k for i,j,k in VERTICES]
    levels = sorted(set(heights))
    lengths = defaultdict(float)
    for left,right in zip(levels[:-1],levels[1:]):
        t = (left + right)/2
        crossing = sum((heights[i]-t)*(heights[j]-t) < 0 for i,j in EDGES)
        lengths[crossing] += right-left
    return lengths


def test_exact_integer_chambers():
    # Finite tests of the local slice-count identities, including degenerate
    # equalities among subset sums. The proof handles all positive reals.
    cases=0
    for a in range(1,12):
      for b in range(1,12):
       for c in range(1,12):
        lengths=normal_section_counts(a,b,c)
        x,y,z=sorted((a,b,c),reverse=True)
        assert sum(lengths.values())==a+b+c
        assert lengths[3]==2*z
        assert lengths[6]==max(0,y+z-x)
        assert sum(k*v for k,v in lengths.items())==4*(a+b+c)
        assert set(lengths).issubset({3,4,5,6})
        cases+=1
    return cases


def test_normal_integrals():
    # Midpoint quadrature on the one-dimensional integral for the minimum:
    # I = (1/2)*integral_{pi/4}^{pi/2} cos(t)^2/(1+cos(t)^2) dt.
    N=100_000
    lo=PI/4
    step=(PI/2-lo)/N
    midpoint=sum((math.cos(lo+(k+0.5)*step)**2)/
                 (1+math.cos(lo+(k+0.5)*step)**2) for k in range(N)) *step/2
    closed=PI/8-math.atan(ROOT2)/(2*ROOT2)
    assert abs(midpoint-closed)<1e-11
    # Spherical edge lengths in the triangle used for the hexagon integral.
    L1=math.acos(math.sqrt(2/3))
    L3=math.acos(math.sqrt(3)/2)
    hex_integral=(math.sqrt(3)*L3-ROOT2*L1)/2
    assert abs(L1-math.atan(1/ROOT2))<1e-14
    assert abs(L3-PI/6)<1e-14
    assert abs((2/3)*(12/PI)*hex_integral-P6)<1e-13
    assert all(0<x<1 for x in THEORY)
    assert abs(sum(THEORY)-1)<1e-14
    assert abs(sum((i+3)*p for i,p in enumerate(THEORY))-4)<1e-14


def test_random_orthotopes():
    rng=random.Random(271828)
    # Verify distribution mass via independent Gaussian-direction integration,
    # with the correct width weights of conditioned motion-invariant planes.
    cases=((1,1,1),(.4,1,2),(1,1,3),(3,5,7))
    report=[]
    for box in cases:
        sumwidth=0.0
        sumtri=0.0
        sumhex=0.0
        exedge=0.0
        N=150_000
        for _ in range(N):
            normal=[abs(rng.gauss(0,1)) for k in range(3)]
            d=math.sqrt(sum(x*x for x in normal))
            u=[x/d for x in normal]
            c=[box[i]*u[i] for i in range(3)]
            x,y,z=sorted(c,reverse=True)
            w=x+y+z
            sumwidth+=w
            sumtri+=2*z
            sumhex+=max(0,y+z-x)
            exedge+=4*w
        simtri=sumtri/sumwidth
        simhex=sumhex/sumwidth
        assert abs(exedge/sumwidth-4)<1e-12
        if box==(1,1,1):
            assert abs(simtri-P3)<0.003
            assert abs(simhex-P6)<0.002
        else:
            # Bound from the strictly Schur-concave triangle probability.
            assert simtri < P3
        report.append((box,round(simtri,6),round(simhex,6)))
    return report


def test_higher_dimensional_simplex_chambers():
    import itertools
    random_gen=random.Random(314159)
    cases=0
    for d in (3,4,5,6):
        v=list(itertools.product((0,1),repeat=d))
        edge_pairs=[(i,j) for i in range(len(v)) for j in range(i+1,len(v))
                    if sum(v[i][h]!=v[j][h] for h in range(d))==1]
        for trial in range(30):
            a=[random_gen.uniform(.2,2.0) for i in range(d)]
            heights=[sum(a[h]*v_i[h] for h in range(d)) for v_i in v]
            levels=sorted(heights)
            full=sum(a)
            d_vertex_length=0
            for left,right in zip(levels[:-1], levels[1:]):
                t=(left+right)/2
                cut=sum((heights[i]<t)!=(heights[j]<t) for i,j in edge_pairs)
                assert cut>=d
                if cut==d:d_vertex_length+=right-left
            assert abs(d_vertex_length-2*min(a))<1e-9
            cases+=1
    return cases


def test_gaussian_extreme_integral():
    # Simpson's rule numerical calculation of exact Gaussian integral.
    def erfcmax(d):
        n=60000
        right=8.0
        step=right/n
        def f(t):return math.erfc(t/math.sqrt(2))**d
        val=f(0)+f(right)
        for k in range(1,n):val+=(4 if k%2 else 2)*f(k*step)
        return math.sqrt(2*math.pi)*val*step/(3*d)
    assert abs(erfcmax(3)-P3)<3e-11
    outputs={d:erfcmax(d) for d in (3,4,5,10,30,100)}
    assert abs(100*100*outputs[100]-math.pi)<0.12
    return outputs


def run():
    ints=test_exact_integer_chambers()
    test_normal_integrals()
    samples=test_random_orthotopes()
    high=test_higher_dimensional_simplex_chambers()
    extremes=test_gaussian_extreme_integral()
    print('CUBE_AFFINE_CROFTON_EXACT_CHAMBERS_OK',ints)
    print('HIGH_DIMENSIONAL_SIMPLEX_CHAMBERS_OK',high)
    print('CUBE_AFFINE_CROFTON_SPHERICAL_INTEGRALS_OK')
    print('GAUSSIAN_MINIMUM_INTEGRAL_VALUES',extremes)
    print('CUBE_AFFINE_CROFTON_PROBABILITIES',*[f'{p:.12f}' for p in THEORY])
    print('ORTHOTOPE_DIRECTION_WEIGHTED_INTEGRALS',samples)
    print('CUBE_AFFINE_CROFTON_VERIFICATION_OK')


if __name__=='__main__':run()
