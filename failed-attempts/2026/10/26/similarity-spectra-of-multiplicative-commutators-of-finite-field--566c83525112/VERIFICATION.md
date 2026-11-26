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

Write E=A−I and F=B−I. The identity (K−I)BA=EF−FE shows rank directly. With t=0 at most one of EF,FE is nonzero, and K=I+EF−FE is identity or a rank-one square-zero update. Covector counts after imposing annihilation of the image line (and, when independent, both distinguished vectors), divided by q−1, give the stated identity and rank-one counts. For t≠0 the image plane has the simultaneous standard form E=e12, F=t e21 and splits off the common fixed space; explicit multiplication gives determinant one, trace 2+t² and nonzero off-diagonal entries, with det(K−I) on the plane equal to −t². The partner count is q^(2n−3) per t. In odd characteristic the conic (y−t)(y+t)=4 gives q−1 pairs, hence split-minus-irreducible count −2 on nonzero t and exactly the stated repeated cases. In characteristic 2 the Artin–Schreier equation has right side t^(−4), with absolute trace equal to that of t^(−1). In n=2 the t=0 nonidentity count is zero. Normalization by T gives the claimed limits; uniformity within GL classes is unconditional (the fixed-A probabilities are for similarity-invariant events only). Inspected the bundled finite checker and its recorded output; the all-field proof above does not use those tests.

## originality

FAIL

The strongest catalogue comparison goes beyond sharing a parameter: for pairs of transvections the commutator similarity type is a deterministic elementary pushforward of the product similarity type, and the indexed exact two-transvection convolution gives all the needed product masses. The arithmetic split totals are elementary character/trace counts for that pushforward. This is mathematical coverage, not a historical priority finding; the product record has a later catalogue date.

## value

PASS

An all-field similarity law for a natural random pair distinguishes exact rank, repeated roots and splitting, rather than just existence or a few dimension-two cases. This general question is meaningful; the direct pushforward calculation does not itself leave a distinct surviving claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
