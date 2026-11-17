# Rank-two complete-Pick rigidity at a critical shift coupling

## Finding

For every real \(a>1\) and \(b\) satisfying \(|b|<a^2-1\), define \(q_b(z)=a^2+bz\) on the unit disk \(\mathbb D\). There is a reproducing-kernel Hilbert space \(\mathcal H_{a,b}\), equal as a set to classical \(H^2(\mathbb D)\) with an equivalent norm, in which
\[
1,\qquad \frac{az}{q_b(z)},\qquad \frac{z^{n+2}}{q_b(z)}\quad(n\ge0)
\]
form an orthonormal basis. Its normalized kernel is
\[
K_{a,b}(z,w)=1+\frac{a^2z\bar w+(z\bar w)^2/(1-z\bar w)}{q_b(z)\overline{q_b(w)}}.
\]
The shift \(T_{a,b}=M_z\) is expansive with defect \(T_{a,b}^*T_{a,b}-I\) of rank exactly two for every allowed \(b\). Within this full parameter range, the following are equivalent:

1. \(K_{a,b}\) is a complete Nevanlinna–Pick (CNP) kernel.
2. \(T_{a,b}\) is logarithmically concave, meaning \(T_{a,b}^{*2}T_{a,b}^2\le T_{a,b}^*T_{a,b}T_{a,b}^*T_{a,b}\).
3. \(b=0\).

More quantitatively, let \(F_b=1-1/K_{a,b}\) near the origin and \(Q_b(z,w)=q_b(z)\overline{q_b(w)}F_b(z,w)\). Its Taylor coefficient matrix indexed by degrees two and three has the **exact** determinant
\[
\det [\widehat Q_b(i,j)]_{i,j=2,3}=-\frac{b^2}{a^4},
\]
whereas the determinant of the logarithmic-concavity slack on the defect space is \(-a^6b^2\). The complete-Pick and logarithmic-concavity conditions therefore both fail for arbitrarily small nonzero \(b\), despite persistence of expansivity and defect rank two. In a fixed abstract Hilbert-space realization, the corresponding multiplication operators differ by a rank-one operator of norm exactly \(|b|\). At \(b=0\), the model is the weighted unilateral shift with successive weights \(a,a,1,1,\ldots\); this CNP shift is logarithmically concave but is not concave. The equality of the two exceptional weights is the critical Pick-coefficient cancellation.

## Assumptions and scope

The scalar parameter \(a\) is real and strictly larger than one. The coupling \(b\) is real with \(|b|<a^2-1\); endpoints and parameters outside this interval are not classified. The Hilbert spaces are complex. Here *concave* means \(T^{*2}T^2-2T^*T+I\le0\), which differs from *logarithmically concave*. The CNP criterion used is the standard normalized-kernel criterion: a nonvanishing kernel with \(K(z,0)=1\) is CNP precisely when \(1-1/K\) is positive semidefinite. Positivity of an analytic kernel implies positive semidefiniteness of its Taylor coefficient matrices.

## Proof

**1. The Hilbert space and operator model.** Since \(|b|<a^2-1<a^2\), both \(q_b\) and \(1/q_b\) are bounded holomorphic multipliers of \(H^2\). The displayed basis is the image of the standard orthonormal basis of \(H^2\oplus\mathbb C^2\) under the invertible linear map
\[
U_b(f,x,y)(z)=\frac{z^2f(z)+azx+q_b(z)y}{q_b(z)}.
\]
It is invertible because multiplication by \(q_b\) reduces recovery of \(x,y\) to the constant and linear Taylor coefficients, after which the remainder is divisible by \(z^2\). Both it and its inverse are bounded. Declare \(U_b\) unitary by transport of norm, and sum the orthonormal-basis kernels to obtain the displayed \(K_{a,b}\), with \(K_{a,b}(z,0)=1\).

