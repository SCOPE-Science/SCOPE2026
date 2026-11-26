"""Independent numerical checks for ideal regular hyperbolic polygon side slimness."""
import cmath, math

def signed_sinh_distance(z, c, radius):
    return abs(1 + abs(z)**2 - 2*(c.conjugate()*z).real)/((1-abs(z)**2)*radius)

def test(n, resolution=401):
    theta = math.pi/n
    center = 1/math.cos(theta)
    radius = math.tan(theta)
    middle = center-radius
    predicted = 2*math.cos(theta)
    mid_distances = [signed_sinh_distance(middle, center*cmath.exp(2j*k*theta), radius) for k in range(1,n)]
    assert abs(min(mid_distances)-predicted)<5e-10
    for k, s in enumerate(mid_distances,1):
        expected = predicted*(math.sin(k*theta)/math.sin(theta))**2
        assert abs(s-expected)<1e-7*max(1,s)
    observed = 0.0
    for j in range(resolution):
        t=(j+0.5)/resolution
        angle=(math.pi/2+theta)*(1-t)+(3*math.pi/2-theta)*t
        z=center+radius*cmath.exp(1j*angle)
        vals=[signed_sinh_distance(z,center*cmath.exp(2j*k*theta),radius) for k in range(1,n)]
        observed=max(observed, math.asinh(min(vals)))
    assert observed<=math.asinh(predicted)+1e-7
    assert math.asinh(predicted)-observed<2e-4
    return math.asinh(predicted),observed

if __name__=='__main__':
    for n in [3,4,5,6,7,8,10,12,20,32,64]:
        a,b=test(n)
        print(n,format(a,'.12f'),format(b,'.12f'))
    print('PASS')
