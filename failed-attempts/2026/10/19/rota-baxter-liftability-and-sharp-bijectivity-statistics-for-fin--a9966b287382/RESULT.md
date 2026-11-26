# Rota–Baxter liftability and sharp bijectivity statistics for finite Heisenberg skew braces

## Finding

For every **odd prime** \(p\), put \(F=\mathbb F_p\), \(V=F^2\), and \(\omega((x,y),(u,v))=xv-yu\). Let \(H=V\times F\) be the Heisenberg group with
\[
(v,z)(w,t)=(v+w,z+t+\tfrac12\omega(v,w)).
\]
For each \(A\in M_2(F)\), the group operation
\[
(v,z)\circ_A(w,t)=(v+w,z+t+\tfrac12\omega(v,w)+\omega(Av,w))
\]
defines a skew brace \(\mathcal B_A=(H,\cdot,\circ_A)\). These are \(p^4\) pairwise distinct operations on the fixed labelled group.

**Complete liftability and fiber theorem.** Exactly the following maps are group Rota–Baxter operators \(B:H\to H\):
\[
B_{A,k,\ell}(v,z)=\left(Av,\;kz+\ell(v)-\tfrac{k}{2}\omega(Av,v)\right),
\qquad \det A=k(1+\operatorname{tr}A),
\]
where \(A\in M_2(F)\), \(k\in F\), \(\ell\in V^*\); this parametrization is unique. The associated brace is \(\mathcal B_A\). The number of Rota–Baxter lifts of \(\mathcal B_A\) equals
\[
\begin{cases}
p^2,&1+\operatorname{tr}A\ne0,\\
p^3,&1+\operatorname{tr}A=0=\det A,\\
0,&1+\operatorname{tr}A=0\ne\det A.
\end{cases}
\]
Here the last case means \(1+\operatorname{tr}A=0\) and \(\det A\ne0\). Thus exactly \(p^4-p^3+p^2+p\) of the \(p^4\) braces admit such a lift, and the total number of Rota–Baxter operators on \(H\) is \(p^6+p^4\).

Moreover, \(\mathcal B_A\cong\mathcal B_C\) as skew braces if and only if \(A\) and \(C\) are similar over \(F\). There are exactly \(p^2\) isomorphism types among the liftable braces and exactly \(p\) types among the nonliftable braces in this family.

**Sharp dual-bijectivity census.** Define \(\widetilde B(g)=g^{-1}B(g^{-1})\). Among all \(p^6+p^4\) Rota–Baxter operators on \(H\), the four disjoint classes, determined by whether \(B\) and \(\widetilde B\) are bijections, have sizes:
\[
\begin{array}{c|c}
(B\text{ bijective},\;\widetilde B\text{ bijective})&p^6-3p^5+4p^3\\
(B\text{ bijective},\;\widetilde B\text{ not})&p^5-2p^3\\
(B\text{ not},\;\widetilde B\text{ bijective})&p^5-2p^3\\
(B\text{ not},\;\widetilde B\text{ not})&p^5+p^4
\end{array}
\]
Consequently, the proportion for which both are bijections tends to \(1\) as \(p\) grows through odd primes.

## Assumptions and scope

Here a group Rota–Baxter operator means a map satisfying \(B(g)B(h)=B(gB(g)hB(g)^{-1})\) for **all** \(g,h\in H\). The group has order \(p^3\). The calculations are over prime fields of odd characteristic; no statement for characteristic two, prime-power fields with nonprime cardinality, or the second extraspecial group of order \(p^3\) is implied. The brace family fixes the original multiplication of \(H\). Isomorphisms of braces must preserve both group operations; they are not merely bijections of the underlying set.

## Proof

**1. The braces.** Conjugation by \((Av,0)\) sends \((w,t)\) to \((w,t+\omega(Av,w))\). The operation \(\circ_A\) is associative because its central correction is bilinear in \(v,w\), has the same identity, and has inverses. Its lambda map is this inner conjugation. Since lambda depends only on the quotient coordinate \(v\) and the quotient of \((H,\circ_A)\) is the additive group \(V\), the lambda homomorphism condition and the skew-brace relation hold. Nondegeneracy of \(\omega\) makes different matrices give different operations.

