---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The two Weyl-covariant orthonormal blocks give complementary 1±σ(C) eigenvalues. For leakage T=(I−P)W_w|_{E_m}, unitarity gives C*C=I−T*T; positivity at w≠0 also follows because a nontrivial exponential times a polynomial cannot be a polynomial. Rotate to a=|w|. Expanding the displaced monomials directly gives the leakage coefficients a^{k−j}(sqrt(k!/j!)/(k−j)!+O(a²)) for k≥m>j. In exterior order r, the unique lowest possible minor takes the first r rows and last r columns, with exponent r². Multiplying reciprocal-factorial rows by (r+i)! changes them to monic falling factorial polynomials, giving the Vandermonde and positive D_{m,r}. For complex a near zero, e^{az}(z−a)^j e^{−a²/2} and its local derivatives are dominated in Fock norm by a polynomial times e^{R|z|} for bounded |a|. This gives a norm-analytic finite family, then a Hilbert–Schmidt analytic exterior map; after removing the unique leading entry, the rest has Hilbert–Schmidt norm O_m(a^{r²+1}). The leading entry's own even correction and the squared Hilbert–Schmidt bound give the relative O_m(a²) for the product of the first r singular values. Taking ratios gives powers 2r−1 for T and 4r−2 for the small Gram eigenvalues. Cancelling the products gives the stated extremal constants. The independent 110-digit full Gram diagonalization by direct Taylor coefficient construction for m=1..6 and a=0.01,0.02 confirmed all tested coefficients to within 0.00060 relative error and checked pairing (python3 /workspace/reviews/evidence/reproduce.py 5, requires mpmath).

## originality

FAIL

Exact coverage in a distinct indexed finding, SCOPE-20261108-6b173840b97e. It gives the identical normalized Gram hierarchy for every fixed m, every channel and the same relative error, as well as the same least-eigenvalue coefficient and a stronger relative-error form for the condition number. Its block reduction also gives exact pairing. There is no distinct residual claim in the frozen Finding. The other entry is catalogued later than this frozen entry; the failure is for demonstrated equivalent coverage in the catalogue, not a claim of earlier publication, authorship, or derivation from the later entry.

## value

PASS

As mathematics, the fixed-m two-site spectrum quantifies conditioning channel by channel and supplies the sharp worst-direction constant, beyond a qualitative separation requirement. This is substantive spectral information, not a normalization check or a small special-case census. This assessment of the theorem's mathematical utility does not credit an equivalent record as a second original contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
