# A square-root price-dominance transition for optimal weighted-star connectivity and incidence-row sampling

## Finding

**Theorem (all positive price vectors).** Fix an integer \(m\ge2\), positive prices \(c_1,\dots,c_m\), and a positive resource budget \(B\). Consider a star with hub vertex \(0\), leaf vertices \(1,\dots,m\), and edge conductances \(w_i\ge0\). Its combinatorial weighted Laplacian is
\[
L(w)=\sum_{i=1}^{m}w_i(e_0-e_i)(e_0-e_i)^\mathsf T.
\]
For \(n=m+1\), introduce
\[
q_i=\sqrt{c_i},\quad C=\sum_{i=1}^m c_i,\quad
\Delta=\Bigl(2\max_iq_i-\sum_{j=1}^mq_j\Bigr)_+,
\quad C_*=C-\frac{\Delta^2}{n}.
\]
Then \(C_*>0\), and the maximum algebraic connectivity subject to \(\sum_i c_iw_i\le B\) is exactly
\[
\boxed{\max_w\lambda_2(L(w))=\frac{B}{C_*}.}
\]
The optimizer is unique and all its edge conductances are strictly positive. If \(\Delta=0\), it is the uniform allocation \(w_i=B/C\). If \(\Delta>0\), there is a unique \(i_*\) with \(q_{i_*}>\sum_{j\ne i_*}q_j\), and the optimizer is
\[
\boxed{
 w_{i_*}=\frac{B}{C_*}\left(1-\frac{\Delta}{nq_{i_*}}\right),
 \qquad
 w_j=\frac{B}{C_*}\left(1+\frac{\Delta}{nq_j}\right)
 \quad(j\ne i_*).
}
\]
The equality case \(\Delta=0\), including exact equality \(\max_i q_i=\sum_{j\ne i}q_j\), belongs to the uniform regime.

**Corollary (cost-sensitive star-incidence projections).** Let \(a_i=(e_0-e_i)/\sqrt2\) be the unit-norm comparison rows of a consistent system, and start the randomized Kaczmarz method with error orthogonal to the constant vector. For an independently drawn row index with probability \(p_i\), let \(\bar c(p)=\sum_i c_ip_i\). On the zero-sum error subspace the sharp one-step worst-direction expected squared-error contraction is
\[
 \mu(p)=\lambda_{\min}\!\left(\sum_i p_i a_i a_i^\mathsf T\bigg|_{\mathbf1^\perp}\right)
 =\frac{\lambda_2(L(p))}{2}.
\]
The work-normalized certificate \(\eta(p)=\mu(p)/\bar c(p)\) is uniquely maximized by \(p_i=w_i^*/\sum_j w_j^*\), and
\[
 \boxed{\max_p\eta(p)=\frac1{2C_*}.}
\]
The optimizer is uniform if and only if \(\Delta=0\). This is a certificate per *expected* work, not a statement about exact finite-iteration error distributions or wall-clock time.

## Assumptions and scope

The graph has exactly \(m+1\) labeled vertices; all existing edges have adjustable nonnegative real conductances, priced linearly by strictly positive \(c_i\). A zero conductance is allowed in the feasible set, but it cannot be optimal. \(\lambda_2\) means the second-smallest eigenvalue of the unnormalized symmetric graph Laplacian, with eigenvalues counted with multiplicity. The budget is an inequality \(\sum_i c_iw_i\le B\) with \(B>0\), attained at equality at the optimum. The Kaczmarz corollary presumes unit row normalization and independent, stationary per-iteration selection; the same positive prices represent expected computational work. The theorem is about the exact spectral optimization and its associated one-step certificate; it does not assert exact iteration-complexity optimality when sample costs are stochastic or implementation-dependent.

## Proof

**Step 1: convert a spectral constraint into a small positive-semidefinite test.** Write \(x=(x_0,x_1,\ldots,x_m)\perp\mathbf1\) and define \(y_i=x_i-x_0\). The map \(x\mapsto y\in\mathbb R^m\) is a bijection from \(\mathbf1^\perp\), with inverse \(x_0=-\sum_i y_i/n\) and \(x_i=y_i-\sum_j y_j/n\). Consequently
\[
 x^\mathsf TL(w)x=\sum_iw_iy_i^2,\qquad
 \|x\|_2^2=\sum_i y_i^2-\frac{(\sum_i y_i)^2}{n}.
\]
For any prescribed threshold \(\tau>0\), \(\lambda_2(L(w))\ge\tau\) is equivalent to
\[
 \operatorname{diag}(w_1-\tau,\ldots,w_m-\tau)
 +\frac\tau n\mathbf1\mathbf1^\mathsf T\succeq0.
\]
By homogeneity it is enough to solve the minimum-cost feasibility problem for \(\tau=1\):
\[
 \min\sum_i c_i v_i\quad\text{subject to}\quad
 M(v)=\operatorname{diag}(v_i-1)+\frac1n\mathbf1\mathbf1^\mathsf T\succeq0,
 \qquad v_i\ge0.
\]

