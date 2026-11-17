---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For circular w=a^pba^qb and 2m<=n, any Abelian-square halves contain either 0 or 1 marked b each; 0 requires 2m<=max(p,q). One in each half is feasible exactly when shorter circular mark separation min(p,q)+1<=2m−1, and a starting offset max(0,m−min(p,q)−1) witnesses sufficiency. Summing the two disjoint types proves z_m and N with all p,q>=0, including zeros and n=2. At odd n, the permitted intervals cover every half-length, with N=(n−1)/2+(|p−q|−1)/2 and sharp |p−q|=1 equality. Independently enumerated every cyclic factor/half-count for 900 (p,q) pairs 0..29.

## originality

PASS

The full most relevant Bhattacharjee 2026 v2 primary manuscript explicitly conjectures odd-length prefix inequality for non-equivalent Abelian-square types; its exact proposition on a^p b^q is for two cyclic runs, not the four-run two-isolated-marker family. The exact two-marker type profile and termwise odd bound solve a motivated special case. Boundary p=0/q=0 is acknowledged as prior two-run. Resultary three-mark record not stronger for two marks.

## value

PASS

The proposed lower bound for non-equivalent circular Abelian square types is a live combinatorics-on-words question. A complete four-run family formula proving the stronger termwise property, with all equality cases, is a meaningful structural partial solution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
