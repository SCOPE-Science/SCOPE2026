# Unique optimal two-color stochastic probing on Boolean hypercubes

## Finding

For a Boolean hypercube of any dimension, the parity bipartition uniquely minimizes the variance of a two-query stochastic trace-probing estimator simultaneously for **every nontrivial positive mixture of graph heat kernels**. This remains true among arbitrary two-set partitions, not merely proper graph colorings or balanced partitions. Moreover, the full excess variance over parity has an exact Walsh-spectral decomposition with a strictly positive quantitative gap.

Let \(d\geq1\), \(V=\{0,1\}^d\), and \(N=2^d\). Let \(L_d=dI-A_d\) be the combinatorial Laplacian of the \(d\)-cube. For a finite positive Borel measure \(\nu\) on \([0,\infty)\) with \(\nu((0,\infty))>0\), set

\[
B=\int_0^\infty e^{-tL_d}\,d\nu(t).
\]

For each two-coloring encoded by \(\sigma:V\to\{-1,1\}\), form independent Rademacher vectors \(z_+,z_-\), each supported on its respective color, with independent fair signs on that color. Define the unbiased estimator

\[
T_\sigma=z_+^{\mathsf T}Bz_++z_-^{\mathsf T}Bz_-.
\]

The globally variance-minimizing colorings are exactly \(\sigma(x)=\pm(-1)^{|x|}\), where \(|x|\) denotes Hamming weight. These two colorings represent the same partition with exchanged labels.

The theorem supplies an exact variance formula. Put \(b(z)=B_{0z}\), \(w(z)=b(z)^2\), and define \(\Lambda_r\), for \(0\leq r\leq d\), by

\[
\Lambda_r=\int\!\!\int
\left(\frac{1+e^{-2(s+t)}}2\right)^{d-r}
\left(\frac{e^{-2s}+e^{-2t}}2\right)^r\,d\nu(s)d\nu(t).
\]

Then \(\Lambda_0>\Lambda_1>\cdots>\Lambda_d>0\), and the exact minimum is

\[
\boxed{\operatorname{Var}(T_{\rm parity})
=N\bigl(\Lambda_0+\Lambda_d-2w(0)\bigr).}
\]

For every coloring define normalized Walsh coefficients

\[
\widehat\sigma(S)=N^{-1}\sum_{x\in V}\sigma(x)(-1)^{\sum_{j\in S}x_j},
\qquad S\subseteq\{1,\ldots,d\}.
\]

The sharp global excess-variance identity is

\[
\boxed{\operatorname{Var}(T_\sigma)-\operatorname{Var}(T_{\rm parity})
=N\sum_{S\ne\{1,\ldots,d\}}
(\Lambda_{|S|}-\Lambda_d)\widehat\sigma(S)^2.}
\]

In particular, it is at least

\[
N(\Lambda_{d-1}-\Lambda_d)
\bigl[1-\widehat\sigma(\{1,\ldots,d\})^2\bigr].
\]

## Assumptions and scope

All dimension parameters are finite integers \(d\ge1\). The heat-mixture measure \(\nu\) is a finite nonnegative measure, with positive mass on strictly positive times; an atom at time zero is permitted. This excludes the trivial diagonal case \(B=cI\), where every partition has the same zero variance. Each color uses exactly one independent Rademacher probing vector, and the cost is two quadratic forms of \(B\) for nonempty colors. Probabilities, magnitudes and signs of all random entries are part of this definition. The color optimization is over every map \(\sigma:V\to\{-1,+1\}\); the proof allows even empty colors, although parity has two nonempty colors and is the unique minimizer in the conventional two-nonempty-color class.

Examples covered by the theorem include \(B=e^{-tL_d}\) for every \(t>0\), finite positive combinations of such matrices and \(B=(\mu I+L_d)^{-1}\) for every \(\mu>0\), by the Laplace-resolvent formula

\[
(\mu I+L_d)^{-1}=\int_0^\infty e^{-\mu t}e^{-tL_d}\,dt.
\]

There is no assumption of spectral-gap size, dimension-independent condition number, or distance-decay rate beyond the stated heat-mixture condition.

