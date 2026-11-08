# Equidimensional jets of the square-zero \(3\times3\) matrix scheme

## Finding

Let \(k\) be any field and let \(\mathscr X\) be the affine scheme cut out by the nine entries of \(X^2\) in the coordinates of a generic \(3\times3\) matrix \(X\). For every integer \(m\ge1\), write \(\mathscr J_m=(J_{m-1}(\mathscr X))_{\mathrm{red}}\). Thus geometric points of \(\mathscr J_m\) are square-zero matrices over \(k[t]/(t^m)\), and \(m\) denotes the **ring length**, not the conventional zero-based jet order.

**Theorem.** The scheme \(\mathscr J_m\) is geometrically equidimensional of dimension
\[
 4m+\left\lfloor\frac m2\right\rfloor,
\]
and has exactly \(\left\lfloor m/2\right\rfloor+1\) geometrically irreducible components. When \(m=2h\), the components are the closures of the exact entry-valuation strata \(0,\ldots,h-1\), together with the affine linear subspace of matrices divisible by \(t^h\). When \(m=2h+1\), the components are the closures of the exact entry-valuation strata \(0,\ldots,h\); the deeper affine subspace divisible by \(t^{h+1}\) lies in the last component. All assertions hold in every characteristic.

There is also an exact arithmetic formula over **every finite commutative chain ring** \(R\) of length \(m\) whose residue field has order \(q\). Define
\[
 N(q)=(q^2+q+1)(q^2-1),\qquad F_m(R)=\#\{X\in M_3(R):X^2=0\}.
\]
Then the answer depends only on \(m\) and \(q\), not on the characteristic or isomorphism type of \(R\):
\[
 F_{2h}=q^{9h}+hN(q)q^{9h-4}\quad(h\ge1),
 \qquad F_{2h+1}=q^{9h}\bigl(1+(h+1)N(q)\bigr)\quad(h\ge0).
\]
With the formal convention \(F_0=1\), the length-generating function is
\[
 \sum_{m\ge0}F_mT^m=
 \frac{1+T}{1-q^9T^2}+
 \frac{N(q)(T+q^5T^2)}{(1-q^9T^2)^2}.
\]
The arithmetic identity is a companion calculation; the geometric jet-component classification is the principal assertion.

## Assumptions and scope

A finite commutative chain ring here means a commutative local principal ideal ring with nilpotent maximal ideal \((\pi)\), satisfying \(\pi^m=0\ne\pi^{m-1}\) for \(m>1\), and residue field \(R/(\pi)\cong\mathbb F_q\). For \(m=1\), \(R\) is the residue field. Its length-\(a\) quotient is \(R_a=R/(\pi^a)\); every successive quotient has \(q\) elements. The geometric assertions concern the **reduced underlying** schemes of jets of the scheme defined by the quadratic equations \(X^2=0\), not the jets of its reduced base variety. Scheme-theoretic multiplicities are not asserted. Entry-valuation means \(\nu(X)=\min_{i,j}\nu(x_{ij})\), truncated at \(m\), with \(\nu(0)=m\).

## Proof

**1. Normal form at a nonzero residue.** Suppose \(X\in M_3(R)\) satisfies \(X^2=0\) and its reduction modulo \((\pi)\) is nonzero. Its residue has rank one and Jordan type \((2,1)\). Choose \(w\in R^3\) with \(u=Xw\) such that \(\bar w,\bar u\) are independent, and complete \(u,w\) to an \(R\)-basis with \(v\). Write \(Xv=a u+bw+cv\). Then \(Xu=0\) and \(Xw=u\), so \(X^2v=0\) yields \(b+ca=0\), \(cb=0\), and \(c^2=0\). Replacing \(v\) by \(v-aw\) gives \(X(v-aw)=c(v-aw)\). Thus
\[
 X\sim J_2(0)\oplus[c],\qquad
 J_2(0)=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad c^2=0.
\]
The scalar \(c\) is the trace of \(X\), hence is a complete conjugacy parameter among such primitive solutions. In a finite chain ring, \(c^2=0\) precisely when \(c\in(\pi^{\lceil m/2\rceil})\), giving \(q^{\lfloor m/2\rfloor}\) parameters.

