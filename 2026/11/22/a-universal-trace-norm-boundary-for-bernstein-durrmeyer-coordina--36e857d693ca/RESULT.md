# A universal trace-norm boundary for Bernstein–Durrmeyer coordinate commutators

## Finding
Let \(M_n\) be the classical unweighted Bernstein–Durrmeyer operator on \(L^2(0,1)\) of polynomial degree \(n\), and let \(X\) be multiplication by the coordinate. For every real \(p>0\), the finite-rank commutator \(C_n=[M_n,X]\) obeys the complete Schatten-power law
\[
\boxed{\displaystyle
\lim_{n\to\infty}n^{(p-1)/2}\sum_{j\ge1}s_j(C_n)^p
=\frac{\Gamma((p+1)/2)^2}{2\sqrt\pi\,\Gamma(1+p/2)\,p^{(p+1)/2}}.}
\]
Here \(s_j\) are the singular values, counted with multiplicity and zero padded. In particular,
\[
\boxed{\displaystyle
\lim_{n\to\infty}\|C_n\|_{\mathcal S_1}=\frac1\pi,\quad
\lim_{n\to\infty}\sqrt n\,\|C_n\|_{\mathcal S_2}^2=\frac{\sqrt\pi}{16\sqrt2},\quad
\lim_{n\to\infty}\sqrt n\,\|C_n\|=\frac1{\sqrt{2e}}.}
\]
Consequently the stable rank has the exact asymptotic
\[
\frac{\|C_n\|_{\mathcal S_2}^2}{\|C_n\|^2}
\sim\frac{e\sqrt\pi}{8\sqrt2}\sqrt n.
\]
The nonvanishing trace norm contrasts with operator-norm convergence to zero, quantifying a growing collection of weak noncommuting spectral modes.

## Assumptions and scope
The complex Hilbert space is \(L^2([0,1],dx)\). For each integer \(n\ge1\), put
\[
b_{n,k}(x)={n\choose k}x^k(1-x)^{n-k},\qquad
(M_nf)(x)=(n+1)\sum_{k=0}^n b_{n,k}(x)\int_0^1 b_{n,k}(t)f(t)\,dt.
\]
Set \((Xf)(x)=xf(x)\) and \(C_n=M_nX-XM_n\). These are bounded operators; \(M_n\) is finite rank, positive and selfadjoint. The Schatten power means \(\|C_n\|_{\mathcal S_p}^p=\sum_js_j(C_n)^p\) even when \(0<p<1\), when it is only a quasi-norm. All limits hold for a fixed \(p>0\) and integer \(n\to\infty\), without uniformity as \(p\) varies or generalization to nonuniform weights.

## Proof
**1. Exact Jacobi matrix.** Let \(L_k(x)=\sqrt{2k+1}\,P_k(2x-1)\), where \(P_k\) is the Legendre polynomial. The classical degree-preservation identity, together with selfadjointness, gives
\[
M_nL_k=\lambda_{n,k}L_k,\qquad
\lambda_{n,k}=\frac{n!(n+1)!}{(n-k)!(n+k+1)!}\quad(0\le k\le n),
\]
with \(\lambda_{n,k}=0\) for \(k\ge n+1\). This eigenvalue formula can also be obtained directly: beta moments show that \(M_n\) maps every degree-\(k\) polynomial to a polynomial of degree at most \(k\), with top coefficient \(n! (n+1)!/((n-k)!(n+k+1)!)\), and selfadjointness forces invariance of its orthogonal degree-one quotients. The normalized three-term recurrence is
\[
XL_k=\beta_kL_{k+1}+\tfrac12L_k+\beta_{k-1}L_{k-1},
\qquad \beta_k=\frac{k+1}{2\sqrt{(2k+1)(2k+3)}},
\]
with \(\beta_{-1}=0\). Therefore \(C_n\) is skew-adjoint, supported on \(\operatorname{span}\{L_0,\ldots,L_{n+1}\}\), and has opposite off-diagonals of modulus
\[
c_{n,k}=\beta_k(\lambda_{n,k}-\lambda_{n,k+1})
=\lambda_{n,k}\frac{(k+1)^2}{(n+k+2)\sqrt{(2k+1)(2k+3)}},\quad0\le k\le n.
\]
Indeed \(\lambda_{n,k+1}/\lambda_{n,k}=(n-k)/(n+k+2)\), including \(k=n\). Multiplication of the Legendre basis by successive complex phases identifies \(i\sqrt n C_n\), up to an overall sign, with a real symmetric zero-diagonal Jacobi matrix \(B_n\) whose positive nearest-neighbor weights are \(a_{n,k}=\sqrt n\,c_{n,k}\). Thus \(s_j(C_n)=s_j(B_n)/\sqrt n\).

