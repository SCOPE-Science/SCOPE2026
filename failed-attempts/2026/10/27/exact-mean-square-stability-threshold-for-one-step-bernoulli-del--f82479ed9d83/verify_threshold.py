"""Exact rational spot checks for the Bernoulli-delay SGD stability theorem."""
from fractions import Fraction as F
from math import sqrt

def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def transpose(A):
    return [list(row) for row in zip(*A)]

def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]

def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]

def mscale(s, A):
    return [[s * A[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]

def covariance_matrix(mu, q):
    p = 1 - q
    return [
        [1 - 2*p*mu + p*mu*mu, -2*q*mu, q*mu*mu],
        [1 - p*mu, -q*mu, F(0)],
        [F(1), F(0), F(0)],
    ]

def characteristic_coefficients(mu, q):
    a = (mu - 1) * (mu*q - mu + 1)
    b = mu*q*(mu*mu*q - mu*mu - mu + 1)
    c = -mu**3*q**2
    return a, b, c

def certificate(mu, q):
    s = 2 - mu - q*mu*mu
    P = [
        [2*(1+q*mu)/(mu*s), -2*q/s],
        [-2*q/s, (2*mu*mu*q*q - mu*mu*q + 2*mu*q - mu + 2)/s],
    ]
    A0 = [[1-mu, F(0)], [F(1), F(0)]]
    A1 = [[F(1), -mu], [F(1), F(0)]]
    EATPA = madd(mscale(1-q, matmul(matmul(transpose(A0), P), A0)),
                  mscale(q, matmul(matmul(transpose(A1), P), A1)))
    I = [[F(1), F(0)], [F(0), F(1)]]
    assert msub(P, EATPA) == I
    detP = P[0][0]*P[1][1] - P[0][1]*P[1][0]
    assert s > 0 and P[0][0] > 0 and detP > 0
    return s, P, detP

def polynomial_at(r, mu, q):
    a, b, c = characteristic_coefficients(mu, q)
    return r**3 + a*r**2 + b*r + c

# Stable points, including both endpoint delay laws and an interior mixture.
for q, mu in [(F(0), F(1)), (F(1), F(1, 2)), (F(1, 2), F(6, 5))]:
    s, P, detP = certificate(mu, q)
    a, b, c = characteristic_coefficients(mu, q)
    assert polynomial_at(F(1), mu, q) == mu*s
    print(f"stable certificate: q={q}, mu={mu}, s={s}, det(P)={detP}")

# An unstable rational point just above the q=1/2 boundary.
q, mu = F(1, 2), F(5, 4)
s = 2 - mu - q*mu*mu
assert s < 0
assert polynomial_at(F(1), mu, q) < 0
assert polynomial_at(F(2), mu, q) > 0
print(f"unstable witness: q={q}, mu={mu}, s={s}, p(1)={polynomial_at(F(1),mu,q)}, p(2)={polynomial_at(F(2),mu,q)}")

print(f"boundary q=1/2: mu*=sqrt(5)-1={sqrt(5)-1:.12f}")
print("PASS: exact rational Lyapunov identities and instability sign witness verified.")
