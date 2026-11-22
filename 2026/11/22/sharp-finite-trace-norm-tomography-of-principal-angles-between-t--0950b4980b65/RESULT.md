# Sharp finite trace-norm tomography of principal angles between two equal-rank projections

## Finding
Let \(k\ge1\). For any fixed, pairwise distinct sampling scales \(0<t_1<\cdots<t_k<1\), the values
\[
\left(\|P-t_jQ\|_{\mathcal S_1}\right)_{j=1}^{k}
\]
uniquely determine all \(k\) principal angles (counting multiplicities) of a pair of rank-\(k\) orthogonal projections \(P,Q\) on any complex Hilbert space of dimension at least \(2k\). In fact, these values determine the pair up to simultaneous unitary equivalence. The count is optimal: every collection of fewer than \(k\) distinct sampling scales fails to distinguish some two such pairs, even if all their principal angles are distinct and strictly between zero and \(\pi/2\).

This is finite tomography of the *angle multiset*, not reconstruction of the original embedded subspaces from invariant scalar measurements.

## Assumptions and scope
The space is complex Hilbert, with finite or infinite dimension \(\dim\mathcal H\ge2k\). Orthogonal projection means self-adjoint idempotent. Both projections have rank exactly \(k\). Sampling scales are fixed independently of the pair, are distinct, and lie strictly between zero and one. We write \(\theta_1,\ldots,\theta_k\in[0,\pi/2]\) for the canonical principal angles and \(a_i=\cos^2\theta_i\in[0,1]\). The nuclear or trace norm is \(\|T\|_{\mathcal S_1}=\operatorname{tr}|T|\). Multiplicities and both endpoints are permitted in the sufficiency assertion; the sharpness construction uses only interior distinct angles.

## Proof
**1. Exact norm pencil.** The standard canonical two-projection decomposition pairs each principal angle with a two-dimensional block, plus a common zero summand. The blocks may be chosen as
\[
P_i=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
Q_i=\begin{pmatrix}a_i&\sqrt{a_i(1-a_i)}\\\sqrt{a_i(1-a_i)}&1-a_i\end{pmatrix}.
\]
They remain legitimate when \(a_i=0\) or \(1\). On each block \(\operatorname{tr}(P_i-tQ_i)=1-t>0\) and \(\det(P_i-tQ_i)=-t(1-a_i)\le0\). Its trace norm therefore equals the difference of its two eigenvalues,
\[
\|P_i-tQ_i\|_{\mathcal S_1}=\sqrt{(1+t)^2-4ta_i}.
\]
Summing over blocks gives
\[
F_{P,Q}(t)=\|P-tQ\|_{\mathcal S_1}=(1+t)\sum_{i=1}^k\sqrt{1-q(t)a_i},\qquad q(t)=\frac{4t}{(1+t)^2}.
\]
The function \(q\) is strictly increasing on \((0,1)\), taking values in \((0,1)\).

**2. Sign-change budget.** Suppose two multisets \(A=(a_i)\) and \(B=(b_i)\) give the same observations. Let the signed atomic measure be \(\mu=\sum_i\delta_{a_i}-\sum_i\delta_{b_i}\). Its total mass is zero. Define the right-continuous cumulative step function \(H(u)=\mu([0,u])\) for \(0\le u<1\). If \(\mu\ne0\), then \(H\) is nonzero on a subset of positive Lebesgue measure: even a mass at \(1\) must be balanced by a mass elsewhere. After canceling common atoms, the jumps of \(H\) consist of at most \(k\) positive unit jumps and at most \(k\) negative unit jumps. Every transition between a positive interval and a negative interval requires the integer-valued walk to pass through zero, completing an excursion that consumes at least one jump of each sign. There are at most \(k\) excursions and hence at most \(k-1\) sign changes across nonzero intervals.

By Stieltjes integration by parts, valid also for endpoint atoms because \(\mu([0,1])=0\), for \(0<q<1\),
\[
\int_{[0,1]}\sqrt{1-qu}\,d\mu(u)
=\frac q2\int_0^1 \frac{H(u)}{\sqrt{1-qu}}\,du.
\]
Thus equal observations imply
\[
\int_0^1H(u)g_j(u)\,du=0,\qquad g_j(u)=(1-q_ju)^{-1/2},\quad q_j=q(t_j).
\]

**3. Strict Chebyshev rigidity.** Every initial subfamily of \(g_1,\ldots,g_k\) is an extended complete Chebyshev system on \([0,1]\). Indeed, writing \((1/2)_r=(1/2)(3/2)\cdots(r-1/2)\) and \((1/2)_0=1\), its first \(r\) Wronskian is
\[
W_r(u)=\left(\prod_{\ell=0}^{r-1}(1/2)_\ell\right)
\left(\prod_{j=1}^{r}(1-q_ju)^{-1/2}\right)
\prod_{1\le i<j\le r}\left(\frac{q_j}{1-q_ju}-\frac{q_i}{1-q_iu}\right)>0.
\]
This follows by factoring each derivative \(g_j^{(\ell)}(u)=(1/2)_\ell(q_j/(1-q_ju))^{\ell}g_j(u)\) and evaluating a Vandermonde determinant.

