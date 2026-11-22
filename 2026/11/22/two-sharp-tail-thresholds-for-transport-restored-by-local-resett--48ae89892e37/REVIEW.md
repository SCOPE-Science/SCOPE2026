# Review of the random-comb weak-return tail theorem

## Correctness — PASS

For every finite periodic comb, independent exact finite-state stationary equations yield \(v_N(r)=(p-q)/(1+aN^{-1}\sum_i\tau_r(L_i))\), and the reflected-tooth resolvent proves the formula for \(\tau_r(L)\). Its exact increments satisfy \(1-\delta_n(r)\le\min(1,rn^2)\) and converge on the scale \(n\sqrt r\) to hyperbolic profiles; tail summation proves all five regimes. The stationary-volume law follows from the strong law and its infinite-mean truncation form. The included standard-library checker independently verified 90 finite cases, with full rational generator solves. The finite checks supplement, but do not replace, the infinite-volume arguments.

## Originality — PASS (priority-qualified)

A detailed comparison was made with the full primary article and supplementary derivations of Sarkar and Gupta (arXiv:2205.15232), full relevant sections of Elliott and Wheater (arXiv:0704.0188), Kotak and Barma (arXiv:2204.05357), and the full accessible 2023 continuum-comb resetting article. The first paper uses coupled backbone/tooth bias and gives general stationary-current formulas; it does not state the independent symmetric-tooth five-regime power-tail law or its sharp tail-index-three susceptibility threshold. The 2007 and 2022 biased-comb papers have no local returns. Closest published geometric-tooth asymptotics use outward tooth bias and exhibit log-periodic coefficients. The new claim does not treat the known exact current method as original. A broader mathematical Tauberian theorem or an unindexed study could still imply this classification; priority is not certified independently.

## Mathematical value — PASS

Two different, physically meaningful moments of the quenched tooth-length distribution determine whether turning local returns off destroys transport (first moment) and whether infinitesimal returns have finite linear response (third moment). The exact constants and two logarithmic endpoint laws are not fixed by the zero-reset transport threshold alone. The theorem solves this natural continuum of polynomial-tail cases rather than a hand-picked finite sample or a routine numerical increment; it directly describes how local return mechanisms regularize traps in random branched media.

## Scope and residual risks

The result is for stationary finite rings followed by a thermodynamic limit, not an asserted almost-sure trajectory speed on an infinite comb. Vertical jumps have rate one, are symmetric, and tooth lengths are iid with exact asymptotic survival tail. The originality assessment remains a self-review; independent literature-priority verification remains outstanding.

Self-review: passed. Independent audit: not yet performed.
