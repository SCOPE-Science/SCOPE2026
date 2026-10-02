from math import sqrt

def K(r):
    states = (-1, 1)
    return states, [[(1 + r*u*v)/2 for v in states] for u in states]

def kron(A, B):
    return [[a*b for a in rowa for b in rowb] for rowa in A for rowb in B]

def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def matpow(A, k):
    n = len(A)
    R = [[float(i == j) for j in range(n)] for i in range(n)]
    B = [row[:] for row in A]
    while k:
        if k & 1:
            R = matmul(R, B)
        B = matmul(B, B)
        k //= 2
    return R

def corr_uniform(P, f, k):
    m = len(f)
    Pk = matpow(P, k)
    mean = sum(f)/m
    var = sum((x-mean)**2 for x in f)/m
    cov = sum((f[i]-mean)*Pk[i][j]*(f[j]-mean)
              for i in range(m) for j in range(m))/m
    return cov/var

def psi(n, t):
    return 1 + 2*sum((1-k/n)*(t**k) for k in range(1, n))

rho = 0.3
beta = 0.8

_, Kb = K(beta)
_, K0 = K(0.0)
P = kron(Kb, K0)
states = list(__import__("itertools").product((-1, 1), repeat=2))
a = sqrt(rho/beta)
b = sqrt(1-rho/beta)
f = [a*u + b*v for u, v in states]

print("rho =", rho, "beta =", beta)
for k in range(1, 7):
    got = corr_uniform(P, f, k)
    want = rho*(beta**(k-1))
    print("lag", k, "computed", f"{got:.12f}", "formula", f"{want:.12f}")
    assert abs(got-want) < 1e-11

for n in (2, 3, 5, 20):
    lower = psi(n, rho)
    upper = 1 + (rho/beta)*(psi(n, beta)-1)
    direct = 1 + 2*sum((1-k/n)*corr_uniform(P, f, k) for k in range(1, n))
    print("n", n, "lower", f"{lower:.12f}", "upper", f"{upper:.12f}",
          "upper-construction", f"{direct:.12f}")
    assert abs(direct-upper) < 1e-10

iat_lower = (1+rho)/(1-rho)
iat_upper = 1 + 2*rho/(1-beta)
print("iat lower", f"{iat_lower:.12f}", "iat upper", f"{iat_upper:.12f}")

# Random finite spectral measures on [0,beta], conditioned to have mean rho
# by mixing an arbitrary measure with a point at 0 or beta.
import random
random.seed(20260920)
for _ in range(1000):
    xs = [random.random()*beta for _ in range(4)]
    ws = [random.random() for _ in xs]
    s = sum(ws)
    ws = [w/s for w in ws]
    m = sum(w*x for w,x in zip(ws,xs))
    if m < rho:
        q = (rho-m)/(beta-m)
        xs2, ws2 = xs+[beta], [(1-q)*w for w in ws]+[q]
    elif m > rho:
        q = (m-rho)/m
        xs2, ws2 = xs+[0.0], [(1-q)*w for w in ws]+[q]
    else:
        xs2, ws2 = xs, ws
    mean = sum(w*x for w,x in zip(ws2,xs2))
    assert abs(mean-rho) < 1e-12
    for k in range(1, 8):
        mk = sum(w*(x**k) for w,x in zip(ws2,xs2))
        assert rho**k - 1e-12 <= mk <= rho*(beta**(k-1)) + 1e-12
    tau = sum(w*(1+x)/(1-x) for w,x in zip(ws2,xs2))
    assert iat_lower - 1e-12 <= tau <= iat_upper + 1e-12

print("1000 randomized spectral-measure checks passed")
