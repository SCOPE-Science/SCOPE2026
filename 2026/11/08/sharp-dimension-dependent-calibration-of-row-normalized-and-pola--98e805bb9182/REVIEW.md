# Scientific review

## Correctness — PASS

The claimed efficiency is exactly the standard spectral/nuclear dual alignment evaluated at a Gram eigenvalue problem. The proof bounds its denominator by \(H_m(\lambda_1)\), maximizes that scalar expression under the exact row-statistic spectral constraint, and supplies an admissible full-rank equicorrelation equality witness. The separate polar-gap supremum follows from the thin SVD and the upper and lower Gershgorin edges, with explicit extremizers or a positive-definite approximating sequence. Independent finite numerical/SVD cross-checks of the formula were carried out by `verify.py` (10699 assertions), but finite sampling is not a proof for all parameters.

## Originality — PASS (best-knowledge, priority not certified)

The motivating RMNP paper defines the row-ratio statistic and motivates row normalization, while a subsequent Hessian-structure study obtains exact agreement for diagonal Gram matrices and a different study analyzes normalization after polar factors. Those studies do not supply the sharp constrained finite-dimensional minimax efficiency and polar-gap formulas or the threshold for uniform dimensional calibration. An older abstract matrix-norm extremal theorem could potentially specialize to this statement. The earlier norm-constrained LMO framework already includes both row and spectral optimizers; the sharp finite-coherence cross-norm comparison is the assessed addition. The standard duality and Gershgorin ingredients are not claimed as inventions.

## Mathematical value — PASS

The result replaces a qualitative large-ratio heuristic for an actually measured numerical-optimization diagnostic with an exact attainable worst-case assessment and a necessary-and-sufficient dimension-scaled criterion. The phenomenon remains material on strictly positive-definite Grams and is not a pathology of missing rank. It is a one-step deterministic model, not a convergence theorem or an assertion about unequal-row momentum measurements.

Self-review: passed. Independent audit: not yet performed.
