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

The claim is proved in `RESULT.md` by an explicit Pascal equation, finite-field quadratic-character identities, and transitivity of \(\operatorname{PGL}_2(\mathbb F_q)\) on each rational conic-line type. The standalone `verify_pascal.py` checks every rational hexagon in prime fields of cardinalities \(5,7,11,13\), tests normalized triples in eight prime fields and \(\mathbb F_{25}\), and records its observed output in `verification_output.txt`.

Finite computations check the algebra and boundary cases but are not a proof of an infinite-field family. The hypotheses exclude characteristics two and three and repeated conic vertices. Independent mathematical audit is not performed.
