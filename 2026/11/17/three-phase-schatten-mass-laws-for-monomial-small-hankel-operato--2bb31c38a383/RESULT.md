# Three-phase Schatten mass laws for monomial small Hankel operators on weighted Besov spaces

## Finding

The degree-growth singular spectrum of the small Hankel operators from the weighted Hilbert Besov space to its anti-holomorphic copy has **three distinct regimes**, separated by an exact logarithmic Schatten boundary. For every real \(\gamma>1\), every \(a>-1\), every integer \(m\geq0\), and every Schatten exponent \(p>0\), consider the small Hankel operator \(H_m=h_{\overline{z^m}}^a\) specified below. Define
\[
\alpha=\frac{\gamma-1}{2}>0,\qquad \beta=a+1-\alpha,\qquad C_\gamma=2^{-\gamma}\Gamma(\gamma+1),
\]
\[
v_j=2(j+1)^2B(2j+2,\gamma+1),\qquad
A_j=\frac{\Gamma(j+a+2)}{\Gamma(j+1)},\qquad
d_j=A_j\sqrt{\frac{v_j}{C_\gamma}}.
\]
The complete nonzero singular multiset, including multiplicities, is exactly
\[
\boxed{\left\{\sigma_{m,j}=\frac{A_j}{A_m}\sqrt{\frac{v_j}{v_{m-j}}}:0\le j\le m\right\}.}
\]
In particular, \(\operatorname{rank}(H_m)=m+1\), and whenever \(0<y<1\) and \(j_m/m\to y\),
\[
\sigma_{m,j_m}\longrightarrow y^\beta(1-y)^\alpha.
\]
For every fixed \(p>0\), write \(S_p(m)=\sum_{j=0}^m\sigma_{m,j}^p=\|H_m\|_{\mathcal S_p}^p\). The **sharp three-way asymptotic** is
\[
\boxed{
S_p(m)\sim
\begin{cases}
m\, B(1+p\beta,1+p\alpha),&p\beta>-1,\\
m\log m,&p\beta=-1,\\
m^{-p\beta}\displaystyle\sum_{j=0}^\infty d_j^p,&p\beta<-1.
\end{cases}}
\]
The series in the third branch converges. The coefficient of the critical logarithm is exactly one in the normalization specified here.

The **operator-norm transition** is
\[
\boxed{
\|H_m\|\sim
\begin{cases}
\dfrac{\alpha^\alpha\beta^\beta}{(\alpha+\beta)^{\alpha+\beta}},&\beta>0,\\
\sup_{j\ge0}d_j,&\beta=0,\\
m^{-\beta}\max_{j\ge0}d_j,&\beta<0.
\end{cases}}
\]
Here the notation \(X_m\sim c\) in the first two cases means \(X_m\to c\). The supremum when \(\beta=0\) is finite and at least one, and the maximum when \(\beta<0\) is attained at a finite index. For \(\beta>0\), every maximizing input degree satisfies \(j_m/m\to\beta/(\alpha+\beta)\); for \(\beta<0\), all maximizing degrees eventually lie in a fixed finite set. These are sharp bulk/edge transitions, not estimates up to constants.

## Assumptions and scope

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) and \(dA(z)=dx\,dy/\pi\). Work on the analytic Hilbert space \(\mathcal B_\gamma\) with
\[
\|f\|_\gamma^2=\int_{\mathbb D}|(I+z\partial_z)f(z)|^2(1-|z|)^\gamma\,dA(z).
\]
For \(\gamma>1\) this is the one-variable, exponent-two, power-weight instance of the weighted Besov spaces introduced in Li--Wang. Its anti-holomorphic copy is equipped with the conjugate norm. The kernel parameter \(a>-1\) is independent of \(\gamma\). Define
\[
d\nu_a(w)=(a+1)(1-|w|^2)^a dA(w),\quad
K_a(w,z)=(1-w\overline z)^{-a-2},
\]
\[
(H_m f)(z)=\int_{\mathbb D}f(w)\overline{w}^{\,m}K_a(w,z)\,d\nu_a(w)
\]
initially for polynomials and then by its (finite-rank) continuous extension. No restrictive kernel admissibility condition is needed for this monomial-symbol calculation. The familiar condition \(2(a+1)>\gamma-1\), corresponding to \(\beta>0\), is instead required for the general-symbol boundedness theorem in the cited work; the present finite-rank family remains well-defined even at and below that boundary. All limits take \(m\to\infty\), with \(a,\gamma,p\) fixed. The Schatten exponent may be less than one: only sums of powers of singular values are used.

