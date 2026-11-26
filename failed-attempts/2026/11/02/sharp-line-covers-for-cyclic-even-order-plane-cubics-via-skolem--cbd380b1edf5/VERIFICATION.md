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

The stated formula and prime specialization are correct. At 2m lines, Bézout forces a disjoint partition into trisecants. The rational flex gives the zero-sum group law for distinct points; summing over the partition contradicts the unique nonzero involution. The Skolem positions give a partition of [1,3m] into triples (j,m+a_j,m+b_j) with the first two terms adding to the third. For each triple not containing h=3m, taking both signed orientations covers its six distinct signed residues. The remaining residues are exactly 0,h,±a,±b with a+b=h and 0<a,b<h, a≠b. The three stated zero-sum triples have distinct entries and cover these residues. This also works for m=1 (triples {3,1,2}, {3,5,4}, {0,1,5} modulo 6). Each triple yields a rational line. In the prime family p≥5, the cubic is smooth with a flex at infinity, cubing permutes the field, the character sum vanishes, and there is just one nonzero rational two-torsion point. In the invariant-factor decomposition the smaller factor divides gcd(p−1,p+1)=2 and cannot be 2 with this two-torsion. The congruences on m=(p+1)/6 follow, and both prime classes are reduced modulo 24. The supplied verify.py was inspected, not executed. Its frozen checks are bounded examples, not the basis of the quantified conclusion; the review relies on the symbolic proof and classical Skolem existence.

## originality

FAIL

A distinct, earlier indexed Resultary finding explicitly proves the same exact cover number for every cubic with a rational flex, point count divisible by three, and precisely one nonzero rational involution. Cyclic groups of order 6m meet those hypotheses for every m, not just the Skolem orders. It also provides a constructive cyclic witness. The prime-family cover number follows from that theorem and the frozen elementary point-count and two-torsion calculation. The Skolem proof is a different construction but does not establish a distinct cover-number theorem. This is affirmative prior coverage, not a failure of access or a finding of mathematical falsity.

## value

FAIL

The one-line involution defect is a meaningful geometric invariant, but its exact general formula and explicit cyclic witnesses already exist. The frozen work narrows the parameters and gives an alternate Skolem implementation without establishing an additional needed covering invariant, reach or advantage. The prime specialization is a direct application, not an independent gap filled.

The dated certificate retains the supplied scientific assessment, sources and limitations.
