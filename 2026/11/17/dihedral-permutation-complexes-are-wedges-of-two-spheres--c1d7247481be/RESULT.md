# Dihedral permutation complexes are wedges of two-spheres

## Finding

For each integer \(n\ge 3\), let \(V=\{0,1,\ldots,n-1\}\), with its natural cyclic order. Let \(R_n^+\) consist of the \(n\) cyclic rotations of the word \(0,1,\ldots,n-1\), and let \(R_n^-\) consist of the \(n\) cyclic rotations of the reversed word \(n-1,\ldots,0\). Given a family \(R\) of full permutations, its *permutation complex* \(X(R)\) is the geometric realization of the semisimplicial set whose \(p\)-faces are the distinct ordered injective words of length \(p+1\) that occur as subsequences of some word of \(R\); faces delete individual letters.

Put \(P_n=X(R_n^+)\), \(Q_n=X(R_n^-)\), and \(D_n=X(R_n^+\cup R_n^-)\). Then

\[
P_n\simeq S^1,\qquad Q_n\simeq S^1,\qquad
D_n\simeq\bigvee^{(n-1)^2-2}S^2.
\]

In addition, \(P_n\cap Q_n\) is the complete bidirected one-dimensional semisimplicial complex on \(n\) vertices, with first integral homology \(\mathbb Z^{(n-1)^2}\). The inclusions induce a split surjection

\[
H_1(P_n\cap Q_n;\mathbb Z)\longrightarrow H_1(P_n;\mathbb Z)\oplus H_1(Q_n;\mathbb Z)\cong\mathbb Z^2.
\]

Thus orientation reversal changes a circle-shaped cyclic-permutation complex into a simply connected wedge of quadratically many two-spheres, with torsion-free integral homology. The first multiplicities, for \(n=3,4,5,6,7,8\), are \(2,7,14,23,34,47\).

## Assumptions and scope

Every word has *distinct* letters. A face is a subsequence, not necessarily a consecutive substring. Repeated descriptions of the same ordered word identify the same cell. Oppositely directed two-letter words are **different** one-cells, even though they have the same endpoints. The resulting object is a regular semisimplicial/Boolean cell complex, not the ordinary abstract clique complex on the underlying vertex set. Its barycentric subdivision yields the usual simplicial model of permutation complexes. Homotopy equivalence is of geometric realizations, and all homology is integral unless stated otherwise.

## Proof

**Step 1: each orientation separately has circle homotopy type.** Index the forward rotations by
\(r_j=(j,j+1,\ldots,n-1,0,\ldots,j-1)\), for \(0\le j<n\), and let \(\Delta_j\) be the subcomplex of subsequences of \(r_j\). Each \(\Delta_j\) is a closed \((n-1)\)-simplex, and \(P_n=\bigcup_j\Delta_j\). For \(j=0,1\), the common subwords lie entirely in either the singleton \(\{0\}\) or the increasing block \(\{1,\ldots,n-1\}\); consequently \(\Delta_0\cap\Delta_1\) is the *disjoint* union of two nonempty simplices. Since both \(\Delta_0\) and \(\Delta_1\) are contractible, their union is homotopy equivalent to the suspension of the disconnected intersection, namely \(S^1\).

Now suppose \(2\le k<n\) and put \(U_{k-1}=\Delta_0\cup\cdots\cup\Delta_{k-1}\). Consider the forward-order subwords of \(r_k\) that have already appeared in some earlier rotation. Every such word is contained entirely in one of the two cyclic blocks cut at \(j\) and \(k\) for some \(j<k\). Taking the union over these cuts gives exactly
\[
U_{k-1}\cap\Delta_k=\Delta(0,1,\ldots,k-1)\ \cup\ \Delta(k,k+1,\ldots,n-1,0,1,\ldots,k-2),
\]
where \(\Delta(w)\) denotes the full simplex of subsequences of the displayed word. The two simplices intersect in the nonempty full simplex \(\Delta(0,1,\ldots,k-2)\), so the intersection is contractible. Attaching the contractible simplex \(\Delta_k\) along this contractible subcomplex preserves homotopy type: this follows from the homotopy-pushout property of CW subcomplex inclusions. By induction \(P_n\simeq S^1\). Reversing all words yields \(Q_n\simeq S^1\).

**Step 2: the intersection is the complete bidirected graph.** Each singleton occurs in both orientations. For any distinct \(u,v\), both ordered pairs \(uv\) and \(vu\) occur in rotations of either orientation. Every ordered triple occurring in a forward rotation has the *positive* cyclic order on those three letters; every ordered triple occurring in a reverse rotation has the *negative* cyclic order. Since the two cyclic orientations of a three-element set are disjoint, no three-letter word lies in both complexes. Neither do any longer words. Therefore \(B_n=P_n\cap Q_n\) has \(n\) vertices, \(n(n-1)\) one-cells and no higher cells. It is connected and has
\[
H_1(B_n;\mathbb Z)\cong\mathbb Z^{n(n-1)-n+1}=\mathbb Z^{(n-1)^2}.
\]

