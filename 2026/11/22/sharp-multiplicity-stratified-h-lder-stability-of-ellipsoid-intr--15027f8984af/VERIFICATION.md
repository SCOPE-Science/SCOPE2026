---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification notes

The proof derives coefficient-distance control from the cited intrinsic-volume Jacobian lemma, independently proves clusterwise root matching by Rouché, and constructs sharpness witnesses for every maximal multiplicity. Analytic assumptions include full-dimensional ellipsoids, positive squared semiaxes and sufficiently small local neighborhoods of a fixed axis multiset. The exact dimension-three coefficient Jacobian follows by elementary beta integrals, not from a floating-point certificate.

Run `python3 verify.py` with Python 3 standard library. The program tests the integral evaluation against unit-ball intrinsic-volume normalization for dimensions two, three and four; compares finite-difference derivatives against the exact ball Jacobian; and evaluates a four-point sequence of cubic ill-conditioning witnesses. Observed: `PASS: 28 finite checks`; data-distance ratios divided by \(\varepsilon^3\) were approximately \(2.0446553848\), \(2.0194812545\), \(2.0075424688\), and \(2.0027054806\). These are finite crosschecks, not a substitute for the all-dimensional proof.

The strict Jacobian lemma is sourced to Myroshnychenko, Tatarko and Yaskin, *Unique determination of ellipsoids by their intrinsic volumes*, arXiv:2611.24923v1 (2026-11-18), Lemmas 3.5, 4.1 and 4.2, and Section 5. The estimate is local and does not identify an ellipsoid's orientation or center. No independent audit has been performed.
