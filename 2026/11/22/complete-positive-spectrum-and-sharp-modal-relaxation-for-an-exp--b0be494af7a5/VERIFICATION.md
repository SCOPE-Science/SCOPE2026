---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Splitting at zero gives block triangular T, with the positive block dominated in its powers by the ordinary ordered Volterra simplex and the negative block unitarily equivalent to cK_q. Away from zero the triangular Riesz projection preserves the negative-block multiplicity. For the midpoint approximation, a principal submatrix has nondecreasing prefix lengths at least the row indices. Its determinant is zero if any lengths repeat, and otherwise the lengths are exactly 1,…,k and the determinant is 1 before rescaling. The contributing limiting domain is {0<u_k<1, 0<u_j<q u_(j+1) for j<k}; the inequality chain printed at RESULT.md line 43 is not literal notation for this region, but the immediately preceding minor condition and the stated substitution specify it. Scaling u_j=q^(k−j)t_j gives the stated coefficient, and the factorial majorant gives locally uniform determinant convergence. Norm convergence, stability of the ranks of isolated Riesz projections and Rouché's theorem transfer all nonzero eigenvalues with multiplicity, using the established real-simple zero theorem. Multiplication by h is unitary on the specified weighted space, so projection removal and Gelfand's formula give the exact rate. The scaled entire functions qE(q,−w/q) converge locally uniformly to −w+w²/2: Rouché on a circle of radius 3 and separate neighborhoods of 0 and 2 counts exactly the first two roots on the scaled domain; bounded-z convergence gives the first root tending to 1. The genus-zero product and Newton identities give the three power sums without an operator trace-class premise. check.py and requirements.txt were inspected, not executed; the 1,847 conditions are finite corroboration only.

## originality

PASS

Prior work provides the conditioned chain, principal eigenfunction and eigenvalue, persistence generating functions displaying the deformed-exponential denominator, and the zero theorem. The supported distinct claim is the exhaustive operator spectrum with algebraic multiplicities and the exact weighted-space operator-norm modal rate, not discovery of the denominator or of the conditioned chain. The closest distinct indexed result is about worst-state total variation, a different norm and conclusion.

## value

PASS

The transition is not treated as self-adjoint and a leading survival mode alone does not give the worst weighted-norm relaxation. Exhausting its nonzero modes with simplicity provides the exact rate for a specified conditioned-chain space, separates it from uniform TV behavior, and identifies its large-expansion scale independent of the innovation endpoint a. The rate and power sums are useful exact spectral quantities beyond the previously known leading mode.

The dated certificate retains the supplied scientific assessment, sources and limitations.
