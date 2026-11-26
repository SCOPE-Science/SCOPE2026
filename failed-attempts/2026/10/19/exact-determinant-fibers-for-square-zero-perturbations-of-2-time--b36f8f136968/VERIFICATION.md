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

For a nonzero square-zero matrix the image and kernel are the same line L. In a basis starting with L, each perturbation is tE12 with t nonzero, and det(A+tE12)=det A−ct, where c is the lower-left entry of A. Thus an invariant line supplies q−1 central points and any other line supplies one point to every off-center fiber; add N=0. Trace is fixed. In characteristic two, trace zero requires a scalar diagonalizable part and the unique scalar gives a square-zero difference by Cayley–Hamilton; nonzero trace gives q/2 split determinant values via the involution r↦s−r. In odd characteristic the split-distinct set has (q−1)/2 values by the discriminant test, and the scalar correction is one exactly when the original discriminant vanishes. Summing the corresponding fibers reproduces all case counts, including q=2 and q=3.

## originality

FAIL

The earlier Resultary record 7b7188752131 already gives the complete needed level-set calculation in its proof. It expands det(A−N) as det A plus a linear form on the nilpotent cone, identifies precisely e(A) annihilated rays, and counts the zero and prescribed nonzero levels. Replacing the prescribed value −det A by z−det A gives the frozen fiber formula verbatim after changing N to −N. The decomposition multiplicities then follow mechanically from the degree-two split-polynomial count and the possible scalar correction. The difference between invertible and diagonalizable summands in the two headlines does not remove this implication.

## value

FAIL

The invariant is naturally motivated, but the submitted result makes no independent exact advance beyond the earlier ray-level calculation. The multiplicity recasting only sums its already-determined fibers over the split degree-two characteristic polynomials and adds the unique possible scalar term. This is useful exposition, not a surviving scientific claim under the exact-invariant standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
