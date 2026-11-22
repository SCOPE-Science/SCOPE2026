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

# Reproducibility and limits

The mathematical proof appears in `RESULT.md`. Run `python3 verify.py` with a standard Python 3 interpreter and no third-party packages. The checker constructs finite flat semilattice action monoids, generates each congruence as the least equivalence closed under multiplication on both sides and the maximum operation, and exhausts the lattice through generators. It compares the complete resulting congruence sets, rather than just their counts, to independently constructed classified families. It also directly examines all \(4{,}140\) partitions of the eight-element case to distinguish ordinary and \(F\)-congruences.

Checked cases: regular \(C_m\) actions at \(m=2,3,4\); a nontransitive \(C_2\) action with a fixed atom; and the natural nonabelian \(S_3\) action. The expected success marker is `FLAT_SEMIDIRECT_F_CONGRUENCES_OK`.

These computations only verify finite examples. The arbitrary finite-group result relies on the fully written algebraic argument, and no independent mathematical audit has been performed.
