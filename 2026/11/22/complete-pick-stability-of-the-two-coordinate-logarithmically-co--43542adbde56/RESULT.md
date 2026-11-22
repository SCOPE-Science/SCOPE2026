# Complete Pick stability of the two-coordinate logarithmically concave Hardy-block shift

## Finding
Let \(H^2\) denote the classical Hardy space, and let \(S\) be its unilateral shift. For real \(a\ge1\), \(b\ge a\), and complex \(u\) satisfying
\[
 a^2|u|^2\le(a^2-1)(b^2-a^2),
\]
consider the operator \(T\) on \(H^2\oplus\mathbb C^2\) defined by
\[
 T(f,\xi)=\big(zf+a\xi_1+u\xi_2,\ (b\xi_2,0)\big).
\]
Then \(T\) is expansive and logarithmically concave, its defect \(T^*T-I\) has rank at most two, and the normalized analytic reproducing-kernel space unitarily representing \(T\) as multiplication by \(z\) has the **complete Nevanlinna–Pick property**. This includes a nonempty open family with \(b>a\) and \(u\ne0\), including operators that are not concave. Within this two-coordinate nilpotent Hardy-block family, the displayed inequality is exactly the logarithmic-concavity condition (subject to \(a\ge1,b\ge a\)). No statement is made about arbitrary rank-two expansive operators outside this model.

## Assumptions and scope
The inner product is the standard complex Hilbert inner product. Expansive means \(T^*T\succeq I\); logarithmically concave means \(T^{*2}T^2\preceq(T^*T)^2\), and concave means \(T^{*2}T^2-2T^*T+I\preceq0\). The model has a nilpotent lower-right block \(A=\begin{psmallmatrix}0&b\\0&0\end{psmallmatrix}\) and a constant upper-right coupling \((a,u)\). The kernel is normalized at the origin; all kernel statements are for points of the unit disk \(\mathbb D\).

Set \(q(z)=ab+uz\). The inequality ensures \(|u|<ab\), so \(q\) has no zeros in the closed disk. The Hilbert space has orthonormal basis
\[
 1,\qquad \frac{az}{q(z)},\qquad \frac{z^{n+2}}{q(z)}\quad(n=0,1,2,\ldots),
\]
and reproducing kernel
\[
 K(z,w)=1+\frac{a^2z\bar w+(z\bar w)^2/(1-z\bar w)}{q(z)\overline{q(w)}}.
\]
Since multiplication by \(q\) carries its algebraic span onto the polynomials and \(q^{-1}\in H^\infty\), this space equals \(H^2\) as a vector space with an equivalent norm. Both forward and backward shifts are bounded.

## Proof
**1. Exact defect and logarithmic-concavity region.** On \(\mathbb C^2\) define
\[
 B=\begin{pmatrix}a&u\\0&b\end{pmatrix},\quad
 D=B^*B-I=\begin{pmatrix}a^2-1&au\\a\bar u&b^2+|u|^2-1\end{pmatrix}.
\]
The Hardy component contributes an isometry and is orthogonal to the constant coupling. Thus \(T^*T-I=0\oplus D\). Since \(D_{11}=a^2-1\ge0\) and
\[
 \det D=(a^2-1)(b^2-1)-|u|^2\ge0,
\]
we have \(D\succeq0\). More generally, putting \(P=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\), we have \(A=PB\) and
\[
 (T^*T)^2-T^{*2}T^2
 =0\oplus B^*WB,
 \qquad W=BB^*-I-P^*DP
 =\begin{pmatrix}a^2+|u|^2-1&bu\\b\bar u&b^2-a^2\end{pmatrix}.
\]
Because \(B\) is invertible, logarithmic concavity is equivalent to \(W\succeq0\). Its determinant is
\[
 \det W=(a^2-1)(b^2-a^2)-a^2|u|^2.
\]
The diagonal conditions and this determinant prove the precise parameter inequality and expansiveness in the stated range.

**2. Kernel model.** Define an isometry initially on \(H^2\oplus\mathbb C^2\) by
\[
 U(f,\xi)(z)=\frac{z^2 f(z)+a z\xi_1+(ab+uz)\xi_2}{q(z)}.
\]
The displayed basis is its image of the standard orthonormal basis, and direct substitution gives \(UT=M_zU\). Summing basis outer products gives \(K\) above.

