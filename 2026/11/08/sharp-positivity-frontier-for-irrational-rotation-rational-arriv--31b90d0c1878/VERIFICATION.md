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

PASS for every irrational phi/pi in (0,1), epsilon in [0,1], all finite orders and nonnegative finite waiting times. The exact matrix-product density from Peralta is e^-T[1-epsilon+epsilon S_k]. Interior partial sums W_m=Re A(1-z^m)>=alpha=Re A-|A|, whereas the terminal W_k=Re A-Re(Bz^k)>=beta>alpha. Summation by parts with nonincreasing a_j=e^-T_j gives S_k>=alpha a_1+(beta-alpha)a_k>alpha for finite times (alpha<0). Irrational rotation makes W_m dense arbitrarily close to alpha; a final long finite wait realizes inf S_k=alpha, with strict interior negative witnesses above threshold. Thus epsilon_star=1/(1-alpha) and critical finite-density positivity. Normalization and non-Markovian consequence correctly rely on original full primary theorem, not claimed new. Independent direct matrix products for k=1..7 reproduced the oscillatory density.

## originality

PASS

PASS best-of-knowledge: Peralta March 2026 introduced exact matrices, density identity, normalization and non-Markovian obstruction but stated a strictly smaller sufficient epsilon bound 1/(1+M); inspected full HTML did not state the global necessary/sufficient range, its unattained critical normalized-density infimum or the endpoint proof. No broader Resultary published result was found beyond this same assigned claim.

## value

PASS

PASS: sharp full parameter domain and a strict/nonuniform critical boundary are motivated by deciding exactly when a known algebraic non-Markovian arrival construction defines genuine positive joint densities. Exact necessity and endpoint property materially improve the original sufficient admissibility interval; a specialized natural construction merits a complete sharp boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