## Proof

**Step 1: Fourier form of the heat kernel.** The one-bit Laplacian is \(\begin{psmallmatrix}1&-1\\-1&1\end{psmallmatrix}\); its heat kernel has diagonal entries \(a_t=(1+e^{-2t})/2\) and off-diagonal entries \(b_t=(1-e^{-2t})/2\). Since the cube Laplacian is the sum of commuting coordinate Laplacians, for \(z\in V\),

\[
(e^{-tL_d})_{0z}=\prod_{j=1}^d
\begin{cases} a_t,&z_j=0,\\b_t,&z_j=1.\end{cases}
\]

Consequently \(B_{xy}=b(x\oplus y)\) depends only on the coordinatewise XOR, and so \(W=(B_{xy}^2)_{x,y}\) is a Walsh-convolution matrix.

**Step 2: The exact spectrum of the squared kernel.** By Fubini, valid because \(\nu\) is finite and all heat entries lie in \([0,1]\),

\[
w(z)=\int\!\!\int\prod_{j=1}^d
\begin{cases}a_sa_t,&z_j=0,\\b_sb_t,&z_j=1\end{cases}
\,d\nu(s)d\nu(t).
\]

For the Walsh character \(\chi_S(z)=(-1)^{\sum_{j\in S}z_j}\), the eigenvalue of \(W\) is \(\sum_z w(z)\chi_S(z)\). Factorization over the coordinates yields

\[
\sum_{z}w(z)\chi_S(z)
=\int\!\!\int(a_sa_t+b_sb_t)^{d-|S|}
(a_sa_t-b_sb_t)^{|S|}\,d\nu(s)d\nu(t)=\Lambda_{|S|}.
\]

Writing \(u=e^{-2s}\), \(v=e^{-2t}\), the two factors are \(A(s,t)=(1+uv)/2\) and \(D(s,t)=(u+v)/2\), with

\[
A(s,t)-D(s,t)=\frac{(1-u)(1-v)}2\ge0.
\]

Both factors are nonnegative, and \(A>D>0\) whenever \(s,t>0\). The product measure of \((0,\infty)^2\) is strictly positive under the hypothesis, hence \(\Lambda_r>\Lambda_{r+1}>0\) for every \(0\le r<d\). No limiting or finite-enumeration argument is needed.

**Step 3: Exact estimator variance.** Independence and the Rademacher fourth-moment identity give the standard colorwise formula

\[
\operatorname{Var}(T_\sigma)=
2\sum_{x\ne y\,;\,\sigma(x)=\sigma(y)}B_{xy}^2.
\]

Using \(2\mathbf 1_{\sigma(x)=\sigma(y)}=1+\sigma(x)\sigma(y)\), separating the diagonal and using the constant row sum \(\Lambda_0\) of \(W\),

\[
\operatorname{Var}(T_\sigma)
=N(\Lambda_0-2w(0))+\sigma^{\mathsf T}W\sigma.
\]

With the normalization of Walsh coefficients above, Parseval gives \(\sum_S\widehat\sigma(S)^2=1\), because \(\sigma(x)^2=1\), and Walsh diagonalization gives

\[
\sigma^{\mathsf T}W\sigma
=N\sum_S\Lambda_{|S|}\widehat\sigma(S)^2.
\]

**Step 4: Global optimality and equality.** Strict eigenvalue ordering implies that this convex combination is minimized uniquely by placing all normalized Walsh energy in the one-dimensional top-degree character \(\chi_{\{1,\ldots,d\}}\). The only real sign vectors of unit magnitude in this eigenspace are its positive and negative characters, i.e. the parity coloring and its color reversal. Subtracting this value proves the full exact gap and its lower bound, using \(\Lambda_{|S|}\ge\Lambda_{d-1}\) whenever \(S\ne\{1,\ldots,d\}\).

The argument simultaneously establishes necessity and sufficiency and includes every boundary of the stated parameter domain.

## Verification

