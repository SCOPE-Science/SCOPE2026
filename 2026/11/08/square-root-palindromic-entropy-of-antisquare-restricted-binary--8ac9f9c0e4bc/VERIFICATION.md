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

The Pansiot adjacent-change code maps precisely the eight forbidden binary factors to Q={010,101,11111,01110}. The published finite-code avoidance criterion implies goodness; the prefix-free block code {0,1100,111100}, centered 6/7 zeros and its reversed copy avoid Q, and even transition parity yields two good palindromes for each distinct block word. T_h satisfies T_h=T_{h-1}+T_{h-4}+T_{h-6}; its unique dominant positive root factors via (x+1)(x^2-x+1)(x^3-x^2-1), giving T_h=Theta(psi^h). Palindromic first halves bound P_n<=G_ceil(n/2), and Baranwal et al. Theorem 19 gives G_n=Theta(psi^n). Two parity classes and finitely many low lengths handled explicitly. Independent small palindrome enumeration agrees through n=14; the infinite proof is the injection and published growth theorem.

## originality

PASS

Baranwal et al. establish the unrestricted growth, finite forbidden core and Pansiot coding, but not a matching *reversal-fixed* lower bound. The published seven-run census and periodic transition enumerator concern different restrictions. The explicit injection gives the new sharp reflection-fixed entropy. No covering equivalent was demonstrated in actual searches; possible general reflection-entropy machinery remains a risk.

## value

PASS

The reflection-fixed entropy of a natural factorial word language is not determined by unrestricted entropy: the half-word upper bound can be strict. The explicit all-length reversible construction and exponential scarcity estimate are motivated sharp infinite asymptotics, not a small numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
