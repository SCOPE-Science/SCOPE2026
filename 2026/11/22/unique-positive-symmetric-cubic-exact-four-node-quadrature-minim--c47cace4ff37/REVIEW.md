# Scientific review of the symmetric four-node cubic-exact minimax quadrature

## Correctness — PASS

The admissible family contains every nonnegative centrally symmetric measure with at most four support nodes. Cubic exactness reduces to the single central second-moment equation. The Jordan-variation error is exactly the maximal discrepancy of the weighted cumulative distribution; one-sided tail steps give sharpness. Every four-atom probability rule has discrepancy at least \(1/8\). For any putative rule with discrepancy \(d\le d_*<1/7\), the rigorous inequalities \(a\le d\), \(b\le3d\), and \(v\ge b-d\) force the second moment to be at most \(9d^2-32d^3\), which is strictly below the required \(1/12\) for \(d<d_*\). Strict equality in this envelope forces the unique stated rule; two distinct tail steps attain the resulting error. The exact rational root enclosure and independent finite tests ran successfully.

## Originality — PASS, with bounded historical risk

The 2014 Aistleitner–Dick general Koksma–Hlawka result supplies the discrepancy framework but does not in its examined main theorem solve a positive weighted four-atom cubic-moment minimax problem. The accessible 2022 Komisarski–Wąsowicz article discusses at-most-three-node symmetric rules and a 3-convex ordering problem, not four-node Jordan-variation minimax optimization. Förster–Petras (1991) is genuinely close: its abstract explicitly analyzes optimal BV errors of positive quadratures, but the full article was not accessible for inspection, so an earlier constrained four-node formula remains a priority risk. No search-result absence is treated as a proof of novelty. The best available comparisons did not establish an equivalent or stronger covering statement.

## Mathematical value — PASS

The exact optimizer identifies a nontrivial cost of combining cubically exact moment matching with worst-case robustness to jumps. The sharp \(d_*\) exceeds the unconstrained four-atom discrepancy minimum \(1/8\), but improves the classical four-node Gauss rule's BV error by about 22.25%, while openly sacrificing degree-seven exactness. The unique balancing of three discrepancy contact conditions and a quadratic moment obstruction is a motivated optimal design result, not a trivial change of coordinates or a mere re-evaluation of a Gaussian rule.

## Scope, evidence, and residual uncertainty

The proof is self-contained in `RESULT.md` and corroborated by `check_quadrature.py`, which checks exact rational bracketing, moment conditions, attainment, random admissible designs, and a conventional benchmark. Random tests are not a completeness certificate. Asymmetric rules, extra nodes, nonpositive weights, and different integration measures are not classified. The 1991 article's unavailable full text is the primary historical-priority limitation; an independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
