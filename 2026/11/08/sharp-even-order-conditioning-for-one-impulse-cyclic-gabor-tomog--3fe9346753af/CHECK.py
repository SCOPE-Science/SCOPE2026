"""Independent direct finite-sum checks of a cyclic Gabor minimax formula."""
import cmath
import math
import random


def direct_minimum(n, z):
    tau = 2.0 * math.pi / n
    v = [1.0 + z if j == 0 else 1.0 + 0j for j in range(n)]
    norm2 = sum(abs(a)**2 for a in v)
    minimum = float('inf')
    for u in range(n):
        for w in range(n):
            correlation = sum(v[(j+u)%n] * v[j].conjugate() * cmath.exp(-1j * tau*w*j)
                              for j in range(n))
            minimum = min(minimum, abs(correlation))
    return minimum / norm2


def branch_minimum(n, z):
    omega = cmath.exp(2j * math.pi/n)
    r = z.real
    nums = [n + abs(z)**2 + 2*r]
    nums += [abs(z)**2+2*r] * (n-1)
    nums += [n + 2*r] * (n-1)
    nums += [z + z.conjugate() * omega**(u*w)
             for u in range(1,n) for w in range(1,n)]
    return min(abs(a) for a in nums) / nums[0].real


def theorem(n):
    a = math.pi / (2*n)
    z = -math.sqrt(n)*cmath.exp(1j*a)
    return z, math.sin(a) / (math.sqrt(n)-math.cos(a))


def run():
    random.seed(2026)
    nc = ac = 0
    for n in (6,8,10,12,14,16,18,20):
        z, exact = theorem(n)
        direct = direct_minimum(n,z)
        assert abs(direct-exact) < 3e-12, (n,direct,exact)
        nc += 1
        for z2 in (z, z.conjugate(), -math.sqrt(n)*1j, 1.25+2.5j,
                   0.5 + 0.2j, 0j):
            d=direct_minimum(n,z2)
            b=branch_minimum(n,z2)
            assert abs(d-b)<3e-12, (n,z2,d,b)
            ac+=1
        # A two-parameter random sweep, tested against the claimed global optimum.
        for _ in range(160):
            r=math.exp(random.uniform(-1.7,1.7))*math.sqrt(n)
            theta=random.uniform(-math.pi,math.pi)
            z2=r*cmath.exp(1j*theta)
            assert branch_minimum(n,z2) <= exact + 5e-13, (n,z2)
            ac+=1
    print('CHECK_OK even_orders=%d direct_cases=%d random_phase_radius_cases=%d' %
          (nc,8*6,8*160))


if __name__=='__main__':
    run()
