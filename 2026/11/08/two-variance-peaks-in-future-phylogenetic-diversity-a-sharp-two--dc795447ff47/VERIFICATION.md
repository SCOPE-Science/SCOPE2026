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

The standalone Python 3 file `verify_variance.py` was run from the same package contents with no third-party dependencies. It checked seven exact rational Bernstein-basis positivity certificates for the critical polynomial, the universal family sign inequalities at their base index and the first 94 instances, exact probability-polynomial enumeration over all 256 eight-taxon survivor sets, equality with the derived variance polynomial, four rational derivative signs, and the exact Descartes sign-change limit.

The universal statement for all \(m\ge7\) is **analytical**, using the decrease of \((8m-18)(7/10)^m/(2m-9)\); enumeration of 94 cases is a supplementary check, not its proof. The certificate of exactly three positive critical points combines disjoint rational sign intervals with Descartes' rule, rather than numerical root counts. The result concerns independent homogeneous extinction and the given rooted topology; no inference is made about empirical extinction processes.