The accompanying standard-library-only file `verify.py` implements exact rational Walsh transforms and covariance identities. Running `python3 verify.py` produced `VERIFY_OK: 9685 exact rational and exhaustive/sampled assertions; all true`. It checks the shifted-Laplacian inverse for dimensions one through four at three positive rational shifts, exhaustively enumerates all sign partitions for dimensions at most three, samples colorings in dimension four, verifies a nontrivial two-atom heat mixture, and enumerates all probe outcomes for two partitions in the three-cube. Exact enumeration in these small dimensions is not used as an infinite-dimensional proof.

As an interpretable rational benchmark, set \(d=3\) and \(B=(I+L_3)^{-1}\). The kernel values at Hamming distances zero through three are

\[
\left(\frac{12}{35},\frac{13}{105},\frac8{105},\frac2{35}\right).
\]

Then the optimal two-color estimator variance is \(1024/3675\), while the one-probe full Rademacher Hutchinson estimator variance is \(16/15\); their ratio is exactly \(64/245\). These estimators have different numbers of quadratic forms, so the ratio is a variance benchmark, not a fixed-computational-cost speedup claim.

## Relationship to prior work

Frommer, Rinelli and Schweitzer (2023), Theorem 3.3 and Section 3.2, give the general variance formula for Rademacher stochastic probing on any supplied color partition, and their Section 3.4 establishes structural upper bounds for distance colorings. Their treatment supplies the estimator framework and an indispensable identity; it does not establish that any particular two-coloring is globally variance-minimizing on the Boolean cube, nor the strictly ordered squared-kernel Walsh spectrum and full equality/gap classification here.

Frommer, Schimmel and Schweitzer (2020), Sections 2--4, develop deterministic distance-color probing and decay bounds, rather than this stochastic all-partition minimization. Stathopoulos, Laeuchli and Orginos (2013) construct and analyze hierarchical graph colorings for lattice inverse-trace probing; such constructions motivate parity and distance coloring but do not furnish a necessity-and-sufficiency variance comparison against improper and unbalanced two-color assignments.

An earlier result for **even cycles** establishes checkerboard optimality for a shifted cycle resolvent. The present theorem is not a relabeling of that result: it treats arbitrary hypercube dimension and an entire positive cone of heat-mixture kernels, with a different Fourier proof and an explicit quantitative gap. The underlying general Rademacher variance identity and Boolean Fourier diagonalization are classical; novelty is claimed only for their exact combination into this all-coloring, all-mixture optimization theorem.

## Limitations

The theorem applies to one independent random probe per color, and minimizes variance rather than wall-clock cost, tail probabilities, the number of required colors, or multi-query joint coupling strategies. It does not apply without proof to signed heat mixtures, non-Hamming-transitive graphs, unnormalized arbitrary Laplacians, weighted or nonuniform edge rates, or nonlinear matrix functions not representable by a finite positive heat-mixture measure. It does not give a dimension-uniform lower bound on the spectral gap. Previously published specialist results on colored trace estimation or harmonic analysis could conceivably imply the same classification; publication novelty has not been independently established. A related later hierarchical-probing extension was located but its full text was not available for a conclusive comparison. Independent scientific review has not been performed.

## References

1. A. Frommer, M. Rinelli, M. Schweitzer, *Analysis of stochastic probing methods for estimating the trace of functions of sparse symmetric matrices*, first posted 2023-08-15, arXiv:2308.07722, especially Theorem 3.3 and Sections 3.2 and 3.4. https://arxiv.org/abs/2308.07722
2. A. Frommer, C. Schimmel, M. Schweitzer, *Analysis of probing techniques for sparse approximation and trace estimation of decaying matrix functions*, arXiv:2009.01589 (2020), especially Sections 2--4. https://arxiv.org/abs/2009.01589
3. A. Stathopoulos, J. Laeuchli, K. Orginos, *Hierarchical probing for estimating the trace of the matrix inverse on toroidal lattices*, arXiv:1302.4018 (2013), especially Sections 1--3. https://arxiv.org/abs/1302.4018
4. J. Laeuchli, A. Stathopoulos, *Extending hierarchical probing for computing the trace of matrix inverses*, SIAM Journal on Scientific Computing 42 (2020), DOI:10.1137/18M1176427. https://doi.org/10.1137/18M1176427
