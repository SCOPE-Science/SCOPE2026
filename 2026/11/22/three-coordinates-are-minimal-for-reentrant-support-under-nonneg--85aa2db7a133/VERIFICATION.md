---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

In one dimension the sign is independent of t after truncating at zero. In two dimensions, the face x_1=0 has unique optimum x_2=max(b_2,0)/(d+t). The missing KKT condition is precisely c max(b_2,0)/(d+t)-b_1 >= 0, including equality. This function is monotone, and for b_1>0 has strictly negative limit, excluding a terminal zero set except the empty set. Repeat for coordinate 2. In the witness, the minors 3, 2 and 23/4 certify SPD. Eliminating coordinates 2 and 3 gives numerator q=(t-1/2)(t-1) and denominator D=(t+3)(t+1)(t+4)-(t+4)-(9/4)(t+1) for the first unconstrained coordinate. All coefficients of D±q are positive, bounding that coordinate between -1 and 1 and making the other two positive via their stationary equations. On the missing-coordinate face the outward gradient in coordinate 1 is -q/[(t+1)(t+4)]; this is nonnegative on exactly [1/2,1]. The KKT proof thus includes the tie endpoints. The eigenvalues shift by t; the distinct extremal eigenvalues imply strictly decreasing condition number. Strict KKT inequalities at 0, 3/4 and 2 persist by continuity of the relevant restricted inverses and gradients, proving robustness of reentry, not fixed transition locations.

## originality

PASS

The supported distinct result is the sharp dimension obstruction for arbitrary b, the monotone two-dimensional positive-b corollary, and the positive-b minimal robust witness. Nonnegative Tikhonov solution methods concern a genuinely overlapping model, but the passages inspected do not give these support-path conclusions. The Resultary matches about loss of positivity or boundary capture involve different quantities or parameters.

## value

PASS

The theorem rules out support reentry in the smallest dimensions and gives a sharp, exact, open-set counterexample to nested supports for positive data in dimension three. Improving conditioning does not rescue support monotonicity even along the standard isotropic path. The explicit thresholds and persistent strict signs make it useful as a minimal test for support-tracking methods, without making a claim about their runtime or individual iterates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
