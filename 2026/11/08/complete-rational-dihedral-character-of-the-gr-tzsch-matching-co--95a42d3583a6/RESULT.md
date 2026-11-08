# Complete rational dihedral character of the Grötzsch matching complex

## Finding
Let \(G=\mu(C_5)\) be the eleven-vertex Grötzsch graph, and let \(X=\mathcal M(G)\) be its ordinary matching complex, whose faces are sets of pairwise vertex-disjoint graph edges. The full graph automorphism group is \(D_5=\langle r,s\mid r^5=s^2=1,\;srs=r^{-1}\rangle\), acting on \(X\). Set \(W=\mathbb Q(\zeta_5)\), a four-dimensional rational representation with \(r\) acting as multiplication by a primitive fifth root \(\zeta_5\) and \(s\) acting by complex conjugation.

The *complete rational homology representation* is
\[
\widetilde H_i(X;\mathbb Q)\cong
\begin{cases}
\mathbb Q[D_5]^{\oplus2}\oplus W,&i=3,\\
0,&i\ne3.
\end{cases}
\]
Its character equals \(24\) at the identity, \(-1\) at each nonidentity rotation, and \(0\) at every reflection. In particular,
\[
\widetilde H_3(X;\mathbb Q)^{D_5}\cong\mathbb Q^2,
\qquad
\widetilde H_3(X;\mathbb Q)^{\langle r\rangle}\cong\mathbb Q^4.
\]
All positive-degree rational homology of the topological orbit space \(|X|/D_5\) vanishes except \(H_3\), which has dimension two. Thus its rational Betti vector in degrees zero through four is \((1,0,0,2,0)\).

## Assumptions and scope
Label the original pentagon vertices \(v_i=i\), their clones \(w_i=5+i\), for \(i\in\mathbb Z/5\mathbb Z\), and the apex \(a=10\). The twenty edges are \(v_iv_{i+1}\), \(w_iv_{i-1}\), \(w_iv_{i+1}\), and \(aw_i\) for all five indices. Each simplicial vertex of \(X\) is one *graph edge*; an oriented simplicial \(d\)-face is an increasing tuple of \(d+1\) disjoint graph-edge indices in lexicographic edge order. The action on oriented faces includes the sign of reordering the image edge indices.

The group induced by \(r(i)=i+1\) and \(s(i)=-i\) on both pentagon and clone indices fixes the apex and has order ten. It is the *full* graph automorphism group: the apex is the unique vertex of degree five, the original pentagon consists of the five degree-four vertices, and the clones are the five degree-three vertices. Every automorphism consequently restricts to an automorphism of the original induced pentagon, and its action on clones is uniquely forced by their two original neighbors. Conversely every pentagon dihedral automorphism extends as indicated.

## Proof
**Exact chain ranks.** The simplicial matching faces are exhaustively enumerable because no matching contains more than five edges on eleven graph vertices. The number of faces in dimensions \(0,1,2,3,4\) is
\[
(20,135,365,360,87).
\]
For each oriented \(d\)-face \([e_0,\ldots,e_d]\), the boundary is the signed alternating deletion sum. The accompanying executable enumerates all faces and every nonzero boundary entry, verifies \(\partial^2=0\), and performs sparse elimination modulo each of \(2\), \(3\), and \(101\). In every field the ranks of the four positive differentials are
\[
(\operatorname{rank}\partial_1,\ldots,\operatorname{rank}\partial_4)=(19,116,249,87).
\]
Field ranks do **not** generally imply equality of rational ranks. Here they do, because the modular ranks furnish rational lower bounds and the chain equations give matching rational upper bounds: \(\operatorname{rank}\partial_1\le20-1=19\) by augmentation; hence \(\operatorname{rank}\partial_2\le135-19=116\), \(\operatorname{rank}\partial_3\le365-116=249\), and \(\operatorname{rank}\partial_4\le87\). Every lower bound is attained. This independently yields \(\widetilde b_3=360-249-87=24\), with all other reduced rational Betti numbers zero. The complete enumeration algorithm is given in `verify.py`; no claim of integral homology follows from field ranks.

