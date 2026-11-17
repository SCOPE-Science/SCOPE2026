---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Conditional on every other internal vertex, g:{0,1}^2->{0,1} is monotone and delta=g11-g10-g01+g00. Setting protected reliabilities from p to one yields I=(1-p)^2 E[delta]. With <=5 total vertices only one other internal variable w exists; sign change requires delta0,delta1 of opposite signs. Monotonicity excludes delta0=-1,delta1=+1; the reverse forces majority-of-three Boolean viability. All three pairs of internal vertices must then each form an s-to-t directed path and each must meet disjoint L={s-out-neighbors} and R={t-in-neighbors}, impossible on a triangle. The explicit six-vertex DAG edges 01,03,12,14,25,34,45 have Boolean reachability x1*x2 + x1*x4 + x3*x4 in OR form and delta=(1,0,0,-1) on remaining pair, giving I=(1-p)^2(1-2p). Independently enumerated 2^15=32768 forward-labelled DAGs times 6 pairs=196608 exact profiles using a separate reachability bitset code: 18 coefficient triples, precisely 24 strict sign reversals, all (1,0,-1). No cyclic six-node classification is claimed. Check includes exact vertex extrema for quadratic in [0,1], not just sampled p.

## originality

PASS

Generic joint reliability importance and sign-variable coherent systems are prior art. The inspected Wu 2005 paper defines the binary JRI as a mixed reliability derivative and multistate extension, without a minimal directed vertex-connectivity realization theorem; Hong–Lie 1993 addresses edge reliability in undirected networks. A k-out-of-n/majority example does not realize the three-intermediate-vertex function as directed s-to-t reachability (proved impossible here). Resultary search found the submitted finding and unrelated network cutoffs, no stronger six-node directed vertex realization classification. Best-of-knowledge original with specialist literature risk.

## value

PASS

A sharp realizability obstruction for a natural intervention interaction, together with a first possible six-node witness and exhaustive six-node DAG polynomial classification, is a motivated structural benchmark for directed reachability reliability. The exact threshold distinguishes general Boolean importance from graph-implementable importance; nontrivial even at six vertices, not an arbitrary tiny slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
