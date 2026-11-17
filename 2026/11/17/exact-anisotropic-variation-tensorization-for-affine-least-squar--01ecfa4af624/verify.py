"""Exact rational diagnostics for product-grid affine least squares in weighted edge BV.
The theorem for arbitrary dimensions is proved symbolically in RESULT.md;
finite cut enumeration here is diagnostic, not a substitute for that proof.
"""
from fractions import Fraction as F
from itertools import product


def instance(nodes, masses, edge_weights, scales=None):
    d=len(nodes)
    if scales is None:scales=[F(1)]*d
    assert d>=1 and all(len(v)>=2 for v in nodes)
    assert all(all(t[i+1]>t[i] for i in range(len(t)-1)) for t in nodes)
    assert all(all(z>0 for z in m) and sum(m)==1 for m in masses)
    assert all(all(z>0 for z in w) for w in edge_weights)
    shape=[len(t) for t in nodes]
    pts=list(product(*[range(n) for n in shape]))
    index={a:i for i,a in enumerate(pts)}
    means=[sum(z*v for z,v in zip(m,t)) for m,t in zip(masses,nodes)]
    variances=[sum(z*(v-mu)**2 for z,v in zip(m,t)) for m,t,mu in zip(masses,nodes,means)]
    cuts=[]
    for j in range(d):
        for a in pts:
            if a[j]+1>=shape[j]:continue
            b=list(a);b[j]+=1;b=tuple(b)
            wt=scales[j]*edge_weights[j][a[j]]
            for k in range(d):
                if k!=j:wt*=masses[k][a[k]]
            cuts.append((index[a],index[b],wt))
    W=[sum(edge_weights[j][k]*(nodes[j][k+1]-nodes[j][k]) for k in range(shape[j]-1)) for j in range(d)]
    c=[]
    for j in range(d):
        accum=F(0)
        for k in range(shape[j]-1):
            accum+=masses[j][k]*(nodes[j][k]-means[j])
            c.append((j,k,W[j]*(-accum)/(variances[j]*edge_weights[j][k])))
    predicted=max(v for _,_,v in c)
    # P maps any array f to its weighted affine L2 projection.
    def proj(f):
        a=[]
        for j in range(d):
            cov=sum(f[t]* (nodes[j][p[j]]-means[j]) *
                    product_mass(p,masses) for t,p in enumerate(pts))
            a.append(cov/variances[j])
        fmean=sum(f[t]*product_mass(p,masses) for t,p in enumerate(pts))
        return [fmean+sum(a[j]*(nodes[j][p[j]]-means[j]) for j in range(d)) for p in pts]
    def tv(f):
        return sum(w*abs(f[b]-f[a]) for a,b,w in cuts)
    best=F(0)
    for bits in range(1,(1<<len(pts))-1):
        f=[F(bool(bits>>i&1)) for i in range(len(pts))]
        ratio=tv(proj(f))/tv(f)
        if ratio>best:best=ratio
    assert predicted==best,(shape,predicted,best)
    # Analytic exact step extremizer.
    j,k,_=max(c,key=lambda e:e[2]); f=[F(p[j]>k) for p in pts]
    assert tv(proj(f))/tv(f)==predicted
    print('EXACT_COAREA_CUT_ENUMERATION_PASS',shape,'value',str(best),'cuts',2**len(pts)-2)
    return predicted


def product_mass(p,masses):
    z=F(1)
    for j,i in enumerate(p):z*=masses[j][i]
    return z


def uniform(n):
    return [[F(i) for i in range(q)] for q in n], [[F(1,q) for _ in range(q)] for q in n],[[F(1)]*(q-1) for q in n]


def exact_uniform_coefficient(n):
    return F(6*(n*n//4),n*(n+1))


def main():
    for shape in ((2,2),(2,3),(3,3),(2,4),(3,4),(2,2,2),(2,2,3)):
        v=instance(*uniform(shape))
        assert v==max(exact_uniform_coefficient(n) for n in shape)
    nodes=[[F(0),F(2)],[F(-3),F(0),F(2)]]
    masses=[[F(1,3),F(2,3)],[F(1,2),F(1,3),F(1,6)]]
    weights=[[F(3,2)],[F(1,5),F(7,3)]]
    v=instance(nodes,masses,weights,[F(2),F(3,4)])
    assert v>0
    # Closed form, first instability dimension independent of number of axes.
    for n in range(2,101):
        c=exact_uniform_coefficient(n)
        assert (c==1 if n in (2,3) else c>1)
        assert c<F(3,2)
    assert exact_uniform_coefficient(2)==1
    assert exact_uniform_coefficient(3)==1
    assert exact_uniform_coefficient(4)==F(6,5)
    print('SHARP_UNIFORM_FOUR_SITE_ONSET_AND_3_OVER_2_ENVELOPE_PASS')
    print('ALL_PRODUCT_GRID_AFFINE_BV_DIAGNOSTICS_PASS')

if __name__=='__main__':main()
