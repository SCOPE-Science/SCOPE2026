# Two real critical-point orbits of weighted annular Szegő kernels and a disappearing-hole phase law

## Finding
Fix a real nome \(0<Q<1\) and a weight parameter \(t>0\). On the annulus \(\mathbb A_{\sqrt Q}=\{z\in\mathbb C:\sqrt Q<|z|<1\}\), consider the weighted Szegő reproducing kernel
\[
S_{Q,t}(z,w)=F_{Q,t}(z\overline w),\qquad
F_{Q,t}(s)=\sum_{n\in\mathbb Z}\frac{s^n}{1+tQ^n},\quad Q<|s|<1.
\]

**Critical-point orbit theorem.** The derivative \(F'_{Q,t}\) has precisely two simple zero orbits under multiplication of its argument by integral powers of \(Q\). One orbit is positive real and the other negative real. In particular there is exactly one positive zero \(p_{Q,t}\in(Q,1)\). There is exactly one negative zero representative modulo \(Q^\mathbb Z\), which may lie at \(-Q\) (equivalently at \(-1\)) and then belongs to the boundary, rather than the open fundamental annulus. Every zero of \(F'_{Q,t}\) lies on one of these two real orbits. There are no nonreal derivative zeros on \(\mathbb C^\times\).

**Shrinking-hole law.** As \(Q\downarrow0\) with \(t>0\) fixed, the positive and negative roots lying in \(Q<|s|<1\) satisfy
\[
s_\pm(Q,t)=\pm\sqrt{Q/t}+\frac{t-1}{t}Q+O_t(Q^{3/2}).
\]
For any fixed \(a\in\mathbb D\setminus\{0\}\), let \(N_{Q,t}(a)\) denote the number of zeros of \(\partial_z S_{Q,t}(z,a)\) within \(\mathbb A_{\sqrt Q}\), counted with multiplicity. For all sufficiently small \(Q\), this number is exactly
\[
N_{Q,t}(a)=
\begin{cases}
2,&t|a|^2<1,\\
1,&t|a|^2=1,\\
0,&t|a|^2>1.
\end{cases}
\]
The middle case is possible for \(a\in\mathbb D\) only when \(t>1\). All stationary points are simple and lie on the diameter through \(a\); their signed locations, when present, are \(z=s_\pm(Q,t)/\overline a\).

## Assumptions and scope
The nome \(Q\) is the square of the annulus's inner radius; thus the physical domain is \(\sqrt Q<|z|<1\), whereas the scalar product variable \(s=z\overline w\) lies in \(Q<|s|<1\). The weight \(t\) is arbitrary and positive. The kernel normalization may be multiplied by any strictly positive scalar without changing its critical points. The derivative is the ordinary holomorphic derivative with respect to the first argument, with the second argument fixed. The theorem concerns stationary points of the kernel, **not** zeros of the kernel itself, and makes no assertion about stationary points after nonlinear conformal changes of coordinate.

