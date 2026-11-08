# Sharp two-color stochastic-probing transition on complete bipartite resolvents

## Finding
Let \(K_{m,n}\) be the complete bipartite graph with positive integer part sizes \(m,n\), let \(L\) be its combinatorial Laplacian, and let \(B=(\mu I+L)^{-1}\) for \(\mu>0\). Among all partitions of its vertices into **exactly two nonempty color classes**, estimate \(\operatorname{tr}B\) by one independent Rademacher quadratic form supported on each class. The optimal partition can always be chosen with one entire original bipartition side monochromatic; in fact **every** optimum has that property. The usual proper bipartition is variance-optimal if and only if
\[
\left(\frac{n}{\mu+n}\right)^2(m-1)\le n,
\qquad
\left(\frac{m}{\mu+m}\right)^2(n-1)\le m.
\]
If either inequality fails, moving some vertices of that side into the other class strictly decreases the variance, despite creating same-color edges. Both inequalities cannot fail simultaneously. In particular, on a star \(K_{m,1}\), the usual coloring is suboptimal precisely when \(m-1>(\mu+1)^2\).

For the complete finite-parameter solution, define
\[
\alpha=\left(\frac{n}{\mu+n}\right)^2,\quad
\beta=\left(\frac{m}{\mu+m}\right)^2,\quad
c=\frac{1}{\mu(\mu+m+n)},
\]
\[
F_L(x)=\alpha x(m-x)+nx\quad (x=0,\ldots,m),
\qquad
F_R(y)=\beta y(n-y)+my\quad(y=0,\ldots,n).
\]
Let \(C_*\) be the larger of the maxima of these two finite concave sequences. Then the **exact global minimum variance** equals
\[
V_*=4c^2\left[\alpha\binom m2+\beta\binom n2+mn-C_*\right].
\]
The maximizers of \(F_L\) are exactly the integers nearest \((m+n/\alpha)/2\) after clipping to \([0,m]\); those of \(F_R\) are exactly the integers nearest \((n+m/\beta)/2\) after clipping to \([0,n]\). Every optimal coloring, up to exchange of the two colors, is obtained by taking an optimizer \(x\) of \(F_L\), coloring \(x\) of the \(m\) vertices with color one and all \(n\) vertices with color two, or the analogous construction from an optimizer of \(F_R\), **retaining only families whose maximum equals \(C_*\)**. Within either original graph part vertices can be permuted arbitrarily. The possible integer ties are included in this classification.

## Assumptions and scope
All integers \(m,n\ge1\) and real \(\mu>0\) are allowed. Every assignment of exactly two nonempty color classes is admissible; the classes need not form a proper graph coloring. A probe restricted to its class has independent symmetric signs \(\pm1\) on that class and zeros elsewhere. The two probes are independent; the estimator is the sum of their two quadratic forms. Exact matrix-vector multiplication is assumed; the cost is precisely two quadratic forms for any partition. This result optimizes estimator variance, not total setup cost, solution cost, or concentration tails.

## Proof
**1. Resolvent entries.** The shifted Laplacian is the block matrix
\[
\mu I+L=\begin{pmatrix}
(\mu+n)I_m&-\mathbf{1}_m\mathbf{1}_n^{\mathsf T}\\
-\mathbf{1}_n\mathbf{1}_m^{\mathsf T}&(\mu+m)I_n
\end{pmatrix}.
\]
Block inversion, or direct multiplication, gives the off-diagonal entries of \(B\): within the first part they are \(cn/(\mu+n)=c\sqrt\alpha\), within the second part \(cm/(\mu+m)=c\sqrt\beta\), and across the two parts \(c\). For completeness, within-part diagonal entries equal the same block constant plus \(1/(\mu+n)\) or \(1/(\mu+m)\), respectively. These expressions hold even if a part has a single vertex (in which case it has no within-part unordered pairs).

**2. Exact variance and weighted cut.** The independent Rademacher quadratic forms are unbiased. For any real symmetric \(B\), their summed variance is four times the sum of \(B_{ij}^2\) over unordered pairs \(i<j\) assigned the *same* color; this is the established Rademacher probing identity. Assign color one to \(x\) first-part vertices and \(y\) second-part vertices. The squared-off-diagonal weight of all unordered pairs, divided by \(c^2\), is
\[
W=\alpha\binom m2+\beta\binom n2+mn.
\]
The corresponding cut weight is
\[
C(x,y)=\alpha x(m-x)+\beta y(n-y)+x(n-y)+(m-x)y
=\alpha x(m-x)+\beta y(n-y)+nx+my-2xy.
\]
Therefore
\[
\operatorname{Var}(T_{x,y})=4c^2[W-C(x,y)],
\]
and minimizing variance is exactly maximizing this explicit integer quadratic cut weight.

