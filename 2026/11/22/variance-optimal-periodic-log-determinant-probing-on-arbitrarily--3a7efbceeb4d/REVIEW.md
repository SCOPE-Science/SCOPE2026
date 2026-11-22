# Scientific review: variance-optimal periodic log-determinant probing on weighted paths

## Correctness — PASS

The claim has exact quantifiers: all orders \(n\ge2\), every positive path conductance and killing rate, all \(1\le k\le n\), exact independent class-supported Rademacher quadratic forms. The trace variance is \(4\sum_{i<j,\,\mathrm{same}}B_{ij}^2\). The strictly diagonally dominant path operator has resolvent factors \(d_su_s(i)v_s(j)\) with increasing left and decreasing right factors. Squaring any positive resolvent mixture, including its mixed-shift terms, yields strictly positive interval coefficients. Counting same-color pairs within each interval produces the exact nonnegative gap certificate, and balanced length-\(k\) windows force the unique periodic partition. The matrix logarithm and fractional powers satisfy the stated integral representations. The uniform-path variance density follows from the bilateral Fourier symbol, polynomial localization, and uniform geometric decay.

Exact standard-library reproduction produced 21,587 passed rational / Fourier assertions. An independent floating-point calculation directly forming matrix logarithms produced 21,184 comparisons. Neither finite test is used as a replacement for the infinite proof. Scientific limits include the independent-probe model and the strictly positive assumptions.

## Originality — PASS on inspected evidence, subject to publication-priority risk

The closest foundational trace papers study either Hutchinson variance in general, hierarchical distance-color probing for inverses, or approximations to matrix-logarithm traces. In the full relevant portions of Han–Malioutov–Shin (2015), Dorn–Enßlin (2015), and Stathopoulos–Laeuchli–Orginos (2013), no theorem comparing every fixed-budget partition for the heterogeneous-path matrix logarithm was found. Benzi–Rinelli–Simunec (2023), §3.1, proves that periodic banded coloring has the *fewest colors necessary to separate vertices to a selected distance*; that statement does not imply minimum variance among partitions using a fixed number of independent Rademacher quadratic forms, including irregular partitions that violate the distance constraint.

The resolvent-only weighted-path setting is a related, already covered special case. This result additionally treats the log determinant and arbitrary positive mixtures, where squaring an integrated Green kernel creates cross terms absent from any single-shift result. Those cross terms require the interval-square argument and are explicitly evaluated. No unqualified priority or independent-certification claim is made. The strongest remaining risk is an unindexed theorem about Monge/interval-decomposable kernels or a matrix-function-specific probing theorem not located by the named searches.

## Value — PASS

Log determinants and fractional inverse traces are well-motivated matrix-function quantities. Computing the determinant of a standalone tridiagonal path is already linear-time, so the log-determinant result is a sharp variance-design benchmark, not an algorithmic speedup claim for that special graph; the fractional-function extension and interval certificate are the structural contributions. The theorem completely resolves the *fixed quadratic-form budget* variance design on an entire heterogeneous path class, without requiring equal edge weights, uniform killing, or equal class sizes. The interval decomposition provides a quantitative certificate for each suboptimal candidate; the homogeneous-path formula gives an explicit per-site variance improvement \(4\operatorname{Li}_2(r^{2k})/k^2\). These are structural and quantitative results, not a recalculation of a known small example. The estimator's exact-action cost restriction is material and stated.

## Closest literature and limitations

Han, Malioutov and Shin (arXiv:1503.06394, 2015-03-22) demonstrate stochastic log-determinant trace approximation, without exact path partition optimization. Stathopoulos, Laeuchli and Orginos (arXiv:1302.4018, 2013-02-17) establish hierarchical inverse probing and distance-color principles. Dorn and Enßlin (arXiv:1504.02661, 2015-04-10) use stochastic integral log-determinant estimation. Benzi, Rinelli and Simunec (Numer. Math. 2023, DOI 10.1007/s00211-023-01368-6) give matrix-function probing and minimum-color distance constraints, a distinct optimization objective.

Limitations: exact matrix-function quadratic forms; independent sign blocks rather than arbitrary couplings; positive conductances and killing rates; fixed budget in the asymptotic formula; same-document textual inspections and semantic searches cannot exclude all future or unindexed equivalent results.

Self-review: passed. Independent audit: not yet performed.
