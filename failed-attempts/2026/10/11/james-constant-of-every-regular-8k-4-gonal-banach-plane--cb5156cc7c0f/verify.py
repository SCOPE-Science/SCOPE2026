from fractions import Fraction
import math

def reg_norm(z,N):
    x,y=z
    return max(
        x*math.cos(2*math.pi*j/N)+y*math.sin(2*math.pi*j/N)
        for j in range(N)
    )

def vertex(theta,N):
    R=1/math.cos(math.pi/N)
    return (R*math.cos(theta),R*math.sin(theta))

# Exact arithmetic check of the residue-class index identities.
for k in range(1001):
    N=8*k+4
    assert Fraction(2*k+1,N)==Fraction(1,4)
    assert N%4==0
    assert N//4==2*k+1

# Reconstruct representative norms and the explicit equality pair.
for N in (4,12,20,28,36,44,52):
    theta=math.pi/4
    x=vertex(theta,N)
    y=vertex(theta+math.pi/2,N)
    A=reg_norm((x[0]+y[0],x[1]+y[1]),N)
    B=reg_norm((x[0]-y[0],x[1]-y[1]),N)
    target=math.sqrt(2)/math.cos(math.pi/N)
    assert abs(reg_norm(x,N)-1)<1e-12
    assert abs(reg_norm(y,N)-1)<1e-12
    assert abs(A-target)<2e-12
    assert abs(B-target)<2e-12

# Exact dodecagonal radical identity, checked after squaring.
# [sqrt(2) sec(pi/12)]^2 = 8/(2+sqrt(3)) = 16-8sqrt(3)
# [2(sqrt(3)-1)]^2 = 16-8sqrt(3).
lhs=math.sqrt(2)/math.cos(math.pi/12)
rhs=2*(math.sqrt(3)-1)
assert abs(lhs-rhs)<1e-14

print("VERIFY_OK residue=N_mod_8_eq_4 samples=7 dodecagon=2(sqrt3-1)")
