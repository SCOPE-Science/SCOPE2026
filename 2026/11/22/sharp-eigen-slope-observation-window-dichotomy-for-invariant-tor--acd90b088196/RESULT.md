# Sharp eigen-slope observation-window dichotomy for invariant toral measures

## Finding
Let \(M\in\mathrm{GL}(2,\mathbb Z)\) be hyperbolic on \(\mathbb T^2\), with expanding eigenvalue of absolute value \(e^\chi>1\). For nonzero integer \(v\), let \(L(v)=\log|\alpha_+(v)/\alpha_-(v)|\), where \(\alpha_\pm\) are linear eigencoordinates of \(M^\top\) with eigenvectors fixed once and for all. Fix a closed interval \(I=[a,b]\subset\mathbb R\). For each primitive integral \(v\) with \(L(v)\in I\), observe the entire law of the circle-valued projection \(\pi_v(z)=\langle v,z\rangle\pmod1\). Within the \(M\)-invariant Borel probabilities, these laws all being Haar determine the torus Haar measure **if and only if**
\[
 b-a\ge2\chi.
\]
For every narrower window, there exists a probability \(\mu\perp m_{\mathbb T^2}\), invariant under \(M\), for which every requested projection is Haar. Thus the threshold is sharp and equality belongs to the rigidity side for closed observation windows.

## Assumptions and scope
An integer matrix is *hyperbolic* here when neither eigenvalue has modulus one; invertibility over \(\mathbb Z\) forces eigenvalue absolute values \(e^{\pm\chi}\). Its eigendirections are irrational, so both eigencoordinates of every nonzero lattice vector are nonzero. Choose real eigenvectors of \(M^\top\), and let \(\alpha_+,\alpha_-\) denote expansion coefficients in that basis. A change of eigenvector normalization adds a constant to \(L\) and translates \(I\), leaving its length and theorem invariant. A lattice vector is primitive when the gcd of its coordinates is one, up to sign. A uniform observation means \((\pi_v)_*\mu=m_{\mathbb T}\), equivalently \(\widehat\mu(\ell v)=0\) for all nonzero integers \(\ell\). The theorem quantifies over **all** such primitive \(v\) in the closed observation window, not over a finite sample. The invariant probability need not be ergodic.

## Proof
**1. Orbit geometry and rigidity.** For all \(k\ne0\),
\[
 L((M^\top)^j k)=L(k)+2j\chi,\qquad j\in\mathbb Z.
\]
Multiplication by a nonzero scalar does not change \(L\). Suppose \(b-a\ge2\chi\). Every arithmetic progression \(L(k)+2\chi\mathbb Z\) intersects \([a,b]\). Thus for each nonzero integer \(k\) there exists \(j\in\mathbb Z\) with \(L((M^\top)^j k)\in I\). Write \((M^\top)^j k=\ell v\) with primitive \(v\). The uniform law of \(\pi_v\) forces \(\widehat\mu((M^\top)^j k)=0\). Invariance makes this Fourier coefficient equal \(\widehat\mu(k)\), hence every nonzero coefficient vanishes; uniqueness of Fourier transforms on the torus gives \(\mu=m_{\mathbb T^2}\). Since \(I\) is *closed*, equality of window length to \(2\chi\) suffices.

**2. The gap and lacunary frequencies.** Assume \(b-a<2\chi\). On \(\mathbb R/(2\chi\mathbb Z)\), the image of \(I\) is a proper closed arc. Since rational lattice directions are dense in the real projective line and \(L\) ranges continuously and surjectively over \(\mathbb R\) away from the two eigenlines, choose \(w_0\in\mathbb Z^2\setminus\{0\}\) so that its residue \(L(w_0)\bmod 2\chi\) has positive circular distance \(d\) from that arc. Choose an **even** integer \(p>0\), sufficiently large that \(\beta=e^{p\chi}>3\) and
\[
 \eta=\log\frac{\beta}{\beta-2}<d.
\]
Let \(w_j=(M^\top)^{pj}w_0\) for all \(j\in\mathbb Z\). For a finitely supported word \(\delta_j\in\{-1,0,1\}\), put \(k=\sum_j\delta_j w_j\). If the word is nonzero, let \(J_+\) and \(J_-\) be its largest and smallest nonzero indices. The expanding coordinate of \(k\) has modulus \(r_+\beta^{J_+}|\alpha_+(w_0)|\); the contracting coordinate has modulus \(r_-\beta^{-J_-}|\alpha_-(w_0)|\), where
\[
 \frac{\beta-2}{\beta-1}\le r_+,r_-\le\frac{\beta}{\beta-1}.
\]
These estimates follow from the geometric sum of the smaller indices. In particular \(k\ne0\) and
\[
 |L(k)-L(w_0)-p\chi(J_++J_-)|\le\eta.
\]
Because \(p\) is even, every nonzero such \(k\) has circular distance at most \(\eta\) from \(L(w_0)\) modulo \(2\chi\), and therefore \(L(k)\notin I\). The same largest-index estimate with coefficients in \([-2,2]\) proves uniqueness of signed digit expansions: if their difference were zero, its expanding coordinate would have modulus at least \(|\alpha_+(w_0)|\beta^J(\beta-3)/(\beta-1)>0\).

