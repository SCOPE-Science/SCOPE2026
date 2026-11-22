# Sharp radial second-moment and first-angular-gap inequalities in weighted polyanalytic Bergman spaces

## Finding
Let \(q\ge1\) be an integer, \(\alpha>-1\), and let \(\mathcal A^2_{q,\alpha}\) be the closed Hilbert space of polyanalytic functions of order at most \(q\) in the disk, with the probability measure
\[
\mathrm d\mu_\alpha(z)=\frac{\alpha+1}{\pi}(1-|z|^2)^\alpha\,\mathrm dA(z).
\]
Write \(Q_n^{(\alpha,\beta)}(t)=P_n^{(\alpha,\beta)}(2t-1)\) for the shifted Jacobi polynomial, and let \(\lambda_{q,\alpha}\) and \(\eta_{q,\alpha}\) be the smallest zeros in \((0,1)\) of \(Q_q^{(\alpha,0)}\) and \(Q_q^{(\alpha,1)}\), respectively. Then \(0<\lambda_{q,\alpha}<\eta_{q,\alpha}<1\), and for every \(f\in\mathcal A^2_{q,\alpha}\),
\[
\int_{\mathbb D}|z|^2|f(z)|^2\,\mathrm d\mu_\alpha\ge
\lambda_{q,\alpha}\|f\|_{2,\alpha}^2
+(\eta_{q,\alpha}-\lambda_{q,\alpha})
\operatorname{dist}_{2,\alpha}(f,\mathbb C\Phi_{q,\alpha})^2,
\tag{1}
\]
where \(\Phi_{q,\alpha}(z)=Q_q^{(\alpha,0)}(|z|^2)/(|z|^2-\lambda_{q,\alpha})\). The quotient is polynomial by divisibility. Both the ground constant and the stability coefficient are sharp. Equality in the unstrengthened ground inequality holds only for scalar multiples of \(\Phi_{q,\alpha}\); equality with a nonzero orthogonal component in (1) occurs precisely when that component is a scalar multiple of
\[
\Psi_{q,\alpha}(z)=z\frac{Q_q^{(\alpha,1)}(|z|^2)}{|z|^2-\eta_{q,\alpha}}.
\]
The first excited eigenspace is exactly \(\mathbb C\Psi_{q,\alpha}\). For fixed \(\alpha>-1\), with \(j_{\nu,1}\) the first positive zero of the Bessel function \(J_\nu\),
\[
\lim_{q\to\infty}q^2\lambda_{q,\alpha}=\frac{j_{0,1}^2}{4},\qquad
\lim_{q\to\infty}q^2(\eta_{q,\alpha}-\lambda_{q,\alpha})
=\frac{j_{1,1}^2-j_{0,1}^2}{4}.
\tag{2}
\]
In particular, the leading ground-radius and gap constants do not depend on the Bergman weight parameter.

## Assumptions and scope
The disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), and \(\mathrm dA\) denotes ordinary planar area. Polyanalytic of order at most \(q\) means \(\partial_{\bar z}^q f=0\) distributionally (equivalently, locally \(f=\sum_{j=0}^{q-1}\bar z^j h_j(z)\) with analytic \(h_j\)). Norm and distance are taken in \(L^2(\mu_\alpha)\); if \(f=0\), (1) is an equality. The complex linear spans in (1) do not depend on the choice of normalization of Jacobi polynomials. No claim is made about an arbitrary radial weight, a higher-dimensional ball, or the true-polyanalytic subspace alone.

## Proof
**1. Angular decomposition.** The rotation eigenspaces in \(\mathcal A^2_{q,\alpha}\) are mutually orthogonal and exhaust the space. At nonnegative angular frequency \(m\), the sector consists of functions \(z^m p(|z|^2)\), \(\deg p<q\). At negative frequency \(-r\), with \(1\le r<q\), the sector consists of \(\bar z^r p(|z|^2)\), \(\deg p<q-r\). This follows by collecting the terms of the standard polyanalytic expansion. Under \(t=|z|^2\), their squared norms are a common positive factor times
\[
\int_0^1|p(t)|^2t^\beta(1-t)^\alpha\,\mathrm dt,
\]
with \(\beta=m\) or \(\beta=r\), respectively. Multiplication by \(|z|^2\) preserves angular frequencies in its associated quadratic form.

