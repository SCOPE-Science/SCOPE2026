---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

With j dissenting leaves on K_(1,m), leaf conversion rate equals j while first hub flip hazard is (j/m)^q. Competing exponential clocks yield exactly product_{j=k+1}^m [1+j^(q-1)/m^q]^-1 for Pr(K_m<=k), with P_m the k=0 product. Each j<m factor strictly increases in q; q=1 gives (m/(m+1))^m<1/2; q=2 gives >1/2 (separately m=2), hence unique q_m in (1,2), q_2=log_2(3). For fixed q>0, logarithms reduce to improper Riemann sum integral_x^1 u^(q-1)du=(1-x^q)/q and uniform log remainder since max_j t_j->0; this yields CDF exp(-(1-x^q)/q), atom e^(-1/q) at zero and q_m->1/log2. These are first-reversal statistics, not unrestricted fixation equality. Actual verify.py inspected, its finite rational recurrences are only supporting tests.

## originality

PASS

Best-of-knowledge original combination of exact first-hub-flip stopping distribution, entire atomic limiting distribution, and sharp half-probability q threshold on a star under a specified nonlinear flip rule. Inspected principal nonlinear-voter literature studies general ordering and mean-field/network dynamics; no found source states this exact first-reversal law. The standard exponential race is credited as standard, not new.

## value

PASS

Leader-stability before a first actual hub reversal is a natural stopping-time observable in nonlinear social contagion; a universal e^(-1/q) survival and sharp q threshold give motivated exact finite-to-large-star information, not a mere arbitrary tiny-instance count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
