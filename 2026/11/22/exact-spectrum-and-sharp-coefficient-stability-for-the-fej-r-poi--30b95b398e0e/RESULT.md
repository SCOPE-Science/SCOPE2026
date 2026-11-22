# Exact spectrum and sharp coefficient stability for the Fejér pointwise inequality

## Finding

Let \(n\ge1\), let \(p(z)=\sum_{j=0}^{n}a_jz^j\) be any complex polynomial of degree at most \(n\), and let \(\tau(t)=|p(e^{it})|^2\). With normalized circle Haar convolution, put
\[
F_n(t)=\sum_{|k|<n}\left(1-\frac{|k|}{n}\right)e^{ikt}.
\]
For every \(\theta\in\mathbb R\), set \(b_j=a_je^{ij\theta}\) for \(0\le j\le n\). Then the following sharp coefficient-stability inequality holds:
\[
2(F_n*\tau)(\theta)-\tau(\theta)\ \ge\ \gamma_n\min_{c\in\mathbb C}\left(|b_0-c|^2+|b_n-c|^2+\sum_{j=1}^{n-1}|b_j|^2\right),
\]
where
\[
\boxed{\gamma_n=\begin{cases}
\displaystyle\frac{1}{n\cos^2(\pi/(2n))},&n\text{ even},\\[4pt]
\displaystyle\frac{1}{n\cos^2(\pi/(2(n+1)))},&n\text{ odd}.
\end{cases}}
\]
This constant is the greatest possible, separately for every integer \(n\ge1\). Equality holds exactly when \(b\) lies in the complex span of the endpoint vector \(e=(1,0,\ldots,0,1)\) and the single soft eigenvector \(v^{\mathrm{soft}}\), defined by
\[
v^{\mathrm{soft}}_j=\begin{cases}
\cos\left(\frac{(n-1)\pi}{n}(j-n/2)\right),&n\text{ even},\\[4pt]
\sin\left(\frac{n\pi}{n+1}(j-n/2)\right),&n\text{ odd}.
\end{cases}
\]
Thus an equality vector is \(b=ce+dv^{\mathrm{soft}}\) with arbitrary \(c,d\in\mathbb C\). To attain the sharp positive ratio, choose \(d\ne0\); the case \(d=0\) gives the zero-deficit classical extremizers.

More strongly, the entire finite-dimensional coefficient-slack spectrum is explicit. Let \(H_n\) be the Hermitian matrix
\[
(H_n)_{jk}=1-\frac{2|j-k|}{n},\qquad 0\le j,k\le n.
\]
Its kernel is \(\mathbb Ce\), and its \(n\) strictly positive eigenvalues, all simple, are
\[
\lambda^{S}_{\ell}=\frac{1}{n\sin^2((2\ell-1)\pi/(2n))},\quad 1\le\ell\le\lfloor n/2\rfloor,
\]
\[
\lambda^{A}_{\ell}=\frac{1}{n\sin^2((2\ell-1)\pi/(2(n+1)))},\quad 1\le\ell\le\lceil n/2\rceil.
\]
The first family is reflection-symmetric with eigenvector components \(\cos(((2\ell-1)\pi/n)(j-n/2))\); the second is antisymmetric with components \(\sin(((2\ell-1)\pi/(n+1))(j-n/2))\). For \(n=1\), the symmetric family is empty, as prescribed.

## Assumptions and scope

The variable \(t\) lies on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\); the Haar measure is \(dt/(2\pi)\). Convolution and the polynomial degree are exactly as defined above. The input \(p\) may have zeros anywhere, and coefficients may vanish. The result applies to every nonnegative trigonometric polynomial \(\tau\) of degree at most \(n\) by choosing any Fejér–Riesz factor \(\tau=|p|^2\); its right-hand side depends on that factor. The spectrum and bounds hold for every integer \(n\ge1\), with no asymptotic restriction.

## Proof

**Coefficient form.** Write \(\tau(t)=\sum_{j,k=0}^{n}a_j\overline{a_k}e^{i(j-k)t}\). The Fourier multiplier of \(F_n\) at frequency \(j-k\) is \(1-|j-k|/n\), including zero at the endpoints \(|j-k|=n\). Hence
\[
2(F_n*\tau)(\theta)-\tau(\theta)
=\sum_{j,k=0}^{n}\overline{b_j}\left(1-\frac{2|j-k|}{n}\right)b_k=b^*H_nb.
\]
The endpoint vector \(e\) is in the kernel because for all \(j\),
\[
(H_ne)_j=\left(1-\frac{2j}{n}\right)+\left(1-\frac{2(n-j)}{n}\right)=0.
\]

**Discrete second difference.** For every vector \(v\), and every \(1\le j\le n-1\),
\[
(H_nv)_{j-1}-2(H_nv)_j+(H_nv)_{j+1}=-\frac4n v_j.
\]
This follows directly from the second difference of \(|j-k|\), which is \(2\) only when \(j=k\) and zero otherwise.

**Symmetric modes.** Fix \(1\le\ell\le\lfloor n/2\rfloor\), set \(\alpha=(2\ell-1)\pi/n\), and \(v_j=\cos(\alpha(j-n/2))\). The vector is reflection-symmetric, has \(v_0=v_n=0\), and satisfies \(v_{j-1}-2v_j+v_{j+1}=-4\sin^2(\alpha/2)v_j\). Set \(\lambda=[n\sin^2(\alpha/2)]^{-1}\). The previous second-difference identity shows \(H_nv-\lambda v\) is affine in \(j\). Reflection symmetry makes it constant. At \(j=0\), the sum \(\sum_k(1-2k/n)v_k\) vanishes by pairing \(k\) with \(n-k\), and \(v_0=0\), so the constant is zero. Thus \(H_nv=\lambda v\).

