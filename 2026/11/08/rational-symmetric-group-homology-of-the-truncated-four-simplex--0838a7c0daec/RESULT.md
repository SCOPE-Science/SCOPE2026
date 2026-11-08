# Rational symmetric-group homology of the truncated four-simplex independence complex

## Finding
Let \(T_5\) be the graph of the ordinarily truncated four-simplex. Its vertices are ordered pairs \((a,b)\) of distinct elements of \(L=\{0,1,2,3,4\}\); two vertices are adjacent precisely when their first coordinates agree or they are reverse pairs. Set \(X=\operatorname{Ind}(T_5)\), with its natural action of \(S_5\). Let \(\mathcal C\) be the set of twenty-four directed Hamiltonian five-cycles on \(L\), taken modulo cyclic rotation, and let \(\mathbb Q[\mathcal C]_{\mathrm{sgn}}\) denote the unique one-dimensional sign subrepresentation of the permutation module \(\mathbb Q[\mathcal C]\). Then, as rational \(S_5\)-representations,
\[
\widetilde H_j(X;\mathbb Q)\cong
\begin{cases}
\operatorname{sgn}\otimes\mathbb Q[L],&j=3,\\
\mathbb Q[\mathcal C]/\mathbb Q[\mathcal C]_{\mathrm{sgn}},&j=4,\\
0,&j\ne3,4.
\end{cases}
\]
In particular, the rational cohomology ring of the orbit space satisfies
\[
H^*(|X|/S_5;\mathbb Q)\cong H^*(S^4;\mathbb Q).
\]
This is an isomorphism of graded rational cohomology rings, **not** an assertion of homotopy equivalence.

## Assumptions and scope
The graph has twenty vertices and forty edges. Each of the five fixed-first-coordinate sets forms a four-clique; between each pair of these cliques is a unique edge, joining their two reverse ordered pairs. Thus all graph automorphisms permute the five four-cliques, and this permutation determines the automorphism, so \(\operatorname{Aut}(T_5)=S_5\). Equivalently, \(T_5\) is the line graph of the graph obtained by subdividing each edge of \(K_5\) once. Its independent sets are partial maps on \(L\) with no fixed points and no directed two-cycle. Each such map has at most five arrows, giving \(\dim X=4\).

Throughout, rational chain groups use the orientation on simplices induced by lexicographically sorting their ordered-pair vertices. The permutation action is a **signed** action on simplicial chains. The claim concerns rational homology; no integral lattice decomposition is claimed.

## Proof
**1. Exact face enumeration and ranks.** Every face is uniquely specified by independently choosing for each source \(a\in L\) either no arrow or exactly one target \(b\ne a\), then discarding every choice containing both arrows of a reciprocal pair. This exhaustive finite construction yields the face vector, in dimensions zero through four,
\[
(f_0,f_1,f_2,f_3,f_4)=(20,150,520,815,444).
\]
Let \(\partial_i:C_i(X;\mathbb Q)\to C_{i-1}(X;\mathbb Q)\) be the signed simplicial boundary. The exact augmented-boundary ranks, counting the augmentation rank as \(r_0=1\), are
\[
(r_0,r_1,r_2,r_3,r_4)=(1,19,131,389,421).
\]
These are certified by the standalone `verify.py`: it constructs every boundary column over \(\mathbb Q\) and performs normalized column echelon elimination using exact `Fraction` arithmetic. Each nonzero pivot contributes one independent boundary vector; every other column reduces to zero. This certifies both rank lower and upper bounds by exhaustive elimination, rather than relying on ranks computed modulo primes. Consequently, the reduced Betti numbers are \((0,0,0,5,23)\).

**2. Exact characters.** For each of the seven conjugacy classes, the verifier constructs a representative \(g\) and obtains the signed trace on each \(C_i\) by counting setwise invariant oriented simplices with the sign of the induced vertex permutation. It separately calculates the trace on \(\operatorname{im}\partial_i\): apply \(g\) to each echelon basis vector of the invariant boundary image, reduce in that exact basis, and sum its diagonal coordinates. The two short exact sequences defining cycles, boundaries and homology give
\[
\operatorname{tr}(g\mid H_i)=\operatorname{tr}(g\mid C_i)
-\operatorname{tr}(g\mid\operatorname{im}\partial_i)
-\operatorname{tr}(g\mid\operatorname{im}\partial_{i+1})
\]
for positive \(i\). The calculated characters, ordered by the partition describing the cycle type, are:

