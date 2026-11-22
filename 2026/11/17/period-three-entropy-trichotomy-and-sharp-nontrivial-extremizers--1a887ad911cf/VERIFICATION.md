---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Three successive rows A,B,C under R form period3 iff F(A)=B xor C, F(B)=C xor A, F(C)=A xor B. Encoding each temporal column as 3 bits yields exact 64-vertex directed pair-column transfer M_r; all n>=3 fixed states are closed walks tr(M_r^n), not simulations at sampled n. Independently implemented all 256 directed 64-node graphs, SCC cycle classification and exact 56-step integer infinity-row-sum comparison: found exponential129, bounded116, empty11 with exact empty rule list 167,173,181,189,191,229,231,239,247,253,255; for each of the other 252 rules max row sum(A^56)*8^56<25^56. Independently computed 16-node SCC characteristic polynomials for rules50,76, both t^7(t-1)(t^2+t+1)^2(t^4-2t^3-2t^2-6t+3). Trace identity and Newton recurrence give S_n plus 6 when n multiple3. For 51 and 204 sitewise identity/complement implies R^3=id on all 4^n states. All-length conclusions rely on finite transfer identity and exact integer certificate, not small-n trace simulation.

## originality

PASS

Qualified best-of-knowledge: previous ECA and second-order reversible rule studies classify dynamical properties, reversibility, and particular rules, but do not in inspected accessible material give the all-rule third-iterate trace/entropy trichotomy, exact nontrivial maximizers 50/76 and rigorous uniform integer spectral gap. Full Formenti–Kamilya 2024 chapter and Takesue 1989 article remain inaccessible; these carry an explicit originality risk, not a false claim of noncoverage.

## value

PASS

An exhaustive sharp phase diagram of a canonical 256-rule reversible CA class for an exact dynamical observable, with strict uniform spectral gap and unique nontrivial maximizers, is a natural complete classification. The quartic all-n trace recurrence and exact 11-rule emptiness set are reusable invariants not mechanically given by first-order image entropy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
