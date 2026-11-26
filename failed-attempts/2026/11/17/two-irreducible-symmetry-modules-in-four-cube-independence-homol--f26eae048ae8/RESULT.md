# Two irreducible symmetry modules in four-cube independence homology

## Finding

Let \(Q_4\) be the graph on \(\mathbb F_2^4\) whose edges join words at Hamming distance one, and put \(X=\operatorname{Ind}(Q_4)\). Its full automorphism group is \(B_4=\mathbb F_2^4\rtimes S_4\), acting by \((b,p)x=b+p(x)\), with \(p\) permuting the four coordinates. For \(p\in S_4\), write \(s(p)=\operatorname{sgn}(p)\), \(f(p)=|\{i:p(i)=i\}|\), and \(|b|\) for Hamming weight.

The seven-dimensional rational homology representation, in its only nonzero reduced degree, is the sum of **two nonisomorphic absolutely irreducible rational modules**:

\[
\widetilde H_3(X;\mathbb Q)\cong
\bigl(\operatorname{sgn}_{S_4}\otimes\operatorname{Std}_{S_4}\bigr)
\oplus U_4.
\]

The three-dimensional summand is inflated from \(S_4\), so translations act trivially. The four-dimensional summand \(U_4\) has a basis \(u_1,\ldots,u_4\) and the explicit action

\[
(b,p)u_i=s(p)(-1)^{\sum_{j\ne p(i)}b_j}\,u_{p(i)}.
\]

In particular, for **every** of the \(384\) automorphisms,

\[
\boxed{\chi(b,p)=s(p)\left(f(p)-1+
\sum_{i:p(i)=i}(-1)^{|b|-b_i}\right).}
\]

The formula gives a uniform geometric symmetry invariant beyond the previously determined nonequivariant sphere count. The sixteen translations fix exactly three independent rational top-homology classes; the complete automorphism group fixes none. Consequently the translation quotient has reduced rational cohomology \(\mathbb Q^3\) in degree three, whereas the full automorphism quotient is rationally acyclic. The subgroup of even coordinate permutations fixes exactly one class, so its quotient has the rational cohomology ring of \(S^3\).

## Assumptions and scope

All topology is ordinary geometric realization of finite simplicial complexes; coefficient field for the representation and quotient results is \(\mathbb Q\). A face of \(X\) is a subset of the sixteen binary words with no adjacent pair. Vertex labels \(0,\ldots,15\) encode the four binary coordinates. The associated doubly periodic \(4\times4\) square grid is \(C_4\square C_4\cong Q_4\). A group element \((b,p)\) first permutes coordinates \(p\) and then adds \(b\) modulo two; this convention fixes the signs in the formula above.

Here \(\operatorname{Std}_{S_4}=\ker(\mathbb Q^4\xrightarrow{\sum}\mathbb Q)\). The formula concerns the **rational** representation; it does not assert a canonical splitting of its integral lattice or a genuinely equivariant wedge decomposition.

## Proof

**1. Complete rational homology.** The standalone `verify.py` enumerates all \(2^{16}\) vertex subsets and accepts one precisely when the no-adjacent-pair predicate holds. Face numbers, indexed by face cardinality from zero through eight, are

\[
(1,16,88,208,228,128,56,16,2).
\]

The empty face is included only to form the augmented chain complex. Exact bitset Gaussian elimination on the full augmented boundary operators over \(\mathbb F_2\), from dimensions zero through seven, gives

\[
(1,15,73,135,86,42,14,2).
\]

Thus reduced \(\mathbb F_2\)-homology is seven-dimensional in degree three and zero in all other degrees. Every nonzero integer minor modulo two remains nonzero over \(\mathbb Q\); therefore, in each degree, the rational Betti number is at most its \(\mathbb F_2\) counterpart. The reduced Euler characteristic obtained directly from the listed faces is \(-7\). Hence the only rational Betti number must be \(\dim\widetilde H_3(X;\mathbb Q)=7\). (The stronger integral sphere-wedge homotopy type is already known and is **not** asserted as new here.)

**2. A complete character certificate.** Every automorphism is uniquely of the stated form: a graph automorphism is determined by the image of \(0\) and by its permutation of the four neighbors of \(0\); graph distance and the unique coordinate-subset structure then determine all remaining images. Thus these \(16\cdot24=384\) signed-coordinate permutations exhaust the graph automorphisms.

For any such permutation \(g\), the reduced Lefschetz number is the alternating trace on oriented simplicial chains,

\[
\widetilde L(g)=-1+\sum_{\substack{\emptyset\ne\sigma\in X\\g\sigma=\sigma}}
(-1)^{|\sigma|-1}\operatorname{sgn}(g|_{\sigma}).
\]

The sign is the sign of the permutation induced by \(g\) on the ordered vertices of that face. Since degree three is the only reduced rational homology degree, \(\chi(g)=-\widetilde L(g)\). The verifier checks this sum on **every one** of the \(384\) elements and independently calculates the same character using the independence polynomial at \(-1\) of the graph on admissible vertex-orbits of \(g\). The two independent computations agree for every element with the displayed closed formula. This is a finite exhaustive proof: the entire vertex-subset universe, every face, every automorphism and every fixed face is checked; no sampling or extrapolation is used. The character value distribution is

