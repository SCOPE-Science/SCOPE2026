"""Independent finite-dimensional checks for Crofton hyperplane sections of regular cross-polytopes.
Only Python's standard library is required; simulation is supporting evidence, not a proof.
"""
import math
import random

SEED = 20261105
random.seed(SEED)


def order_expectations(dim, step=0.004, upper=10.0):
    count = int(round(upper / step))
    assert count % 2 == 0
    val = [0.0] * (dim + 1)
    for idx in range(count + 1):
        x = idx * step
        f = math.erf(x / math.sqrt(2.0))
        q = 1.0 - f
        w = (1 if idx == 0 or idx == count else (4 if idx % 2 else 2)) * step / 3
        masses = [math.comb(dim, k) * f**k * q**(dim-k) for k in range(dim)]
        prefix = 0.0
        for j in range(1, dim+1):
            prefix += masses[j-1]
            val[j] += w * prefix
    return val


def analytic(dim):
    z = order_expectations(dim)
    prob = {r * (2*dim-r-1): 0.0 for r in range(1,dim+1)}
    for r in range(1,dim+1):
        count = r*(2*dim-r-1)
        prob[count] += (z[dim-r+1]-z[dim-r])/z[dim]
    assert abs(sum(prob.values())-1.0) < 1e-11
    mean = sum(n*p for n,p in prob.items())
    mean_from_edges = (2*dim*(dim-1)/math.sqrt(math.pi))/z[dim]
    assert abs(mean-mean_from_edges) < 4e-7
    return prob,mean


def independent_simulation(dim,samples):
    weighted = {};total=0.0
    for _ in range(samples):
        g = [random.gauss(0,1) for _ in range(dim)]
        m=max(abs(x) for x in g)
        if m==0: continue
        weight = m/math.sqrt(sum(x*x for x in g))
        offset = random.uniform(-m,m)
        vertex_heights = g + [-v for v in g]
        cut = 0
        for a in range(2*dim):
            for b in range(a+1,2*dim):
                if (a+dim==b) or (a>=dim and b+dim==a):
                    continue
                # Vertices form an edge iff they are not antipodal.
                if (vertex_heights[a]-offset)*(vertex_heights[b]-offset)<0:
                    cut+=1
        weighted[cut]=weighted.get(cut,0.0)+weight
        total += weight
    return {k:v/total for k,v in weighted.items()}


def main():
    for d in (3,4,6):
        theo,mean=analytic(d)
        obs=independent_simulation(d,30000)
        err=max(abs(theo.get(k,0)-obs.get(k,0)) for k in set(theo)|set(obs))
        assert err<0.022,(d,theo,obs,err)
        print('dimension=',d,'pmf=',theo,'mean=',mean,'max_abs_sim_error=',round(err,5))
    p6=math.pi/(2*math.atan(1/math.sqrt(2)))-2
    assert abs(analytic(3)[0][6]-p6)<2e-6
    assert abs(analytic(3)[0][4]-(1-p6))<2e-6
    print('CROSSPOLYTOPE_CROFTON_FINITE_LAW_OK')

if __name__=='__main__':main()
