# Zero-forcing polynomial of cycle squares from a degree-two induced-subgraph criterion

## Finding

For each integer \(n\ge 7\), let \(H_n=C_n^2\) have vertex set \(\mathbb Z/n\mathbb Z\) and edges between vertices of cyclic distance \(1\) or \(2\). A vertex subset \(S\) is an ordinary zero-forcing set of \(H_n\) **if and only if** the induced subgraph \(H_n[S]\) has a vertex of degree at least \(3\). Thus every failed zero-forcing set induces maximum degree at most \(2\).

Define the full cardinality polynomials
\[
\mathcal Z_n(z)=\sum_{S\text{ zero-forcing}}z^{|S|},\qquad
\mathcal F_n(z)=\sum_{S\text{ not zero-forcing}}z^{|S|}.
\]
Set
\[
D(u,z)=1-u-zu^2-z^2u^3-z^3u^5+z^4u^7+z^5u^8.
\]
Then **every coefficient at every order \(n\ge7\)** is specified by
\[
\boxed{\mathcal Z_n(z)=(1+z)^n-[u^n]\frac{u+2zu^2+3z^2u^3+5z^3u^5-7z^4u^7-8z^5u^8}{D(u,z)}.}
\]
In particular, the minimum zero-forcing size is \(4\), there are exactly \(3n\) minimum zero-forcing sets, and the largest cardinality of a failed set is \(\lfloor2n/3\rfloor\). The latter two extremal quantities are stated as deductions of the complete characterization, not as standalone originality claims.

## Assumptions and scope

All graphs are finite, simple and undirected. Ordinary zero forcing begins with the vertices of \(S\) black. A black vertex with **exactly one white neighbor** may recolor that neighbor black; the set is zero-forcing when a sequence of legal steps colors all vertices. The word "failed" means not zero-forcing; it does not refer to the skew forcing rule. The results hold for **all integers \(n\ge7\)**. The graph \(H_n\) is four-regular in this range, and no claim for smaller orders is made. The polynomial variables \(u,z\) are formal indeterminates; \([u^n]\) denotes formal coefficient extraction over \(\mathbb Z[z]\).

## Proof

**Step 1: a five-consecutive-vertex propagation lemma.** If five consecutive cyclic vertices are black, then all vertices can be forced black. Indeed, while a nonblack vertex remains, take a maximal consecutive black interval \([a,b]\) containing those five vertices, where the interval is viewed in cyclic order. Its vertex \(b-1\) has four neighbors \(b-3,b-2,b,b+1\); the first three are black. If \(b+1\) is white, it can be forced. If \(b+1\) is already black, enlarge the consecutive interval without forcing. Repeat to finish. This argument applies without assuming that all other vertices are initially white.

**Step 2: complete forcing-set characterization.** A vertex \(v\in S\) having at least three neighbors in \(S\) has either exactly three (then it immediately forces its fourth neighbor) or all four black. In either case all five vertices \(v-2,v-1,v,v+1,v+2\) become black, and Step 1 completes the forcing. Conversely, if every vertex of \(H_n[S]\) has degree at most two, then every black vertex has at least two white neighbors at the initial stage. No first forcing step exists, so \(S\) is failed. This proves the equivalence, including \(S=\varnothing\).

**Step 3: a finite-state exact enumerator.** Encode \(S\) by its cyclic binary characteristic word \(b_0b_1\cdots b_{n-1}\), with a one for a black vertex. By Step 2 this word represents a failed set exactly when none of its cyclic length-five windows \((a,b,c,d,e)\) has \(c=1\) and \(a+b+d+e\ge3\). Use the \(16\) four-bit states \(s=(a,b,c,d)\), indexed by \(0,\ldots,15\), and the \(16\times16\) matrix \(T(z)\). For each \(e\in\{0,1\}\), permit the transition \((a,b,c,d)\to(b,c,d,e)\) with weight \(z^e\) if and only if \(c=0\) or \(a+b+d+e\le2\), and otherwise assign weight zero. Entries sum transition weights if necessary. For \(n\ge7\), every cyclic characteristic word yields exactly one labeled closed state walk of length \(n\), with total weight \(z^{|S|}\), and conversely. Therefore
\[
\mathcal F_n(z)=\operatorname{tr}(T(z)^n).
\]

**Step 4: evaluate the determinant (not just a symbolic transfer prescription).** Direct polynomial determinant computation gives
\[
\det(I-uT(z))=D(u,z).
\]
A fully specified exact integer-algebra reproduction of this identity is in `verify.py`: it computes all sixteen traces \(p_j(z)=\operatorname{tr}(T(z)^j)\) using path-counting dynamic programming, then uses Newton's identities \(jc_j=-\sum_{i=1}^jc_{j-i}p_i\), with \(c_0=1\), to reconstruct every coefficient in \(\det(I-uT(z))=\sum_{j=0}^{16}c_j(z)u^j\). It checks the displayed eight-degree polynomial coefficientwise, including the vanishing of all other terms. This is a finite exact identity over \(\mathbb Z[z]\), not interpolation or evidence from numerical cases.

