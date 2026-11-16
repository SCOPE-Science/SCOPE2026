# A unique conditional-independence angle for three periodic heat-kernel samples

## Finding

Let \(H_t(\theta)=\sum_{m\in\mathbb Z}e^{-tm^2}e^{im\theta}\) be the positive periodic heat covariance on \(\mathbb R/(2\pi\mathbb Z)\). Sample a centered Gaussian field with this covariance at \((-a,0,a)\), where \(t>0\) and \(0<a<\pi\), and let \(Q_t(a)\) be the inverse of the resulting \(3\times3\) covariance matrix. There is exactly one threshold \(a_*(t)\) in the explicit interval
\[
\frac{\pi}{2}<a_*(t)<\arccos\!\left(-\frac13\right)
\]
with the precise signs
\[
Q_{12}=Q_{23}<0,\qquad
\begin{cases}
Q_{13}>0,&0<a<a_*(t),\\
Q_{13}=0,&a=a_*(t),\\
Q_{13}<0,&a_*(t)<a<\pi.
\end{cases}
\]
In particular the two outer Gaussian observations are conditionally independent given the middle observation at exactly one separation in this symmetric three-point family. The threshold has two different explicit endpoint laws:
\[
\lim_{t\downarrow0}a_*(t)=\pi(2-\sqrt2),\qquad
a_*(t)=\frac\pi2+e^{-t}+O(e^{-2t})\quad(t\to\infty).
\]
The parameter \(t\) is the Fourier heat time, so no hidden variance, circle-length, or diffusion-time normalizations are assumed.

## Assumptions and scope

All statements hold for every real \(t>0\) and \(a\in(0,\pi)\). The three sampling sites are ordered \((-a,0,a)\) modulo \(2\pi\). We use a real Gaussian process: \(H_t\) is real and even. The result makes no statement about non-symmetric triples, four or more sampling sites, other stationary kernels, or monotonicity of \(a_*(t)\) in \(t\). A common positive multiplicative covariance normalization does not change the sign or independence assertions.

## Proof

**Positive definiteness and precision cofactors.** For distinct angles \(x_j\) and nonzero real \(v_j\),
\[
\sum_{i,j}v_iv_jH_t(x_i-x_j)
=\sum_{m\in\mathbb Z}e^{-tm^2}\left|\sum_jv_je^{imx_j}\right|^2>0.
\]
Indeed vanishing would require all Fourier moments to vanish, including the first \(n\) moments of a Vandermonde matrix on distinct points, forcing \(v=0\). Also \(H_t(x)>0\) by the periodized-Gaussian Poisson formula and \(H_t(x)<H_t(0)\) when \(x\notin2\pi\mathbb Z\), since the Fourier series gives \(H_t(0)-H_t(x)=2\sum_{m\ge1}e^{-tm^2}(1-\cos mx)>0\). Put \(h_0=H_t(0)\), \(h_1=H_t(a)\), \(h_2=H_t(2a)\). The covariance is
\[
\Sigma=\begin{pmatrix}h_0&h_1&h_2\\h_1&h_0&h_1\\h_2&h_1&h_0\end{pmatrix},\qquad \det\Sigma>0.
\]
The inverse cofactors give
\[
Q_{13}=\frac{h_1^2-h_0h_2}{\det\Sigma},\qquad
Q_{12}=Q_{23}=\frac{h_1(h_2-h_0)}{\det\Sigma}<0.
\]
Thus it remains to determine the sign of \(h_1^2-h_0h_2\).

**A one-crossing theta-product identity.** Set \(q=e^{-t}\), \(c=\cos a\) and \(r_j=q^{2j-1}\). The classical Jacobi triple product (DLMF 20.5.3) reads
\[
H_t(x)=\prod_{j=1}^\infty(1-q^{2j})(1+2r_j\cos x+r_j^2).
\]
The ratio \(R_t(c)=H_t(a)^2/[H_t(0)H_t(2a)]\), which is strictly positive, satisfies
\[
\log R_t(c)=\sum_{j=1}^\infty \log\frac{B_{r_j}(c)^2}{A_{r_j}C_{r_j}(c)},\qquad
B_r(c)=1+2rc+r^2,\quad A_r=(1+r)^2,\quad C_r(c)=(1-r)^2+4rc^2.
\]
Since \(r_j\in(0,1)\), all denominators are positive for \(c\in[-1,1]\). The key exact factorization, valid for every \(r\in(0,1)\), is
\[
B_r(c)^2-A_rC_r(c)=4r(1-c)\big[c(1+r+r^2)+r\big].\tag{1}
\]
At \(c=0\) every summand is strictly positive, while at \(c=-1/3\) every summand is strictly negative, because \(r-(1+r+r^2)/3=-(1-r)^2/3<0\). In fact every factor ratio is below one for \(c\in[-1,-1/3]\), and above one for \(c\in[0,1)\). On \(-1/3\le c\le0\),
\[
\frac{\partial}{\partial c}\log\frac{B_r(c)^2}{A_rC_r(c)}
=\frac{4r}{B_r(c)}-\frac{8rc}{C_r(c)}>0.
\]
The defining series and its derivative converge uniformly on this compact interval for each \(q<1\), since \(\sum_jr_j<\infty\) and all denominators have positive lower bounds. Therefore \(\log R_t(c)\) has precisely one root \(c_t\in(-1/3,0)\), has positive sign for \(c>c_t\), and negative sign for \(c<c_t\). As \(c=\cos a\) decreases strictly on \((0,\pi)\), this gives the claimed unique threshold \(a_*(t)=\arccos c_t\) and all its signs, with strictness at every noncritical angle.

