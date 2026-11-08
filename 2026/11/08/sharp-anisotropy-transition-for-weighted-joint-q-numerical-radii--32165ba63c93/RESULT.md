# Sharp anisotropy transition for weighted joint \(q\)-numerical radii of a Pauli pair

## Finding

Put
\[
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix}
\]
on the complex Hilbert space \(\mathbb C^2\). For \(\alpha\ge\beta>0\), \(1\le p\le\infty\), and \(q\in\mathbb C\) with \(0<|q|<1\), define the weighted joint \(q\)-numerical radius
\[
R_{p,q}(\alpha,\beta)=
\sup_{\substack{\|x\|_2=\|y\|_2=1\\\langle x,y\rangle=q}}
\left\|\bigl(\alpha\langle Xx,y\rangle,
\beta\langle Yx,y\rangle\bigr)\right\|_{\ell_p^2}.
\]
Here the inner product is linear in its first variable, and the usual maximum-coordinate interpretation is used for \(p=\infty\). Write \(s=\sqrt{1-|q|^2}\). For \(1\le p<2\) put \(k=2p/(2-p)\). The **exact formula for every permissible parameter** is
\[
\boxed{
R_{p,q}(\alpha,\beta)=
\begin{cases}
\sqrt{1+s^2}\,(\alpha^k+\beta^k)^{1/k},
&1\le p<2\ \text{and}\ s\le(\beta/\alpha)^{p/(2-p)},\\[3pt]
(\alpha^p+\beta^p s^p)^{1/p},
&1\le p<2\ \text{and}\ s\ge(\beta/\alpha)^{p/(2-p)},\\[3pt]
(\alpha^p+\beta^p s^p)^{1/p},&2\le p<\infty,\\[3pt]
\alpha,&p=\infty.
\end{cases}}
\]
Both expressions agree at the transition. If \(1\le p<2\) and \(\alpha>\beta\), the maximizing geometry switches at the unique overlap
\[
\boxed{|q|=q_*(p,\alpha,\beta)
=\sqrt{1-(\beta/\alpha)^{2p/(2-p)}}.}
\]
For overlaps strictly larger than this, both Pauli coordinates contribute with an interior optimal allocation; for smaller overlaps, the larger-weight coordinate saturates at modulus one. In particular, for \(p=1\) the two branches are \(\sqrt{2-|q|^2}\sqrt{\alpha^2+\beta^2}\) and \(\alpha+\beta\sqrt{1-|q|^2}\), with threshold \(\sqrt{1-(\beta/\alpha)^2}\).

A precise equality allocation is available. Let \(a=|\langle Xx,y\rangle|^2\), \(b=|\langle Yx,y\rangle|^2\), and \(T=1+s^2\). For each finite \(p\), every extremizer satisfies \(a+b=T\). For \(1\le p<2\), its unique squared-modulus allocation is
\[
a=\min\left\{1,\frac{T\alpha^k}{\alpha^k+\beta^k}\right\},\qquad b=T-a.
\]
For \(p>2\) and \(\alpha>\beta\), the unique allocation is \((a,b)=(1,s^2)\); if \(\alpha=\beta\), either ordered endpoint is optimal. At \(p=2\), the same rule holds for unequal weights, while equal weights permit every allocation with \(a+b=T\). All stated allocations are attained by unit-vector pairs with the stipulated overlap. At \(p=\infty\), the radius equals \(\alpha\). If \(\alpha>\beta\), equality requires \(|\langle Xx,y\rangle|=1\); if \(\alpha=\beta\), equality requires at least one of the two Pauli numerical values to have modulus one. Other coordinates need not saturate the Parseval sum in these maximum-norm cases.

## Assumptions and scope

