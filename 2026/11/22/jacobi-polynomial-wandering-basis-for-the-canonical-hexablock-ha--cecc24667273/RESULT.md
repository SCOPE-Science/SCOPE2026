# Jacobi-polynomial wandering basis for the canonical hexablock Hardy shift

## Finding

Let \(H^2(\mathbb H)\) be the Hardy space obtained from normalized Haar measure on \(\mathbb T^4\) through the canonical hexablock boundary map in the assumptions below. For the coordinate multiplier \(V=M_{x_3}\), the wandering subspace \(\mathcal W=H^2(\mathbb H)\ominus VH^2(\mathbb H)\) has an explicit orthonormal basis given by classical Jacobi polynomials, and its forward \(V\)-translates form an orthonormal basis of all \(H^2(\mathbb H)\).

More precisely, for every triple of integers \(J\ge L\ge0\) and \(K\ge0\), write
\[
 j=J-L,\quad Q=K+L,\quad r=\min(K,L),\quad
 \alpha=|K-L|-\tfrac12,\quad\beta=j-\tfrac12.
\]
Define \(p_m=a^j x_1^{K-m}x_2^{L-m}x_3^m\) for \(0\le m\le r\), and uniquely define the real coefficients \(c_m\) by
\[
P_r^{(\alpha,\beta)}(1-2t)=\sum_{m=0}^{r}c_m t^{r-m},
\]
where \(P_r^{(\alpha,\beta)}\) is the standard Jacobi polynomial. Put
\[
h_r=\int_0^1t^{\alpha}(1-t)^{\beta}
  \bigl(P_r^{(\alpha,\beta)}(1-2t)\bigr)^2\,dt,
\qquad
w_{J,K,L}=\sqrt{\frac\pi{h_r}}\sum_{m=0}^{r}c_mp_m.
\]
Then \(\{w_{J,K,L}:J\ge L\ge0,\ K\ge0\}\) is an orthonormal basis of \(\mathcal W\), and
\[
\boxed{\bigl\{x_3^n w_{J,K,L}:n\ge0,\ J\ge L\ge0,\ K\ge0\bigr\}}
\]
is an orthonormal basis of \(H^2(\mathbb H)\). Each \(\mathbb T^3\) character space has precisely one wandering dimension. Its explicit moment matrix is
\[
\boxed{\langle p_m,p_n\rangle=\frac1\pi
 B\!\left(Q-m-n+\tfrac12,\ j+\tfrac12\right),\qquad 0\le m,n\le r.}
\]
For \(r\ge1\), the Jacobi norm has the closed form
\[
h_r=\frac{\Gamma(r+\alpha+1)\Gamma(r+\beta+1)}
{(2r+\alpha+\beta+1)\,r!\,\Gamma(r+\alpha+\beta+1)};
\]
for \(r=0\), use \(h_0=B(\alpha+1,\beta+1)\). This separate endpoint convention is necessary when \(\alpha=\beta=-\tfrac12\).

## Assumptions and scope

Use variables \((\xi,\eta,\lambda,\mu)\in\mathbb T^4\) and define
\[
 \Psi(\xi,\eta,\lambda,\mu)=
 \left(\lambda\frac{\xi-1}{2},\ \eta\frac{\xi+1}{2},\
 \lambda\mu\frac{\xi+1}{2},\ \xi\eta\lambda\mu\right)
 =(a,x_1,x_2,x_3).
\]
Let \(\nu=\Psi_*(m_{\mathbb T^4})\), where \(m_{\mathbb T^4}\) is probability Haar measure, and set \(H^2(\mathbb H)=\overline{\mathbb C[a,x_1,x_2,x_3]}^{L^2(\nu)}\). This is precisely the canonical unweighted boundary Hardy space in Pal–Su–Tomar (2026). All Hilbert-space inner products are linear in the first variable. The theorem concerns this specific measure and multiplier, not an arbitrary hexablock-weighted Hardy space.

## Proof

**Character decomposition.** Under independent rotations of \(\eta,\lambda,\mu\), the pullback of \(a^j x_1^k x_2^\ell x_3^m\) has torus character \(\eta^{k+m}\lambda^{j+\ell+m}\mu^{\ell+m}\). Thus its character indices are \((J,K,L)=(j+\ell+m,k+m,\ell+m)\). At fixed \(J\ge L\ge0\) and \(K\ge0\), the possible monomials are exactly \(p_0,\ldots,p_r\). Distinct triples are orthogonal by Haar character integration. Polynomial density proves the orthogonal direct sum of these finite-dimensional spaces, denoted \(\mathcal H_{J,K,L}\).

**Moment matrix and independence.** Let \(t=\cos^2(\arg\xi/2)\). Its distribution under Haar \(\xi\) is \(dt/(\pi\sqrt{t(1-t)})\). The identities \(\lvert(\xi+1)/2\rvert^2=t\), \(\lvert(\xi-1)/2\rvert^2=1-t\), and \(((\xi+1)/2)^2=\xi t\) imply, for almost every \(\xi\),
\[
 p_m\circ\Psi=\eta^K\lambda^J\mu^L
 \left(\frac{\xi-1}{2}\right)^j
 \left(\frac{\xi+1}{2}\right)^Q t^{-m}.
\]
Here the apparent singularity at \(t=0\) is removable in the original polynomial expression. Multiplying two such expressions and integrating gives the displayed beta moment matrix. Since the common factor is nonzero almost everywhere and \(1,t^{-1},\ldots,t^{-r}\) are linearly independent on \((0,1)\), \(\dim\mathcal H_{J,K,L}=r+1\).

