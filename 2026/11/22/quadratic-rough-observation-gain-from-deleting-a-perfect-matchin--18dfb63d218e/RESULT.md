# Quadratic rough-observation gain from deleting a perfect matching in balanced bicliques

## Finding

**Theorem (exact observation and collision census).** Fix an integer \(n\ge3\). Let \(G_n\) be the crown graph obtained from the complete bipartite graph on labelled parts \(A=\{a_1,\dots,a_n\}\) and \(B=\{b_1,\dots,b_n\}\) by deleting exactly the edges \(a_i b_i\) for \(1\le i\le n\). Equip its \(2n\) vertices with the reflexive symmetric *closed-neighborhood tolerance* \(R\). For every vertex subset \(X\) put
\[
U(X)=\{v:N[v]\cap X\ne\varnothing\},\qquad
L(X)=\{v:N[v]\subseteq X\},
\]
and let \(\mathscr R_n=\{(L(X),U(X)):X\subseteq A\sqcup B\}\) denote the set of *distinct* approximation pairs. Then
\[
\boxed{|\mathscr R_n|=4\cdot2^n+2n^2-5.}
\]
The comparison family \(K_{n,n}\) has exactly \(4\cdot2^n-5\) approximation pairs. Thus deleting one perfect matching creates **exactly \(2n^2\) additional distinct observations**, although the removed edge family is only linear in \(n\).

More strongly, write \(\operatorname{fib}(P)=|\{X:(L(X),U(X))=P\}|\). There is a single central observation \((\varnothing,A\sqcup B)\), whose fiber has cardinality
\[
\boxed{c_n=4^n-(2n+4)2^n+2n^2+4n+6.}
\]
There are \(4n\) distinguished noncentral observations, identified in the proof, whose fibers all have size
\[
\boxed{d_n=2^{n-1}-n.}
\]
Every remaining \(4\cdot2^n+2n^2-4n-6\) noncentral observation has a singleton fiber. At \(n=3\), \(d_3=1\), so *all* noncentral fibers are singleton; for \(n\ge4\), these \(4n\) are precisely the noncentral fibers larger than one. The small exceptional crown graphs satisfy \(|\mathscr R_1|=4\) and \(|\mathscr R_2|=9\).

## Assumptions and scope

All graphs are finite, undirected, simple before adjoining reflexive loops to form their approximation relations. Both lower and upper approximations use the **same** reflexive closed-neighborhood relation; neither uses open neighborhoods, graph-orbit equivalence, or a different covering operator. Vertex labels and the deleted perfect matching are fixed, but the count depends only on \(n\). Observation fibers count source subsets \(X\), not isomorphism classes of subsets. For the main formulas, \(n\ge3\) is essential. The comparison to \(K_{n,n}\) is made on the same labelled vertex set, with the same reflexivity convention.

## Proof

**1. Replace the lower approximation by a second upper approximation.** Let \(V=A\sqcup B\). Because \(R\) is symmetric and reflexive,
\[
L(X)=V\setminus U(V\setminus X).
\]
Therefore the correspondence \(X\mapsto (L(X),U(X))\) has exactly the same fiber partition as \(\Phi(X)=(U(X),U(V\setminus X))\). We count the image and the inverse-fiber sizes of \(\Phi\).

Identify both shores with \([n]=\{1,\dots,n\}\). If \(X\) selects index sets \(S\subseteq[n]\) on the \(A\)-shore and \(T\subseteq[n]\) on the \(B\)-shore, write \(C(S,T)=(U(X)\cap A,U(X)\cap B)\), using the shore index identifications. Directly from the closed neighborhoods,
\[
\begin{aligned}
i\in C_A(S,T)&\iff i\in S\ \text{or}\ T\setminus\{i\}\ne\varnothing,\\
i\in C_B(S,T)&\iff i\in T\ \text{or}\ S\setminus\{i\}\ne\varnothing.
\end{aligned}
\tag{1}
\]
Thus, when \(|T|\ge2\), \(C_A(S,T)=[n]\); when \(T=\{j\}\), \(C_A(S,T)=[n]\setminus\{j\}\) unless \(j\in S\); and when \(T=\varnothing\), \(C_A(S,T)=S\). The other coordinate has the symmetric description. In what follows let \(F=[n]\) and \(F_i=F\setminus\{i\}\).

**2. Classify every nonfull upper observation.** Formula (1) gives this disjoint list of all values \(C(S,T)\ne(F,F)\):

