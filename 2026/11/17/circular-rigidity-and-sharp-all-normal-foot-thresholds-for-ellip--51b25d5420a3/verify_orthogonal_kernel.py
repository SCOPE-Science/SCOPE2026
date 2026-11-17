"""Finite standard-library regression checks for normal-foot feasibility."""
import math


def threshold(n):
    if n == 4:
        return math.inf
    x = math.pi / n
    return math.sqrt(min(math.tan((2*j+2)*x)/math.tan((2*j+1)*x)
                         for j in range(n//4+1) if (2*j+2)*x < math.pi/2 - 1e-12))


def center_feasible_direct(n, a, b):
    xy = [(a*math.cos(2*math.pi*j/n), b*math.sin(2*math.pi*j/n)) for j in range(n)]
    for j in range(n):
        u, v = xy[j], xy[(j+1)%n]
        d = (v[0]-u[0], v[1]-u[1])
        dot = -u[0]*d[0]-u[1]*d[1]
        length2 = d[0]*d[0]+d[1]*d[1]
        if not 0 < dot < length2:
            return False
    return True


def ellipse_residual(a, b, theta):
    s, c = math.sin(theta), math.cos(theta)
    return abs((a*a-b*b)*s*c)/math.hypot(a*s, b*c)


def main():
    checks = 0
    for n in range(4, 202, 2):
        r = threshold(n)
        assert r > 1
        for ratio in ([1, 1.2, 2, 4, 10] if n == 4 else
                      [1, 1+(r-1)*.1, 1+(r-1)*.5, 1+(r-1)*.98, r*1.02, r*1.2]):
            assert center_feasible_direct(n, ratio, 1) == (ratio < r)
            checks += 1
    for n, expected in [(6, math.sqrt(3)), (8, math.sqrt(1+math.sqrt(2))),
                        (10, 5**.25)]:
        assert abs(threshold(n)-expected) < 1e-12
        checks += 1
    for a, b in [(1, 1), (2, 1), (4, 3), (5, 2)]:
        best = max(ellipse_residual(a,b, j*2*math.pi/120000)
                   for j in range(120000))
        assert abs(best-(a-b)) < 1e-7
        checks += 1
    for n in (200, 400, 800, 1600, 3200):
        assert abs(n*(threshold(n)-1)-math.pi) < 0.1
        checks += 1
    print('PASS:', checks, 'finite regression checks')


if __name__ == '__main__':
    main()
