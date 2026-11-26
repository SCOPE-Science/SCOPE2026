# Two-step minimax edge sampling on the four-vertex path

## Finding

Let \(P_n\) be the path with vertices \(1,\ldots,n\). At each independent iteration select edge \(i\)--\(i+1\) with a fixed probability \(p_i\), then replace its two endpoint values by their arithmetic mean. For a unit-norm initial vector orthogonal to the constants, let \(F_k(p)\) be the worst expected squared Euclidean norm after exactly \(k\) iterations. On \(P_4\), the **unique** one-step minimax sampling law is
\[
 p^{(1)}=(3/10,2/5,3/10),\qquad F_1(p^{(1)})=9/10.
\]
The **unique** two-step minimax law instead is
\[
 p^{(2)}=(a_*,1-2a_*,a_*),\quad
 a_*=0.302839075823308103\ldots,\quad
 F_2(p^{(2)})=0.774552853191493931\ldots,
\]
where \(a_*\) is the unique minimizer on \([0,1/2]\) of
\[
 f(a)=\frac12+\frac{10a^2-3a+\sqrt{116a^4+68a^3+5a^2-48a+16}}8.
\]
It is characterized without numerical optimization as the unique zero of \(f'(a)\) in \((0,1/2)\). In particular \(a_*>3/10\): the best one-step law is strictly suboptimal even after only two steps. Moreover, among paths \(P_n\) with \(n\ge2\), \(P_4\) is the smallest where the unique one- and two-step minimax laws disagree: on \(P_2\) and \(P_3\), the minimizers coincide.

At the one-step law, the exact two-step loss is \(F_2(p^{(1)})=1/2+\sqrt{754}/100\), strictly exceeding \(F_2(p^{(2)})\) by \(0.00003775116342568\ldots\). The separation concerns **exact worst-case two-step mean-square error**, not just its usual spectral-gap upper bound.

## Assumptions and scope

All graphs are unweighted simple paths, and probabilities \(p_i\ge0\) sum to one. Sampling is independent and identically distributed over iterations; the same law is used at both steps. There is no relaxation, exogenous noise, adaptivity, or sequential re-optimization. For the standard basis vectors \(e_i\), let
\[
 P_i=I-\tfrac12(e_i-e_{i+1})(e_i-e_{i+1})^{\mathsf T},\quad
 x^{(k)}=P_{i_k}\cdots P_{i_1}x^{(0)}.
\]
Write \(V_n=\{x\in\mathbb R^n:\sum_jx_j=0\}\). The criterion has the precise quantifier order
\[
 F_k(p)=\max_{x\in V_n,\,\|x\|_2=1}\mathbb E_{i_1,\ldots,i_k}\|P_{i_k}\cdots P_{i_1}x\|_2^2,
\]
with a single deterministic starting vector chosen adversarially **before** sampling. All maxima and minima exist by finite-dimensional compactness.

## Proof

**1. Exact moment matrices.** Since the \(P_i\) are orthogonal projections, put
\[
 M_1(p)=\sum_i p_iP_i=I-\tfrac12L_p,\qquad
 M_2(p)=\sum_{i,j}p_ip_jP_iP_jP_i,
\]
where \(L_p=\sum_i p_i(e_i-e_{i+1})(e_i-e_{i+1})^{\mathsf T}\). Then \(F_k(p)=\lambda_{\max}(M_k(p)|_{V_n})\) for \(k=1,2\). The order \(P_iP_jP_i\) follows by expanding the squared norm of \(P_jP_i x\); it cannot be replaced by the square of the average matrix.

**2. Unique one-step law on \(P_4\).** Set \(w=(-3,-1,1,3)^{\mathsf T}\). Because \(\|w\|^2=20\) and every successive difference has square \(4\), the Rayleigh quotient obeys
\[
 \lambda_2(L_p)\le\frac{w^{\mathsf T}L_pw}{\|w\|^2}=\frac15
\]
for every sampling distribution. At \(p=(3/10,2/5,3/10)\), the eigenvalues of \(L_p\) are exactly \(0,1/5,3/5,6/5\), so equality is attained. If any law attains equality, \(w\) itself must be an eigenvector of \(L_p\) for eigenvalue \(1/5\), since it attains the smallest nonzero Rayleigh quotient on \(V_4\). The first and last eigenvector equations force \(p_1=p_3=3/10\), and normalization forces \(p_2=2/5\). Thus this law is unique and its largest \(M_1\) eigenvalue on \(V_4\) equals \(1-(1/5)/2=9/10\).

**3. Reflection symmetrization and its strictness.** Every distribution is uniquely \(p=(a+d,1-2a,a-d)\), where \(0\le a\le1/2\) and \(|d|\le a\). Let \(W(a)=M_2(a,1-2a,a)\). The end-edge projections commute because the edges are disjoint; consequently
\[
 \tfrac12\big(M_2(a+d,1-2a,a-d)+M_2(a-d,1-2a,a+d)\big)
 =W(a)+d^2H,
\]
where \(H=(P_1-P_3)^2\succeq0\). Reflecting the path conjugates the matrices at \(d\) and \(-d\), so their restricted top eigenvalues coincide. Convexity and monotonicity of the largest eigenvalue give \(F_2(a+d,1-2a,a-d)\ge F_2(a,1-2a,a)\).

To prove strictness at any potential minimizing interior point, use the orthonormal zero-sum vectors
\[
 s=(1,-1,-1,1)^{\mathsf T}/2,\quad
 u=(1,0,0,-1)^{\mathsf T}/\sqrt2,\quad
 v=(0,1,-1,0)^{\mathsf T}/\sqrt2.
\]
In this basis \(W(a)|_{V_4}\) is the direct sum of
\[
 S(a)=\frac{6a^2-9a+4}{4},\qquad
 B(a)=\frac18\begin{pmatrix}
 6a^2-9a+8&a(10a+1)\\
 a(10a+1)&a(14a+3)
\end{pmatrix}.
\]
For \(0<a\le1/2\), \(B_{11}-S=3a(3-2a)/8>0\); hence the top eigenvalue of \(W|_{V_4}\) comes from \(B\). For \(0<a<1/2\), \(B_{11}-B_{22}=1-3a/2-a^2>0\) and \(B_{12}>0\); its top unit eigenvector has positive coordinates \((\alpha,\beta)\) with \(\alpha>\beta\). On the span of \(u,v\), the matrix \(H\) is \(\tfrac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\), giving the strict Rayleigh increment \(d^2(\alpha-\beta)^2/2\) whenever \(d\ne0\). At \(a=0\) or \(a=1/2\), one edge is never sampled, so \(F_2=1\). Since the interior symmetric point \(a=3/10\) gives less than one, **every** global two-step minimizer has \(d=0\) and \(0<a<1/2\).

**4. Unique exact two-step minimizer.** The larger eigenvalue of \(B(a)\) simplifies to the displayed \(f(a)\). To prove strict convexity on the entire interval without numerical evidence, write
\[
 z_1(a)=1-3a/2-a^2,\quad z_2(a)=a(10a+1)/4,\quad
 r(a)=\sqrt{z_1(a)^2+z_2(a)^2}.
\]
Here \(z_1,z_2\ge0\), \(r>0\), and \(r=\sqrt{116a^4+68a^3+5a^2-48a+16}/4\). The standard norm-differentiation identity yields
\[
 r''=\frac{\|z'\|^2-(z\cdot z')^2/r^2}{r}+\frac{z\cdot z''}{r}
 \ge \frac{-2z_1+5z_2}{r}\ge-2.
\]
Since \(f=(\operatorname{tr}B+r)/2\) and \((\operatorname{tr}B)''=5\), one has \(f''\ge3/2>0\). Direct differentiation gives
\[
 f'(a)=\frac{20a-3}{8}+
 \frac{464a^3+204a^2+10a-48}{16\sqrt{116a^4+68a^3+5a^2-48a+16}},
\]
with \(f'(0)=-9/8\), \(f'(1/2)=9/4\), and
\[
 f'(3/10)=\frac38-\frac{441\sqrt{754}}{30160}<0.
\]
Thus precisely one stationary point occurs, it is the unique global minimum, and it satisfies \(a_*>3/10\). To verify the last strict inequality exactly, square positive sides to check \(441^2\cdot754> (3\cdot30160/8)^2\). High-precision interval evaluation brackets \(302839075823/10^{12}<a_*<302839075824/10^{12}\), with the quoted decimal value.

