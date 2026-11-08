# Complete doubled-node decomposition of symmetric cubics in characteristic two

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\) and let \(n=4r\ge4\). Write \(R=k[x_1,\ldots,x_n]\) and let \(X\subset\mathbb P_k^{n-1}\) be the cubic hypersurface defined by the elementary symmetric polynomial \(f=e_3(x_1,\ldots,x_n)\). Let \(J=(\partial_1 f,\ldots,\partial_n f)\) be its homogeneous Jacobian ideal. For each \(S\subseteq\{1,\ldots,n\}\) of cardinality \(|S|\equiv1\pmod4\), choose \(i_0\in S\) and \(j_0\notin S\), and define

\[
I_S=\bigl(x_i-x_{i_0}: i\in S\setminus\{i_0\},\quad x_j-x_{j_0}:j\in S^c\setminus\{j_0\},\quad x_{j_0}^{2}\bigr).
\]

(The complementary index condition is expanded unambiguously below.) The Jacobian ideal has the **exact homogeneous primary decomposition**

\[
\boxed{\ J=\bigcap_{|S|\equiv1\ (\mathrm{mod}\ 4)} I_S\ }.
\]

In particular, \(J\) is saturated, and its projective singular scheme consists of \(2^{n-2}\) pairwise distinct length-two curvilinear points. Their reduced supports are exactly \(P_S=[\mathbf1_S]\). Each point is an ordinary quadratic double point of the cubic hypersurface in the characteristic-two tangent-cone sense. The total singular-scheme length is \(2^{n-1}\), and the homogeneous Jacobian coordinate ring is a complete intersection with Hilbert series

\[
\boxed{\ H_{R/J}(t)=\frac{(1+t)^{n-1}}{1-t}\ }.
\]

For example, \(n=8\) gives \(64\) ordinary double points, each with singular-scheme length \(2\), and \(n=12\) gives \(1024\) such points.

## Assumptions and scope
All claims hold over an algebraically closed field of characteristic exactly \(2\); there is no restriction on transcendence degree. The variable count is any positive multiple of four. The scheme is the projective hypersurface singular scheme, not merely the reduced critical locus. Euler's identity yields \(f=\sum_i x_i\partial_i f\) because \(3=1\) in characteristic \(2\), so the Jacobian ideal already includes the hypersurface equation scheme-theoretically.

Precisely, with \(S^c=\{1,\ldots,n\}\setminus S\), the displayed ideal means

\[
I_S=(\,x_i-x_{i_0}\ (i\in S\setminus\{i_0\}),\ x_j-x_{j_0}\ (j\in S^c\setminus\{j_0\}),\ x_{j_0}^{2}\,).
\]

Its isomorphism class and its actual ideal in \(R\) are independent of the representatives \(i_0,j_0\). The quotient \(R/I_S\cong k[a,b]/(b^2)\), with \(a=x_{i_0}\) and \(b=x_{j_0}\), is primary to the line prime \((x_i-x_{i_0},x_j:j\in S^c)\), and is saturated.

## Proof
**1. Set-theoretic critical points.** Put \(E_1=\sum_i x_i\) and \(E_2=\sum_{i<j}x_ix_j\). In characteristic \(2\), deleting the \(i\)-th variable yields

\[
g_i:=\partial_i f=E_2+x_iE_1+x_i^2. \tag{1}
\]

At a common zero, every \(x_i\) is a root of \(T^2+E_1T+E_2\). If \(E_1=0\), this quadratic has a unique root \(a\) over the algebraically closed field, so all coordinates equal \(a\). But \(g_i=\binom{n-1}{2}a^2=a^2\), since \(n\equiv0\pmod4\); hence \(a=0\), impossible projectively.

Thus \(E_1\ne0\) and the common quadratic has distinct roots \(a,b\), with \(a+b=E_1\) and \(ab=E_2\). Both occur: if there were only one coordinate value, \(E_1=na=0\). Let \(m\) be the number of \(a\)'s and \(l=n-m\) the number of \(b\)'s. The equality \(E_1=ma+lb=a+b\) forces \(m,l\) odd. Expanding \(E_2\) and using \(E_2=ab\) gives

\[
\binom m2 a^2+\binom l2 b^2=0. \tag{2}
\]

If \(m\equiv1\pmod4\), then \(l\equiv3\pmod4\), so (2) forces \(b=0\). If \(m\equiv3\pmod4\), then \(l\equiv1\pmod4\), so \(a=0\). Hence every nonzero projective critical point has one common nonzero coordinate value on a subset \(S\) with \(|S|\equiv1\pmod4\), and zero elsewhere. Conversely, at every \(P_S\) of this form, \(E_1=1\), \(E_2=0\), and equation (1) vanishes for each \(i\). Therefore these are exactly the geometric projective critical points.

**2. Complete intersection and degree.** Each \(g_i\) is quadratic, and \(\sum_i g_i=(n-2)E_2=0\) in characteristic \(2\). The projective zero set is finite and nonempty by Step 1, so \(\operatorname{ht}J=n-1\). A polynomial ring is Cohen–Macaulay; any \(n-1\) chosen gradient generators that generate an ideal of height \(n-1\) form a regular sequence. Thus \(J\) is a complete intersection of \(n-1\) quadrics. It is saturated (the one-dimensional graded quotient is Cohen–Macaulay), and its degree is \(2^{n-1}\). The same regular sequence proves the Hilbert-series formula.