The matrices \(X,Y\) are the two anticommuting Hermitian Pauli unitaries displayed above. The Hilbert space has **complex** dimension two. The overlap is prescribed, not averaged or optimized, and has modulus strictly between zero and one. The parameter \(p\) is any real exponent at least one, including infinity. Nonnegative weights are not considered: both weights are strictly positive and may be relabeled so that \(\alpha\ge\beta\). This is a joint two-coordinate norm and not the \(q\)-numerical radius of a single linear combination of the two matrices. No assertion is made for non-Pauli operator pairs or arbitrary Hilbert dimensions.

## Proof

**Step 1: Two sharp universal constraints.** Set \(Z=\operatorname{diag}(1,-1)\). The four matrices \(I,X,Y,Z\), divided by \(\sqrt2\), form an orthonormal basis of the Hilbert–Schmidt space of complex two-by-two matrices. For unit \(x,y\), expand the rank-one matrix \(M=xy^*\) in this basis. Parseval's identity gives
\[
|\langle x,y\rangle|^2+
|\langle Xx,y\rangle|^2+
|\langle Yx,y\rangle|^2+
|\langle Zx,y\rangle|^2=2\|xy^*\|_{\rm HS}^2=2.
\]
Thus, with \(a=|\langle Xx,y\rangle|^2\), \(b=|\langle Yx,y\rangle|^2\),
\[
0\le a\le1,\quad 0\le b\le1,\quad a+b\le T:=2-|q|^2=1+s^2.
\tag{1}
\]
The individual upper bounds follow from the fact that \(X,Y\) are unitaries and \(x,y\) are unit vectors. These are inequalities for the actual pair and do not depend on a relaxed matrix completion.

**Step 2: Every point of the exposed allocation edge is attained.** Multiplying \(y\) by a unimodular scalar changes \(q\) and the two numerical values by the same unimodular factor. Consequently, it suffices to work at real \(q=r=|q|\), with \(s^2=1-r^2\). For any \(\theta\in[0,\pi/2]\), define
\[
u=\cos\theta+i s\sin\theta,\qquad
v=\sin\theta-i s\cos\theta.
\]
Direct calculation gives \(u^2+v^2=r^2\) and \(|u|^2+|v|^2=1+s^2\). The matrix
\[
M_\theta=\tfrac12(rI+uX+vY)
\]
has determinant \((r^2-u^2-v^2)/4=0\), trace \(r\), and Hilbert–Schmidt norm one, by the orthonormal Pauli expansion. Hence it is a rank-one matrix with sole nonzero singular value one, so \(M_\theta=xy^*\) for some unit vectors \(x,y\). Its trace ensures \(\langle x,y\rangle=r\), and taking traces against \(X,Y\) yields \(\langle Xx,y\rangle=u\) and \(\langle Yx,y\rangle=v\). Therefore
\[
a=|u|^2=s^2+r^2\cos^2\theta,
\qquad b=|v|^2=T-a.
\]
As \(\theta\) varies, \(a\) traverses the full interval \([s^2,1]\). Thus **every** allocation \((a,T-a)\) on the feasible top edge is realized, with the exact overlap, and the inequalities (1) introduce no gap in the optimization.

**Step 3: Reduction to a single strictly positive variable.** For finite \(p\), maximizing the joint norm is equivalent to maximizing \(\alpha^p a^{p/2}+\beta^p b^{p/2}\) subject to (1). Monotonicity in both variables ensures a maximum can be taken on the attained edge \(a+b=T\). All such maximizers are obtained by maximizing
\[
F(a)=\alpha^p a^{p/2}+\beta^p(T-a)^{p/2},\qquad s^2\le a\le1.
\tag{2}
\]
For \(1\le p<2\), \(F\) is strictly concave. Its unique unconstrained critical point satisfies
\[
\left(\frac{a}{T-a}\right)^{(2-p)/2}
=\left(\frac\alpha\beta\right)^p,
\quad\text{hence}\quad
 a_0=\frac{T\alpha^k}{\alpha^k+\beta^k},\quad k=\frac{2p}{2-p}.
\]
Since \(\alpha\ge\beta\), this point cannot fall below the left endpoint \(s^2\). It belongs to the allowed interval exactly when \(s\le(\beta/\alpha)^{p/(2-p)}\). In that case, substitution into (2) gives
\[
F(a_0)^{1/p}=\sqrt T\,(\alpha^k+\beta^k)^{1/k}.
\]
Otherwise the unique maximizer is the right endpoint \(a=1\), giving \((\alpha^p+\beta^p s^p)^{1/p}\). The threshold relation stated in the finding follows by solving the equality for \(|q|\).

