"""Independent finite checks for the cone-directed three-cylinder packing law.
Finite floating-point checks are diagnostic; the proof is analytical.
"""
import math


def dot(a, b): return sum(x*y for x, y in zip(a, b))
def sub(a, b): return tuple(x-y for x, y in zip(a, b))
def add(a, b): return tuple(x+y for x, y in zip(a, b))
def mul(t, a): return tuple(t*x for x in a)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def norm(a): return math.sqrt(dot(a,a))
def unit(a): return mul(1/norm(a),a)

k_star=(7+math.sqrt(17))/16

def dual(a,k):
    b=1-2*a
    return a*math.sqrt(2-2*k)+2*math.sqrt(a*a+b*b+2*k*a*b)

def optimum(c):
    k=(1-3*c*c)/(1+3*c*c)
    q=math.sqrt(2-2*k)
    if k>=k_star:
        a=.5
        g=1+q/2
    else:
        a=(2-k-(1-k)*math.sqrt((1+k)/(9-7*k)))/(5-4*k)
        g=(q*(2-k)+math.sqrt(2*(1-k*k)*(9-7*k)))/(5-4*k)
    return k,q,g,a

def golden(f,lo=0.,hi=.5):
    h=(math.sqrt(5)-1)/2
    x1=hi-h*(hi-lo); x2=lo+h*(hi-lo)
    y1=f(x1); y2=f(x2)
    for i in range(100):
        if y1<y2:
            hi=x2; x2=x1; y2=y1; x1=hi-h*(hi-lo); y1=f(x1)
        else:
            lo=x1; x1=x2; y1=y2; x2=lo+h*(hi-lo); y2=f(x2)
    return f((lo+hi)/2)

count=0
for ii in range(1001):
    c=0.0001+ii*(.9998/1000)
    k,q,g,a=optimum(c)
    assert -0.5<k<1 and 0<a<=.5
    assert abs(dual(a,k)-g)<3e-12
    assert abs(golden(lambda x:dual(x,k))-g)<3e-12
    v=[(math.sqrt(1-c*c)*math.cos(2*math.pi*j/3),
        math.sqrt(1-c*c)*math.sin(2*math.pi*j/3),c) for j in range(3)]
    w=[unit(cross(v[j],v[(j+1)%3])) for j in range(3)]
    for j in range(3):
        assert abs(dot(w[j],w[(j+1)%3])-k)<1e-12
    b=1-2*a
    xm=[unit(add(mul(a,w[0]),mul(b,w[2]))),unit(sub(w[1],w[0])),
        unit(mul(-1,add(mul(a,w[1]),mul(b,w[2]))))]
    xp=[unit(sub(w[j],w[(j-1)%3])) for j in range(3)]
    dm=[dot(sub(xm[j],xm[(j+1)%3]),w[j]) for j in range(3)]
    dp=[dot(sub(xp[j],xp[(j+1)%3]),w[j]) for j in range(3)]
    assert min((dm[0],dm[1],-dm[2]))>=g-2e-12
    assert min(dp)>=q-2e-12
    for j in range(3):
        assert abs(norm(xm[j])-1)<1e-12
        assert abs(dot(xm[j],v[j]))<1e-12
    assert (g>q)==(k>0), (c,k,g,q)
    if k>k_star+1e-7:
        assert -dm[2]>g+1e-8, (c,k,g,dm)
    if k<k_star-1e-7:
        assert abs(-dm[2]-g)<2e-12
    count+=1

# Endpoint and transition checks
assert abs(optimum(1/math.sqrt(3))[1]-math.sqrt(2))<1e-13
assert abs(optimum(0)[2]-1)<1e-13
cstar=math.sqrt((1-k_star)/(3*(1+k_star)))
assert abs(optimum(cstar)[0]-k_star)<1e-13
print('PASS',count,'cone values: dual minimizer, explicit primal configurations, signs, contacts, and transitions')
print('contact threshold c_star =',repr(cstar))
print('R(perpendicular axes) =',repr(1+math.sqrt(2)))
