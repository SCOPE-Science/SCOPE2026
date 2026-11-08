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

# Verification

Run `python3 check.py` with Python 3 and its standard library only. The printed result is `VERIFY_OK 2175 exact assertions`.

The checker constructs all spanning trees for seven small \(K_{a,b}\) examples independently by examining edge subsets and testing connectivity/acyclicity. It compares all edge-set inclusions of size at most three against rational transfer-current determinants, including matching-forest formulas and the Hadamard bound; it independently compares ordered second factorial moments against the three-case formula for two, three, and four tree layers. Full tuples of three and four trees are also enumerated on small examples and their overlap moments compared with the formulas. Exact arithmetic is used throughout.

An additional finite sequence of cases checks that critical-window factorial-moment lower/upper bounds are ordered and positive. This finite evidence does not establish convergence in total variation, the supercritical threshold, or universality. Those follow from the proof's determinant identity, factorial-moment bounds and inversion, negative pair dependence, and symmetry/collision argument. The proof is self-contained conditional on the classical weighted matrix-tree theorem and elementary determinant identities.

No independent mathematical audit has been performed. Historical-priority coverage is limited to the specified inspected publications and searches.