**3. Invariant singular measure.** Fix \(0<q<1/2\). Form nonnegative trigonometric polynomials
\[
 R_N(z)=\prod_{j=-N}^N\big(1+2q\cos(2\pi\langle w_j,z\rangle)\big).
\]
The uniqueness of expansions proves \(\int R_N\,dm_{\mathbb T^2}=1\) and that \(R_Nm_{\mathbb T^2}\) weakly converges to a probability \(\rho\) whose Fourier coefficients are \(q^{\sum_j|\delta_j|}\) on finitely supported signed-digit sums and zero elsewhere. Index shift gives \((M^p)_*\rho=\rho\). Step 2 shows \(\widehat\rho(k)=0\) whenever \(L(k)\in I+2\chi\mathbb Z\). Define
\[
 \mu=\frac1p\sum_{j=0}^{p-1}(M^j)_*\rho.
\]
Then \(M_*\mu=\mu\), and the Fourier support of every term remains outside \(I\) because \(M^\top\) adds \(2\chi\) to \(L\). Consequently \(\widehat\mu(\ell v)=0\) for each specified primitive \(v\) and integer \(\ell\ne0\), so all requested projections are Haar.

For completeness, let \(C_N=N^{-1}\sum_{j=0}^{N-1}\cos(2\pi\langle w_j,z\rangle)\). Under \(\rho\), its mean is \(q\) and distinct summands are uncorrelated, giving variance at most \(1/N\). Under torus Haar its mean is zero and variance \(1/(2N)\). Chebyshev and Borel–Cantelli along \(N=2^r\) give almost-sure limits \(q\) and \(0\), respectively, hence \(\rho\perp m_{\mathbb T^2}\). Since \(M\) preserves Haar, every translate \((M^j)_*\rho\) and their finite mixture \(\mu\) are singular. Also \(\widehat\mu(w_0)\ge q/p>0\), so the measure is not Haar. This completes both directions.

## Verification
The argument is an infinite Fourier proof; finite tests alone are not relied upon. For \(M=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)\) one has \(\chi=\log((3+\sqrt5)/2)\). The elementary checker `verify.py` tests the frequency-gap, signed-digit uniqueness, and interval-avoidance inequalities on explicitly bounded digit words for \(I=[0,\chi]\) using \(w_0=(1,3)\) and even \(p=4\). The full theorem rests on geometric-series bounds, torus Fourier uniqueness, and the Borel–Cantelli argument, not enumeration.

## Relationship to prior work
Xiaolong Han, *Invariant measures with uniform projection on surfaces and billiards* (first posted 13 November 2026), Appendix A, constructs a singular invariant probability for every hyperbolic integral \(2\times2\) toral automorphism with **one fixed coordinate marginal** Haar. The present theorem uses Han's signed-digit Riesz-product method and geometric inequalities, fully credited, but changes the question to **all primitive integer circle observables in an entire eigen-slope window** and proves the complete sharp observation-width dichotomy, including the closed endpoint. Fan–Schmidt–Verbitskiy (2021/2024) examine Riesz products for Bohr chaoticity of algebraic actions, not this directional observation threshold. The new statement is not a claim of a new general Riesz-product technique. No inspection establishes exhaustive global historical priority.

## Limitations
This is for \(2\)-dimensional hyperbolic **integral automorphisms**, closed intervals in the logarithmic eigenslope coordinate, and circle-valued group-homomorphism projections. It is not a theorem for arbitrary physical Euclidean line projections, higher-dimensional maps, open-window endpoint conventions, or ergodic counterexample measures. The eigenbasis changes the location but not the threshold width. The construction depends closely on existing Riesz-product machinery, so mathematical novelty relative to unlocated reformulations of that machinery is a residual priority risk. 

## References
1. X. Han, *Invariant measures with uniform projection on surfaces and billiards*, arXiv:2611.18817v1 (13 November 2026), especially Appendix A, Sections A.1–A.3. https://arxiv.org/html/2611.18817v1
2. A. Fan, K. Schmidt, E. Verbitskiy, *Bohr chaoticity of principal algebraic actions and Riesz product measures*, arXiv:2103.04767v1 (8 March 2021), especially the discussion of Riesz products. https://arxiv.org/abs/2103.04767
3. A. Zygmund, *Trigonometric Series*, Section V.7 (classical Riesz-product background as cited by Han).
