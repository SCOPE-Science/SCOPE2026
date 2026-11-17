# A one-third deletion optimum and an exponential volume-moment gap for cycle-root polytopes

## Finding
For each integer \(n\ge3\), take the cycle graph \(C_n\) with labeled vertices \(0,\ldots,n-1\) and edges \(j(j+1)\) (indices modulo \(n\)). Fix an integer \(1\le m\le n-1\), delete exactly \(m\) distinct edges uniformly at random, and call the resulting forest \(G\). Its symmetric edge polytope, with ambient Euclidean metric inherited from \(\mathbb R^n\), is
\[
 P_G=\operatorname{conv}\{\pm(e_i-e_j):ij\in E(G)\}.
\]
Let \(k=n-m\), let \(V_k(P_G)\) mean the \(k\)-dimensional Hausdorff volume in the linear span of this polytope, and define the cross-polytope-normalized *squared intrinsic volume*
\[
 X_{n,m}=\left(\frac{k!}{2^k}V_k(P_G)\right)^2.
\]
The normalization divides out the volume of the standard unit \(k\)-cross-polytope before squaring, so \(X_{n,m}\) records the squared Euclidean determinant of its edge-root generators.

**Exact law and sharp deletion optimum.** If \(s_1,\ldots,s_m\) are the vertex counts in the components of \(G\), then
\[
 X_{n,m}=\prod_{i=1}^m s_i,
 \qquad
 \mathbb E X_{n,m}=
 \frac{\Gamma(m)\Gamma(n+m)}{\Gamma(2m)\Gamma(n)}.
\]
More generally, for every real \(t\), its full Mellin transform is
\[
 \mathbb E X_{n,m}^{t}=
 \frac{[z^n]\left(\sum_{s\ge1}s^t z^s\right)^m}
 {\binom{n-1}{m-1}}.
\]
For each fixed \(n\ge3\), the exact mean is uniquely largest at \(m=\lfloor n/3\rfloor\) if \(n\equiv0,1\pmod3\). If \(n\equiv2\pmod3\), precisely \(m=\lfloor n/3\rfloor\) and \(m=\lfloor n/3\rfloor+1\) tie for the maximum. This discrete one-third threshold is sharp for every \(n\).

**Asymptotic fluctuation and annealed–typical separation.** Suppose \(m=m(n)\) is integral and \(q_n=m/n\to q\in(0,1)\). For \(S_q\) geometric on \(\{1,2,\ldots\}\), with \(\mathbb P(S_q=s)=q(1-q)^{s-1}\), define
\[
 \mu(q)=\mathbb E\log S_q,\quad
 \tau(q)^2=\operatorname{Var}(\log S_q)
 -\frac{\operatorname{Cov}(S_q,\log S_q)^2}{\operatorname{Var}(S_q)}.
\]
Then \(\tau(q)^2>0\) and the conditional-volume central limit theorem is
\[
 \frac{\log X_{n,m}-m\mu(q_n)}{\sqrt{m}\,\tau(q_n)}
 \ \Longrightarrow\ \mathcal N(0,1).
\]
With \(F(q)=(1+q)\log(1+q)-q\log q-2q\log2\), the exact mean satisfies, uniformly when \(q_n\) stays in a fixed compact subset of \((0,1)\),
\[
 \mathbb E X_{n,m}
 =\sqrt{\frac{2}{1+q_n}}\,e^{nF(q_n)}\bigl(1+O(n^{-1})\bigr).
\]
In particular, the maximum possible exponential mean rate is \(F(1/3)=\log(4/3)\), attained at the deletion fraction \(1/3\). Yet the typical rate is strictly smaller: setting \(z=(1-q)/(1+q)\) and
\[
 P_q(s)=q(1-q)^{s-1},\qquad Q_q(s)=(1-z)^2s z^{s-1},
\]
we have
\[
 \frac{\log\mathbb E X_{n,m}-\log X_{n,m}}{n}
 \ \xrightarrow{\mathbb P}\ F(q)-q\mu(q)
 =q D_{\mathrm{KL}}(P_q\Vert Q_q)>0.
\]
At the one-third deletion fraction, the logarithmic mean and typical rates are respectively \(0.28768207245\ldots\) and \(0.27620221078\ldots\) per vertex, so the average squared intrinsic volume is exponentially larger than its typical value.

## Assumptions and scope
The graph is the simple labeled cycle with \(n\ge3\); the \(m\) missing edges are a uniformly selected \(m\)-subset of its \(n\) edges, not independent vertex thinning. We restrict \(1\le m\le n-1\) so that \(P_G\) has positive intrinsic dimension \(k=n-m\). This dimension changes with \(m\), which is why comparisons across deletion counts use the explicitly normalized \(X_{n,m}\), not raw volumes in differing dimensions. The central limit theorem and entropy comparison are only asserted when \(m/n\) tends to a fixed limit strictly between zero and one; no endpoint-uniform limit is claimed. All logarithms are natural.

