# Sharp diagonal sensitivity of one-spike semidefinite repair

## Finding

For every integer \(n\ge2\), nearest positive-semidefinite repair can amplify a single diagonal entry by a sharp, dimension-dependent factor within the natural family consisting of one positive spectral mode and a flat negative bulk. Let \(\Pi(A)=A_+\) for real symmetric matrices, and set
\[
K_n=\sup_{\substack{\delta>0,\ \|u\|_2=1,\ 1\le i\le n\\H=H^\top,\ \|H\|_{\max}\le1}}
\bigl|(D\Pi_{uu^\top-\delta(I-uu^\top)}(H))_{ii}\bigr|.
\]
Here \(\|H\|_{\max}=\max_{i,j}|H_{ij}|\). Define \(t_n\) as the unique positive root of
\[
(n-1)t^3+3\sqrt{n-1}\,t^2-(n+1)t-\sqrt{n-1}=0.
\]
The exact sharp answer is
\[
\boxed{K_n=\frac{t_n^4+(n+1)t_n^2+2\sqrt{n-1}\,t_n}{(1+t_n^2)^2}.}
\]
The supremum is approached as \(\delta\downarrow0\) but never attained at finite positive \(\delta\). The constants increase strictly, \(K_2=3/2\), \(K_3<2<K_4\), and
\[
\boxed{K_n=\frac n4+\frac{\sqrt n}{2}+\frac34+O(n^{-1/2}).}
\]
In particular the unrestricted global entrywise Lipschitz constant of \(\Pi\) is at least \(K_n\); the result does **not** calculate that unrestricted constant.

## Assumptions and scope

All matrices are real symmetric of order \(n\ge2\). Spectral positive part \(A_+\) clips each negative eigenvalue of \(A\) to zero and is the nearest positive-semidefinite matrix in the Frobenius norm. The special base matrices are \(A_{\delta,u}=P-\delta Q\), with \(P=uu^\top\), \(Q=I-P\), a unit vector \(u\), and \(\delta>0\). The Fréchet derivative exists at every such base matrix because zero is absent from its spectrum. The input constraint \(\|H\|_{\max}\le1\) bounds every symmetric entry independently; only a **diagonal output coordinate** is optimized. No assertion of a sharp global or full-matrix output norm is made.

## Proof

**Spectral derivative.** Put \(\alpha=(1+\delta)^{-1}\in(0,1)\). Spectral divided differences of the scalar positive-part function at eigenvalues \(1,-\delta\) give
\[
D\Pi_{A_{\delta,u}}(H)=PHP+\alpha(PHQ+QHP)
=\alpha(PH+HP)+(1-2\alpha)PHP.
\]
This formula follows directly by differentiating the positive-eigenvalue spectral projection, or by the standard divided-difference rule for symmetric matrix functions; it applies to the stated spectral gap, not to the singular limit itself.

**Exact entrywise coefficient norm.** Fix diagonal index \(i\), write \(z=u_i^2\), and set \(S=\sum_{j\ne i}|u_j|\). The coefficient of \(H_{ii}\) in the indicated diagonal derivative is \(z^2+2\alpha z(1-z)\). Each independent off-diagonal \(H_{ij}\), \(j\ne i\), has coefficient \(2u_i u_j[z+\alpha(1-2z)]\); all entries supported on the other indices have the common coefficient sign \(\operatorname{sgn}(1-2\alpha)\), with their absolute total \(|1-2\alpha|zS^2\). Since \(z+\alpha(1-2z)=(1-\alpha)z+\alpha(1-z)\ge0\), optimizing independently over \(H_{jk}\in[-1,1]\) gives the *exact*, attained absolute row sum
\[
L(z,S,\alpha)=z^2+2\alpha z(1-z)
+2\sqrt z\,[z+\alpha(1-2z)]S+|1-2\alpha|zS^2.
\]
For fixed \(z\), each coefficient of \(S\) and \(S^2\) is nonnegative. Cauchy–Schwarz yields \(S\le\sqrt{(n-1)(1-z)}\), with equality precisely when the complementary coordinates of \(u\) have equal absolute values; hence the overall optimum uses this equality. Boundary values \(z=0,1\) follow by continuity.

**The endpoint comparison.** For every fixed \(z,S\), \(L\) is convex in \(\alpha\), being a linear function plus \(|1-2\alpha|zS^2\). Therefore
\[
L(z,S,\alpha)\le(1-\alpha)L(z,S,0)+\alpha L(z,S,1).
\]
The first endpoint equals \(z(\sqrt z+S)^2\). With \(S\) maximized as above, a one-variable maximization gives
\[
G_n:=\max_z L(z,\sqrt{(n-1)(1-z)},0)
=\frac{(1+\sqrt n)^2}{4}.
\]
For the second endpoint set \(t=\sqrt{z/(1-z)}\). Direct substitution yields
\[
F_n(t):=L(z,\sqrt{(n-1)(1-z)},1)
=\frac{t^4+(n+1)t^2+2\sqrt{n-1}\,t}{(1+t^2)^2}.
\]
At \(t=1\),
\[
F_n(1)-G_n=\frac{1+2\sqrt{n-1}-2\sqrt n}{4}>0\qquad(n\ge2).
\]
Indeed \(\sqrt n-\sqrt{n-1}=1/(\sqrt n+\sqrt{n-1})<1/2\). Thus \(K_n=\max_{t\ge0}F_n(t)\), and because \(G_n<K_n\), the strict convex-combination bound implies no \(0<\alpha<1\), hence no finite \(\delta>0\), attains \(K_n\).

