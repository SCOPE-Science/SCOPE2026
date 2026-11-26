---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Write tau^3(0)=A010, tau^3(1)=A01, tau^3(2)=A. Thus t=tau^3(t) begins with A, and the next arches are the intervening suffixes followed by A, namely B,C,A according to the source letter 0,1,2. Each block contains 0 and 1 before its unique final 2. Alternatively the three identities tau^3 d=d sigma hold and iterate from d(A)=tau^2(0), verifying the whole arch fixed point. Greedy arch count equals universality index: each complete arch supplies any requested next symbol, while the sequence of arch-end letters followed by a symbol absent in the suffix is not realizable. Thus the prefix formula holds, and three successive emission counts give |tau^n(0)|_2=|tau^(n-3)(0)| for n>=3. In a factor with r occurrences of 2 every complete arch consumes at least one 2, and the r-1 disjoint intervals from a 2 up to the next 2 contain the alphabet. This gives exactly the claimed two-sided envelope, with the r=0 case handled separately. For the strict all-factor discrepancy, Richomme–Saari–Zamboni Proposition 2.6 states that the prefix discrepancy for 2 lies strictly between -0.88 and 0.62. A factor discrepancy is the difference of its two endpoint prefix discrepancies (including the zero-length prefix), so is strictly less than 1.5 in absolute value. The index differs from the 2 count by at most one, proving the strict 5/2 bound and uniform limit. The original's attribution of the 3/2 input to the nominated Lejeune–Rigo–Rosenfeld paper was not substantiated in the inspected material; the mathematical input is verified directly in Richomme–Saari–Zamboni, independently corroborated by the discrepancy-series argument.

## originality

FAIL

The earlier indexed multinacci result gives exactly the three arch types and their ordered coding at m=3, the prefix equality, the substitution-length formula and the prefix density. The displayed sigma is a conjugate coding of the known substitution power, not a distinct derived system. The arbitrary-factor statements are not quoted verbatim in that record, but are immediate from its explicit arch structure together with the prior sharp-enough prefix discrepancy proposition. The failure is demonstrated coverage and direct implication, not failure to access literature or a mathematical counterexample.

## value

FAIL

The relationship between uniform subsequence universality and Tribonacci occurrences is mathematically natural. Here, however, the exact arch/prefix structure is already available, and the remaining all-factor envelope and sufficient constant merely apply the known blocks and subtract two known prefix bounds. No sharp discrepancy threshold, new endpoint rule, or other independent substantive remainder is established. Thus no scientifically valuable distinct narrowing of this frozen result is delivered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