For any square matrix over the polynomial ring, the formal trace-determinant identity is
\[
\sum_{n\ge1}\operatorname{tr}(T(z)^n)u^n=-u\,\partial_u\log\det(I-uT(z))
=-\frac{u\,\partial_uD(u,z)}{D(u,z)}.
\]
Expanding the derivative yields exactly the numerator stated in the finding. The identity and Step 3 establish the formula simultaneously for every \(n\ge7\). Since failed and successful sets partition the \(2^n\) subsets, their cardinality polynomials sum to \((1+z)^n\).

**Step 5: extremal consequences.** No black set of size at most \(3\) can have a black vertex with three black neighbors, whereas the choice of \(v\) and any three of its four neighbors gives a zero-forcing set of size \(4\). There are \(4n\) such centered choices. Any selected four-set has at most two possible qualifying centers; two centers occur exactly for four consecutive cyclic vertices (there are \(n\) such sets), and all other choices have one center. Hence exactly \(4n-n=3n\) distinct minimum sets.

For any failed set \(S\), each selected vertex has at least two unselected neighbors. The edges crossing the cut consequently satisfy \(2|S|\le e(S,V\setminus S)\le4(n-|S|)\), implying \(|S|\le\lfloor2n/3\rfloor\). Equality is attained by the following cyclic binary words, all of which have every selected vertex adjacent to at most two selected vertices: \((110)^k\) when \(n=3k\), \((110)^k0\) when \(n=3k+1\), and \((110)^k10\) when \(n=3k+2\). The boundary words here are valid for every \(n\ge7\), proving the failed-set maximum.

## Verification

The standalone standard-library program `verify.py` constructs the exact degree-polynomial transfer matrix implicitly from the stated five-window rule. It reconstructs \(\det(I-uT(z))\) by Newton identities over integer polynomials and checks every coefficient against \(D\). Separately, for each labeled cycle square of order \(7\) through \(14\), it exhaustively iterates all vertex subsets and compares (a) the original iterative ordinary zero-forcing rule, (b) the structural induced-degree criterion, and (c) the transfer-trace cardinality enumerator. It also checks both extremal corollaries. Its successful reproduction prints `VERIFY_OK transfer_states=16 determinant_degree_u=8 traced_powers=16 cycle_orders=7..14 exhaustive_subsets=32640 coefficient_and_forcing_checks=passed`.

The unrestricted proof depends on the finite exact determinant and the combinatorial equivalence; the finite graph census is an independent corroborating test and **not** the reason the statement holds at arbitrary order.

## Relationship to prior work

The AIM Minimum Rank–Special Graphs Work Group introduced ordinary zero forcing in *Zero forcing sets and the minimum rank of graphs* (available publicly on 2007-11-26, DOI 10.1016/j.laa.2007.10.009); its focus is the minimum size and matrix rank, not the complete order-by-order subset enumerator here. Boyer et al. introduced the zero-forcing polynomial framework in arXiv:1801.08910, studying several graph families; their treatment of ordinary cycles does not imply the square-of-cycle polynomial. Bermond and Peyrat studied induced subgraphs of powers of cycles (DOI 10.1137/0402039), but their published abstract gives a minimum-degree/size bound, not an enumerator of induced subgraphs of maximum degree two. Later work by Gomez et al. (DOI 10.20429/tag.2024.110105) treats largest failed-set sizes for circulants; the largest-size corollary here may overlap that work and is not asserted to be novel by itself. Johnson et al. (DOI 10.3390/appliedmath5020032) address **skew** zero forcing of cycle powers and circulants, which has a different forcing rule.

## Limitations

Originality remains subject to possible earlier equivalent enumerations under the terminology of two-dependent subsets, binary circular words with forbidden local patterns, or induced maximum-degree-two subgraphs. One closely titled 1989 source on induced subgraphs of cycle powers and a later source on failed zero forcing in circulants were not available for full-text comparison; their abstracts were compared and their unresolved coverage risk is documented in the associated review. This result does not concern skew forcing or cycle powers beyond the second power, and no claim is made that the generic finite-state technique is new.

## References

1. AIM Minimum Rank–Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648, DOI: 10.1016/j.laa.2007.10.009. Full published article: https://draganstevanovic.wordpress.com/wp-content/uploads/2012/09/published-version2.pdf (first publicly available 2007-11-26).
2. K. Boyer et al., “The zero forcing polynomial of a graph,” arXiv:1801.08910 (first version 2018-01-26), https://arxiv.org/abs/1801.08910.
3. J.-C. Bermond and C. Peyrat, “Induced Subgraphs of the Power of a Cycle,” *SIAM Journal on Discrete Mathematics* 2 (1989), 452–455, DOI: 10.1137/0402039.
4. L. Gomez, K. Rubi, J. Terrazas, R. Flórez and D. Narayan, “Failed Zero Forcing Numbers of Trees and Circulant Graphs,” *Theory and Applications of Graphs*, DOI: 10.20429/tag.2024.110105.
5. A. Johnson, A. Vick, R. Flórez, D. Narayan, “Failed Skew Zero Forcing Numbers of Path Powers and Circulant Graphs,” *AppliedMath* 5 (2025), article 32, DOI: 10.3390/appliedmath5020032.