**2. Centralizers and the primitive count.** For \(X_c=J_2(0)\oplus[c]\), every commuting matrix has the unique form
\[
 Y=\begin{pmatrix}a&b&u\\0&a&cu\\cv&v&d\end{pmatrix},
 \quad a,b,u,v,d\in R.
\]
This follows by multiplying \(YX_c=X_cY\), using \(c^2=0\). Invertibility is equivalent to \(a,d\in R^\times\). Thus the invertible centralizer has size \(q^{5m-2}(q-1)^2\). Since \(\#GL_3(R)=q^{9(m-1)}\#GL_3(\mathbb F_q)\), every such conjugacy orbit has exactly \(N(q)q^{4(m-1)}\) points. Different \(c\) give disjoint orbits by trace. Therefore the primitive locus, where the residue matrix is nonzero, has exactly
\[
 P_m=N(q)q^{4(m-1)+\lfloor m/2\rfloor}
\]
points. The argument works without any characteristic restriction and for mixed-characteristic chain rings.

**3. Divisible branch and arithmetic solution.** Every solution not in the primitive locus is uniquely of the form \(X=\pi Y\) with \(Y\) defined modulo \(\pi^{m-1}\). When \(m\ge2\), the condition \(X^2=0\) is equivalent to \(Y^2=0\) modulo \(\pi^{m-2}\). Every such reduced \(Y\) has \(q^9\) lifts modulo \(\pi^{m-1}\). Hence
\[
 F_m=P_m+q^9F_{m-2}\quad(m\ge2),\qquad F_0=1,\quad F_1=1+N(q).
\]
Solving this recurrence separately at even and odd lengths gives the displayed closed forms and generating function. Notice that \(m=2h\) has both an unrestricted deep branch of size \(q^{9h}\) and \(h\) primitive-type contributions, whereas \(m=2h+1\) has \(h+1\) primitive-type contributions and a smaller deep branch.

**4. Irreducibility of each geometric valuation stratum.** Now take \(R_m=k[t]/(t^m)\) and base-change to an algebraic closure. In the primitive length-\(\ell\) locus, the trace parameter \(c\) satisfies \(c^2=0\) and has precisely \(\lfloor\ell/2\rfloor\) free coefficients (the others vanish on the reduced underlying space). The conjugation morphism
\[
 GL_3(R_\ell)\times\mathbb A^{\lfloor\ell/2\rfloor}
 \longrightarrow\{\text{primitive square-zero matrices over }R_\ell\}
\]
is surjective on geometric points by Step 1, and its fibers are centralizers of dimension \(5\ell\) by Step 2. The domain is geometrically irreducible. Therefore the reduced primitive locus is geometrically irreducible of dimension \(9\ell+\lfloor\ell/2\rfloor-5\ell=4\ell+\lfloor\ell/2\rfloor\).

For \(0\le j<\lceil m/2\rceil\), the locus \(S_j\) of exact entry-valuation \(j\) consists of matrices \(t^jY\), where \(Y\) is primitive modulo \(t^{m-j}\), and \(Y^2=0\) modulo \(t^{m-2j}\). Reducing \(Y\) modulo \(t^{m-2j}\) has an affine space of dimension \(9j\) as fiber. Consequently \(S_j\) is geometrically irreducible of dimension
\[
 4(m-2j)+\left\lfloor\frac{m-2j}{2}\right\rfloor+9j
 =4m+\left\lfloor\frac m2\right\rfloor.
\]
The residual deep locus \(D=\{X:t^{\lceil m/2\rceil}\mid X\}\) is affine of dimension \(9\lfloor m/2\rfloor\), and all its points automatically satisfy \(X^2=0\). When \(m=2h\), \(\dim D=9h=4m+\lfloor m/2\rfloor\). When \(m=2h+1\), \(\dim D=9h<9h+4\). Every point \(t^{h+1}Z\) of the latter deep locus is a specialization from \(S_h\): choose \(J_2(0)\oplus0\) in \(M_3(k)\) and set \(X_s=t^h(sJ+tZ)\), which is square zero modulo \(t^{2h+1}\), primitive at valuation \(h\) for \(s\ne0\), and equals \(t^{h+1}Z\) at \(s=0\). Hence \(D\subset\overline{S_h}\) in odd length.

The finitely many locally closed, pairwise disjoint \(S_j\) are each dense and open in their irreducible closures. Their distinct closures cannot coincide, because an irreducible topological space cannot contain two disjoint nonempty open dense subsets. They have equal dimension, so none can contain another. At even length \(D\) is a further distinct irreducible closed subset of the same dimension; at odd length it contributes no new component. Their union is all of the reduced jet scheme. This proves the geometric component count and equidimensionality.

## Verification

Run the three standalone checks from the package directory: compile `check_squarezero_jets.cpp` and `check_mixed_chain.cpp` with a C++17 compiler, and run `check_normal_form_centralizers.py` with Python 3. The packaged output files record exact execution. The finite-field checker enumerates all candidates whose residue can satisfy the equation, then tests all nine entries of the square of each complete truncated-polynomial matrix. It covers \(\mathbb F_2\) at lengths \(1,2,3\), \(\mathbb F_3\) at lengths \(1,2\), and \(\mathbb F_5\) at length \(1\). The mixed-characteristic checker exhaustively tests matrices over \(\mathbb Z/4\mathbb Z\), \(\mathbb Z/8\mathbb Z\), and \(\mathbb Z/9\mathbb Z\). A separate exhaustive check enumerates centralizer matrices over \(\mathbb F_2[t]/(t^2)\) for both square-zero trace parameters and tests their units. These tests validate finite cases only; the unbounded assertions are proved in the preceding steps.

## Relationship to prior work

Avni, Onn, Prasad and Vaserstein classify similarity classes of arbitrary \(3\times3\) matrices over local principal ideal rings; their extensive classification and centralizer theory is acknowledged as general background for the arithmetic part. That paper does not state the geometric component classification of the reduced jets of the **nonreduced quadratic square-zero scheme**. Yuen studies jets of determinantal varieties defined by minors, whereas the present defining ideal consists of entries of \(X^2\); neither the schemes nor their jet schemes are the same. Moreau and Yu study jet schemes of **reduced nilpotent orbit closures**, principally over characteristic zero. The present scheme is nonreduced already along its generic nonzero square-zero locus, and the result applies in every characteristic. None of those inspected source statements provides the full equidimensional component theorem proved here. The possibility of an unlocated general theorem about jets of nonreduced representation schemes remains a historical-priority risk.

## Limitations

The geometric result concerns reduced underlying jets, not their scheme-theoretic multiplicities, singular strata, or intersections. The arithmetic part counts matrices satisfying \(X^2=0\) over **finite chain rings**, not matrices satisfying higher nilpotence powers or over arbitrary non-chain finite rings. The equivalence of the formulas to any unlocated broader classification has not been independently certified. No mathematical assertion is made about matrix sizes other than three.

## References

1. C. Yuen, *Jet schemes of determinantal varieties*, arXiv:math/0608632v1 (publicly posted 2006-08-25), especially introduction and Section 5. https://arxiv.org/abs/math/0608632
2. N. Avni, U. Onn, A. Prasad, L. Vaserstein, *Similarity classes of 3x3 matrices over a local principal ideal ring*, arXiv:0708.1608v1 (2007-08-12), especially Sections 3–5. https://arxiv.org/abs/0708.1608
3. A. Moreau and R. W. T. Yu, *Jet schemes of the closure of nilpotent orbits*, arXiv:1411.6427v1 (2014-11-24), Sections 1 and 6. https://arxiv.org/abs/1411.6427
