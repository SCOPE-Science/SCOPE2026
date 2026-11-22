# Scientific review: weighted complete-bipartite Schur norms

## Correctness — PASS
The claimed formula applies to all integers \(a,b\ge2\) and all real edge weights \(t\). The positive-semidefinite symbol criterion proves exact contractivity on the interval \(ab|t|^2\le1\). Above this threshold, the explicitly constructed positive-order certificate has two semidefinite residuals and diagonal bound \(1+2(abt^2-1)/(2ab|t|+a+b)\). A separately calculated unit-vector trace-norm witness attains the same bound. The discriminant, determinant, normalized witness and exact trace identity were algebraically rechecked. Finite arithmetic diagnostics passed 909454 assertions; the analytical certificates prove the universal result. The infinite-dimensional formula follows from an explicit diagonal-expectation/unitary-conjugation decomposition and finite-corner lower bounds.

## Originality — PASS relative to inspected evidence
The closest exact published statement is the \(|t|=1\) looped-complete-bipartite projection formula. Another sharp statement handles the \(a=1\) star for arbitrary real weights. Their union does not imply the weighted \(a,b\ge2\) formula, phase boundary, or double-infinite limit: for example, an exact value at one weight does not establish the threshold or the nonlinear rational branch. Christensen provides the positive-order variational method and Davidson–Donsig discuss transitive factorization, but neither inspected article states this three-parameter closed-form theorem. The motivating tree transference paper concerns intermediate Schatten classes and tree geometry, while complete bipartite graphs with both parts of size at least two contain cycles. Remaining risks are earlier equivalent symmetric-matrix norm calculations and priority not fully decidable by indexed searches.

## Value — PASS
The exact threshold identifies precisely when a natural bipartite covariance-like Schur filter ceases to be completely positive and becomes norm amplifying. The sharp rational branch determines the full amplification for arbitrarily unbalanced finite classes, while the countably infinite double-class limit has a different, simple law. These are motivated structural phase distinctions in a natural symmetric multiplier family, not a restatement of the known idempotent endpoint or a finite table calculation.

## Limitations and evidence
The theorem is restricted to real cross-edge weights and operator/completely bounded endpoints, not general complex phase patterns or \(S_p\)-norms for intermediate \(p\). Mathematical priority beyond the inspected material is not certified. The accompanying `VERIFY.py` is a diagnostic exact-arithmetic checker; it is not a substitute for the universal upper/lower certificate proof in `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