**Wandering line.** Since \(|x_3|=1\) almost everywhere on the parametrized boundary, \(V=M_{x_3}\) is an isometry. Its character action sends \((J,K,L)\) to \((J+1,K+1,L+1)\). Consequently,
\[
 V H^2(\mathbb H)\cap\mathcal H_{J,K,L}
  =\operatorname{span}\{p_1,\ldots,p_r\}
\]
with the right side interpreted as zero when \(r=0\). Indeed, multiplication by \(x_3\) maps the preceding character space \((J-1,K-1,L-1)\) onto this span when \(r\ge1\); otherwise no predecessor exists. Thus its orthogonal complement in each \(\mathcal H_{J,K,L}\) has dimension exactly one.

**Jacobi orthogonality and normalization.** Since \(Q-2r=|K-L|\), the pullback of \(\sum c_mp_m\) has the form of the common prefactor in the moment calculation times \(t^{-r}P_r^{(\alpha,\beta)}(1-2t)\). For each \(1\le k\le r\),
\[
 \left\langle\sum_{m=0}^r c_mp_m,p_k\right\rangle
 =\frac1\pi\int_0^1t^{\alpha}(1-t)^\beta
 P_r^{(\alpha,\beta)}(1-2t)t^{r-k}\,dt=0,
\]
by Jacobi orthogonality to polynomials of degree less than \(r\). Its norm squared is \(h_r/\pi\). Both \(\alpha\) and \(\beta\) exceed \(-1\), so \(h_r>0\) and the normalized vector is defined for every stated triple. Different triples are orthogonal by their characters. We have therefore found an orthonormal basis of the entire wandering subspace.

**Completeness of the translated basis.** The weighted polynomial degree \(\deg a=\deg x_1=\deg x_2=1\), \(\deg x_3=2\) provides an orthogonal homogeneous decomposition (by Haar rotations). Multiplication by \(x_3^n\) increases this degree by \(2n\), so \(\bigcap_{n\ge0}V^n H^2(\mathbb H)=\{0\}\): a vector lying in all ranges has no nonzero homogeneous component. Thus \(V\) is a pure isometry. The Wold decomposition then gives \(H^2(\mathbb H)=\bigoplus_{n\ge0}V^n\mathcal W\). Applying the explicit wandering basis proves the claimed orthonormal basis.

## Verification

The standalone `check.py` computes the Jacobi coefficients, evaluates beta moments, verifies orthogonality to the image span, checks the predicted normalization and tests Gram positivity across \(245\) parameter triples \(0\le K,L\le6\), \(0\le J-L\le4\). Its recorded output was `HEXABLOCK_JACOBI_CHECK_OK 1400`. These finite diagnostics check normalizations and boundary cases, but do not certify the infinite basis theorem: that follows from the preceding character, Jacobi and Wold arguments.

As a concrete low-degree case, \((J,K,L)=(1,1,1)\) gives \(r=1\), \(\alpha=\beta=-\tfrac12\), and \(P_1^{(-1/2,-1/2)}(1-2t)=\tfrac12-t\); hence \(w_{1,1,1}=\sqrt8\bigl(\tfrac12 x_3-x_1x_2\bigr)\). It is orthogonal to \(x_3\) and has norm one.

## Relationship to prior work

Pal, Su and Tomar (2026, arXiv:2611.17140v1) define the canonical boundary Hardy space, identify quasi-homogeneous and fibre-degree decompositions, and prove that \(M_{x_3}\) is a pure isometry. Those are premises, not new claims here. Their results do not supply the three-character beta moment matrices or explicit Jacobi vectors for the wandering space. Pal and Tomar (2025, arXiv:2507.14589) prove an abstract Wold-type decomposition for hexablock isometries and give vector-valued operator models; this is not an orthonormal polynomial basis for the subsequent canonical boundary Hardy space. The new result explicitly identifies every one-dimensional wandering character component and its normalization, then uses the established pure-isometry property to obtain an orthonormal basis. Standard Jacobi orthogonality and the classical Wold decomposition are used as established mathematical tools.

## Limitations

The construction applies specifically to the unweighted canonical Haar-pushforward Hardy measure. It does not give a classification of all hexablock isometries, a complete formula for all other coordinate multipliers in this basis, or a corresponding basis for alternative weighted measures. The novelty comparison is based on inspected accessible primary texts and mathematical-record searches; an equivalent basis under different variables in unidentified earlier literature cannot be categorically excluded. No independent mathematical audit has been performed.

## References

- S. Pal, G. Su and N. Tomar, *Hardy Spaces and Toeplitz operators on the Hexablock*, arXiv:2611.17140v1, 12 November 2026. https://arxiv.org/html/2611.17140v1
- S. Pal and N. Tomar, *Operators associated with a domain in \(\mathbb C^4\) and applications* (also indexed as *Operators associated with the hexablock*), arXiv:2507.14589, first submitted 19 July 2025. https://arxiv.org/abs/2507.14589
- Classical Jacobi polynomial orthogonality, e.g. NIST Digital Library of Mathematical Functions, Chapter 18, https://dlmf.nist.gov/18
- Classical Wold decomposition for isometries (standard Hilbert-space operator theory).
