# Logarithmic positivity delay with vanishing amplitude in anisotropic four-cycle fractional heat

## Finding

Consider the four vertices \(V=\{0,1\}^2\). Give both edges that change the first coordinate conductance \(a>0\), and both edges that change the second coordinate conductance \(b>0\). Let \(L\) be the *combinatorial*, rather than normalized, weighted graph Laplacian. For every real \(\alpha>0\) and \(t\geq0\), define
\[
K_\alpha(t)=\exp(-tL^\alpha),
\]
using the nonnegative spectral functional calculus and \(0^\alpha=0\). Write
\[
A=(2a)^\alpha,\qquad B=(2b)^\alpha,\qquad
C=(2a+2b)^\alpha,\qquad
q(t)=1-e^{-At}-e^{-Bt}+e^{-Ct}.
\]

**Exact sign classification.** All diagonal entries and all entries across an original edge of \(K_\alpha(t)\) are strictly positive for \(t>0\). Each of its four antipodal (graph-distance-two) entries is \(q(t)/4\). If \(0<\alpha\leq1\), all entries are strictly positive for every \(t>0\). If \(\alpha>1\), there exist unique times \(0<s_\alpha<t_\alpha<\infty\) such that \(q\) decreases on \((0,s_\alpha)\), increases on \((s_\alpha,\infty)\), is negative precisely on \((0,t_\alpha)\), and vanishes at \(t_\alpha\). Thus the exact entrywise nonnegativity condition is \(t=0\) or \(t\geq t_\alpha\). Moreover,
\[
\|K_\alpha(t)\|_{\infty\to\infty}
=1+\tfrac12\max\{0,-q(t)\},
\]
and its unique peak for \(\alpha>1\) occurs at \(s_\alpha\), characterized by
\[
A e^{(C-A)s_\alpha}+B e^{(C-B)s_\alpha}=C.
\]

**Uniform scalar bracket and weak-edge singularity.** By interchanging the two coordinate directions, suppose \(0<a\leq b\). For \(\alpha>1\), set
\[
r=a/b,\quad\delta=(1+r)^\alpha-1,\quad
\Lambda=\log\!\left(\frac{\delta}{r^\alpha}\right),\quad
\tau=(2b)^\alpha t_\alpha.
\]
Then \(\delta>r^\alpha\), and the positive root has the explicit strict brackets
\[
\boxed{\quad\frac{\Lambda}{1+\delta}<\tau<\Lambda.\quad}
\]
For each *fixed* \(\alpha>1\) and fixed \(b>0\), as \(r\downarrow0\),
\[
\boxed{\quad(2b)^\alpha t_\alpha
=(\alpha-1)\log(1/r)+\log\alpha+o(1),\quad}
\]
while
\[
\boxed{\quad(2b)^\alpha s_\alpha\longrightarrow1,
\qquad\max_{t\geq0}\|K_\alpha(t)\|_{\infty\to\infty}
=1+\frac{\alpha}{2e}r+o(r).\quad}
\]
Thus the duration of the temporary sign loss diverges *logarithmically* as one conductance vanishes, even though its maximum operator-norm excess vanishes *linearly*.

**Near-order-one crossover.** For fixed \(a,b>0\), let
\[
H(a,b)=(a+b)\log(a+b)-a\log a-b\log b>0.
\]
As \(\alpha\downarrow1\) from above,
\[
t_\alpha=\frac{H(a,b)}{2ab}(\alpha-1)+O((\alpha-1)^2),
\]
and
\[
\max_{t\geq0}\|K_\alpha(t)\|_{\infty\to\infty}
=1+\frac{H(a,b)^2}{8ab}(\alpha-1)^2+O((\alpha-1)^3).
\]
If both limits are coupled with \(r\downarrow0\), \(\alpha(r)>1\), \(\alpha(r)\to1\), and \((\alpha(r)-1)\log(1/r)\to\eta\in[0,\infty)\), then the dimensionless positivity-recovery time tends to \(\eta\):
\[
(2b)^{\alpha(r)}t_{\alpha(r)}\longrightarrow\eta.
\]

## Assumptions and scope

The graph has exactly four vertices and two parallel pairs of **positive** conductances. The exponent \(\alpha\) is any positive real number, including values above one (which need not generate a positivity-preserving semigroup for small times). The space is \(\mathbb R^4\), and the operator norm \(\|M\|_{\infty\to\infty}\) is the maximum absolute row sum. It is not the maximum absolute matrix-entry norm. The time \(t=0\) is treated separately. All limiting statements specify which parameters are fixed and which vary. There is no assertion about arbitrary four-cycle weights, larger grids, directed networks, or time-fractional Caputo/Mittag-Leffler evolution.

