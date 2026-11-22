# Magnetic-flux rigidity and a half-flux norm transition for three-mode quantum-torus convolution

## Finding

Fix three affinely independent lattice frequencies \(n_0,n_1,n_2\in\mathbb Z^2\), with \(\Delta=\det(n_1-n_0,n_2-n_0)\ne0\). For real deformation parameters \(\theta_1,\theta_2\), consider Fourier polynomials on the corresponding quantum two-tori,
\[
x=\sum_{j=0}^{2}\xi_jW_{\theta_1}(n_j),\qquad
y=\sum_{j=0}^{2}\eta_jW_{\theta_2}(n_j).
\]
Their quantum convolution is \(z=x\star y=\sum_{j=0}^{2}\xi_j\eta_jW_{\vartheta}(n_j)\), where \(\vartheta=\theta_1+\theta_2\). Put \(t_j=|\xi_j\eta_j|\) and \(q=\exp(2\pi i\vartheta\Delta)\).

**Flux-rigidity theorem.** The complete equality criterion for the Fourier \(\ell^1\) bound is
\[
\|z\|_\infty=\sum_{j=0}^{2}t_j
\quad\Longleftrightarrow\quad
q=1\ \text{or at most two of the }t_j\text{ are nonzero}.
\]
For nonzero \(x,y\), equality in the sharp Young bound
\[
\|x\star y\|_\infty\le \|x\|_2\|y\|_2
\]
holds precisely when the nonnegative vectors \((|\xi_0|,|\xi_1|,|\xi_2|)\) and \((|\eta_0|,|\eta_1|,|\eta_2|)\) are proportional **and** either \(q=1\) or their common nonzero support has cardinality at most two.

If \(q=-1\), let
\[
S=t_0^2+t_1^2+t_2^2,\qquad M=\max(t_0^2,t_1^2,t_2^2).
\]
Then every nonnegative coefficient triple has the **exact** norm
\[
\boxed{\quad
\|z\|_\infty=
\begin{cases}
\sqrt{2S},&2M\le S,\\
\sqrt M+\sqrt{S-M},&2M\ge S.
\end{cases}\quad}
\]
The two formulas coincide at \(2M=S\). In particular, three equal nonzero convolution coefficients give \(\|z\|_\infty=\sqrt6\,t_0\), rather than the commutative value \(3t_0\). This transition occurs exactly at the squared-amplitude triangle boundary, not at a chosen coefficient ordering.

## Assumptions and scope

We use the usual twisted Fourier generators \(W_\theta(n)\) of the rotation algebra, satisfying \(W_\theta(0)=I\), \(W_\theta(n)^*=W_\theta(-n)\), and
\[
W_\theta(n)W_\theta(m)
=\exp\bigl(\pi i\theta\det(n,m)\bigr)W_\theta(n+m).
\]
The canonical trace is normalized by \(\tau_\theta(W_\theta(n))=0\) for \(n\ne0\) and \(\tau_\theta(I)=1\). The resulting \(L^2\)-norm is computed using this trace; \(\|\cdot\|_\infty\) is the operator norm in the faithful tracial von Neumann representation. Convolution is the Fourier-coefficient product of Sukochev, Tastankul, Tulenov and Zanin, with output parameter the sum of input parameters.

The frequencies must be distinct and affinely independent. Zero coefficient entries are permitted. The first equality statement applies to every real output deformation, and the exact quantitative formula applies when \(\vartheta\Delta\in\mathbb Z+\tfrac12\), with no requirement that the individual deformation parameters be rational. The theorem concerns the special three-frequency Fourier packet, not a claim about equality or norms for arbitrary Fourier supports or other exponent triples.

## Proof

