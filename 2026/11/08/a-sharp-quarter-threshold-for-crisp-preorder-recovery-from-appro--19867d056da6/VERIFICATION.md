---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

Nonempty finite W, arbitrary R in [0,1]^{W²}, standard Łukasiewicz t-norm max(0,a+b-1), residuum min(1,1-a+b) and box inf_v(R(u,v)⇒p(v)); K/T/4 deficits are sup over ALL real-valued valuations at ALL worlds. Write D_Rp(u)=max_v(R(u,v)-p(v))_+, so box p=1-D_Rp. For K the nested implication deficit is (D_R q-D_R p-D_R(p⇒q))_+: choose a q-maximizing v, bound by min(h,r)-(h-(1-r))_+<=min(r,1-r), where h=(p(v)-q(v))_+. A witness q(v)=0,p(v)=min(r,1-r), p=q=1 elsewhere attains the max for each r. For T the exact max deficit 1-R(u,u) follows from box p(u)<=R(u,u)⇒p(u) with p(u)=0, p(others)=1. For 4, Łukasiewicz residuation and finite min interchange give box_R box_R p=box_S p, S(u,z)=max_v R(u,v)⊙R(v,z). The max defect is max_{u,z}(S(u,z)-R(u,z))_+, witnessed by setting p(z)=R(u,z), all other p=1 (D_R=0, D_S equal positive violation). If Q is a crisp preorder and eta=||R-Q||inf, K,T<=eta, and if Q(u,v)=Q(v,z)=1 then Q(u,z)=1 forces S-R<=eta; otherwise one edge weight <=eta implies their Ł-product <=eta. Hence Δ<=eta. With e=Δ<1/4, all entries lie in [0,e]∪[1-e,1]; nearest endpoint rounding P is unique, its error is δK; diagonal weights>=1-e imply P reflexive; high two-step edges force R(u,z)>=1-3e>e and thus the third high edge, so P transitive. Therefore distance to crisp preorders=Δ=δK. At e=1/4, R=[[1,3/4,1/4],[0,1,3/4],[0,0,1]] has (δK,δT,δ4)=(1/4,0,1/4) and every crisp preorder is at distance >=3/4; adding 1→3 or removing a 3/4 edge attains 3/4. Independently implemented exact-rational Łukasiewicz semantics and all crisp preorders for all 630 one-/two-world five-level frames plus 2 independent three-world samples and sharp example; all checks matched. These finite checks corroborate but do not prove arbitrary W and real valuations; the preceding symbolic argument establishes all quantifiers.

## originality

PASS

Best-of-knowledge originality rests on the full mathematical comparison: the 2026 modal S4 source validates modal axioms in a compatible fuzzy-topological semantics; it does not quantify K/T/4 valuation deficiencies or give an exact uniform nearest-CRISP-preorder radius. Earlier Boixader–Recasens fuzzy-approximation work develops degrees of transitivity and distance to fuzzy T-preorders; it does not derive unique Boolean rounding of an arbitrary fuzzy frame from the three modal deficiencies. Their 2013 full text explicitly shows general rounding may destroy transitivity (Example 3.7 and Proposition 4.14), but does not supply the epsilon<1/4 stability criterion for relations near endpoints. Luo (2026) optimizes fuzzy-equality proximity over all T-transitive FUZZY relations, not all crisp preorders; it does not imply the exact three-modal-defect identity. Relevant published SCOPE records on monoidal completion, three-valued frame census, Gödel regrading, and a separate Alexandrov quarter-law concern different invariants. A 2011 discretization conference article remains an unresolved priority risk owing to unavailable full text and disconnected institutional VPN; this is not treated as proof of priority.

## value

PASS

This gives a sharp and directly interpretable robustness theorem for approximating crisp S4 accessibilities from all-valuations modal defect measurements, a natural stability question at the interface of many-valued modal logic and fuzzy relation approximation. The separate exact K/T/4 formulae, an explicit unique nearest crisp preorder under e<1/4, and a minimal three-world obstruction at the boundary provide a structural result not mechanically obtained from general fuzzy-preorder proximity or qualitative crisp-frame soundness. The uniform finite-carrier result is not a random small grid computation, parameter substitution, or unsupported tiny gain; it establishes an explicit sharp mathematical boundary useful for deciding when graded frames can be rounded while retaining preorder semantics. It is confined to finite standard Łukasiewicz Kripke semantics; it does not guarantee arbitrary S4 consequences or infinite-frame behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
