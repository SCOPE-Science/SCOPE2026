# Exact Grassmannian landscape and endpoint stability for real two-by-two Schatten widths

## Finding

Fix real exponents \(0<p<q\le\infty\). On the real four-dimensional space \(M_2(\mathbb R)\), consider the restriction norm
\[
\Phi_{p,q}(E)=\sup_{0\ne A\in E}\frac{\|A\|_{\mathcal S_q}}{\|A\|_{\mathcal S_p}}
\]
for every real two-dimensional linear plane \(E\), with \(\|A\|_{\mathcal S_\infty}\) the largest singular value. Let
\[
G_{p,q}(r)=\begin{cases}
\displaystyle \frac{((1+r)^q+(1-r)^q)^{1/q}}{((1+r)^p+(1-r)^p)^{1/p}},&q<\infty,\\[4pt]
\displaystyle \frac{1+r}{((1+r)^p+(1-r)^p)^{1/p}},&q=\infty,
\end{cases}\quad 0\le r\le1.
\]
There is a complete exact description of \(\Phi_{p,q}\) on the real Grassmannian \(\operatorname{Gr}_2(M_2(\mathbb R))\):

* If \(E\) contains a nonzero singular matrix, then \(\Phi_{p,q}(E)=1\).
* Otherwise, uniquely one of two mutually orthogonal conformal planes is dominant. In the identification of real matrices with complex-linear and conjugate-linear maps \(\xi\mapsto z\xi+w\bar\xi\), the plane is the graph \(w=Lz\) or \(z=Lw\) of a real-linear operator \(L:\mathbb C\to\mathbb C\) with \(\rho=\|L\|_{2\to2}<1\). Then
\[
\boxed{\Phi_{p,q}(E)=G_{p,q}(\rho).}
\]
Moreover, if \(E_0\) is the dominant conformal plane, the largest principal-angle sine in the Hilbert–Schmidt metric satisfies the **exact stability identity**
\[
\boxed{\|P_E-P_{E_0}\|_{\mathcal S_\infty}=\frac{\rho}{\sqrt{1+\rho^2}}.}
\]
Here \(P_E\) and \(P_{E_0}\) act on the four-real-dimensional Hilbert–Schmidt space, and \(\|\cdot\|_{\mathcal S_\infty}\) is the corresponding operator norm.

The strictly increasing function \(G_{p,q}\) maps \([0,1]\) onto \([2^{1/q-1/p},1]\), where \(1/\infty=0\). Thus there are precisely **two minimizer planes**, the complex-linear and conjugate-linear conformal planes, and the entire loss of optimality determines the exact Hilbert–Schmidt Grassmannian distance to the appropriate minimizer. The sharp local stability exponent changes at the operator-norm endpoint. For fixed finite \(q\), as \(\rho\downarrow0\),
\[
\Phi_{p,q}(E)=2^{1/q-1/p}\bigl(1+\tfrac{q-p}{2}\rho^2+O_{p,q}(\rho^4)\bigr),
\]
whereas for \(q=\infty\),
\[
\Phi_{p,\infty}(E)=2^{-1/p}\bigl(1+\rho+O_p(\rho^2)\bigr).
\]
The two exact optimizer planes yield the known third Gelfand number \(c_3(\mathrm{id}:\mathcal S_p^2(\mathbb R)\to\mathcal S_q^2(\mathbb R))=2^{1/q-1/p}\). The **new result is the global objective profile and sharp stability law for every admissible two-plane**, not that scalar minimum.

## Assumptions and scope

All planes and linear maps are **real-linear**, and all underlying matrices are real \(2\times2\). The exponents satisfy \(0<p<q\le\infty\), including \(p<1\); for quasi-Banach exponents only the homogeneous quasi-norm ratio is used. The Hilbert–Schmidt inner product is \(\langle A,B\rangle=\operatorname{tr}(A^TB)\). The two conformal planes are
\[
E_+=\left\{\begin{pmatrix}a&-b\\b&a\end{pmatrix}:a,b\in\mathbb R\right\},\quad
E_-=\left\{\begin{pmatrix}c&d\\d&-c\end{pmatrix}:c,d\in\mathbb R\right\}.
\]
They are orthogonal two-planes, and \(M_2(\mathbb R)=E_+\oplus E_-\).

## Proof

**1. Complex decomposition and singular values.** Regard \(\mathbb R^2\) as \(\mathbb C\). Each real-linear \(2\times2\) matrix acts uniquely by \(\xi\mapsto z\xi+w\bar\xi\) with \(z,w\in\mathbb C\). Its determinant is \(|z|^2-|w|^2\), and its singular values are precisely \(|z|+|w|\) and \(\bigl||z|-|w|\bigr|\). To verify the latter, the operator norm is \(|z|+|w|\), attained by matching the phases of \(z\xi\) and \(w\bar\xi\), while the product of singular values is the absolute determinant. Continuity covers zero. The Hilbert–Schmidt squared norm is \(2(|z|^2+|w|^2)\), making the \(z\) and \(w\) planes orthogonal.