Let \(S\) be the Hardy unilateral shift, \(e_0(z)=1\), \(v_b(x,y)=e_0(ax+by)\) and \(A(x,y)=(ay,0)\). Direct substitution gives \(U_b\mathcal T_b=M_zU_b\) for
\[
\mathcal T_b=\begin{pmatrix}S&v_b\\0&A\end{pmatrix}
\quad\text{on }H^2\oplus\mathbb C^2.
\]
Indeed \(z(az,q_b(z))=z^2(a,b)+(az,q_b(z))A\), where the rightmost product is read row-wise. Consequently \(T_{a,b}\) is bounded and its defect can be computed using \(S^*e_0=0\).

**2. Rank-two expansivity.** On the \(\mathbb C^2\) summand, \(\mathcal T_b^*\mathcal T_b-I\) equals
\[
D_b=\begin{pmatrix}a^2-1&ab\\ab&a^2+b^2-1\end{pmatrix}.
\]
Its leading entry is positive and \(\det D_b=(a^2-1)^2-b^2>0\), so \(D_b\) is strictly positive, while the defect vanishes on the Hardy summand. Thus the defect is positive of rank exactly two for every allowed \(b\).

**3. Exact logarithmic-concavity boundary.** Logarithmic concavity is equivalent to positivity of \(\Delta+\Delta^2-\mathcal T_b^*\Delta\mathcal T_b\), where \(\Delta=0\oplus D_b\). Its nonzero block equals \(E_b=D_b+D_b^2-A^*D_bA\), explicitly
\[
E_b=\begin{pmatrix}
a^2(a^2+b^2-1)&ab(2a^2+b^2-1)\\
ab(2a^2+b^2-1)&b^2(3a^2+b^2-1)
\end{pmatrix},\qquad \det E_b=-a^6b^2.
\]
For \(b\ne0\) the negative determinant precludes positive semidefiniteness. For \(b=0\), \(E_0=\operatorname{diag}(a^2(a^2-1),0)\ge0\). The ordinary concavity slack at \(b=0\) is \(D_0-A^*D_0A=\operatorname{diag}(a^2-1,-(a^2-1)^2)\), which is indefinite.

**4. Exact complete-Pick boundary.** Put \(\tau=z\bar w\), \(R(z,w)=a^2\tau+\tau^2/(1-\tau)\), and \(P(z,w)=q_b(z)\overline{q_b(w)}\). Near \((0,0)\),
\[
Q_b=\frac{R}{1+R/P}=R-\frac{R^2}{P}+\frac{R^3}{P^2}-\cdots.
\]
Only terms through \(R^3\) can contribute to powers of degree at most three in both variables. Writing \(\widehat Q_b(i,j)\) for the \(z^i\bar w^{\,j}\) coefficient, direct exact expansion gives
\[
[\widehat Q_b(i,j)]_{i,j=2,3}=
\begin{pmatrix}
0&b/a^2\\
b/a^2&1-a^{-2}-b^2/a^4
\end{pmatrix}.
\]
If \(b\ne0\), its determinant is \(-b^2/a^4<0\). A positive analytic kernel has positive semidefinite Taylor coefficient matrices; since multiplication by \(q_b(z)\overline{q_b(w)}\) preserves positivity, the normalized CNP criterion excludes \(b\ne0\) (and the criterion also excludes a kernel having a zero).

For \(b=0\), \(K_{a,0}(z,w)=k_a(\tau)\), where
\[
k_a(\tau)=\frac{1-\alpha\tau-\beta\tau^2}{1-\tau},\qquad
\alpha=1-a^{-2}>0,\quad \beta=(a^2-1)a^{-4}>0.
\]
Since \(\alpha+\beta=1-a^{-4}<1\), its numerator has no zeros in \(|\tau|<1\). Write \(1-1/k_a(\tau)=\sum_{n\ge1}f_n\tau^n\). The rational identity
\[
1-\frac1{k_a(\tau)}=\frac{a^{-2}\tau-\beta\tau^2}{1-\alpha\tau-\beta\tau^2}
\]
shows \(f_1=a^{-2}>0\), \(f_2=0\), and \(f_n=\alpha f_{n-1}+\beta f_{n-2}\ge0\) for all \(n\ge3\). Hence \(1-1/K_{a,0}\) is a positive kernel, and the normalized criterion proves the CNP property.

