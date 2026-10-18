---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: Group generator rules yield m=p^(k-1) isolated nonunit rotations and the active K_((p-1)m,m,...,m), p reflection parts. General white-pair forcing analysis gives the polynomial and minsets. Independent exhaustive simulation on all 2^6 and 2^18 initial subsets verifies polynomials for p=3,k=1 and k=2. Rank2 p=odd k=1 has explicit rank2 Gram; k>=2 null-cone Gram gives rank3, and rank2 exclusion by >2 distinct isotropic lines. However these calculations are mathematical consequences of earlier complete-multipartite results.

## originality

FAIL

FAIL: Reddy–Samant 2023 already explicitly identifies the group graph as a complete multipartite component plus isolates. Fallat–Hogben 2007 survey, Example 2.19, gives the real symmetric minimum rank exactly 2 when third-largest part <=2 and 3 when third-largest >=3, reproducing the full k=1 versus k>=2 transition by substitution. Boyer et al 2018 Theorem 1 gives the three highest zero-forcing polynomial coefficients for every graph, while Resultary October 4 full general complete-multipartite characterization supplies the exact two-white forcing criterion and its count. Combined with compulsory isolates, all submitted coefficients and minimum sets follow immediately. These are stronger prior implications, not only matching terminology.

## value

FAIL

FAIL: The dihedral group application is natural, but its graph type and all claimed zero forcing/minrank consequences are specializations of published group structure and generic complete-multipartite formulas; there is no new graph-family classification or independent invariant beyond plugging in p,k. The gap transition is an arithmetic boundary already dictated by Fallat-Hogben Example 2.19. Correctness alone cannot create value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
