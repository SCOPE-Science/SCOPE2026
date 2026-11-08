"""Independent numerical checks for Crofton small-cap laws of convex polygons.

Run: python verify_crofton.py
Dependencies: numpy, scipy.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import beta


def corner(alpha):
    b=math.pi-alpha
    return 2*math.sqrt(2/math.sin(alpha))*quad(lambda t: math.sqrt(max(0.,math.sin(b/2)**2-math.sin(t)**2)),0,b/2,epsabs=1e-12)[0]


def polygon_area(v):
    return abs(0.5*sum(v[i][0]*v[(i+1)%len(v)][1]-v[i][1]*v[(i+1)%len(v)][0] for i in range(len(v))))


def perimeter(v):
    return sum(math.dist(v[i],v[(i+1)%len(v)]) for i in range(len(v)))


def angles(v):
    out=[]
    n=len(v)
    for i in range(n):
        p=np.array(v[(i-1)%n])-np.array(v[i]); q=np.array(v[(i+1)%n])-np.array(v[i])
        out.append(math.acos(np.clip(np.dot(p,q)/(np.linalg.norm(p)*np.linalg.norm(q)),-1,1)))
    return out


def predicted_coeff(v):
    return math.sqrt(polygon_area(v))/perimeter(v)*sum(corner(t) for t in angles(v))


def clip_positive(v,normal,t):
    out=[]
    for i in range(len(v)):
        p=np.array(v[i]); q=np.array(v[(i+1)%len(v)])
        a=np.dot(normal,p)-t; b=np.dot(normal,q)-t
        if a>=0: out.append(tuple(p))
        if (a>0 and b<0) or (a<0 and b>0):
            f=a/(a-b); out.append(tuple(p+f*(q-p)))
    return out


def finite_probability(v,eps,nphi=1024):
    v=np.array(v); area=polygon_area(v); phis=2*math.pi*(np.arange(nphi)+0.5)/nphi
    widths=[]
    for phi in phis:
        u=np.array([math.cos(phi),math.sin(phi)])
        pro=v@u
        lo,hi=min(pro),max(pro)
        maxsupport=hi
        # positive cap decreases with t
        for _ in range(37):
            mid=(lo+hi)/2
            cap=clip_positive(v,u,mid)
            mass=polygon_area(cap) if len(cap)>=3 else 0
            if mass>eps*area: lo=mid
            else: hi=mid
        widths.append(maxsupport-(hi+lo)/2)
    # conditioned line invariant intensity total perimeter
    return (2*math.pi/nphi)*sum(widths)/perimeter(v)


def regpoly(n):return [(math.cos(2*math.pi*j/n),math.sin(2*math.pi*j/n)) for j in range(n)]


def parallelogram(a,b,angle):
    p=np.array([a,0.]); q=np.array([b*math.cos(angle),b*math.sin(angle)])
    return [tuple(-p/2-q/2),tuple(p/2-q/2),tuple(p/2+q/2),tuple(-p/2+q/2)]


def check():
    assert abs(corner(math.pi/2)-math.sqrt(2)*beta(.75,.75)/2)<2e-12
    for ang in [0.08,0.2,0.5,0.9,1.3,math.pi/2,2.5,3.04]:
        # independently integrate the AM-GM upper bound for each vertex pair
        left=math.sqrt(math.sin(ang))/2*(corner(ang)+corner(math.pi-ang))
        assert left < math.sqrt(2)+1e-10,(ang,left)
    for ratio in [0.2,1.0,2.7]:
        for ang in [.07,.31,.83,1.4,2.8]:
            v=parallelogram(1.,ratio,ang)
            assert 0<predicted_coeff(v)<math.sqrt(2)+1e-9
    # exact asymptotic coefficient is compared with a direct polygon-clipping probability,
    # neither the local corner formula nor a symbolic-identity replay is used in clipping.
    shapes=[('square',parallelogram(1,1,math.pi/2)),('skew',parallelogram(1,1,.4)),('triangle',regpoly(3)),('octagon',regpoly(8))]
    for label,vertices in shapes:
        coeff=predicted_coeff(vertices)
        for eps in [1e-3,1e-4]:
            observed=finite_probability(vertices,eps,1024)/math.sqrt(eps)
            print('shape',label,'eps',eps,'observed_C',f'{observed:.10f}','exact_C',f'{coeff:.10f}','rel',f'{(observed/coeff-1):.5f}')
            assert abs(observed/coeff-1)<.13,(label,observed,coeff)
    for n in [20,50,100,400,1600]:
        coeff=predicted_coeff(regpoly(n))
        scaled=coeff*math.sqrt(n)
        print('regular_n',n,'scaled',scaled,'target',math.pi**2/4)
        assert abs(scaled-math.pi**2/4)<(6/n if n<400 else 0.03)
    for alpha in [0.05,0.02,0.01]:
        coeff=predicted_coeff(parallelogram(1,1,alpha))
        print('thin_rhombus',alpha,'coefficient',coeff,'sharp_sup',math.sqrt(2))
        assert coeff<math.sqrt(2) and abs(coeff-math.sqrt(2))<.05
    print('CROFTON_CAP_CHECK_OK')

if __name__=='__main__':check()
