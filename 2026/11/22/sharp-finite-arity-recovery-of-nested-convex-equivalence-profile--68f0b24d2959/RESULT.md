# Sharp finite-arity recovery of nested convex-equivalence profiles over ordered rationals

## Finding
Fix an integer \(h\geq1\), and let \(L_h\) be the countable homogeneous dense linear order with \(h\) named nested convex equivalence relations, concretely \(\mathbb Q^{h+1}\) in lexicographic order. The finest equivalence \(E_1\) identifies points having their first \(h\) coordinates equal, and \(E_j\) identifies points having their first \(h+1-j\) coordinates equal. Let \(A\subset L_h\) be a nonempty finite pointwise-named set, with \(n=|A|\), and write \(m_j\) for the number of \(E_j\)-classes that meet \(A\). Thus \(n\geq m_1\geq\cdots\geq m_h\geq1\).

Let \(t_r(A)\) be the number of complete types of ordered injective \(r\)-tuples over \(A\), with every coordinate outside \(A\). Set \(t_0(A)=1\). The exponential generating function is
\[
F_A(z)=\sum_{r\geq0}\frac{t_r(A)}{r!}z^r
=(1-z)^{-n-m_1}\prod_{j=2}^{h}
\left(\frac{1-(j-1)z}{1-jz}\right)^{m_{j-1}+m_j}
\left(\frac{1-hz}{1-(h+1)z}\right)^{m_h+1}.
\]
In particular, the entire numerical spectrum is independent of the positions of all the named equivalence-class cuts. With \(b_r(A)=r[z^r]\log F_A(z)\), one has
\[
b_r(A)=n+(h+1)^r-h^r+\sum_{j=1}^{h}m_j\big((j+1)^r-(j-1)^r\big),\quad r\geq1.
\]
The first \(h\) type counts \(t_1(A),\ldots,t_h(A)\), together with \(n\), determine the full vector \((m_1,\ldots,m_h)\), hence every \(t_r(A)\). The bound \(h\) is universally sharp: for every \(h\), there are two same-size named bases with distinct complete numerical spectra agreeing through arity \(h-1\). Moreover the number of distinct order-and-equivalence isomorphism types of \(n\)-point bases with a fixed recovered \(m\)-vector equals
\[
\prod_{j=1}^{h}\binom{m_{j-1}-1}{m_j-1},\qquad m_0=n.
\]
Consequently distinct base isomorphism types with identical all-arity numerical spectra first arise on three points for every \(h\geq1\).

## Assumptions and scope
All equivalence relations are convex in the linear order; \(E_1\subseteq\cdots\subseteq E_h\), and all quotient orders and all equivalence classes are dense without endpoints. The structure \(L_h\) is the Fraïssé limit of finite linear orders carrying such nested convex equivalences. Parameters are individually named, not merely setwise preserved. Only tuples of distinct new elements, disjoint from the parameters, are counted. Equivalence classes meeting parameters and classes disjoint from parameters both have infinitely many points and are densely interspersed in the requisite quotient orders. All formulas hold for \(h\geq1\), \(n\geq1\), and every \(r\geq0\).

## Proof
**1. Finite extension diagrams are complete types.** In a homogeneous relational structure, an injective tuple outside a pointwise-named finite parameter set is classified by the finite induced ordered equivalence pattern on the union. Every finite compatible pattern is realized by the extension property of the homogeneous limit. In particular an order-preserving isomorphism between such finite patterns induces equality of complete tuple types.

**2. Counts of fresh classes.** Write \(B_j(z)\) for the exponential generating function of a nonempty freshly created \(E_j\)-class whose points and all lower-level subclasses are entirely outside the base; an \(E_0\)-class means one point. A fresh \(E_1\)-class is a nonempty ordered sequence of new points, whence \(B_1(z)=z/(1-z)\). For \(j\geq2\), a fresh \(E_j\)-class is a nonempty ordered sequence of fresh \(E_{j-1}\)-classes. Under labelled exponential enumeration,
\[
B_j(z)=\frac{B_{j-1}(z)}{1-B_{j-1}(z)}=\frac{z}{1-jz}.
\]
Thus an arbitrary (possibly empty) sequence of new \(E_{j-1}\)-classes has EGF \(1/(1-B_{j-1})=(1-(j-1)z)/(1-jz)\). An arbitrary sequence of new \(E_h\)-classes at the top has EGF \((1-hz)/(1-(h+1)z)\).

**3. Independence of cuts and full EGF.** Within a named \(E_1\)-class containing \(s\) points, there are exactly \(s+1\) gaps available for ordered sequences of new points. Summing over the \(m_1\) named finest classes gives \(n+m_1\) such gaps, contributing \((1-z)^{-n-m_1}\). For \(j=2,\ldots,h\), every named \(E_j\)-class containing \(s\) named \(E_{j-1}\)-classes has \(s+1\) gaps for sequences of entirely new \(E_{j-1}\)-classes. Across the \(m_j\) named \(E_j\)-classes the number of these gaps is \(m_{j-1}+m_j\), regardless of the distribution of \(s\). At the top there are \(m_h+1\) gaps for fresh \(E_h\)-classes. Multiplication of the independent labelled EGF factors proves the displayed \(F_A(z)\) for all arities, including \(r=0\).

