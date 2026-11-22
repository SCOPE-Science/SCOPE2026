# Sharp Lipschitz phase diagram for distance-normalized kernels on weighted stars

## Finding

Let \(X=\{0,1,\ldots,m\}\) be the unit-edge star with hub \(0\) and \(m\ge1\) leaves. Give its hub mass \(a>0\) and leaves masses \(b_i>0\), and put \(B=\sum_{i=1}^{m}b_i\). For \(0<q<1\), define the positive averaging operator

\[
(T_qf)(x)=\sum_{y\in X}K_q(x,y)f(y),\qquad
K_q(x,y)=\frac{w_yq^{d(x,y)}}{\sum_{z\in X}w_zq^{d(x,z)}},
\]

where \(w_0=a\), \(w_i=b_i\), and \(d\) is the shortest-path metric. Set \(S_i=B-b_i\). In the graph-Lipschitz seminorm \(\operatorname{Lip}_d f=\max_i|f(i)-f(0)|\), the **exact** operator coefficient on functions modulo constants is

\[
\boxed{\mathcal L(q)=\max_{1\le i\le m}
\frac{(1-q^2)b_i(a+2qS_i)}{(a+qB)(b_i+aq+q^2S_i)}.}
\tag{1}
\]

The operator is nonexpansive **at every** \(q\in(0,1)\) precisely when

\[
\boxed{a^2\ge\max_{1\le i\le m}b_i(B-2b_i).}
\tag{2}
\]

If (2) fails, let \(I=\{i:b_i(B-2b_i)>a^2\}\). For each \(i\in I\), let \(q_i^*\in(0,1)\) be the unique positive root of

\[
S_i(S_i+3b_i)q^2+2aBq+a^2-b_i(S_i-b_i)=0.
\tag{3}
\]

Then \(\mathcal L(q)>1\) **exactly** when \(0<q<\max_{i\in I}q_i^*\); it equals one at the threshold and is strictly below one for all larger \(q<1\). In the equal-mass case \(a=b_i\), expansivity is possible if and only if \(m\ge4\) (five total vertices). Across all stars, masses, and \(0<q<1\), the coefficient is strictly smaller than \(2\), but its sharp supremum is \(2\).

## Assumptions and scope

The star is finite, all vertex masses are strictly positive, all edge lengths are one, and \(q\) is strictly between zero and one. Inputs are all real-valued functions on \(X\), modulo constants. No connectedness, symmetry, or normalization of the masses beyond positivity is required (multiplying all masses by a common positive factor changes nothing). The result concerns one application of this row-normalized distance kernel, not a continuous-time heat semigroup or iteration of the metric itself. The limits \(q\downarrow0\) and \(q\uparrow1\) are not included in (3).

## Proof

**1. Edgewise operator norm.** Since the graph is a star, for every function the Lipschitz seminorm is \(\max_{1\le i\le m}|f(i)-f(0)|\). Subtracting \(f(0)\), we may take \(f(0)=0\), with each \(f(j)\in[-1,1]\) independently. Write \(\mu_x(y)=K_q(x,y)\). For any edge \((0,i)\), the exact dual norm is

\[
\sup_{\operatorname{Lip}_df\le1}|(T_qf)(0)-(T_qf)(i)|
=\sum_{j=1}^m|\mu_0(j)-\mu_i(j)|.
\tag{4}
\]

This is also the \(W_1\) distance between these two probability rows, by the tree-cut transport formula; alternatively (4) follows directly from independent optimization of the leaf values.

**2. Exact signs and sharpness.** The normalizers are

\[
Z_0=a+qB,\qquad Z_i=b_i+aq+q^2S_i.
\]

For the distinguished leaf, and then for every other leaf, straightforward common-denominator subtraction yields

\[
\mu_i(i)-\mu_0(i)=\frac{(1-q^2)b_i(a+qS_i)}{Z_0Z_i}>0,
\]

\[
\mu_0(j)-\mu_i(j)=\frac{(1-q^2)q b_ib_j}{Z_0Z_i}>0
\quad (j\ne i,\ j\ge1).
\]

Consequently, the sum of absolute leaf differences is exactly the \(i\)-th term of (1). It is attained by the explicit potential \(f(0)=0\), \(f(i)=-1\), and \(f(j)=1\) for the other leaves. Taking the maximum over the hub–leaf edges proves (1), with an attained optimum for every fixed set of parameters.

**3. All-bandwidth classification.** Denote the \(i\)-th term of (1) by \(C_i(q)\). Exact algebra, without sign assumptions, gives

\[
C_i(q)-1=\frac{q\big[b_i(S_i-b_i)-a^2-2aBq-S_i(S_i+3b_i)q^2\big]}{(a+qB)(b_i+aq+S_iq^2)}.
\tag{5}
\]

