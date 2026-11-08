# Exact singular spectrum and sharp conditioning of diagonal positive couplings of a shift pair

## Finding
Let \(U\) be the unilateral forward shift on \(H=\ell^2(\mathbb N_0)\). For a bounded strictly positive diagonal operator \(C e_j=c_j e_j\), where each \(c_j>0\), define
\[
 T_C=\begin{pmatrix}U&C\\0&U^*\end{pmatrix}\quad\text{on }H\oplus H,\qquad
 F(t)=\frac{\sqrt{t^2+4}+t}{2}.
\]
The entire singular spectrum, the inverse norm, the optimal conditioning under a uniform positivity constraint, and the Schatten proximity to a unitary operator are explicit:
\[
 \sigma(|T_C|)=\overline{\{c_0\}\cup\{F(c_j),F(c_j)^{-1}:j\ge1\}},\qquad
 \|T_C\|=\max\{c_0,F(d)\},\quad
 \|T_C^{-1}\|=\max\{c_0^{-1},F(d)\},
\]
where \(d=\sup_{j\ge1}c_j\). The spectrum formula concerns the positive modulus, not the eigenvalue spectrum of \(T_C\).

For every \(\mu>0\), the optimal Hilbert-space condition number over diagonal couplings satisfying \(C\ge\mu I\) is
\[
 \inf_{C\ge\mu I}\|T_C\|\,\|T_C^{-1}\|=F(\mu)^2.
\]
In contrast, restriction to scalar couplings \(C=cI\), with \(c>0\), gives the sharp and attained lower bound
\[
 \inf_{c>0}\|T_{cI}\|\,\|T_{cI}^{-1}\|=2,
 \qquad\text{uniquely at }c=1/\sqrt2.
\]
Among all strictly positive (not necessarily bounded below) diagonal couplings, the condition-number infimum is \(1\), but is not attained.

Let \(P_0\) be the rank-one projection onto \(\mathbb C e_0\), and define the unitary bridge
\[
 W=\begin{pmatrix}U&P_0\\0&U^*\end{pmatrix}.
\]
For every \(0<p<\infty\), including \(p<1\),
\[
 T_C-W\in\mathcal S_p\quad\Longleftrightarrow\quad
 |c_0-1|^p+\sum_{j\ge1}c_j^p<\infty;
\]
the nonzero singular values of this difference are precisely the nonzero members of \(\{|c_0-1|,c_1,c_2,\ldots\}\), with multiplicities.

## Assumptions and scope
The Hilbert space is complex \(\ell^2(\mathbb N_0)\); \(Ue_j=e_{j+1}\); \(U^*e_0=0\) and \(U^*e_{j+1}=e_j\). The sequence \((c_j)\) is bounded and each entry is strictly positive. Uniform positivity \(C\ge\mu I\) is required only in the specified extremal statement. No lower bound on \(\inf_jc_j\) is needed for invertibility of \(T_C\). Condition number means the product of operator norms. Schatten membership is classical on \(H\oplus H\). If an endpoint value appears only as a limit of the displayed singular magnitudes, it belongs to the spectrum of \(|T_C|\) but need not be an eigenvalue.

## Proof
Write \(v=v_0e_0+Uy\) uniquely, with \(y\in H\). Then direct substitution gives
\[
 T_C(u,v)=\big(c_0v_0e_0+U(u+Dy),y\big),\qquad De_j=c_{j+1}e_j.
\]
The domain and target changes of coordinates \((u,v)\leftrightarrow(v_0,u,y)\) and \((x,z)\leftrightarrow(x_0,U^*x,z)\) are unitary maps onto \(\mathbb C\oplus H\oplus H\). Thus \(T_C\) is **two-sided unitarily equivalent** (not claimed unitarily similar) to
\[
 [c_0]\oplus\begin{pmatrix}I&D\\0&I\end{pmatrix}
 \simeq[c_0]\oplus\bigoplus_{j\ge1}
 \begin{pmatrix}1&c_j\\0&1\end{pmatrix}.
\]
The inverse exists and is bounded since \(c_0>0\) and \(D\) is bounded, even if the diagonal entries of \(C\) tend to zero.