**4. Moment inversion.** Expanding \(\log(1-cz)=-\sum_{r\geq1}c^rz^r/r\) in the product shows the displayed formula for \(b_r\). The coefficient of \(m_j\) in \(b_r\) is \(D_{rj}=(j+1)^r-(j-1)^r\). For fixed \(r\), \(D_{rj}\) is a polynomial in \(j\) of degree \(r-1\) and leading coefficient \(2r\). Evaluation at \(j=1,\ldots,h\) therefore gives the Vandermonde determinant
\[
\det(D_{rj})_{1\leq r,j\leq h}
=\left(\prod_{r=1}^{h}2r\right)\left(\prod_{1\leq i<j\leq h}(j-i)\right)
=2^h\prod_{r=1}^{h}r!\ne0.
\]
The formal logarithm coefficients through degree \(h\) are functions of precisely the first \(h\) coefficients of \(F_A\), so these counts uniquely recover \(m\). Conversely the factorization shows that \(m\) determines all counts.

**5. Sharpness and exact fibers.** For \(h\geq2\), the first \(h-1\) rows of the \(h\)-column matrix \(D\) have a nonzero rational kernel vector. Scale it to a nonzero integral vector \(v\). Choose integers \(n>m_1>\cdots>m_h\geq1\) with all gaps, including \(n-m_1\), much larger than \(\max_j|v_j|\). Both \(m\) and \(m+v\) then describe realizable same-size finite nested convex equivalence patterns, agree on all moments through \(h-1\), but differ at some higher arity because the full \(D\) matrix is invertible. For \(h=1\), two different \(m_1\) values on a two-point base already show that zero counts do not suffice. Each base pattern amounts exactly to an \((n-1)\)-gap word assigning a separation depth between consecutive old points, with depth at least \(j\) marking an \(E_j\)-cut. Choosing successively which \(m_j-1\) of the \(m_{j-1}-1\) finer cut sites remain at level \(j\) gives the stated product of binomial coefficients. For \(n\leq2\), each vector is represented by exactly one gap word, hence no numerical collision. For \(n=3\), the gap words \((1,0)\) and \((0,1)\) give nonisomorphic ordered bases with identical \((m_1,\ldots,m_h)=(2,1,\ldots,1)\), proving the first collision at three points for every \(h\).

## Verification
The included `verify.py` enumerates every order insertion of new labelled points and every admissible gap-depth assignment, independently checks restriction to the old base by taking maxima along merged gaps, and compares exact integer counts with the rational EGF through small sizes. It separately tests moment determinants against the closed product, complete small-base fiber multiplicities, and the first collision. The finite output is in `verification_output.txt`; these tests are supplementary to, not substitutes for, the all-size proof.

## Relationship to prior work
The classical Fraïssé and structural Ramsey framework includes the homogeneous ordered rational plane \((\mathbb Q^2,<_{\mathrm{lex}},E)\) and the associated order-preserving automorphism groups [1]. The general hierarchy of convexly ordered equivalences is also studied for big Ramsey degrees [2]. These sources justify the underlying natural homogeneous structures but do not supply the finite-point-stabilizer all-arity numeric EGF, its exact Vandermonde recovery cutoff, or the collision-fiber formula. Existing results on unmarked colored-gap ultrametric orbits, the countable grid with independent equivalences, and finite unordered nested equivalences involve different invariants and do not imply the present formulas [3–5]. The formulas are proved here directly; historical priority under other terminology is not fully settled.

## Limitations
The theorem is only about numerical counts of complete injective tuple types over a *pointwise*-named finite base, not equivalence of base diagrams or recovery of the placements of named equivalence-class boundaries. It requires convex nested equivalences and dense quotient and fiber orders; it does not transfer to arbitrary nested equivalence structures without order. The uniqueness cutoff assumes the base size \(n\) is known, and sharpness is universal over sufficiently large bases rather than asserted separately for every small \(n\). Historical-priority comparison is provisional.

## References
[1] A. S. Kechris, V. G. Pestov, S. Todorcevic, *Fraïssé Limits, Ramsey Theory, and Topological Dynamics of Automorphism Groups*, arXiv:math/0305241, first posted 2003-05-16. https://arxiv.org/abs/math/0305241

[2] R. Coulson, N. Dobrinen, R. Patel, *Fraïssé Classes with Simply Characterized Big Ramsey Structures*, arXiv:2010.02034, first posted 2020-10-05. https://arxiv.org/abs/2010.02034

[3] *Colored-gap orbit profiles for minimal chain ultrametric expansions*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-colored-gap-orbit-profiles-for-minimal-chain-ultrametric-expansi--d80a1c925594

[4] *Arity-two saturation and unbounded collisions in finite-base type spectra of the countable grid*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-arity-two-saturation-and-unbounded-collisions-in-finite-base-typ--801562567ff1

[5] *Sharp one-involution capacity for coloured nested equivalences*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-one-involution-capacity-for-coloured-nested-equivalences--4dcdd3147eb1
