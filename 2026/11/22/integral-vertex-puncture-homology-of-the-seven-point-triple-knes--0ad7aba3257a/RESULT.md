# Integral vertex-puncture homology of the seven-point triple-Kneser independence complex

## Finding
Let \(G=\mathrm{KG}(7,3)\) have as vertices the \(35\) triples of \([7]\), with two triples adjacent exactly if they are disjoint. Let \(X=\operatorname{Ind}(G)\), \(v\) any vertex, \(D=X[V(G)\setminus\{v\}]\), and \(L=\operatorname{lk}_X(v)\). The complete **reduced integral homology groups** are

\[
\widetilde H_i(L;\mathbb Z)\cong
\begin{cases}\mathbb Z^6,&i=5,\\\mathbb Z^4,&i=8,\\0,&\text{otherwise},\end{cases}
\qquad
\widetilde H_i(D;\mathbb Z)\cong
\begin{cases}\mathbb Z^{23},&i=6,\\\mathbb Z^3,&i=9,\\0,&\text{otherwise}.\end{cases}
\]

For \(i=6,9\), the inclusion-induced map \(\widetilde H_i(D;\mathbb Z)\to\widetilde H_i(X;\mathbb Z)\) is a split injection, with respective cokernels \(\mathbb Z^6\) and \(\mathbb Z^4\). No homotopy-equivalence classification of \(L\), \(D\), or \(X\) is asserted.

## Assumptions and scope
The ground set is exactly \([7]\) and \(G\) is the ordinary simple Kneser **disjointness** graph, not its complement. A face of \(X\) is a family of triples that pairwise intersect. Choose \(v=\{1,2,3\}\) without loss of generality under relabeling. Then \(L=\operatorname{Ind}(G-N_G[v])\) and \(D=\operatorname{Ind}(G-v)\); \(G-N_G[v]\) has \(30\) vertices because \(G\) is four-regular. Integral homology is reduced unless otherwise stated.

## Proof
**Exact face sets.** Enumerate the triples in lexicographic order, indexed from zero in the attached implementation. For each index, mark as compatible all *other* triples with nonempty intersection. Starting with the empty face, recursively append only compatible indices in increasing order; this enumerates every nonempty independent set precisely once, by its unique increasing sequence. Excluding the chosen vertex gives \(1,000,971\) nonempty faces for \(D\). Excluding it and the four disjoint triples gives \(277,713\) nonempty faces for \(L\).

**Exhaustive acyclic face matchings.** Process a prescribed ordering of the admissible graph vertices. For each index \(p\), pair every remaining face \(\sigma\) lacking \(p\) with \(\sigma\cup\{p\}\), provided both are still unpaired; then remove the two faces from subsequent passes. For \(L\), use increasing admissible indices. For \(D\), use the explicit permutation of admissible indices in `MORSE_CHECK.py`, rather than an unspecified pseudorandom seed. The code confirms that no face is paired twice and that the remaining unmatched faces number exactly one dimension-zero face, six dimension-five faces and four dimension-eight faces for \(L\), and one dimension-zero face, twenty-three dimension-six faces and three dimension-nine faces for \(D\).

**Acyclicity is checked rather than assumed.** Forman's discrete-Morse orientation on the **nonempty** face Hasse diagram points upward on each matched codimension-one incidence and downward on every other such incidence. The attached certificate constructs the entire orientation, traverses every face, and rejects an edge entering the active depth-first search stack. It verifies no directed cycle among all \(277,713\), respectively \(1,000,971\), nonempty faces. The correspondence between directed cycles and closed gradient paths makes the matching an acyclic discrete Morse matching. No incomplete partial face search is used.

**Integral computation.** The discrete Morse theorem gives a CW complex with one cell per unmatched face, homotopy equivalent to the original. Here each CW complex has one zero-cell and positive-dimensional cells only in degrees \(5\) and \(8\) for the link, respectively \(6\) and \(9\) for the deletion. As no consecutive dimensions occur, every integral cellular boundary map vanishes; the displayed integral homology groups follow, including torsion-freeness. This argument **does not** infer a wedge of spheres: higher attaching maps could remain nonzero.

**Primitive inclusion.** Decompose \(X=D\cup(v*L)\), with intersection \(L\). Since the cone is contractible, the reduced Mayer–Vietoris sequence, together with the two calculated homology profiles, reduces to split short exact sequences

\[
0\to\mathbb Z^{23}\to\widetilde H_6(X;\mathbb Z)\to\mathbb Z^6\to0,
\qquad
0\to\mathbb Z^3\to\widetilde H_9(X;\mathbb Z)\to\mathbb Z^4\to0.
\]

They split as abelian groups because the quotient is free, so both inclusions are primitive. The resulting ambient integral ranks \(29\) and \(7\) agree with, but are not offered as novel replacements for, published computations.

## Verification
Run `python3 MORSE_CHECK.py` (standard library only). The output must equal `EXPECTED.txt` byte-for-byte. The program rebuilds the Kneser vertex set, compatibility graph, every face, the prescribed matching, every critical-cell dimension, and an exhaustive directed-Hasse cycle check. This is a finite **complete** certificate for the two specified complexes; the proof makes no asymptotic or all-parameter extrapolation.

## Relationship to prior work
Feng's October 2026 paper determines the **rational** homology of the whole seven-point triple-Kneser independence complex as part of an infinite family. A separate published integral computation already gives torsion-freeness and ambient ranks \(29\) and \(7\); published rational symmetric-group characters also concern the whole complex. The present contribution instead determines both local objects, the vertex-deletion and the link, integrally, and the primitive ranks of the inclusion maps. Full-complex homology alone does not imply these local groups. Relevant published source texts and priority risks are discussed in `REVIEW.md`.

## Limitations
Only the first seven-point triple-Kneser case and a single removed graph vertex are covered. The results concern integral homology, not an exact wedge-of-spheres homotopy type, an equivariant lattice classification, or higher triple-Kneser parameters. Publication priority cannot be guaranteed against unindexed or inaccessible equivalent work; an independent mathematical audit has not been performed.

## References
- Ziqin Feng, *The rational homology of independence complexes of Kneser graphs on triples*, first posted 2026-10-12, arXiv:2610.17394: https://arxiv.org/abs/2610.17394.
- *Torsion-free integral homology for the first nontrivial triple Kneser independence complex*, published mathematical finding: https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-torsion-free-integral-homology-for-the-first-nontrivial-triple-k--4fc04e767560.
- *Full rational \(S_7\) homology of the seven-point triple Kneser complex*, published mathematical finding: https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-full-rational-s-7-homology-of-the-seven-point-triple-kneser-comp--0c1e2b2ee47c.
- R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
