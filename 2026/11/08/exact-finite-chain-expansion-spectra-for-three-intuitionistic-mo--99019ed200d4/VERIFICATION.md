---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

PASS: For finite Heyting chain H_n the implication table is a->b=top if a<=b else b and pseudocomplement is top only at a=bottom. The WM condition reduces to exactly f=bottom, g=bottom, or both initial values bottom; stars-and-bars counts W_n=T_n²+2(M_n-T_n). IM imposes forbidden band: with h=rank f(top), g(a) has v<h or v=top. The three disjoint cases count to I_n=1+M_n-T_n+sum_h binom(n+h-2,n-2)binom(n+h-1,n-1). The ratio A_(n,h-1)/A_(n,h)=h²/[(n+h-2)(n+h-1)] tends to 1/4 near the terminal term and is bounded by 1/3, proving the 2/3 limit. Brute evaluation of every monotone pair for n=2..5 reproduces (9,6,4),(100,44,29),(1225,430,288),(15876,5012,3377). No optional normal axioms or neighborhood frame converse asserted.

## originality

PASS

PASS, qualified: Original modal systems CM, WM, IM and their axioms are due to de Groot and Dalmonte–de Groot. An earlier October 12 finite-Heyting-chain work counts operation pairs induced by continual constructive-neighbourhood frames and proves two-neighborhood compression; its A_n sequence (3,22,224,...) has different semantic realizability restrictions and does not equal or imply the present all-monotone-pair CM/WM/IM binomial census. The inspected primary proof-theory paper defines the axioms but does not give these finite-chain counts. An unindexed earlier same-axiom table remains possible.

## value

PASS

PASS: A complete normal-form and all-size count of labelled algebra expansions for three naturally nested modal axiom systems is a meaningful finite-model structural census. The exact asymptotic losses of freedom 1/4 and 2/3 are intrinsic to the same chain object rather than an arbitrary numeric slice. Existing semantic frame-operation counts cannot replace this axiom-defined algebraic classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