**2. Exact finite-section spectra.** On polynomials of degree below \(n\) equipped with weight \(t^\beta(1-t)^\alpha\), the compression of multiplication by \(t\) has exactly the \(n\) simple zeros of \(Q_n^{(\alpha,\beta)}\) as eigenvalues. Indeed, if \(x\) is one such zero, the nonzero polynomial \(p_x(t)=Q_n^{(\alpha,\beta)}(t)/(t-x)\) has degree \(n-1\), and for every polynomial \(h\) of degree below \(n\),
\[
\int_0^1(t-x)p_x(t)\overline{h(t)}t^\beta(1-t)^\alpha\,\mathrm dt=0
\]
by Jacobi orthogonality. The \(n\) distinct zeros therefore exhaust the spectrum. The sector \(m\ge0\) contributes all zeros of \(Q_q^{(\alpha,m)}\); sector \(-r\) contributes all zeros of \(Q_{q-r}^{(\alpha,r)}\).

**3. The first two levels.** For each fixed nonzero polynomial \(p\) and \(\beta\ge0\), the expectation of \(t\) against the probability density proportional to \(|p(t)|^2t^\beta(1-t)^\alpha\) increases strictly with \(\beta\). Its derivative is \(\operatorname{Cov}(t,\log t)>0\), a strict inequality since the density is positive on an interval and both functions are strictly increasing. Taking minimizing polynomials shows that the lowest eigenvalue of a fixed-dimensional block strictly increases with \(\beta\). Reducing the polynomial degree cannot decrease the minimum. Thus all nonzero angular sectors have bottom strictly larger than the radial bottom, and among them the frequency \(+1\) block has the unique smallest bottom \(\eta_{q,\alpha}\). In particular, every negative-frequency block begins strictly above this value.

For \(q\ge2\), the Christoffel identity
\[
Q_q^{(\alpha,1)}(t)=c_{q,\alpha}\frac{Q_{q+1}^{(\alpha,0)}(t)+Q_q^{(\alpha,0)}(t)}{t},\qquad c_{q,\alpha}\ne0,
\]
expresses the degree-\(q\) orthogonal polynomial after multiplication of the Jacobi weight by \(t\). The identity follows by orthogonality and the cancellation of the numerator at zero, since \(Q_n^{(\alpha,0)}(0)=(-1)^n\), or by the Jacobi contiguous relation. At successive zeros of \(Q_q^{(\alpha,0)}\), the numerator alternates signs by the strict interlacing of consecutive Jacobi polynomials. Hence the first zero of \(Q_q^{(\alpha,1)}\) lies strictly between the first two zeros of \(Q_q^{(\alpha,0)}\). There are \(q-1\) such intervening zeros. The remaining zero lies after the last radial zero: the min–max principle applied to the strictly increasing Rayleigh quotient as the Jacobi exponent \(eta\) grows shows that each ordered eigenvalue of the same-size compression strictly increases. For \(q=1\), there is no second radial zero. Consequently \(\eta_{q,\alpha}\) is always the simple second eigenvalue of the global compressed radial multiplication operator. The corresponding two eigenspaces were constructed in step 2.

**4. Sharp coercivity and equality.** Orthogonally decompose \(f=a\Phi_{q,\alpha}+g\), with \(g\perp\Phi_{q,\alpha}\). The quadratic form in (1) equals \(\lambda_{q,\alpha}\|a\Phi_{q,\alpha}\|^2+\langle Tg,g\rangle\), where \(T\) is the compression of multiplication by \(|z|^2\). Step 3 gives \(\langle Tg,g\rangle\ge\eta_{q,\alpha}\|g\|^2\), with equality if and only if \(g\in\mathbb C\Psi_{q,\alpha}\). This proves the sharp inequality and all equality cases.

