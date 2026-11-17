# Eight-site saturation of the centered-Hilbert stability bound for cyclic morphological opening

## Finding

For every integer \(n\ge2\), define the flat cyclic two-site opening \(O_n:\mathbb R^n\to\mathbb R^n\) by
\[
(O_nx)_i=\max\{\min(x_{i-1},x_i),\min(x_i,x_{i+1})\}
=\min\{x_i,\max(x_{i-1},x_{i+1})\},
\]
where indices are interpreted modulo \(n\). This is erosion by the two-site structuring element followed by its adjoint dilation. Put
\[
H_n(h)=\left(\sum_{i=0}^{n-1}(h_i-\bar h)^2\right)^{1/2},\qquad
\bar h=n^{-1}\sum_i h_i.
\]
The sharp global two-input Lipschitz coefficient \(L_n=\sup_{H_n(x-y)>0}H_n(O_nx-O_ny)/H_n(x-y)\) obeys the complete saturation classification
\[
L_2=0,\qquad 1<L_n<\sqrt3\quad(3\le n\le7),\qquad
\boxed{L_n=\sqrt3\quad\text{for every }n\ge8.}
\]
For every \(n\ge8\), the coefficient \(\sqrt3\) is attained by explicit pairs of arbitrarily close inputs, not only approached in a limit. Thus eight sites are the exact first cycle size at which the universal replication bound is attained. The result is about the two-input centered Euclidean seminorm, not single-input variation or pointwise stability.

A structural equality criterion underlies the cutoff. If a strict-order region of the opening has row-selector matrix \(A\) and \(c_j\) is the number of rows selecting input coordinate \(j\), then \(\max_j c_j\le3\). The induced centered-Hilbert norm of this branch equals \(\sqrt3\) **if and only if** at least two columns have multiplicity three. Such a region is possible exactly when \(n\ge8\).

## Assumptions and scope

The input signals are arbitrary real vectors indexed by an unweighted cycle; the two-site opening uses periodic boundary conditions and flat (zero-height) structuring elements. The distance is the centered Euclidean seminorm, so constants have zero distance. Since \(O_n(x+a\mathbf1)=O_n(x)+a\mathbf1\) for every real \(a\), the quotient Lipschitz coefficient is well-defined. No positivity restriction is imposed on inputs.

## Proof

**Selector reduction.** For generic inputs with pairwise distinct entries, site \(i\) is unchanged unless it is a strict local maximum. At a strict local maximum, the output is the *larger* of its two neighbors. Thus on every strict-order chamber the opening is a linear row-selector map \(x\mapsto Ax\): each row of \(A\) contains one entry equal to one and all others zero. Each input coordinate \(j\) may be selected by its own output row and by at most two adjacent rows, hence its replication multiplicity \(c_j\le3\). In fact a strict local maximum is not selected by its own row, nor by an adjacent row, and has multiplicity zero.

Let \(P=I-n^{-1}\mathbf1\mathbf1^{\mathsf T}\) be orthogonal centering. For centered \(h\),
\[
\|PAh\|_2^2\le\|Ah\|_2^2=\sum_j c_jh_j^2\le3\|h\|_2^2.
\]
Every row-selector fixes constant vectors, and consequently this is the bound on the quotient centered-Hilbert norm. The opening is continuous and piecewise linear with finitely many such chambers. Integrating along generic input segments, then taking limits for nongeneric segments, establishes \(H_n(O_nx-O_ny)\le\sqrt3 H_n(x-y)\) for **all** \(x,y\).

**Equality criterion.** Equality in both inequalities requires a nonzero centered \(h\) supported on columns with \(c_j=3\), and also \(Ah\) centered. In particular there must be at least two such columns, since a nonzero vector supported on only one coordinate cannot have mean zero. Conversely, if \(c_r=c_s=3\) for distinct \(r,s\), take \(h=e_r-e_s\). Then \(h\) is centered and \(Ah\) is centered, since its coordinate sum is \(c_r-c_s=0\); also \(\|Ah\|_2^2=6=3\|h\|_2^2\). Thus the branch norm is exactly \(\sqrt3\) precisely when at least two columns have multiplicity three.

**Seven-site obstruction.** Every multiplicity-three source requires **both** its neighboring positions to be strict local maxima that copy this source. Two different multiplicity-three sources therefore require four *distinct* strict local maxima: the same output row cannot copy two sources. On a cycle of length \(n\ge3\), strict local maxima are pairwise nonadjacent, so there are at most \(\lfloor n/2\rfloor\). If \(n\le7\), four such maxima are impossible. Hence every selector branch has norm strictly below \(\sqrt3\). There are only finitely many selectors, so their maximum is also strictly below \(\sqrt3\), including across chamber boundaries.

