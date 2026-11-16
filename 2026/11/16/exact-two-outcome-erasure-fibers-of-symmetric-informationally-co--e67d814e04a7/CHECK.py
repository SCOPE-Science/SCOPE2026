"""Independent small-dimensional arithmetic/numerical sanity checks for a SIC two-erasure theorem.
The theorem for arbitrary dimensions is proved analytically in RESULT.md.
Requires numpy; run: python CHECK.py.
"""
import numpy as np

def check():
    d = 3
    omega = np.exp(2j * np.pi / 3)
    base = np.array([0, 1, -1], complex) / np.sqrt(2)
    vectors = [np.array([omega**(ell*j) * base[(j-k)%d] for j in range(d)])
               for k in range(d) for ell in range(d)]
    P = [np.outer(v, v.conj()) for v in vectors]
    G = np.array([[np.trace(A@B).real for B in P] for A in P])
    assert np.allclose(G, (d*np.eye(d*d)+np.ones((d*d,d*d)))/(d+1), atol=1e-12)
    H = P[0] - P[1]
    values, Q = np.linalg.eigh(H)
    assert np.allclose(values, [-np.sqrt(3/4),0,np.sqrt(3/4)], atol=1e-12)
    e_minus, e_plus = Q[:,0], Q[:,2]
    a = np.sqrt(0.2)
    b = np.sqrt(0.8)*np.exp(0.4j)
    psi = a*e_plus + b*e_minus
    phi = np.conj(b)*e_plus + np.conj(a)*e_minus
    probs = lambda x: np.array([np.vdot(x, A@x).real/d for A in P])
    first, other = probs(psi), probs(phi)
    assert np.max(np.abs(first[2:]-other[2:])) < 1e-12
    delta = np.abs(a)**2-np.abs(b)**2
    assert np.allclose(first[0]-other[0], delta/np.sqrt(d*(d+1)), atol=1e-12)
    assert np.allclose(first[1]-other[1], -delta/np.sqrt(d*(d+1)), atol=1e-12)
    chordal = np.sqrt(1 - abs(np.vdot(psi,phi))**2)
    assert np.allclose(chordal, abs(delta), atol=1e-12)
    D = lambda A: ((d+1)*A - np.eye(d))/d
    assert np.allclose(np.linalg.eigvalsh(D(P[0])+D(P[1])), [-2/3,0,4/3], atol=1e-12)
    print('CHECK_OK dimension=3 sic_gram=exact_to_roundoff retained_outcomes=7 exact_gap=verified chordal_relation=verified unnormalized_exception=verified')

if __name__ == '__main__':
    check()
