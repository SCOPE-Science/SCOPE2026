---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

In J=Kt+Kt^2+Kt^3 with sigma(a)=a^q, m>=2, direct Ore multiplication gives commutation iff a sigma(A)=A sigma(a) and a sigma(B)+b sigma²(A)=A sigma(b)+B sigma²(a). When a!=0, A/a lies in F_q and B=ub+v a sigma(a), v in F_q, giving the entire commutative associative centralizer H(a,b) of size q²Q. J² is a maximal commuting clique because sigma is nontrivial. Distinct H are parametrized by projective [a] and b modulo F_q a^{q+1}. Intersections governed by [a] to [a^{q+1}], with kernel gcd((Q-1)/(q-1),q+1) = 1 odd m, q+1 even m. First-coefficient-zero centralizer spectrum follows the sigma² norm equation; double counting all commuting pairs yields Q³[(q²+q+1)Q-q(q+1)]. The algebra group 1+J preserves commutation. Independent GF4 quotient arithmetic yielded centralizer sizes 16 (56 elements) and 64 (8 elements), 1408 ordered commuting pairs, seven maximal commuting classes, agreeing with the formulas. Small computations corroborate, not certify, all q,m.

## originality

PASS

Best of knowledge: no earlier statement in inspected sources gives a full maximal commuting-subalgebra classification, parity-dependent projective incidence, and joint centralizer-size distribution for this precise Frobenius-skew nilpotent t^4 radical. The closest triangular-ring commuting graph has different algebra and noncentral-vertex convention. The cyclic field norm/projective map tools are classical; those alone do not state the joint count and intersection classification. No guaranteed global priority.

## value

PASS

Maximal commuting subsets and their intersections are natural structural invariants of nilpotent algebra groups; the odd/even extension-degree incidence change is a sharp field-theoretic boundary, with exact centralizer and commuting-pair distributions. This is not just an arbitrary numerical slice or a relabeling of generic commuting probability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
