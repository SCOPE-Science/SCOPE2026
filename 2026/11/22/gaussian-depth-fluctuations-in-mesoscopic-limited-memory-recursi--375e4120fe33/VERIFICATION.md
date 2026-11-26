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

The backwards ancestry exposes independent parents at strictly decreasing labels, with a uniform jump on 1,...,b_l. Telescoping the potential gives F(n)=D_n+M+R with a bounded centered martingale increment and nonnegative R. A width boundary m-1 to m has drop 2/[m(m+1)], is charged by at most one jump and is charged at most b_l times. At that crossing v is of order l for large l because b_l=o(l), hence b_l=O_beta(m). The widths increase by at most one, so the total charge is O_beta(1+log n) pathwise, including the finitely many initial labels. The per-step bracket is (b_l-1)/(3(b_l+1)). Martingale isometry and the deterministic remainder give D_n/F(n) -> 1 in probability and in mean; the bracket divided by F(n) tends to 1/3 both in probability and in expectation by removing finitely many small labels. The bounded-increment triangular-array CLT and Cauchy–Schwarz for the variance of M+R give the two distinct limiting assertions. F(n) ~ 2 n^(1-beta)/(1-beta); its exact discrete form, not merely that leading term, is used for centering.

## originality

PASS

The closest primary work establishes this same tree model and first-order geometry. The inspected literature and distinct indexed records do not give the second-order last-born-depth result, floor-sensitive centering and limiting variance together or imply them from their stated results. The already known model and first-order scale are not credited as new.

## value

PASS

This addresses second-order uncertainty in a natural existing model. The explicit centering is accurate on the fluctuation scale with integer-window effects intact, and the variance statement controls actual moments rather than simply naming a Gaussian limit. The pathwise boundary-charge argument is the substantive bridge beyond a first-order law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
