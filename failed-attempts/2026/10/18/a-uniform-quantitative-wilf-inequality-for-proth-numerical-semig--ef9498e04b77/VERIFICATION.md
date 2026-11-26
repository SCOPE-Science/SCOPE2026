---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The published generators give multiplicity M+1 and e=k+1. The matching Apéry formula is N_{-j}=jM+(M+1)T(j), 0<=j<=M, where T counts greedy coins of sizes 2^i-1, 1<=i<=k. Summing the representatives and subtracting M/2 yields g=M(M-1)/2+sum T(j). The k-1 lower digits have sum at most k: each is at most two and any two in a higher position forces smaller digits to vanish, so at most one digit is two. The top digit is at most one because M<=2^(k+1)-2^n<2(2^k-1). Thus g<=M(M-1)/2+(k+1)M. The residue -M gives c>=M²+(T(M)-1)(M+1)+1>=M²+1. As ν=c-g, the Wilf number is kc-(k+1)g and substitution yields exactly the frozen polynomial. Dividing its linear coefficient by k-1 gives 2k+5+6/(k-1)<=4n+5<M (k>=4, k<=2n-1, M>=3*2^n; the last inequality holds at n=3 and persists by induction). This proves strict positivity on the full parameter domain. Independent residue shortest-path spot checks with a generator list extending above k covered five odd parameters including n=3,m=3 and n=3,m=7. The first gave g=334,c=652, margin 938 versus bound 328; the latter 1706,3309,6309 versus 4429. Replay: python3 -I /tmp/opencode/frozen_audit_small_checks.py, proth(). Frozen code was inspected, not run.

## originality

FAIL

The exact polynomial was not located verbatim, but is a direct uniform corollary of earlier stronger results on this same family. The exact genus/Apéry formulas, their published digit restriction, and the known embedding dimension already entail the stated polynomial by the elementary upper sum and single-residue lower estimate below. No new extremal Apéry or genus information or additional nonstandard structural lemma is needed. This is demonstrated prior coverage by implication, not an assertion that the exact inequality was printed in the earlier paper.

## value

PASS

Wilf's inequality across the full nontrivial odd Proth family is a natural question going beyond the parameters in the earlier explicit Proth Wilf theorem. A positive uniform algebraic margin can be useful as a documented corollary without needing exact Frobenius maximization. This utility does not make it a distinct finding when the complete implication from existing structural results is so direct.

The dated certificate retains the supplied scientific assessment, sources and limitations.
