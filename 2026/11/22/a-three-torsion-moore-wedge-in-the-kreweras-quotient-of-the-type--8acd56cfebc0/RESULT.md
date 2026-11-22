# A three-torsion Moore wedge in the Kreweras quotient of the type-\(D_4\) noncrossing complex

## Finding
Let \(W=W(D_4)\) be the even-signed-permutation Coxeter group, and let \(c\) be the specific Coxeter element of order six described below. Let \(\mathrm{NC}(W,c)=[1,c]\) be its absolute-order noncrossing partition lattice, and let \(X=\Delta(\mathrm{NC}(W,c)\setminus\{1,c\})\). Kreweras complementation \(\kappa(w)=w^{-1}c\) is an order-reversing automorphism and induces a simplicial action on \(X\). Its effective order is six. The **ordinary geometric orbit space** satisfies the complete homotopy classification

\[
|X|/\langle\kappa\rangle\simeq M(\mathbb Z/3\mathbb Z,1)\vee S^2\vee S^2,
\]

where \(M(\mathbb Z/3\mathbb Z,1)=S^1\cup_{\deg 3} e^2\). In particular, \(\pi_1\cong H_1(-;\mathbb Z)\cong\mathbb Z/3\mathbb Z\), \(H_2(-;\mathbb Z)\cong\mathbb Z^2\), and all higher integral homology vanishes.

## Assumptions and scope
A signed permutation is a tuple \(w=(w(1),w(2),w(3),w(4))\) with distinct absolute values \(1,2,3,4\) and an even number of negative entries; extend by \(w(-i)=-w(i)\), and multiply by composition \((uv)(i)=u(v(i))\). The four simple reflections, listed in the order used to form the Coxeter element, are

\[
(-2,-1,3,4),\quad(2,1,3,4),\quad(1,3,2,4),\quad(1,2,4,3),
\]

so that \(c=(-1,3,4,-2)\). Let \(T\) be the twelve signed pair-exchange reflections, including the simultaneous sign-negated exchange for each unordered coordinate pair. Define \(\ell_T(w)\) as shortest word length in \(T\), and

\[
\mathrm{NC}(W,c)=\{w:\ell_T(w)+\ell_T(w^{-1}c)=4\},\qquad
u\le_T v\iff\ell_T(u)+\ell_T(u^{-1}v)=\ell_T(v).
\]

The order-reversing symmetry of the *poset order* is the Kreweras map \(\kappa(w)=w^{-1}c\), not conjugation alone; the latter is the square of the former up to choice of inverse. The asserted quotient is the quotient of the geometric realization. Merely identifying orbit vertices in the original order complex would not give its correct cell structure.

## Proof
**1. Finite Coxeter interval.** Breadth-first traversal from the identity using all twelve reflections produces every element of the order-\(192\) even-signed-permutation group, and gives exact reflection length. The interval predicate above selects precisely \(50\) elements, with rank distribution \((1,12,24,12,1)\). This agrees independently with the type-\(D\) Narayana formula of Athanasiadis–Reiner. Removing the endpoints gives \(48\) vertices and strict-rank chain counts \((48,189,162)\) in simplex dimensions zero, one and two. Direct exhaustive testing confirms that \(\kappa\) maps the interval to itself and reverses every comparison. Of the proper elements, \(42\) have complement-period six and \(6\) period three, proving effective action order six.

**2. Genuine orbit CW complex.** Barycentrically subdivide \(X\). A vertex of this subdivision is a nonempty face of \(X\), and a simplex is an inclusion chain of faces of strictly increasing sizes. Because the action preserves face sizes, no symmetry can permute vertices within such a simplex; the quotient has one regular open cell per orbit of face flags. The unsubdivided face counts \((48,189,162)\) yield barycentric face counts \((399,1350,972)\). Enumerating all complement orbits of these flags gives quotient cells

\[
(f_0,f_1,f_2)=(72,231,162),\qquad\chi=72-231+162=3.
\]

The oriented boundary of a flag is the usual alternating sum of shorter flags, then passed to flag orbits. No averaging or division by stabilizers occurs. The constructed signed matrices have zero consecutive product.

