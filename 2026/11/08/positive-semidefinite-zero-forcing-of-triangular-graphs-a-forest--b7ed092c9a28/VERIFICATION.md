---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: PSD zero forcing is applied componentwise in the white induced subgraph. A white-edge cycle in K_n cannot be broken by a blue K_n edge, since any blue edge meeting the cycle sees both incident white cycle edges in the same component. A spanning tree (one ground component) has no initial force. Conversely, if white graph F is disconnected forest, any white leaf u in a nontrivial component C and w outside C give a blue edge uw with precisely one white neighbor uv in white component L(C); induction removes all edges. Thus B succeeds iff F is forest with >=2 ground components for all n>=3, including empty F. Cayley exponential set partitions enumerate all forest sizes; independent Python computed exact 2-component minimum counts n=3..8 as 3,15,110,1080,13377,200704. Reviewed independent PSD simulator in check_psd.py and forest counter in check_forest_counts.py, but infinite theorem rests on structural proof rather than bounded enumeration.

## originality

PASS

PASS best-of-knowledge: Peters 2012 Proposition 3.16 and Fallat et al 2015 Lemma 8.3 establish only scalar PSD minimum N-n+2 for J(n,2), not the complete all-initial-blue-sets forest predicate or polynomial. Prior ordinary zero forcing on J(n,2) has a stronger white-forest-with-isolate condition: K4 disjoint white edges form a PSD-successful, ordinary-unsuccessful witness. General PSD polynomial for complete multipartite graphs is not equivalent. Full 2013 thesis and unindexed exact tables remain historical risks, not automatic failure.

## value

PASS

PASS: The exact structural characterization of every PSD forcing set in an unbounded natural graph family is substantially more informative than scalar Z_+. It converts a dynamic process into disconnected labeled forests, yields a full exact generating polynomial and counts all minimum forcing sets, and quantifies a genuine rule-dependent distinction starting with two disjoint K4 edges. Independently useful exact invariant; not mere known minimum recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