If \(H\) has \(r\le k-1\) sign changes, select one point in each separating zero interval or, if adjacent nonzero intervals meet, at their common boundary. Chebyshev interpolation gives a nonzero linear combination \(G\) of \(g_1,\ldots,g_{r+1}\) with exactly those \(r\) simple zeros and no others in \([0,1]\). Orient its sign so \(G(u)H(u)\ge0\) almost everywhere, with a strictly positive integral. But the \(k\) orthogonality relations give \(\int_0^1HG=0\), a contradiction. Therefore \(H=0\) almost everywhere and the atomic signed measure \(\mu\) is zero. The multisets coincide. The canonical decomposition then yields simultaneous unitary equivalence, as both ranks and ambient dimensions are fixed.

**4. Optimality of \(k\) measurements.** Fix \(0\le m<k\) distinct scales and consider the open angle-parameter chamber \(\Omega=\{0<a_1<\cdots<a_k<1\}\). The measurement map is
\[
\Phi(a_1,\ldots,a_k)=\left(\sum_{i=1}^{k}\sqrt{1-q_ja_i}\right)_{j=1}^m.
\]
Its Jacobian is \(\partial\Phi_j/\partial a_i=-q_jg_j(a_i)/2\). Every square evaluation matrix \((g_j(a_i))_{1\le j,i\le m}\) on distinct nodes is nonsingular by the Chebyshev property proved above; hence the Jacobian has full row rank \(m\). The implicit-function theorem makes each local level set a positive-dimensional smooth manifold of dimension \(k-m\). Distinct points in that local level set yield distinct strict-interior angle multisets with identical measurements. All are realized by the canonical two-dimensional blocks. The case \(m=0\) is immediate.

**5. Comparison with Hilbert--Schmidt data.** For all \(t\in\mathbb R\),
\[
\|P-tQ\|_{\mathcal S_2}^2=k(1+t^2)-2t\operatorname{tr}(PQ)=k(1+t^2)-2t\sum_ia_i.
\]
For \(k\ge2\) this cannot distinguish different lists with the same sum, even if measured at arbitrarily many scales.

## Verification
The attached standalone script `checks/projection_pencil_check.py` verifies the block nuclear-norm identity against independently computed eigenvalues and the Wronskian factorization for random parameters in dimensions one through five; it prints `PROJECTION_TRACE_TOMOGRAPHY_DIAGNOSTIC_OK 950` when all its 950 finite checks pass. The all-dimensions, all-scales uniqueness and sharpness claims are proved analytically above, not inferred from those checks.

## Relationship to prior work
The paper by Plevnik and Rani (first posted 15 November 2026) establishes Schatten-distance geometry and isometry classification of fixed-rank Grassmannians, including the single-scale projection difference formula. It does not give the affine-pencil finite-sampling theorem above. Classical principal-angle/Jordan-plane decompositions are used, not claimed as new. The strict Chebyshev-system and fixed-node interpolation theory supplies standard tools; the specifically equal-weight signed-measure sign-change bound and its sharp application to arbitrary fixed trace-norm pencil samples are the additional argument. Classical generalized Gaussian quadrature uses variable weights and commonly requires twice as many basis constraints; it is not in itself this equal-weight injectivity statement. Searches did not identify a preexisting theorem with exactly this principal-angle recovery conclusion; this is not a claim of exhaustive bibliographic uniqueness.

## Limitations
Only finite equal ranks are covered; reconstruction is up to simultaneous unitary equivalence, not recovery of spatial orientation. The theorem is injective, not a quantitative conditioning or noise-stability guarantee. The scales must be strictly between zero and one; the theorem does not assert a similar result for arbitrary Schatten exponents. Generalized equal-weight quadrature literature could contain a more abstract theorem implying the injectivity component. A separate independent mathematical audit has not been performed.

## References
1. L. Plevnik and J. Rani, *Schatten isometries of Grassmann spaces*, arXiv:2611.19919v1 (first posted 15 November 2026), https://arxiv.org/html/2611.19919v1 .
2. T. A. Loring, *Principal angles and approximation for quaternionic projections*, Annals of Functional Analysis **5** (2014), 176–187, https://doi.org/10.15352/afa/1396833512 (preprint arXiv:1306.1923).
3. D. Huybrechs, *On the computation of Gaussian quadrature rules for Chebyshev sets of linearly independent functions*, arXiv:1710.11244, https://arxiv.org/abs/1710.11244 .
4. *On the positivity and magnitudes of Bayesian quadrature weights*, Statistics and Computing (2019), section 3.2.1 (Chebyshev interpolation), https://doi.org/10.1007/s11222-019-09901-0 .
5. K.-J. Förster and G.-P. Ostermeyer, *On weighted Chebyshev-type quadrature formulas*, Mathematics of Computation **46** (1986), https://www.ams.org/journals/mcom/1986-46-174/S0025-5718-1986-0829638-2/ .