**Small heat time.** Poisson summation yields
\[
H_t(x)=\sqrt{\pi/t}\sum_{k\in\mathbb Z}\exp\!\left(-\frac{(x-2\pi k)^2}{4t}\right).
\]
For fixed \(a\in(\pi/2,\pi)\), the shortest angular distances of \(a\) and \(2a\) from zero are respectively \(a\) and \(2\pi-2a\). Hence
\[
\lim_{t\downarrow0}4t\log R_t(\cos a)=-2a^2+4(\pi-a)^2.
\]
This continuous function changes sign exactly at \(a_0=\pi(2-\sqrt2)\) in the proven threshold interval. Comparison at \(a_0\pm\varepsilon\) and uniqueness of the threshold then imply \(a_*(t)\to a_0\).

**Large heat time.** When \(q=e^{-t}\downarrow0\), the leading triple-product factor has \(r_1=q\), and the sum of the remaining factors in \(\log R_t(c)\) is \(O(q^3)\) uniformly near \(c=0\). Its derivative in \(c\) is also \(O(q^3)\). Equation (1) for the first factor has its root at \(c=-q/(1+q+q^2)=-q+O(q^2)\), and the leading log-derivative is \(4q+O(q^2)\). A mean-value comparison gives \(c_t=-q+O(q^2)\), and \(\arccos c_t=\pi/2+q+O(q^2)\). This concludes the proof.

## Verification

The accompanying standalone `check.py` uses 65-digit theta evaluation and independently inverts the full \(3\times3\) matrices, comparing the predicted sign against the actual precision entry at several heat times and angles on both sides of the unique threshold. It also checks the exact algebraic factorization (1). Executing `python check.py` with `mpmath` installed produced 85 passing assertions. These finite computations provide cross-checks only; the proof above establishes the universal statements. The analytic limits do not rely on extrapolating computed root values.

## Relationship to prior work

Borovitskiy, Terenin, Mostowsky and Deisenroth (first public 2020-06-17, arXiv:2006.10160) give the periodic squared-exponential/heat covariance and its circle theta representation, including their Example 3 and Appendix B, Example 7. The present statement concerns sign changes and zero patterns of inverse covariance entries of a particular irregular three-site design, not kernel construction.

Huang and Li (first public 2022-01-30, arXiv:2201.12856) study a different circular Matérn spectral family and its sparse Markov/conditional-autoregressive connection; their precision results do not directly cover the periodic Gaussian heat kernel in this theorem. Cunden, Mezzadri and O'Connell (2018) note strict positivity of odd-order circle heat-kernel determinants through Karlin–McGregor; such determinant positivity does not decide the sign of the non-principal \(2\times2\) minor \(h_1^2-h_0h_2\) and hence does not yield this unique transition. The classical Jacobi triple product is an acknowledged mathematical ingredient, not claimed new.

## Limitations

The new result is a one-parameter symmetric three-site classification, not a universal rule for arbitrary site collections. The proof does not establish monotonic dependence of the critical angle on heat time. Classical theta-function inequalities or general cyclic total-positivity comparisons might contain an equivalent previously published one-crossing statement not located in the inspected sources; independent historical-priority review is still needed.

## References

1. V. Borovitskiy, A. Terenin, P. Mostowsky and M. P. Deisenroth, *Matérn Gaussian Processes on Riemannian Manifolds*, arXiv:2006.10160, first public 2020-06-17, https://arxiv.org/abs/2006.10160 and open full text https://arxiv.org/html/2006.10160v6.
2. NIST Digital Library of Mathematical Functions, §20.5.3 (Jacobi theta-product identity), https://dlmf.nist.gov/20.5.E3.
3. F. Cunden, F. Mezzadri and N. O'Connell, *Free Fermions and the Classical Compact Groups*, *Journal of Statistical Physics* 171 (2018), 768–801, section 7, p. 793; open copy https://maths.ucd.ie/~noconnell/pubs/cmo18.pdf.
4. C. Huang and A. Li, *The Circular Matérn Covariance Function and its Link to Markov Random Fields on the Circle*, arXiv:2201.12856, first public 2022-01-30, https://arxiv.org/abs/2201.12856.