## Proof
**1. The Gram-volume identity.** Orient the \(k\) retained edges arbitrarily and form their \(n\times k\) incidence matrix \(B\), with columns \(e_i-e_j\). Because \(G\) is a forest, the columns are linearly independent. The image under \(B\) of the standard \(k\)-cross-polytope \(\operatorname{conv}\{\pm e_1,\ldots,\pm e_k\}\) is precisely \(P_G\). The Euclidean Jacobian for this linear embedding is \(\sqrt{\det(B^{\mathsf T}B)}\), and the standard cross-polytope has volume \(2^k/k!\). Thus
\[
 X_{n,m}=\det(B^{\mathsf T}B).
\]
Each component is a path on \(s_i\) vertices. Its incidence Gram matrix is the \((s_i-1)\)-by-\((s_i-1)\) tridiagonal matrix with diagonal \(2\) and off-diagonal \(-1\). Its determinant \(d_j\) obeys \(d_0=1,d_1=2,d_j=2d_{j-1}-d_{j-2}\); hence \(d_j=j+1\). Isolated vertices contribute the empty determinant \(1\). Since the component Gram matrices are block diagonal, \(\det(B^{\mathsf T}B)=\prod_i s_i\).

**2. Uniform cyclic gaps and exact moments.** Mark one of the \(m\) deleted edges, and read clockwise the \(m\) positive lengths \(s_i\) of the path components between successive missing edges. There are \(n\binom{n-1}{m-1}=m\binom nm\) such marked configurations, and each ordered positive composition of \(n\) into \(m\) parts occurs at exactly \(n\) choices of marked starting position. Since \(X_{n,m}\) is invariant under the marking, its distribution is that of \(\prod_i s_i\) for a uniform positive composition of \(n\) into \(m\) parts. The number of these is \(\binom{n-1}{m-1}\). Taking ordinary generating functions gives the Mellin-transform identity. At \(t=1\), use
\[
 \sum_{s\ge1}sz^s=\frac{z}{(1-z)^2},\qquad
 [z^n]\left(\frac{z}{(1-z)^2}\right)^m
 =\binom{n+m-1}{n-m},
\]
which simplifies to the Gamma ratio in the claim.

**3. Sharp one-third extremum and large-deviation-scale mean.** Write \(M_{n,m}=\mathbb E X_{n,m}\). Direct division of the two exact expressions gives
\[
 \frac{M_{n,m+1}}{M_{n,m}}
 =\frac{n+m}{2(2m+1)}
\]
for \(1\le m<n-1\). This is greater than, equal to, or less than \(1\) according as \(n>3m+2\), \(n=3m+2\), or \(n<3m+2\), proving the complete maximizer classification. Stirling's expansion applied to \(\Gamma(m)\Gamma(n+m)/(\Gamma(2m)\Gamma(n))\), uniformly on compact deletion-fraction intervals, yields the stated exponential mean and prefactor. Differentiation gives \(F'(q)=\log((1+q)/(4q))\) and \(F''(q)=-1/[q(1+q)]<0\); therefore \(q=1/3\) uniquely maximizes the limiting rate, with \(F(1/3)=\log(4/3)\).

**4. Conditional central limit theorem.** Set \(q_n=m/n\). Let \(S_1,\ldots,S_m\) be independent geometric random variables with success probability \(q_n\), and write \(T_i=\log S_i\). Every positive integer vector with sum \(n\) has the same probability \(q_n^m(1-q_n)^{n-m}\), so the law of the composition is exactly the conditional law of \((S_1,\ldots,S_m)\) given \(\sum_iS_i=n\). Notice that \(\sum_i \mathbb E S_i=m/q_n=n\): the conditioning is at the mean.

For completeness, a standard Fourier-inversion argument gives the conditional limit here. Let \(v=\operatorname{Var}(S_{q_n})\), \(c=\operatorname{Cov}(S_{q_n},T_{q_n})\), and \(w=\operatorname{Var}(T_{q_n})\). The conditional characteristic function of \((\sum_iT_i-m\mu(q_n))/\sqrt m\) is the quotient of the inversion integrals on \([ -\pi,\pi]\) for the joint characteristic function of the centered pair \((S_{q_n}-1/q_n,T_{q_n}-\mu(q_n))\), once with and once without the logarithmic Fourier argument. On writing the Fourier variable as \(u/\sqrt m\), the logarithm of its \(m\)-th power converges locally uniformly to
\[
 -\frac12\bigl(vu^2+2cut+wt^2\bigr).
\]
Because geometric variables have uniformly exponential tails for \(q_n\) in a compact subset of \((0,1)\), Taylor remainders are uniform. Their integer span equals \(1\); hence outside any fixed neighborhood of Fourier frequency zero their characteristic functions have modulus uniformly below \(1\), while a quadratic Gaussian bound controls the inner region. The off-origin contributions vanish exponentially and dominated convergence applies after rescaling. Dividing the resulting Gaussian integrals gives \(\exp\{-t^2(w-c^2/v)/2\}\). By strict Cauchy–Schwarz, \(w-c^2/v>0\): \(\log s\) is not affine in \(s\) on the geometric support \(s\ge1\). This proves the stated conditional Gaussian limit.