**1. Elimination of coefficient phases.** Left multiplication of \(z\) by the unitary \(W_\vartheta(n_0)^*\) preserves its norm and turns its three terms into scalar multiples of \(I,U,V\), with
\[
UV=qVU,\qquad U,V\text{ unitary},\qquad q=e^{2\pi i\vartheta\Delta}.
\]
A torus gauge automorphism multiplies \(W_\vartheta(n)\) by \(e^{is\cdot n}\). The map \(s\mapsto(s\cdot(n_1-n_0),s\cdot(n_2-n_0))\) modulo \(2\pi\) is surjective because the integer matrix has nonzero determinant. Consequently all three coefficient phases can be aligned, up to an overall scalar. Thus
\[
\|z\|_\infty=\|t_0I+t_1U+t_2V\|.
\]
The same gauge action shows the spectrum of any nontrivial relative Weyl unitary is the whole circle, so a sum supported on at most two distinct frequencies has norm equal to the sum of its coefficient magnitudes.

**2. Strictness under a nontrivial flux.** Write \(T=t_0I+t_1U+t_2V\). For every unit Hilbert-space vector \(h\), expansion of the squared norm gives the exact defect identity
\[
(t_0+t_1+t_2)^2-\|Th\|^2
=t_0t_1\|(U-I)h\|^2+t_0t_2\|(V-I)h\|^2+t_1t_2\|(U-V)h\|^2.
\]
Because \(UV=qVU\) and both unitaries have norm one,
\[
|1-q|=\|(UV-VU)h\|
\le2\bigl(\|(U-I)h\|+\|(V-I)h\|\bigr).
\]
It follows, for positive \(t_0,t_1,t_2\), that
\[
\|T\|^2\le (t_0+t_1+t_2)^2
-\frac{|1-q|^2}{8}\,t_0\min(t_1,t_2).
\]
The choice of base index can be rotated, giving the stronger version with \(t_0\min(t_1,t_2)\) replaced by \(\max_j t_j\min_{k\ne j}t_k\). For \(q\ne1\) this is strictly smaller than the coefficient sum. If \(q=1\), \(U,V\) commute and the gauge torus action forces their joint spectrum to be the full two-torus, so the coefficient sum is attained in the joint functional calculus. This proves the first equivalence, including zero-coefficient boundary cases.

**3. Equality in Young's inequality.** Orthogonality of distinct Fourier generators under the canonical trace gives
\[
\|x\|_2^2=\sum_j|\xi_j|^2,\qquad
\|y\|_2^2=\sum_j|\eta_j|^2.
\]
The coefficient triangle inequality followed by Cauchy–Schwarz yields
\[
\|x\star y\|_\infty\le\sum_j|\xi_j\eta_j|
\le\bigl(\sum_j|\xi_j|^2\bigr)^{1/2}
\bigl(\sum_j|\eta_j|^2\bigr)^{1/2}.
\]
For nonzero input vectors equality in Cauchy–Schwarz is equivalent to proportionality of the two nonnegative magnitude vectors, which also makes their supports agree. Combining this with Step 2 proves the stated necessary and sufficient Young equality criterion.

