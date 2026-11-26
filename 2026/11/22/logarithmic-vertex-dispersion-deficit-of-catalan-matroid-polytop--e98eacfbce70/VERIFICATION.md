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

Each distinct 0/1 Dyck incidence vector is extreme, so uniform vertices are exactly uniform paths. Reflecting ballot prefixes gives the stated prefix counts; reversing suffixes and summing the two possible signs after time 2j yields the bivariate Catalan series. With s=√(1−4x), t=√(1−4y), subtract the zero-suffix term C(x)−1 to obtain F=(s−t)/(s+t). For D=x∂x+y∂y one has DF=F/(st) and D(D+1)F=(s²−t²)/(2s³t³)=S(x)yS′(y)−xS′(x)S(y); comparing homogeneous degrees gives (L−j)a_j a_L/[n(n+1)], n=j+L. Division by the Catalan count gives the stated odd-step bias, equal to the preceding even-step bias by the local swap at odd positive height. Endpoints are forced. The coordinate variances (1−μ_i²)/4 then yield the inertia, and independent sampling doubles it for squared pair distance; the hypersimplex has all means 1/2. To verify the constant and error independently, put b_j=(a_j/4^j)², E(z)=Σe_jz^j with e₀=1 and e_j=b_j−1/(πj)=O(j⁻²) for j≥1. DLMF's real singular expansion and absolute convergence imply E(1)=log(16)/π. The coefficients of E(z)log(1/(1−z)) are E(1)/n+O(log n/n²) by splitting j≤n/2 from the tail, and those of E² are O(n⁻²). Together with the exact log-squared coefficients 2H_{n−1}/n, this gives T_n as stated. Since j b_j=1/π+O(1/j), U_n=n/π²+O(log n). The squared bias weight (n−2j)²/n² accounts for −4U_n/n² and the two unit endpoint contributions give the frozen formula for n/2−I_n. Substitution confirms both constants and both remainders. An independent exact ballot dynamic program (python3 /workspace/reviews/evidence_4_5.py) verified all marginals and the distance identity for n=2..50; it did not execute the supplied script, and the exact check is not the asymptotic proof.

## originality

PASS

The supported distinct assertion is the exact and sharp asymptotic uniform-vertex Euclidean second moment, equivalently independent Dyck up-step Hamming overlap. The Catalan embedding, identity of squared distance with Hamming distance on binary vertices, variance–distance relation and elliptic expansion are not new. An exact earlier ordinary-time excursion mean would determine the step marginals; the best matching finite-height study was not accessible in full, leaving an explicit risk about this ingredient.

## value

PASS

Uniform vertex dispersion is a natural comparison with the hypersimplex in the same coordinate metric. The calculation establishes that the Dyck constraint changes macroscopic pair distance by a sharply quantified logarithmic deficit, not by an order-n or a bounded loss, and gives its explicit constant and a controlled error. This is not a claim about volume, covariance eigenvalues or the full distance distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