**2. The rank-one boundary.** For every \(A\ne0\), the strict relation \(0<p<q\) implies \(\|A\|_{\mathcal S_q}/\|A\|_{\mathcal S_p}\le1\), and equality holds exactly for rank-one \(A\). A nonzero singular real \(2\times2\) matrix is rank one. Consequently, any plane meeting the determinant cone has \(\Phi_{p,q}(E)=1\).

**3. Graph dichotomy.** Suppose \(E\) has no nonzero singular element. The real projective line of \(E\) is connected, so \(\det A\) has the same strict sign for every nonzero \(A\in E\). If determinants are positive, the projection \((z,w)\mapsto z\) is an injective real-linear map from two-dimensional \(E\) onto two-dimensional \(\mathbb C\), hence bijective. Therefore \(E=\{(z,Lz):z\in\mathbb C\}\) for a unique real-linear \(L\). Strict determinant positivity gives \(|Lz|<|z|\) for every nonzero \(z\), and compactness of the unit circle gives \(\rho=\|L\|<1\). For negative determinants, interchange \(z\) and \(w\). This establishes the exhaustive graph or rank-one trichotomy.

**4. Exact objective.** For a nonzero graph element, put \(r=|Lz|/|z|\). The singular values are a common positive factor times \(1+r\) and \(1-r\), hence the ratio equals \(G_{p,q}(r)\). Set \(x=(1-r)/(1+r)\). For finite \(q\), its logarithmic derivative with respect to \(x\in(0,1)\) is
\[
\frac{x^{q-1}}{1+x^q}-\frac{x^{p-1}}{1+x^p}<0,
\]
because \(0<p<q\). For \(q=\infty\) the first term is zero and the derivative is again negative. Since \(x\) decreases strictly as \(r\) increases, \(G_{p,q}\) is strictly increasing on \([0,1]\). Compactness of the unit circle provides a \(z\) satisfying \(|Lz|=\rho|z|\). Therefore the exact supremum is \(G_{p,q}(\rho)\). Endpoints are \(G_{p,q}(0)=2^{1/q-1/p}\) and \(G_{p,q}(1)=1\). Only \(\rho=0\) attains the lower endpoint, forcing the graph to be one of the two conformal planes.

**5. Grassmannian distance.** Under the orthogonal Hilbert–Schmidt decomposition \(E_+\oplus E_-\), the principal angles between the graph of \(L\) and its base conformal plane have tangents equal to the singular values of \(L\). Accordingly the largest angle has sine \(\rho/\sqrt{1+\rho^2}\). For equal-dimensional real Hilbert subspaces the norm of the difference of their orthogonal projections equals this largest sine, giving the exact identity. Both conformal minimizer planes are fixed, not merely equivalent up to unspecified isometries.

**6. Local expansion.** For any finite positive \(s\), \((1+r)^s+(1-r)^s=2+s(s-1)r^2+O_s(r^4)\). Expanding the ratio proves the finite-\(q\) quadratic coefficient \((q-p)/2\). At \(q=\infty\), the numerator is \(1+r\) and the denominator has zero first derivative, yielding the displayed linear coefficient. Because these are nonzero for the stated exponents, both stability orders are sharp.

## Verification

The included standalone `check.py` implements the decomposition in real arithmetic, reconstructs the singular values by NumPy SVD, confirms the exact graph norm against direct sampling across multiple exponent pairs including quasi-Banach cases, checks monotonicity, and verifies the endpoint orders. All infinite-dimensional or all-plane assertions are proven by the preceding exact matrix identities and graph argument; finite numerical tests are supplementary rather than certificates of a universal statement. Execute `python check.py` with NumPy available.

## Relationship to prior work

Prochno's *Gelfand numbers of Schatten class embeddings in the quasi-Banach range* (arXiv:2611.08448, first publicly posted 5 November 2026) studies Gelfand-number asymptotics across matrix sizes. Hinrichs–Prochno–Vybíral (arXiv:2011.06554) and Prochno–Strzelecki (arXiv:2103.13050) obtain broad estimates for the embedding. The exact scalar third width in real order two is already available and is not claimed as original here. The new claim instead gives the exact **restriction norm for every real two-dimensional subspace**, the two uniquely minimizing conformal planes, and the exact principal-angle loss and finite-target versus operator-norm endpoint stability transition. This distinguishes a scalar width from its full Grassmannian objective landscape.

## Limitations

The theorem does not apply to complex-linear test subspaces, larger matrix orders, or mappings with \(p\ge q\). It does not claim that the scalar Gelfand number or the algebraic conformal decomposition is new. The novelty assessment depends on accessible research literature and may miss a historical formulation of the entire Grassmannian profile. The expansions are pointwise for fixed exponents, not uniform as \(q\to\infty\). Independent mathematical audit has not been performed.

## References

1. J. Prochno, *Gelfand numbers of Schatten class embeddings in the quasi-Banach range*, arXiv:2611.08448v1 (2026), https://arxiv.org/abs/2611.08448.
2. A. Hinrichs, J. Prochno and J. Vybíral, *Gelfand numbers of embeddings of Schatten classes*, arXiv:2011.06554 (2020), https://arxiv.org/abs/2011.06554.
3. J. Prochno and M. Strzelecki, *Approximation, Gelfand, and Kolmogorov numbers of Schatten class embeddings*, arXiv:2103.13050 (2021), https://arxiv.org/abs/2103.13050.
