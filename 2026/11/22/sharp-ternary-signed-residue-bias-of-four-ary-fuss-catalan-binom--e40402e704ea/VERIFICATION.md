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

In 4n=n+3n, a carry forces divisibility by 3; without carries the only Lucas factor equal to -1 mod 3 is the adjacent pair 11. Leading and trailing zeros contribute unit factors. This gives the symmetric signed transfer matrix B, with B² rows (3,0,1), (0,2,1), (1,1,1) and B³=3B+I. Thus D_0,D_1,D_2=1,3,4 yield the rational series and positive recurrence at all complete cutoffs. Its simple dominant pole gives the stated positive residue coefficient; the other real roots have moduli 2 cos(2pi/9) and 2 cos(4pi/9). Conversely, on a ternary-aligned block whose upper digits are admissible, fixing the first upper digit amounts to an extra terminal matrix factor selecting that digit; the absolute block sum is at most ||B^(j+1)||_2=theta^(j+1) for a block of length 3^j. There are at most two blocks per scale in [0,X), giving the uniform bound; the nearest lower power of three proves the lower bound for max_{X<=Y}. The unsigned transfer growth is greater than theta, proving relative equidistribution on the nonzero support. Exact independent binomial counts through n<3^7 gave D_0..D_7=1,3,4,10,15,34,55,117 and (N_0,N_1,N_2)=(572,106,51) at L=6 and (1834,235,118) at L=7. Replay: branches/cd8a9689-48f6-4c88-9154-3d152592732d/independent_direct_counts.py and check_log.md. The frozen checker was read, not executed. Its loop checks L=7 but does not print that row, contrary to the minor reporting detail in RESULT.md:70; this does not affect the finding.

## originality

PASS

The support count, numerical recurrences as sequences, and standard digit-transfer methods are known. What remains distinct is the identification of the signed unit-residue count for this binomial diagonal with that particular sequence, and the sharp signed bound for arbitrary prefixes. The strongest same-family and same-method matches were inspected at statement level and do not give that identification or bound.

## value

PASS

The result resolves more than support density or a table of complete intervals: it identifies a systematic positive bias between the two unit residues and proves the optimal discrepancy scale uniformly over arbitrary ternary prefixes. This quantitative refinement of the natural nondivisibility census needs sign information discarded by valuations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