- \((\varnothing,\varnothing)\), one value;
- \((\{i\},F_i)\) and \((F_i,\{i\})\), \(2n\) values;
- \((H,F)\) and \((F,H)\), for all \(H\subseteq F\) with \(2\le|H|\le n-1\), yielding \(2(2^n-n-2)\) values;
- \((F_j,F_i)\) for distinct indices \(i,j\), yielding \(n(n-1)\) values.

For completeness: if one shore of the input is empty, these are exactly the first three families (with the full value omitted); if both input shores are nonempty, a nonfull value requires a singleton shore whose excluded matching index does not occur in the other shore. Two distinct singleton shores yield the fourth family; one singleton and at least two selected vertices on the other shore yield a co-singleton value already in the third family. This exhausts every input, and the listed outputs are pairwise distinct for \(n\ge3\). Hence the number of nonfull coverage values is
\[
H_n=1+2n+2(2^n-n-2)+n(n-1)=2^{n+1}+n^2-n-3.
\tag{2}
\]
Each of these \(H_n\) values has an input whose complement has full coverage. Explicit representatives are respectively \((S,T)=(\varnothing,\varnothing)\), \((\{i\},\varnothing)\) and its mirror, \((H,\varnothing)\) and its mirror, and \((\{i\},\{j\})\) for \(i\ne j\). The complements have full coverage by (1), since \(n-1\ge2\).

**3. The only pairs with both coverages nonfull.** Suppose \(C(S,T)\ne(F,F)\) and \(C(F\setminus S,F\setminus T)\ne(F,F)\). If either \(S\) or \(T\) is empty, (1) shows the complement has full coverage whenever the original coverage is nonfull. Otherwise nonfull coverage requires a singleton \(S=\{i\}\) with \(i\notin T\), or the symmetric condition. If \(S=\{i\}\), then its complement has at least two elements; for the complementary coverage to fail, \(F\setminus T\) must be the singleton \(\{i\}\), which means \(T=F_i\). The symmetric case exchanges the shores. Conversely all these inputs work. Therefore there are precisely \(2n\) such input sets,
\[
(S,T)=(\{i\},F_i)\quad\text{or}\quad (F_i,\{i\}),\qquad i\in F,
\tag{3}
\]
and their \(\Phi\)-values are mutually distinct, namely \(((F,F_i),(F_i,F))\) and the reverse. Each has a singleton fiber.

Every nonfull upper value can be paired with a full complementary value by Step 2. The \(H_n\) values on either side of \(\Phi\) give \(2H_n\) distinct ordered pairs; Step 3 contributes \(2n\), and there is exactly one pair with both coverages full. Thus
\[
|\mathscr R_n|=1+2H_n+2n=4\cdot2^n+2n^2-5,
\]
proving the main census.

**4. Complete inverse-fiber classification.** For a given nonfull coverage value \(P\), consider inputs satisfying \(C(S,T)=P\) with complementary coverage full. The explicit classification in Step 2 shows the representative is unique, except when \(P=(F,F_i)\) or \(P=(F_i,F)\). For instance the inputs with \(C(S,T)=(F,F_i)\) are exactly
\[
(S,T)=(\varnothing,F_i)\quad\text{or}\quad
(S,T)=(\{i\},T),\quad T\subseteq F_i,\quad |T|\ge2.
\]
The unique input \((\{i\},F_i)\) from the second group has *nonfull* complementary coverage, so it is excluded from this one-full fiber. The first group contributes one input, and the remaining second-group choices contribute \(\sum_{k=2}^{n-2}\binom{n-1}{k}\). Therefore
\[
\operatorname{fib}((P,(F,F)))=1+\sum_{k=2}^{n-2}\binom{n-1}{k}=2^{n-1}-n=d_n.
\]
The mirror \((F_i,F)\) and the exchange of the two entries in \(\Phi\) give \(4n\) distinguished fibers of this size. All \(2n\) both-nonfull observations, and every other one-full observation, have singleton fibers. There are exactly \(4\cdot2^n+2n^2-4n-6\) other noncentral values, so counting the \(4^n\) input subsets forces the single central fiber to have cardinality
\[
\begin{aligned}
c_n&=4^n-4n(2^{n-1}-n)-(4\cdot2^n+2n^2-4n-6)\\
&=4^n-(2n+4)2^n+2n^2+4n+6.
\end{aligned}
\]
This proves the complete multiplicity distribution, including \(n=3\).