**5. Hard-edge limit.** The classical Mehler–Heine asymptotics for Jacobi polynomials near the endpoint \(-1\), or equivalently the shifted endpoint \(t=0\), give for each fixed \(\beta\ge0\)
\[
q^2\,\min\{t\in(0,1):Q_q^{(\alpha,\beta)}(t)=0\}
\longrightarrow j_{\beta,1}^2/4
\]
for each fixed \(\alpha>-1\). Apply this for \(\beta=0\) and \(1\) and subtract to obtain (2).

## Verification
The standalone `verify.py` uses only Python's standard library. It computes rational moment-pencil determinants \(\det(H-\lambda G)\), where \(G_{ij}=\int_0^1t^{\beta+i+j}(\alpha+1)(1-t)^\alpha\,\mathrm dt\) and \(H_{ij}=G_{i,j+1}\), and checks their exact polynomial proportionality to \(Q_q^{(\alpha,\beta)}\) for \(q\le4\), \(\beta\le3\), and four rational \(\alpha\) values. It also checks finite root ordering, including negative angular blocks, for \(q\le7\), using numerical bracketing. The actual replay returned `PASS 316 finite checks`. The infinite assertions, strict interlacing, and Bessel hard-edge limit depend on the written argument and classical Jacobi theory, not on these finite tests.

For \(q=2\), \(\alpha=0\), the sharp constants are \(\lambda_{2,0}=(1-1/\sqrt3)/2\) and \(\eta_{2,0}=(6-\sqrt6)/10\), so the stability gap is approximately \(0.143726\).

## Relationship to prior work
Barrera-Castelán, Maximenko, and Ramos-Vazquez (2020) give the angular decomposition of weighted polyanalytic Bergman spaces and a general matrix representation of radial Toeplitz operators. Their Sections 2, 3, 7, and 8 supply the established framework, including integral matrices for arbitrary bounded radial symbols; those results are not claimed here. The present claim singles out the natural radial second moment and establishes the exact two lowest *globally ordered* levels, their one-dimensional equality spaces, the globally sharp stability constant, and its simultaneous hard-edge scaling for all orders and beta weights. Their 2023 study of the generated radial Toeplitz operator algebras concerns a different operator-algebra question. These general representations facilitate an independent derivation of the finite matrix pencils, but do not themselves state the sharp ordered inequality or its hard-edge gap. Literature priority is provisional, particularly regarding possible earlier Gaussian-quadrature interpretations of the same special multiplication symbol.

## Limitations
This is an analytic proof using standard results on Jacobi zeros and Mehler–Heine asymptotics. The numerical tests are finite diagnostics, not substitutes for those results. No uniform-in-\(\alpha\) hard-edge limit is claimed: \(\alpha\) is fixed as \(q\to\infty\). The strict spectral gap is at the bottom of the whole full polyanalytic space, not a classification of all higher eigenvalue multiplicities. The authors of possible earlier equivalent classical quadrature formulations have not been exhaustively identified, so external historical-priority review remains important.

## References
1. R. M. Barrera-Castelán, E. A. Maximenko, G. Ramos-Vazquez, *Radial operators on polyanalytic weighted Bergman spaces*, first public preprint 29 September 2020, https://arxiv.org/abs/2009.14301 . Sections 2, 3, 7, 8.
2. R. M. Barrera-Castelán, E. A. Maximenko, G. Ramos-Vazquez, C-star algebras generated by radial Toeplitz operators on polyanalytic weighted Bergman spaces*, first public preprint 9 June 2023, https://arxiv.org/abs/2306.06231 . Sections 2, 3, 10.
3. Classical Jacobi orthogonality, Christoffel transformation, strict interlacing of consecutive Jacobi zeros, and the Mehler–Heine formula. Standard special-function facts used explicitly in the proof; these are not presented as new results.
