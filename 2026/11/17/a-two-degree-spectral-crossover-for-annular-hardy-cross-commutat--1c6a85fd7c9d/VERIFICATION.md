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

For the normalized Hardy Laurent basis e_j=z^j/sqrt(1+r^(2j)), direct multiplication gives K_{m,n}e_j=F_{mh,nh}(jh)e_{j+n-m}, h=-2log r; the index shift is injective, so these coefficients give precisely all positive singular values. Differentiating log F, a sum of negatives of log-sum-exp terms, shows strict concavity with exponential tails. Every strict upper-level set is a single interval: integer-grid count differs from length/h by <=1, and layer-cake yields all-p Schatten-power discrepancy <=M^p (also p<1). Parameter-uniform exponential tails give simultaneous m h→a>0 and n h→b>0 limits and peak convergence. The stated rational/log H2 integral was independently checked against numerical integration for multiple unequal a,b; rational cross coefficients and symmetry exchange were checked. The diagonal a=b is a calibration, not claimed new.

## originality

PASS

Exact mixed-degree commutator coefficients and fixed-symbol thin-annulus selfcommutator Weyl laws are previously known. The compared published fixed-Laurent-degree result explicitly holds degree constant as h→0; this cannot imply the positive finite a=mh and b=nh unequal-degree double scaling. The independent two-parameter singular values, uniform count/Schatten remainders and closed cross-H2 law are substantive additional operator invariants on current available comparisons.

## value

PASS

The simultaneous degree/thickness regime is a natural spectral crossover of nonnormal cross-commutators, distinct from fixed-symbol limits and self-commutators. A complete positive singular-value profile with uniform counting and Schatten remainders plus an explicit two-variable H2 integral supplies a useful exact family of compact-operator invariants, not merely a known diagonal identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
