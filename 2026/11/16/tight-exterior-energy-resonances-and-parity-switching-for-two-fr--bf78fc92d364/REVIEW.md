# Scientific review: tight two-frequency exterior-energy resonances

## Correctness — PASS

The theorem is proved for all exterior lengths \(h>0\), all distinct real frequency pairs, and arbitrary complex coefficients. The main proof gives both exact Gram forms: the cosine and sine basis is orthogonal on the symmetric input and exterior sets, and its denominator eigenvalues are strictly positive because \(|\sin d|<d\). Subtracting \(h\) from the two generalized eigenvalues yields quantities with opposite signs. Equality therefore forces exactly \(\sin((1+h)d)=(1+h)\sin d\). At consecutive half-odd-integer multiples of \(\pi\), the resonance function has strict alternating signs, establishing infinitely many interior roots and parity changes by continuity. A separate Taylor calculation proves the collision correction. The standalone finite checks agree with these formulas for the stated samples; no inference about all parameters is drawn from numerics.

## Originality — PASS relative to the inspected evidence

Ruizhe Zhang, *Optimal Extrapolation Bounds for Sparse Fourier Sums* (arXiv:2607.10501; first public 2026-07-11), studies exactly the two symmetric exterior prediction windows, including actual integrated transfer (Section 5.3, Proposition 5.6). It gives general \(k\)-term growth estimates and a worst-frequency **supremum**, not the present fixed-gap complete generalized spectrum or its sharp **infimum** over gaps. The previously published two-frequency leverage results supply exact evaluations at a **single exterior point** and their confluent limit. Integrating pointwise maxima does not determine the norm of an integrated operator, because maximizing coefficients can depend on the point. Independent source/statement comparisons found no equivalent two-tail spectral degeneracy or all-gap classification. This is a provisional literature-based originality finding, not proof of publication priority.

## Mathematical value — PASS

The exact spectrum answers the natural fixed-frequency-subspace energy extrapolation problem, and its sharp gap-design minimum is unexpectedly equal to the outer-to-inner length ratio. The complete resonance equation proves infinitely many **perfectly tight** transfer subspaces, not just approximate tightness, and shows universal parity switches in the worst-concentrated signal as the frequency gap varies. This exact two-mode boundary is relevant when general sparse Fourier transfer bounds are not sharp enough to guide spacing choices. The positive small-gap deficit quantifies the approach from a nearly confluent Fourier pair.

## Closest comparisons and residual risks

The exact pointwise two-frequency works address a different functional (evaluation instead of integrated energy), while Zhang's integrated transfer addresses a different optimization (unrestricted worst-gap instead of gap minimization). Older two-atom time-window/frame-design results might present the same elementary trigonometric eigenvalue condition in another notation. The theorem is specific to symmetric equal-length exterior windows; it does not solve general sparse extrapolation or noise-robust inverse recovery. Independent mathematical audit has not been carried out.

Self-review: passed. Independent audit: not yet performed.
