---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The actual theorem and both formulas are correct. For monotone maps of the same rank, write the interval kernel blocks and the images in increasing order. Mutual inverse requires each image to meet the other's blocks exactly once; conversely the two transversals force g(a_i)=b_i and f(b_i)=a_i for the ordered images of f and g, proving the composites. Frozen line 18 incorrectly describes the one-sided statement as an equivalence: f=(1,1,2) and g=(1,1,3) have im(g) a transversal of f's kernel, but fgf=(1,1,1). The required two-sided criterion at lines 14–17 is nevertheless true by the ordered argument just given. At rank two, b<=c maps to cut a and images b,c+1; the new images straddle c, and a straddles the old images in the cut convention a<=a<b. The other branch reverses this substitution, and all straddling cases are idempotent. At rank n-1 the missing value of each map must belong to the other's doubled block, which the two exchanged nonidempotent branches satisfy, and z=c or c+1 gives exactly the idempotents. The bounds on the cuts and image values hold also for n=3 where the classes coincide. Constants and the identity cover rank one and rank n. An independent in-memory enumeration checked both formulas, order, rank, inverse equations, involutivity and the idempotents on 987 map/formula pairs for n=3 through 9, counting the coinciding class twice at n=3. The bundled n=3 through 8 code was inspected, not executed.

## originality

FAIL

A distinct indexed record has the same closed formulas and properties at both extremal ranks for every n>=4. The only difference from its stated range is the coinciding n=3 class, and the compared formulas and proof apply there without modification. This is demonstrated overlap, not a priority inference from dates or a failure based on the unread 2019 paper.

## value

PASS

As mathematics, a uniform closed involution fixing all idempotents at two natural ranks strengthens mere existence of a permutation matching and handles the odd-size case not reached by rank-two divisibility. This intrinsic value is already represented in the catalogue. The overlapping n=3 boundary does not by itself motivate a new result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