**3. Positive Pick-defect decomposition.** Write \(t=z\bar w\) and
\[
 \gamma=b^{-2},\quad \eta=\frac{a^2-1}{a^2b^2},\quad x=\frac{u}{ab},\quad Q(z)=1+xz.
\]
Then
\[
 K(z,w)=1+\frac{t(\gamma-\eta t)}{Q(z)\overline{Q(w)}(1-t)}.
\]
Consider the Hermitian kernels
\[
 R=1-\frac{\gamma-\eta t}{Q(z)\overline{Q(w)}},
 \qquad H=\gamma R-\eta.
\]
After multiplying by the nowhere-zero factor \(Q(z)\overline{Q(w)}\), the coefficient matrices of these degree-one kernels, in the basis \((1,z)\), are
\[
 C_R=\begin{pmatrix}1-\gamma&\bar x\\x&|x|^2+\eta\end{pmatrix},\quad
 C_H=\begin{pmatrix}\gamma-\eta-\gamma^2&(\gamma-\eta)\bar x\\(\gamma-\eta)x&(\gamma-\eta)|x|^2+\gamma\eta\end{pmatrix}.
\]
Their determinants are
\[
 \det C_R=(1-\gamma)\eta-\gamma|x|^2
 =\frac{(a^2-1)(b^2-1)-|u|^2}{a^2b^4},
\]
\[
 \det C_H=(\gamma-\eta-\gamma^2)\gamma\eta-\gamma^2(\gamma-\eta)|x|^2
 =\frac{(a^2-1)(b^2-a^2)-|u|^2}{a^4b^8}.
\]
These are nonnegative by the parameter inequality. Their diagonal entries are nonnegative because \(b\ge a\ge1\), \(\gamma-\eta=1/(a^2b^2)>0\), and \(\eta\ge0\). Hence \(R\succeq0\) and \(H\succeq0\). Furthermore, \(R(z,z)=1-(\gamma-\eta|z|^2)/|Q(z)|^2<1\), since \(\gamma>\eta\ge0\); positivity also gives \(R(z,z)\ge0\). Cauchy–Schwarz for positive kernels yields \(|R(z,w)|<1\), so the series below converges locally uniformly.

Using \(1-tR=[Q(z)\overline{Q(w)}(1-t)+t(\gamma-\eta t)]/[Q(z)\overline{Q(w)}]\), the normalized Pick defect \(F=1-K^{-1}\) has the identity
\[
 \boxed{\displaystyle
 F(z,w)=\frac{\gamma t}{Q(z)\overline{Q(w)}}
  +\frac{t^2 H(z,w)}{Q(z)\overline{Q(w)}}\sum_{j=0}^{\infty}t^j R(z,w)^j.}
\]
Each term is a positive kernel: \(t^j\), \(R^j\), \(H\) are positive by Schur products, and division by the nonvanishing \(Q(z)\overline{Q(w)}\) preserves positivity. Hence \(F\succeq0\). Also \(K(z,z)>0\), so \(F(z,z)=1-1/K(z,z)<1\). Positivity then implies \(|F(z,w)|<1\). Thus \(K=(1-F)^{-1}\) is nonvanishing and normalized, and the McCullough–Quiggin/Agler–McCarthy characterization proves that \(K\) is complete Pick.

**4. Nonconcave genuinely coupled examples.** The triple \((a,b,u)=(2,3,1)\) has \(\det W=11>0\) and \(\det D=23>0\), so its shift is expansive and logarithmically concave with rank-two defect. However, the \((2,2)\) entry of \(D-A^*DA\) is \(9-27=-18<0\). This violates concavity. The coupling is genuinely nonzero; it cannot be inferred from a theorem assuming concavity.

## Verification
The standalone program `verify.py` performs exact rational arithmetic for 499 admissible integer triples. It checks the two defect determinants, both positive-kernel coefficient matrices, and the rational kernel/Pick-defect identity at selected disk points. It is a finite consistency diagnostic; the above Schur-product argument is the proof for every admissible complex \(u\) and the entire unit disk.

## Relationship to prior work
Luo–Rydhe (arXiv:2611.12778v1, 9 November 2026) prove that operator concavity implies the complete Pick property, and exhibit a counterexample to the analogous claim for logarithmic concavity using a three-coordinate nilpotent Hardy-block model. The present statement isolates the *two-coordinate* logarithmically concave class and proves its positive Pick property, including genuinely nonconcave couplings. A separate earlier calculation for the equal-diagonal subfamily \(b=a\) classifies its real one-parameter perturbations and identifies that its logarithmically concave locus has \(u=0\); that special locus does not imply positivity for \(b>a,u\ne0\). McCullough–Quiggin/Agler–McCarthy is used only as the standard CNP characterization, not as prior classification of this family. Ahmed–Das–Panja and Sau provide broader structural criteria for de Branges–Rovnyak kernels, but neither inspected theorem states the present nilpotent-block positivity region.

## Limitations
This establishes sufficiency only **within** the explicitly defined two-coordinate nilpotent Hardy-block family. It is not a classification of all rank-two defects, and it does not prove that all logarithmically concave expansive analytic shifts of rank two are complete Pick. No conclusion is drawn about arbitrary nonnilpotent lower-right blocks. The comparison to the literature is based on inspected accessible texts and indexed records; an unindexed equivalent remains possible. No independent audit has been performed.

## References
1. S. Luo and E. Rydhe, *Concave shifts and the complete Nevanlinna–Pick property*, arXiv:2611.12778v1 (first public 2026-11-09), https://arxiv.org/abs/2611.12778.
2. H. Ahmed, B. K. Das and S. Panja, *de Branges–Rovnyak spaces which are complete Nevanlinna–Pick spaces*, arXiv:2403.19377, https://arxiv.org/abs/2403.19377.
3. H. Sau, *On de Branges–Rovnyak kernels admitting a complete Pick factor*, arXiv:2606.09680, https://arxiv.org/abs/2606.09680.
4. J. Agler and J. E. McCarthy, *Complete Nevanlinna–Pick kernels*, arXiv:1610.01997, https://arxiv.org/abs/1610.01997.