**3. Collapse to a one-vertex presentation complex.** A spanning tree in the quotient one-skeleton has \(71\) edges. Collapsing it is a homotopy equivalence, leaving one vertex, \(160\) loop edges and \(162\) two-cells. For an oriented flag triangle \((a\subset b\subset d)\), its attaching word is the edge from \(a\) to \(b\), followed by \(b\) to \(d\), then the inverse edge from \(a\) to \(d\); tree edges contribute the empty word. The original reduced relators have length distribution \((56,53,53)\) for lengths one, two and three.

An exact finite sequence of **159 generator–two-cell cancellations** follows. At each step, a selected cyclically reduced attaching word contains one chosen generator **exactly once**. Solve that relator for the generator, substitute its word in the other two-cell attaching maps, freely and cyclically reduce, and remove the generator and its two-cell. This is the standard elementary two-dimensional CW deformation: the other attaching maps slide across the selected two-cell and the resulting free generator–cell pair collapses. Every step is reconstructed and checked by the attached standard-library Python program. Exactly \(112\) cancellations use a one-letter relator and \(47\) use a two-letter relator. The surviving complex has **one vertex, one loop and three two-cells**, whose attaching words, after naming the surviving loop \(x\), are

\[
x^{-3},\qquad x^3,\qquad 1.
\]

Slide the two-cell attached by \(x^{-3}\) across the oppositely attached degree-three two-cell. The former then has null attaching map, so is a wedge summand \(S^2\); the already null-attached third two-cell is another \(S^2\). The remaining one-loop, one-two-cell subcomplex is exactly \(S^1\cup_{\deg 3}e^2\). This proves the displayed homotopy equivalence, not just the homology groups.

## Verification
Run `python3 verify_d4.py` with Python 3.10 or later; no third-party Python modules or external data are needed. The program constructs the full finite group, verifies the reflection-length interval and the anti-automorphism property on all ordered pairs, enumerates all chains and barycentric face flags, verifies the quotient boundary composition, constructs the spanning tree, and replays every generator–two-cell cancellation. It asserts the final two degree-three relators and the third null-attached cell, and reports `D4_KREWERAS_MOORE3_TWO_SPHERES_OK`. Every finite search here is exhaustive for the specified \(D_4\) object.

## Relationship to prior work
Athanasiadis–Reiner (2004) define and enumerate the type-\(D\) absolute-order noncrossing lattice and its chain statistics; those results cross-check the finite interval but do not compute the topology of a Kreweras quotient. Armstrong–Stump–Thomas (first public preprint 2011) establish Kreweras orbit combinatorics and cyclic sieving for type \(D\); their orbit counts do not specify the attaching maps of the geometric quotient. Published finite calculations on type-\(B_4\) Coxeter conjugation and type-\(D_5\) Coxeter conjugation concern different groups and/or different actions. In particular, the order-reversing Kreweras action is not the order-preserving Coxeter-conjugation action, and the present degree-three Moore summand is not a consequence of enumerating fixed elements alone.

## Limitations
This is an exact result only for type \(D_4\), not a generalization to every type \(D_n\). The comparison to accessible literature establishes originality relative to identified sources, not absolute priority against all unindexed work. The executable finite certificate supplies a fully reproducible derivation of the stated CW reductions, but the proof has not received an independent mathematical audit. Homotopy-orbit and fixed-point-space claims are not asserted.

## References
1. C. A. Athanasiadis and V. Reiner, *Noncrossing Partitions for the Group* \(D_n\), **SIAM Journal on Discrete Mathematics** 18 (2004), 397–417, DOI: https://doi.org/10.1137/S0895480103432192; full text: https://www-users.cse.umn.edu/~reiner/Papers/ncd.pdf (electronically published December 9, 2004).
2. D. Armstrong, C. Stump, H. Thomas, *A Uniform Bijection Between Nonnesting and Noncrossing Partitions*, first public arXiv version January 6, 2011, https://arxiv.org/abs/1101.1277; **Transactions of the AMS** 365 (2013), 4121–4151, DOI: https://doi.org/10.1090/S0002-9947-2013-05729-7.
3. D. Armstrong, *Generalized Noncrossing Partitions and Combinatorics of Coxeter Groups*, first public arXiv submission November 4, 2006, https://arxiv.org/abs/math/0611106.
