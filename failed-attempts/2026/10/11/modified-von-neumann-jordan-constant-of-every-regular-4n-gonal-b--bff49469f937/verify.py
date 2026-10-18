import math

def polygon_norm(z,N):
    x,y=z
    return max(
        x*math.cos(2*math.pi*j/N)+y*math.sin(2*math.pi*j/N)
        for j in range(N)
    )

def radial_unit(theta,N):
    # For the inradius-one polygon, the radial boundary is found by scaling a Euclidean unit direction.
    u=(math.cos(theta),math.sin(theta))
    q=polygon_norm(u,N)
    return (u[0]/q,u[1]/q)

for N in (4,8,12,16,20,24,32,40):
    assert N%4==0
    alpha=math.pi/N
    R=1/math.cos(alpha)

    x=(R*math.cos(alpha), R*math.sin(alpha))
    y=(R*math.cos(alpha),-R*math.sin(alpha))
    assert abs(polygon_norm(x,N)-1)<2e-12
    assert abs(polygon_norm(y,N)-1)<2e-12

    A=polygon_norm((x[0]+y[0],x[1]+y[1]),N)
    B=polygon_norm((x[0]-y[0],x[1]-y[1]),N)
    target=1/(math.cos(alpha)**2)
    quotient=(A*A+B*B)/4
    assert abs(A-2)<3e-12
    assert abs(B-2*math.tan(alpha))<3e-12
    assert abs(quotient-target)<4e-12

    # Deterministic boundary stress test of the global upper bound.
    pts=[radial_unit(2*math.pi*k/720,N) for k in range(720)]
    # Pair every sampled direction with a deterministic collection of offsets.
    for k,p in enumerate(pts):
        for off in (0,1,7,23,91,179,180,271,359):
            q=pts[(k+off)%len(pts)]
            plus=(p[0]+q[0],p[1]+q[1])
            minus=(p[0]-q[0],p[1]-q[1])
            val=(polygon_norm(plus,N)**2+polygon_norm(minus,N)**2)/4
            assert val<=target+2e-11,(N,k,off,val,target)

# Low-order exact-form numerical identities.
assert abs(1/math.cos(math.pi/8)**2-(4-2*math.sqrt(2)))<2e-14
assert abs(1/math.cos(math.pi/12)**2-(8-4*math.sqrt(3)))<2e-14

print("VERIFY_OK N=4,8,12,16,20,24,32,40 formula=Cprime_NJ=sec^2(pi/N)")
