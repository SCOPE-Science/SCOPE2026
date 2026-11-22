# Scientific review: mesoscopic common diagonals in two random triangulations

## Correctness — PASS

The probability of including a diagonal of small-side index \(r\) is \(C_rC_{n-r-2}/C_{n-2}\). All ordered pairs partition into disjoint short arcs, properly nested short arcs, and crossing pairs; only the first two are feasible. Their exact counts and joint probabilities yield the displayed finite factorial-moment identity. Uniform Catalan ratios and a summable difference kernel show that the disjoint pairs contribute the square of the mean and that nesting contributes \(2(4/\pi-1)\) times the mean. The Euler beta integral gives the explicit constant. The weighted extension follows by the same Riemann sum and domination, with no unproved independence step. The `check.py` file passed 94 exact finite assertions and reported consistent numerical limits. Risk: finite tests do not by themselves establish the asymptotics; the written analytic proof bears that burden.

## Originality — PASS, with residual priority risk

Noy (December 16, 1999) treats diagonal lengths and longest diagonals of a **single** uniform triangulation. Ralaivaosaona, Ravelomanana and Wagner (2018) enumerate pairs of triangulations by the **total** number of common diagonals, without a length-resolved square-root variance. The 2026 published conditional-correlation study covers pairs of compatible diagonals in **one** triangulation, not independent-pair coincidences and a universal rescaled covariance functional. Searches of prior local research records and the mathematical literature found no matching statement or stronger result implying the universal factor. All these classical Catalan and relevant newer ingredients remain credited. Risk: an unindexed length-marked generating function or an earlier probability treatment of paired Catalan trees could imply the present theorem; full historical priority requires independent review.

## Value — PASS

The square-root band is a natural rarity window: a particular diagonal at that scale has joint occurrence probability of order \(n^{-3/2}\), while there are order \(n^{3/2}\) eligible candidates. A Poisson heuristic would predict equal limiting mean and variance, but nested shared diagonals retain a nonzero clustering covariance and produce the exact, band-independent Fano factor \(8/\pi-1>1\). The general test-function covariance gives a reusable second-order description of overlap geometry relevant to matching Catalan trees/triangulations. This is a motivated structural scale and dependence mechanism, not an arbitrary small finite computation.

## Closest literature and scope

The comparison concerns the complete statements and their implications, not keyword similarity. Neither a single-triangulation longest diagonal result nor an unmarked total-common-diagonal generating function supplies the length-window covariance without an additional marked asymptotic analysis. The resulting theorem does not establish a complete limiting distribution, independence of disjoint bands, or historical uniqueness.

Self-review: passed. Independent audit: not yet performed.
