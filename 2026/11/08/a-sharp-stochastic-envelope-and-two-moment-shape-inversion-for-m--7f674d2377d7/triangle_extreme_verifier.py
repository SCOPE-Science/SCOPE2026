"""Numerical and exact checks for maximum sampled triangle area and its boundary-corner limit.
Requires Python 3 with NumPy and SciPy.
"""
from itertools import combinations
import numpy as np


def boundary_sample(vertices, n, rng):
    edgevec=np.roll(vertices,-1,axis=0)-vertices
    edges=np.linalg.norm(edgevec,axis=1)
    perimeter=edges.sum()
    s=rng.uniform(0,perimeter,n)
    i=np.searchsorted(np.cumsum(edges),s,side='right')
    t=(s-np.r_[0,np.cumsum(edges)[:-1]][i])/edges[i]
    return vertices[i]+t[:,None]*edgevec[i],i,t,edges


def six_candidates(points, edge_index, edge_parameter):
    ix=[]
    for e in range(3):
        js=np.flatnonzero(edge_index==e)
        if len(js):
            ix.extend([int(js[np.argmin(edge_parameter[js])]),int(js[np.argmax(edge_parameter[js])])])
    return points[sorted(set(ix))]


def max_triangle_area(points):
    if len(points)<3: return 0.
    mx=0.
    for i,j,k in combinations(range(len(points)),3):
        a,b,c=points[[i,j,k]]
        area=abs(np.linalg.det(np.array([b-a,c-a])))/2
        mx=max(mx,area)
    return mx


def quantile_distributions(n, vertices, rep=1200):
    rng=np.random.default_rng(160516+n)
    A=abs(np.linalg.det(np.array([vertices[1]-vertices[0],vertices[2]-vertices[0]])))/2
    out=[]
    failures=0
    for _ in range(rep):
        pts,e,t,l=boundary_sample(vertices,n,rng)
        six=six_candidates(pts,e,t)
        area=max_triangle_area(six)
        if n<=20:
            exact=max_triangle_area(pts)
            if abs(exact-area)>1e-12:failures+=1
        out.append(n*(1-area/A))
    return np.asarray(out),failures


def limit_rates(vertices):
    edges=np.linalg.norm(np.roll(vertices,-1,axis=0)-vertices,axis=1)
    return np.asarray([(edges[(i-1)%3]+edges[i])/sum(edges) for i in range(3)])


def checks():
    rng=np.random.default_rng(72)
    for _ in range(20):
        v=np.array([[0,0],[rng.uniform(.5,4),0],[rng.uniform(.1,3),rng.uniform(.3,4)]],dtype=float)
        x,e,t,_=boundary_sample(v,16,rng)
        assert abs(max_triangle_area(x)-max_triangle_area(six_candidates(x,e,t))) < 1e-11
    for lengths in [(1.,1.,1.), (3.,4.,5.),(1.,1.,0.1)]:
        p=np.array(lengths)/sum(lengths)
        alpha=1-p
        m=sum(1/alpha); vari=sum(1/alpha**2)
        q=(m*m-vari)/2
        r=np.sort(np.roots([1.,-m,q,-q/2]).real)
        assert np.allclose(r,np.sort(1/alpha),atol=1e-9)
    # Analytic pair-rate majorization check via survival curves.
    for rr in [(.51,.99),(.57,.77),(.7,.9)]:
        a,b=rr;r=(a+b)/2; d=(b-a)/2
        for z in np.linspace(0,15,60):
            uneven=np.exp(-r*z)*(np.cosh(d*z)+(r/d)*np.sinh(d*z))
            equal=np.exp(-r*z)*(1+r*z)
            assert uneven+1e-13>=equal
    v_equ=np.array([[0,0],[1,0],[.5,np.sqrt(3)/2.]])
    v_other=np.array([[0,0],[3,0],[.6,1.4]])
    summaries=[]
    for vertices in [v_equ,v_other]:
        alpha=limit_rates(vertices)
        m=sum(1/alpha);var=sum(1/alpha**2)
        for n in [20,100,600]:
            xx,fail=quantile_distributions(n,vertices, rep=1300)
            assert fail==0
            summaries.append((list(np.round(alpha,6)),n,round(float(xx.mean()),4),round(m,4),round(float(xx.var()),4),round(var,4)))
    print('VERIFY_OK six_point_exact=20 inversion=3 rate_pair_inequalities=180 full_or_reduced_extrema=7800')
    for item in summaries:print('rates,n,sim_mean,lim_mean,sim_var,lim_var:',item)

if __name__=='__main__':checks()
