---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

On H=C, with two equal weave families, K=(1/2)I, full subspaces, positive weights 1, active Λ_i0=(1/2)I and passive Λ_i1=0, each full weave has energy (1/4)||f||²=||K*f||², hence A=B=1 satisfy the source definitions (m=2>1). For the proper deletion I={0}, ||K†||²=4 and C=sum_i ||Λ_i0||²=1/2. The printed hypothesis 1/2<4 holds and predicts remaining lower A-C=1/2, but all remaining weaves have energy zero for nonzero f in R(K)=H. The original proof actually gives lower A-C||K†||² on R(K), because the deleted sum is <=C||f||²<=C||K†||²||K*f||². Thus the asserted counterexample and repaired SUFFICIENT bound C||K†||²<A are correct. Exact Fraction computations independently confirm all scalar identities. Original six actual pinned Git blob hashes were read with the GitHub connector, current main has exactly the same six hashes, and an independent Git-tree serialization matches 204d3d8d82f0ef666c4f7e32d3126f3c3ac1dfc8. No claim of necessity or optimality is established.

## originality

FAIL

An already public independent Resultary research finding, SCOPE-20261011-db7405dd7d3f, addresses exactly Sadri--Rahimlou--Ahmadi Theorem 2.5 and states both the same invalid printed threshold and the same correction C||K†||²<A with lower A-C||K†||². Its complete proof and R² counterexample were read, not just its title or search snippet. The submitted H=C construction arises from restricting that witness to span(e1), scaling its analysis maps by 1/2 and relabeling the two indices. Moreover, the original 2021 source already contains the correct coefficient in its last proof line. Therefore there is no independent original correction or counterexample theorem left. The published near-duplicate and assessed record share publication date 2026-10-11, so relative intra-day chronology is not claimed.

## value

FAIL

Avoiding a false erasure guarantee is practically motivated, and the pseudoinverse factor matters sharply. Nevertheless, the exact correction and a stronger (nonzero surviving analysis) counterexample are already provided in a separate public full-text finding. The submitted zero-survivor scalar construction is a routine restriction and rescaling, not an additional structural lemma, natural classification, new boundary or distinct diagnostic. The original paper itself prints the corrected coefficient in the proof. A second publication of this mathematically covered one-dimensional instance adds no independently needed scientific fact under the value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
