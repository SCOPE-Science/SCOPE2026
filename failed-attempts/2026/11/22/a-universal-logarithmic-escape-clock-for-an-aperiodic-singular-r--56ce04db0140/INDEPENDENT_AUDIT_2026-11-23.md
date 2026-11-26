# Independent mathematical audit

## correctness

PASS

Directly conjugating the frozen rational map by w=u+1 gives F(w)=-w-2/w. It never reaches zero on a real nonzero input, reverses sign, and strictly increases absolute value. Therefore t=w^2 satisfies t_(n+1)=t_n+4+4/t_n. The lower bound t_0+4n and summation give t_n=4n+O(log n); 4/t_k-1/k=O(log(k+1)/k^2) is absolutely summable and yields the finite orbit-dependent centered residual, with coefficient +1 on log n. Sign alternation gives opposite parity escapes, and increasing t excludes cycles. Escape from every compact and invariance applied to its indicator, followed by compact exhaustion of the punctured line, exclude invariant Borel probabilities. Read the supplied VERIFICATION.md and verify.py without executing them; finite tests are supplementary. The fault is not mathematical falsity.

## originality

FAIL

The advertised two-term escape law and finite renormalized residual are a direct specialization of a prior stronger simple-parabolic Fatou-coordinate theorem, once the exact one-line squared-coordinate reduction is made. Neither the sign/escape check needed to enter the attracting petal nor the measure corollary supplies an independent uncovered scientific claim. Alexanian's numerical example does not itself supply the logarithmic coefficient. The rejection rests on inspected prior theorem coverage, not the unavailable chapter or lack of an exact title match.

## value

FAIL

The clean proof usefully explains the old numerical example, but the clock is a mechanical specialization after one change of variables, and the affine shift, monotone escape, sign alternation and ensuing no-cycle/no-invariant-probability conclusions are immediate from the same one-line expression. No substantively independent nonroutine claim survives to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
