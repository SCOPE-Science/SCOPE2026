# Universal fixed-gap condensation of rational Hartogs Bergman zeros

## Finding
Fix an integer \(k\ge1\). For every positive integer \(n\) with \(\gcd(n,k)=1\), put \(m=n+k\) and let \(Q_{m,n}\) be the degree-\(2k\) reciprocal polynomial on the oblique Bergman-kernel slice of the rational Hartogs triangle \(\mathbb H_{m/n}\), with the precise normalization defined below. Let
\[
S_k(z)=1+z+\cdots+z^{k-1},\qquad P_k(z)=(z^2+4z+1)S_k(z)^2.
\]
Then, **coefficientwise and locally uniformly on the complex plane**,
\[
\boxed{\frac{6k^2}{m^3}Q_{m,n}(z)=P_k(z)+O_k(m^{-2})\quad(n\to\infty,\ \gcd(n,k)=1).}
\]
The coefficient error is \(O_k(m^{-2})\) simultaneously in all \(2k+1\) coefficients; for fixed \(R>0\), the complex-uniform error on \(|z|\le R\) is \(O_{k,R}(m^{-2})\).

Consequently, for every fixed \(k\), all sufficiently large admissible \(n\) give a polynomial with \(2k\) **simple**, nonzero roots, exactly \(k\) inside the unit disk. Its interior roots have a unique labeling consisting of one **real negative outlier** \(\rho_{n,k}\) and \(k-1\) boundary-bound roots \(z_{n,k,h}\), \(1\le h\le k-1\), satisfying
\[
\boxed{\rho_{n,k}=-2+\sqrt3+O_k(m^{-2}),\qquad
z_{n,k,h}=e^{2\pi ih/k}+O_k(m^{-1}).}
\]
The second family is empty for \(k=1\). Every exterior root is the reciprocal conjugate of one interior root. In particular, the empirical probability measure of the \(k\) interior roots converges weakly to
\[
\boxed{\frac1k\delta_{-2+\sqrt3}+\frac1k\sum_{h=1}^{k-1}\delta_{e^{2\pi i h/k}}.}
\]
The fixed interior limit \(-2+\sqrt3\) is **independent of the gap** \(k\); all the other interior zeros condense at the nontrivial \(k\)-th roots of unity. The results identify the limiting locations, not the full first-order radial constants at those boundary points.

## Assumptions and scope
For \(\gamma=m/n>1\), write
\[
\mathbb H_\gamma=\{(z_1,z_2)\in\mathbb C^2:|z_1|^{\gamma}<|z_2|<1\}.
\]
For \(z,w\in\mathbb H_\gamma\), put \(s=z_1\overline{w_1}\), \(t=z_2\overline{w_2}\). The standard Bergman-kernel formula of Almughrabi and Edholm--Mathew is
\[
K_\gamma(z,w)=\frac{P_{m,n}(s,t)}{m\pi^2(1-t)^2(t^n-s^m)^2},
\]
where \(P_{m,n}\) is the explicit finite polynomial below. Set
\[
Q_{m,n}(z)=z^{1-2n}P_{m,n}(z,z).
\]
This is an ordinary polynomial of degree \(2(m-n)=2k\), despite the displayed Laurent expression. Its roots in \(0<|z|<1\) correspond to zeros of the two-point Bergman kernel along \(s=t=z\). This is the **oblique coordinate-product slice**, not the Hermitian diagonal \(z=w\), on which the Bergman kernel is strictly positive.

The limit is taken with \(k\) fixed and \(n\to\infty\) through integers coprime to \(k\), equivalently \(\gcd(m,n)=1\). The error constants may depend on \(k\). No claim of uniformity in growing \(k\), or classification of the entire two-variable kernel zero set, is made.

