"""Exact Euclidean enclosing-sphere checks for complete multipartite Laplacian simplices.

Requires Python 3 stdlib; NumPy/SciPy optional for independent numerical checks.
Run: python check_multipartite_ball.py
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement

def formula(parts):
    n = sum(parts)
    b = [(n-a)*(n-a+1) for a in parts]
    active = []
    tau = None
    # Find the KKT active set without assuming any ordering of equal sizes.
    for j in sorted(range(len(parts)), key=lambda i: (-b[i], i)):
        active.append(j)
        tau = F(sum(parts[i]*b[i] for i in active)-2*n*n,
                sum(parts[i] for i in active))
        if all((b[i] > tau) == (i in active) for i in range(len(parts))):
            break
    assert tau is not None
    positive = [max(F(0), F(z)-tau) for z in b]
    assert sum(parts[i]*positive[i] for i in range(len(parts))) == 2*n*n
    masses = [F(parts[i])*positive[i]/(2*n*n) for i in range(len(parts))]
    assert sum(masses) == 1
    c = [positive[i]/(2*n)-1 for i,a in enumerate(parts) for _ in range(a)]
    radius = F(n)+tau+sum(parts[i]*positive[i]**2 for i in range(len(parts)))/(4*n*n)
    return b,tau,masses,c,radius

def laplacian_columns(parts):
    n=sum(parts); group=[]
    for j,a in enumerate(parts): group += [j]*a
    vertices=[]
    for i in range(n):
        d=n-parts[group[i]]
        vertices.append([F(d) if k==i else F(-1) if group[k]!=group[i] else F(0) for k in range(n)])
    return vertices, group

def exact_test(parts):
    b,tau,masses,c,r2 = formula(parts)
    verts,g = laplacian_columns(parts)
    n = sum(parts)
    assert sum(c) == 0
    assert all(sum(v)==0 for v in verts)
    dot = lambda v,w: sum(x*y for x,y in zip(v,w))
    ds=[dot([x-y for x,y in zip(v,c)],[x-y for x,y in zip(v,c)]) for v in verts]
    assert all(d<=r2 for d in ds)
    assert all(r2-d == max(F(0),tau-b[g[i]]) for i,d in enumerate(ds))
    weights=[masses[g[i]]/parts[g[i]] for i in range(n)]
    assert sum(weights)==1 and all(w>=0 for w in weights)
    assert all(weights[i]==0 or ds[i]==r2 for i in range(n))
    assert all(sum(weights[i]*verts[i][k] for i in range(n))==c[k] for k in range(n))
    assert sum(weights[i]*ds[i] for i in range(n))==r2
    return bool(any(bi==tau for bi in b)),sum(bi>tau for bi in b),sum(a for a,bi in zip(parts,b) if bi>=tau)

def numeric_test(parts):
    import numpy as np
    from scipy.optimize import minimize
    v=np.array(laplacian_columns(parts)[0],float)
    n=v.shape[0]
    b,tau,masses,c,r2=formula(parts)
    # An unrestricted ambient-dimensional convex program, not a class-symmetric fit.
    def objective(z):return z[-1]
    def grad(z):return np.r_[np.zeros(n),1.]
    def constr(z):return z[-1]-np.sum((v-z[:n])**2,axis=1)
    def constrjac(z):return np.column_stack((2*(v-z[:n]),np.ones(n)))
    x0=np.r_[np.zeros(n),np.max(np.sum(v*v,axis=1))+1]
    ans=minimize(objective,x0,method='SLSQP',jac=grad,
                 constraints=[{'type':'ineq','fun':constr,'jac':constrjac}],
                 options={'ftol':2e-10,'maxiter':1000})
    assert ans.success,(parts,ans.message)
    assert abs(ans.fun-float(r2)) < 2e-5, (parts,ans.fun,r2)
    assert np.linalg.norm(ans.x[:n]-np.array(c,float)) < 1e-3, (parts,ans.x[:n],c)

if __name__ == '__main__':
    total=0; zero_weight_contacts=0; positives={}; positive_contacts=set(); numeric=0
    for r,amax in [(3,10),(4,7),(5,5),(6,4)]:
        for parts in combinations_with_replacement(range(1,amax+1),r):
            tie,ct,ctverts=exact_test(parts)
            total+=1; zero_weight_contacts+=tie; positives[(r,ct)]=positives.get((r,ct),0)+1
            positive_contacts.add(ct)
            if (total%17==0 and sum(parts)<=16 and numeric<30):
                numeric_test(parts); numeric+=1
    for parts in [(3,3,6),(4,17,17),(2,2,6),(2,2,4),(4,4,4,6),(7,14,14)]:
        tie,ct,ctverts=exact_test(parts);total+=1; zero_weight_contacts+=tie; positive_contacts.add(ct)
    for parts in [(3,3,6),(2,2,6),(2,2,4),(2,5,5)]:
        numeric_test(parts);numeric+=1
    assert formula((3,3,6))[1]==42
    assert formula((3,3,6))[-1]==78
    assert formula((4,17,17))[1]==468
    assert formula((4,17,17))[-1]==867
    assert set(range(1,4)).issubset(positive_contacts)
    assert zero_weight_contacts>0
    print('MULTIPARTITE_LAPLACIAN_BALL_PASS exact_profiles=%d weak_contact_profiles=%d independent_unrestricted_numeric=%d support_cardinalities=%s' % (total,zero_weight_contacts,numeric,str(sorted(positive_contacts))))