## Proof

**1. Exact Fourier representation.** Let \(S_1,S_2\) flip the first and second bits. They commute and satisfy \(S_j^2=I\), and
\[
L=a(I-S_1)+b(I-S_2).
\]
The four normalized Boolean characters jointly diagonalize them. Their \(L\)-eigenvalues are \(0,2a,2b,2(a+b)\); hence the four spectral multipliers of \(K_\alpha(t)\) are \(1,x,y,z\), with \(x=e^{-At}\), \(y=e^{-Bt}\), and \(z=e^{-Ct}\). Character inversion gives the four entry types:
\[
\begin{array}{c|c}
\text{pair type}&4K_\alpha(t)_{uv}\\\hline
u=v&1+x+y+z\\
\text{first-coordinate neighbors}&1-x+y-z\\
\text{second-coordinate neighbors}&1+x-y-z\\
\text{opposite corners}&1-x-y+z.
\end{array}
\]
The neighbor values are positive since \(1-x>0\), \(y-z>0\), \(1-y>0\), and \(x-z>0\). Every row sums to one because the constant character has multiplier one.

**2. Order threshold and unique recovery.** For \(0<\alpha\leq1\), scalar subadditivity gives \(C\leq A+B\), so
\[
q(t)\geq 1-e^{-At}-e^{-Bt}+e^{-(A+B)t}
=(1-e^{-At})(1-e^{-Bt})>0
\]
for \(t>0\). For \(\alpha>1\), strict superadditivity gives \(C>A+B\). Now
\[
q'(t)=e^{-Ct}\left(Ae^{(C-A)t}+Be^{(C-B)t}-C\right).
\]
The expression in parentheses is strictly increasing, starts at \(A+B-C<0\), and diverges to infinity. Therefore \(q'\) has exactly one zero \(s_\alpha>0\), and \(q\) decreases then increases. With \(q(0)=0\), \(q(s_\alpha)<0\), and \(q(t)\to1\), there is exactly one positive root \(t_\alpha>s_\alpha\). Since every row has exactly one antipodal position and all other entries are positive, taking absolute row sums gives \(\|K_\alpha(t)\|_{\infty\to\infty}=1+\max\{0,-q(t)\}/2\). The minimum of \(q\) is unique, proving the peak statement.

**3. Global bracket.** Assume \(a\leq b\) and rescale time by \(B=(2b)^\alpha\). The antipodal zero equation becomes
\[
1-e^{-r^\alpha\tau}=e^{-\tau}(1-e^{-\delta\tau}).
\]
Let \(\varphi(u)=(1-e^{-u})/u=\int_0^1e^{-su}\,ds\). This function is strictly decreasing and satisfies \(e^{-u}<\varphi(u)<1\) for \(u>0\). Dividing the zero equation by \(\tau\) and rearranging yields
\[
\tau=\Lambda+\log\!\frac{\varphi(\delta\tau)}{\varphi(r^\alpha\tau)}.
\]
Here \(\delta>r^\alpha\), so the logarithm is negative, proving \(\tau<\Lambda\). It is strictly greater than \(-\delta\tau\), because \(\varphi(\delta\tau)>e^{-\delta\tau}\) and \(\varphi(r^\alpha\tau)<1\). Hence \(\tau>\Lambda/(1+\delta)\).

**4. Weak-edge asymptotics and time/amplitude separation.** At fixed \(\alpha>1\), as \(r\downarrow0\), \(\delta=\alpha r+O(r^2)\) and
\[
\Lambda=(\alpha-1)\log(1/r)+\log\alpha+O(r).
\]
The bracket implies \(0<\Lambda-\tau<\delta\Lambda/(1+\delta)=O(r\log(1/r))=o(1)\). This proves the recovery-time expansion. In dimensionless time \(u=(2b)^\alpha t\), write
\[
Q_r(u)=1-e^{-r^\alpha u}-e^{-u}+e^{-(1+\delta)u}.
\]
On each bounded \(u\)-interval, \(Q_r(u)/r\to-\alpha u e^{-u}\) and \(Q_r'(u)/r\to\alpha e^{-u}(u-1)\), uniformly. For \(\alpha>1\), each derivative has exactly one zero by Step 2; signs at \(u=1\pm\varepsilon\) force the zero to tend to one. Substitution into the first limit gives \(\min Q_r=-\alpha r/e+o(r)\) and the claimed maximum row-sum amplification.

**5. Order-one expansion and coupled crossover.** With \(\varepsilon=\alpha-1\), \(C-A-B=2H(a,b)\varepsilon+O(\varepsilon^2)\). Taylor expansion at \(t=0\), uniform near \(\alpha=1\), gives
\[
\frac{q(t)}t=-(C-A-B)+\frac{C^2-A^2-B^2}{2}t+O(t^2).
\]
At \(\alpha=1\), the coefficient of \(t\) on the right is \(4ab\), strictly positive. The implicit function theorem yields the unique small positive root \(t_\alpha=H(a,b)\varepsilon/(2ab)+O(\varepsilon^2)\). The minimizing time is half the leading root, and inserting it into the quadratic approximation gives \(\min q=-H(a,b)^2\varepsilon^2/(4ab)+O(\varepsilon^3)\), hence the peak norm formula. Finally, for \(r\downarrow0\) and \(\alpha(r)\downarrow1\) with \((\alpha-1)\log(1/r)\to\eta\), the expansion of \(\Lambda\) remains uniform for bounded \(\alpha\); the bracket bounds then squeeze \(\tau\to\eta\).

## Verification

`CHECK.py` is a reproducible Python 3 standard-library supplementary checker. It separately diagonalizes the weighted four-by-four Laplacian by symmetric Jacobi rotations, compares the resulting matrix function with the Boolean-character formulas, tests row sums and neighbor signs, solves scalar peak and recovery equations, and checks the strict bracket and selected asymptotic regimes. Execute `python CHECK.py` from the extracted package directory. The submitted run passed 348 cases. These tests do not replace the analytic proof and do not certify infinite parameter ranges.

## Relationship to prior work

Benzi, Bertaccini, Durastante and Simunec (2019 preprint, published 2020) construct fractional graph dynamics and prove stochasticity and decay properties principally for \(0<\alpha\leq1\). Benzi and Simunec (2020 preprint) study numerical approximation of fractional graph diffusion, again emphasizing powers below one. Their full-text discussions explain the positivity-preserving regime but do not state the present all-order, anisotropic four-cycle root classification or the logarithmic weak-coupling law.

The published published-finding corpus record on complete multipartite networks establishes the order-one positivity boundary and exact profiles on *unweighted* complete multipartite graphs. It includes the equal-weight square as a special case and therefore covers that special case; the unequal positive conductance pairs and the singular \(a/b\to0\) time/amplitude separation are not implied by the record's stated unweighted hypotheses. This distinction is about implications, not different terminology. A separate weighted-triangle classification concerns a different graph with three, rather than four, vertices and does not imply this statement. A published two-timescale result for fourth-order heat on increasingly unbalanced *unweighted* complete bipartite graphs is qualitatively related but varies graph size, not an edge-rate ratio in a fixed four-cycle, and has different asymptotic orders.

## Limitations

Historical originality is qualified: an as-yet-unidentified treatment of weighted Boolean products or exponential-polynomial sign changes might contain equivalent formulas. The relevant published published-finding corpus entry was compared using its available title and summary, not a successfully obtained full record, leaving residual priority risk. This theorem describes a specific two-parameter weighted square, not arbitrary weighted cycles; the critical delay is an idealized finite-network result and not a general prediction for large physical systems. Mathematical correctness here rests on the explicit derivation; computational checks are illustrative. Independent validation has not been performed.

## References

1. M. Benzi, D. Bertaccini, F. Durastante, I. Simunec, *Nonlocal network dynamics via fractional graph Laplacians*, arXiv:1912.07288, first posted 2019-12-16; Journal of Complex Networks 8 (2020), cnaa017. https://arxiv.org/abs/1912.07288
2. M. Benzi, I. Simunec, *Rational Krylov methods for fractional diffusion problems on graphs*, arXiv:2012.08389, first posted 2020-12-15; BIT Numerical Mathematics 62 (2022). https://arxiv.org/abs/2012.08389
3. *A sharp positivity transition for fractional graph heat on complete multipartite networks*, published published-finding corpus record, 2026-10-26, identifier `2026/10/26/SCOPE-a-sharp-positivity-transition-for-fractional-graph-heat-on-compl--8af258cef8b1`.
4. *Two timescales of transient amplification and positivity recovery on unbalanced bipartite graphs*, published published-finding corpus record, 2026-10-26, identifier `2026/10/26/SCOPE-two-timescales-of-transient-amplification-and-positivity-recover--61512629ac2e`.
