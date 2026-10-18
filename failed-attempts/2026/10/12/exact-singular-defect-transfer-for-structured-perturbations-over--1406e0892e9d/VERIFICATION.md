---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Under P1–P3 exactly as in Öinert Theorem A and Lemma 2.1, source R^n=ker F ⊕ X(R^k), target R^n=im A ⊕ E(R^k), and A_0=A|ker F is an isomorphism. Direct substitution T_D(u+Xc)=Au+EDc proves ψ^{-1}T_Dφ=A_0⊕D for EVERY D, no ring commutativity or D invertibility. Kernel and cokernel transfer follow functorially. T_D(G+XHY)T_D=A+E(DHD)F, with the reflexive product G+X(HDH)Y, while T_DQT_D=T_D forces D(FQE)D=D; vN regularity iff D regular. Field rank/nullity are only field corollaries. No finite check substitutes for these ring identities.

## originality

FAIL

The full primary Öinert article itself gives in Lemma 2.1 (proof) the complete source/target direct-sum decompositions, isomorphism A_0, and maps X,Y,G independent of D. Therefore for any D its published lemma ALREADY yields the exact block equivalence A_0⊕D by an immediate single substitution. The kernel, cokernel, regularity, and generalized-inverse claims are elementary consequences of that prior *stronger splitting result*. Missing exact phrasing or numerical singular-D examples does not establish originality. This is positive prior mathematical implication, not an inaccessible-literature inference. No repaired novel remainder was identified.

## value

PASS

The singular-D kernel/cokernel and inner-inverse descriptions are a natural structurally useful diagnostic over noncommutative rings, and the exact statement would help users of structured updates. Value is recognized independently of its rejection for established-prior implication; utility and a concise proof do not make it original.

The dated certificate retains the supplied scientific assessment, sources and limitations.
