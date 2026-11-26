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

The frozen text promises all real-even optimizers but gives only one at even N; already 1+cos(3θ) is another. The value T_N=2 was not in error. The repaired RESULT.md supplies the entire even face and specifies odd-only uniqueness. In both ranges real-part averaging preserves mass and feasibility, reducing the complex value to the two real-even Fourier coefficients. For even N the j=N/2 bound forces a+b=1/2 at equality; the polynomial then factors as (1+x)[1−8b x(1−x)]. At x=±1 there is no further constraint. On all other sampled x the extrema of x(1−x) are −c(1+c), with c=cos(2π/N), and the positive grid maximum G_N. These give the necessary and sufficient b interval in the repair. For odd N the cubic roots are −C,u,w. Direct angle comparisons place u,w in consecutive grid gaps, with both endpoints sampled in the residue class N≡3 mod 6; there are no sample points strictly between u and w. This gives feasibility. The two active rows (u,4u³−3u) and (−C,−cos(3δ)) have nonzero determinant and a positive linear combination equal to (−1,−1). Thus equality is attained by the displayed polynomial and fixes its two coefficients uniquely. The strict improvement over 2 uses the positive margin of 1+cosθ, the sign and vanishing of a use the exact angle interval, and expanding uw=1/4+O(δ²) and C=1−δ²/2+O(δ⁴) yields the stated mass correction. Independent sampled LP vertex enumeration corroborated the mass for N=7 through 31; it is not the proof of the all-modulus statement or of the even optimizer interval.

## originality

PASS

For the repaired claim, the supported distinct result is the exact odd cyclic mass and residue-dependent optimizer, together with a complete real-even equality description on the same family. The even value alone is an immediate parity bound and does not establish originality. Neither the exact-support infinite-group result nor the finite coefficient-extremal result covers the odd mass or full equality formulas.

## value

PASS

This fixed five-site support of separated odd jumps is a natural parity-sensitive Turán test case. The continuum/infinite-group bound gives no magnitude for the odd-grid defect. The exact finite answer quantifies it for every modulus, identifies when the shorter jump is unused, and distinguishes the positive-dimensional even real-even face from the unique odd real-even optimizer. These are useful exact benchmarks for small-support cyclic optimization, beyond recovering the infinite-group limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
