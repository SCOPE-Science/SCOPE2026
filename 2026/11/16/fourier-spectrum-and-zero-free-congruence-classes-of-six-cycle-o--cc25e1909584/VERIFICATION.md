---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For all n>=3, an unoriented simple six-cycle in K_(3,n) corresponds uniquely (not twice) to an injection of its three column vertices into row pairs (12,13,23); there are n(n-1)(n-2) cycles. In a sign column x=ab,y=ac,z=bc with xyz=1, inclusion-exclusion of the three repeated-index loci in sum x_i y_j z_k proves W=XYZ-X²-Y²-Z²+2n. Four (x,y,z) types are equiprobable with 2 signs each, giving the exact 2^n multinomial spectral multiplicity. Each edge occurs 2(n-1)(n-2) times, even, hence W≡n(n-1)(n-2)≡2 (mod4) for n≡3 mod4. If n≡6 mod8, X,Y,Z even, half-sums have odd sum; both parity cases yield W≡8 (mod16), proving universal ν2=3. Independent 4-cell exact enumeration gave zero counts 0/64 at n3, 192/256 at n4, 240/1024 at n5 and no zeros at n6,7,11,14,15; checked universal congruence in n=3,6,7,10,11,14,15. The endpoint norm is E|W| under uniform column types; (X,Y,Z)/sqrt(n) tends to independent N(0,1), and bounded normalized sixth moments justify uniform integrability of |XYZ|/n^(3/2). The quadratic correction is O(n) in expectation, giving constant (2/pi)^(3/2). Finite samples are not the infinite proof.

## originality

PASS

PASS based on the exact signed six-cycle character distribution, two universal 2-adic classes, and sharp Gaussian endpoint constant; conventional graph-cycle dimension and finite-Fourier frameworks do not imply these specialized global statements.

## value

PASS

This is a natural family of graph cycles, not a handpicked small example. The full frequency multiplicity and two infinite invertibility regimes, with sharp all-size endpoint norm expressed as a finite exact sum and Gaussian n^(3/2) law, give nontrivial quantitative Fourier observability/stability information; neither follows from routine graph rank facts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
