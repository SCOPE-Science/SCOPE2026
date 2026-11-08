# Review of the two-voter consensus–polarization threshold

## Correctness — PASS

The proof starts with the exact two-agent equation (8) from Ohlin, Bencherki and Tegling. Its residual-susceptibility update is \(u_{n+1}=u_n[1-c(1-u_n)x_n]\), rather than an update based on any extra factor of stubbornness. The monotone limits, two strict sufficient and eventually necessary tests, order-preserving parameter dependence and critical uniqueness ratio are all reconstructed in `RESULT.md`. On a critical orbit \(w_{n+1}-w_n=cu_n^2x_n\); telescoping proves \(u_n=cx_n-(c^2/2)x_n^2+O(x_n^3)\). This gives a reciprocal-gap increment \(c+(c^2/2)x_n+O(x_n^2)\), yielding the universal logarithmic term \((c/2)\log n\) with a finite remainder. Algebraic checker and representative classification diagnostics run successfully; finite diagnostics are not substituted for proof.

## Originality — PASS on inspected evidence

The primary 2022 paper's complete accessible text was compared at the exact recursion level, including its equation (8), sufficient Theorem 3.1, explicit comment on conservativeness in Remark 3.1, examples and appendix. Its criterion \(cx_0+	heta_0<1\) does not prove a unique boundary and does not supply a critical logarithmic correction. Published consensus analyses with exogenous changing matrices, and increasing-stubbornness models for multidimensional opinions, are different and do not directly imply this theorem. Searches for alternate descriptions of the critical separatrix, dual variables and asymptotic law did not uncover stronger exact coverage. Some relevant broader literature was accessible only at abstract level, and unindexed equivalent results remain possible.

## Mathematical value — PASS

A sharp separator between consensus and persistent polarization is a motivated missing invariant in this state-dependent voting model, directly addressing the original paper's acknowledged conservative basin. The coefficient of the subleading logarithm is not just a positive sign test: it quantifies critical slowdown and is independent of initial opinion separation. The conclusion distinguishes three global trajectory classes and gives checkable bounds on the implicit threshold.

## Restrictions and priority

The claim is deterministic and limited to two equal-weight, initially equally stubborn voters. The threshold is implicit; asymmetry, larger graphs, and stochastic updates are not covered. A 2022 conference publication predates the exactly dated January 19, 2023 public catalogue entry; the first circulation day has not been established. The journal-strength related full texts and some unpublished analyses have not all been inspected, so independent publication-priority verification is still warranted.

Self-review: passed. Independent audit: not yet performed.
