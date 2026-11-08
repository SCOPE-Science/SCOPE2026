# Integral reversal modules of path moment-angle complexes

## Finding
For every integer \(n\ge3\), take the simplicial path \(P_n\) with vertices \(1,\dots,n\) and edges \(\{i,i+1\}\). Let \(Z_n=(D^2,S^1)^{P_n}\) be its complex moment-angle space, and let \(s\) reverse the path's vertex labels, acting on \(Z_n\) by permuting disk-circle coordinates. Put \(G=\langle s\rangle\cong C_2\). Let \(\mathbb Z_+\), \(\mathbb Z_-\), and \(\mathbb Z[G]\) be respectively the trivial, sign, and regular integral \(G\)-lattices.

Define, for \(2\le k\le n\),
\[
 b_{n,k}=(k-1)\binom nk-(n-1)\binom{n-2}{k-2},\qquad
 a_n=\left\lfloor\frac{n-1}{2}\right\rfloor,
\]
and set \(N_{n,k}=\binom{a_n}{k/2}\) if \(k\) is even, and \(N_{n,k}=0\) if \(k\) is odd. Out-of-range binomial coefficients are zero. Then \(R_{n,k}=(b_{n,k}-N_{n,k})/2\) is a nonnegative integer, and the **entire integral cohomology representation** is
\[
 H^{k+1}(Z_n;\mathbb Z)\cong
 \begin{cases}
 \mathbb Z[G]^{\oplus R_{n,k}},&k\text{ odd},\\
 \mathbb Z[G]^{\oplus R_{n,k}}\oplus \mathbb Z_+^{\oplus N_{n,k}},&k\equiv2\pmod4,\\
 \mathbb Z[G]^{\oplus R_{n,k}}\oplus \mathbb Z_-^{\oplus N_{n,k}},&k\equiv0\pmod4.
 \end{cases}
\]
Here \(H^0(Z_n;\mathbb Z)=\mathbb Z_+\), and every other cohomology group not displayed is zero. All groups are free abelian. In particular the reversal character and the rational quotient Betti numbers are exactly
\[
 \operatorname{tr}(s\mid H^{k+1}(Z_n;\mathbb Q))
 =\begin{cases}(-1)^{k/2+1}\binom{a_n}{k/2},&k\text{ even},\\0,&k\text{ odd},\end{cases}
\]
\[
 b_{k+1}(Z_n/G;\mathbb Q)=\frac12\left(b_{n,k}+
 \operatorname{tr}(s\mid H^{k+1}(Z_n;\mathbb Q))\right).
\]
The total positive-degree rational Betti number of the quotient is \((n-3)2^{n-3}+1\). This is a classification of the **integral group-action lattice**, not just a formula for rational traces.

## Assumptions and scope
The pair \((D^2,S^1)\) uses the standard complex disk and its boundary circle, and \(P_n\) is regarded as a one-dimensional simplicial complex with all its vertices and the empty face. Coordinates are labeled by increasing vertex number. The involution \(s(i)=n+1-i\) exchanges entire coordinate factors; it does not conjugate complex coordinates. Cohomology is ordinary singular cohomology with the stated coefficients. Only the finite coordinate-permutation quotient \(Z_n/G\) is considered; it is not a torus quotient. No claim is made about an equivariant wedge-of-spheres homotopy splitting or integral cohomology of the quotient itself.

## Proof
**1. A signed, integral support decomposition.** Use the standard cellular differential graded algebra with generators \(u_i\) in degree one and \(v_i\) in degree two, \(du_i=v_i\), \(dv_i=0\), \(u_i^2=u_iv_i=v_i^2=0\), and \(v_\sigma=0\) unless \(\sigma\) is a face of \(P_n\). The products \(u_\omega v_\sigma\), where \(\omega\cap\sigma=\varnothing\), split the cochains by support \(I=\omega\sqcup\sigma\). For nonempty \(I\), the support-\(I\) complex is the augmented simplicial cochain complex of the induced forest \(P_n[I]\), shifted so that its reduced degree zero occurs in total cohomological degree \(|I|+1\). This equivalence holds over \(\mathbb Z\).

The equivariant signs are essential: the involution on the support-\(I\) summand acts as the induced action on augmented simplicial cochains, multiplied by the sign of the permutation of the ordered vertices of \(I\). To verify this directly, write \(r=|\sigma|\), and let \(\nu(\omega,\sigma)\) count inversions in the sequence consisting of the increasing list \(\omega\) followed by the increasing list \(\sigma\), relative to the increasing order of \(I\). Multiplying the basis vector \(u_\omega v_\sigma\) by
\[
 (-1)^{\nu(\omega,\sigma)+r(|I|-1)-r(r-1)/2}
\]
identifies its differential with the simplicial coboundary. Comparing the shuffle signs before and after any permutation of \(I\) proves the extra determinant-sign factor. In particular, an invariant support with \(j\) reversed vertex pairs has sign \((-1)^j\).

**2. Component lattices.** Since \(P_n[I]\) is a forest, its only potentially nonzero reduced cohomology is
\[
 \widetilde H^0(P_n[I];\mathbb Z)
 \cong \mathbb Z^{c(I)}/\mathbb Z(1,\ldots,1),
\]
where \(c(I)\) is the number of nonempty connected components. Hence the support contributes rank \(c(I)-1\) in degree \(|I|+1\), and no torsion. The empty support contributes \(H^0=\mathbb Z\). Supports not fixed by \(s\) occur in pairs and contribute \(\mathbb Z[G]^{\oplus(c(I)-1)}\) in their common degree.

