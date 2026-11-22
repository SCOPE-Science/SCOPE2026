# Sharp two-threshold smoothness–frame-stability frontier for cycle-host Fourier extensions

## Finding

Let integers \(m\ge3\) and \(q\ge\max\{2,m-2\}\) be given, and put \(N=m+q\). View \(m\) consecutive vertices of the unweighted cycle \(C_N\) as the isometrically embedded path \(P_m\). Let \(W:\mathbb C^N\to\mathcal K\) be **any** Parseval analysis map, \(W^*W=I_N\), including the normalized full Fourier transform and the normalized full-translation spectral-filter-bank wavelet transforms on the cyclic group. Consider every complex-linear completion \(E:\mathbb C^m\to\mathbb C^N\) which reproduces the \(m\) observed values exactly. For a prescribed budget \(\beta\ge0\), impose
\[
\|WE\|_{2\to2}^2\le1+\beta.
\]
Let \(L_N\) denote the **combinatorial** (not normalized) cycle Laplacian and minimize the trace Dirichlet energy \(\operatorname{Tr}(E^*L_NE)\) over these completions. Then the optimum is unique, real, and depends only on the two endpoint values of the observed path.

Put
\[
 s_+(q)=\frac q2,\qquad s_-(q)=\frac{q(q-1)}{6(q+1)},
 \qquad 0<s_-(q)<s_+(q).
\]
As the budget increases there are **exactly two parity-mode activation thresholds**:

* For \(0<\beta<s_-(q)\), both the endpoint-symmetric and endpoint-antisymmetric complementary profiles are strictly regularized.
* For \(s_-(q)\le\beta<s_+(q)\), the antisymmetric profile is exactly harmonic while the symmetric profile remains strictly regularized.
* For \(\beta\ge s_+(q)\), the completion is exactly the unconstrained harmonic extension.

More precisely, let \(A_q\) be the \(q\times q\) tridiagonal Dirichlet Laplacian with diagonal \(2\) and immediate off-diagonal \(-1\), and \(b_\pm=(e_1\pm e_q)/\sqrt2\) in \(\mathbb R^q\). Set
\[
 F_\pm(\lambda)=\|(A_q+\lambda I)^{-1}b_\pm\|_2^2,\qquad \lambda\ge0.
\]
For \(\beta\ge s_\pm(q)\) take \(\lambda_\pm=0\); for \(0<\beta<s_\pm(q)\) let \(\lambda_\pm>0\) be the **unique** solution of \(F_\pm(\lambda_\pm)=\beta\); and interpret \(\lambda_\pm=+\infty\) at \(\beta=0\). The unique completion assigns the missing \(q\) values to
\[
 T_\beta(a,b)=\frac{a+b}{\sqrt2}(A_q+\lambda_+I)^{-1}b_+
   +\frac{a-b}{\sqrt2}(A_q+\lambda_-I)^{-1}b_-,
\]
where the resolvent is understood as zero at \(\lambda=+\infty\). All nonendpoint observed coordinates have zero influence on the missing values. Its sharp lower and upper squared frame bounds are
\[
 \boxed{1\quad\text{and}\quad1+\min\{\beta,q/2\}.}
\]

The exact optimal trace energy is \(2(m-1)+J_q(\beta)\), where
\[
 J_q(\beta)=2-\sum_{\sigma\in\{+,-\}}
 \left[G_\sigma(\lambda_\sigma)+\lambda_\sigma F_\sigma(\lambda_\sigma)\right],
\quad
G_\sigma(\lambda)=\langle b_\sigma,(A_q+\lambda I)^{-1}b_\sigma\rangle,
\]
with each bracket interpreted as zero for \(\lambda_\sigma=+\infty\). Both scalar functions are **explicit finite trigonometric sums**:
\[
 \begin{aligned}
 F_+(\lambda)&=\frac4{q+1}\sum_{\substack{1\le k\le q\\k\text{ odd}}}
 \frac{\sin^2(k\pi/(q+1))}{[\lambda+2-2\cos(k\pi/(q+1))]^2},\\
 F_-(\lambda)&=\frac4{q+1}\sum_{\substack{1\le k\le q\\k\text{ even}}}
 \frac{\sin^2(k\pi/(q+1))}{[\lambda+2-2\cos(k\pi/(q+1))]^2},
 \end{aligned}
\]
while \(G_\pm\) use the same sums with denominator to the first power. In particular,
\[
 J_q(0)=2,\qquad J_q(\beta)=\frac2{q+1}\quad(\beta\ge q/2),
 \qquad J_q(\beta)=2-4\sqrt\beta+4\beta+O_q(\beta^{3/2})\quad(\beta\downarrow0).
\]
For the first nontrivial missing arc, \(q=2\), the frontier is entirely elementary:
\[
\boxed{J_2(\beta)=
\begin{cases}
2-4\sqrt\beta+4\beta,&0\le\beta\le1/9,\\
(1-\sqrt\beta)^2+2/3,&1/9\le\beta\le1,\\
2/3,&\beta\ge1.
\end{cases}}
\]
For all \(q\ge2\), the two thresholds are asymptotic to \(q/6\) and \(q/2\), respectively, so their ratio tends to \(1/3\).

