---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Binet's formula gives J_k>0 for k>=1 and permits the absolutely convergent geometric expansion with x=2^(-n) and epsilon=(-1)^n: S_n is the sum over j>=0 of a_j epsilon^j x^(j+2), with a_j=9(j+1)/(1-(-1)^j 2^(-j-2)). The first coefficients are 12, 16, 144/5 and 384/11. For x<=1/8 the later terms have absolute sum <=(3456/49)x^6<71x^6, using a_j<=12(j+1). Multiplication by A_n=(1-4 epsilon x/3)/(12x^2) cancels the term linear in x; the next coefficients are 28/45 and -16 epsilon/55. The stated rational brackets, bounded at 1/8 by monotonicity, give 0<A_n S_n-1<(256/243)x^2, while S_n>=12x^2/(1+x)^2>=(256/27)x^2. Division yields the strict gap less than 1/9, and the ratio of leading coefficients gives 7/135. The residues of the numerator mod 36 are 20,32,8 with period three because its three-step increment is 189*4^n+36*(-2)^n. Thus the gap cannot cross an integer. For n=1,2 the tail exceeds one, so its inverse and A_n both have floor zero. Independent exact rational enclosures with recurrence-generated denominators and a Binet-envelope remainder corroborate the floors through n=64 and the strict gap for n=3,...,64.

## originality

PASS

The strongest same-object square-tail result found is Gaber's printed odd-index inequality, which is false at n=3 and does not supply exact floors or the residual limit. An earlier exact Jacobsthal inverse-tail result deals with first powers, while the general-family square-tail formulas inspected impose different recurrences. None of the checked catalogue matches, exact count formulas or stronger statements covers the all-index square-tail result. This is a bounded, best-of-knowledge assessment.

## value

PASS

This answers the same exact-classification question motivated by earlier first-power floor laws and the failed odd-index square-tail bound. It identifies the integer part for every index, including both parities and all small cases, with a uniform rational enclosure and an explicit nonzero error limit. An investigator using inverse reciprocal-tail formulas gets a complete rigorous benchmark for a classical recurrence not covered by the inspected square-tail families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