## Proof

**Exact anti-diagonal reduction.** Rotation invariance makes the monomials orthogonal. Direct polar integration yields
\[
\|z^j\|_\gamma^2=2(j+1)^2\int_0^1r^{2j+1}(1-r)^\gamma\,dr=v_j.
\]
Expanding the kernel in its absolutely convergent power series gives
\[
K_a(w,z)=\sum_{\ell\ge0}\frac{\Gamma(\ell+a+2)}{\Gamma(a+2)\Gamma(\ell+1)}w^\ell\overline z^{\,\ell}.
\]
For the input monomial \(w^k\), angular integration forces \(k+\ell=m\). The normalized Bergman moment of \(|w|^{2m}\) equals the reciprocal of the degree-\(m\) kernel coefficient. Consequently
\[
H_m z^k=\begin{cases}
\dfrac{A_{m-k}}{A_m}\overline z^{\,m-k},&0\le k\le m,\\
0,&k>m.
\end{cases}
\]
After dividing input and output monomials by the square roots of their \(v\)-norms, this is an anti-diagonal weighted partial isometry. Its \(m+1\) weights are strictly positive, and their absolute values are precisely the displayed \(\sigma_{m,j}\). This proves finite rank, bounded extension, and the exact singular spectrum independently of any symbol criterion.

**Gamma-ratio control.** The standard gamma-ratio limit, obtained for example by Stirling's formula with a fixed shift, gives
\[
A_j\sim j^{a+1},\qquad v_j\sim C_\gamma j^{-2\alpha},\qquad d_j\sim j^\beta.
\]
For every fixed \(a,\gamma\), two-sided bounds hold with constants independent of nonnegative \(j\):
\[
A_j\asymp(j+1)^{a+1},\qquad v_j\asymp(j+1)^{-2\alpha},\qquad d_j\asymp(j+1)^\beta.
\]
In particular, for \(0\le j\le m\) and \(m\ge1\),
\[
\sigma_{m,j}\lesssim
\left(\frac{j+1}{m}\right)^\beta
\left(\frac{m-j+1}{m}\right)^\alpha.
\]
Here an exponent can be negative, and this estimate uses the actual positive factors with the indicated ratios, not a supposed monotonicity. For \(j_m/m\to y\in(0,1)\), applying the asymptotic equalities to the exact expression proves the bulk profile. For each fixed \(j\), the exact formula gives
\[
\lim_{m\to\infty}m^\beta\sigma_{m,j}=d_j.
\]

**Schatten bulk.** If \(p\beta>-1\), the preceding bound gives an integrable endpoint majorant for the Riemann sums (and \(p\alpha>0\)). Splitting into \(j\le\varepsilon m\), \(\varepsilon m<j<(1-\varepsilon)m\), and \(j\ge(1-\varepsilon)m\) shows that after division by \(m\) the endpoint sums are bounded by constants times \(\varepsilon^{1+p\beta}\) and \(\varepsilon^{1+p\alpha}\), respectively. The middle sum converges to the beta integral. Letting \(\varepsilon\downarrow0\) gives the first branch.

**Critical logarithm.** If \(p\beta=-1\), the fixed-index asymptotics and the regular variation of the gamma ratios imply uniformly as \(J\to\infty\), \(\varepsilon\downarrow0\), and \(J\le j\le\varepsilon m\),
\[
\frac{\sigma_{m,j}^p}{m}\;=\;\frac{1+o(1)+O(\varepsilon)}{j},
\]
where the errors are uniform in such a truncated strip. The strip contributes asymptotically \(m\log m\). The finitely many indices below \(J\) contribute \(O(m)\); the remaining indices \(j>\varepsilon m\) contribute \(O_\varepsilon(m)\), since the bulk profile is bounded on that range and the right edge decreases as a positive power. Division by \(m\log m\) proves coefficient one.

