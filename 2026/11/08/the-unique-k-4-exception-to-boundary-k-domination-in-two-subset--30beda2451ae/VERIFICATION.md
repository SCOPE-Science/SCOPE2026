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

Translate an ordinary k-dominating edge family H of size t in KG(2k+3,2) to d_H(u)+d_H(v)<=t−k for every nonedge uv. At t=k+2, a vertex of degree>=3 would be universal and impossible; degree 2 forces <=3 total edges; degree <=1 is a matching of at most k+1: thus t>=k+3. At equality t=k+3, maximum degree <=3. A degree 3 vertex leads to a K4 or impossible K4−e, forcing k=3 and six K4 edges. Otherwise all degree-2 vertices form a triangle and remaining 2k degree-1 vertices form a perfect matching. Counts are binom(2k+3,3)(2k)!/(2^k k!) plus binom(9,4) at k3. K4 selected edges have only one selected open Kneser neighbor and two closed-neighborhood members, so fail both tuple variants. Independently checked literal domination for K4 and triangle+matching at k3; examined full exhaustive k2,k3 verification source, not claiming to rerun its >2m candidates.

## originality

PASS

The exact triangle-plus-matching minimum k-tuple structure is already published by Cornet–Torres Theorem 20 (and following paragraph); Brešar–Cornet–Dravec–Henning Proposition 9 already proves equal numeric minimum sizes for all three variants. Their theorems do not classify ordinary k-domination minimizers, which have an extra K4 at k3. Originality lies in distinguishing ordinary minimizers from tuple/total-tuple minimizers and counting 126 exceptions.

## value

PASS

The one-parameter boundary k-domination classification isolates a genuinely exceptional coincidence of optimum cardinalities but not optimum families. The complete minimizer characterization and the first/unique separating K4 are useful structural domination facts, not a trivial restatement of an already-known scalar threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
