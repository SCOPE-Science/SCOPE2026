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

The exact weighted-shift formula and its diagonal self-commutator follow by projecting monomials in the orthonormal Bergman basis. Symbolic algebra verifies the rational difference and the expansion through order \(n^{-2}\), including divisibility of the critical remainder by \(6\rho^3-13\rho^2+6\rho-1\). The strict signs \(G<0\), \(L<0\), and \(4G+2|L|<0\) are checked using the isolated real root in \((1.6097,1.6099)\). A symbolic checker and exact-rational finite examples are supplied in `verify.py`.

The proof requires, beyond finite computations, a global localization step: strict monotonicity before the shift threshold, the positivity of the higher coefficients of the shifted derivative cubic near the critical ratio, and the resulting bounded set of possible maximizers. The final infinite switching conclusion uses irrationality of the cubic root and density of its rotation sequence. Those are mathematical arguments, not conclusions drawn from sample counts.

The uniform critical-window expansion applies to bounded \(m-\rho n\). The floor-sequence two-choice rule does not settle the winner in the unresolved \(O(n^{-1})\) neighborhood of the threshold. No independent audit has been performed.