| Cycle type | \(1^5\) | \(2\,1^3\) | \(3\,1^2\) | \(2^2\,1\) | \(4\,1\) | \(3\,2\) | \(5\) |
|:---|---:|---:|---:|---:|---:|---:|---:|
| \(\chi_3\) | 5 | -3 | 2 | 1 | -1 | 0 | 0 |
| \(\chi_4\) | 23 | 1 | -1 | -1 | 1 | 1 | 3 |

The signed-boundary equivariance identities are also checked on both generators \((0\ 1)\) and \((0\ 1\ 2\ 3\ 4)\), for every simplex of positive dimension. These generate \(S_5\), so the chain-level representations are well-defined over the full group.

**3. Representation identification.** The sign-twisted permutation representation on five letters has character
\[
\operatorname{sgn}(g)\,\#\operatorname{Fix}_L(g),
\]
which exactly reproduces \(\chi_3\). The permutation action on \(\mathcal C\) is transitive, with stabilizer \(C_5\), and a permutation fixes one of the directed cycles exactly if it belongs to its cyclic subgroup. Thus \(\mathbb Q[\mathcal C]\) has character \(24\) at the identity, \(4\) on five-cycles, and zero otherwise. Since a five-cycle is even, Frobenius reciprocity shows that the sign representation occurs exactly once in \(\mathbb Q[\mathcal C]\). Subtracting its character yields \(\chi_4\). Rational representations of a finite group are semisimple and determined by their characters, proving both asserted isomorphisms.

**4. Quotient.** The sign-twisted five-letter permutation module has no \(S_5\)-invariants. The twenty-four-cycle permutation module has a one-dimensional invariant line, while the sign line has none; hence \(\dim\widetilde H_4(X;\mathbb Q)^{S_5}=1\). For any finite simplicial group action, the rational cohomology of its orbit space equals the invariant rational cohomology of the original space, after subdivision if necessary. Therefore the quotient has ordinary rational cohomology of ranks one in degrees zero and four and zero otherwise. Multiplication of positive-degree classes vanishes for degree reasons, yielding the stated graded-ring isomorphism.

## Verification
Run `python verify.py` with Python's standard library; the embedded `verification_output.txt` records one successful execution. The script checks 1,949 nonempty faces, 960 independent normalized boundary pivots in total, exact ranks \((1,19,131,389,421)\), and both signed-chain generator actions on 3,858 positive-dimensional generator-face pairs. It constructs seven rational homology characters without floating point or modular reduction and independently checks agreement with the two stated representation characters. The invariant dimensions are confirmed by averaging over all 120 permutations.

## Relationship to prior work
Engström's 2005 preprint on claw-free graph independence complexes establishes general connectivity bounds, not the full rational \(S_5\) homology action of this graph. Barmak's 2010 treatment of star clusters and matching complexes likewise provides broad topological methods and connectivity bounds, not these two characters. A published exact calculation of the *same* truncated four-simplex complex already establishes its integral nonequivariant homotopy type \(\bigvee^5 S^3\vee\bigvee^{23}S^4\). That earlier sphere-wedge classification is not claimed as new here: it does not determine the degreewise permutation action, the five-cycle quotient representation or the cohomology of the full symmetry quotient. The theorem is the precise equivariant refinement; it is not implied by equality of ordinary Betti numbers or nonequivariant homotopy types. Relevant research-record searches using the subdivided-complete-graph matching complex and partial-function aliases did not identify a covering character calculation.

## Limitations
The theorem concerns one natural finite graph and its rational representations. It does not classify the integral \(S_5\)-lattices, torsion in the orbit space, equivariant homotopy type, or all truncated simplices. The abstract representation isomorphisms are not asserted to arise from explicit geometric cycles indexed by five-cycles. The exact verifier certifies the finite rational computation but does not establish any infinite-family theorem. Equivalent work in inaccessible or unindexed literature remains possible; independent mathematical validation and definitive priority determination have not been performed.

## References
1. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420v1, first posted 17 December 2005, https://arxiv.org/abs/math/0512420.
2. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first posted 2 July 2010, https://arxiv.org/abs/1007.0418.
3. *The independence complexes of the truncated four- and five-simplices*, published result and complete proof in the public `published-finding corpus/2026` repository under record `2026/10/11/SCOPE-the-independence-complexes-of-the-truncated-four-and-five-simpli--4f07444cc928`, 11 October 2026. The present work uses only the scientific statement for comparison and independently computes all new rational representations.
