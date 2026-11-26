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

For a fixed label-two support H in K_n with t edges, the exact best weight is N_n+t-ab, where a and b count root vertices of degree zero and one: an edge outside H sees d_H(u)+d_H(v) defenders and all ab eligible edges must be zero at optimum. Let c=n−a−b. If c>0 and b is even, 2t≥b+2c makes ab−t at least c(b+1) below the value Q_n(b)=b(n−b)−b/2 from a matching on b vertices. If b is odd, integrality gives an extra 1/2 loss; b−1 and b+1 are feasible even sizes and the two changes from Q_n(b) sum to −2, so one matching loses at most 1 and still strictly wins. Thus every optimum support is a matching. The matching weight is N_n+4r²+(1−2n)r, with unique nearest feasible integer to (2n−1)/8, namely floor((2n+3)/8); no ties occur because 2n−1 is odd. The labels are forced by the conditional optimum, so counting labelled partial pairings gives exactly the factorial formula. This covers n=3 and the entire permitted range. An independent direct original-adjacency check agreed for all supports through n=6, also testing every ternary labelling through n=5.

## originality

PASS

The strongest inspected overlaps use a materially different admissibility condition or a comparison that does not preserve weight. No equivalent determination of the standard perfect parameter, optimum matching support, and exact optimizer count was found in the bounded checks.

## value

PASS

Triangular graphs are a canonical highly symmetric family, and imposing uniqueness of the defending neighbor changes the order of the minimum from ordinary Roman’s linear value to quadratic. The degree-class argument proves an actual rigidity result, not just an example giving the optimal weight: every optimizer has a unique matching support with a forced labelling. This yields an exact count usable independently of the scalar parameter and identifies why ordinary-Roman polynomial information is inadequate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
