# Sharp local stability of the Dirichlet-range Hardy–Littlewood contraction

## Finding
Fix real parameters \(0<\alpha<1\), \(\beta>\alpha\), and \(p>0\); put \(q=p\beta/\alpha\). Define \(\mathcal N_{s,t}(f)\) for analytic \(f\) by
\[
\mathcal N_{s,t}(f)^t=|f(0)|^t+\int_0^1\frac{d}{dr}\left[\frac1{2\pi}\int_0^{2\pi}|f(re^{i\theta})|^t\,d\theta\right](1-r^2)^{s-1}\,dr.
\]
The known sharp contraction is \(\mathcal N_{\beta,q}(f)\le\mathcal N_{\alpha,p}(f)\). For perturbations \(f=1+h\) with \(h(0)=h'(0)=0\), let
\[
\|h\|_{s,2}^2=\sum_{k\ge2}\frac{|h_k|^2}{c_s(k)},\qquad c_s(k)=\frac{(s)_k}{k!},\quad h(z)=\sum_{k\ge2}h_kz^k.
\]
For every \(\eta>0\) there is \(\varepsilon>0\), depending only on \(\alpha,\beta,p,\eta\), such that every bounded analytic \(h\) satisfying \(h(0)=h'(0)=0\) and \(\|h\|_\infty+\|h\|_{\alpha,2}<\varepsilon\) obeys the **sharp transverse local stability inequality**
\[
\mathcal N_{\alpha,p}(1+h)^2-\mathcal N_{\beta,q}(1+h)^2
\ge\left[\frac p2\frac{\beta-\alpha}{\beta+1}-\eta\right]\|h\|_{\alpha,2}^2.
\]
The coefficient \(\frac p2\frac{\beta-\alpha}{\beta+1}\) is optimal as a local limiting constant: no larger coefficient can hold for every sufficiently small transverse perturbation, because \(h(z)=t z^2\), \(t\downarrow0\), attains the limit. The full transverse second-variation operator is diagonal in the monomial basis, with eigenvalues
\[
\lambda_k=\frac p2\left[1-\frac\beta\alpha\frac{c_\alpha(k)}{c_\beta(k)}\right],\quad k\ge2.
\]
They are strictly increasing from \(\lambda_2=\frac p2\frac{\beta-\alpha}{\beta+1}\) toward \(p/2\). The first-order mode has \(\lambda_1=0\), precisely matching the infinitesimal conformal extremizer symmetry. By a local Möbius gauge, the inequality holds transversely to the full nearby conformal extremizer family, not just to the constant representative.

## Assumptions and scope
The domain is the open unit disk, with normalized planar area measure \(dm=dx\,dy/\pi\). Parameters are fixed, not uniformly variable; \(q=p\beta/\alpha\). The function \(h\) is bounded and analytic, and small in both the supremum norm and the Hilbert quantity \(\|h\|_{\alpha,2}\). For \(\eta\) larger than the sharp coefficient the displayed bound is vacuous but remains true; the substantive regime is \(0<\eta<\lambda_2\). This is a local theorem, not an asserted global distance-to-extremizers remainder inequality.

## Proof
**1. Hilbert and integral identities.** The Hardy–Stein identity and Fubini yield, for arbitrary \(s,t>0\),
\[
\mathcal N_{s,t}(f)^t=|f(0)|^t+\frac{t^2}{4}\int_{\mathbb D}|f(z)|^{t-2}|f'(z)|^2\omega_s(|z|^2)\,dm(z),
\quad\omega_s(x)=\int_x^1\frac{(1-u)^{s-1}}u\,du.
\]
The formula is used only when \(f=1+h\) stays away from zero (ensured by \(\|h\|_\infty<1/2\)). With \(h(0)=0\) the case \(t=2\) gives
\[
\int_{\mathbb D}|h'|^2\omega_s(|z|^2)\,dm=\|h\|_{s,2}^2=\sum_{k\ge1}\frac{|h_k|^2}{c_s(k)}.
\]
Both identities and the normalization are in Brevig–Kulikov–Seip–Zlotnikov, Eqs. (2.2) and Lemma 2.2 (arXiv:2510.14333v1).

**2. Uniform quadratic expansion.** If \(\delta=\|h\|_\infty<1/2\), the elementary estimate \(\left||1+h|^{t-2}-1\right|\le C_t\delta\), valid uniformly in the disk for each fixed \(t>0\), gives
\[
\mathcal N_{s,t}(1+h)^t=1+\frac{t^2}{4}\|h\|_{s,2}^2+O_t(\delta\|h\|_{s,2}^2).
\]
Taylor expansion of the positive real power \((1+x)^{2/t}\), with the quadratic remainder bounded for small \(x\), yields
\[
\mathcal N_{s,t}(1+h)^2=1+\frac t2\|h\|_{s,2}^2+O_{s,t}\bigl((\delta+\|h\|_{s,2}^2)\|h\|_{s,2}^2\bigr).
\]
Since \(c_\beta(k)\ge c_\alpha(k)\) for all \(k\) and \(h(0)=0\), the \(\beta\)-Hilbert norm is bounded by the \(\alpha\)-Hilbert norm. Subtraction therefore gives an error uniform over all bounded analytic perturbations:
\[
\mathcal N_{\alpha,p}(1+h)^2-\mathcal N_{\beta,q}(1+h)^2
=\frac p2\left(\|h\|_{\alpha,2}^2-\frac\beta\alpha\|h\|_{\beta,2}^2\right)
+O_{\alpha,\beta,p}\bigl((\|h\|_\infty+\|h\|_{\alpha,2}^2)\|h\|_{\alpha,2}^2\bigr).
\]

**3. Entire spectrum and sharp gap.** The Hilbert coefficient formula transforms the quadratic expression into \(\sum_{k\ge1}\lambda_k|h_k|^2/c_\alpha(k)\). The binomial recurrence gives
\[
\frac{c_\alpha(k+1)/c_\beta(k+1)}{c_\alpha(k)/c_\beta(k)}=\frac{\alpha+k}{\beta+k}<1.
\]
Hence \(\lambda_1=0\), \(\lambda_k\) strictly increases for all positive integers \(k\), and \(\lambda_k\to p/2\) because \(c_\alpha(k)/c_\beta(k)=O(k^{\alpha-\beta})\). At \(k=2\),
\[
\lambda_2=\frac p2\left[1-\frac\beta\alpha\frac{\alpha(\alpha+1)}{\beta(\beta+1)}\right]
=\frac p2\frac{\beta-\alpha}{\beta+1}>0.
\]
For \(h'(0)=0\), only indices \(k\ge2\) remain; choosing \(\varepsilon\) so the uniform remainder coefficient is below \(\eta\) proves the stated inequality. For \(h=t z^2\) the remainder is \(o(t^2)\), proving sharpness.

**4. Symmetry-modulated form.** Write \(\kappa=\alpha/p=\beta/q\), and use the source's common isometry
\[
T_{w,\kappa}f(z)=f\!\left(\frac{w-z}{1-\overline w z}\right)
\frac{(1-|w|^2)^\kappa}{(1-\overline w z)^{2\kappa}}.
\]
The derivative at the origin vanishes exactly when
\[
2\kappa\overline w\,f(w)-(1-|w|^2)f'(w)=0.
\]
For \(f\) sufficiently near the constant \(1\) in the bounded-analytic topology, the real implicit-function theorem gives a unique small solution \(w\) (the derivative in \(w\) at \((w,f)=(0,1)\) is \(w\mapsto2\kappa\overline w\), which is invertible as a real-linear map). Set \(F=T_{w,\kappa}f\) and \(g=F/F(0)=1+h\). Then \(h'(0)=0\). For sufficiently small \(f-1\) in the indicated intersection of norms, \(g-1\) is small in both norms (disk automorphisms act continuously locally on the weighted Hilbert space and the accompanying analytic multipliers remain bounded, as follows directly from the weighted derivative integral with changes of variables and the product rule). The common isometry and homogeneity imply the exact identity
\[
\mathcal N_{\alpha,p}(f)^2-\mathcal N_{\beta,q}(f)^2
=|F(0)|^2\bigl[\mathcal N_{\alpha,p}(g)^2-\mathcal N_{\beta,q}(g)^2\bigr].
\]
Thus the transverse gap applies after normalization to the entire nearby orbit of equality cases. No assertion is made about a uniform lower bound in a larger global space without a small supremum-norm condition.

## Verification
The attached `CHECK.py` computes exact rational binomial coefficient ratios and Hessian eigenvalues over several parameter triples, verifies strict monotonicity, and compares high-precision finite Taylor evaluations for perturbations \(1+t z^k\) against the predicted quadratic coefficients. Its role is to detect normalization/algebra errors; the proof of the infinite-dimensional statement is the preceding analytic argument. The full strength of the remainder uses the explicit uniform integral estimate, not a finite experiment.

## Relationship to prior work
Brevig, Kulikov, Seip and Zlotnikov (arXiv:2510.14333v1, October 16, 2025), Theorems 1.1 and 1.3, establish weighted conformal isometry and the sharp contractive inequality, including equality cases, in the Dirichlet range. Their paper does not state a quantitative remainder transverse to the extremizer orbit, the full monomial Hessian spectrum, or the sharp second-mode gap. These theorems and their Hilbert coefficient formula are essential prerequisites here; the contraction itself is not claimed as new.

Llinares (2024) establishes a related contractive Dirichlet-to-Hardy inclusion in a special parameter range; its main theorem is an inclusion inequality rather than the present two-parameter local coercivity and spectral threshold. Kulikov (2021) proves a coefficient-majorant Hardy–Littlewood estimate in a different fixed Hardy-norm setting. The current statement is not a rewording of either global contraction or first-coefficient sharpness: qualitative equality allows zero spectral curvature along extremizer directions but does not yield a positive, sharp uniform gap on their infinite-dimensional complement.

## Limitations
The result is local near the conformal extremizer manifold and assumes smallness in both a supremum norm and the appropriate Hilbert norm. It proves neither a global deficit estimate nor closeness from an arbitrary small functional deficit, and establishes no compactness for unconstrained near-extremizing sequences. The source paper raises questions about linearity of the Dirichlet-range classes; nothing here resolves those questions. Although checked against close published sources and semantic records, older equivalent local-quantitative results under different terminology cannot be ruled out without independent literature review.

## References
1. O. F. Brevig, A. Kulikov, K. Seip, I. Zlotnikov, *Contractive Hardy–Littlewood inequalities in the Dirichlet range*, arXiv:2510.14333v1 (first posted October 16, 2025), https://arxiv.org/html/2510.14333v1.
2. A. Llinares, *Contractive inequalities between Dirichlet and Hardy spaces*, Revista Matemática Iberoamericana 40 (2024), 389–398, DOI:10.4171/RMI/1418, https://ems.press/journals/rmi/articles/9492290.
3. A. Kulikov, *A contractive Hardy–Littlewood inequality*, Bulletin of the London Mathematical Society 53 (2021), 740–746, DOI:10.1112/blms.12455, https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.12455.
