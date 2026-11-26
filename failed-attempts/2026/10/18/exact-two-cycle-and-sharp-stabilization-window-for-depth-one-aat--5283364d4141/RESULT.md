# Exact two-cycle and sharp stabilization window for depth-one AATGS on planar shifted rotations

## Finding
For any \(\mu>0\), \(\omega>0\), \(\beta>0\), and any initial point \(x_0\ne A^{-1}b\), let
\[
A=\mu I+\omega J,\qquad J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad f(x)=b-Ax.
\]
Apply the **unrestarted, one-vector-window AATGS(1)** iteration of Tang et al., using the same prescribed constant \(\beta\) at every mixing step. Write \(x_*=A^{-1}b\),
\[
S=\mu^2+\omega^2,\qquad \beta_{\rm MR}=\mu/S,\qquad r=\omega/\sqrt S,\qquad z=\sqrt{1-2\mu\beta+S\beta^2}.
\]
Then its steps alternate **exactly**:
\[
x_{2j+1}=x_{2j}+\beta f(x_{2j}),\qquad
x_{2j+2}=x_{2j+1}+\beta_{\rm MR}f(x_{2j+1})\quad(j\ge0).
\]
The unnormalized least-squares coefficients at even positive indices are zero; those at odd positive indices equal \(1-\beta_{\rm MR}/\beta\). Consequently,
\[
\|x_{2j}-x_*\|=(rz)^j\|x_0-x_*\|,\qquad
\|x_{2j+1}-x_*\|=z(rz)^j\|x_0-x_*\|.
\]
The method converges for every starting point if and only if
\[
0<\beta<\beta_{\rm crit}:=\frac{\mu}{S}\left(1+\sqrt{2+\frac{\mu^2}{\omega^2}}\right).
\]
At equality the error norms on the even and odd subsequences remain fixed and strictly positive; for larger \(\beta\) the errors diverge. By contrast, ordinary unaccelerated Richardson with the same fixed step converges if and only if \(0<\beta<2\mu/S\). Since \(\beta_{\rm crit}>2\mu/S\), an open interval of **divergent base iterations is rescued** by one-vector acceleration. Indeed \(\beta_{\rm crit}/(2\mu/S)\to\infty\) as \(\omega/\mu\downarrow0\), while \(\kappa_2(A)=1\) identically.

## Assumptions and scope
All quantities are real, \(\mu,\omega,\beta>0\), computations exact, initial error nonzero. The scalar is the constant input mixing parameter \(\beta\), **not** a line search recomputed at each step. The AATGS(1) convention is to initialize \(x_1=x_0+\beta f_0\) and at each \(j\ge1\) normalize \(q_j=(f_j-f_{j-1})/\|f_j-f_{j-1}\|\), pair it with \(u_j=(x_j-x_{j-1})/\|f_j-f_{j-1}\|\), and update
\[
\theta_j=q_j^Tf_j,\qquad x_{j+1}=x_j-u_j\theta_j+\beta(f_j-q_j\theta_j).
\]
Window one does no orthogonalization against earlier columns. The algorithm is well defined at every finite step, since \(A\) is nonsingular and no finite iterate equals \(x_*\).

## Proof
First \(A^TA=SI\), and therefore for every nonzero vector \(v\),
\[
\langle v,Av\rangle=\mu\|v\|^2,\qquad \|Av\|^2=S\|v\|^2.
\]
Put \(\alpha_j\) for the last actual scalar step whenever \(x_j-x_{j-1}=\alpha_j f_{j-1}\). Then \(f_j=(I-\alpha_j A)f_{j-1}\), \(\Delta f_{j-1}=-\alpha_j A f_{j-1}\), and direct substitution gives the **unnormalized** least-squares coefficient
\[
t_j:=\frac{\langle f_j,\Delta f_{j-1}\rangle}{\|\Delta f_{j-1}\|^2}=1-\frac{\beta_{\rm MR}}{\alpha_j}.
\]
The prescribed AATGS formula is equivalently
\[
x_{j+1}=x_j+\beta f_j-(\Delta x_{j-1}+\beta\Delta f_{j-1})t_j.
\]
If \(\alpha_j=\beta\), then \(\Delta x_{j-1}+\beta\Delta f_{j-1}=\beta f_j\), so the next step is \(\beta(1-t_j)=\beta_{\rm MR}\) times \(f_j\). If \(\alpha_j=\beta_{\rm MR}\), then \(t_j=0\), so the next step is \(\beta f_j\). Since \(\alpha_1=\beta\), induction proves the claimed alternation; in normalized coordinates the coefficient is \(\theta_j=\|\Delta f_{j-1}\|t_j\), so statements about zero/nonzero should be understood for the **unnormalized** least-squares coefficient \(t_j\), not literally \(\theta_j\). In particular \(\theta_j\) vanishes for even \(j\), while \(t_j=1-\beta_{\rm MR}/\beta\) for odd \(j\).

