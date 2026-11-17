"""Standalone numerical checks for the cone-apex clique laws.

Run with: python3 cone_apex_cliques_check.py
Only Python 3 standard-library modules are needed. Finite sampling supports,
but does not prove, the infinite-n Poisson result.
"""
import bisect
import itertools
import math
import random

RNG = random.Random(19052013)


def successful(angles, cone_angle):
    a = sorted(angles)
    gaps = [a[j + 1] - a[j] for j in range(len(a) - 1)]
    gaps.append(cone_angle - a[-1] + a[0])
    return min(gaps) > math.pi


def slow_count(angles, cone_angle, k):
    return sum(successful(t, cone_angle) for t in itertools.combinations(angles, k))


def sparse_count(angles, cone_angle, k):
    a = sorted(angles)
    delta = cone_angle - k * math.pi
    if delta <= 0:
        return 0
    n = len(a)
    twice = a + [x + cone_angle for x in a]
    count = 0
    for i, origin in enumerate(a):
        windows = []
        for j in range(1, k):
            lo = origin + j * math.pi
            left = bisect.bisect_left(twice, lo)
            right = min(bisect.bisect_right(twice, lo + delta), i + n)
            windows.append(range(left, right))
        for indices in itertools.product(*windows):
            points = [origin] + [twice[j] for j in indices]
            if all(points[j] - points[j - 1] > math.pi for j in range(1, k)) and origin + cone_angle - points[-1] > math.pi:
                count += 1
    assert count % k == 0
    return count // k


def uniform_points(n, angle):
    return [RNG.random() * angle for _ in range(n)]


for k in (3, 4, 5):
    theta = k * math.pi + 2.0
    trials = 150000
    observed = sum(successful(uniform_points(k, theta), theta) for _ in range(trials)) / trials
    expected = (2.0 / theta) ** (k - 1)
    sigma = math.sqrt(expected * (1.0 - expected) / trials)
    assert abs(observed - expected) < 6 * sigma + 0.0002, (k, observed, expected)
    print('fixed subset', k, 'observed', round(observed, 7), 'exact', round(expected, 7))

# Condition on success, then the normalized excess gaps are uniform on a simplex.
k = 3
theta = k * math.pi + 3.0
samples = []
for _ in range(220000):
    raw = uniform_points(k, theta)
    # Anchor at a fixed LABEL rather than the smallest azimuth:
    # smallest-azimuth anchoring introduces a seam-size bias.
    angles = sorted((x - raw[0]) % theta for x in raw)
    gaps = [angles[j + 1] - angles[j] for j in range(k - 1)] + [theta + angles[0] - angles[-1]]
    if min(gaps) > math.pi:
        samples.append((gaps[0] - math.pi) / 3.0)
m1 = sum(samples) / len(samples)
m2 = sum(v * v for v in samples) / len(samples)
assert abs(m1 - 1/3) < 0.02, m1
assert abs(m2 - 1/6) < 0.02, m2
print('conditional slack moments', len(samples), round(m1, 5), round(m2, 5))

# Shared-two-vertex probability for pairs of successful triples.
theta = 3 * math.pi + 2.0
delta = 2.0
q = 2 * delta ** 3 / (3 * theta ** 3)
trials = 200000
both = 0
for _ in range(trials):
    z = uniform_points(4, theta)
    both += successful(z[:3], theta) and successful((z[0], z[1], z[3]), theta)
empirical = both / trials
assert abs(empirical - q) < 6 * math.sqrt(q / trials) + 0.00015
print('overlap probability', round(empirical, 6), round(q, 6))

for k in (3, 4):
    for n in (5, 7, 9):
        theta = k * math.pi + 1.0
        for _ in range(9):
            a = uniform_points(n, theta)
            assert sparse_count(a, theta, k) == slow_count(a, theta, k)
print('fast and exhaustive counters agree on all finite checks')

# Exact variance for three-apex cliques, independent of the radial distribution.
n = 11
theta = 3 * math.pi + 3.0
p = (3.0 / theta) ** 2
q = 2 * 3.0 ** 3 / (3 * theta ** 3)
mean = math.comb(n, 3) * p
variance = math.comb(n, 3) * p * (1-p) + 2 * math.comb(n, 2) * math.comb(n-2, 2) * (q - p*p)
values = [sparse_count(uniform_points(n, theta), theta, 3) for _ in range(2200)]
observed_mean = sum(values) / len(values)
observed_variance = sum((v-observed_mean)**2 for v in values) / len(values)
assert abs(observed_mean - mean) < 6 * math.sqrt(variance / len(values))
assert abs(observed_variance - variance) < 0.25 * variance
print('triple count mean/variance', tuple(round(t, 4) for t in (observed_mean,mean,observed_variance,variance)))

for k, n, trials in ((3, 180, 950), (4, 1000, 280)):
    c = (math.factorial(k) * (k * math.pi) ** (k-1)) ** (1/(k-1))
    theta = k * math.pi + c * n ** (-k/(k-1))
    lamb = math.comb(n, k) * ((theta-k*math.pi)/theta)**(k-1)
    observed = [sparse_count(uniform_points(n, theta),theta,k) for _ in range(trials)]
    m = sum(observed)/trials
    assert abs(m-lamb)<0.35, (k,m,lamb)
    # Total-variation convergence is asymptotic; finite k=4 samples cluster noticeably.
    print('critical window',k,n,'observed mean',round(m,4),'exact mean',round(lamb,4),
          'zero frequency',round(observed.count(0)/trials,4),'Poisson zero target',round(math.exp(-lamb),4))
print('CONE_APEX_CLIQUE_CHECKS_OK')