**Antisymmetric modes.** Fix \(1\le\ell\le\lceil n/2\rceil\), take \(\alpha=(2\ell-1)\pi/(n+1)\), and \(v_j=\sin(\alpha(j-n/2))\). Again the second-difference identity says \(d=H_nv-\lambda v\) is affine, with \(\lambda=[n\sin^2(\alpha/2)]^{-1}\). It is antisymmetric about \(n/2\). Extend the sine formula to \(j=-1\); the quantization \((n+1)\alpha\in(2\mathbb Z+1)\pi\) gives \(v_{-1}=v_0\). Antisymmetry gives \(\sum_{k=0}^{n}v_k=0\), hence
\[
(H_nv)_1-(H_nv)_0=\frac2n\left(\sum_{k=0}^{n}v_k-2v_0\right)=-\frac4n v_0.
\]
But \(\lambda(v_1-v_0)=\lambda(v_1-2v_0+v_{-1})=-4v_0/n\). Therefore \(d_1-d_0=0\). An affine antisymmetric sequence of zero slope is identically zero, proving this eigenpair.

**Completeness and simple spectrum.** There are \(\lfloor n/2\rfloor\) symmetric and \(\lceil n/2\rceil\) antisymmetric positive eigenvectors, plus \(e\). All eigenvalues within either family are positive and strictly decreasing with \(\ell\). No eigenvalues across the families coincide: equality of angles in \((0,\pi)\) would force \((2\ell-1)(n+1)=(2k-1)n\), impossible modulo \(n\) because \(1\le2\ell-1<n\). There are \(n+1\) distinct eigenvalues, so these vectors form a basis and the stated kernel is exact.

**Sharp stability and equality.** The largest sine angle of a symmetric mode is \((n-1)\pi/(2n)\) when \(n\) is even, and the largest sine angle of an antisymmetric mode is \(n\pi/(2(n+1))\) when \(n\) is odd. Comparing the competing families yields exactly the stated \(\gamma_n\), with one-dimensional eigenspace spanned by \(v^{\mathrm{soft}}\). Since \(H_n\) is Hermitian positive semidefinite with kernel \(\mathbb Ce\), the spectral theorem gives
\[
b^*H_nb\ge\gamma_n\|b-\Pi_{\mathbb Ce}b\|_2^2,
\quad\Pi_{\mathbb Ce}b=\frac{b_0+b_n}{2}e.
\]
Equality holds precisely on \(\mathbb Ce\oplus\mathbb Cv^{\mathrm{soft}}\). Taking \(b=v^{\mathrm{soft}}\) makes the ratio exactly \(\gamma_n\), so the constant cannot be enlarged. Given \(b\) and \(\theta\), set \(a_j=b_je^{-ij\theta}\) to realize the example as a polynomial; its modulus square is nonnegative. This proves all assertions.

## Verification

The included standard-library Python program `verify.py` checks the exact rational entries and second differences of \(H_n\), each stated eigenvector/eigenvalue relation and orthogonality for \(1\le n\le70\), the sharp soft-mode equality, and the independent sum-of-squares identity
\[
b^*H_nb=\frac1n\sum_{m=0}^{n-1}\left|\sum_{j=0}^n b_j-2\sum_{j=0}^m b_j\right|^2
\]
for deterministic complex coefficients at \(1\le n\le34\). It reports 421265 finite exact/spectral/identity assertions passed. These finite checks are supplementary; the preceding proof covers every integer degree.

## Relationship to prior work

MacDonald, *A convolution inequality and the Krzyż conjecture* (arXiv:2611.05363, first public November 3, 2026), proves the sharp pointwise inequality \(\tau\le2F_n*\tau\) and characterizes its zero-deficit factors. Its proof gives the sum-of-squares formula displayed above. The present theorem refines that exact identity by determining **every** eigenvalue, the optimal coefficient-distance stability constant, and the unique least-stable coefficient direction with a parity transition. The source proof does not state these spectral constants or modal classifications.

Ruzieh and Powers, *The distance spectrum of the path* (1990), diagonalize the unmodified graph distance matrix \((|j-k|)\). The matrix here is \(H_n=J-2D/n\) with a noncommuting rank-one term \(J\); the path-distance eigenvalues do not immediately give the stated spectrum or the Fejér stability constant. General discrete Brownian-bridge covariance spectra provide related finite-difference technology but do not, in the material inspected, identify this specific Fejér slack with its equality classes. No result with the same statement was found in the queried published mathematical records.

## Limitations

The result is an exact Hilbert coefficient-space stability inequality for a *chosen* Fejér–Riesz factor, not a uniform stability bound in a factor-independent function-space distance, and it does not settle the Krzyż conjecture. Equality does not imply the original zero-deficit extremizer when the soft-mode coefficient is nonzero. The literature comparison is based on inspected accessible sources; earlier formulations under distance-matrix, discrete-Green, or Brownian-bridge terminology could contain equivalent spectral facts. This has not received an independent mathematical audit.

## References

1. Sullivan Francis MacDonald, *A convolution inequality and the Krzyż conjecture*, arXiv:2611.05363 (v1 November 3, 2026; v2 November 5, 2026). https://arxiv.org/abs/2611.05363
2. S. N. Ruzieh and D. L. Powers, *The distance spectrum of the path \(P_n\) and the first distance eigenvector of connected graphs*, *Linear and Multilinear Algebra* **28** (1990), 75–81, https://doi.org/10.1080/03081089008818032
3. Classical Fejér–Riesz factorization theorem for nonnegative trigonometric polynomials, used only to transfer the proved polynomial-factor statement to \(\tau\).
