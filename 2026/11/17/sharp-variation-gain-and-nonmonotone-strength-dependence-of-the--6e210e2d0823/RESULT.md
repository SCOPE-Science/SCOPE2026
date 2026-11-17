# Sharp variation gain and nonmonotone strength dependence of the bilateral Hodrick–Prescott smoother

## Finding
Let \(L=2I-S-S^{-1}\) be the positive nearest-neighbor Laplacian on the integer lattice, and let \(T_\lambda=(I+\lambda L^2)^{-1}\) with \(\lambda>0\). On real bounded sequences of finite adjacent total variation, its **exact, attained sharp variation gain** is
\[
\mathcal G(\lambda)=|K_\lambda(0)|+2\sum_{j=1}^{\infty}|K_\lambda(j)|,
\qquad
K_\lambda(j)=\frac1{\sqrt\lambda}\operatorname{Im}\frac{q_\lambda^{|j|+1}}{1-q_\lambda^2},
\]
where \(q_\lambda\) is the unique solution of
\[
q_\lambda+q_\lambda^{-1}=2-\frac{i}{\sqrt\lambda},
\qquad |q_\lambda|<1,\quad \operatorname{Im}q_\lambda>0.
\]
The series is absolutely convergent and admits explicit geometric error bounds. Every one-jump (Heaviside) sequence is an extremizer. Despite its low-pass frequency response, \(\mathcal G(\lambda)>1\) for every \(\lambda>0\), and the sharp gain is **not monotone in smoothing strength**. Certified rational inequalities give
\[
\mathcal G(1/16)>1.088,\qquad \mathcal G(1/9)<1.081.
\]
The weak- and strong-smoothing limits are
\[
\mathcal G(\lambda)=1+4\lambda+O(\lambda^2)\quad(\lambda\downarrow0),
\]
\[
\boxed{\lim_{\lambda\to\infty}\mathcal G(\lambda)=
1+\frac{\sqrt2\,e^{-3\pi/4}}{1-e^{-\pi}}
=1.140093467050976\ldots.}
\]
Furthermore, if \(j_\lambda\) denotes the least nonnegative index with \(K_\lambda(j_\lambda)<0\), then
\[
j_\lambda\sim\frac{3\pi}{2\sqrt2}\lambda^{1/4}
\qquad(\lambda\to\infty).
\]

## Assumptions and scope
The shift is \((Sy)_j=y_{j-1}\), and the domain is the real space
\[
\mathrm{BV}(\mathbb Z)=\left\{y\in\ell^\infty(\mathbb Z):V(y)=\sum_{j\in\mathbb Z}|y_j-y_{j-1}|<\infty\right\}.
\]
The operator is the bounded-convolution extension of the inverse \(I+\lambda L^2\) from \(\ell^2(\mathbb Z)\); this extension preserves constants and has no finite-endpoint boundary convention. The norm is the homogeneous seminorm quotient \(\sup_{V(y)>0}V(T_\lambda y)/V(y)\). The normalization is exactly \(I+\lambda L^2\), not \(I+2\lambda L^2\).

## Proof
**1. Resolvent kernel.** For \(a=\lambda^{-1/2}\), the partial fraction identity
\[
(I+\lambda L^2)^{-1}=\frac{(L-iaI)^{-1}-(L+iaI)^{-1}}{2i\sqrt\lambda}
\]
holds on \(\ell^2\). The decaying Green kernel of \(L-iaI\) is \(q^{|j|+1}/(1-q^2)\), because the recurrence has characteristic equation \(q+q^{-1}=2-ia\) and the jump equation at the origin gives the prefactor. Taking the imaginary part yields the claimed real symmetric kernel. Its geometric decay makes it absolutely summable. Evaluating its Fourier multiplier at zero gives \(\sum_jK_\lambda(j)=1\), and thus convolution preserves constants.

**2. Sharp variation norm.** Write \((Dy)_j=y_j-y_{j-1}\). Since \(D\) commutes with convolution, \(D(T_\lambda y)=K_\lambda*(Dy)\) and Young's inequality gives \(V(T_\lambda y)\le\|K_\lambda\|_{\ell^1}V(y)\). For the bounded Heaviside sequence \(y_j=\mathbf1_{\{j\ge0\}}\), \(Dy=\delta_0\) and equality holds. The displayed series therefore equals the exact sharp coefficient. Truncation after \(j=N\ge0\) incurs at most
\[
\frac{2|q_\lambda|^{N+2}}
{\sqrt\lambda\,|1-q_\lambda^2|(1-|q_\lambda|)}.
\]

**3. Strict amplification and first negative lobe.** From the characteristic equation, \(q_\lambda\) lies in the first quadrant. Put \(\phi=\arg q_\lambda\in(0,\pi/2)\) and \(\delta=\arg(q_\lambda/(1-q_\lambda^2))\in(0,\pi)\). Then \(K_\lambda(j)\) is a positive multiple of \(|q_\lambda|^j\sin(j\phi+\delta)\). Some index has negative sine (choose the first integer after the phase crosses \(\pi\)); consequently \(\|K_\lambda\|_1>\sum_jK_\lambda(j)=1\). Moreover, as \(t=\lambda^{1/4}\to\infty\), \(\phi\sim1/(\sqrt2t)\) and \(\delta\to\pi/4\). The first negative index therefore satisfies the stated asymptotic.

