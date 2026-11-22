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
# Verification record

The derivation is self-contained in RESULT.md. A standard-library Python verifier, `verify_minimal_nilpotent_graph_fibers.py`, enumerates every labeled simple graph without a universal vertex on \(2\), \(3\), or \(4\) vertices (\(46\) graphs altogether), every permitted multiplication table, its graph automorphisms, and the orbit representatives under relabeling. It compares direct orbit counts to the closed antipodal-cycle Burnside expression. It additionally checks the edgeless graphs through \(6\) vertices and specific cycle and matching graphs.

To reproduce, run `python verify_minimal_nilpotent_graph_fibers.py` in a directory containing the script. Expected terminal line: `GRAPH_CONDITIONED_NILPOTENT_SEMIGROUP_FIBERS_VERIFIED`.

Finite enumeration is not an infinite proof. General correctness rests on the exhaustive table normal form, the fixed-orbit consistency lemma, and Burnside's lemma in RESULT.md. The literature comparison does not certify historical priority. Independent external validation has not been performed.