**5. Minimality among paths.** For \(P_2\), there is only one edge and hence only one law. On \(P_3\), let \(p\) and \(1-p\) be the edge probabilities, and \(t=p(1-p)\). A two-dimensional calculation on \(V_3\) gives \(\operatorname{tr}(M_2|_{V_3})=1-3t/2\) and \(\det(M_2|_{V_3})=3t/16+27t^2/64\). Therefore
\[
 F_2(p)=\tfrac12\left(1-\tfrac32t+\sqrt{1-\tfrac{15}{4}t+\tfrac9{16}t^2}\right).
\]
Both the outer linear term and the positive square-root term strictly decrease as \(t\) ranges from zero to \(1/4\); hence \(p=1/2\) is the unique two-step optimum. The one-step factor is \(F_1(p)=(1+\sqrt{1-3t})/2\), likewise uniquely minimized at \(p=1/2\). The first divergence between horizons therefore occurs exactly on \(P_4\).

## Verification

The accompanying standalone \(\texttt{verify.py}\) runs using only Python's standard library. It checks projection identities, the displayed \(P_4\) invariant blocks and strict-symmetrization polynomial, the exact \(P_3\) two-step trace and determinant, the one-step eigenvector equality, and the rational bracket for the two-step optimizer. It prints `VERIFY_OK`. The universal inequalities and uniqueness are proved analytically above; sampling checks and decimal approximations are **not** substituted for those proofs.

