"""Finite diagnostics for Fock Weyl coherent kernels and chirp spectral equality.

The analytic theorem, including the infinite-dimensional assertion, is proved
in RESULT.md; these tests do not provide an independent infinite proof.
"""
import cmath
import math

count = 0

def close(a, b, tol=4e-10):
    global count
    assert abs(a - b) <= tol * max(1.0, abs(a), abs(b)), (a, b)
    count += 1


def hdot(z, w):
    return sum(a * b.conjugate() for a, b in zip(z, w))


def norm2(z):
    return hdot(z, z).real


def mm(A, z):
    return [sum(row[j] * z[j] for j in range(len(z))) for row in A]


def add(x, y):
    return [a + b for a, b in zip(x, y)]


def k(z, w):
    return cmath.exp(hdot(z, w) - norm2(w) / 2)


def weight(A, b, z):
    return cmath.exp(-hdot(mm(A, z), b) - norm2(b) / 2)


def kcenter(A, b, w):
    return add(mm(A, w), b)


def adjoint_kernel_phase(A, b, w):
    return cmath.exp(1j * hdot(mm(A, w), b).imag)


def inner_coherent(x, y):
    return cmath.exp(hdot(y, x) - (norm2(x) + norm2(y)) / 2)


# A genuinely noncommuting pair of 2 x 2 unitary matrices.
A0 = [[1+0j, 0j], [0j, -1+0j]]
A1 = [[0j, 1+0j], [1+0j, 0j]]
A2 = [[0+1j, 0j], [0j, 1+0j]]
bs = [[0.24+0.31j, -0.4+0.12j], [0.63-0.07j, 0.29+0.44j], [-0.33+0.01j, -0.05-0.52j]]
As = [A0, A1, A2]
ws = [[(i-4)/7 + 1j*(j+1)/11, (j-3)/13+1j*(i+2)/9] for i in range(10) for j in range(9)]
zs = [[0.12+0.03j, 0.21-0.43j], [0.7-0.2j, -0.3+0.2j]]
for A, b in zip(As, bs):
    for w in ws:
        # Explicit action on normalized kernel as an entire function.
        phase = adjoint_kernel_phase(A, b, w)
        center = kcenter(A, b, w)
        # Gaussian coherent-state coefficient of W^*k_w.
        adj_scalar = weight(A, b, w).conjugate() * math.exp((norm2(center) - norm2(w))/2)
        close(phase, adj_scalar)
        close(abs(phase), 1)
        for z in zs:
            close(adj_scalar * k(z, center), phase * k(z, center))
for A, bi, bj in [(A0,bs[0],bs[1]), (A1,bs[0],bs[2])]:
    for w in ws:
        xi, xj = kcenter(A,bi,w), kcenter(A,bj,w)
        left = adjoint_kernel_phase(A,bi,w) * adjoint_kernel_phase(A,bj,w).conjugate() * inner_coherent(xi,xj)
        diff = [x-y for x,y in zip(bi,bj)]
        phase = 2 * hdot(mm(A,w),diff).imag + hdot(bj,bi).imag
        right = cmath.exp(-norm2(diff)/2 + 1j*phase)
        close(left,right)

# Every size is verified numerically, while the proof uses exact character sums.
for N in range(2,91):
    omega = cmath.exp(2j*math.pi/N)
    chirp = [cmath.exp(1j*math.pi*(j*j if N%2==0 else j*(j+1))/N) for j in range(N)]
    for h in range(N):
        corr = sum(chirp[(j+h)%N]*chirp[j].conjugate() for j in range(N))
        close(corr, N if h==0 else 0)
    for n in range(N):
        freq = sum(chirp[j]*omega**(j*n) for j in range(N))
        close(abs(freq)**2,N)
print(f"WEYL_FOCK_AFFINE_FINITE_DIAGNOSTIC_OK {count}")
