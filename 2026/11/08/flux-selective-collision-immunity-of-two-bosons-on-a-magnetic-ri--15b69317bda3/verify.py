"""Finite-dimensional checks for flux-selective two-boson collision loss.

Requires Python 3 and NumPy. The all-size statement follows from the
Fourier-sector proof, not from finite-dimensional computations.
"""
import math
import numpy as np


def operators(n, flux):
    shift = np.roll(np.eye(n, dtype=complex), 1, axis=0)
    hop = np.exp(1j * flux/n) * shift + np.exp(-1j * flux/n) * shift.conj().T
    ident = np.eye(n, dtype=complex)
    free = np.kron(hop, ident) + np.kron(ident, hop)
    exchange = np.zeros((n*n, n*n), dtype=complex)
    detector = np.zeros((n*n, n), dtype=complex)
    for x in range(n):
        detector[x*n+x, x] = 1
        for y in range(n):
            exchange[y*n+x, x*n+y] = 1
    sym = (np.eye(n*n) + exchange)/2
    common_shift = np.kron(shift, shift)
    return free, exchange, detector, sym, common_shift


def predicted(n, flux, sym, common_shift):
    root = np.exp(2j * math.pi/n)
    sector = [p for p in range(n) if abs(math.cos((flux-math.pi*p)/n)) < 1e-10]
    if not sector:
        return np.zeros_like(sym), None
    assert len(sector) == 1
    p = sector[0]
    projector = np.zeros_like(sym)
    power = np.eye(n*n, dtype=complex)
    for a in range(n):
        projector += root**(p*a) * power/n
        power = power @ common_shift
    d = np.zeros(n*n, dtype=complex)
    for x in range(n):
        d[x*n+x] = root**(p*x)/math.sqrt(n)
    return sym @ projector - np.outer(d,d.conj()), p


def symmetric_basis(n):
    columns = []
    for x in range(n):
        for y in range(x,n):
            v = np.zeros(n*n, dtype=complex)
            if x == y:
                v[x*n+x] = 1
            else:
                v[x*n+y] = v[y*n+x] = 1/math.sqrt(2)
            columns.append(v)
    return np.array(columns).T


def independent_dark_rank(free, detector, basis):
    # Diagonalize H restricted to the symmetric sector, group each real
    # eigenvalue, and subtract the rank of its collision-amplitude map.
    energy, eigvectors = np.linalg.eigh(basis.conj().T @ free @ basis)
    dark = 0
    start = 0
    while start < len(energy):
        end = start+1
        while end < len(energy) and abs(energy[end]-energy[start]) < 1e-8:
            end += 1
        collision = detector.conj().T @ basis @ eigvectors[:,start:end]
        singular = np.linalg.svd(collision,compute_uv=False)
        dark += (end-start) - sum(s>1e-8 for s in singular)
        start=end
    return dark


def main():
    tested = 0
    for n in range(3,11):
        basis = symmetric_basis(n)
        for flux in (0,math.pi/2,math.pi,3*math.pi/2,math.pi/3):
            free, exchange, detector, sym, common_shift = operators(n,flux)
            proj,p = predicted(n,flux,sym,common_shift)
            assert np.linalg.norm(proj-proj.conj().T) < 1e-8
            assert np.linalg.norm(proj@proj-proj) < 1e-8
            assert np.linalg.norm(free@proj) < 1e-8
            assert np.linalg.norm(detector.conj().T@proj) < 1e-8
            assert np.linalg.norm(exchange@proj-proj) < 1e-8
            dim = int(round(np.trace(proj).real))
            assert dim == independent_dark_rank(free,detector,basis), (n,flux,dim)
            gamma = np.diag([1+0.07*i for i in range(n)])
            loss = free - 0.5j * detector @ gamma @ detector.conj().T
            eig = np.linalg.eigvals(basis.conj().T @ loss @ basis)
            assert sum(abs(z.imag)<1e-8 for z in eig) == dim
            for x in range(n):
                e = np.zeros(n*n,complex)
                e[x*n+x]=1
                assert abs(np.vdot(e,proj@e)) < 1e-8
                for y in range(x+1,n):
                    v = np.zeros(n*n,complex)
                    v[x*n+y]=v[y*n+x]=1/math.sqrt(2)
                    expected=0 if p is None else (1+int(n%2==0 and y-x==n//2)*(-1)**p)/n
                    assert abs(np.vdot(v,proj@v).real - expected)<1e-8
            tested+=1
    print(f"PASS: {tested} ring/flux cases; all matrix and capture checks passed")

if __name__ == '__main__':
    main()