**2. Square-root spectral window and uniform tail.** For each finite \(R>0\), uniformly in \(0\le k\le R\sqrt n\),
\[
\lambda_{n,k}=\exp(-k^2/n+o_R(1)),\qquad
 a_{n,k}=\frac{k}{2\sqrt n}\exp(-k^2/n)+o_R(1).
\]
This follows by taking logarithms of the exact product \(\prod_{j=0}^{k-1}(n-j)/(n+j+2)\) and using \(\log(1+u)=u+O(u^2)\) on \(k=O(\sqrt n)\). Hence the continuous profile is
\[
a(t)=\frac{t}{2}e^{-t^2}\qquad(t\ge0).
\]
For all \(0\le k\le n\), the same product and \(\log(1-u)\le-u\) yield
\[
0\le\lambda_{n,k}\le e^{-k(k+1)/(2(n+1))},\qquad
0\le a_{n,k}\le\frac{k+1}{\sqrt n}\,e^{-k(k+1)/(2(n+1))}.
\]
Thus, for every fixed \(p>0\),
\[
\lim_{R\to\infty}\limsup_{n\to\infty}
\frac1{\sqrt n}\sum_{k\ge R\sqrt n}a_{n,k}^p=0.
\]
For \(p\ge1\), the Schatten triangle inequality for the forward and backward weighted shifts bounds the \(p\)-th trace of any tail by \(2^p\sum a_{n,k}^p\); for \(0<p\le1\), trace-power subadditivity bounds it by \(2\sum a_{n,k}^p\). The same tail control therefore applies to the Jacobi matrix after discarding high-frequency weights.

**3. All-Schatten spectral limit.** Fix \(R>0\), restrict the Jacobi matrix to frequencies below \(R\sqrt n\), and divide into consecutive blocks of length \(\ell_n=\lfloor n^{1/4}\rfloor\), discarding the one edge coupling between adjacent blocks. There are \(O(\sqrt n/\ell_n)\) discarded couplings with uniformly bounded norm; their normalized Schatten \(p\)-th mass tends to zero by the same weighted-shift estimate. Over any block, replace each nearest-neighbor weight by \(a(k_0/\sqrt n)\), where \(k_0\) is the starting integer index of that block. By the compact-window approximation in Step 2 and uniform continuity of \(a\) on \([0,R]\), the operator norm of this blockwise replacement error tends to zero, whereas its rank is \(O(\sqrt n)\). Its normalized Schatten power therefore tends to zero. To pass from perturbation bounds to normalized traces for \(p<1\), use the trace-power subadditivity of positive singular-value sums and the corresponding reverse inequality; for \(p\ge1\) use the Schatten triangle inequality and boundedness of the normalized masses.

A constant-weight tridiagonal block of length \(\ell_n\) has eigenvalues \(2a(t)\cos(j\pi/(\ell_n+1))\), \(1\le j\le\ell_n\). The resulting angle Riemann sum, followed by the frequency Riemann sum, gives
\[
\lim_{n\to\infty}\frac1{\sqrt n}\operatorname{tr}|B_n|^p
=\frac1\pi\int_0^\infty\int_0^\pi
|t e^{-t^2}\cos\theta|^p\,d\theta\,dt.
\]
The tail estimate of Step 2 permits \(R\to\infty\). Evaluating the two independent gamma integrals,
\[
\int_0^\infty t^p e^{-pt^2}dt
=\frac{\Gamma((p+1)/2)}{2p^{(p+1)/2}},\qquad
\frac1\pi\int_0^\pi|\cos\theta|^p d\theta
=\frac{\Gamma((p+1)/2)}{\sqrt\pi\Gamma(1+p/2)},
\]
proves the general constant, since \(\operatorname{tr}|B_n|^p=n^{p/2}\|C_n\|_{\mathcal S_p}^p\).