The statement about the global zero set of \(F'_{Q,t}\) refers to its meromorphic continuation to \(\mathbb C^\times\). Multiplication by \(Q\) maps each orbit onto itself but need not preserve the physical scalar-product annulus. The equality case in the shrinking-hole trichotomy assumes the basepoint \(a\) and \(t\) stay fixed as \(Q\to0\).

## Proof
**1. Convergent Laurent series and the established theta identity.** The series for \(F_{Q,t}\), and all of its derivatives, converge absolutely and locally uniformly on \(Q<|s|<1\): positive indices are controlled by \(|s|^n\), while negative indices are controlled by \((Q/|s|)^{|n|}/t\). Write
\[
\Theta(s;Q)=\prod_{j\ge0}(1-sQ^j)(1-Q^{j+1}/s).
\]
The classical Ramanujan bilateral summation, in the normalization used by Katori--Shirai, gives the meromorphic identity
\[
F_{Q,t}(s)=C_{Q,t}\frac{\Theta(-ts;Q)}{\Theta(s;Q)},\qquad
C_{Q,t}=\frac{\prod_{j\ge1}(1-Q^j)^2}{\Theta(-t;Q)}>0.
\]
Here \(\Theta(Qu;Q)=-\Theta(u;Q)/u\) and \(\Theta(u;Q)\) has simple zeros precisely at \(u=Q^k\), \(k\in\mathbb Z\). Consequently
\[
F_{Q,t}(Qs)=-t^{-1}F_{Q,t}(s),\qquad
F'_{Q,t}(Qs)=-(tQ)^{-1}F'_{Q,t}(s).
\]
The poles of \(F_{Q,t}\) are precisely the simple poles at positive \(Q^k\): no cancellation occurs, since \(-tQ^k<0\) cannot be a theta zero. Therefore \(F'_{Q,t}\) has precisely double poles at those points, and no other poles on \(\mathbb C^\times\).

**2. Exactly two derivative zeros per multiplicative period.** Choose \(R\) with \(1<R<Q^{-1}\) so that neither boundary circle of \(Q R<|s|<R\) meets a zero of \(F'_{Q,t}\). Such radii exist because zeros are isolated. This annulus contains exactly one pole, a double pole at \(s=1\). Parameterize its two circular boundaries by \(Re^{i\phi}\) and \(QRe^{i\phi}\). The quasi-periodicity in step 1 says that their \(F'\)-images differ only by a fixed nonzero scalar. Their winding numbers about zero agree. By the argument principle the zero count minus the pole count is therefore zero, and \(F'_{Q,t}\) has **exactly two zeros counted with multiplicities** in this annulus. Every nonzero point has one representative in each open multiplicative fundamental annulus, except for a possible boundary representative; hence there are exactly two zero orbits counted with multiplicity.

**3. Reality, signs, and simplicity.** For real \(x\in(Q,1)\), termwise differentiation yields
\[
F''_{Q,t}(x)=\sum_{n\in\mathbb Z}\frac{n(n-1)x^{n-2}}{1+tQ^n}>0,
\]
because every summand is nonnegative and those with \(n=2\) and \(n=-1\) are strictly positive. Moreover \(F'_{Q,t}(x)\to-\infty\) as \(x\downarrow Q\), from the negative-index tail, and \(F'_{Q,t}(x)\to+\infty\) as \(x\uparrow1\), from the positive-index tail. Thus \(F'_{Q,t}\) has exactly one positive zero in \((Q,1)\), and it is simple. Quasi-periodicity makes this the only positive orbit. Since all Laurent coefficients are real, zeros are invariant under complex conjugation. A nonreal second zero would force a separate conjugate zero, exceeding the two-orbit count in step 2. The remaining zero orbit is therefore real and not positive, hence negative. Since the first orbit uses multiplicity one, the second orbit is also simple. This excludes every nonreal critical point.

**4. Uniform scaled expansion and both critical roots.** Fix \(t>0\). Set \(s=\sqrt Q\,u\) with \(u\) in a compact subset of \(\mathbb C^\times\). In the derivative series isolate the terms with indices \(1,-1,2,-2\). The first pair gives \(1-1/(tu^2)+O_t(Q)\); the second gives \(2\sqrt Q\,(u-1/(tu^3))+O_t(Q^{3/2})\). The combined tails with indices at least \(3\) or at most \(-3\) are \(O_t(Q)\), uniformly on the compact set, by geometric estimates for the positive and negative tails. Therefore
\[
F'_{Q,t}(\sqrt Q\,u)=1-\frac1{tu^2}
 +2\sqrt Q\left(u-\frac1{tu^3}\right)+O_t(Q).
\]
The limiting expression has two distinct simple zeros \(u=\pm t^{-1/2}\). Rouché's theorem on disjoint small disks around them and the holomorphic implicit-function expansion yield two simple roots satisfying
\[
u_\pm=\pm t^{-1/2}+\frac{t-1}{t}\sqrt Q+O_t(Q).
\]
Here the coefficient is obtained by dividing minus the first-order perturbation \(2(u-1/(tu^3))\) by the derivative \(2/(tu^3)\) at each limiting zero. Multiplication by \(\sqrt Q\) gives the asserted root expansion. For sufficiently small \(Q\), both roots lie in \(Q<|s|<1\), and step 3 proves they are all the derivative zeros there.

**5. Exact eventual physical stationary-point count.** For fixed \(a\ne0\), \(\partial_zS_{Q,t}(z,a)=\overline a\,F'_{Q,t}(z\overline a)\). The relevant product variable must satisfy \(\sqrt Q|a|<|s|<|a|\). Both derivative zeros from step 4 eventually satisfy the upper inequality. Their leading modulus is \(\sqrt Q/\sqrt t\). If \(t|a|^2<1\), both exceed the lower threshold for all sufficiently small \(Q\); if \(t|a|^2>1\), neither does. On equality, \(|a|=t^{-1/2}<1\) forces \(t>1\), and the sharper second term gives
\[
|s_+|=\frac{\sqrt Q}{\sqrt t}+\frac{t-1}{t}Q+O_t(Q^{3/2}),\qquad
|s_-|=\frac{\sqrt Q}{\sqrt t}-\frac{t-1}{t}Q+O_t(Q^{3/2}).
\]
Thus exactly the positive-aligned critical point lies in the annulus. Simplicity and collinearity were already established.

## Verification
The accompanying standalone script `check_stationary.py` evaluates the Jacobi product representation at specified complex points, checks the multiplicative quasi-periodicity of the quotient and its derivative, and reconstructs the two real derivative roots at two small nomes. It tests the three physical count regimes for \(t=4\) and fixed basepoint moduli \(0.4\), \(0.5\), and \(0.6\). It is a finite corroboration only: the two-orbit count and every asymptotic quantifier are proved analytically above, not inferred from the script.

## Relationship to prior work
Katori and Shirai (2020 preprint; 2022 journal) provide the weighted annular Szegő kernel, its theta quotient, and theta-function identities. Gafai, Murid, and Wahid (2022) establish another Ramanujan product representation and analyze zeros of the *kernel*. Their published formula is starting material here; no new summation identity or prior kernel-zero formula is claimed. The 2023 conformal-mapping study by Gafai and colleagues addresses kernel zeros in other doubly connected regions, rather than the derivative-zero classification at issue.

The new result instead counts **all holomorphic critical points** of a weighted annular kernel modulo the annular deck transformation, shows that both critical-point orbits are real and simple for every positive parameter, and derives a sharp zero/two/one stationary-point phase law for the shrinking-hole family. These conclusions need the additional divisor argument, real convexity, and perturbative asymptotic analysis; the previously published product identities alone do not state this classification.

## Limitations
The two-orbit theorem applies to a specific Laurent-series weighted Szegő family, not to arbitrary annular radial weights or doubly connected domains. The physical classification is eventually exact for each **fixed** basepoint and weight; no uniform threshold in parameters approaching the equality boundary is asserted. No effective quantitative value of the sufficiently-small threshold is claimed. At fixed nome, the negative critical orbit can lie on the boundary of the canonical scalar-product fundamental annulus, which is why the orbit statement does not unconditionally claim two critical points in that open annulus. The proof imports the classical theta-product identity and its elementary zero and quasi-periodicity facts, and does not claim those as new.

## References
1. M. Katori and T. Shirai, *Zeros of the i.i.d. Gaussian Laurent series on an annulus: weighted Szegő kernels and permanental-determinantal point processes*, arXiv:2008.04177 (first public version 2020-08-10), *Communications in Mathematical Physics* 392 (2022), 1099–1151. https://arxiv.org/abs/2008.04177 ; https://doi.org/10.1007/s00220-022-04365-2 . In particular, the kernel formula (1.4), theta quotient (1.6), and theta identities (2.11)–(2.14).
2. N. S. Gafai, A. H. M. Murid, and N. H. A. A. Wahid, *Infinite Product Representation for the Szegö Kernel for an Annulus*, arXiv:2202.09114 (first public version 2022-02-18), *Journal of Function Spaces* (2022), article 3763450. https://arxiv.org/abs/2202.09114 . Sections 3 and 5 on the unweighted and weighted product formulas.
3. N. S. Gafai, A. H. M. Murid, S. Naqos, and N. H. A. A. Wahid, *Computing the zeros of the Szegö kernel for doubly connected regions using conformal mapping*, *AIMS Mathematics* 8 (2023), 12040–12061. https://doi.org/10.3934/math.2023607 . Background comparison for kernel-zero problems.