For \(t\ge0\), the characteristic polynomial of the positive \(2\times2\) Gram matrix of the triangular block is \(z^2-(2+t^2)z+1\). Its singular values are exactly \(F(t)\) and \(F(t)^{-1}\). Since \(F\) is continuous and strictly increasing on \([0,\infty)\), taking the direct sum proves the claimed spectrum, norm, and inverse norm. The inverse of the triangular block has the same two singular values; the scalar inverse block contributes \(c_0^{-1}\).

For \(C\ge\mu I\), necessarily \(d\ge\mu\), whence each of \(\|T_C\|\) and \(\|T_C^{-1}\|\) is at least \(F(d)\ge F(\mu)\). Equality is realized with \(c_j=\mu\) for every \(j\ge1\) and \(c_0=\max\{1,\mu\}\): here \(c_0\le F(\mu)\) and \(c_0^{-1}\le F(\mu)\). For scalar \(C=cI\), the product is \(F(c)\max\{c^{-1},F(c)\}\). The first branch \(F(c)/c\) decreases strictly in \(c\), while the second branch \(F(c)^2\) increases strictly. They meet exactly when \(F(c)=c^{-1}\), equivalent to \(c=1/\sqrt2\), where the product equals \(2\).

Since \(d>0\) for every strictly positive diagonal sequence, \(\|T_C\|\,\|T_C^{-1}\|\ge F(d)^2>1\). Taking \(c_0=1\) and \(c_j=\varepsilon>0\) for \(j\ge1\) yields condition number \(F(\varepsilon)^2\to1\), proving nonattained infimum \(1\). Choosing instead \(c_0=1\) and \(c_j=\varepsilon 2^{-j}\) for \(j\ge1\) gives the same limiting conditioning phenomenon while \(T_C-W\) belongs simultaneously to every positive Schatten class.

Finally \(W=T_{P_0}\) is unitary: for \(v=v_0e_0+Uy\), \(W(u,v)=(v_0e_0+Uu,y)\), an onto isometry. The difference \(T_C-W\) has a single nonzero off-diagonal corner \(C-P_0\). Its nonzero singular values are precisely the moduli of the entries on that diagonal, proving the Schatten criterion for every positive exponent, with no appeal to a triangle inequality in the quasi-Schatten range.

## Verification
The accompanying standalone `CHECK.py` uses exact rational arithmetic to verify finite coordinate identities, block Gram characteristic polynomials, scalar extremum comparisons, and the unitary bridge identities. These are finite checks; the infinite-dimensional statements follow from the displayed unitary coordinate changes and exact block spectral computation, not finite enumeration.

## Relationship to prior work
Ji and Wang, *Riccati Equations and the Third Problem of Halmos* (arXiv:2610.39605v1, 29 October 2026), prove invertibility and invariant-subspace existence for the much larger class of positive couplings \(C\) and Cowen–Douglas pairs \(A,A^*\). Their proof provides an abstract inverse formula and Riccati method but no exact singular-value spectrum or conditioning optimization for positive diagonal couplings of the unilateral shift. The present result does not strengthen their invariant-subspace theorem and is deliberately restricted to a particularly tractable shift-pair model. Its two-sided unitary reduction is elementary, so analogous formulas may exist in older weighted-shift or block-operator literature under different notation; the novelty claim is only best-knowledge.

## Limitations
The result does not extend its exact formulas to arbitrary nondiagonal positive couplings or to general Cowen–Douglas operators. Two-sided unitary equivalence determines singular values but not similarity-invariant eigenvalue or invariant-subspace structure. The spectral formula is for the positive modulus, not for the spectrum of the original nonnormal operator. External independent review and exhaustive publication-priority certification have not been performed.

## References
1. K. Ji and Z. Wang, *Riccati Equations and the Third Problem of Halmos*, arXiv:2610.39605v1 (29 October 2026), https://arxiv.org/abs/2610.39605.
2. J. Fang, B. Hou, C. Jiang and Y. Zhang, *The Invariant Subspace Problem and Rosenblum Operators II*, arXiv:2610.11202 (2026), https://arxiv.org/abs/2610.11202.
3. M. J. Cowen and R. G. Douglas, *Complex geometry and operator theory*, Acta Math. 141 (1978), 187–261, https://doi.org/10.1007/BF02545748.
