#!/usr/bin/env python3
"""Exact finite covariance checks for product pyramids, plus asymptotic diagnostics."""
from fractions import Fraction as Q
from itertools import product
from math import factorial


def outer(x,y): return [[a*b for b in y] for a in x]
def cov_from_vertices(V):
    N=len(V);r=len(V[0]); mu=[sum(v[j] for v in V)/N for j in range(r)]
    cov=[[sum(v[i]*v[j] for v in V)/N-mu[i]*mu[j] for j in range(r)] for i in range(r)]
    return mu,cov

def cov_product_pyramid(V,m):
    r=len(V[0]); vv=list(product(V,repeat=m)); vec=[[Q(1)]+[Q(0)]*(m*r)]
    for vs in vv:vec.append([Q(0)]+[a for v in vs for a in v])
    return cov_from_vertices(vec)[1],len(vec)

def vertex_formula(V,m):
    r=len(V[0]);v=len(V);t=v**m; D=t+1; d=m*r
    mu,S=cov_from_vertices(V)
    cm=Q(t,D);aa=Q(t,D*D)
    w=[Q(1)]+[-x for _ in range(m) for x in mu]
    C=outer(w,w)
    for i in range(d+1):
        for j in range(d+1): C[i][j]*=aa
    for h in range(m):
        for i in range(r):
            for j in range(r):C[1+h*r+i][1+h*r+j]+=cm*S[i][j]
    return C

def volume_formula(mu,S,m):
    r=len(mu);d=m*r; c=Q(d+1,d+3);aa=Q(d+1,(d+2)**2*(d+3))
    w=[Q(1)]+[-x for _ in range(m) for x in mu]
    C=[[aa*y for y in row] for row in outer(w,w)]
    for h in range(m):
        for i in range(r):
            for j in range(r):C[1+h*r+i][1+h*r+j]+=c*S[i][j]
    return C

def independent_beta_volume(mu,S,m):
    # Derive raw moments by independent source B samples and beta slice integrals.
    r=len(mu);d=m*r
    def beta(h,s):return Q((d+1)*factorial(h)*factorial(d+s),factorial(d+h+s+1))
    Es=beta(0,1);Eh=beta(1,0)
    wmu=[Eh]+[Es*z for _ in range(m) for z in mu]
    C=[[Q(0) for _ in range(d+1)] for _ in range(d+1)]
    C[0][0]=beta(2,0)-Eh**2
    for i in range(d):
        C[0][i+1]=C[i+1][0]=beta(1,1)*mu[i%r]-wmu[0]*wmu[i+1]
        for j in range(d):
            raw=mu[i%r]*mu[j%r]
            if i//r==j//r:raw+=S[i%r][j%r]
            C[i+1][j+1]=beta(0,2)*raw-wmu[i+1]*wmu[j+1]
    return C

def check():
    # For simplex, measure is normalized area; barycentric moment formulas.
    triangle=[[Q(0),Q(0)],[Q(1),Q(0)],[Q(0),Q(1)]]
    square=list(map(list,product([Q(0),Q(1)],repeat=2)))
    shifted=[[a+2,b-Q(1)] for a,b in triangle]
    examples=[]
    for V,kind in ((triangle,'simplex'),(square,'square'),(shifted,'simplex')):
        if kind=='simplex':
            mu=[sum(v[j] for v in V)/3 for j in range(2)]
            S=[[Q(1,18),-Q(1,36)],[-Q(1,36),Q(1,18)]]
        else:
            mu=[Q(1,2),Q(1,2)]
            S=[[Q(1,12),Q(0)],[Q(0),Q(1,12)]]
        examples.append((V,mu,S))
    total=0;nn=0
    for V,mu,S in examples:
        for m in range(1,5):
            v, count=cov_product_pyramid(V,m)
            f=vertex_formula(V,m)
            assert v==f,(V,m,'vertex')
            vol=volume_formula(mu,S,m)
            assert vol==independent_beta_volume(mu,S,m),(V,m,'volume')
            total+=2*len(v)**2;nn+=count
    print('PRODUCT_PYRAMID_DUAL_COVARIANCE_CHECKS_PASSED', 'matrices=',len(examples)*4*2,'exact_entries=',total,'enumerated_vertices=',nn)
if __name__=='__main__':check()