**3. Strict exclusion of interior optimizers.** For every integer point with \(0<x<m\) and \(0<y<n\), both its neighbors \((x+1,y-1)\) and \((x-1,y+1)\) are feasible, and direct expansion yields
\[
C(x+1,y-1)+C(x-1,y+1)-2C(x,y)
=2(2-\alpha-\beta)>0.
\]
Indeed \(0<\alpha,\beta<1\). Hence at least one neighbor has strictly greater cut weight. Every maximizing integer point is on a rectangle edge. Reversing the color labels maps \((x,y)\) to \((m-x,n-y)\) without changing the cut, so it suffices to inspect the two edges \(y=0\) and \(x=0\). These are exactly \(F_L\) and \(F_R\). Both attain at least \(mn>0\), at \(x=m\) and \(y=n\), so the all-one-color boundary points never maximize. This proves both the global value and the complete optimizer characterization. Strict concavity of either one-variable quadratic gives the claimed closest-integer formulas and all ties.

**4. Sharp proper-coloring transition.** The proper coloring has cut weight \(mn\). For integer \(x\) one has
\[
F_L(x)-mn=(m-x)(\alpha x-n).
\]
Consequently \(F_L\) exceeds \(mn\) exactly when \(\alpha(m-1)>n\); if equality holds, \(x=m-1\) ties the usual coloring. Analogously \(F_R\) exceeds \(mn\) exactly when \(\beta(n-1)>m\). The two strict inequalities cannot both occur, since their product would imply
\[
\alpha\beta(m-1)(n-1)>mn,
\]
contradicting \(\alpha\beta<1\) and \((m-1)(n-1)<mn\). This proves the necessary and sufficient transition, including equality cases. Taking \(n=1\) reduces its sole nontrivial inequality to \(m-1>(\mu+1)^2\).

**5. Exact example.** For \(m=10\), \(n=1\), \(\mu=1\), one has \(c=1/12\), \(\alpha=1/4\), and \(F_L(7)=49/4\). The optimal partition assigns seven leaves to the first class and the remaining three leaves together with the hub to the second class. Its variance is \(1/4\), whereas the proper two-color partition has variance \(5/16\), an exact reduction of \(20\%\) for the same two quadratic forms.

## Verification
Run `python verify.py` using Python 3 standard library; `VERIFY_OUTPUT.txt` gives the recorded output. The checker independently inverts the full rational shifted Laplacian, tests all block entries, enumerates all integer class counts for small graphs, compares direct matrix-based variances to the cut formula, and checks the sharp phase boundary on larger parameter grids. The current run passed 10,067 exact rational assertions. The analytic proof above, not these finite checks, establishes the theorem for every dimension and positive real shift.

## Relationship to prior work
Frommer, Rinelli and Schweitzer (2023), Theorem 3.3 and Lemma 3.5, establish the general stochastic-probing variance formula for a **given** partition; their discussion emphasizes graph-distance colorings and optimizes the *number of stochastic samples after a partition is fixed*. That foundational identity is used here, not claimed as new. The present result instead optimizes over **all partitions** for the explicitly inverted resolvent of every complete bipartite graph and identifies the exact parameter regime where the standard proper bipartition is not optimal. Earlier hierarchical-probing work of Stathopoulos, Laeuchli and Orginos constructs distance-based schedules for lattice-type matrices, with a distinct graph family and target. A generic partition variance identity does not imply the present sharp complete-bipartite phase transition without solving its weighted-cut problem.

## Limitations
The optimality concerns exactly two independent Rademacher probes, one per nonempty class, and the inverse of the positive shifted combinatorial Laplacian on \(K_{m,n}\). It does not optimize more probe colors, unequal numbers of repeated samples per class, correlated/orthogonal probes, execution time, nonuniform graph-edge weights, different matrix functions, or tail probabilities. The mathematical proof is self-contained given the standard variance identity; the publication-precedence assessment is provisional because a specialized weighted-MaxCut or probing paper could contain an equivalent closed form.

## References
1. A. Frommer, M. Rinelli and M. Schweitzer, *Analysis of stochastic probing methods for estimating the trace of functions of sparse symmetric matrices*, arXiv:2308.07722v1 (public 15 August 2023), Theorem 3.3, Lemma 3.5, and Section 3.2. https://arxiv.org/abs/2308.07722
2. A. Stathopoulos, J. Laeuchli and K. Orginos, *Hierarchical probing for estimating the trace of the matrix inverse on toroidal lattices*, arXiv:1302.4018v1 (2013), Sections 1–2. https://arxiv.org/abs/1302.4018
3. J. Laeuchli and A. Stathopoulos, *Extending hierarchical probing for computing the trace of matrix inverses*, SIAM Journal on Scientific Computing, DOI:10.1137/18M1176427 (2019). https://doi.org/10.1137/18M1176427
