# Symmetry-free sharp circular sign uncertainty from a compressed cosine moment matrix

## Finding

Let \(\mu\) be a nonzero finite positive Borel measure on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), with no reflection assumption, and fix any integer \(N\ge1\). Let \(\rho_N(\mu)\) be the least radius \(r\in[0,\pi]\) attained or approached by nonzero real trigonometric polynomials \(f\) of degree at most \(N\) such that \(\int f\,d\mu\le0\) and \(f(\theta)\ge0\) for all \(r\le|\theta|\le\pi\). All angles are radians, with the distinguished center at \(\theta=0\).

**Theorem.** If \(\#\operatorname{supp}(\mu)\le N\), then \(\rho_N(\mu)=0\). Otherwise define the positive definite Hermitian moment matrix \(G\) and Hermitian cosine matrix \(C\), indexed by \(0\le j,k<N\), by
\[
G_{jk}=\int_{\mathbb T}e^{i(k-j)\theta}\,d\mu(\theta),\qquad
C_{jk}=\int_{\mathbb T}\cos\theta\,e^{i(k-j)\theta}\,d\mu(\theta).
\]
Let \(\Lambda_N\) be the largest generalized eigenvalue of \(C v=\lambda Gv\). Then \(-1<\Lambda_N<1\), and
\[
\boxed{\rho_N(\mu)=\arccos\Lambda_N.}
\]
Every extremizer, and no other, is a polynomial
\[
\boxed{ f(\theta)=(\Lambda_N-\cos\theta)\left|\sum_{j=0}^{N-1}v_j e^{ij\theta}\right|^2,\quad 0\ne v\in\ker(C-\Lambda_NG). }
\]
Positive scaling is included by scaling \(v\). These functions have integral exactly zero. In particular, if the maximal generalized eigenvalue is simple, the extremizer is unique up to positive scaling.

**Asymmetric atomic example.** Let \(m\) denote normalized Haar measure and put \(\mu_w=(1-w)m+w\delta_{\pi/2}\), with \(0<w<1\). In degree \(N=2\),
\[
\Lambda_2(\mu_w)=\frac12\sqrt{\frac{1-w}{1+w}},\qquad
\rho_2(\mu_w)=\arccos\!\left(\frac12\sqrt{\frac{1-w}{1+w}}\right).
\]
For its reflection symmetrization \(\mu_w^{\mathrm{sym}}=(1-w)m+\tfrac w2(\delta_{\pi/2}+\delta_{-\pi/2})\), the sharp radius is instead \(\arccos((1-w)/2)\), strictly larger for every \(0<w<1\). Hence reflected symmetrization does not preserve the sharp radius. As \(w\uparrow1\), the radii approach \(\pi/2\), whereas the pure one-atom measure has radius zero because its support size is below the degree cutoff.

## Assumptions and scope

Finite positive means \(0<\mu(\mathbb T)<\infty\). Reflection symmetry, absolute continuity, a density lower bound, and a prescribed mass are not required. A polynomial of degree at most \(N\) is \(\sum_{k=-N}^N a_k e^{ik\theta}\) with \(a_{-k}=\overline{a_k}\). Its last-sign radius is the infimum of radii \(r\in[0,\pi]\) for which it is nonnegative on the closed complement of the centered open arc. The support cardinality may be infinite. The Gram matrices depend only on moments through order \(N\), and a strictly positive rescaling of \(\mu\) does not change \(\rho_N\).

## Proof

**1. Positivity and extremal eigenvalue.** If \(\#\operatorname{supp}\mu>N\), then \(v^*Gv=\int|Q_v(e^{i\theta})|^2\,d\mu>0\) for \(v\ne0\), because a nonzero polynomial \(Q_v\) of degree at most \(N-1\) cannot vanish at more than \(N-1\) distinct support points. Consequently the generalized Rayleigh quotient
\[
\frac{v^*Cv}{v^*Gv}=
\frac{\int\cos\theta\,|Q_v(e^{i\theta})|^2d\mu}
{\int|Q_v(e^{i\theta})|^2d\mu}
\]
attains a maximum \(\Lambda_N\). It is strictly less than \(1\), because \(1-\cos\theta\) vanishes at the single point \(\theta=0\), leaving more than \(N-1\) other support points; similarly it exceeds \(-1\). For every nonzero \(Q\) of degree at most \(N-1\) and every real \(c\ge\Lambda_N\),
\[
\int(c-\cos\theta)|Q(e^{i\theta})|^2d\mu\ge(c-\Lambda_N)\int|Q|^2d\mu.
\tag{1}
\]
Equality at \(c=\Lambda_N\) holds precisely for the maximal eigenspace.

**2. Arc factorization (degree-sensitive, with no evenness hypothesis).** Fix \(-1<c<1\), write \(R^2=(1+c)/(1-c)\), and suppose \(f\) is a real trigonometric polynomial of degree at most \(N\) that is nonnegative on \(\{\theta:\cos\theta\le c\}\). Set \(x=\tan((\theta-\pi)/2)\). Then
\[
\cos\theta=\frac{x^2-1}{1+x^2},\quad
\{\cos\theta\le c\}\longleftrightarrow[-R,R],\quad
F(x)=(1+x^2)^N f(\theta)
\]
is a real polynomial of degree at most \(2N\), nonnegative for \(x\in[-R,R]\). The degree bound follows by multiplying each Fourier monomial by \((1+x^2)^N\) and using the Cayley formula \(e^{i\theta}=-(1+ix)/(1-ix)\).

The real Markov–Lukács interval factorization gives real polynomials \(A,B\), with \(\deg A\le N\) and \(\deg B\le N-1\), satisfying
\[
F(x)=A(x)^2+(R^2-x^2)B(x)^2. \tag{2}
\]
For completeness, apply real-coefficient Fejér–Riesz factorization to the even nonnegative trigonometric polynomial \(F(R\cos t)\) of degree at most \(2N\). If \(H(e^{it})\) is its real-coefficient spectral factor of degree at most \(2N\), the real and imaginary parts of \(e^{-iNt}H(e^{it})\) are respectively a real polynomial in \(R\cos t\) of degree at most \(N\) and \(\sin t\) times a real polynomial there of degree at most \(N-1\). Taking their squared moduli yields (2). This argument covers endpoints and zeros by the nonnegative (not merely strictly positive) Fejér–Riesz theorem.

With \(z=e^{i\theta}\), the identities \(x=i(1+z)/(1-z)\) and \(1-ix=2/(1-z)\) convert \(A/(1-ix)^N\) and \(B/(1-ix)^{N-1}\) into ordinary polynomials \(P(z),Q(z)\) of degrees at most \(N,N-1\). Since \(c-\cos\theta=(1-c)(R^2-x^2)/(1+x^2)\), division of (2) by \((1+x^2)^N\) gives, on the entire circle by continuity,
\[
\boxed{f(\theta)=|P(e^{i\theta})|^2+
\frac{c-\cos\theta}{1-c}|Q(e^{i\theta})|^2.}\tag{3}
\]
No reflection assumption was used. The spectral factor can be chosen real because the cosine polynomial has real Fourier coefficients and one can choose its zero factors in conjugate pairs; factors on the unit circle have even multiplicity.

**3. Lower bound and complete equality cases.** For any \(c\in(\Lambda_N,1)\), apply (3) to a nonzero \(f\) nonnegative where \(\cos\theta\le c\). By (1),
\[
\int f\,d\mu\ge\int|P|^2d\mu+
\frac{c-\Lambda_N}{1-c}\int|Q|^2d\mu>0,
\]
unless \(P=Q=0\), contradicting \(f\ne0\). Thus a polynomial with nonpositive integral cannot have a last-sign radius smaller than \(\arccos\Lambda_N\). For every top eigenvector \(v\), the claimed \(f=(\Lambda_N-\cos\theta)|Q_v|^2\) has integral zero, is nonnegative when \(\cos\theta\le\Lambda_N\), and is negative at points arbitrarily close inside the corresponding arc boundary because a nonzero polynomial has isolated zeros. Hence its radius is exactly \(\arccos\Lambda_N\).

Conversely, any extremizing \(f\) is nonnegative on that closed complement: continuity and the definition of infimum guarantee it. Apply (3) with \(c=\Lambda_N\). The integral is a sum of two nonnegative quantities, the first strictly positive unless \(P=0\). Since \(\int f\le0\), it follows that \(P=0\) and \(Q\) is a maximal generalized eigenvector. Reabsorbing the positive factor \((1-\Lambda_N)^{-1}\) into \(Q\) gives precisely the asserted family.

**4. Small support and strict asymmetric example.** If \(\#\operatorname{supp}\mu=s\le N\), the nonzero nonnegative trig polynomial \(\prod_{j=1}^{s}|e^{i\theta}-e^{i\theta_j}|^2\) has degree \(s\le N\), zero \(\mu\)-integral, and last-sign radius zero. For \(\mu_w\), the matrices in the basis \((1,z)\) are
\[
G=\begin{pmatrix}1&iw\\-iw&1\end{pmatrix},\qquad
C=\begin{pmatrix}0&(1-w)/2\\(1-w)/2&0\end{pmatrix}.
\]
The equation \(\det(C-\lambda G)=0\) yields \(\lambda=\pm\frac12\sqrt{(1-w)/(1+w)}\). For its reflected symmetrization \(G=I\) and the same \(C\), giving \(\Lambda=(1-w)/2\). The strict comparison and the limit statements follow directly.

## Verification

Run \(\texttt{python3 CHECK.py}\) using only the standard library. The script evaluates six genuinely asymmetric Haar-plus-atom examples, checks the generalized eigen-equations, the exact zero-integral identity, strict signs at both sides of the predicted radius, and the contrasting reflected-case radius. It also reproduces the Haar benchmark in degrees one through twelve. The run returned \(\texttt{CHECK_OK}\) with sixty-six diagnostic assertions. The arbitrary-degree result and the factorization step rely on the analytical proof, not on finite sampling.

## Relationship to prior work

Ismoilov [1, Theorem 1] solves the sharp circular sign-uncertainty problem for reflection-symmetric measures using paraorthogonal zeros. Its proof and uniqueness statement do not assert a sharp formula for arbitrary nonsymmetric measures. The present compressed-cosine formula removes that assumption, identifies all equality fibers, and shows through \(\mu_w\) that the asymmetry cannot be eliminated by replacing a measure with its reflection average. The published symmetric Haar-plus-central-atom crossover [4] only concerns reflected measures and its critical small-atom regime; it does not determine the nonsymmetric problem.

The interval sum-of-squares factorization is classical [2], not claimed as new. Carneiro–Ismoilov–Ramos [3] develop sign uncertainty for even measures on the real line in de Branges spaces and do not state a finite circular nonsymmetric moment-pencil theorem. Combining classical arc factorization with a sharp moment-pencil argument is the contribution; the possibility of an older equivalent formulation in the truncated trigonometric moment literature remains a priority risk.

## Limitations

The exact result applies to finite **positive** measures and real trigonometric polynomials with a centered symmetric allowed-negative arc; signed measures, displaced nonsymmetric allowed-negative regions, and perturbation-stability estimates are not treated. Finite-support degeneracy is handled separately and leads to discontinuity at pure atoms. The explicit eigenvalue rule is exact but does not itself provide closed radicals in unbounded degree. Priority remains provisional pending an independent literature audit. No independent mathematical audit has been performed.

## References

[1] Tolibjon Ismoilov, *Sharp sign uncertainty for trigonometric polynomials*, arXiv:2606.02299v1 (first public June 1, 2026), Theorem 1 and Sections 1.2–1.3, 3. https://arxiv.org/abs/2606.02299

[2] Markov–Lukács interval nonnegativity factorization; see Bogdan Dumitrescu, *Positive Trigonometric Polynomials and Signal Processing Applications*, 2nd ed., Springer (2017), sections on trigonometric and arc factorization.

[3] Emanuel Carneiro, Tolibjon Ismoilov, and Antonio Pedro Ramos, *Sign uncertainty and de Branges spaces*, arXiv:2408.01186v1 (first public August 2, 2024), Introduction and Theorem 1. https://arxiv.org/abs/2408.01186

[4] *A critical point-mass boundary layer for sharp circular sign uncertainty*, publicly indexed mathematical finding dated November 1, 2026, available at https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-critical-point-mass-boundary-layer-for-sharp-circular-sign-unc--6e183d4a9c64
