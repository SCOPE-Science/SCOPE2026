# Scientific review

## Correctness — PASS

The normalized BDF polynomials follow directly from the defining sum. The coefficient at index two enforces sharp necessities \(\alpha\leq7/32\) for BDF4 and \(\alpha\leq13/150\) for BDF5; the corresponding BDF6 coefficient is positive for all \(\alpha>0\). At each positive boundary, an exact coefficient recurrence checks indices \(1\) through \(999\), and rational Schur reductions give zero-free disks for the remaining generating function factors. Cauchy's inequality and a signed binomial coefficient lower bound control every index \(n\geq1000\). Raising the boundary power to a smaller positive exponent transfers strict coefficient negativity to the full sharp interval by a nonnegative formal composition. The executable `verify.py` checks exact Schur fractions, finite recurrence signs, and strict infinite-tail constants. A finite computation is not substituted for an infinite argument.

## Originality — PASS on documented comparisons

Lubich's 1986 generating symbols and Schädle–López-Fernández–Lubich's 2005 high-order convolution quadrature treatment establish the antecedent numerical framework but not these sharp BDF4/BDF5 all-index sign intervals or the BDF6 obstruction. López-Fernández–Płociniczak's 2023 analysis explicitly treats negative convolution weights as a useful condition, investigates BDF2 and numerical behavior, but does not obtain the present BDF4/BDF5 classification. Jin–Li–Zhou's high-order starting corrections concern distinct convergence statements. The related lower BDF2/BDF3 sign classifications do not imply the BDF4/BDF5 theorem, because both the generating polynomials and their zero-free radii change. Actual source comparisons and semantic database searches revealed no explicit dominating theorem; this is not a claim that searches prove absence of prior publication.

## Mathematical value — PASS

The sign of every historical convolution weight is an explicit structural assumption in comparison and discrete energy methods for fractional-in-time evolution; knowing its exact validity range matters for applying those methods to higher BDF formulas. The theorem locates two sharp admissibility frontiers and proves the sixth-order obstruction, with all-index rather than experimentally sampled sign guarantees. Its analytic zero separation and tail certificate address a genuine gap not resolved by a cheap finite sign test. The theorem stops short of claiming solver positivity or convergence.

## Source comparisons and limitations

Primary full-text sources inspected include Ch. Lubich, *Discretized Fractional Calculus* (1986); A. Schädle, M. López-Fernández and C. Lubich, *Fast and oblivious convolution quadrature* (arXiv:math/0504461v1, 2005-04-22); M. López-Fernández and Ł. Płociniczak, *Convolution Quadrature for the quasilinear subdiffusion equation* (arXiv:2311.00081); and B. Jin, B. Li and Z. Zhou, *Correction of High-Order BDF Convolution Quadrature for Fractional Evolution Equations* (2017). Remaining priority risks include unindexed specialist discussions of high-order CQ coefficient sign ranges and independent replication of the Schur/Cauchy proof.

Self-review: passed. Independent audit: not yet performed.