For fixed \(I\), components of \(P_n[I]\) are either interchanged in pairs or one component containing the geometric midpoint of the path is fixed and all others are paired. In the second case, taking the paired component classes as a basis of the quotient by the diagonal gives an integral sum of regular modules; twisting by the determinant sign does not change its regular-module isomorphism type. In the first case there are \(2h\) components. Label the exchanged pairs \((A_i,B_i)\), for \(1\le i\le h\). In \(\mathbb Z^{2h}/\mathbb Z(1,\ldots,1)\), the elements \(A_i,B_i\) for \(i<h\), together with \(w=A_1+\cdots+A_h\), form an **integral basis**: the final \(A_h\) can be recovered from \(w\), and the final \(B_h\) from the diagonal relation. Reversal interchanges each earlier pair and sends \(w\) to \(-w\). Thus this lattice is \(\mathbb Z[G]^{\oplus(h-1)}\oplus\mathbb Z_-\), before the support-determinant twist. A fixed support without a central component has even cardinality \(k=2j\), so the twist changes the last line to eigenvalue \((-1)^{j+1}\).

**3. Counting and multiplicities.** For nonempty \(I\) with \(|I|=k\), the forest has \(c(I)=k-e(I)\), where \(e(I)\) counts induced edges. Across all such \(I\), every one of the \(n-1\) path edges belongs to \(\binom{n-2}{k-2}\) subsets. Summing \(c(I)-1\) gives precisely \(b_{n,k}\). A symmetric subset with no midpoint component must avoid the middle vertex when \(n\) is odd, or avoid the middle adjacent pair when \(n\) is even. There are \(a_n\) freely selectable mirrored vertex pairs, so exactly \(\binom{a_n}{j}\) such subsets have cardinality \(2j\). Each supplies one exceptional integral line, of the type in the theorem. All remaining rank lies in regular modules. Consequently their multiplicity is \(R_{n,k}\), automatically integral and nonnegative, which proves the stated full integral representation.

**4. Traces and finite quotient.** A regular \(G\)-lattice has reversal trace zero; the exceptional lines give the displayed binomial trace. For a finite group acting cellularly, rational cohomology of the underlying quotient is the invariant part of rational cohomology. Averaging the identity and reversal characters gives the quotient formula. Summing \(b_{n,k}\) over \(2\le k\le n\) gives \((n-3)2^{n-2}+1\), and summing the nonzero reversal traces gives \(1\) by the binomial theorem. Their half-sum is \((n-3)2^{n-3}+1\), as asserted.

## Verification
Run `python3 path_moment_verification.py` with Python 3 and no third-party dependencies. For every path length from 3 through 18, the program enumerates all support subsets (524,264 in total), derives independent component-module multiplicities, and compares their ranks and traces with the closed formulas. It separately computes signed cellular Lefschetz supertraces using the disk/circle cell dimensions. For lengths 3 through 10 it checks all signs in the explicit integral cochain identification, both for the differential and for reversal. Finite-field incidence-rank checks for lengths 3 through 9 corroborate the induced-forest part. These computations are finite cross-checks only; the uniform integral conclusion follows from the signed support isomorphism and the explicit unimodular component bases in the proof.

## Relationship to prior work
Buchstaber and Panov established the moment-angle and Koszul cochain framework; Bahri, Bendersky, Cohen and Gitler gave the additive polyhedral-product splitting. Grbić, Panov, Theriault and Wu identify wedge-of-spheres homotopy types for chordal flag complexes, including paths, and state their nonequivariant Betti numbers in terms of induced-component counts. Those foundational results are prerequisites, **not** claimed as new. The contribution here is the all-degree *integral* path-reversal module decomposition with explicit regular and one-dimensional multiplicities and the resulting finite coordinate-permutation quotient ranks. Li Yu's partition-associated quotients concern toral subgroup actions, a different quotient construction. General equivariant versions of polyhedral-product splittings may provide alternative derivations; no uniqueness or publication priority is claimed.

## Limitations
The formula concerns the complex pair \((D^2,S^1)\), simplicial paths, and their order-two coordinate-reversal action. It does not classify integral cohomology of the quotient, other graph automorphisms, generalized polyhedral products, or equivariant homotopy types. An equivalent closed-form integral classification could exist in unindexed or inaccessible literature. The result has not undergone independent mathematical audit.

## References
- V. M. Buchstaber and T. E. Panov, *Torus actions, equivariant moment-angle complexes, and coordinate subspace arrangements*, arXiv:math/9912199, first submitted 1999-12-24. https://arxiv.org/abs/math/9912199
- A. Bahri, M. Bendersky, F. R. Cohen, S. Gitler, *The polyhedral product functor: a method of computation for moment-angle complexes, arrangements and related spaces*, arXiv:0711.4689, first submitted 2007-11-29. https://arxiv.org/abs/0711.4689
- J. Grbić, T. Panov, S. Theriault, J. Wu, *Homotopy types of moment-angle complexes for flag complexes*, arXiv:1211.0873, first submitted 2012-11-05. https://arxiv.org/abs/1211.0873
- L. Yu, *On Hochster's formula for a class of quotient spaces of moment-angle complexes*, arXiv:1406.7392, first submitted 2014-06-28. https://arxiv.org/abs/1406.7392