**Step 2: there can be at most one deficient edge.** If every \(v_i\ge1\), the objective is at least \(C\), with equality uniquely at \(v_i=1\) for all indices. If some \(v_i<1\), the matrix inequality forces \(v_j>1\) for every \(j\ne i\): the quadratic form of \(M(v)\) along \(e_i-e_j\) equals \(v_i+v_j-2\), and a zero surplus \(v_j=1\) gives a strictly negative value. Thus there is exactly one potentially deficient index \(i\). Set \(d=1-v_i>0\), \(a_j=v_j-1>0\) for \(j\ne i\), and \(S=\sum_{j\ne i}a_j^{-1}\).

**Step 3: the exact Schur bound.** In the block of other indices, \(\operatorname{diag}(a_j)+\mathbf1\mathbf1^\mathsf T/n\) is positive definite. The Sherman–Morrison identity gives \(\mathbf1^\mathsf T(\operatorname{diag}(a_j)+\mathbf1\mathbf1^\mathsf T/n)^{-1}\mathbf1=nS/(n+S)\); taking the scalar Schur complement of this block in \(M(v)\) yields the equivalent bound
\[
 0<d\le\frac1{n+S}.
\]
Define \(P=\sum_{j\ne i}\sqrt{c_j}\) and \(Q=\sqrt{c_i}\). Cauchy–Schwarz gives
\[
 \sum_{j\ne i}c_ja_j\ge\frac{P^2}{S},
 \qquad \sum_i c_iv_i-C=\sum_{j\ne i}c_ja_j-c_id
 \ge \frac{P^2}{S}-\frac{Q^2}{n+S}.
\]
If \(Q\le P\), the right side is strictly positive since
\(P^2/S\ge Q^2/S>Q^2/(n+S)\). Thus a deficient edge can improve cost only when its square-root price strictly dominates *all other* square-root prices together. At most one index can do so.

**Step 4: an exact nonnegative square and equality cases.** Suppose \(Q>P\) and put \(D=Q-P>0\). For every \(S>0\), the identity
\[
 \frac{P^2}{S}-\frac{Q^2}{n+S}
 +\frac{D^2}{n}
 =\frac{(nP-DS)^2}{nS(n+S)}\ge0
\]
implies the universal cost lower bound \(C-D^2/n\). Equality in the displayed identity requires \(S=nP/D\); equality in Cauchy–Schwarz requires \(a_j\) proportional to \(1/\sqrt{c_j}\), and equality in the Schur bound requires \(d=1/(n+S)\). Solving these three equalities gives uniquely
\[
 a_j=\frac{D}{n\sqrt{c_j}},\quad
 d=\frac{D}{nQ}.
\]
The resulting \(v_i=1-D/(nQ)>0\) and \(v_j=1+D/(n\sqrt{c_j})>1\) satisfy the matrix constraint at equality. If no index strictly dominates, the unique minimizer remains \(v_i=1\) for all \(i\). The minimum unit-threshold cost is therefore precisely \(C_*=C-\Delta^2/n\). It is positive because \(0\le\Delta<\max_i\sqrt{c_i}\), so \(\Delta^2/n< C\).

**Step 5: rescaling and sharpness.** The candidate \(v\) in either regime has \(M(v)\succeq0\) with a zero eigenvalue. In the uniform regime the zero vector lies in the subspace orthogonal to \(\mathbf1\) in leaf-difference coordinates; in the dominant-price regime the Schur complement vanishes. Thus \(\lambda_2(L(v))=1\). The budget allocation is uniquely \(w^*=Bv/C_*\), with connectivity \(B/C_*\). For any feasible \(w\) with \(\lambda=\lambda_2(L(w))>0\), the rescaled \(v=w/\lambda\) satisfies the unit-threshold matrix constraint and hence \(\sum_i c_iw_i\ge\lambda C_*\); because the cost does not exceed \(B\), necessarily \(\lambda\le B/C_*\), with equality only at the proved unique minimizer. Any disconnected allocation has connectivity zero and cannot be optimal.

