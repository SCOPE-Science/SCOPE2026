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

# Reproduction and proof boundaries

The file `verify.py` needs Python 3 with no third-party dependencies. Execute `python3 verify.py` from a directory containing the script; success prints four PASS statements and exits with code zero. This exact-arithmetic program enumerates all 126 vertex quintuples in the square–pentagon free sum and checks the signed pentagon triangle determinants through rational arithmetic in \(\mathbb Q(\sqrt5)\). It also checks the Cartesian support sets for all 31 cubed nonempty triples of pentagon vertex sets, enforcing **oriented** equality, which is necessary for convex-combination extremality. It confirms 15 maximal ordered vertex triangles, 15 ordered one-edge support systems, and the resulting five-cycle incidence, replicated over four rigid square pairs.

For arbitrary vertices within the polytope, exhaustive checking is neither claimed nor needed. The proof in `RESULT.md` establishes the general equality-support principle by multi-affinity of the oriented determinant, proves both square vertices rigid using \(\|a\|_2\le1\) with equality only at the four square vertices, and proves at most one movable pentagon vertex using a four-versus-three incidence obstruction. The finite exact checker verifies the proof's combinatorial ingredients and strict trigonometric comparisons. It is not an external or independent audit. The sharp value and original extremal polytope are already known in the cited sources; the new point is completeness of the optimizer locus and its topology.
