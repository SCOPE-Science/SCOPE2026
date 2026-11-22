# Sharp finite-degree conditioning of the hexablock coordinate multiplier

## Finding
Let \(H^2(\mathbb H)\) be the canonical Haar-pushforward Hardy space on the hexablock, and \(\mathcal P_{\le N}\) its weighted-polynomial subspace of degrees at most \(N\), using weights \((1,1,1,2)\) for \((a,x_1,x_2,x_3)\). For every integer \(N\ge0\),
\[
\min_{0\ne f\in\mathcal P_{\le N}}\frac{\|af\|^2}{\|f\|^2}=\sin^2\!\left(\frac{\pi}{2(N+2)}\right).
\]
The lowest singular value of multiplication by \(a\), restricted to \(\mathcal P_{\le N}\) and regarded as a map into the full Hardy space, has multiplicity exactly one when \(N\) is even and exactly two when \(N\) is odd. A complete finite spectral formula for all singular values is given below.

## Assumptions and scope
Define \(\Psi:\mathbb T^4\to\mathbb C^4\), with \(z,u,v,w\in\mathbb T\), by
\[
\Psi(z,u,v,w)=\left(v(z-1)/2,\ u(z+1)/2,\ vw(z+1)/2,\ zuvw\right).
\]
The Hilbert norm is \(\|f\|^2=\int_{\mathbb T^4}|f\circ\Psi|^2dm_4\), with normalized Haar probability. The coordinate \(a\) refers to the first component of \(\Psi\). The space \(\mathcal P_{\le N}\) consists of polynomials with \(a,x_1,x_2\) of weight one and \(x_3\) of weight two, total weight at most \(N\). All assertions concern this canonical *unweighted* boundary measure, not an alternative weighted measure.

For each triple \((i,B,C)\in\mathbb N_0^3\) with \(i+B+C\le N\), put \(m=\min(B,C)\), \(\delta=|B-C|\). An orthogonal summand \(E_{i,B,C}\) has basis
\[
\{a^i x_1^{B-j}x_2^{C-j}x_3^j:0\le j\le m\}.
\]
The full squared singular-value multiset of \(M_a|_{\mathcal P_{\le N}}\) is the union, over these triples, of
\[
\left\{(1+\zeta)/2:P_{m+1}^{(\delta-1/2,i-1/2)}(\zeta)=0\right\},
\]
with algebraic multiplicities, where \(P_n^{(\alpha,\beta)}\) denotes the standard Jacobi polynomial, with weight \((1-z)^\alpha(1+z)^\beta\) on \((-1,1)\).

## Proof
Pulling a basis monomial back to \(\mathbb T^4\) gives an external character \(u^Bv^{i+C}w^C\), times a one-variable polynomial in \(z\) of degree at most \(i+B+C\). Different triples have distinct characters, so their subspaces are mutually orthogonal for both \(\langle f,g\rangle\) and \(\langle af,ag\rangle\). For a fixed triple the one-variable subspace has the exact form
\[
(z-1)^i(z+1)^\delta z^m\,\mathbb C_m[t],\qquad t=(2+z+z^{-1})/4=|(1+z)/2|^2,
\]
up to a nonzero common scalar and external character. Here \(\mathbb C_m[t]\) denotes polynomials of degree at most \(m\). On the circle, \(|a|^2=1-t\). Under normalized Haar measure in \(z\), the induced density of the squared norm on \(\mathbb C_m[t]\) is a positive scalar multiple of \(t^{\delta-1/2}(1-t)^{i-1/2}\,dt\) for \(0<t<1\). Thus the compression of \(M_a^*M_a\) to this block is multiplication by \(1-t\), compressed to degree \(m\); its eigenvalues are \(1-t_j\), where \(t_j\) are the Gauss--Jacobi nodes. The above Jacobi-zero formula follows after the substitution \(\zeta=1-2t\).