**Step 6: passage to randomized projections.** For \(a_i=(e_0-e_i)/\sqrt2\), orthogonal projection removes the squared component along \(a_i\). Hence conditionally on error \(e\perp\mathbf1\),
\[
 \mathbb E[\|e^+\|_2^2\mid e]
 =\|e\|_2^2-e^\mathsf T\!\left(\frac12L(p)\right)e.
\]
The optimal worst-direction contraction coefficient is \(\lambda_2(L(p))/2\). Under the homogeneous transformation \(v=p/(\sum_i c_ip_i)\), the cost of \(v\) equals one and the objective becomes \(\lambda_2(L(v))/2\). By Step 5 at budget one its unique maximum is \(1/(2C_*)\); conversely normalize the optimal \(v\) to \(p_i=v_i/\sum_jv_j\). This proves both the Kaczmarz optimum and its uniqueness.

## Verification

The standalone file `verify.py` constructs exact rational candidates for square-rational price examples and tests every principal minor of the leaf-coordinate matrix \(M(v)\), exactly confirming positive semidefiniteness and singularity for these instances. It additionally compares the explicit costs and predicted eigenvalues with direct Laplacian calculations and random feasible competitors. Run from an extracted package with `python3 verify.py` (requires NumPy). The replay reported `VERIFY_OK exact_design_cases=1367 principal_minors=36225 random_comparisons=12980`. These tests are finite cross-checks; the proof above supplies the all-dimensional statement.

For example, with three leaves, prices \((c_1,c_2,c_3)=(25,1,1)\), and budget \(B=1\), one has \(C=27\), \(\Delta=3\), \(n=4\), and \(C_*=99/4\). The optimal conductances are \((17/495,7/99,7/99)\), with \(\lambda_2=4/99\). Uniform conductances attain only \(1/27\).

## Relationship to prior work

Ghosh and Boyd (2006) develop spectral connectivity optimization through convex programming, supplying the broader setting but not the heterogeneous-price star formula or its square-root dominance boundary [1]. Shafi, Arcak and El Ghaoui (2010) formulate edge-weight and cost-aware Laplacian spectral design as convex constraints without a closed-form star price-dominance solution [5]. Strohmer and Vershynin (2007) give the original norm-sampled randomized Kaczmarz rate theory [2]. Gower and Richtárik (2015, section 5.1) explicitly formulate probability selection as a semidefinite eigenvalue optimization, without the present work-normalized star incidence solution [3]. Sarkar (2026) derives a general cost-sensitive E-optimal design and dual certificate for randomized block Kaczmarz; consequently **the abstract cost-sensitive SDP reduction is prior work**, not claimed as new here. The contribution here is its explicit non-generic star solution, complete equality cases, unique optimal sampling distribution, and sharp criterion in terms of square-root prices [4].

## Limitations

The proof assumes independent, stationary sampling, linear positive per-row work prices, a star graph with unweighted incidence-row normalization, and an objective defined by the worst-direction *single-step* expected squared-error decrease divided by expected work. It does not establish optimal probability distributions for exact finite-time mean-square error, almost-sure convergence exponents, adaptive sampling, correlated rows, wall-clock runtime, arbitrary trees, or arbitrary cost models. The spectral theorem itself is exact for all real positive prices and all integer numbers of leaves at least two. Prior-art inspection is not a proof of global publication uniqueness: unindexed or inaccessible graph-specific solutions may exist. No independent external mathematical review has been performed.

## References

[1] A. Ghosh and S. Boyd, "Upper bounds on algebraic connectivity via convex optimization," *Linear Algebra and its Applications* 418 (2006), 693–707. Available online 2006-05-05. DOI: 10.1016/j.laa.2006.03.006. https://web.stanford.edu/~boyd/papers/pdf/eigbounds_laplacian.pdf

[2] T. Strohmer and R. Vershynin, "A randomized Kaczmarz algorithm with exponential convergence," arXiv:math/0702226, first version 2007-02-08. https://arxiv.org/html/math/0702226v1

[3] R. M. Gower and P. Richtárik, "Randomized Iterative Methods for Linear Systems," *SIAM Journal on Matrix Analysis and Applications* 36 (2015), 1660–1690, sec. 5.1. DOI: 10.1137/15M1025487. https://pages.stat.wisc.edu/~bwu62/771/gower2015.pdf

[4] S. Sarkar, "Cost-sensitive spectral sampling algorithms for randomized block Kaczmarz methods," publicly posted 2026-06-24. DOI: 10.21203/rs.3.rs-10036143/v1. https://www.researchgate.net/publication/408033023_Cost-sensitive_spectral_sampling_algorithms_for_randomized_block_Kaczmarz_methods

[5] S. Y. Shafi, M. Arcak and L. El Ghaoui, "Designing Node and Edge Weights of a Graph to Meet Laplacian Eigenvalue Constraints," *48th Allerton Conference* (2010). https://people.eecs.berkeley.edu/~elghaoui/Pubs/SAE_Allerton_2010.pdf