The denominator is positive. The numerator's bracket is strictly decreasing in \(q\ge0\) because \(aB>0\). If its value at \(q=0\) is nonpositive, then \(C_i(q)<1\) for all \(0<q<1\). Otherwise it has a unique positive root, necessarily below one since \(C_i(1)=0\), and the sign is positive exactly below that root. Applying this observation to all leaves proves (2), (3), and the single expansive bandwidth interval. Notice that equality in (2) still gives strict contraction for every positive \(q\).

**4. Dimension and mass consequences.** When \(a=b_i=1\), the initial bracket in (5) is \(m-3\), so the four-leaf case is the first expansive equal-mass star. Its sharp threshold is \(q^*=(-4+\sqrt{34})/18\). As an unbalanced three-vertex example, \(a=1/10\), \(b_1=1\), \(b_2=9\) gives a positive initial bracket \(799/100\) for leaf one and therefore an expansive interval even though \(m=2\).

**5. The sharp universal envelope and positivity.** Every two probability distributions on a metric space of diameter two have \(W_1\le2\). Here every row assigns positive mass to every vertex; the common positive mass at any vertex can be coupled at zero cost, leaving strictly less than unit mass to transport, so \(C_i(q)<2\). Conversely, for equal masses on \(m+1\) vertices and \(q=m^{-3/4}\), formula (1) gives

\[
\mathcal L(q)=\frac{(1-q^2)(1+2(m-1)q)}{(1+mq)(1+q+(m-1)q^2)}\longrightarrow 2
\quad (m\to\infty),
\]

since \(mq\to\infty\) but \(mq^2\to0\). Thus the supremum is sharp and never attained at finite positive parameters. Finally, the symmetric matrix \(H_{xy}=q^{d(x,y)}\) is strictly positive definite: it is the covariance of independent centered unit-variance variables \(Y_0=G_0\), \(Y_i=qG_0+\sqrt{1-q^2}\,G_i\). Detailed balance holds with stationary weights \(\pi_x\propto w_xZ_x\), so \(K_q\) is similar to the positive-definite symmetric matrix \([\sqrt{w_xw_y/(Z_xZ_y)}\,H_{xy}]\). It has strictly positive real spectrum. This shows the expansive examples remain positive-spectrum reversible averaging operators.

## Verification

The included `verify.py` is self-contained and uses exact rational arithmetic. It exhausts all \(2^m\) vertex-sign potentials for each of 870 positive-mass/rational-bandwidth test cases with up to six leaves, matches them against (1), checks each leaf witness and the sign polynomial (5), and probes dimension and envelope examples. Run `python verify.py` from the extracted package. These finite checks supplement, but do not replace, the all-parameters algebraic proof above.

## Relationship to prior work

Mémoli–Smith–Wan's Wasserstein transform [1] motivates localization of a metric space by point-indexed probability measures. Its published finite-metric localization and data-perturbation stability statements do not themselves give the star-specific operator norm (1) or all-mass criterion (2). Montrucchio–Pistone [2] (Theorems 4.1–4.2) gives the general tree transport/cut formula used in (4); (1)–(3) require additional analysis of the specific row-normalized exponential-distance operator and its sign transitions. Jin–Mémoli–Wan [3] studies Gaussian 2-Wasserstein localization, rather than this finite graph 1-Wasserstein operator.

Published exact heat-semigroup Lipschitz results for star graphs [4,5] concern \(e^{tQ}\) of continuous-time Markov generators, not \(K_q(x,y)\propto w_yq^{d(x,y)}\). Therefore they do not directly imply the all-weight bandwidth frontier derived here. The possibility of an unindexed equivalent formula or a hidden specialization in other literature remains open to further external priority checking.

## Limitations

The exact coefficient and classification are restricted to finite unit-edge stars and strictly positive masses; no general-tree formula or stochastic-sampling guarantee is claimed. This is not a statement about all positive spectral filters or continuous-time diffusion. Full external novelty verification and independent mathematical review are not claimed. The provided checker covers finite rational test instances only; the proof, not its enumerations, establishes the unrestricted parameter theorem.

## References

1. F. Mémoli, Z. Smith, Z. Wan, *The Wasserstein Transform*, Proceedings of Machine Learning Research 97 (2019), 4496–4504, https://proceedings.mlr.press/v97/memoli19a.html ; first public preprint arXiv:1810.07793 (17 October 2018).
2. L. Montrucchio, G. Pistone, *Kantorovich distance on a finite metric space*, arXiv:1905.07547, first posted 18 May 2019, https://arxiv.org/html/1905.07547v5 .
3. K. Jin, F. Mémoli, Z. Wan, *The Gaussian Transform*, arXiv:2006.11698, 21 June 2020, https://arxiv.org/abs/2006.11698 .
4. *Exact Wasserstein amplification on a rate-defect star and its metastable peak*, public indexed research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-wasserstein-amplification-on-a-rate-defect-star-and-its-me--48121e61fb36 .
5. *Two-conductance stars: exact heat-Lipschitz norm, slow-edge rigidity and a sharp fixed-size amplification envelope*, public indexed research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-two-conductance-stars-exact-heat-lipschitz-norm-slow-edge-rigidi--20e568f24dba .
