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

In the unnormalized successor-arc model a marked arc of length d separates the d−1 strictly interior labels (none can join its block or span the arc) from the exterior, where contracting its endpoints leaves n−d labels. Thus N_e=C_(d−1)C_(n−d). Catalan log-convexity gives N_e≤C_(n−2) for d≥2, with N_e=C_(n−1) for d=1; contracting two distinct adjacent-label arcs gives N_ef=C_(n−2) also when they share a vertex. Expanding the quadratic character gives C_n−2N_e−2N_f+4N_ef. For zero, one and two adjacent-label arcs the stated bounds are positive from n=5 (as is the singleton bound). At n=6 the three marked common-source arcs are mutually exclusive and have counts 42,14,10, giving zero. Reduction modulo 4 uses even N_e and C_6=132. The −4 witness has total singleton count 80 and only two compatible pairs, of multiplicities 4 and 2, with no triple: 132−160+24=−4. A fresh exact calculation independently agreed on the support of 132 vectors and evaluated every signed sum directly; it confirmed all six-label degree-zero multiplicities in the zero census, 25 cubic zeros, rank 23684, nullity 9084 and the absolute nonzero minimum 4. At n=5 the same calculation finds 164 zeros beginning at degree 4. The phrase ‘first cubic obstruction’ is correct in the stated n≥5 regime, not globally: at n=4 the three adjacent chain arcs give 14−2·15+4·6−8=0. Nor does ‘first cubic’ mean the first singular operator. The accompanying original checker uses int.bit_count, requiring Python 3.10 or later rather than 3.8; the independent run is not dependent on that checker.

## originality

PASS

The Catalan arc object is known, as are related Walsh spectra in materially different embeddings and restricted families. The checked statements do not give the all-n successor-arc quadratic positivity or the exact unrestricted six-label successor-arc census.

## value

PASS

There is a natural cutoff by Walsh degree in a fixed Catalan encoding: all quadratic modes survive at every size from five, but cubic modes can already disappear at six. The exact finite loss and first nonzero magnitude are useful invariants of this operator, beyond object counts or arbitrary sample statistics. This does not assert an all-size high-frequency classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
