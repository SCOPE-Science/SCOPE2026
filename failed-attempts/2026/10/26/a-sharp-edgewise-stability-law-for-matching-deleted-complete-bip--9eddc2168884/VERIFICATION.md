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

With orthonormal columns U spanning the full gradient space, the surviving restriction U_R has full column rank by connectedness. Its Gram matrix is I-U_D^T U_D; applying the inverse update gives A+C(I-H)^(-1)C^T. The deleted block has H=(2/n)I-J/n^2, giving the printed kernel. For a row with no marked endpoints the sharing entries are positive and nonsharing negative. For a row with one mark, the only additional nonnegative entries are the n-t opposite-side matches with one mark, of size (t-1)/(n(n-2)D_t), including the t=1 zeros. For two marks the only additional strictly positive entry is the reversed-index edge: its numerator n(n-4)+2t is positive also for n=3, when t>=2. Counting the sharing columns and these extras gives absolute row sums 3-4/n plus, respectively, 2(n-2)/(nD_t), 2(t-1)(n-t-1)/(n(n-2)D_t), and zero. These rely on row sum one. The product in the middle correction is at most (n-2)^2/4, so type zero wins whenever present. At t=n only type two survives. Choosing the maximizing row's signs attains the norm; subtraction yields the two drops and ratio D_(n-2)=(n-2)(n+1).

## originality

FAIL

A distinct Resultary record gives the full same projector, row-type comparisons and terminal-drop ratio in the language of two-way additive least squares. The orientation change is only a sign convention on the vertex potentials: a cell fitted as a_i+b_j is the gradient from potential a_i on the left to -b_j on the right. This is demonstrated equivalent coverage in the inspected catalog, not evidence of earlier publication, a priority judgment, or a claim of dependence.

## value

FAIL

The induced norm is a motivated measure of worst-case bounded edge error; in isolation the abrupt last-deletion effect is a meaningful structural fact. As a distinct contribution to the inspected record, however, the full exact fact and its mechanism are already supplied in the equivalent additive least-squares result. The compact transfer-current expression is an algebraic restatement of that projector; it does not leave a new usable invariant or new scope to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