**3. Primary pieces and equality.** For a given \(S\) let \(m=|S|\equiv1\pmod4\) and \(l=n-m\equiv3\pmod4\). Specialize the \(S\)-coordinates to \(a\) and all complementary coordinates to \(b\). The formulas \(E_1=a+b\) and \(E_2=ab+b^2\) then give \(g_i=b^2\) for *every* \(i\), whether \(i\in S\) or \(i\in S^c\). Consequently \(J\subseteq I_S\) for every \(S\). Each \(I_S\) has quotient \(k[a,b]/(b^2)\), so it is saturated and primary, and its projectivization has length \(2\) and reduced support \(P_S\). Distinct subsets give distinct supports.

Exactly one quarter of the \(2^n\) subsets have cardinality \(1\pmod4\): the odd subsets total \(2^{n-1}\), and taking complements (since \(4\mid n\)) bijects the congruence classes \(1\) and \(3\) modulo \(4\). Therefore there are \(2^{n-2}\) ideals \(I_S\), and the disjoint union of their projective schemes has total length \(2\cdot2^{n-2}=2^{n-1}\). The inclusion of saturated homogeneous ideals \(J\subseteq\bigcap_S I_S\) induces an inclusion of zero-dimensional projective schemes with equal lengths. It is equality scheme-theoretically; saturation then yields the displayed equality of homogeneous ideals. This also rules out any other embedded component.

**4. Smooth quadratic tangent cone.** At \(P_S\), the diagonal entries of the Hessian of \(f\) vanish. The off-diagonal entries are \(E_1+x_i+x_j\): they equal \(1\) if \(i,j\) belong to the same block \(S\) or \(S^c\), and \(0\) if they are in different blocks. Thus the full Hessian is block diagonal, with off-diagonal-one matrices of odd sizes \(m\) and \(l\). Its two-dimensional kernel is spanned by \(\mathbf1_S\) and \(\mathbf1_{S^c}\). After passing to an affine projective chart \(x_{i_0}=1\), the polar form of the quadratic tangent cone has rank \(n-2\) and one-dimensional radical generated by the common increment of all complementary coordinates. The quadratic form itself evaluates on this radical vector as \(\binom l2=1\) in \(k\), since \(l\equiv3\pmod4\). Hence there is no nonzero projective point on the quadratic tangent cone where all polar derivatives vanish. The projectivized tangent cone is a smooth quadric, establishing that each \(P_S\) is an ordinary double point in characteristic \(2\). Notice that its Jacobian local length is \(2\), not the characteristic-zero value \(1\): in characteristic \(2\) a smooth quadratic tangent cone in odd ambient tangent-space dimension has an anisotropic one-dimensional polar radical.

## Verification
The standalone Python 3 verifier `check.py` uses exact arithmetic over \(\mathbb F_2\). It exhaustively checks all \(2^n-1\) projective \(\mathbb F_2\)-points for \(n=4,8,12\), verifies the gradient-zero support and the cubic equation, checks the two-block derivative restrictions, and checks that the projective tangent-cone polar rank is \(n-2\) with nonvanishing quadratic value on its radical. Its observed output was:

```
n=4: GF(2) points=4; support, two-block restriction, Hessian and tangent cone PASS
n=8: GF(2) points=64; support, two-block restriction, Hessian and tangent cone PASS
n=12: GF(2) points=1024; support, two-block restriction, Hessian and tangent cone PASS
ALL_EXACT_FINITE_CHECKS_PASS
```

The infinite theorem, the scheme decomposition over arbitrary algebraically closed characteristic-two fields, and saturation all follow from Steps 1–4; the finite checks are not an infinite proof.

## Relationship to prior work
Ying Xie, *Derivative and multiplicity loci of elementary symmetric polynomials in positive characteristic* (arXiv:2610.00259v1, first publicly available 2026-09-24), proves the general dimension formulas and the generic local ring of the coordinate-axis components of this critical scheme. The paper explicitly leaves smaller-dimensional and embedded components, full primary decompositions, and global reducedness unresolved (Section 7). Here the full projective critical scheme is zero-dimensional and every noncoordinate component is determined; the doubly thickened noncoordinate points are not entailed by the published coordinate-generic ring statement. The point-count and complete primary decomposition constitute the extra result, not Xie's dimension or coordinate multiplicity formulas.

Ian Orzel, *Computing the Elementary Symmetric Polynomials in Positive Characteristics* (arXiv:2509.05009), studies general dimension bounds in this setting; the present exact characteristic-two primary decomposition is not among those bounds. Cafure–Matera–Privitelli, *Singularities of symmetric hypersurfaces and Reed–Solomon codes* (arXiv:1109.2265), supplies a broader partition-space/dimension framework, but not the present saturated doubled-point decomposition. These comparisons concern claim implications, not mere title matches; possible coverage under older terminology remains a residual historical-priority risk.

## Limitations
The proof assumes \(n\) is divisible by four, that the cubic has *unit coefficients* as the elementary symmetric polynomial, and that the base field is algebraically closed of characteristic two. It does not classify characteristic-two symmetric cubics when \(n\not\equiv0\pmod4\), other degrees, or arbitrary coefficient perturbations. The adjective ordinary refers to the smooth projectivized quadratic tangent cone in characteristic two, not to an identically reduced Jacobian scheme. Historical priority remains provisional, and no independent mathematical audit has been performed.

## References
1. Ying Xie, *Derivative and multiplicity loci of elementary symmetric polynomials in positive characteristic*, arXiv:2610.00259v1 (2026-09-24). https://arxiv.org/html/2610.00259v1
2. Ian Orzel, *Computing the Elementary Symmetric Polynomials in Positive Characteristics*, arXiv:2509.05009 (first submitted 2025-09-05). https://arxiv.org/html/2509.05009v3
3. A. Cafure, G. Matera, M. Privitelli, *Singularities of symmetric hypersurfaces and Reed–Solomon codes*, Advances in Mathematics of Communications 6 (2012), 69–94; arXiv:1109.2265. https://arxiv.org/abs/1109.2265
