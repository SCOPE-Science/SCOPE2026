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

Represent 3n=(3k+1)x+(3k+2)y with x≡y mod3 to obtain generators m=2k+1,u=3k+1,v=3k+2. Minimality follows m<u<v<2m. Since u+v=3m and u≡k,v≡-k modm, the Apéry set is W_j=min(ju,(m-j)v), j=0..2k, split at j=k; ±1 neighbors shift j by ∓2. Only j=k (h=1) and j=k+1 (h=1,2) satisfy both neighbor inequalities. Sum W_j proves genus; max W_j proves Frobenius. The k=1 boundary has gaps {1,2}, none isolated. Independently constructed coin-membership DP and direct quotient checks passed 49,345 bounded assertions over k<=140; unrestricted proof is the Apéry argument.

## originality

PASS

Cabanillas arXiv:1904.08240v2 develops general quotient generators, Frobenius, genus, pseudo-Frobenius and type, but not an exact isolated-gap set for this family (full PDF TOC, §1 and §5 inspected, keyword check). Smith (2022) provides general Apéry criteria and two-generator exact classification; Singh–Ram 2024 concerns embedding dimension 2 whereas Q_k has embedding dimension 3. Neither implies the parameter-uniform exactly-three isolated-gap positions without an additional residue classification. A high-relevance Smith full article was inaccessible, and an implicit family-specific corollary remains a genuine risk.

## value

PASS

Isolated gaps are a standard natural invariant related to perfect numerical semigroups. The threefold quotients of consecutive coprime generators are a canonical, infinite embedding-dimension-three family; a complete three-point isolation pattern and exact boundary at k=1 is an unknown, non-implied classification beyond the contextual genus/Frobenius and generic Apéry algorithm, potentially useful as test family for isolation and quotient theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
