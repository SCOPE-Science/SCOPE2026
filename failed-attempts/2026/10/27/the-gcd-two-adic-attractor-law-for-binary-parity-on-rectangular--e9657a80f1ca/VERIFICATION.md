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

The group-algebra update factors as (x+y)(1+xy)/(xy). Extending scalars preserves ranks; the two odd parts split into distinct roots and every local ring is truncated in the two directions at k and ell. Exactly g pairs have equal coordinates and g have inverse coordinates, with intersection only (1,1); outside them the multiplier is a unit. The nilpotent dimension is therefore k ell (2g−1). The stable image is the periodic set since its map is an invertible permutation of a finite vector space; the complementary nilpotent space gives the phase-fibre cardinality and equal basins per phase. At (1,1) each summand x+x^−1 or y+y^−1 starts in degree two and its power can be tested on one axis, giving sharp index max(1,k/2,ell/2). At any other zero pair the one-variable derivatives are nonzero, so the terms can be used as separate coordinates X,Y and the update is X+Y. For k≥ell, replacing X by W=X+Y leaves truncations W^k,Y^ell because k is a two-power and Y^k=0. This gives index k and rank ell at power k−1; the reversed inequality and k=ell work as stated. Thus the last rank drop for g>1 and M>1 comes from the 2(g−1) noncentral pairs; for k=ell=1 it is the entire nilpotent dimension. Uniform counting on the nilpotent part gives the stated fractions. For two dyadic circumferences only the central block exists and m,n≥3 make the extinction index max(m,n)/2. Bounded independent bit-rotation/rank checks at 13 pairs (including 16×32 and cases both inside and outside the frozen sample) replay with python3 /workspace/review-evidence/checks.py 5. Those checks corroborate the arbitrary-size argument; the supplied script and log were read, not executed.

## originality

FAIL

The stronger same-object all-rectangles nilpotent Jordan classification is demonstrably covered in Resultary 714a981ac90e. It implies the entire frozen stable-rank, clock, basin and peak-depth claim. That indexed record is dated later than the assigned record; this is a retrospective coverage decision under the current corpus, not evidence that the stronger record preceded the frozen work or that the frozen work copied it. External historical priority is unresolved.

## value

PASS

The scientific problem is a natural finite-state dynamics problem over an infinite family of graphs, not a recomputation of an isolated exact invariant. The dimension and clock reveal different roles of the odd gcd and dyadic sizes, and the peak-depth split distinguishes central and noncentral zero sectors. These exact structural quantities are useful for characterizing basins without enumerating exponentially many states. Current coverage of these results is addressed separately on originality; this value judgment does not credit any additional improvement over the stronger indexed theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
