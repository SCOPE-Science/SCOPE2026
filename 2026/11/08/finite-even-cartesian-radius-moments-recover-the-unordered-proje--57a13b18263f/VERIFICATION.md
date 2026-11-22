---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

Full proof reconstructed from seven actual frozen Git blobs. For finite unitary eigenphases, normal spectral calculus gives max |cos(t-alpha)| = cos(projective distance). Each cyclic gap of length ell contributes 2/pi integral_0^(ell/2) cos^p(x)dx, with m=1 singleton gap ell=pi. For p=2k, cos^(2k) binomial expansion gives M_k=4^(-k)C(2k,k)+2/(pi*4^k) sum_{j<=k} C(2k,k-j)s_j/j. The diagonal s_k coefficient is 2/(pi*4^k*k), nonzero. Chebyshev U_{j-1} maps s_j to polynomial moments of the positive at-most-n-atom measure sum sin(ell)delta_(cos ell). A difference of two such measures has <=2n nodes, so vanishing power moments degrees 0..2n-1 and invertible Vandermonde force equality. Dividing atom mass by sin(ell)>0 retrieves exact integer gap multiplicity. s1=0 iff projective singleton, including n=1. The explicit gap words (1,2,3,4) vs (1,3,2,4), scaled by pi/10, have equal multisets but are outside each other's dihedral orbit. A fresh independent vectorized 100001-midpoint phase-quadrature check of 28 even moments over five profiles m=1..5 gave maximum absolute error 8.90e-11; seven arbitrary-p gap-integral comparisons agreed to 1e-65. Numerical tests are diagnostic, not proof. A separate attempted high-precision brute quadrature timed out and contributes no evidence. Git tree SHA independently reconstructed from all seven fetched blob SHAs and matches the assignment.

## originality

PASS

Best-of-knowledge PASS with a material elementary-prior-method risk. The earlier October 11 projective-gap theorem supplies the exact p=2 forward integral and its proof already supplies the nearest-point gap geometry; Audeh–Kittaneh–Moradi–Sahoo define the entire Cartesian p family. Classical Prony uniqueness for finitely supported measures supplies the abstract inverse step. However none of the closely inspected prior mathematical statements provides the particular triangular conversion of the first 2n even operator radii into all 2n Chebyshev moments, followed by the explicit all-n repeated projective gap reconstruction and non-dihedral cyclic-order obstruction as one operator-radius identifiability theorem. This is a concise but nonidentical new synthesis; priority is not certified.

## value

PASS

Finite measurements resolving exactly what the newly defined unitary Cartesian-radius family can identify are a natural operator inverse problem. The theorem recovers continuous, arbitrarily repeated projective gap lengths uniformly for all matrix sizes up to n and demonstrates a sharp intrinsic cyclic-order information loss. The explicit spectral-geometric to finite-atomic-moment conversion is the useful object-specific step rather than a mere new norm inequality or arbitrary instance. The proof uses well-known Vandermonde/Prony ideas and does not establish optimality or conditioning; those are limits, not intrinsic reasons to deny this exact natural classification value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