**Step 3: a primitive, surjective winding map.** On oriented edges \(uv\) in \(P_n\), define the integral one-cochain \(c_+(uv)=1\) when \(u>v\) and \(0\) otherwise. Every positive-cyclic triple \(uvw\) has at most one numerical descent, and it obeys \(c_+(uv)+c_+(vw)-c_+(uw)=0\). Thus \(c_+\) is a cocycle. Similarly \(c_-(uv)=1\) when \(u<v\) is an integral cocycle on \(Q_n\). Let \(d\) be the directed digon \(01+10\), and let \(t\) be the closed directed triangle \(01+12+20\), viewed as cellular one-cycles of \(B_n\). Their paired evaluations are
\[
(c_+(d),c_-(d))=(1,1),\qquad(c_+(t),c_-(t))=(1,2).
\]
The determinant is \(1\). Since each oriented complex has first homology \(\mathbb Z\), the cochains are primitive generators of the respective dual groups, and the homomorphism \(H_1(B_n)\to H_1(P_n)\oplus H_1(Q_n)\) is integrally surjective with a direct-summand kernel.

**Step 4: the total space is a two-sphere bouquet.** Since \(P_n,Q_n\simeq S^1\) and \(B_n\) is connected, van Kampen presents \(\pi_1(D_n)\) as the pushout of the two cyclic fundamental groups along \(\pi_1(B_n)\). The winding map of Step 3 surjects onto \(\mathbb Z^2\). In particular, it contains elements with images \((1,0)\) and \((0,1)\), so the resulting pushout kills each generator of the free product \(\mathbb Z*\mathbb Z\). Therefore \(\pi_1(D_n)=1\).

The integral Mayer–Vietoris sequence, together with the surjection in Step 3, yields
\[
\widetilde H_2(D_n;\mathbb Z)\cong\mathbb Z^{(n-1)^2-2},
\qquad\widetilde H_j(D_n;\mathbb Z)=0\quad(j\ne2).
\]
In particular there is no integral torsion. The Hurewicz isomorphism \(\pi_2(D_n)\cong H_2(D_n;\mathbb Z)\) supplies a map from the displayed wedge of two-spheres inducing an integral homology isomorphism. The homological Whitehead theorem for simply connected CW complexes makes it a homotopy equivalence. This proves the theorem for every \(n\ge3\).

## Verification

The standalone standard-library Python program `verify_dihedral_permutation.py` regenerates all ordered faces from the full rotations, checks the exact intersection identities in Steps 1–2, verifies both integral descent cocycles and the unimodular winding determinant, and independently computes boundary ranks over \(\mathbb F_2\) for \(3\le n\le8\) and over \(\mathbb F_3\) for \(3\le n\le7\). All six dimensions agree with the asserted homology and the two circle subcomplexes; its recorded output is `verification_output.txt`. These finite calculations are consistency checks; the arbitrary-\(n\) assertion follows from the four mathematical steps above, not extrapolation.

## Relationship to prior work

Chachólski–Levi–Meshulam introduced and studied permutation complexes, including a homotopy classification for *two generators* and stable realizability by general families. This theorem concerns the specific natural *\(2n\)-generator* dihedral family and gives its unrestricted exact homotopy type. Govc's November 2026 result proves that every permutation complex has a free fundamental group; the present proof gives the stronger value \(\pi_1(D_n)=1\) and identifies the full higher-dimensional integral homotopy type for this family. Elizalde–Hanlon–Hersh study pattern-avoiding injective-word subcomplexes, which select facets by a different condition; their listed shellability classifications do not provide the stated dihedral formula. No claim is made that the general freeness theorem or the two-permutation theorem is new.

## Limitations

The classification is nonequivariant and concerns only the union of *both complete sets of rotations* of the two opposite circular orders. It does not classify arbitrary subsets of dihedral permutations, their equivariant homology modules, or generic permutation complexes. The novelty assessment is based on inspected primary preprints, targeted literature searches and available research records; a result under an unindexed equivalent formulation remains a bibliographic risk.

## References

1. Dejan Govc, *Fundamental Groups of Permutation Complexes*, arXiv:2611.11362, first submitted 2026-11-08, https://arxiv.org/abs/2611.11362.
2. Wojtek Chachólski, Ran Levi, Roy Meshulam, *On the topology of complexes of injective words*, arXiv:1908.03394, first submitted 2019-08-09; Journal of Applied and Computational Topology 4 (2020), 29–44, https://arxiv.org/abs/1908.03394.
3. Sergi Elizalde, Philip Hanlon, Patricia Hersh, *Complexes of pattern-avoiding injective words*, arXiv:2610.07303, first submitted 2026-10-05, https://arxiv.org/abs/2610.07303.