**Unique maximizer and explicit near-extremizers.** Differentiation gives
\[
F_n'(t)=\frac{2[(n+1)t-(n-1)t^3+\sqrt{n-1}(1-3t^2)]}{(1+t^2)^3}.
\]
The negative of its numerator is \((n-1)t^3+3\sqrt{n-1}t^2-(n+1)t-\sqrt{n-1}\), whose nonzero coefficients have exactly one sign change. Descartes' rule and the opposite signs at zero and infinity yield one positive root \(t_n\), with derivative positive before and negative after. Hence \(t_n\) is the unique positive maximizer of \(F_n\). Choose an index \(i\), set
\[
|u_i|=\frac{t_n}{\sqrt{1+t_n^2}},\qquad
|u_j|=\frac1{\sqrt{(n-1)(1+t_n^2)}}\quad(j\ne i),
\]
and choose all coordinates nonnegative. Take the symmetric sign matrix \(H\) with \(H_{ii}=1\), all entries touching \(i\) equal to \(1\), and all entries with both indices different from \(i\) equal to \(-1\). For \(\alpha\uparrow1\), this realizes \(F_n(t_n)\) in the derivative; arbitrarily small actual input increments realize sensitivities arbitrarily close to it at nearby nonsingular base matrices.

**Dimension threshold.** For fixed \(t>0\), the numerator of \(F_{n+1}(t)-F_n(t)\) is \(t^2+2(\sqrt n-\sqrt{n-1})t>0\), so \(K_n\) strictly increases. For \(n=2\), the unique root is \(t_2=1\), hence \(K_2=3/2\). For \(n=3\),
\[
2-F_3(t)=\frac{t^4+2-2\sqrt2\,t}{(1+t^2)^2}>0
\]
because the numerator has global minimum \(2-3\cdot2^{-2/3}>0\), equivalent to \(32>27\). For \(n=4\), \(K_4\ge F_4(1)=(6+2\sqrt3)/4>2\). Therefore dimension four is the first crossing of two for this **restricted local diagonal sensitivity**, not necessarily for unrestricted matrix sensitivity.

**Asymptotic coefficient.** Divide the critical cubic by \(n\) and expand around its positive limiting root \(1\). The implicit equation yields \(t_n=1-n^{-1/2}+O(n^{-1})\). Uniform Taylor expansion for bounded real \(s\) gives
\[
F_n(1+s/\sqrt n)=\frac n4+\frac{\sqrt n}{2}+\frac12-\frac{s}{2}-\frac{s^2}{4}+O(n^{-1/2}).
\]
Substituting the maximizer, \(s=-1+O(n^{-1/2})\), establishes the claimed \(n/4+\sqrt n/2+3/4+O(n^{-1/2})\).

Finally, at fixed nonsingular \(A_{\delta,u}\), the local derivative is a limit of finite differences, so any bound valid for the unrestricted global Lipschitz constant must dominate the derived local sensitivity. This proves the claimed global **lower bound**, without identifying the unrestricted optimum.

## Verification

The standalone `verify.py` reproduces exact-rational coefficient identities, maximizer uniqueness indicators, matrix-level finite differences at nonsingular base matrices, dimension threshold examples, and asymptotic numerical residuals. Its run passed **1,671 assertions**. A finite checker supplies consistency tests only; the unrestricted all-dimension theorem is proved above analytically. Reproduce with `python verify.py` using Python, NumPy, and SciPy.

## Relationship to prior work

Nearest positive-semidefinite repair by spectral clipping is classical (Higham, 1988). Malick and Sendov (2006) study generalized Jacobians of the PSD-cone projector, which supplies general spectral derivative machinery. Bhojanapalli and Jain (arXiv:1402.2324, first posted 2014-02-10) describe the rank-one matrix tangent-space projector \(Z\mapsto PZ+ZP-PZP\) in a matrix-completion context: this coincides with our \(\alpha\uparrow1\) derivative, **so the limiting linear operator itself is not claimed as new**. Their work studies incoherence and sampling, rather than the sharp unconstrained entrywise diagonal operator norm on symmetric matrices and its cubic/asymptotic characterization. Goulart, Nakatsukasa, and Rontsis (arXiv:1908.01606) study gap-independent Frobenius perturbation bounds, not the exact componentwise constant here. The special order-two sharp global entrywise constant \(3/2\) is independently known; the present new claim is the all-order sharp *one-spike local diagonal* law, growth and threshold.

## Limitations

No equality is asserted for the unrestricted global Lipschitz modulus. The base matrices have one positive eigenvalue and a negative flat bulk; neither arbitrary spectra nor every output-matrix entry is optimized. All near-extremizers are limits as the negative bulk tends to zero while the base matrix remains nonsingular. The boundary point itself need not have a classical Fréchet derivative. Priority remains provisional: an unlocated equivalent norm optimization in older semidefinite or matrix-completion literature cannot be excluded. The Malick–Sendov full-text comparison was limited by access, and was not represented as a completed full-text inspection. Independent validation has not been performed.

## References

1. N. J. Higham, "Computing a nearest symmetric positive semidefinite matrix," *Linear Algebra and its Applications* 103 (1988), 103–118. DOI: 10.1016/0024-3795(88)90223-6.
2. J. Malick and H. S. Sendov, "Clarke generalized Jacobian of the projection onto the cone of positive semidefinite matrices," *Set-Valued Analysis* (2006), DOI: 10.1007/s11228-005-0005-1.
3. S. Bhojanapalli and P. Jain, "Universal Matrix Completion," arXiv:1402.2324, version 1 publicly posted 2014-02-10, especially its tangent-space projection formula.
4. P. J. Goulart, Y. Nakatsukasa, and S. Rontsis, "Accuracy of approximate projection to the semidefinite cone," arXiv:1908.01606, first posted 2019-08-05.
