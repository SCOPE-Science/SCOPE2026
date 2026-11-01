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

For fixed finite nonempty A⊂{2,3,...}, the distinct power set B_A satisfies M=B_A(X)≤K_A log X. The assigned proof takes x=log X/3, Q=∏_{p≤x}p, H=floor(c_A log x), and S0={j-w:1≤j≤H,w∈B_A∩[0,X]}. Averaging b0 mod Q leaves ≤HM φ(Q)/Q=(3e^{-gamma}c_A K_A+o_A(1))x shifts, so c_A sufficiently small makes ≤η x; all distinct shifts have |s|≤X=e^{3x}. The published Radomskii Lemma 3.1 produces one t≤e^x for the survivors (also k=0). Among ≤M powers in [X/4,3X/4], one empty interval has D≥X/(2(M+1))≫_A X/log X, whereas Q+Qe^x+H=X^{2/3+o(1)}=o(D) and y=exp(x/(log x)^5)=X^{o(1)}=o(D). Placement inside its middle ensures w either above the block (negative difference) or below it with N+j-w>y; a divisor ≤x or ≤y is therefore proper, proving each difference composite. This reconstructs the all-X asymptotic, duplicate powers, possible empty S, all n≥1 and the fixed-family dependence. Independently, the stronger October 9 Theorem 1.1 directly implies the same bound, corroborating correctness.

## originality

FAIL

The claimed all-finite-base theorem is an immediate specialization of an earlier, quantitatively stronger arbitrary-additive-summand theorem published on 2026-10-09, before the record dated 2026-10-12. The published proof even uses the same all-shift sieving and summand-free-gap placement. An absence of the particular Romanoff wording does not defeat mathematical implication.

## value

FAIL

Although simultaneous avoidance of finitely many Romanoff bases is a natural example, the precise bound is an immediate substitution into an earlier general theorem about arbitrary prime sumsets P+B. The submitted proof repeats the source theorem’s residue-class averaging, summand-free interval and large-shift lemma without an independently needed new lemma, stronger constant, new critical boundary, or classification. The finite-family specialization may serve as exposition, but it is not an independent mathematical contribution under the common mathematical-value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
