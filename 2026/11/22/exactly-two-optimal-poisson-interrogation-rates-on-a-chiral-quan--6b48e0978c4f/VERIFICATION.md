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

Independently recomputed the one-attempt rational functions by summing the exact Laplace transforms of differences of the three eigenfrequencies using spectral projectors, rather than relying on the source checker. They agree for both fixed source-target orientations. Unit-hopping |0⟩ preparation and |2⟩ detection are unchanged under the diagonal gauge D=diag(1,i,i). The forward matrix gauged as D*H₊D has 01 and 12 entries one and 02 entry −i; this gives sin Φ=−1 in the matching stationary-reset source. Independently renewed durations and outcomes justify E[T]=1/(rp) without assuming success independent of its own trial duration; the sum of durations weighted by survival to each trial is a convergent geometric sum. In the repaired proof division by r² gives rp=2(x∓3)/(x²+3) for x=r+6/r≥2√6. The forward rational function has a unique strict maximum in x at 3+2√3>2√6, with value 1/(3+2√3); both positive inverse images are exact and distinct. The backward function is strictly decreasing in x on the entire interval, giving the unique fixed-point rate √6 and mean 27/(6+4√6). This proves global optimality, reproduces the original rates and signs, and explains why the same reciprocal symmetry permits different optimizer multiplicities.

## originality

PASS

Pass for the repaired global optimizer classification, not the one-attempt probability law. The exact same-gauge individual populations in 848fc77e7b52 supply both probability functions on specialization. The strongest inspected matching result instead optimizes the stationary site-population imbalance. It does not classify global optima of the different elapsed-time objective, or imply the reciprocal symmetry's two-preimage optimum from its imbalance theorem.

## value

PASS

A maximally chiral three-site ring is a natural smallest cycle with flux, and mean detection time with renewal is a standard objective. A precisely tied finite pair, in contrast to a strict single optimum on changing only flux direction, is stronger than finding multiple local extrema and provides a sharp benchmark for attempts to prove single-optimum behavior. The reciprocal-rate symmetry shows the mathematical mechanism and explains why it produces two rates only for one orientation. The value is not in re-integrating the known site occupation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
