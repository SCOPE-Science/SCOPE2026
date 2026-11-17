---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The floor identity reduces F(n) for p∤n to gcd(n,t_(n mod p))=1, with F=0 on p multiples because k≥2. CRT proves pQ is a period, and no period can omit p or any ell|Q by constructing contradictory translated residue tests. Fiberwise coprime density is (1/p) sum phi(t_r)/t_r; power-residue coset identity follows from k-th power map. Expanding phi/t with the Möbius divisor sum, the principal term yields 1/zeta(2), and nonprincipal character sums by Polya–Vinogradov yield O_k((log p)^2/sqrt p); g=gcd(k,p-1)≤k controls uniformity. Independent exact floor/gcd and divisor-period checks for 48 triples matched. A finite check is not the proof of infinite p or uniform analytic bound.

## originality

PASS

The result concerns exact prime-denominator rational monomial floor-gcd periods and coset-dependent densities; the published irrational-coefficient asymptotic literature and rational linear cases do not imply these. The uniform transition rate is a natural complement, with classical character bounds explicitly credited.

## value

PASS

Sharp least-period and full density classification for natural rational higher-degree integer-part coprimality, plus a quantitative transition to the irrational-like density; coset stratification makes the arithmetic structure explicit rather than a renamed formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