Both \(I-\beta A\) and \(I-\beta_{\rm MR}A\) are real scalar rotations/dilations, with Euclidean norm factors \(z\) and \(r\), respectively. Their product has norm factor \(rz\). The strict inequality \(r^2z^2<1\) is equivalent to
\[
\beta^2-2\beta_{\rm MR}\beta-\frac{\mu^2}{\omega^2S}<0,
\]
whose unique positive root is \(\beta_{\rm crit}\). The root exceeds \(2\beta_{\rm MR}\), since \(\sqrt{2+\mu^2/\omega^2}>1\). For every \(\beta>0\), \(I-\beta A\) is invertible because \(\omega>0\), and similarly \(I-\beta_{\rm MR}A\) is invertible, so errors never become zero at finite time. Then \(\Delta f_{j-1}=-\alpha_j A f_{j-1}\ne0\). Finally \(A^TA=SI\) also proves \(\kappa_2(A)=1\) and the unaccelerated Richardson threshold; the ratio of the two thresholds diverges as claimed.

## Verification
The standalone \(`verify.py`\) implements Algorithm 1 with both general window sizes and the fixed-input window-one specialization. It checks the alternating coefficients and norm laws across a parameter grid, reproduces one rational certificate, and evaluates the strict stability boundaries. Execute \(`python verify.py`\) from the directory containing the file; no third-party package is needed. Its output is embedded in \(`verification_output.txt`\). Finite arithmetic checks illustrate, but do not prove, the infinitely iterated statements; the proof above is algebraic.

## Relationship to prior work
Tang, Xu, He, Saad and Xi [1] introduce AATGS, establish its limited-depth residual minimization property (Proposition 8) and full-depth correspondence with Anderson/GMRES. Those general facts, and the classical one-dimensional minimal-residual orthogonality, are prior machinery. The present result identifies the exact **alternating scalar recurrence** on a natural shifted-rotation test family and derives its necessary-and-sufficient stability window, including rescue of otherwise divergent fixed-relaxation steps; these specific conclusions were not found in the source's limiting-depth or skew-symmetry discussion. Potra and Engler [2] treat full-history Anderson and optimized mixing, where the mixing parameter is chosen after the history correction, rather than this fixed-parameter one-window dynamics. General prior results about GMRES or the minimal-residual line search do not directly state the one-window two-cycle and sharp boundary.

## Limitations
This is an exact-arithmetic planar real-normal family, not a universal stability theorem for arbitrary nonsymmetric matrices or nonlinear mappings. The method is **unrestarted** with window one and a constant positive input \(\beta\). The leading divergence or convergence is measured at individual iteration indices; local roundoff, near-boundary transient amplification, noise and nonconstant mixing are not analyzed. A related formula may exist under historical restarted-GMRES/ORTHOMIN terminology; mathematical novelty has not received independent validation.

## References
[1] Z. Tang, T. Xu, H. He, Y. Saad and Y. Xi, *Anderson Acceleration with Truncated Gram–Schmidt*, arXiv:2403.14961v1 (2024-03-22), https://arxiv.org/abs/2403.14961, especially Algorithm 1, Lemma 1, Proposition 8 and Sections 2.3–2.4.

[2] F. A. Potra and H. Engler, *A characterization of the behavior of the Anderson acceleration on linear problems*, arXiv:1102.0796v1 (2011-02-03), https://arxiv.org/abs/1102.0796, especially Sections 3–5.
