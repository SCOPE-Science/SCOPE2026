"""Independent geometric section-checks of explicit planar Fourier-mean identities.
Python 3 standard library only; tests do not replace the analytic theorem.
"""
import math

def sectional_jumps(vertices, u):
    """Find projected knots and derivative jumps from intersections, not Fourier sums."""
    n = len(vertices)
    tangent = (-u[1], u[0])
    levels = sorted(set(round(x*u[0] + y*u[1], 12) for x, y in vertices))
    chords = []
    for h in levels:
        crossings = []
        for j in range(n):
            a, b = vertices[j], vertices[(j + 1) % n]
            da, db = a[0]*u[0] + a[1]*u[1], b[0]*u[0] + b[1]*u[1]
            if abs(db-da) < 1e-13:
                continue
            v = (h-da)/(db-da)
            if -1e-10 <= v <= 1+1e-10:
                z = (a[0] + v*(b[0]-a[0]), a[1] + v*(b[1]-a[1]))
                crossings.append(z[0]*tangent[0] + z[1]*tangent[1])
        chords.append(max(crossings)-min(crossings) if crossings else 0.)
    slopes = [(chords[j+1]-chords[j])/(levels[j+1]-levels[j]) for j in range(len(levels)-1)]
    jumps = [slopes[0]] + [slopes[j]-slopes[j-1] for j in range(1, len(slopes))] + [-slopes[-1]]
    assert abs(sum(jumps)) < 1e-7
    assert abs(sum(jumps[j]*levels[j] for j in range(len(levels)))) < 1e-7
    return levels, jumps

def rho3(vertices, u, area):
    levels, jumps = sectional_jumps(vertices, u)
    energy = sum(c*d*abs(x-y) for x,c in zip(levels,jumps) for y,d in zip(levels,jumps))
    return -3*math.pi*energy/(2*area)

def rho2(vertices, u, area):
    levels, jumps = sectional_jumps(vertices, u)
    terms = [c*d*(x-y)**2*math.log(abs(x-y)) for x,c in zip(levels,jumps) for y,d in zip(levels,jumps) if abs(x-y)>1e-10]
    return sum(terms)/area

def close(a,b,tol=1e-8):
    assert abs(a-b) < tol*max(1,abs(b)), (a,b)

square = [(-1,-1),(1,-1),(1,1),(-1,1)]
triangle = [(0,0),(2,0),(0,1)]
u = (2**-0.5,2**-0.5)
# Each expected value is independently obtained from direct product/integration
# of a Fourier transform: square 8 sin^2(r/sqrt(2))/r^2,
# triangle 8 sin^2(r/(2 sqrt(2)))/r^2.
close(rho3(square,u,4), 6*math.pi*math.sqrt(2))
close(rho3(triangle,u,1),12*math.pi*math.sqrt(2))
close(rho2(square,u,4),16*math.log(2))
close(rho2(triangle,u,1),16*math.log(2))
# General rectangular diagonal p=3 and the exact facet-normal horn constant.
for theta in (0.2,0.1,0.03,0.01,0.003,0.001):
    unit=(math.sin(theta),math.cos(theta))
    close(rho3(square,unit,4),3*math.pi/(math.cos(theta)**2*math.sin(theta)),2e-7)
# Predicted horn: square constant 3*pi, triangle constant 6*pi.
for vertices,area,constant in [(square,4,3*math.pi),(triangle,1,6*math.pi)]:
    theta=1e-4
    value=theta*rho3(vertices,(math.sin(theta),math.cos(theta)),area)
    assert abs(value-constant)/constant < 5e-3, (value,constant)
print('GEOMETRIC_FOURIER_POLYGON_CHECKS_OK 12')
