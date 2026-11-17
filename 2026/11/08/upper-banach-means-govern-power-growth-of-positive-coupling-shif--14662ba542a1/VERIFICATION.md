---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The positive diagonal coupling  T=[S D_c;0 S*]  has exact power upper-right block H_n=sum_{j=0}^{n-1} S^{n-1-j}D_c(S*)^j. Its nonnegative row and column sums each run over at most n consecutive c entries, so Schur gives ||H_n||<=b_n=sup_m sum_{j=0}^{n-1}c_{m+j}. The b_n are subadditive (finite, nM bounded); thus beta=lim b_n/n=inf b_n/n. For any fixed n choose near-optimal long windows length L; flat normalized vectors in an L+O(n) window give ||H_n||>=n(b_L-1-3nM)/sqrt((L+2n+1)(L-2n)), hence ||H_n||>=n beta. Triangular scalar majorant gives ||T^n||<=(b_n+sqrt(b_n^2+4))/2. Combining and dividing by n gives lim ||T^n||/n=beta for every bounded sequence 0<c_j<=M (no uniform positive lower bound). The inverse is x=S*u-S*D_c S v, y=S v+(u_0/c_0)e_0; S*D_c e_0=0 makes the omitted scalar term vanish. For constant t, flat vectors far from boundary saturate the majorant, giving ||T^n||=(nt+sqrt(n^2t^2+4))/2. Independently constructed finite-section matrix products matched H_n, Schur bounds and upper majorants for 20 cases; 12 truncated constant-coupling norms approached (not equaled) the infinite formula. Finite sections do NOT certify the infinite limit; the analytic arbitrary-L lower bound does.

## originality

PASS

Best-of-knowledge searches and original theorem-level readings distinguish the claim from the Ji-Wang positive-coupling invertibility/invariant-subspace theorem, Garcia's exact Foguel norm formula and sharp uniform-in-c power bound (oppositely oriented blocks), and the same-day single-power singular-spectrum result. None supplies the exact beta(c) moving-window asymptotic for every nonuniform positive c. This is not a universal originality guarantee.

## value

PASS

The exact upper Banach mean controls the natural linear growth invariant of all bounded positive diagonal shift couplings. It rigorously classifies sublinear power growth versus long high-coupling windows, including sparse large entries, and refines the classical uniform ||c||∞ power bound. The precise asymptotic coefficient is independently useful within a motivated invertible Cowen–Douglas block family rather than an arbitrary finite parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