**5. Arbitrarily small coupling.** All \(\mathcal T_b\) act on the same \(H^2\oplus\mathbb C^2\), and \(\mathcal T_b-\mathcal T_0\) sends the second defect coordinate to \(b e_0\) and annihilates its orthogonal complement. It therefore has rank one and norm \(|b|\). As \(b\to0\), the equivalent Hardy norms likewise converge under their identity identification, because the multiplier \(1/q_b\) and its inverse vary continuously in multiplier norm. The sharp boundary is internal to a continuous family of expansive rank-two shifts, not a consequence of leaving that class.

## Verification

The identity \(\det E_b=-a^6b^2\), the coefficient matrix of \(Q_b\) and its determinant are independently regenerated using exact rational formal-bivariate arithmetic in `checker.py`, with no floating-point approximations. The checker also verifies the recursive nonnegative CNP coefficients at \(b=0\) for finitely many indices, as a supplemental check only. The proof for every real parameter uses the exact algebra and kernel positivity argument above, not finite sampling.

## Relationship to prior work

Luo and Rydhe, *Concave shifts and the complete Nevanlinna–Pick property*, arXiv:2611.12778v1 (9 November 2026), prove that concave shifts on forward/backward invariant holomorphic RKHSs are CNP and exhibit an expansive logarithmically concave rank-three-defect shift that is not CNP. Their Section 4 employs a Hardy-shift-plus-finite-defect model and a finite Pick-coefficient obstruction. The present rank-two *critical-coupling classification* is a different statement: the unique CNP parameter is logarithmically concave but nonconcave, while every nonzero rank-one coupling destroys both properties. It does not assert the existence of a logarithmically concave non-CNP shift of defect rank two. The finite-rank defect framework was also studied by Luo and Rydhe (2023), for Dirichlet-type and higher-isometric shifts, without this Pick/logarithmic-concavity boundary. The general normalized-kernel criterion is classical; see Ahmed, Das and Panja (2024), and Chu (2019). Their broad CNP criteria do not themselves specify this two-parameter defect-matrix boundary or the exact quadratic obstructions.

## Limitations

The theorem classifies only the stated critical rank-two family with \(c=a\) in the nilpotent coupling \(A\), real \(a,b\), and strict interval \(|b|<a^2-1\). It makes no claim about all expansive rank-two shifts, the endpoints, arbitrary complex perturbations or higher-rank defects. In particular, the theorem is not a minimal-rank counterexample to the logarithmically concave CNP implication. General equivalent presentations of the example may exist in older shift-model or de Branges–Rovnyak literature; the exact family and two determinants have not been independently certified as new.

## References

- Shuaibing Luo and Eskil Rydhe, *Concave shifts and the complete Nevanlinna–Pick property*, arXiv:2611.12778v1, first posted 9 November 2026. https://arxiv.org/html/2611.12778v1
- Hamidul Ahmed, B. Krishna Das and Samir Panja, *de Branges-Rovnyak spaces which are complete Nevanlinna-Pick spaces*, arXiv:2403.19377, first posted 28 March 2024. https://arxiv.org/abs/2403.19377
- Cheng Chu, *Which de Branges-Rovnyak spaces have complete Nevanlinna-Pick property?*, arXiv:1910.04830, first posted 10 October 2019. https://arxiv.org/abs/1910.04830
- Shuaibing Luo and Eskil Rydhe, *On Dirichlet-type and n-isometric shifts in finite rank de Branges–Rovnyak spaces*, arXiv:2310.19393, first posted 30 October 2023. https://arxiv.org/abs/2310.19393
