---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For n-element unordered four-symbol vectors x,y, a common three-symbol output exists iff Omega(x,y)=sum min(x_i,y_i)>=3, hence a code is a clique under Omega<=2. Heavy-coordinate packing bounds cardinality by four for n>=9, pure vectors attain; the source checker exhaustively searches nonexistence of cliques of sizes 12,7,6,6,6 at n=4..8. Independently implemented complete increasing-index bitmask clique backtracking and checked absence for each forbidden size, plus the explicit witnesses. Values 20 at n=3, 11 at n=4, 6 at n=5, 5 at n=6..8, and 4 at n>=9 are correct. The finite combinatorial searches prove only finite exceptional sizes, while heavy-coordinate argument proves infinite tail.

## originality

FAIL

Decisively covered. FULL published October 25 quaternary theorem proves exactly S4(n,n-3)=6 at n5, 5 at n6..8 and 4 at n>=9, including all constructions and stronger analytic upper bounds. FULL November 2 arbitrary-q theorem contains n>=6 via q=4. FULL October 18 graph-pairing theorem explicitly credits the already-known exact length-four one-deletion cardinality q+binom(q,2)+D(q,4,3), giving 4+6+1=11 when q=4. The remaining n=3 value 20 counts all three-multisets, a trivial equality. Hence the entire five-piece cardinality claim is already known, despite different finite certificates.

## value

FAIL

Scientific value as a new contribution fails because every segment is either an already published exact cardinality (n>=4) or elementary counting (n=3). Recomputing a published optimal-code table with alternative clique certificates supplies no distinct extremal structure or new mathematical consequence. The original claim cannot be made new by citing a different checker.

The dated certificate retains the supplied scientific assessment, sources and limitations.
