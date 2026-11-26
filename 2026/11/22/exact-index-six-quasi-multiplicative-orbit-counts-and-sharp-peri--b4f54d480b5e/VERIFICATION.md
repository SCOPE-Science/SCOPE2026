---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The exponents of an exact-index-six function have a common residue r modulo s; bijectivity on the cosets implies gcd(r,s)=1. A unit exponent normalizes r to 1 modulo s, and output scaling normalizes F(1)=1. Writing the normalized function on nonzero inputs as x times a profile on the sixth roots gives the permutation test j+H_j mod 6 and residual maps H'_j=ksj+H_{t+(1+ks)j}-H_t modulo 6s. By the invertible sixth-root evaluation transform, support in one class c modulo d amounts to H_{j+6/d}-H_j=cs(6/d) modulo 6s. The characters are disjoint for a given d, and the joint failures for d=2,3 are exactly the d=6 term; inclusion-exclusion and Burnside therefore count exact index six. Independently reproduced the integer sums by solving both families of edge constraints on the full six-vertex profile graph modulo 6s, propagating affine offsets in H_t on spanning forests and counting permitted component offsets, not by invoking the supplied quotient-cycle code. `python3 /workspace/reproductions/index6.py 7` matched the six frozen rational expressions at all 72 interpolation primes, 12 further primes, and 8 nonprime prime powers. Fan's Theorem 4.5 makes six distinct matches per residue a polynomial identity, not empirical extrapolation. For period T, pairs of residues modulo 12 congruent modulo gcd(T,12) can be joined to one admissible residue modulo T by avoiding the single forbidden class at each prime p>=5 dividing T. Both CRT progressions then have infinitely many primes by Dirichlet, forcing equality of their polynomials. The 0-versus-6 and 0-versus-4 differences exclude all proper gcds, so 12 is minimal on the actual domain.

## originality

PASS

The supported contribution is the evaluated index-six coefficient polynomials together with sharpness of the period on prime-power inputs. Fan already gives the normalization, finite counting machinery and the upper period/degree bounds; no novelty is credited for those. The available exact source and indexed comparisons do not give the evaluated coefficient data or the period obstruction.

## value

PASS

Index six is the first squarefree composite index and the first such test of the even-index bound. The result supplies usable coefficients for the entire arithmetic family and shows that the bound remains sharp after restricting to genuine finite fields. This is a motivated sharpness witness, not just sample counts or substituting six into a known period bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
