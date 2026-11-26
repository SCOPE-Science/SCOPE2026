---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Every length-m binary target embeds one symbol per image block. Greedy matching of a length-(m+1) word succeeds iff some block is the first to consume two symbols; its two symbols are then exactly the indexed ordered pair in the statement. The all-constant targets show absence is possible. Counting prefixes by their last symbol gives updates (p+q,q) or (p,p+q), starting at (1,1). Distinct subsequences of the source ending in a newly appended symbol are exactly the old distinct subsequences with that symbol appended, so their endpoint counts plus one obey the same updates. With the right-to-left matrix product M_k, M_{k+1}=(JM_k)^2, det(JM_k)=-1, and Cayley–Hamilton gives a_{k+1}=2+t_k^2 and t_{k+1}=a_k t_k, with (a_0,t_0)=(2,1); a_k+t_k is the sum of all entries. The logarithmic recurrence has characteristic roots 2 and -1 and the bounded forcing log(1+2/t_j^2); division by 2^k gives the stated absolutely convergent series, and the sum a_k+t_k has the same exponential base as t_k. This is an unrestricted algebraic check of RESULT.md lines 42–91; checker.py was inspected, not run. The packaged finite test is not an independent run or an all-order proof.

## originality

FAIL

A distinct same-day indexed result states exactly the general local characterization and equivalent all-level Thue–Morse recurrence. Its arbitrary-source transfer formula also gives the general D(v)+1 identity by the standard distinct-subsequence endpoint update, with just a shift of the two initial counts. The growth-base series is obtained by solving the scalar logarithmic recurrence already implied by the matched trace formulas. This is demonstrable scientific overlap and direct implication, not a finding about which record came first.

## value

FAIL

An exact enumeration of this family is a natural goal, but the package repeats its decisive all-level recurrence. The general count bridge is just the already available transfer with shifted endpoint counts, and the limiting base follows by routine solution of a first-order forcing term in a linear logarithmic recurrence with roots 2 and -1. No independently useful non-mechanical remainder justifies a repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