**Signed Lefschetz traces.** For \(g\in D_5\), let \(T_d(g)\) denote its oriented trace on the \(d\)-face chain group: each setwise-fixed face contributes \(+1\) or \(-1\) according to the parity of the induced permutation of its edges. Exhaustive fixed-face enumeration gives
\[
\begin{array}{c|rrrrr}
& T_0&T_1&T_2&T_3&T_4\\\hline
1&20&135&365&360&87\\
r^k\ (1\le k\le4)&0&0&0&0&2\\
sr^k\ (0\le k\le4)&2&-3&-5&0&1
\end{array}
\]
The signed face action is a chain map, since vertex permutations commute with the oriented boundary. The reduced Lefschetz number therefore equals \(-1+T_0-T_1+T_2-T_3+T_4\). As only reduced degree-three homology survives, its character is the negative of this number. The three row types give exactly \(24,-1,0\), respectively. The code checks *all ten* group elements, not merely representatives.

**Representation and quotient.** The character of the regular rational \(D_5\)-module is ten at the identity and zero elsewhere. The trace of nontrivial powers of \(\zeta_5\) on \(\mathbb Q(\zeta_5)\) is \(-1\), while complex conjugation composed with any such multiplication has trace zero. Thus \(2\mathbb Q[D_5]\oplus W\) has exactly the computed character. Rational finite-group representations are semisimple and determined by their characters; the claimed isomorphism follows. The invariant dimensions are \(\frac1{10}(24+4(-1)+5(0))=2\) and \(\frac15(24+4(-1))=4\). Finally, rational transfer/averaging for finite group actions on finite simplicial complexes identifies the rational cohomology of the orbit space with invariant rational cohomology of the complex; over \(\mathbb Q\), dimensions agree with invariant homology. This proves the quotient Betti assertion.

## Verification
From the extracted directory, execute `python3 verify.py` with Python 3 and no third-party packages. The code constructs the graph from its explicit edge rules, exhaustively enumerates every matching, reconstructs all signed boundaries, verifies \(\partial^2=0\), checks ranks modulo three primes, and recomputes all ten oriented Lefschetz traces. Its deterministic expected stdout is included as `verification_output.txt`. The output terminates with `GROTZSCH_MATCHING_D5_EXACT_PASS`; the rank-bound argument above, not a probabilistic test, proves the rational ranks. All integer and modular calculations operate on precisely the graph defined above.

## Relationship to prior work
The first public version of Alexander Engström's *Independence complexes of claw-free graphs* (arXiv:math/0512420, 17 December 2005) gives general connectivity tools applicable to line-graph independence complexes, but no Grötzsch dihedral module. Jakob Jonsson's *More torsion in the homology of the matching complex* (arXiv:1203.5658, 26 March 2012) studies complete-graph matching complexes rather than this named graph. The publicly available result *The Grötzsch graph matching complex is a wedge of twenty-four three-spheres* (11 October 2026, identifier below) already determines the **ordinary integral homotopy type** \(\bigvee^{24} S^3\). That statement is not claimed here and does not specify a group action on homology. Balasubramanian's 2025 matching-polynomial work treats matching counts for symmetric graphs but not the signed simplicial action. The present result supplies the full action of every automorphism and the homology of the finite-symmetry orbit space.

## Limitations
This is an exact finite-graph result, not a theorem for all Mycielski graphs. It determines the rational \(D_5\)-representation, not the integral \(\mathbb Z[D_5]\)-lattice, an equivariant wedge decomposition, or integral homology of the quotient. No independent mathematical validation or definitive priority determination has been performed. An equivalent unindexed calculation could exist. The claim does not assert a new nonequivariant homotopy type.

## References
1. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420v1 (public 17 December 2005), https://arxiv.org/abs/math/0512420.
2. J. Jonsson, *More torsion in the homology of the matching complex*, arXiv:1203.5658 (public 26 March 2012), https://arxiv.org/abs/1203.5658.
3. *The Grötzsch graph matching complex is a wedge of twenty-four three-spheres*, publicly available mathematical research record dated 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-gr-tzsch-graph-matching-complex-is-a-wedge-of-twenty-four-th--514850eb507b.
4. K. Balasubramanian, *Matching Polynomials of Symmetric, Semisymmetric, Double Group Graphs, Polyacenes, Wheels, Fans, and Symmetric Solids in Third and Higher Dimensions*, *Symmetry* **17** (2025), 133, https://doi.org/10.3390/sym17010133.