## Assumptions and scope

All Hilbert-space norms and traces are unweighted counting-measure norms. The cycle carries the unit-conductance graph energy \(\sum_{\{u,v\}\in E(C_N)}|x_u-x_v|^2\). The \(m\) observed vertices are consecutive, with their order fixed. The complementary arc has \(q\) unobserved vertices and \(q+1\) edges. The inequality \(q\ge m-2\) makes the path inclusion isometric; the extra condition \(q\ge2\) keeps the symmetric and antisymmetric positive thresholds distinct. The trace energy is the sum of cycle energies of the completions of an orthonormal basis of \(\mathbb C^m\), equivalently the expected cycle energy for a zero-mean, identity-covariance observed signal. There is no positivity, support, or statistical distribution assumption on individual signals. Completions are **all** complex-linear maps fixing observed values, not merely endpoint-local or reflection-equivariant maps.

## Proof

**1. Frame reduction and boundary locality.** Order the cycle so that the observed path occupies the first \(m\) coordinates and the missing arc occupies the last \(q\). Every admissible \(E\) has block form \(E f=(f,Tf)\) for some complex \(q\times m\) matrix \(T\). Parseval gives \(\|WEf\|^2=\|f\|^2+\|Tf\|^2\), so the budget is exactly \(\|T\|_{2\to2}^2\le\beta\). The \(m-1\) internal path edges give a fixed trace contribution \(2(m-1)\). Write the remaining, complementary-arc trace contribution as
\[
 \operatorname{Tr}(T^*A_qT)-2\operatorname{Re}\operatorname{Tr}(B^*T)+2,
\]
where \(B\) has columns \(e_1,e_q\) at the two observed endpoints and zero columns elsewhere. Each nonendpoint column of \(T\) contributes the strictly positive quadratic form \(v^*A_qv\), with no linear term. Setting such columns to zero cannot increase \(\|T\|\), since right-composition with an orthogonal coordinate projection is contractive. Consequently the unique minimizer, if it exists, is endpoint-local. The objective is strictly convex because \(A_q\) is positive definite; the spectral-norm ball is closed, bounded and convex. A unique global minimizer therefore exists for every \(\beta\ge0\).

**2. Symmetry and independent scalar ball constraints.** Reflect both the missing arc and the two observed endpoints. The objective and spectral-norm constraint are invariant under this transformation, so uniqueness forces the minimizing endpoint matrix to commute with reflection. Its real and imaginary parts also obey the real-data symmetry; complex conjugation plus uniqueness makes the minimizer real. In the orthonormal endpoint parity basis \(u_\pm=(1,\pm1)/\sqrt2\), its two missing-coordinate columns \(v_\pm\) are symmetric and antisymmetric under reversal, hence orthogonal. Thus \(\|T\|^2=\max\{\|v_+\|^2,\|v_-\|^2\}\), and the energy separates into
\[
 2+\sum_{\sigma\in\{+,-\}}
 [\langle v_\sigma,A_qv_\sigma\rangle
 -2\langle b_\sigma,v_\sigma\rangle],
 \qquad \|v_\sigma\|^2\le\beta.
\]
Each scalar-channel quadratic is strictly convex. The unique norm-ball minimizer is its harmonic value \(A_q^{-1}b_\sigma\) if feasible and otherwise \((A_q+\lambda_\sigma I)^{-1}b_\sigma\) for the unique positive KKT multiplier satisfying the active norm constraint. Strict decrease of \(F_\sigma\) follows from its positive spectral expansion (or from differentiating the squared resolvent norm). The KKT conditions are sufficient because the optimization is convex; uniqueness handles the boundary \(\beta=0\) directly.

**3. Exact thresholds.** The inverse of the Dirichlet path Laplacian is
\[
 (A_q^{-1})_{ij}=
 \frac{\min\{i,j\}(q+1-\max\{i,j\})}{q+1},\qquad1\le i,j\le q.
\]
Therefore the unconstrained extension of endpoint data \((a,b)\) has value \(((q+1-t)a+tb)/(q+1)\) at position \(t\). The symmetric unit endpoint vector extends to the constant vector \((1/\sqrt2,\ldots,1/\sqrt2)\), whose squared norm is \(q/2\). The antisymmetric vector extends to entries \((q+1-2t)/(\sqrt2(q+1))\), whose squared norm is \(q(q-1)/[6(q+1)]\), by the elementary centered-square sum. These norms are strictly ordered for \(q\ge2\). They are exactly \(F_\pm(0)\), proving all three phases and both sharp thresholds.