**4. Weak smoothing.** The convolution stencil of \(L^2\) is \((1,-4,6,-4,1)\), with \(\ell^1\)-norm \(16\). For \(0<\lambda<1/16\), the convolution Neumann series proves
\[
K_\lambda=\delta_0-\lambda(\delta_{-2}-4\delta_{-1}+6\delta_0-4\delta_1+\delta_2)+O_{\ell^1}(\lambda^2).
\]
Taking the \(\ell^1\)-norm (accounting for signs at \(0,\pm1,\pm2\)) gives \(1+4\lambda+O(\lambda^2)\).

**5. Strong smoothing.** Set \(t=\lambda^{1/4}\) and \(q_\lambda=e^{-w_\lambda}\) with positive real part of \(w_\lambda\). The identity \(\cosh w_\lambda=1-i/(2t^2)\) implies
\[
w_\lambda=\frac{1-i}{\sqrt2t}+O(t^{-3}).
\]
Uniformly on compact subsets of \(x\ge0\),
\[
tK_\lambda(\lfloor tx\rfloor)\longrightarrow
\kappa(x)=\frac{e^{-x/\sqrt2}}{2\sqrt2}
\left(\cos\frac{x}{\sqrt2}+\sin\frac{x}{\sqrt2}\right).
\]
The exact geometric kernel gives \(|K_\lambda(j)|\le(C/t)e^{-cj/t}\) for all sufficiently large \(t\), with positive absolute constants \(C,c\). Consequently its absolute discrete sum converges to \(\int_{\mathbb R}|\kappa(|x|)|\,dx=\int_0^\infty e^{-u}|\cos u+\sin u|\,du\). The integrand changes sign on \((3\pi/4+2k\pi,7\pi/4+2k\pi)\). Since its signed integral is one, summing the negative intervals using \(\int e^{-u}(\cos u+\sin u)\,du=-e^{-u}\cos u\) gives the claimed closed constant.

**6. Certified nonmonotonicity.** For each rational \(\lambda\in\{1/16,1/9\}\), solve \(Ah=\delta_0\) exactly over the integer indices \(-7,\ldots,7\) with \(h=0\) elsewhere, where \(A=I+\lambda L^2\). Define the finitely supported residual \(r=\delta_0-Ah\) and exact rational sums \(H=\|h\|_1\), \(R=\|r\|_1\). Since \(R<1\), the convolution identity \(h=K_\lambda*(\delta_0-r)\) and the \(\ell^1\)-Neumann inverse yield
\[
\frac{H}{1+R}\le\mathcal G(\lambda)\le\frac{H}{1-R}.
\]
The supplied standalone rational checker verifies, by fraction arithmetic, that the first lower bound exceeds \(136/125=1.088\) and the second upper bound is below \(1081/1000=1.081\). This proves a strict decrease between two increasing smoothing strengths, independent of floating-point numerics.

## Verification
Run `python check.py` (Python standard library only). It reconstructs the two rational finite-section certificates, their full off-domain convolution residuals and both strict inequalities. It separately compares the complex-root kernel against the five-point resolvent recurrence and mass normalization, checks sample finite-variation inequalities and numerically probes the large-parameter limit. The rational certificate proves nonmonotonicity; the analytical arguments prove all-parameter sharpness and limits. The finite tests are not used as substitutes for infinite proofs.

## Relationship to prior work
The lattice filter is the bilateral low-pass Hodrick–Prescott/second-order Whittaker–Henderson smoother. McElroy's 2006 public research report derives exact filter weights, including their geometric decay and signed side lobes; those kernel identities are known and not claimed as new here. The contribution is the exact **variation-operator norm**, single-jump attainment, a certified nonmonotone parameter comparison and the explicit universal strong-smoothing limit. Kim–Koh–Boyd–Gorinevsky (2009) compare a distinct \(\ell^1\)-penalized trend estimator to the quadratic filter; their penalty seminorm is not the variation norm of the quadratic smoother. Other relevant published results concern finite paths, or periodic cycles and eventual positivity, rather than this bi-infinite norm. The novelty conclusion is conditional on the source comparisons, not on failed keyword searches alone.

## Limitations
This theorem is for real signals on the **bi-infinite one-dimensional uniform lattice** with the squared second-difference penalty. It does not address finite-sample endpoint effects, periodization, higher-dimensional lattices, other penalty orders or arbitrary weights. It establishes a continuum limit but not a complete analytic classification of every local extremum of the parameter-dependent norm. Historical priority is not independently certified; some finite-sample sources were available only through abstracts.

## References
1. T. McElroy, *Exact Formulas for the Hodrick–Prescott Filter*, U.S. Census Bureau Research Report RRS2006-09, issued 2006-09-07, https://www.census.gov/library/working-papers/2006/adrm/rrs2006-09.html ; full text https://www.census.gov/content/dam/Census/library/working-papers/2006/adrm/rrs2006-09.pdf .
2. S.-J. Kim, K. Koh, S. Boyd and D. Gorinevsky, *\(\ell_1\) Trend Filtering*, SIAM Review **51** (2009), 339–360, https://web.stanford.edu/~boyd/papers/pdf/l1_trend_filter.pdf .
3. A. Cornea-Madeira, *The Explicit Formula for the Hodrick–Prescott Filter in Finite Sample*, Review of Economics and Statistics **99** (2017), 314–318, https://eprints.whiterose.ac.uk/id/eprint/97954/ .