**Boundary-dominated Schatten mass.** If \(p\beta<-1\), the exponent \(\beta\) is negative. The uniform bound simplifies to
\[
(m^\beta\sigma_{m,j})^p\lesssim(j+1)^{p\beta},
\]
which is summable. At each fixed index the summand converges to \(d_j^p\). Dominated convergence for sequences (extending each finite row by zeros) proves \(m^{p\beta}S_p(m)\to\sum_{j\ge0}d_j^p\).

**Maximal singular values.** If \(\beta>0\), the bulk profile extends continuously to \([0,1]\) by zero at both endpoints and is uniquely maximized at \(y=\beta/(\alpha+\beta)\). The endpoint bounds are uniformly negligible, giving the stated constant and maximizing-degree convergence. If \(\beta<0\), the dominated bound \(m^\beta\sigma_{m,j}\lesssim(j+1)^\beta\) forces all maximizers into a finite set and the fixed-index limit yields \(m^\beta\|H_m\|\to\max_jd_j\). At \(\beta=0\), the same splitting into fixed indices, indices with \(j/m\to0\) and bulk indices shows \(\|H_m\|\to\sup_jd_j\); the bulk and diffuse-edge limits do not exceed one, while \(d_j\to1\). No attainment claim is made at \(\beta=0\).

## Verification

The coefficient calculation may be checked from the exact beta moments, without truncating any infinite operator in order to infer its rank. The accompanying `check.py` evaluates both the gamma-ratio singular formula and the predicted moment constants on finite degrees for representative parameter values; it explicitly treats numerical outputs as diagnostics only. The proof above establishes the full infinite-degree limits, and no finite computation certifies novelty or the universal limits. The source weight, Bergman-kernel coefficients, and output normalization are identical to those in Li--Wang equations (1.2) and (1.3), specialized to one variable, exponent two, and \(\omega(t)=t^\gamma\).

## Relationship to prior work

Li and Wang, *Small Hankel Operators on Weighted Besov Spaces over the Polydisc* (arXiv:2611.03901v1, November 2, 2026), characterize boundedness of small Hankel maps using symbol criteria; their main theorem controls norms up to constants under a strict kernel condition. Their full-text introduction and arguments do not give the degree-dependent exact singular multiset, the kernel-boundary crossing, or the three exact Schatten mass coefficients above. This manuscript derives its Hilbert-space and integral conventions directly from their definitions.

Janson's *Hankel operators between weighted Bergman spaces* (1988), and Arazy--Fisher--Peetre's work on Hankel operators on weighted Bergman spaces (1988), provide older operator-ideal theory in related spaces. Those results are not reasserted here as new; the quantitative leading constants for this specific independently weighted Besov monomial family are the stated object of study. The distinction from the big Bergman Hankel operator is essential: its range lies outside the analytic space and its monomial matrix is not this finite anti-diagonal. Analytic (rather than operator-theoretic) equivalence of weighted Besov and weighted Bergman norms also does not transfer *exact* singular-value coefficients.

## Limitations

The result concerns the one-variable Hilbert case, power weights, and a single monomial symbol. It does not assert spectral laws for arbitrary symbols, nonpower weights, or higher-dimensional polydiscs. The strongest novelty risk is a possible older exact monomial formula in weighted small-Hankel literature expressed using equivalent Hilbert coefficient spaces. In particular, the entire full text of Janson's 1988 journal paper was not available for inspection; only its bibliographic summary and citation context could be checked. An independent literature and mathematical audit has not been performed.

## References

1. Chen Li and Kai Wang, *Small Hankel Operators on Weighted Besov Spaces over the Polydisc*, arXiv:2611.03901v1 (first posted November 2, 2026), https://arxiv.org/html/2611.03901v1.
2. Svante Janson, *Hankel operators between weighted Bergman spaces*, Arkiv för Matematik 26 (1988), 205–219, https://doi.org/10.1007/BF02386120.
3. Jonathan Arazy, Stephen D. Fisher and Jaak Peetre, *Hankel operators on weighted Bergman spaces*, American Journal of Mathematics 110 (1988), 989–1053, https://doi.org/10.2307/2374685.
4. Benoit Florent Sehba, *Hankel Operators on Bergman Spaces of Tube Domains over Symmetric Cones*, Integral Equations and Operator Theory 62 (2008), 233–245, https://doi.org/10.1007/s00020-008-1620-7 (subject-classification analogue for 47B35).