**4. Exact value, spectral sums and frame bounds.** If \(v_\sigma=(A_q+\lambda_\sigma I)^{-1}b_\sigma\), then \(A_qv_\sigma=b_\sigma-\lambda_\sigma v_\sigma\), and the channel energy is \(1-G_\sigma(\lambda_\sigma)-\lambda_\sigma F_\sigma(\lambda_\sigma)\). Summing proves the asserted exact optimal trace. The Dirichlet sine eigenvectors of \(A_q\) have eigenvalues \(2-2\cos(k\pi/(q+1))\); their endpoint reflection parity is \((-1)^{k+1}\). Expansion of \(b_\pm\) in these eigenvectors gives exactly the displayed odd/even finite sums. The winning completion has two orthogonal missing-coordinate columns, with squared norms \(\min\{\beta,s_+\}\) and \(\min\{\beta,s_-\}\). Since an interior observed coordinate is untouched by \(T\), the least eigenvalue of \(E^*E=I_m+T^*T\) is exactly \(1\) for \(m\ge3\); the greatest is exactly \(1+\min\{\beta,q/2\}\). Parseval transfers these sharp bounds to \(WE\).

**5. Endpoint values and fine-budget asymptotics.** Zero padding has complementary-arc trace \(2\). Unconstrained harmonic continuation has complementary-arc trace \(2/(q+1)\), giving the claimed endpoints. As \(\beta\downarrow0\), both norm constraints are active and \(v_\sigma=\sqrt\beta\,b_\sigma+O_q(\beta)\) with transverse correction orthogonal to \(b_\sigma\) to first order. Hence \(\langle b_\sigma,v_\sigma\rangle=\sqrt\beta+O_q(\beta^{3/2})\) and \(\langle v_\sigma,A_qv_\sigma\rangle=\beta\langle b_\sigma,A_qb_\sigma\rangle+O_q(\beta^{3/2})\). As \(\langle b_+,A_qb_+\rangle+\langle b_-,A_qb_-\rangle=4\), the small-budget expansion follows. For \(q=2\), \(b_+,b_-\) are eigenvectors of \(A_2\) of eigenvalues \(1,3\), giving the stated three-piece closed form. Finally \(s_-(q)/s_+(q)=(q-1)/(3(q+1))\to1/3\).

## Verification

The accompanying `verify.py` is a Python 3 standard-library script. Execute `python3 verify.py` in the same extracted directory. It uses exact rational arithmetic to verify the harmonic threshold identities and both endpoint energies for \(2\le q\le30\). It independently compares resolvent norm calculations with the odd/even sine-spectrum expansions, checks that the optimal extension hits its permitted sharp frame upper bound, tests thousands of random feasible competing completions (including a nonendpoint column), and checks unitary discrete Fourier energy conservation on sample host cycles. In the final reviewed package it printed `PASS: 6242 exact-identity, spectral, numerical and feasible-competitor checks`. These finite checks test calculations but do not replace the all-integer proof above.

## Relationship to prior work

Souop and Bitjoka (arXiv:2607.14168, first publicly submitted July 15, 2026) construct Parseval Fourier-group graph wavelets and identify unconstrained minimum-Dirichlet-energy harmonic host completion. The presently identified target is **different**: all linear completions are optimized under an externally imposed sharp Parseval-analysis amplification budget, with exact two activation thresholds and an energy frontier on a canonical isometric path-in-cycle embedding. Unconstrained harmonic completion is precisely the final branch here, not a new claim. Beck, Ghandehari, Hudson and Paltenstein (arXiv:2303.02812) construct group-theoretic Cayley frames and characterize their frame bounds without giving this constrained-completion frontier. Ou, Yao and Zhang (arXiv:2611.10692) characterize when zero extension preserves a graph Dirichlet equation and compute interface errors, rather than optimize the smoothness versus coefficient-energy amplification of arbitrary linear completions. These comparisons rely on the accessible portions/material stated in the accompanying literature review; a complete section-by-section inspection of the motivating 2026 manuscript was unavailable, so older equivalent optimization formulas or an uninspected appendix remain bibliographic risks.

## Limitations

The result concerns unweighted cycle hosts with a **single contiguous observed path**, counting-measure norms, trace-average Dirichlet energy, complex-linear completions and a host Parseval analysis. It does not claim the same two thresholds for irregular hosts, weighted paths, sparse/noncontiguous observations, nonlinear extensions, anisotropic input covariance, or maximum-over-input Dirichlet energy. The minimized trace is an isotropic expected energy, not a minimax energy. The exact frontiers are independent of the chosen Parseval filters because complete Parseval coefficient energy is fixed; they do not optimize a partial, bandlimited or erased subfamily of wavelet coefficients. No independence, external certification, or publication priority is asserted.

## References

1. R. Fokam Souop and L. Bitjoka, *Tight Wavelet Frames on Graphs via Isometric Group Embedding*, arXiv:2607.14168v1 (July 15, 2026), https://arxiv.org/abs/2607.14168.
2. K. Beck, M. Ghandehari, S. Hudson and J. Paltenstein, *Frames for Signal Processing on Cayley Graphs*, arXiv:2303.02812 (2023), https://arxiv.org/abs/2303.02812; Journal of Fourier Analysis and Applications **30** (2024), article 66.
3. Y. Ou, X. Yao and G. Zhang, *Zero Extension for the Dirichlet Problem on Graphs*, arXiv:2611.10692v1 (November 7, 2026), https://arxiv.org/abs/2611.10692.