For the sharp minimum, any one-variable polynomial \(h(z)=\sum_{j=0}^Nc_jz^j\) satisfies
\[
\int_{\mathbb T}|(1-z)h(z)/2|^2dm(z)=\frac12\sum_{j=0}^N|c_j|^2-\frac12\operatorname{Re}\sum_{j=0}^{N-1}c_{j+1}\overline{c_j}.
\]
This is the Rayleigh form of the \((N+1)\)-square tridiagonal matrix with diagonal \(1/2\) and adjacent entries \(-1/4\). Its least eigenvalue is \(\sin^2(\pi/(2(N+2)))\), simple, with strictly positive eigenvector \(c_j=\sin((j+1)\pi/(N+2))\). Applying this inequality to each orthogonal character component gives the lower bound for all \(f\in\mathcal P_{\le N}\).

Let \(\theta=\pi/(N+2)\) and \(g_N(z)=\sum_{j=0}^N\sin((j+1)\theta)z^j\). Its exact rational representation is
\[
g_N(z)=\sin\theta\,\frac{1+z^{N+2}}{1-2z\cos\theta+z^2}.
\]
It is a self-reciprocal polynomial of degree \(N\), nonzero at \(z=1\). At \(z=-1\) it has no zero if \(N\) is even, and exactly one zero if \(N\) is odd. If \(N=2m\), self-reciprocity writes \(g_N(z)=z^mR_m(t)\), where \(R_m\) has degree \(m\), hence realizes equality in \(E_{0,m,m}\). If \(N=2m+1\), it writes \(g_N(z)=(z+1)z^mR_m(t)\); both \(E_{0,m+1,m}\) and \(E_{0,m,m+1}\) realize equality. Conversely, any equality component must be a scalar multiple of \(g_N\), by simplicity of the tridiagonal least eigenvalue. Nonvanishing at \(1\), the precise order at \(-1\), and degree exactly \(N\) force \(i=0\), \(\delta=0\) for even \(N\) or \(\delta=1\) for odd \(N\), and \(i+B+C=N\). This leaves respectively one or two external characters, proving the multiplicities. The case \(N=0\) is included.

## Verification
The standalone \(check.py\) evaluates the Jacobi-node block formula for every cutoff \(0\le N\le40\), checks the exact predicted least squared singular value and its parity-dependent multiplicity, and checks the tridiagonal eigenvector residual. Its run reported `HEXABLOCK_FINITE_CUTOFF_DIAGNOSTIC_OK 123`. These finite calculations corroborate but do not replace the infinite family proof. All algebraic and measure claims needed for the proof are displayed above.

## Relationship to prior work
Pal--Su--Tomar introduce the canonical hexablock boundary Hardy space, its pullback map, and its weighted homogeneous decomposition (arXiv:2611.17140v1, Sections 3--4). The elementary tridiagonal eigenvalue formula is classical. A prior explicit Jacobi Wold-basis result for the same Hardy space supplies block Gram measures but does not state the sharp degree-cutoff conditioning, the simultaneous minimization over all character blocks, or the equality-mode multiplicity dichotomy. Those foundations are not claimed as new. The present assertion concerns the exact natural finite-cutoff multiplier invariant and its rigidity, rather than a new general Toeplitz eigenvalue principle.

## Limitations
The estimate is specific to the Haar-pushforward measure and the first coordinate. It does not characterize the spectrum of the untruncated multiplier or establish comparable optimality for other boundary measures. The proof uses standard finite Toeplitz eigenvalues; its novelty claim is limited to this exact hexablock finite-degree classification. Possible equivalent formulations in older polynomial extremal or Hardy-module literature remain a bibliographic risk; independent verification has not been performed.

## References
1. S. Pal, G. Su, N. Tomar, *Hardy Spaces and Toeplitz operators on the Hexablock*, arXiv:2611.17140v1 (first public posting 2026-11-12), https://arxiv.org/html/2611.17140v1.
2. G. Szegő, *Orthogonal Polynomials*, standard Jacobi orthogonality and Gaussian quadrature (classical background).
3. Classical spectrum of the finite symmetric path-adjacency (tridiagonal Toeplitz) matrix (standard background).
