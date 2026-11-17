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

# Reproduction and boundaries

Run `python3 verify_one_missing_whisker_morse.py` with Python 3.10+ using only the standard library; compare against `VERIFIER_OUTPUT.txt`. The verifier constructs graph edges, checks connectedness, and enumerates all admissible faces using induced vertex degree at most one. For every connected labelled core graph on \(n=3,4,5\) vertices and every root it reduces binary boundary operators exactly and checks reduced homology: 3,804 rooted instances in total, of which 144 have a predicted sphere. Testing roots of degree one goes beyond the theorem's domain but does not broaden the accepted theorem.

The program independently assembles the directed Hasse diagram for a sample of 59 connected rooted graphs, including three friendship graphs, using the prescribed least-eligible-leaf pairing; it checks critical cells and proves that the finite directed matching diagram has no directed cycles by exact topological sorting. Its recorded output reports the face and matched-pair counts for the three windmills.

Neither finite rank computation nor finite cycle enumeration proves an all-size result. The all-size proof is the explicit Boolean-fiber acyclic matching and classification of unmatched cores in `RESULT.md`; its CW conclusion holds over the integers. The independent-audit channel is not performed.
