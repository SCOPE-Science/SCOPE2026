---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Use the standard reduced complete quotients α_j=(√D+m_j)/q_j, whose conjugates are in (−1,0); this holds initially and is preserved by the continued-fraction step. In particular √D−q_j<m_j≤A. Reversal of the integer numerator is the classical least-period symmetry. Independently, the involution I(α)=−1/conj(α) sends α_j to (√D+m_j)/q_{j−1}, sends α_1 to the terminal quotient, and reverses the Gauss step on the reduced cycle since I(α_j)=a_{j−1}−conj(α_{j−1}) for j≥2. Thus m_r=m_{r+1} for the even least period, and q_r C=2m_r. If q_r=1 then m_r=A, which is already the terminal state and contradicts leastness. If q_r=2 then C=m_r is A or A−1. Otherwise 3C≤2m_r≤2A. The case A=1 causes no spurious zero value since C>0. For D=(3t)²+3 the midpoint q=3 gives C=2t, and the next state is (3t,1), proving least period two and sharpness. For C=A−2 the bound leaves precisely A=3 through 6, and an independently written integer-state census of all 36 candidates confirmed the exceptional periods [1,6], [2,8], [1,1,2,1,1,8] and [4,12] for D=15,20,21,39 respectively. The census can be replayed via /workspace/branches/d7bf490b-3a87-4a68-b58e-3fc38a047141/audit_census.py; it agrees with an independent stop-on-repeat-state enumeration. Read VERIFICATION.md and verify.py without running the supplied code. The exact finite calculation establishes the offset classification only after the universal reduction; the result is not a classification of all attainable smaller C.

## originality

PASS

Credit the classical reversal identity and the already covered sharpness family. The distinct contribution supported by the comparison is the sharp denominator-gap restriction for all even least periods and the resulting exhaustive first-offset classification, including the unique longer-period D=21 among those exceptions. The inspected prior statements on central parity, block patterns and short periods neither state that universal restriction nor supply the four-case classification. This is a bounded best-of-knowledge decision.

## value

PASS

The central quotient is singled out canonically by the least-period symmetry. The theorem gives an optimal scale bound below the two large midpoint values, and an actual finite classification of the first lower deviation across unrestricted radicands. This rules out infinitely many otherwise plausible midpoint patterns and reduces the first-offset query from unbounded period computations to 36 exact cases. The useful result is that universal cutoff and its exact consequence, not recomputing familiar individual continued fractions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
