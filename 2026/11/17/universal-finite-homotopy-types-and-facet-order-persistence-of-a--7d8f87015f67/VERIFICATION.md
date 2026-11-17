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

# Executable verification

Run `python verify_universality.py` in a Python 3 environment with SymPy. The source is standalone and generates directed graph vertices, arrows and binary initial configurations from lists of facets. It independently advances all nonsink chips at every parallel firing round, checks the exact target and auxiliary firing sets, checks that each auxiliary vertex fires exactly once and admits its prescribed anchor retraction at every stage, and confirms the projective-plane signed Smith factors over the integers.

The packaged `replay_output.txt` records checks on one simplex, two disconnected vertices, a triangle boundary, a mixed-dimensional disconnected complex, the six-vertex projective plane, and an exhaustive enumeration of all 166 nonempty antichains of nonempty subsets of four labeled vertices. The projective-plane chain calculation uses the integral cycle basis from a star spanning tree of its complete one-skeleton and returns nine Smith units and one factor two. The constructed projective-plane graph has 141 firing vertices plus its sink.

The unrestricted theorem does not rely on computation: the exact firing-time formula and dominated-vertex retractions are proved in `RESULT.md`. Only finite examples and the stated integer matrix are machine-checked. The checker does not constitute an external or independent audit.