**4. Reduction at half flux.** If \(q=-1\), then \(UV=-VU\), so \(U^2\) and \(V^2\) are central in the generated algebra. Every irreducible fiber is a two-dimensional Clifford representation; after scalar phases and unitary conjugation one may take
\[
U=e^{iu}\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
V=e^{iv}\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Conversely, each choice of \(u,v\in\mathbb R\) defines a representation, and the gauge action makes the resulting fibers exhaustive for the norm. Thus the universal operator norm is the supremum of these matrix norms. For \(a=t_0\), \(b=t_1\), \(c=t_2\), computing the eigenvalues of the matrix times its adjoint gives
\[
\|aI+bU+cV\|^2
=S+2\max_{u,v}\sqrt{a^2b^2\cos^2u+a^2c^2\cos^2v+b^2c^2\sin^2(v-u)}.
\]
Set \(A=a^2b^2\), \(B=a^2c^2\), \(C=b^2c^2\). Writing \(h=\cos(2(v-u))\), the square of the expression maximized beneath the radical equals
\[
\frac{A+B+C}{2}+
\frac12\max_{-1\le h\le1}
\left[\sqrt{A^2+B^2+2ABh}-Ch\right].
\]
For positive \(a,b,c\), the bracket is concave and its derivative vanishes at
\[
h_*=\frac{a^4-b^4-c^4}{2b^2c^2}.
\]
If the squared amplitudes \(a^2,b^2,c^2\) satisfy all triangle inequalities, \(-1\le h_*\le1\), and substitution yields a maximal radicand \(S^2/4\). Otherwise a largest squared amplitude, say \(a^2\), exceeds the sum of the other two; the maximum is at \(h=1\) and the radicand is \(a^2(b^2+c^2)=M(S-M)\). The alternative endpoint \(h=-1\) gives the analogous result when \(b^2\) or \(c^2\) dominates. Thus the maximal radicand is
\[
\begin{cases}S^2/4,&2M\le S,\\M(S-M),&2M\ge S.\end{cases}
\]
Taking \(\sqrt{S+2\sqrt{\cdot}}\) gives the asserted piecewise norm formula. It extends by continuity to zero coefficients. At \(2M=S\), both expressions agree, so no endpoint is omitted.

## Verification

The defect identity is exact in any representation and proves strictness uniformly over states, not merely failure of finite-dimensional norm attainment. The half-flux reduction is a full C*-norm computation, not a finite spectral truncation. The companion standalone checker tests the closed formula against thousands of deterministic Pauli fibers, including the balanced, dominant and boundary regimes; finite tests corroborate but do not replace Steps 1–4. Its source and reproducibility instructions are included as `checker.py`.

For the equal three-coefficient case, \(S=3\), \(M=1\), so the formula gives \(\sqrt6\), while the coefficient-triangle and Young upper bound with equal input magnitudes is \(3\). For two nonzero coefficients the formula reduces to their sum, as required by Step 1.

## Relationship to prior work

Sukochev, Tastankul, Tulenov and Zanin construct the convolution, prove its general Young inequalities and establish the globally sharp constant one. Their Theorem 4.1 is the starting point, not a new contribution here. The additional statement is the **complete three-affinely-independent-mode equality criterion** and the **all-weight exact norm and phase transition at half flux**. The authors' proof of general sharpness uses constant generators and does not supply this sparse extremizer classification. Earlier work on quantum convolution in Frobenius von Neumann algebras uses a distinct algebraic construction; work on the operator \(u+v\) in rotation algebras concerns two generators, not the three-term, half-flux, all-weight norm diagram. General C*-algebraic Clifford reduction and classical equality conditions in Cauchy–Schwarz are standard tools, not claimed as new.

## Limitations

This theorem is restricted to a pair of inputs sharing three affinely independent frequencies in a two-dimensional quantum torus and to the \(L^2\times L^2\to L^\infty\) Young endpoint. The exact norm expression applies at half-integral total flux through the frequency triangle; away from those flux values only the equality classification and quantitative strictness estimate are established. It does not assert a best possible strictness gap for arbitrary flux or a classification of all arbitrary-support Young extremizers. Its mathematical originality remains subject to possible implicit coverage by general results on rotation-algebra norm geometry or sparse Fourier packets not located in the inspected sources.

## References

1. F. Sukochev, R. Tastankul, K. Tulenov, D. Zanin, *Convolution on quantum tori I: Sharp Young inequalities and endpoint Sobolev embeddings*, arXiv:2611.16350v1 (12 November 2026), https://arxiv.org/abs/2611.16350 .
2. L. Huang, Z. Liu, J. Wu, *Quantum convolution inequalities on Frobenius von Neumann algebras*, arXiv:2204.04401, https://arxiv.org/abs/2204.04401 .
3. J. Fang, C. Jiang, H. Lin, F. Xu, *On generalized universal irrational rotation algebras and the operator u+v*, arXiv:1210.4771, https://arxiv.org/abs/1210.4771 .
4. M. Ruzhansky, S. Shaimardan, K. Tulenov, *Hörmander type Fourier multiplier theorem and Nikolskii inequality on quantum tori, and applications*, arXiv:2402.17353, https://arxiv.org/abs/2402.17353 .
