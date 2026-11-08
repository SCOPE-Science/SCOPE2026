"""Independent geometric and algebraic spot checks for a maximin solid-angle theorem."""
import math
import random


def dot(u,v): return sum(x*y for x,y in zip(u,v))
def cross(u,v): return (u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
def norm(u): return math.sqrt(dot(u,u))
def difference(u,v): return tuple(x-y for x,y in zip(u,v))


def independent_angles(a,b,c):
    vertices=[(0.,0.,0.),(a,0.,0.),(a,b,0.),(a,b,c)]
    result=[]
    for i,v in enumerate(vertices):
        u,w,z=[difference(vj,v) for j,vj in enumerate(vertices) if j!=i]
        numerator=abs(dot(u,cross(w,z)))
        denominator=norm(u)*norm(w)*norm(z)+dot(u,w)*norm(z)+dot(w,z)*norm(u)+dot(z,u)*norm(w)
        result.append(2*math.atan2(numerator,denominator))
    return result


def stated_angles(a,b,c):
    E=math.sqrt(a*a+b*b+c*c)
    D_a=math.hypot(a,b);D_c=math.hypot(c,b)
    return [2*math.atan(b*c/((a+D_a)*(D_a+E))),math.atan(c/b),math.atan(a/b),
            2*math.atan(b*a/((c+D_c)*(D_c+E)))]


def half_tangent_on_symmetric_path(t):
    r=math.sqrt(1+t*t);q=math.sqrt(2+t*t)
    return t/((1+r)*(r+q))


def log_derivative(t):
    return (math.sqrt(2+t*t)-t*t)/(t*math.sqrt(1+t*t)*math.sqrt(2+t*t))


if __name__=='__main__':
    random.seed(991213)
    optimum=2*math.atan(math.sqrt(2)/(5+3*math.sqrt(3)))
    assert abs(optimum-0.27564279921626544)<1e-14
    count=0
    for k in range(20000):
        a=math.exp(random.uniform(-4,4)); b=math.exp(random.uniform(-4,4)); c=math.exp(random.uniform(-4,4))
        observed=independent_angles(a,b,c)
        formula=stated_angles(a,b,c)
        assert max(abs(x-y) for x,y in zip(observed,formula))<3e-10,(a,b,c,observed,formula)
        assert min(formula)<=optimum+2e-11,(a,b,c,formula,optimum)
        count+=1
    for k in range(1000):
        t=math.exp(random.uniform(-6,6))
        h=1e-5*t
        empirical=(math.log(half_tangent_on_symmetric_path(t+h)) - math.log(half_tangent_on_symmetric_path(t-h)))/(2*h)
        assert abs(empirical-log_derivative(t))<2e-5,(t,empirical,log_derivative(t))
        assert half_tangent_on_symmetric_path(t)<=half_tangent_on_symmetric_path(math.sqrt(2))+1e-13
        count+=1
    a=1.;b=math.sqrt(2);c=1.
    exact_angles=stated_angles(a,b,c)
    assert abs(min(exact_angles)-optimum)<1e-14
    assert exact_angles[1]>optimum and exact_angles[2]>optimum
    print('ORTHOSCHEME_MAXIMIN_OK',count,'sharp_min_steradians',format(optimum,'.16f'))
