"""Exact rational checks of the polygonal affine oscillator reduction.
Public-domain arithmetic verifier; no third-party libraries required.
These finite tests supplement, rather than replace, the analytic theorem.
"""
from fractions import Fraction as Q

def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def det(a,b): return a[0]*b[1]-a[1]*b[0]
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def scale(a,c): return (a[0]*c,a[1]*c)

def run():
    verts=[(Q(2),Q(0)),(Q(0),Q(1)),(Q(-1),Q(0)),(Q(0),Q(-2))]
    checked=0
    rates=[]
    for i,p in enumerate(verts):
        nxt=verts[(i+1)%len(verts)]
        e=add(nxt,scale(p,-1)); n=(e[1],-e[0]); Delta=det(p,nxt)
        assert Delta>0 and dot(n,e)==0 and dot(n,p)==Delta
        L2=dot(e,e)
        lam=Q(i+2,2)
        mu=lam*dot(p,e)/Delta-Q(1,2)
        B0=lam*dot(p,e)-mu*Delta
        B1=B0+lam*L2
        omega=B1+Q(3,2)
        assert B0==Delta/2 and omega>B1>0
        c=lam*L2; rates.append(c)
        for rad in [Q(1,17),Q(1,2),Q(1),Q(5,3),Q(13)]:
            for u in [Q(0),Q(1,5),Q(3,5),Q(1)]:
                x=scale(add(p,scale(e,u)),rad)
                V=dot(n,x)-Delta
                F=add(scale(e,omega-mu*V),scale(n,-lam*V))
                radial_rhs=-c*(rad-1)
                u_numerator=omega+(B0+c*u)*(rad-1)
                F_from_coordinates=add(scale(p,radial_rhs),scale(e,radial_rhs*u+u_numerator))
                assert F==F_from_coordinates
                assert dot(n,F)==-c*V
                assert V==Delta*(rad-1)
                assert u_numerator>0
                checked+=1
    assert sum(dot(verts[i],add(verts[(i+1)%4],scale(verts[i],-1))) for i in range(4))== -sum(dot(add(verts[(i+1)%4],scale(verts[i],-1)),add(verts[(i+1)%4],scale(verts[i],-1))) for i in range(4))/2
    # Symmetric diamond yields the explicit full-plane example.
    p=(Q(1),Q(0)); nxt=(Q(0),Q(1)); e=add(nxt,scale(p,-1)); Delta=det(p,nxt); lam=Q(1); mu=Q(-2); omega=Q(4)
    B0=lam*dot(p,e)-mu*Delta
    B1=B0+lam*dot(e,e)
    assert (B0,B1,omega)==(Q(1),Q(3),Q(4))
    # Necessity of sharp positivity conditions: violating either makes
    # the angular numerator negative at an admissible sector interior point.
    assert omega + Q(-1)*(Q(6)-1) < 0 # B0=-1, r=6, omega=4
    assert Q(2)+Q(3)*(Q(1,10)-1) < 0 # omega=2 < B1=3, r=1/10
    print(f'VERIFY_OK exact_sector_states={checked} nonuniform_rates={len(set(rates))} square_full_plane=1 sign_boundary_counterexamples=2')
if __name__=='__main__':run()