**2. Every group Rota–Baxter map preserves the center.** The defining identity gives \(B(1)=1\) and \(B(gz)=B(g)B(z)\) for central \(z\), so the restriction of \(B\) to \(Z(H)\) is a homomorphism. For a central generator \(z\), suppose \(u=B(z)\) has nonzero image \(\overline u\) in \(V\). Choose \(h\) with \([u,h]=z^j\), \(j=\omega(\overline u,\overline h)\ne0\). Applying the identity with \(g=z\) and using the central-shift rule yields \(u B(h)=B(h)u^{1+j}\). Modulo the center this says \(j\overline u=0\), a contradiction. Thus \(B(Z(H))\subseteq Z(H)\).

**3. General form.** The induced map on \(H/Z(H)=V\) is additive: the Rota–Baxter argument \(gB(g)hB(g)^{-1}\) has quotient coordinate \(v+w\). Because \(F\) is a prime field, this map is \(F\)-linear, say \(A\). On the center write \(B(0,z)=(0,kz)\). The central-shift relation implies \(B(v,z)=(Av,kz+\phi(v))\) for some function \(\phi:V\to F\). Evaluating the defining identity on \((v,0),(w,0)\) gives
\[
\phi(v+w)-\phi(v)-\phi(w)
=\tfrac12\omega(Av,Aw)-k\omega(Av,w)-\tfrac{k}{2}\omega(v,w).
\]
Interchanging \(v,w\), using \(\omega(Av,Aw)=\det(A)\omega(v,w)\) and
\(\omega(Av,w)+\omega(v,Aw)=\operatorname{tr}(A)\omega(v,w)\), proves the **necessary** condition \(\det A=k(1+\operatorname{tr}A)\). When it holds, the right side is the polarization of \(v\mapsto-\tfrac{k}{2}\omega(Av,v)\). The difference is additive, hence a unique linear \(\ell\in V^*\). Conversely, substitution shows every displayed map satisfies the identity. Its induced brace is \(\mathcal B_A\).

**4. Lift fibers, labelled counts, and isomorphism types.** For \(1+\operatorname{tr}A\ne0\), the determinant relation specifies exactly one \(k\), with \(p^2\) independent choices of \(\ell\). When \(\operatorname{tr}A=-1\), it has \(p\) choices of \(k\) if \(\det A=0\), and none otherwise. For every prescribed trace \(t\) and determinant \(d\), the number of \(2\)-by-\(2\) matrices is
\[
M_p(t,d)=p\bigl(p+\chi(t^2-4d)\bigr),
\]
where \(\chi(0)=0\). Indeed, write \(A=\begin{psmallmatrix}a&b\\c&t-a\end{psmallmatrix}\); for each \(a\), the equation \(bc=a(t-a)-d\) has \(2p-1\) solutions when its right side is zero and \(p-1\) otherwise. The resulting quadratic has \(1+\chi(t^2-4d)\) roots. Hence precisely \(p(p+1)\) matrices have \(\operatorname{tr}A=-1\), \(\det A=0\). This proves both the liftable-brace count \((p-1)p^3+p(p+1)=p^4-p^3+p^2+p\) and the operator count
\[
(p^4-p^3)p^2+p(p+1)p^3=p^6+p^4.
\]
Every automorphism of \(H\) has the form \((v,z)\mapsto(Pv,\det(P)z+\lambda(v))\) for \(P\in\mathrm{GL}_2(F)\) and \(\lambda\in V^*\). Transport of \(\circ_A\) gives \(\circ_{PAP^{-1}}\). The similarity classes of \(2\)-by-\(2\) matrices have total number \(p^2+p\): each trace/determinant pair has one non-scalar class, and each of the \(p\) repeated-root pairs has an additional scalar class. In the nonliftable locus \(t=-1,d\ne0\), each of its \(p-1\) determinant values gives one class, except \(d=1/4\) gives two. Thus exactly \(p\) classes are nonliftable and \(p^2\) liftable.