## Proof
**1. Exact coefficient identity.** Define the finite triangular weight
\[
D_m(v)=\begin{cases}v+1&0\le v\le m-1,\\2m-1-v&m\le v\le2m-2,\\0&\text{otherwise,}\end{cases}
\quad W_m(a)=(m-|a|)_+.
\]
The known numerator formula is
\[
P_{m,n}(s,t)=\sum_{a=0}^{2m-2}\sum_{b=0}^{2n}
 D_m(a)D_m(mb+na+m+n-1-2mn)s^a t^b.
\]
Making the substitutions \(A=a-m+1\) and \(B=b-n\), extending the finite-support sums by zero, and using \(m=n+k\), gives the exact identity
\[
Q_{m,n}(z)=\sum_{A,B\in\mathbb Z}W_m(A)W_m(nA+mB)z^{k+A+B}.
\]
Thus for every integer \(-k\le j\le k\), the coefficient \(c_{k+j}\) of \(z^{k+j}\) is
\[
\boxed{c_{k+j}=\sum_{A\in\mathbb Z}W_m(A)W_m(mj-kA).}\tag{1}
\]
These sums are finite. The support inequalities \(|A|<m\) and \(|mj-kA|<m\) imply \(|j|<k+1\), so no other exponents occur. Reflection \(A\mapsto-A\) shows \(c_{k+j}=c_{k-j}\). The endpoint coefficients are nonzero, so the reciprocal polynomial has degree exactly \(2k\).

**2. Universal triangular-integral limit.** Put \(h_j(x)=(1-|x|)_+(1-|j-kx|)_+\). Identity (1) becomes
\[
\frac{c_{k+j}}{m^3}=\frac1m\sum_{A\in\mathbb Z}h_j(A/m).
\]
Each \(h_j\) is continuous, compactly supported, piecewise quadratic, and has finitely many breakpoints (at most six) and bounded one-sided derivatives for fixed \(k\). On cells without breakpoints the composite trapezoidal quadrature error is bounded by a constant times \(m^{-3}\) per cell, and on the bounded number of cells meeting breakpoints it is bounded by a constant times \(m^{-2}\) per cell. Since there are \(O(m)\) regular cells, summing yields
\[
\frac1m\sum_Ah_j(A/m)=\int_{\mathbb R}h_j(x)\,dx+O_k(m^{-2}),\tag{2}
\]
uniformly over the finite set \(-k\le j\le k\). This is a **quantitative** quadrature argument, not an inference from numerical coefficient fitting.

The integral is elementary. By symmetry assume \(j\ge0\). For \(1\le j\le k-1\) the second triangular factor is supported on \([(j-1)/k,(j+1)/k]\subset[0,1]\); integrating its symmetric tent against \(1-x\) gives \((k-j)/k^2\). At \(j=k\) the overlap is \([(k-1)/k,1]\) and the integral is \(1/(6k^2)\). At \(j=0\) direct integration on \([-1/k,1/k]\) gives \((3k-1)/(3k^2)\). Hence
\[
6k^2\int h_j(x)\,dx=\begin{cases}
6k-2,&j=0,\\6(k-|j|),&1\le|j|\le k-1,\\1,&|j|=k.
\end{cases}\tag{3}
\]
The coefficient sequence in (3) is exactly that of \((1+4z+z^2)(1+\cdots+z^{k-1})^2\): convolution with \((1,4,1)\) of the triangular coefficients of \(S_k^2\) produces \((1,6,12,\ldots,6(k-1),6k-2,6(k-1),\ldots,12,6,1)\). Equations (2)--(3) prove the asserted polynomial asymptotic.

**3. The unit-circle separation.** We recall an explicit proof of the known strict positivity for these reciprocal polynomials, since counting an interior root requires ruling out a unit-circle root. Let
\[
T_m(u)=\sum_{a\in\mathbb Z}W_m(a)e^{iau}=\left|\sum_{r=0}^{m-1}e^{iru}\right|^2.
\]
For \(z=e^{i\theta}\), inserting the finite Fourier-character indicator of \(V\equiv nA\pmod m\) into the centered sum gives
\[
e^{-ik\theta}Q_{m,n}(e^{i\theta})=
\frac1m\sum_{\ell=0}^{m-1}
T_m\!\left(\frac{k\theta-2\pi n\ell}{m}\right)
T_m\!\left(\frac{\theta+2\pi\ell}{m}\right).\tag{4}
\]
Coprimality \(\gcd(m,n)=1\) and Fourier orthogonality imply that the sum of the first factors equals \(m^2\). If \(\theta\notin2\pi\mathbb Z\), every second factor is at least \(\sin^2(\theta/2)>0\), by the finite geometric-sum identity. Therefore the expression in (4) is at least \(m\sin^2(\theta/2)>0\). At \(\theta\in2\pi\mathbb Z\), (4) equals \(m^3>0\). Thus no root lies on \(|z|=1\), and reciprocal symmetry implies exactly \(k\) roots inside and \(k\) outside, counting multiplicities. This positivity argument is known; it is included to make the subsequent root-count transfer fully justified, not claimed as a separate discovery.