**5. The strict annealed–typical gap.** The central limit theorem implies \(\log X_{n,m}/n\to q\mu(q)\) in probability. Combining with Stirling gives a gap \(F(q)-q\mu(q)\). The probability distribution \(Q_q(s)=(1-z)^2sz^{s-1}\), where \(z=(1-q)/(1+q)\), is normalized by \(\sum_{s\ge1}sz^{s-1}=(1-z)^{-2}\) and has the same mean \(1/q\) as \(P_q\). Direct substitution into \(D_{\mathrm{KL}}(P_q\Vert Q_q)=\sum_sP_q(s)\log(P_q(s)/Q_q(s))\) gives exactly
\[
 qD_{\mathrm{KL}}(P_q\Vert Q_q)=F(q)-q\mu(q).
\]
The two distributions differ for every \(0<q<1\), because their consecutive probability ratios are respectively constant and proportional to \((s+1)/s\). Strict positivity of Kullback–Leibler divergence finishes the proof.

## Verification
The standalone `verify.py` provides exact incidence-Gram determinant checks for every retained-edge subset of cycles from \(n=3\) through \(n=10\). It independently enumerates component sizes and verifies the full conditional mean and sharp finite optimum. Additional numerical checks cover the predicted Stirling prefactor, the strict divergence identity, the positive conditional variance, and finite-composition moment convergence to the stated conditional Gaussian variance. Run with `python verify.py` (Python 3 plus SymPy). In the recorded run, all **2,086** checks passed. Exact enumeration is limited to the indicated sizes and does not substitute for steps 1–5 of the proof.

## Relationship to prior work
Donzelmann, Juhnke, Rednoß, and Thäle (2026) introduce distributional analysis for random symmetric-edge polytopes on Erdős–Rényi graphs, studying face and triangulation-edge counts rather than intrinsic Euclidean volume in a cycle-edge deletion model. Their full paper motivates moving to another natural random-graph geometry observable.

The incidence Gram determinant and rooted-forest interpretation are classical; the exact mean is therefore also recognizable as a coefficient of the rooted-forest enumerator of a cycle. It is not claimed that this determinant identity or general matrix-forest enumeration is new. The contribution here is the integrated *geometric* conditional volume law, the exact deletion-density maximizer, the conditional log-volume fluctuation coefficient, and the strict exponential separation between mean and typical squared volume.

Schmutz and Shapcott (2012) prove asymptotic lognormality of the product of parts in compositions with a **varying number of parts**. Their result does not assert the fixed-proportion, fixed-part-count central limit theorem and covariance-projection variance above; its methods and classical composition correspondence are relevant precedents. Cuchilla et al. (2025) study volume relationships for permutation-fixed symmetric-edge-polytopes, not this random intrinsic-volume distribution. Tamura and Tanaka (2026) study rooted spanning forests of wheel graphs with prescribed roots, rather than cycle-edge deletion volume fluctuations. Other published studies of cycle graphical zonotopes concern Minkowski sums and intrinsic-volume profiles, whereas the present bodies are centrally symmetric *convex hulls* of retained roots.

## Limitations
The exact identities include all \(1\le m\le n-1\), but the asymptotic statements require the deletion fraction bounded away from both endpoints. The squared intrinsic-volume normalization is part of the definition and is essential when comparing different random intrinsic dimensions; no monotonicity of unnormalized Euclidean volumes is asserted. The central limit theorem has no claimed Berry–Esseen rate. Classical rooted-forest formulas and composition probability methods provide substantial ingredients; historical priority for the combined conditional geometric conclusions remains provisional, and no independent mathematical audit has been performed.

## References
1. T. Donzelmann, M. Juhnke, B. Rednoß, C. Thäle, *Central limit theorems for high dimensional lattice polytopes: symmetric edge polytopes*, arXiv:2603.10650v1, first public March 11, 2026. https://arxiv.org/abs/2603.10650
2. E. Schmutz, C. Shapcott, *Part-products of S-restricted integer compositions*, arXiv:1203.2374v1, March 11, 2012. https://arxiv.org/abs/1203.2374
3. T. A. Cuchilla et al., *Unitary actions and equivariant volumes of symmetric edge polytopes*, arXiv:2507.18846, July 24, 2025. https://arxiv.org/abs/2507.18846
4. S. Tamura, Y. Tanaka, *Rooted spanning forests in wheel graphs: Fibonacci-Lucas formulas and extremal root configurations*, arXiv:2609.29486, September 4, 2026. https://arxiv.org/abs/2609.29486
