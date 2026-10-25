---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Reconstructed all six steps from pinned RESULT.md. Hf=f(0)+f′ is a positive continuous sup-unit profile; for h in P every fiber consists exactly of 0<=a<=min h with f_{h,a}(0)=a, f′=h−a and a+‖h−a‖∞=a+(1−a)=1. Positive f,g satisfy ‖f+g‖_(1)=‖Hf+Hg‖∞ exactly. Distinct u,v in P have different positive-sum profiles: if u(s0)<v(s0), choose a unit bump w supported where u<u(s0)+ε with 0<ε<v(s0)−u(s0); then ‖u+w‖∞<u(s0)+ε+1<‖v+w‖∞, including u(s0)=0 and endpoints. Onto T carries equal H-fibers into equal H-fibers using every test Tk, and induces a surjective norm-additive Φ:P→P. The checked full primary proof of Ezumi–Miura Theorem 2.1 proves Φ(h)=h∘τ for one homeomorphism τ. On each fiber T produces ψ_h:[0,min h]→[0,min h]; bijectivity of Φ and onto T force ψ_h onto. Conversely any τ and such ψ_h give nonnegative derivative h∘τ−ψ_h(a), correct unit norm, surjectivity fiberwise, and exact pairwise preservation. h constant1 full interval, min h=0 singleton, no regularity assumptions. Unique τ by separation, unique ψ by initial values. Proof is analytic, not numerical. No findings for nonsurjective maps or other norms.

## originality

FAIL

The exact kernel/fiber classification, positive-sum identity and freedom of arbitrary surjective interval-fiber maps are already the complete RESULT.md of the distinct published Resultary record "Exact positive-sum quotient at the endpoint" (2026-10-11). Ezumi–Miura arXiv:2610.02862v1 Theorem 2.1 (2026-10-02) already proves that every surjective norm-additive self-map of the positive C(I) sphere is composition with a homeomorphism. Applying its theorem to the quotient of any onto endpoint T is a direct consequence of the pre-existing fiber-identification: norm-sum indistinguishability makes the induced quotient map well-defined, and surjectivity makes it onto. Both halves and the indexed fiber converse are mechanically determined. The complete formula is not separately printed in those sources, and same-day Resultary posting order is unknown, so do not claim chronological discovery priority. At statement-and-implication level the advertised new classification has no independent theorem beyond the two established results. The separate Enami et al. isometry paper is narrower and not used as coverage; complete text unavailable.

## value

FAIL

The endpoint problem is naturally motivated, and displaying the complete combined classification is pedagogically useful. But as a stand-alone new mathematical result the entire quotient/fiber decomposition is an already published exact theorem, and the quotient action follows mechanically by applying an already published Banach–Stone theorem after descending an onto map through the identified kernel. The additional steps are standard passage to a quotient and reassembling fibers, with no new difficult structural lemma, independent parameter range, classification beyond the known ingredients or unknown invariant. As an explanatory synthesis it is useful, but not a distinct scientific finding meeting the value criterion; this is not a penalty for short proofs but for complete immediate implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