## Relationship to prior work

Pairwise averaging is the edge-incidence case of randomized Kaczmarz. Strohmer and Vershynin (2007) establish randomized Kaczmarz convergence rates; Boyd and collaborators (2004) optimize gossip by the second eigenvalue of the average update matrix. This exactly captures the one-step minimax law here, but not the finite-horizon mean-square optimum. Agaskar, Wang, and Lu (2014) give a formula for exact Kaczmarz mean-square error at any iteration count and optimize the **asymptotic annealed error exponent**, rather than solving the worst-initial-condition finite-two-step probability minimization for \(P_4\). Gower and Richtárik (2015) provide the general sketch-and-project perspective and geometric bounds. The present claim is the explicit global finite-horizon **optimizer**, its provably different value at horizons one and two, and the smallest-path boundary, not the established general MSE formula or the general theory of random gossip.

## Limitations

Only the paths with two, three, or four vertices and exactly one or two draws are classified. The result does not assert a formula for optimal probabilities on larger graphs, longer horizons, state-dependent sampling, or other error norms. The improvement in two-step worst-case error is small but strictly positive; the substantive feature is the proved optimizer change and its first possible graph size. Searches of available literature and mathematical-result records did not identify the same exact classification, but unindexed or uninspected results may overlap. Independent validation has not been performed.

## References

1. T. Strohmer and R. Vershynin, *A randomized Kaczmarz algorithm with exponential convergence*, first public arXiv version 8 February 2007, https://arxiv.org/abs/math/0702226.
2. S. Boyd, A. Ghosh, B. Prabhakar, and D. Shah, *Analysis and Optimization of Randomized Gossip Algorithms*, CDC 2004, https://web.stanford.edu/~boyd/papers/pdf/gossip_opt.pdf.
3. A. Agaskar, C. Wang, and Y. M. Lu, *Randomized Kaczmarz algorithms: Exact MSE analysis and optimal sampling probabilities*, GlobalSIP 2014, DOI 10.1109/GlobalSIP.2014.7032145, https://dash.harvard.edu/entities/publication/73120379-2750-6bd4-e053-0100007fdf3b.
4. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, arXiv first version 10 June 2015, https://arxiv.org/abs/1506.03296, DOI 10.1137/15M1025487.