**Exact attainment from eight sites onward.** Fix \(n\ge8\). Define the base signal \(x\) by assigning value three at sites \(1,3,5,7\), value one at sites \(2,6\), and zero at all other sites. For any \(0<\varepsilon<1\), let \(y=x+\varepsilon(e_2-e_6)\). The local maxima at \(1,3\) copy site \(2\); those at \(5,7\) copy site \(6\); sites \(2,6\) retain their own values, and all other outputs have zero perturbation. Therefore
\[
O_ny-O_nx=\varepsilon(e_1+e_2+e_3-e_5-e_6-e_7).
\]
Both the input perturbation and the output perturbation are centered, and their squared Euclidean norms are respectively \(2\varepsilon^2\) and \(6\varepsilon^2\). Their quotient is exactly \(\sqrt3\) for every eligible size and for arbitrarily small \(\varepsilon\). These inputs also exhibit the two multiplicity-three columns.

**Strict expansion below the saturation size.** For each \(n\ge3\), choose a strict-order input with only one local maximum, at site \(1\), whose larger neighboring site is \(2\); for instance take \(x_1=n\), \(x_2=n-1\), \(x_3=n-2\), ..., \(x_{n-1}=2\), \(x_0=1\). In a sufficiently small perturbation, its selector copies site \(2\) into row \(1\) and fixes every other row. Apply the centered perturbation \(h=e_2-e_0\). Then \(H_n(h)^2=2\) and \(H_n(Ah)^2=3-1/n\), so the local squared quotient is \((3-1/n)/2>1\). It is achieved by sufficiently nearby actual input pairs. For \(n=2\) the opening maps both sites to their common minimum, hence its centered output is always zero. Combining the cases proves the classification.

## Verification

Run `python3 check_opening.py` with standard-library Python. The checker enumerates all distinct-order selector patterns for sizes \(3\) through \(8\), verifies their replication counts and the existence of two three-fold columns only at size eight, checks the exact rational attaining input pairs for sizes \(8\) through \(60\), and tests the two-input bound on 14,500 independently generated rational pairs. These finite checks corroborate the unrestricted analytic proof; they are not used as substitutes for its infinite family of inequalities. The source file is embedded with this result, not borrowed from any other record.

## Relationship to prior work

Maragos and Schafer (1987, Parts I and II) establish the mathematical morphology of erosion, dilation and opening, the max-min representation of related filters, and their connections to medians and stack filters. Their treatment supports the operator definition but does not state the centered-Hilbert two-input amplification bound or its eight-site sharpness cutoff. Related published work on *weighted path total variation* for finite-window minima and maxima uses a different seminorm and studies a different stability property; such results do not imply the centered-Euclidean sharp constant for the cyclic composition. The distinction is not terminological: an exact norm of each component does not in general yield an exact norm of its composition. The present result uses the branch replication and the two-source equality obstruction.

## Limitations

The result concerns only the two-site flat opening on finite cycles with uniform observation masses and the centered Euclidean seminorm. Although it classifies precisely when the universal \(\sqrt3\) ceiling is attained, it does not compute the exact intermediate sharp constants for each of the five dimensions \(3\) through \(7\). It does not cover longer or nonuniform structuring elements, nonperiodic boundaries, weighted variances, multivariate grids or different composition orders. Earlier formulations not indexed by the literature searches remain a priority risk; no independent mathematical audit has been performed.

## References

1. P. Maragos and R. W. Schafer, “Morphological Filters—Part I: Their Set-Theoretic Analysis and Relations to Linear Shift-Invariant Filters,” *IEEE Transactions on Acoustics, Speech, and Signal Processing* **35** (1987), 1153–1169, doi:10.1109/TASSP.1987.1165259. IEEE records publication on 1987-08-31. https://ieeexplore.ieee.org/abstract/document/1165259/
2. P. Maragos and R. W. Schafer, “Morphological Filters—Part II: Their Relations to Median, Order-Statistic, and Stack Filters,” *IEEE Transactions on Acoustics, Speech, and Signal Processing* **35** (1987), 1170–1184, doi:10.1109/TASSP.1987.1165254. Author-hosted open text: https://robotics.ntua.gr/wp-content/uploads/publications/1987_MaragosSchafer_MorphologicFilters-part2_ieeetASSP_%2Bcorrections1989.pdf
3. J. Masci, J. Angulo and J. Schmidhuber, “A Learning Framework for Morphological Operators using Counter-Harmonic Mean,” arXiv:1212.2546, first posted 2012-12-11. https://arxiv.org/abs/1212.2546
