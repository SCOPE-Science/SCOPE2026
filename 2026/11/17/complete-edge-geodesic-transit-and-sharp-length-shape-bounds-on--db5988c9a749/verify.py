"""Independent numerical checks for complete-edge transit on parallel metric corridors.

Usage: python verify.py. No third-party dependencies.
"""
import math
import random


def exact_transit_probability(lengths):
    a = min(lengths)
    assert len(lengths) >= 3 and lengths.count(a) == 1 and a > 0
    d = [x - a for x in lengths if x != a]
    L = sum(lengths)
    return (sum(x*x for x in d)/4 +
            sum(d[i]*d[j] for i in range(len(d)) for j in range(i+1,len(d)))) / L**2


def independent_geodesic(lengths, i, x, j, y):
    """Return whether the shortest path traverses the entire uniquely shortest edge."""
    k = min(range(len(lengths)), key=lambda p: lengths[p])
    a = lengths[k]
    if i == j:
        candidates = [(abs(x-y), False)]
        if i != k:
            candidates += [(x+a+lengths[i]-y, True),
                           (lengths[i]-x+a+y, True)]
    else:
        candidates = [(x+y, False),
                      (lengths[i]-x+lengths[j]-y, False)]
        if i != k and j != k:
            candidates += [(x+a+lengths[j]-y, True),
                           (lengths[i]-x+a+y, True)]
        else:
            # Any complete traversal would have to enter both end vertices
            # from outside the shortest edge; one endpoint already lies on it.
            pass
    return min(candidates, key=lambda pair: pair[0])[1]


def simulated(lengths, count, seed):
    random.seed(seed)
    L = sum(lengths)
    counts = 0
    for _ in range(count):
        endpoints = []
        for __ in range(2):
            z = random.random()*L
            for edge, ell in enumerate(lengths):
                if z < ell:
                    endpoints.append((edge,z)); break
                z -= ell
        (i,x),(j,y) = endpoints
        counts += independent_geodesic(lengths,i,x,j,y)
    return counts/count


def grid_quadrature(lengths,N=180):
    L=sum(lengths)
    s=0
    for i,li in enumerate(lengths):
        for j,lj in enumerate(lengths):
            count=0
            for u in range(N):
                x=(u+0.5)*li/N
                for v in range(N):
                    y=(v+0.5)*lj/N
                    if independent_geodesic(lengths,i,x,j,y):count+=1
            s+=li*lj*count/(N*N)
    return s/(L*L)


def main():
    configs=[(1,2,2),(0.1,2,2),(1,2,4),(2,2.2,3.4),
             (1,1.01,6,8),(0.3,1.2,2.1,3.5,4.8),
             (0.05,2,2,2,2,2,2),(1,2,3,4,5,6)]
    for idx, lengths in enumerate(configs):
        target=exact_transit_probability(lengths)
        approx=grid_quadrature(lengths,N=230)
        sim=simulated(lengths,80000,seed=12113+idx)
        err=abs(approx-target)
        se=math.sqrt(target*(1-target)/80000)
        assert err < .005, (lengths,target,approx)
        assert abs(sim-target)< 5.5*se+0.001, (lengths,target,sim)
        print(len(lengths), tuple(lengths), 'exact',round(target,8),
              'quadrature',round(approx,8),'MC',round(sim,8))
        # Sharp fixed-shortest and fixed-total upper bound.
        m=len(lengths);a=min(lengths);L=sum(lengths)
        sharp=(2*m-3)/(4*(m-1))*(1-m*a/L)**2
        assert target<=sharp+1e-12
        if len(set(lengths[1:]))==1 and lengths[0]==a:assert abs(target-sharp)<1e-12
    # Independently sample the conditional endpoint-coordinate regions.
    # Given a fixed nonminimal edge, positive orientation induces a
    # triangular simplex law, whose three barycentric means are 1/3.
    lengths = (0.6, 3.2, 4.7)
    a, li, lj = lengths
    di, dj = li-a, lj-a
    rng = random.Random(885101)
    tri = [0.0, 0.0, 0.0]
    box = [0.0, 0.0]
    n_tri = n_box = 0
    for _ in range(650000):
        x = rng.random()*li
        y = rng.random()*li
        if x < y and independent_geodesic(lengths,1,x,1,y):
            coord=(2*x/di, 2*(li-y)/di)
            tri[0] += coord[0]
            tri[1] += coord[1]
            tri[2] += 1-coord[0]-coord[1]
            n_tri += 1
        z = rng.random()*lj
        if independent_geodesic(lengths,1,x,2,z) and x<di/2 and lj-z<dj/2:
            box[0] += 2*x/di
            box[1] += 2*(lj-z)/dj
            n_box += 1
    assert n_tri > 50000 and n_box > 40000, (n_tri,n_box)
    assert max(abs(t/n_tri-1/3) for t in tri) < 0.008, tri
    assert max(abs(t/n_box-1/2) for t in box) < 0.008, box
    print('conditional coordinate means', [round(t/n_tri,5) for t in tri],
          [round(t/n_box,5) for t in box], 'sample sizes', n_tri, n_box)
    print('PARALLEL_GEODESIC_COMPLETE_EDGE_TRANSIT_CHECKS_OK',len(configs))

if __name__=='__main__':main()
