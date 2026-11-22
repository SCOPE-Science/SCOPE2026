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

The theorem was checked algebraically by reconstructing the facet classification from the polar cube section and the exact range/gauge covering criterion for a free sum of two centered simplices. The complete proof is in `RESULT.md`.

Run `python CHECK.py` using a standard Python 3 interpreter. The checker uses exact fractions, verifies all polar facets for cycle orders from three through ten, and tests 4,120 convex combinations of free-sum vertices for pairs of simplex sizes from two through five. For every such pair it also verifies a rational exposed noncovered boundary point for a strictly larger generation weight. `CHECK_OUTPUT.txt` records the replay result.

Finite checks do not establish the infinite-parameter statement. The proof invokes the face-inheritance and central-symmetry boundary-lifting lemmas of Artstein-Avidan, Falah and Slomka (arXiv:2407.20604), specifically their Lemmas 2.2 and 5.1, and proves the additional free-sum lemma directly. Independent audit has not been performed.
