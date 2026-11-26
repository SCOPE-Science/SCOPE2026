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

Summing the logarithmic two-cycle equations fixes the midpoint by invertibility of the coexistence matrix. In antiphase coordinates the two forward equations are U_X(u)=alpha*w and U_Y(w)=beta*u, and negating the displacements gives the reverse equations. The scalar function U_L(t)=t-2atanh(t/L) has negative second derivative for positive t. Positive right sides force both loads above two, and multiplying the strict chord-slope bounds excludes equality as well as larger products. Conversely, w(t)=U_X(t)/alpha gives a positive residual near zero under the strict bound. The residual is negative at first contact with the positive zero of U_Y, or at the positive zero of U_X if there is no contact. Continuity gives an interior primitive cycle. At fixed X,Y, each chord-slope ratio can approach its upper bound only at amplitude zero, so both amplitudes vanish as the product approaches the threshold from below. Direct differentiation gives the stated determinant. This is not a stability theorem: at the boundary the trace is less than -2, so the other multiplier is below -1. The finite checker was inspected, not executed; its three reported reconstructions corroborate examples, and its four exclusions use the formula, not a search. The proof supplies the universal evidence.

## originality

PASS

The verified distinct claim is the global iff and disappearance of every antiphase cycle at fixed coexistence loads, allowing unequal loads and unequal positive couplings. Earlier symmetric exchange existence, complementary low-load exclusion, and bifurcation calculations overlap but do not imply that result. No claim of priority is made for the symmetric exchange threshold or the local characteristic factor.

## value

PASS

In a standard competitive map the result identifies the exact region permitting opposite oscillations, including unequal loads where exchange symmetry is unavailable. It distinguishes the existence boundary of any such orbit from numerical detection of stable attractors and controls all possible finite-amplitude branches as the boundary is approached. These are useful exact facts for bifurcation studies even without a multiplicity or attraction theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
