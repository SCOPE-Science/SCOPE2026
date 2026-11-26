---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Reconstructed the stars-and-bars model: for t specified internal gaps of total size s, the probability is (r)_t(n−r)_s/(n)_{s+t} in falling-factorial notation; the ordered distinct choices in a joint factorial moment are (r−1)_t. At r/√n→c the resulting moments tend to c^(2t), determining the independent Poisson law (with a finite exponential moment); the fixed discrete lattice upgrades convergence to total variation by a finite-box truncation. At most 2(k−1) sites can cause clipping, and a union bound over neighboring internal-gap pairs with bounded total length gives O_k(r³/n²) for triple windows. With neither event, each close pair at gap d occupies k−d windows and supplies one count per two-one offset. Removing the two singleton contributions to each such window and correcting the count of occupied windows recovers exactly the displayed affine map, with a two-one coordinate recovering each X_d. Coupling the two spectra to that map and multiplying the one-coordinate sum of squared Poisson masses gives the stated Bessel collision law. For the reference profile, zero counts for all patterns with at least two ones forbid close pairs; total one-incidence kr then requires every one to have its full k windows, including at the boundary. Subtracting k−1 from all gaps gives the stated binomial ratio (also valid for r=0 and n≥k). Expanding its product gives log probability −(k−1)r²/n+o(1) for r=O(√n); when feasible its log is at most −(k−1)r(r+1)/n. The outer-regime assertion is for the reference-profile probability, not a proved supercritical limit for all collisions. Independent bounded enumeration matched 12,365 affine comparisons and 379 reference counts; the replay also checks nonnegativity, which unary Counter filtering in the supplied checker alone does not establish. Exact finite moments at n=2500,r=50,k=4 are consistent with the recorded simulation, which is diagnostic only. Inspected source support; no uploaded code executed. Replay: python3 /workspace/branches/936dc3d4-20c2-43ca-b9be-07fdbf163ebe/bounded_replay.py.

## originality

PASS

Best-of-knowledge pass for the full fixed-width multiplicity law and its critical collision consequence. The short-gap Poisson mechanism is classical in kind; the fixed-three-marker trigram reference count is prior, and neither that case nor a presence-only spectrum is the growing-weight all-coordinate theorem.

## value

PASS

This is an information-loss invariant of a specified observation channel. Reducing a full overlapping multiplicity vector to independent sparse gaps at the critical weight explains both the exact separated-profile threshold and a nondegenerate, computable probability of readout ambiguity. The general k-coordinate statement and collision law are useful beyond a one-motif approximation or the already known fixed-three-marker case. They do not estimate unique recovery, noisy observations, or any biological process.

The dated certificate retains the supplied scientific assessment, sources and limitations.
