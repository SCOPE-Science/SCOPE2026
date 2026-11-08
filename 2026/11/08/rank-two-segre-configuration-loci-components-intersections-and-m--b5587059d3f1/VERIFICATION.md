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

# Reproducible checks

The accompanying `verify.py` requires only a standard Python 3 interpreter. Run `python3 verify.py`. It enumerates ordered tuples of Segre points over finite prime fields and computes their projective row ranks by exact modular elimination, then separately evaluates the closed motivic class using finite-field counts of projective spaces and Grassmannians. The five independent tests are for \((q;m_1,\ldots,m_r;n)=(2;1,1;3),(2;1,1;4),(3;1,1;3),(2;1,2;3),(2;1,1,1;3)\), with counts \(261,729,928,1449,2295\).

The all-parameter statements are proven geometrically in `RESULT.md`: the quadrics/three-point argument, line classification, irreducible incidence families, pairwise intersections, and scissor relation. Checks over finite fields do not prove an infinite-parametric theorem. No check of radicality or Cohen–Macaulayness of the original ideal is claimed. Independent validation has not been performed.