**4. Root condensation and quantitative rates.** The limiting polynomial has the simple real roots \(\alpha=-2+\sqrt3\) and \(\alpha^{-1}=-2-\sqrt3\), together with a **double root** at each nontrivial \(k\)-th root of unity. The quadratic factor is nonzero on the unit circle, while \(S_k\) has simple zeros at exactly those \(k-1\) points. The polynomial error from Step 2 is \(O_{k,R}(m^{-2})\) on every bounded disk. On circles of radius \(C_km^{-2}\) around the two simple roots, the limiting polynomial has modulus bounded below by a fixed multiple of the radius; choosing \(C_k\) large enough permits Rouché's theorem. Each circle therefore contains exactly one perturbed root, with displacement \(O_k(m^{-2})\). The root near \(\alpha\) is real because its small conjugation-symmetric disk contains exactly one root of a real polynomial.

Similarly, on circles of radius \(C_km^{-1}\) centered at each double root, the limiting polynomial has modulus bounded below by a positive multiple of the squared radius. Rouché gives exactly two perturbed roots there. Real reciprocal symmetry pairs every nonunit root \(z\) with \(1/\overline z\), and this pairing fixes each limiting unit point. Because Step 3 forbids unit roots, the two roots near each such point consist of **one inside and one outside**. Together with the two simple-root clusters, these account for all \(2k\) roots. The interior roots are pairwise distinct and, for large \(n\), simple, with the stated location rates. Weak convergence of the empirical root measure follows from the finite root labeling.

## Verification
Run `python3 CHECK.py` with the dependency declared in `requirements.txt`. The checker compares three distinct exact coefficient constructions (centered convolution, the original two-index numerator and a residue-reindexed expression), tests reciprocal symmetry and coefficient positivity, numerically checks the \(O_k(m^{-2})\) coefficient law, and compares full polynomial root clusters in representative cases. At preparation it passed 108530 assertions. All infinite claims are justified by the preceding finite sums, quantitative quadrature, positivity and Rouché arguments; the finite tests are reproducibility checks only.

## Relationship to prior work
Edholm--Mathew (first public 26 May 2025) establish the effective rational Hartogs kernel numerator and reciprocal symmetry, study the small gaps \(k=1,2\), and in Remark 4.18 explicitly identify the special gap-two limit \((z+1)^2(z^2+4z+1)\). Published work on gap three gives a sharper first-order radial constant for that **single gap**. The recent Deng--Fu theorem establishes strict unit-circle positivity for all coprime pairs, but not the fixed-gap all-orders limit polynomial or quantitative universal root condensation proved here. The new claim is the full **arbitrary fixed \(k\)** factorization and resulting one-outlier/\(k-1\)-boundary geometry, with uniform coefficient error and root-location rates; no priority is claimed for the source polynomial, special gaps or unit-circle nonvanishing.

## Limitations
The result does not characterize arbitrary off-slice Bergman zeros. The constants in the error terms depend on \(k\); no uniform double-limit theorem with \(k\to\infty\) is asserted. The \(O_k(m^{-1})\) boundary-root estimates do not give sharp individual radial coefficients. Existing formulas already determine every finite polynomial in principle, so the originality claim concerns the explicit universal **asymptotic** theorem, not an entirely new finite-n kernel representation. Independently verifying publication priority against all specialized literature remains beyond the present review.

## References
1. L. D. Edholm and V. T. Mathew, *Arithmetic properties and zeros of the Bergman kernel on a class of quotient domains*, arXiv:2505.20489, first submitted 26 May 2025; especially Theorem 1.3 and Section 4.
2. G. Deng and Q. Fu, *Bergman Kernel Zeros on Rational Hartogs Triangles*, arXiv:2611.07480, first submitted 5 November 2026; especially Lemma 2.1, Lemma 3.1 and Theorem 1.1.
3. *Cubic-root condensation of diagonal Bergman-kernel zeros in gap-three Hartogs triangles*, published mathematical research record (2026), exact \(k=3\) radial-condensation comparison.
4. R. Almughrabi, *Bergman kernels of two dimensional monomial polyhedra*, Complex Analysis and Operator Theory 17 (2023), article 103.