\[
\begin{array}{c|rrrrrr}
\chi(g)&-3&-1&1&3&5&7\\\hline
\#\{g\}&24&161&188&6&4&1.
\end{array}
\]

In particular \(\frac1{384}\sum_{g\in B_4}\chi(g)^2=2\).

**3. Identification of both summands.** Fourier inversion on the normal translation subgroup \(T=\mathbb F_2^4\) gives the following character multiplicities in \(\widetilde H_3\): the trivial character occurs three times, and each of the four characters \(b\mapsto(-1)^{\sum_{j\ne i}b_j}\) occurs once; every other translation character occurs zero times. The verifier obtains these integer multiplicities by averaging over all sixteen translations.

It follows that the three-dimensional \(T\)-fixed space and its four-dimensional complement are each invariant under the whole group. Averaging the full trace over translations yields the character \(s(p)(f(p)-1)\) on the fixed space, exactly the sign-twisted standard representation of \(S_4\). This is absolutely irreducible. The four nontrivial translation characters are pairwise distinct and are transitively permuted by \(S_4\). Each corresponding weight space is one-dimensional, so a nonzero submodule invariant under \(T\rtimes S_4\) must contain all four. Hence the complement is absolutely irreducible. The explicit signed-monomial representation \(U_4\) in the statement has exactly these translation characters and the remaining character \(s(p)\sum_{i:p(i)=i}(-1)^{|b|-b_i}\). Equality of characters over characteristic zero proves the claimed rational module isomorphism. This proves the full character and its two-irreducible decomposition, rather than simply its seven-dimensional rank.

**4. Quotients.** For a finite group \(H\) acting simplicially, rational transfer identifies \(H^*(|X|/H;\mathbb Q)\) with \(H^*(X;\mathbb Q)^H\); the usual barycentric subdivision can be used to make the quotient cellular. Averaging the verified character over the six named subgroups gives the reduced degree-three ranks: translations \(3\), even translations \(3\), central inversion \(3\), coordinate permutations \(0\), even coordinate permutations \(1\), and all \(B_4\) \(0\). No other reduced rational cohomology exists. Since the only positive degree is three, positive-degree cup products necessarily vanish.

## Verification

Run `python3 verify.py` using Python 3 with no external dependencies; the expected exact output is embedded as `verification_output.txt`. The verifier reconstructs the full augmented simplicial boundary operators; computes exact binary ranks; enumerates all \(384\) graph symmetries; computes signed fixed-simplex traces, independent orbit-graph polynomial traces, and the formula; performs all sixteen Fourier averages; and checks character inner products and subgroup invariant dimensions. It terminates with `Q4_INDEPENDENCE_B4_CHARACTER_PASS` only after every assertion succeeds. The package contains both the complete source and its actual checked output; a log alone is not the proof.

## Relationship to prior work

The exact nonequivariant homotopy type \(X\simeq\bigvee^7 S^3\) and its seven-dimensional homology rank were already established by a discrete-Morse calculation of the four-cube independence complex [4]. Jonsson's 2008 grid-homology preprint [3] also includes \(7t^3\) at the \(4\times4\) entry of its table of small periodic-grid homology ranks; that table is **known prior data**, not part of the originality claim. Earlier Fendley–Schoutens–van Eerten [1] and Jonsson [2] study alternating independent-set counts and toric hard-square partition functions, not the action on homology. Bousquet-Mélou–Linusson–Nevo [5] determine open/cylindrical grid-complex homotopy types rather than the full action for the toroidal \(4\times4\) case. Jonsson's cross-cycle results [3] identify special cycles of periodic grids but do not provide the full \(B_4\)-character or the two irreducible modules. The added theorem is precisely the **complete hyperoctahedral homology representation and the resulting quotient rational cohomology**, not any of those earlier nonequivariant ranks, homotopy types or tiling enumerations.

## Limitations

Only this sixteen-vertex graph is treated, and only its rational symmetry representation and ordinary quotient rational cohomology. No uniform character formula for arbitrary hypercubes, no integral \(B_4\)-lattice classification, no quotient torsion, and no equivariant homotopy inverse are established. The verification is exhaustive **finite** combinatorics and character theory, not independent validation; equivalent unindexed literature remains possible.

## References

[1] P. Fendley, K. Schoutens, H. van Eerten, *Hard squares with negative activity*, first public arXiv version 2004-08-24, arXiv:cond-mat/0408497, https://arxiv.org/abs/cond-mat/0408497 .

[2] J. Jonsson, *Hard Squares with Negative Activity and Rhombus Tilings of the Plane*, Electronic Journal of Combinatorics 13 (2006), R67, DOI:10.37236/1093, https://doi.org/10.37236/1093 .

[3] J. Jonsson, *Certain Homology Cycles of the Independence Complex of Grid Graphs*, author preprint dated 2008-10-19, later Discrete & Computational Geometry 43 (2010), 927–950, DOI:10.1007/s00454-009-9224-9. Table 1 lists the \(4\times4\) rank as \(7t^3\).

[4] *The four-cube independence complex is a wedge of seven three-spheres*, publicly indexed mathematical finding dated 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-four-cube-independence-complex-is-a-wedge-of-seven-three-sph--9947aaad144c .

[5] M. Bousquet-Mélou, S. Linusson, E. Nevo, *On the independence complex of square grids*, arXiv:math/0701890, 2007, https://arxiv.org/abs/math/0701890 .
