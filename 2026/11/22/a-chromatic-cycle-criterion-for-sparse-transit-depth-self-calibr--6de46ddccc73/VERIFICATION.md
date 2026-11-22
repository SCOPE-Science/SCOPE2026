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

# Exact checks and limits

The accompanying self-contained `verify_chromatic_cycles.py` runs under Python 3 using only `fractions` and `random`, with a fixed pseudo-random seed. Reproduction command: `python3 verify_chromatic_cycles.py`.

The script checks a fully rational four-edge case with two epochs and two distinct spectral contrasts. The observed reciprocal depths are exactly \(95/2\), \(45\), \(34\), and \(28\); the corresponding holonomy is exactly \(153/133\ne1\). It validates affine reconstruction of the epoch covering fractions and intrinsic band depths. For graphs with two through seven epochs and two through six bands, it tests the four-edge mixed-contrast cycle with all other vertices attached as leaves, recovering exactly the generated rational parameters; removing a cycle edge makes the graph a spanning tree with a free parameter. It also constructs an exact, nontrivial one-parameter gauge change for equal-contrast bands and checks that it leaves all observations unchanged.

Observed test output during preparation: `PASS: 31988 exact-rational assertions; illustrative numerical checks only`. The exact finite assertion count supplements the symbolic argument; it neither proves the universal graph criterion nor establishes priority. The mathematical proof supplies the arbitrary graph statement and generic measure-zero qualification. No independent external verification has been performed. The theorem contains no noise or model-error guarantee.