**5. Simultaneous bijectivity.** The map \(B_{A,k,\ell}\) is bijective exactly when \(k\ne0\) and \(\det A\ne0\). Its dual has quotient matrix \(-I-A\) and center scalar \(-1-k\), so it is bijective exactly when \(1+k\ne0\) and \(\det(I+A)\ne0\). Under the determinant relation,
\(\det(I+A)=1+\operatorname{tr}A+\det A=(1+k)(1+\operatorname{tr}A)\).
All matrices with \(\operatorname{tr}A=-1,\det A=0\) give neither bijection, contributing \(p^5+p^4\) operators. For the other traces, the singularities \(\det A=0\) and \(\det A=-(1+\operatorname{tr}A)\) are distinct; they give exactly one bijective member of the pair. The count of matrices on which both are bijective is
\[
\sum_{t\ne-1}\bigl[p^3-M_p(t,0)-M_p(t,-1-t)\bigr]
=p^4-3p^3+4p,
\]
because \(t^2\) and \((t+2)^2\) are the two discriminants and each vanishes at exactly one allowed trace. Multiplying by the \(p^2\) choices of \(\ell\) yields \(p^6-3p^5+4p^3\). Each of the two single-bijective cases has \(p^5-2p^3\) operators, by the same trace sums (or the involution \(B\mapsto\widetilde B\)); the four totals sum to \(p^6+p^4\).

## Verification

The accompanying `verify.py` is a Python 3 standard-library checker. Run `python3 verify.py`. It enumerates all matrix parameters for \(p=3,5,7,11\), compares the full four-cell dual-bijectivity counts with the closed formulas, and for \(p=3\) checks the group Rota–Baxter identity on **every pair** of elements for **every one** of the \(810\) parametrized operators. It directly tests the images of \(B\) and \(\widetilde B\). It also counts all liftable braces and matrix-similarity orbits for \(p=3,5\). The exact finite checks supplement but do not replace the proofs for arbitrary odd primes.

## Relationship to prior work

Savelyev's 2026 classification of Rota–Baxter operators on the finite Heisenberg group supplies the underlying structural setting and investigates simultaneous bijectivity. The general matrix constraint is consistent with that classification; **it is not claimed as a new discovery in isolation**. The additional conclusions here are the complete fiber cardinalities over the natural \(p^4\) inner-brace family, its exact liftable/unliftable isomorphism-type census, the total labelled operator census, and sharp four-cell bijectivity distribution and limit.

Caranti–Stefanello's 2022 cohomological characterization proves a general obstruction to inner skew-brace liftability and exhibits a scalar one-parameter Heisenberg example with a nonliftable point. Their separate brace-block construction covers existence of operations of the form \(\circ_A\). These prior results are not presented as absent: the new contribution is the explicit **all-matrices** realizability/fiber and isomorphism distribution coupled to the precise dual-bijectivity census. Rathee's 2024 work addresses related Heisenberg structures over complex scalars, rather than these finite-prime-field enumerations.

## Limitations

This is a classification **within the \(p^4\) inner-conjugation brace family**, not a classification of all skew braces on a group of order \(p^3\). It does classify every brace induced by a group Rota–Baxter map on this particular \(H\), because every such map has quotient matrix \(A\). It does not calculate Rota–Baxter conjugacy classes or treat non-Heisenberg extraspecial groups. The counting and isomorphism consequences are derived from a previously known structural setting; the existence of an equivalent complete enumeration in unindexed literature remains a bibliographic risk.

## References

1. A. Savelyev, *Rota—Baxter operators on extraspecial groups*, arXiv:2608.28291 (first public version 2026-08-28), https://arxiv.org/abs/2608.28291.
2. A. Caranti and L. Stefanello, *Skew braces from Rota–Baxter operators: a cohomological characterisation and some examples*, arXiv:2201.03936 (2022), https://arxiv.org/html/2201.03936v6.
3. A. Caranti and L. Stefanello, *Brace blocks from bilinear maps and liftings of endomorphisms*, arXiv:2110.11028 (2021; Journal of Algebra 2022), https://arxiv.org/html/2110.11028v4.
4. N. Rathee, *Rota–Baxter operators and skew left brace structures over Heisenberg Group*, arXiv:2402.15428 (2024), https://arxiv.org/abs/2402.15428.