**5. Comparison with the undeleted biclique.** In \(K_{n,n}\), full upper coverage occurs whenever both input shores are nonempty, or when exactly one shore is entirely selected. The nonfull coverage values are just \((\varnothing,\varnothing)\), \((S,F)\) and \((F,T)\) for \(\varnothing\ne S,T\subsetneq F\), a total of \(2^{n+1}-3\). Each has a complement with full coverage, and no input gives two nonfull complementary coverages. Thus the existing biclique count follows directly:
\[
|\mathscr R(K_{n,n})|=1+2(2^{n+1}-3)=4\cdot2^n-5.
\]
Subtracting yields the exact quadratic increase. At \(n=1\), the crown graph has two isolated points and hence four distinct pairs. At \(n=2\), it has two disconnected edges, each of which supplies exactly three Pawlak statuses, giving nine pairs.

## Verification

The accompanying `verify.py` uses only Python's standard library and constructs each reflexive neighborhood directly from graph edges. It enumerates all input subsets for the crown graphs through \(n=9\) and the undeleted bicliques through \(n=7\), computing lower and upper approximations *independently* from their definitions. It checks the main and boundary counts, the full upper-image classification, the precise \(2n\) two-nonfull cases, and the entire inverse-fiber multiplicity distribution. Execute `python3 verify.py` in the same directory. The observed output is `VERIFY_OK family_cases=15 crown_subsets=349524`. These finite checks are not used as a proof of the all-\(n\) statements; Steps 1–5 provide the general proof.

For reference, the counts \(|\mathscr R_n|\) for \(n=1,\dots,9\) are \(4,9,45,91,173,323,605,1147,2205\), and the special central fiber sizes for \(n=3,\dots,6\) are \(20,118,652,3174\).

## Relationship to prior work

Järvinen and Radeleczki establish the general rough-set framework for reflexive symmetric tolerances, with structural theorems about their approximation orders and completions. Syau, Liau, and Lin investigate categorical structures for equivalence-based rough approximations and motivate extensions beyond equivalence relations. Hafez and collaborators discuss graph-based approximation constructions and foundational limitations. None of those general structural statements directly gives this precise graph-family image or inverse-fiber census.

An existing complete-multipartite tolerance classification gives the cardinality \(4\cdot2^n-5\) for \(K_{n,n}\), and the present work treats that baseline as prior knowledge. The crown graph \(K_{n,n}\setminus M_n\) with \(n\ge3\) is not complete multipartite: its nonadjacency is not a disjoint union of equivalence classes. Existing exact rough-count identities for **dual incidence posets** count a different relation on a different vertex set and do not specialize to the graph's reflexive-neighborhood tolerance. The new claim is the quadratic *difference* under matching deletion and the complete observation-fiber distribution. An unlocated equivalent specialized enumeration remains a priority risk.

## Limitations

The formulas are for a full deleted perfect matching in a balanced biclique, not arbitrary partial matchings, unbalanced bicliques, or arbitrary graphs. The distinguished fiber size formula counts full inverse images, not probability-normalized multiplicities. It does not assert that the resulting rough-set order is a lattice, nor does it identify its full order-theoretic structure. Small orders \(n=1,2\) require the separate values stated above. No claim of an application-specific improvement in rough-data processing is made merely from the exact count.

## References

1. Y.-R. Syau, C.-J. Liau and E.-B. Lin, *Categorical Structures in Rough Set Theory and Information Systems*, Mathematics 14 (2026), 369, first public 2026-01-22, DOI: 10.3390/math14020369. https://www.mdpi.com/2227-7390/14/2/369
2. H. Hafez, K. A. Dib, R. El-Shanawany and A. A. El Atik, *A study on rough graphs*, Mathematical and Applied Sciences in Engineering 7 (2026), DOI: 10.5206/mase/23201, publicly listed 2026-03-14. https://ojs.lib.uwo.ca/index.php/mase/article/view/23201
3. J. Järvinen and S. Radeleczki, *Rough sets determined by tolerances*, arXiv:1303.6332 (2013), https://arxiv.org/abs/1303.6332
4. *The rough-set lattice of a complete multipartite tolerance: normal form, symmetries, and reconstruction*, publicly accessible mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-the-rough-set-lattice-of-a-complete-multipartite-tolerance-norma--b1b4dc7b9990
5. *Rough-set cardinalities of graph-incidence orders are a Tutte evaluation*, publicly accessible mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-rough-set-cardinalities-of-graph-incidence-orders-are-a-tutte-ev--80b1c1990293
6. A. El Atik, A. Nawar and M. Atef, *Rough approximation models via graphs based on neighborhood systems*, *Granular Computing* 6 (2021), 1025–1035, DOI:10.1007/s41066-020-00245-z. https://doi.org/10.1007/s41066-020-00245-z