**4. Operator norm and stable rank.** For every Jacobi matrix of nonnegative weights, \(\|B_n\|\le2\max_k a_{n,k}\), and Step 2 makes the upper limit \(2\max_{t\ge0}a(t)=1/\sqrt{2e}\). For the reverse bound choose a growing block of indices centered at \(k\sim\sqrt{n/2}\), with length \(o(\sqrt n)\) but tending to infinity. The restriction of \(B_n\) to the block approaches a constant-weight Toeplitz tridiagonal matrix, whose top eigenvalue approaches \(2a(1/\sqrt2)\). This proves the sharp operator norm. Substituting \(p=1\) and \(p=2\) into the gamma formula gives \(1/\pi\) and \(\sqrt\pi/(16\sqrt2)\), and the stable-rank statement follows by division of those verified norm asymptotics.

## Verification
The standalone `check_durrmeyer_commutator.py` independently evaluates the Hilbert–Schmidt norm through both Legendre spectral weights and a double-beta kernel identity with exact rational arithmetic, checks finite-dimensional Jacobi singular values and confirms the limiting constants numerically at large degrees. Run `python3 check_durrmeyer_commutator.py` with Python's standard library; NumPy and SciPy add optional spectral checks. The checks are finite and do not establish the universal limiting theorem: Steps 2–4 supply the asymptotic proof.

## Relationship to prior work
The Bernstein–Durrmeyer kernel and its Gaussian approximation are studied by Mowzer (2023); the spectral decomposition is classical (Derriennic 1981 and later literature). Abel, Acu, Heilmann and Raşa (2026) study commutativity of Bernstein–Durrmeyer-type operators among themselves and with differential operators, not the coordinate-multiplier commutator. The published multivariate Dirichlet Bernstein–Durrmeyer spectral-power trace result concerns \(\operatorname{tr}(M_n^s)\), not the off-diagonal \([M_n,X]\) singular distribution. The Bernstein–Kantorovich nonnormality defect concerns a different integral operator. General results on locally Toeplitz or generalized locally Toeplitz sequences are related to the block argument, but their standard normalized full-matrix spectral distribution has zero limit here because only \(O(\sqrt n)\) of the \(O(n)\) matrix modes are non-negligible; that ordinary limit does not furnish the present zoomed all-\(p\) coefficients without further analysis. No complete historical-priority guarantee is asserted.

## Limitations
The theorem concerns only the unweighted one-dimensional classical operator and coordinate multiplication, with \(p>0\) fixed and \(n\to\infty\). No fixed-rank singular-value asymptotics, individual eigenvalue counting error, first lower-order corrections, uniform-in-\(p\) bounds, or comparable statement for arbitrary weights are proved. The all-Schatten proof is analytic; finite matrices alone would not justify it. An unindexed historical expression of the same constants or an application of stronger semiclassical trace theorems has not been ruled out, and independent validation has not been performed.

## References
1. M. T. Mowzer, *Convergence in distribution of the Bernstein-Durrmeyer kernel and pointwise convergence of a generalised operator for functions of bounded variation*, arXiv:2303.11061v1 (first posted 20 March 2023), https://arxiv.org/abs/2303.11061.
2. U. Abel, A. M. Acu, M. Heilmann and I. Raşa, *Commutativity for a General Class of Bernstein–Durrmeyer Operators*, Results in Mathematics **81** (2026), article 192, published online 7 October 2026, https://doi.org/10.1007/s00025-026-02740-2.
3. E. E. Berdysheva and K. Jetter, *Multivariate Bernstein–Durrmeyer operators with arbitrary weight functions*, Journal of Approximation Theory **162** (2010), 576–598, https://doi.org/10.1016/j.jat.2009.11.005.
4. E. E. Berdysheva, N. Dyn, E. Farkhi and A. Mokhov, *Metric Approximation of Set-Valued Functions of Bounded Variation by Integral Operators*, Constructive Approximation (2024), https://doi.org/10.1007/s00365-024-09681-5.
5. published-finding corpus mathematical record, *Spectral-power trace cancellation for Dirichlet Bernstein–Durrmeyer operators on simplices*, 18 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-spectral-power-trace-cancellation-for-dirichlet-bernstein-durrme--7bbc01919259.
6. published-finding corpus mathematical record, *A finite nonnormality defect for Bernstein–Kantorovich averaging*, 18 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-finite-nonnormality-defect-for-bernstein-kantorovich-averaging--e37d2aef5162.
