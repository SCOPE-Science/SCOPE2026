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

For 0 ≤ t ≤ d, a length-t walk ends at a target precisely when the source's last d−t letters match the target's first d−t letters. Thus all-one at t means every one of q^(d−t) disjoint initial classes of size q^t is occupied. This gives both the exact product count and binomial empty-class law; all-one is absorbing, so subtracting successive cumulative counts is valid. At t=0 only all-one hits, at t=d every nonzero state hits, and a singleton cannot hit by d−1. The sole infinite hitting time belongs to all-zero; this is a clock to all-one, not to either unanimous configuration. At t=(1±ε)log_q(d), with the appropriate integer rounding, the mean empty count diverges or vanishes, respectively. At binary d=2^h+h+c the empty-class means at h−1, h, h+1 are 2^(2^(h−1)+c+1), 2^c, 2^(c−1−2^h). Independence at each time gives the Poisson limit at h and the two adjacent hitting masses without requiring independence across times. An independent direct-update census agreed at (2,1),(2,2),(2,3),(2,4),(3,1),(3,2), including finite counts (1,6560,44064,14400,510) and one nonhit at (2,4); this corroborates only finite cases. The frozen verification paths are verify_exhaustive.py and verify_reachability.py with their recorded outputs; neither frozen program was executed in this review.

## originality

PASS

Qualified to the all-size labelled hitting census and the lattice-scale random-initialization law for this graph. General OR propagation, primitiveness and independent-block Poisson approximation are prior; the checked general results do not supply the exact suffix partition or its hitting invariant, and the closer cutoff analogues have different obstruction sets.

## value

PASS

The formula gives the count of all labelled inputs meeting any deadline, and the entire biased reliability curve, on a standard directed network. This is more informative than its exponent or its fixed points: it quantifies d versus log_q d and identifies the sparse dimension subsequences where each of two adjacent clocks retains positive mass. The dimension window is forced by keeping the mean number of empty classes finite, rather than selected as an arbitrary numerical slice. Value is in the exact graph-specific invariant and calibration, not in a new general occupancy principle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
