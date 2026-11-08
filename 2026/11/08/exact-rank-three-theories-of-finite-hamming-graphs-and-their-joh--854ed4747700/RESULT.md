# Exact rank-three theories of finite Hamming graphs and their Johnson coincidences

## Finding

Let \(H(d,q)\) be the simple graph on \(\{0,\ldots,q-1\}^d\) whose vertices are adjacent exactly when they differ in one coordinate, with integers \(d,q\ge1\). Interpret these graphs in the pure first-order language with equality and one undirected irreflexive edge relation. Write \(G\equiv_3 G'\) when they satisfy exactly the same sentences of quantifier rank at most three, with unrestricted numbers of variables.

**Theorem.** The family of all finite Hamming graphs has exactly eight \(\equiv_3\)-classes, described by the following disjoint parameter regimes:

| Class | Parameters | Pair-profile spectrum \(\Sigma\) |
| --- | --- | --- |
| 1 | \(q=1\), any \(d\) | \(\varnothing\) |
| 2 | \(d=1,q=2\) | \(\{(1,0)\}\) |
| 3 | \(d=1,q\ge3\) | \(\{(1,8)\}\) |
| 4 | \(d=2,q=2\) | \(\{(0,8),(1,6)\}\) |
| 5 | \(d=3,q=2\) | \(\{(0,6),(0,15),(1,7)\}\) |
| 6 | \(d\ge4,q=2\) | \(\{(0,7),(0,15),(1,7)\}\) |
| 7 | \(d=2,q\ge3\) | \(\{(0,15),(1,15)\}\) |
| 8 | \(d\ge3,q\ge3\) | \(\{(0,7),(0,15),(1,15)\}\) |

The invariant \(\Sigma\) is defined below. In particular, \(H(3,3)\), on 27 vertices, is the **smallest Hamming graph** realizing the rank-three theory approached as both parameters diverge: for all \(d,q\ge3\),
\[
H(d,q)\equiv_3 H(3,3).
\]
Neither threshold can be lowered uniformly.

There are also exact cross-family coincidences with the Johnson graph \(J(n,k)\), whose vertices are the \(k\)-subsets of an \(n\)-set and whose edges join pairs with symmetric difference of size two:
\[
H(2,q)\equiv_3 J(n,2)\quad(q\ge3,\ n\ge6),
\]
\[
H(d,q)\equiv_3 J(n,k)\quad(d,q\ge3,\ n\ge7,\ 3\le k\le n-3).
\]
The statements concern quantifier rank three only: no elementary equivalence of the full theories, no all-rank Hamming limit law, and no graph isomorphism is asserted.

## Assumptions and scope

All graphs are finite, nonempty, simple, undirected, and interpreted in the edge-only language with equality. Quantifier rank counts the maximum number of *nested* quantifiers; Boolean combinations do not add ranks. Both Hamming parameters are positive integers, including the one-letter degenerate graph \(H(d,1)\). For the Johnson comparisons, \(n,k\) are integers with \(0\le k\le n\) and the ranges stated in the theorem. No colors, coordinate predicates, order or counting quantifiers are available to formulas.

For distinct vertices \(x,y\) in a graph \(G\), define \(m_G(x,y)\) by examining all vertices \(z\notin\{x,y\}\). For \(a,b\in\{0,1\}\), set the bit of weight \(2^{2a+b}\) if there is such a \(z\) for which \(E(x,z)\) has truth value \(a\) and \(E(y,z)\) has truth value \(b\). Define the pair-profile spectrum
\[
\Sigma(G)=\left\{\bigl(\mathbf1_{E(x,y)},m_G(x,y)\bigr):x\ne y\right\}.
\]
Thus a mask of 15 means all four third-vertex adjacency patterns occur, 7 means all but a common neighbor occur, and 6 means that only the two asymmetric patterns occur. This definition is a **set**, not a multiset; bounded-rank first-order logic cannot count how often a profile occurs with only three nested quantifiers.

## Proof

**Step 1: an exact three-round game invariant.** For any two nonempty finite *vertex-transitive* simple graphs \(G,G'\),
\[
G\equiv_3 G'\quad\Longleftrightarrow\quad\Sigma(G)=\Sigma(G').
\]
For the forward direction, a profile \((e,m)\) can be specified by a rank-three sentence: choose distinct \(x,y\) with edge truth value \(e\), then for each of the four possible patterns specify, using one additional quantified vertex \(z\), whether it occurs or does not occur. The conjunction of these four requirements has rank three. Hence two graphs with different spectra differ on some rank-three sentence.

For the reverse direction, play the three-round Ehrenfeucht–Fraïssé game. After the first move, vertex transitivity permits Duplicator to match arbitrary roots. At the second move, if the selected element repeats the first, Duplicator repeats it as well; otherwise Duplicator matches the adjacency bit and the full third-vertex pattern mask, possible because the spectra agree and vertex transitivity moves a realizing pair to any specified first endpoint. At the third move, she either copies an equality to a previous element or uses the matched mask to choose a new element with the same adjacency pattern to both previously chosen elements. If the second move repeated the first, existence of a neighbor or nonneighbor is determined by the projection of the common nonempty pair spectra onto its adjacency bit, so this case also works; if the spectrum is empty, both graphs are singletons. The pebbled partial map is an isomorphism, proving three-round equivalence and therefore agreement on all sentences of rank at most three.

**Step 2: exact third-vertex counts in Hamming graphs.** Assume \(q\ge2\), put \(N=q^d\), \(r=d(q-1)\), and let two vertices be at Hamming distance \(h\). For \(a,b\in\{0,1\}\), let \(c_{ab}(h)\) count distinct third vertices \(z\) having adjacency pattern \((a,b)\) to the ordered pair. Every vertex has degree \(r\). A pair at distance one has exactly \(q-2\) common neighbors (alter its differing coordinate to a third symbol); a pair at distance two has exactly two (change either differing coordinate to its counterpart); and a pair at distance at least three has none. Subtracting the selected pair and its common and exclusive neighbors gives, with \(c_{01}=c_{10}\),
\[
\begin{array}{c|ccc}
 h&c_{11}&c_{10}=c_{01}&c_{00}\\\hline
 1&q-2&(d-1)(q-1)&q^d+q-2d(q-1)-2\\
 2&2&d(q-1)-2&q^d-2d(q-1)\\
 h\ge3&0&d(q-1)&q^d-2d(q-1)-2.
\end{array}
\]
Only the first row occurs when \(d=1\), the first two when \(d=2\), and all three when \(d\ge3\). All counts are integers and nonnegative in the ranges where their rows occur.

**Step 3: positivity is sharp.** For \(d,q\ge2\), the first-row \(c_{10}\) is positive, while its \(c_{11}\) is positive exactly for \(q\ge3\). The second-row \(c_{10}\) is zero only at \((d,q)=(2,2)\); its \(c_{11}=2\) is always positive. The last-row \(c_{10}\) is positive, and \(c_{11}=0\).

The three potentially vanishing counts \(c_{00}\) are, respectively,
\[
F_1(d,q)=q^d+q-2d(q-1)-2,\quad
F_2(d,q)=q^d-2d(q-1),\quad
F_3(d,q)=q^d-2d(q-1)-2.
\]
For \(d,q\ge2\), both \(F_1,F_2\) vanish at \((2,2)\) and are strictly positive elsewhere. For \(d\ge3,q\ge2\), \(F_3\) vanishes at \((3,2)\) and is strictly positive elsewhere. To prove the assertions without extrapolating finite data, note that each function increases strictly with \(d\), because
\[
F_i(d+1,q)-F_i(d,q)=(q-1)(q^d-2)>0.
\]
For the same fixed \(d\), the increase from \(q\) to \(q+1\) is \((q+1)^d-q^d-2d\) for \(F_2,F_3\), and one more for \(F_1\), all positive for \(d,q\ge2\). The base values stated above prove exactly the claimed zero sets. Reading the positive entries as the four mask bits gives the eight spectra in the Finding table. They are pairwise distinct, so Step 1 proves both completeness and sharpness of the classification. In class 8, the smallest graph has \(d=q=3\), hence \(3^3=27\) vertices.

**Step 4: comparison with Johnson graphs.** Replace Hamming distance by Johnson distance \(h=|A\setminus B|\). The Johnson graph has \(N=\binom nk\) vertices and degree \(r=k(n-k)\). Two distinct vertices at Johnson distance one have \(n-2\) common neighbors, at distance two have four, and at larger distance have none. Consequently the respective triples \((c_{11},c_{10}=c_{01},c_{00})\) are
\[
\begin{array}{c|ccc}
1&n-2&r-n+1&N+n-2r-2\\
2&4&r-4&N-2r+2\\
h\ge3&0&r&N-2r-2.
\end{array}
\]
When \(k=2,n\ge6\), only distances one and two occur; all four third-vertex patterns have positive counts in both rows. Hence \(\Sigma(J(n,2))=\{(1,15),(0,15)\}\), matching class 7. When \(n\ge7\) and \(3\le k\le n-3\), all counts in rows one and two are positive; row three has exactly the three non-common-neighbor patterns. Indeed \(N-2r-2>0\): it is 9 at \((n,k)=(7,3)\), and for \(n\ge8\) it follows from \(\binom nk\ge\binom n3\), \(r\le n^2/4\), and \(\binom n3-n^2/2-2>0\). Thus the Johnson spectrum matches class 8. Step 1 proves both cross-family equivalences.

## Verification

Run `python3 checker.py` using Python's standard library. The checker independently constructs the adjacency graph for every tested Hamming and Johnson parameter pair with at most 800 vertices, computes every third-vertex mask from actual adjacency sets for a fixed root, and compares the result against the formulas. It also checks that the eight Hamming classes have eight distinct spectra, and verifies the two Johnson–Hamming coincidences on representative parameter values. The current execution returned:

`RANK_THREE_HAMMING_CHECKS_OK direct_graph_checks= 116 classes= 8`

The finite checks corroborate the formulas and do not constitute the uniform proof for unbounded \(d,q,n,k\); Steps 1–4 give that proof. An exact two-parameter classification of the full first-order theories is not claimed.

## Relationship to prior work

Benediktsson, Macpherson and Adler's October 2026 study of Johnson graphs proves completeness and stability of a Johnson limit theory and gives a general Ehrenfeucht–Fraïssé bound; its final section explicitly identifies Hamming graph limit theories as a direction for future work. It does not state an exact three-round classification for Hamming graphs or the two cross-family equivalences. The earlier Hamming/Johnson VC-dimension and VC-density paper and Benediktsson's thesis discuss neighborhood geometry and the model-theoretic prospects of Hamming graphs, but their inspected results do not determine these low-rank logical spectra. This finding is therefore a **sharp bounded-depth contribution**, not a solution of the full Hamming limit-theory problem.

## Limitations

Rank three is essential: larger quantifier ranks can distinguish members of each listed class, and neither eventual full elementary equivalence nor an all-rank uniform convergence theorem is established. All formulas use the pure graph language; naming coordinates or supplying counting quantifiers changes the statement. The minimality of 27 vertices is only among Hamming graphs with the stated rank-three theory. Literature searches do not establish absolute historical priority; more general earlier theorems about vertex-transitive graphs or association schemes might subsume parts of the classification. No independent mathematical audit has been performed.

## References

1. B. G. Benediktsson, D. Macpherson, I. Adler, *Model Theory of Johnson Graphs*, arXiv:2610.40054v1, first submitted 2026-10-29, especially Theorem 1.0.4 and Section 6.
2. I. Adler, B. G. Benediktsson, D. Macpherson, *Vapnik–Chervonenkis dimension and density on Johnson and Hamming graphs*, Discrete Applied Mathematics 312 (2022), 29–44, DOI:10.1016/j.dam.2021.09.017.
3. B. G. Benediktsson, *Model-theoretic methods for algorithmically tame graph classes*, doctoral thesis, University of Leeds, 2022, especially Chapters 6–7, https://etheses.whiterose.ac.uk/id/eprint/30660/1/Thesis.pdf.
4. A. Ehrenfeucht, *An application of games to the completeness problem for formalized theories*, Fundamenta Mathematicae 49 (1961), 129–141.
