# Sharp cubic-gap stability for optimally placed Sobolev mean constraints on a circle

## Finding

Let \(N\ge3\) and \(S>0\). Place \(N\) distinct equally weighted point masses on the unit metric circle, with fixed total atomic mass \(S\), in addition to unit arclength measure. Among all placements, the *unique* minimizers of the sharp squared mean-zero \(H^1\)-to-\(L^\infty\) embedding constant, modulo rotation and relabeling, are the equally spaced configurations. The exact minimum is

\[
\mathcal K_{N,S}^{\min}=\frac1{12}+\frac{S(1+2S)}{12N^2(1+S)^2}.
\]

More strongly, there is an **exact three-term nonnegative deficit identity** for every placement. Let the cyclic gaps be \(g_1,\ldots,g_N>0\), with \(\sum_i g_i=1\); let \(m_i\) be the midpoint of the corresponding open circular gap. Write \(r(t)=\{t\}(1-\{t\})\) for the circle's effective-resistance kernel, \(V(x)=N^{-1}\sum_j r(x-a_j)\), and \(B=\max_xV(x)\). Then

\[
\boxed{\begin{aligned}
\mathcal K(a_1,\ldots,a_N)-\mathcal K_{N,S}^{\min}
={}&\frac{S(1+2S)}{12(1+S)^2}
\sum_i\left(g_i-\frac1N\right)^2\left(g_i+\frac2N\right)\\
&+\frac{S}{1+S}\sum_i g_i\bigl(B-V(m_i)\bigr)
+\frac{S^2}{4(1+S)^2}\sum_i g_i\bigl(V'(m_i)\bigr)^2.
\end{aligned}}
\]

All terms are nonnegative; the first vanishes exactly when all gaps are equal. This also yields the quantitative geometric lower bound obtained by retaining the first term. In an equally spaced configuration the only norm-maximizing evaluation points are the \(N\) gap midpoints; all nonzero equality functions are scalar multiples of their centered Green representers.

## Assumptions and scope

Work on \(\mathbb T=\mathbb R/\mathbb Z\) with ordinary arclength \(dt\), real periodic \(H^1\) functions, and derivative energy \(E(f)=\int_0^1|f'(t)|^2\,dt\). The distinct sites \(a_1,\ldots,a_N\in\mathbb T\) carry identical mass \(S/N\), and the constraint measure and Hilbert space are

\[
\mu=dt+\frac{S}{N}\sum_{j=1}^N\delta_{a_j},\quad M=\mu(\mathbb T)=1+S,\quad
H_\mu=\{f\in H^1_{\rm per}(\mathbb T;\mathbb R):\int f\,d\mu=0\}.
\]

The squared optimal constant is
\[
\mathcal K(a_1,\ldots,a_N)=\sup_{0\ne f\in H_\mu}\frac{\|f\|_\infty^2}{E(f)}.
\]

The gap midpoint and \(V'\) are unambiguous: \(V\) is smooth on each open gap, even when that gap wraps around the chosen coordinate origin. The atomic constraint is not a penalty term in the energy. The result concerns all \(N\ge3\) and real \(S>0\), with no asymptotic or smallness assumption.

## Proof

**1. Green diagonal and the physical normalization.** For \(x,y\in\mathbb T\), the effective resistance is \(r(x-y)=\{x-y\}(1-\{x-y\})\). The periodic distribution identity is \(r''=2\delta_0-2dt\). On the mean-zero derivative-energy Hilbert space, the squared norm of evaluation at \(x\) is the centered Green diagonal
\[
K_\mu(x)=\frac1M\int r(x-y)\,d\mu(y)
-\frac1{2M^2}\iint r(y-z)\,d\mu(y)d\mu(z).
\]
Indeed, with \(\eta_x=\delta_x-\mu/M\), its evaluation representer is the unique periodic energy-class solution of \(-G_x''=\eta_x\) with \(\int G_x\,d\mu=0\), and \(E(G_x)=G_x(x)=-\frac12\iint r(u-v)d\eta_x(u)d\eta_x(v)\). Since \(\int_0^1r(t-y)\,dt=1/6\), setting \(\nu=N^{-1}\sum_j\delta_{a_j}\) and \(W=\iint r(y-z)d\nu(y)d\nu(z)\) yields the exact formula
\[
K_\mu(x)=\frac1{12M^2}+\frac S M V(x)-\frac{S^2}{2M^2}W.
\]
The last term is independent of \(x\). Hence the sharp constant is the right side with \(V(x)\) replaced by \(B=\max_xV(x)\), and norming points are precisely the maximizers of \(V\).

**2. Exact gap quadrature.** Since \(V''=2\nu-2dt\), one has \(V''=-2\) on every open gap. For any midpoint \(m_i\) and all \(t\) in its lifted gap,
\[
V(t)=V(m_i)+V'(m_i)(t-m_i)-(t-m_i)^2.
\]
Writing \(Q=\sum_i g_i^3\) and integrating each quadratic gives
\[
\int_0^1V(t)dt=\sum_i g_iV(m_i)-\frac Q{12}=\frac16,
\quad B-\frac16=\frac Q{12}+\sum_i g_i(B-V(m_i)).
\]
Every summand in the final sum is nonnegative.

**3. Exact self-interaction identity.** Integration by parts for the continuous piecewise-smooth \(V\) gives
\[
W-\frac16=\int V\,d(\nu-dt)=\frac12\langle V,V''\rangle=-\frac12\int_0^1|V'|^2dt.
\]
On each gap, \(V'(t)=V'(m_i)-2(t-m_i)\), and therefore
\[
\int_0^1|V'|^2dt=\sum_i\left(g_i(V'(m_i))^2+\frac{g_i^3}{3}\right),
\qquad W=\frac16-\frac Q6-\frac12\sum_i g_i(V'(m_i))^2.
\]
No Fourier truncation or approximation is used.

**4. Assemble and sharpen.** Substituting the two preceding identities into the Green diagonal yields the exact, all-placements formula
\[
\mathcal K=\frac1{12}+\frac{S(1+2S)}{12M^2}Q
+\frac SM\sum_i g_i(B-V(m_i))
+\frac{S^2}{4M^2}\sum_i g_i(V'(m_i))^2.
\]
The strict convexity of \(t\mapsto t^3\), \(\sum_i g_i=1\), implies \(Q\ge N^{-2}\), with equality only if all \(g_i=N^{-1}\). In the equally spaced configuration, rotation symmetry and strict concavity of each gap profile imply \(V'(m_i)=0\) and \(V(m_i)=B\) for all \(i\), so every nonnegative remainder vanishes. Finally the elementary *exact* identity
\[
Q-\frac1{N^2}=\sum_i\left(g_i-\frac1N\right)^2\left(g_i+\frac2N\right)
\]
produces the asserted three-term deficit. All equality cases are now forced by the positive first term, and the centered Riesz representer argument proves the claimed functions.

For example, when \(N=3\), \(S=1\), and the three cyclic gaps are \((1/2,1/4,1/4)\), direct substitution gives \(\mathcal K=31/288\), whereas the equal-gap optimum is \(13/144\). The strictly positive excess is exactly \(5/288\).

## Verification

Execute `python3 check_circle.py` with standard Python. It performs 441 exact-rational configurations, covering \(2\le N\le8\), several atomic masses, all equally spaced cases and 20 randomized nonuniform gap patterns per parameter pair. A *separate* variational calculation integrates the squared derivative of the centered evaluation representer directly between sites and an evaluation location, rather than applying the resistance identity. All 4,410 such point evaluations are checked exactly as rational numbers. The finite checker corroborates but does not replace the foregoing universal proof.

## Relationship to prior work

Solomyak's arXiv:math/0206235 (June 23, 2002), Theorems 1.1 and 1.2, develops sharp graph-wide approximation bounds for Sobolev functions; it does not give this placement-dependent mean-zero point-evaluation problem. Baker and Faber's arXiv:math/0407428 (July 25, 2004), Section 6, establishes the electrical resistance and Green-function machinery used in Step 1. These basic identities are **prior inputs**, not asserted as new.

Hardin, Kendall and Saff's arXiv:1208.5261 (August 26, 2012), Theorem 1, already implies that equal spacing minimizes the *isolated* maximum \(B=\max V\): take its convex decreasing potential to be a constant minus \(r\). This polarization fact and the classical optimum for pairwise resistance energy must not be counted as new. The distinct claim here is the exact sharp centered-Sobolev constant and its all-configurations **three-term positive stability identity** with explicit cubic gap penalty and complete equality classification for the joint functional involving both \(B\) and \(W\). Santin's arXiv:2210.15959 (October 28, 2022), Theorem 5, treats Brownian-bridge *interpolation power functions* with Dirichlet endpoint conditions, not an atomic-mean constraint on a periodic circle.

## Limitations

This result applies to equal positive atomic masses plus uniform arclength and periodic derivative energy. It does not establish optimal site placement for unequal atomic masses, nonuniform background densities, higher Sobolev orders, nonperiodic domains, or other metric graphs. The equal-spacing property alone is covered by known circle polarization principles; the scientific scope of the contribution is the quantitatively exact centered-Sobolev identity, sharp constant and extremizer class. Priority relative to unindexed work on quadrature design and periodic reproducing-kernel discrepancy remains a bibliographic risk.

## References

- M. Solomyak, *On approximation of functions from Sobolev spaces on metric graphs*, first public arXiv version June 23, 2002, arXiv:math/0206235, https://arxiv.org/abs/math/0206235.
- M. Baker and X. Faber, *Metrized graphs, electrical networks, and Fourier analysis*, first public arXiv version July 25, 2004, arXiv:math/0407428, https://arxiv.org/abs/math/0407428.
- D. P. Hardin, A. P. Kendall and E. B. Saff, *Polarization optimality of equally spaced points on the circle for discrete potentials*, first public arXiv version August 26, 2012, arXiv:1208.5261, https://arxiv.org/abs/1208.5261.
- G. Santin, *Equally spaced points are optimal for Brownian Bridge kernel interpolation*, first public arXiv version October 28, 2022, arXiv:2210.15959, https://arxiv.org/abs/2210.15959.