For \(p=2\), (2) is affine in \(a\) and is maximal at \(a=1\) unless \(\alpha=\beta\), when it is constant. For \(p>2\), (2) is strictly convex, so its maximum lies at one of the two endpoints; because \(\alpha\ge\beta\), the endpoint \(a=1\) is optimal (strictly so if \(\alpha>\beta\)). Finally \(p=\infty\) yields \(\sup\max\{\alpha\sqrt a,\beta\sqrt b\}=\alpha\), since \(a=1\) is attainable. The claimed complete formulas and equality allocations follow.

## Verification

The proof reduces all quantifiers to exact identities and one-variable optimization on a fully realized edge. Critical checks are: Hilbert–Schmidt Parseval normalization (two, not one); the exact rank-one lifting through the determinant-zero matrix \(M_\theta\); continuity at the interior/saturated transition; and allocation uniqueness at exponent two. The standalone `verify.py` uses only the Python standard library and independently samples admissible vector pairs and the rank-one edge for many parameters. Run it using `python3 verify.py` from a directory containing the extracted file. It reports **11,997 finite diagnostic assertions passed**. These tests are diagnostics only; the universal result is established by the displayed proof.

## Relationship to prior work

Azadi (2026, arXiv:2610.32504) defines joint \(q\)-numerical ranges of operator-valued fields and proves compactness and realization statements, with the principal realization theorem restricted to unit-modulus overlap. The present statement instead optimizes an explicit noncommuting two-matrix field for interior overlap, two positive weights, and all \(\ell_p\) exponents. Feki, Patra, Rani and Taki (2024 preprint, 2026 publication, arXiv:2410.03669) give general joint \(q\)-numerical-radius inequalities and nonconvex two-by-two examples, and their Theorem 17 gives a generic block-matrix upper bound. Their inspected statements do not supply the exact anisotropic formula or its transition. Xu, Schwonnek and Winter (2024) investigate joint ranges of Pauli strings for ordinary state expectations; those are distinct from two-vector fixed-interior-overlap radii. General \(\ell_p\)-norm inequalities alone also do not imply the sharp crossover without the exact attained Pauli allocation edge.

## Limitations

The result is an exact theorem for the displayed two-dimensional anticommuting Pauli pair, not a claim about arbitrary noncommuting tuples, larger Clifford representations, or arbitrary weights on other matrix families. The proof is analytic and needs no external computation for its validity. Publication-priority risk remains from generalized \(C\)-numerical range or Clifford-orbitope work under different terminology, and a broader older result could imply the weighted formula even without naming this pair. No independent mathematical audit or priority certification has been performed.

## References

1. A. Azadi, *Joint q-Numerical Ranges of Continuous Operator-Valued Functions*, arXiv:2610.32504v1 (first submitted 2026-10-23), https://arxiv.org/abs/2610.32504 .
2. K. Feki, A. Patra, J. Rani, Z. Taki, *Joint q-Numerical Ranges of Operators in Hilbert and Semi-Hilbert Spaces*, arXiv:2410.03669 (first submitted 2024-09-12); *Linear and Multilinear Algebra* 74 (2026), 294–316, https://arxiv.org/abs/2410.03669 .
3. Z.-P. Xu, R. Schwonnek, A. Winter, *Bounding the Joint Numerical Range of Pauli Strings by Graph Parameters*, *PRX Quantum* 5 (2024), 020318, https://doi.org/10.1103/PRXQuantum.5.020318 .
