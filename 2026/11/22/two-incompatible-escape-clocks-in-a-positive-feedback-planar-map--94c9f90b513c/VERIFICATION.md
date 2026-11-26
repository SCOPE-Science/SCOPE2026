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

The exact identity y_(n+1)+r y_n=c x_n gives |y_n|+|y_(n+1)|≥|c||x_n|/r since r>1. Multiplying the two positive x-update factors gives the stated quadratic lower bound with equality when y_n=cx_n/r and y_(n+1)=0. For a≥1 and x_0≠0 each parity subsequence is bounded below by iteration of Z↦Z+qZ² with q=ab|c|/r>0, so it diverges. Eventually qZ>1, after which log(qZ) at least doubles per two steps, giving a common positive lower constant for the √2 base. When x_0=0, |y_n|=r^n|y_0|. Escape leaves every compact set, so stationarity and dominated convergence for compactly supported test functions force an invariant Borel probability to be supported at zero. For 0<a<1 the two points with |y|=(1−a)/b and x=(1+r)y/c are nonzero fixed points, proving sharpness. At a=r, b,c>0 the update gives x'≥rx and 0≤y'≤cx≤cx'/r, strictly in the cone interior, with the two boundary rays exchanged. Substitution yields y_(n+2)=(r²+bc x_n)y_n there. On the zero-ray subsequence the x return map is r²z+rbc z²; t=rbc z has t' = t²+r²t. The normalized log(t)/2^m has positive summable increments 2^(−m−1)log(1+r²/t_m) and is eventually positive, giving a finite positive limit. In the interior both parity sequences of y diverge, so x_n/x_(n−1)→∞; the previous y is at most cx_(n−2), making y_n/(cx_(n−1))→1. Hence log(bc x_n) obeys a Fibonacci recurrence with a bounded forcing tending to zero. Dividing the exact Fibonacci convolution by φ^n gives termwise limits dominated by a summable geometric sequence in forcing index; a lower homogeneous comparison for log((bc/2)x_n) from two eventually positive consecutive terms makes the limit positive. At odd times on the boundary x is r times the previous zero-ray value once that subsequence starts, so the √2 base is genuinely sharp in original time.

## originality

PASS

Zhou et al. give the exact recurrence and fixed points, so neither is new. The sharp all-state positive-feedback escape (including the resonant equality cases) and two distinct positive finite normalized logarithmic limits do not follow from their fixed-point or numerical analysis. The polynomial branch's golden-ratio degree growth is a meaningful general-dynamics antecedent, not a real-orbit limit theorem.

## value

PASS

The positive-feedback chamber in an existing map has a sharp global escape criterion that matters for interpreting attractor diagrams and excludes all nontrivial invariant probabilities there. At one set of resonant parameters the generic cone interior and exceptional rays have incompatible superexponential clocks; an algebraic degree alone would miss the ray growth. The exact lower growth base and its sharp witness are structural, not a finite simulation or an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
