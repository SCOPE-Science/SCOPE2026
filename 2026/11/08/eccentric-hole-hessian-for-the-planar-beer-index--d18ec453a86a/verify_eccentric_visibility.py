"""Independent numerical checks for eccentric circular-hole visibility geometry.
Public scientific verification only; standard-library Python 3.
"""
import math, random

PI=math.pi

def centered(a):
    return 2*(math.acos(a)-a*math.sqrt(1-a*a))/(PI*(1-a*a))

def curvature(a):
    return 5*a/(PI*(1-a*a)**1.5)

def nonvisible_quadrature(a,e,nq=360,nt=480):
    # Composite midpoint integration of Blaschke-Petkantschin line cross-pair density.
    s=0.0
    for i in range(nq):
        latitude=-PI/2+PI*(i+0.5)/nq
        q=a*math.sin(latitude)
        h=a*math.cos(latitude)
        for j in range(nt):
            theta=PI*(j+0.5)/nt
            p=q+e*math.cos(theta)
            L=math.sqrt(1-p*p)
            tangent=e*math.sin(theta)
            s += 2*((L-h)**2-tangent*tangent)*(L+h)*a*math.cos(latitude)
    return s*(PI/nq)/nt/(PI*(1-a*a)**2)

def direct_visibility_MC(a,e,trials=170000,seed=1729):
    rng=random.Random(seed)
    def point():
        while True:
            r=math.sqrt(rng.random()); ang=2*PI*rng.random()
            x=r*math.cos(ang); y=r*math.sin(ang)
            if (x-e)**2+y*y >= a*a: return (x,y)
    visible=0
    for i in range(trials):
        x,y=point(); u,v=point()
        dx=u-x;dy=v-y; d2=dx*dx+dy*dy
        tau=max(0.0,min(1.0,((e-x)*dx-y*dy)/d2))
        xx=x+tau*dx-e; yy=y+tau*dy
        if xx*xx+yy*yy>=a*a: visible+=1
    return visible/trials

def main():
    for a in (0.2,0.5,0.8):
        b0=1-nonvisible_quadrature(a,0.0)
        assert abs(b0-centered(a))<1.2e-5,(a,b0,centered(a))
        c=curvature(a)
        e=.004*(1-a)
        finite_difference=((1-nonvisible_quadrature(a,e))-b0)/(e*e)
        assert abs(finite_difference/c-1)<1.5e-3,(a,finite_difference,c)
        for shift in (0.0,0.33*(1-a)):
            exact=1-nonvisible_quadrature(a,shift)
            mc=direct_visibility_MC(a,shift)
            assert abs(exact-mc)<.011,(a,shift,exact,mc)
    print('ECCENTRIC_BEER_LOCAL_HESSIAN_AND_DIRECT_SEGMENTS_OK')

if __name__=='__main__':main()
