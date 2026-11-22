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

# Verification of the Franel correlation spectrum

The supplied `verify_franel5.py` is standalone and uses only Python's standard library. Run it with `python3 verify_franel5.py` from the directory containing this document. The verifier reconstructs 450 Franel numbers independently from their binomial-cube definition and compares quadratic-character results to the digit-product formula, checks all five outgoing-carry coefficients, calculates the unwrapped shifted products for 151 shifts at each of depths \(1,2,3,4,5\), tests the stabilized recurrence and sharp equality classification at 1999 positive shifts, and checks all signed spectrum multiplicities for the 3905 shifts across depths one through five. All those computations completed successfully.

The proof's infinite coverage rests on two exact algebraic transitions, not these finite checks: the unwrapped digit-carry recurrence with coefficients \((4,0),(0,1),(-1,0),(0,-1),(1,0)\), and the signed/unsigned state matrices whose \(r\)-th powers give \(Q_r(t)=1\) and \(P_r(t)=((1+4t)^r+1)/2\). The existence of fixed-shift limiting correlations and eventual constant errors follows by induction on shift. The only unresolved matters concern historical priority, other primes and moving shifts. No independent audit is implied by this document.
