# A sharp two-fifths VC law for inclusion-minimal domination on paths

## Finding
Let \(P_n\) be the path on \(n\) labeled consecutive vertices, and let \(\mathcal D_n\) consist of the characteristic functions of **all inclusion-minimal dominating vertex sets** of \(P_n\), queried by vertex membership. There is no minimum-cardinality restriction. For every integer \(n\ge0\), with the empty path interpreted in the usual way,
\[
\boxed{\operatorname{VCdim}(\mathcal D_n)=\left\lfloor\frac{2n+2}{5}\right\rfloor.}
\]
In addition, every coefficient of the complete shattered-support polynomial \(\Phi_n(z)=\sum_{S\text{ shattered}}z^{|S|}\) is given by an explicit **206-state, two-letter deterministic transfer system**, specified algorithmically below and in the standalone `verify.py`. Consequently the bivariate series is rational:
\[
\boxed{\sum_{n\ge0}\Phi_n(z)t^n=e_0^{\mathsf T}\bigl(I-t(T_0+zT_1)\bigr)^{-1}a.}
\]
Here \(T_0,T_1\) are explicit zero-one transition matrices of size \(206\), \(e_0\) is the initial-state indicator, and \(a\) marks terminal accepted states; the defining finite construction is given in the proof. In particular,
\[
\Phi_{11}(z)=1+11z+51z^2+98z^3+48z^4,
\quad
\Phi_{13}(z)=1+13z+74z^2+201z^3+213z^4+48z^5.
\]
The sharp VC formula extends the previously checked small-path dimensions to **every** path length.

## Assumptions and scope
All graphs are finite, simple, undirected, and vertex-labeled. A set \(D\subseteq V(P_n)\) dominates when every vertex lies in \(D\) or has a neighbor in \(D\). It is inclusion-minimal when no proper subset still dominates. For an arbitrary support \(S\subseteq V(P_n)\), its trace family is \(\{D\cap S:D\in\mathcal D_n\}\); \(S\) is shattered precisely when this equals \(2^S\). The empty graph has the single empty dominating set and VC dimension zero. The theorem does not concern minimum-cardinality dominating sets, maximal independent sets alone, or online dimension.

## Proof
**1. A five-position local verifier.** Write the membership bits of \(D\) as \(d_0,\ldots,d_{n-1}\), with \(d_i=0\) outside the path. For every genuine vertex \(i\), domination requires \(d_{i-1}+d_i+d_{i+1}\ge1\). Furthermore, a dominating set is minimal if and only if each selected vertex \(i\) has a *private neighbor*: some genuine \(j\in\{i-1,i,i+1\}\) satisfying \(d_{j-1}+d_j+d_{j+1}=1\). This is equivalent to nonremovability, because deletion of \(i\) loses domination exactly at such a vertex \(j\).

We process genuine bits from left to right, keeping the last four bits \(h\in\{0,\ldots,15\}\), oldest first, and a phase \(p\in\{0,1,2,3\}\) equal to the number of genuine bits seen, capped at three. There are \(64\) possible local states. When appending a genuine bit \(b\), if \(p\ge2\), inspect the centered five-bit window consisting of those four bits followed by \(b\). Its middle vertex must satisfy domination and (if selected) the private-neighbor condition. At the first checked vertex, exclude the nonexistent candidate to its left. Append two artificial right zeros at the end to check the final two genuine centers, excluding the nonexistent right private-neighbor candidate on the last check. A failed local test discards the state. The executable function `edge(s,b,pad)` is the precise complete transition specification, including the boundaries. A genuine \(n\)-bit word survives the two finishing checks if and only if it represents an inclusion-minimal dominating set of \(P_n\).

**2. Determinization over all labels.** Represent any nonempty set \(Q\) of feasible local states by a \(64\)-bit integer, and write \(\delta_b(Q)\) for the union of their surviving successors upon reading bit \(b\). For a candidate support indicator, maintain a finite *family* \(F\) of these state-subsets: each member corresponds to one assignment of all support labels seen so far, while nondeterminism within that member represents unconstrained vertex choices. Initially \(F=\{\{(p,h)=(0,0)\}\}\). At a position outside the support, replace each \(Q\in F\) by \(\delta_0(Q)\cup\delta_1(Q)\). At a support position, replace each \(Q\) by **both** \(\delta_0(Q)\) and \(\delta_1(Q)\). Identical resulting subsets can be merged. If any resulting subset is empty, the support is irreversibly rejected. At the end, accept exactly when every member \(Q\in F\) has a surviving path through the two right-padding checks.

Induction on the scanned length proves that the family contains exactly the local-state possibilities for *each* label assignment to the queried positions. Therefore these transitions recognize exactly the shattered support indicators, not an over- or under-approximation. A breadth-first traversal of these mathematically specified transitions, starting from the initial family and omitting the rejecting sink, produces **exactly 206 reachable families**. Of these, 140 pass the final test; 79 of the 412 marked/unmarked outgoing edges lead to the sink. Index the families by this deterministic breadth-first discovery order, processing unmarked before marked. Define \((T_b)_{uv}=1\) when reading support mark \(b\) sends family \(u\) to family \(v\), and zero otherwise. The transfer identity in the finding follows from ordinary weighted path counting; no truncated search or guessed rational function is used.

**3. Infinite-length maximum by an exact finite certificate.** For a reachable family \(v\), let \(w_n(v)\) be the maximum number of marked positions in an \(n\)-bit support prefix ending at \(v\), with \(-\infty\) if unreachable. The recurrence is
\[
 w_{n+1}(v)=\max_{u\to v\text{ with mark }b}\bigl(w_n(u)+b\bigr),
\]
with only the initial family assigned zero at length zero. The maximum over final-accepted \(v\) is precisely the VC dimension at length \(n\). The attached standard-library checker rebuilds all 206 families and all transitions from the five-window rules, then evaluates exact integer vectors and verifies, **for every one of the 206 state-vector coordinates (including the value \( -\infty \) for states not reached at that exact length), not merely for the final maximum**, the five identities
\[
 w_{n+5}(v)=w_n(v)+2\qquad(n=16,17,18,19,20).
\]
These five complete statewise identities propagate by the max-plus recurrence to every \(n\ge16\): the equality at one length implies the equality at the next, hence the first equality alone suffices for induction once verified, and the five checks provide redundant boundary coverage. At length 16, exactly 128 state values are finite and the other 78 equal \( -\infty \); the componentwise equality includes all 206 values under the standard convention \( -\infty+2=-\infty \). The direct base calculation for \(n=0,1,\ldots,20\) gives VC dimensions
\[
 0,0,1,1,2,2,2,3,3,4,4,4,5,5,6,6,6,7,7,8,8.
\]
They agree with \(\lfloor(2n+2)/5\rfloor\). This expression also increases by exactly two when \(n\) increases by five. Induction proves the boxed formula for every integer \(n\ge0\).

**4. Finite-certificate integrity and independent direct checks.** The graph is regenerated from the local definitions, not read from a hard-coded adjacency file. In breadth-first order the compact transition-pair array has SHA-256 `745e40a73b2b4c98aa3dee965bd42ffe216cefd75c1ccb361d3d905f7650bd1d`. An independent direct implementation enumerates all subsets of \(P_n\), tests domination by neighborhoods and minimality by literal vertex deletion, and counts the traces on **every** support for \(0\le n\le13\). Every coefficient matches the transfer computation. These finite comparisons test the implementation; the proof for arbitrarily large \(n\) rests instead on the exhaustive 206-state transition construction, the statewise period certificate, and the preceding induction.

## Verification
Execute `python3 verify.py` in the same directory as the accompanying `verification_output.txt` (Python 3 standard library only). It terminates with `ALL_CHECKS_PASS` and verifies the exact graph digest, 206 reachable families, 140 accepting families, 79 rejecting transitions, five complete statewise max-plus identities, all dimensions through length 20, and all shattered-face coefficients through length 13. The output file records the actual execution. No solver, numerical tolerance, external table, or unprovided artifact is required.

## Relationship to prior work
A 2018 study by Bonamy, Defrain, Heinrich, Raymond and Pilipczuk treats **enumeration** of inclusion-minimal dominating sets and the associated transversal problem, not their vertex-trace VC dimension. Mofidi's 2022 manuscript studies dominating reconfiguration graphs, complements of minimal dominating sets, median graphs and partial cubes, but not the all-length shattering capacity of the family of minimal sets. Hernández-Gómez and collaborators (2020) fully characterize **minimum-cardinality** dominating sets of paths, which form a different, generally smaller family. Guingona, Kolesnikov, Nierwinski and Soucy (2021) treat the VC and online dimensions of **linear zero-set families**, with no implication covering path domination concepts. Mary (2024) studies enumeration of minimal transversals when the **input hypergraph** has bounded VC dimension; its parameter is not the VC dimension of the output family of minimal transversals, so the theorem does not imply the present path-specific formula.

The closest accessible previously published mathematical record, *First VC–Littlestone separation for minimal dominating sets of paths* (2026), computes exact dimensions only through length 11 and an unbounded gap on disjoint copies of that path; its full result explicitly leaves larger **connected** path dimensions open. The present theorem determines those static dimensions for every connected path and supplies an all-coefficient transfer system. The separate record *A periodic shattering law for minimum independent dominating sets of paths* concerns minimum-cardinality **independent** dominating sets, not all inclusion-minimal dominating sets; its bounded VC rank does not imply the result here. A prior shattering enumerator for maximal independent sets of paths concerns the independent subclass and is not a stronger formula for the present family.

## Limitations
The transfer representation has 206 states rather than a small displayed scalar rational numerator and denominator; it is nevertheless a complete finite exact specification of the generating function. The proof of the sharp global bound includes a reproducible **finite computer-assisted certificate** whose state graph and base vectors are constructed and checked in the supplied Python source. It is not a paper-and-pencil classification of all shattered supports. It does not determine the Littlestone dimension of the connected-path class for arbitrary lengths. Literature priority is judged against the sources actually inspected and searched; equivalent unpublished or differently indexed results remain possible. This finite-state proof does not constitute independent experimental or expert validation.

## References
1. M. Bonamy, O. Defrain, M. Heinrich, J.-F. Raymond and M. Pilipczuk, *Enumerating minimal dominating sets in \(K_t\)-free graphs and variants*, first posted October 1, 2018, https://arxiv.org/abs/1810.00789.
2. A. Mofidi, *On dominating graph of graphs, median graphs and partial cubes, and graphs in which complement of every minimal dominating set is minimal dominating*, first posted December 8, 2022, https://arxiv.org/abs/2212.04570.
3. J. C. Hernández-Gómez, G. Reyna-Hérnandez, J. Romero-Valencia and O. R. Cayetano, *Transitivity on Minimum Dominating Sets of Paths and Cycles*, *Symmetry* 12 (2020), 2053, published December 11, 2020, https://doi.org/10.3390/sym12122053.
4. V. Guingona, A. Kolesnikov, J. Nierwinski and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, first posted September 10, 2021, https://arxiv.org/abs/2109.04805.
5. *First VC–Littlestone separation for minimal dominating sets of paths*, public mathematical record, October 26, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-first-vc-littlestone-separation-for-minimal-dominating-sets-of-p--85d3ecbad804.
6. *A periodic shattering law for minimum independent dominating sets of paths*, public mathematical record, November 8, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-periodic-shattering-law-for-minimum-independent-dominating-set--ab94895bb7a2.
7. A. Mary, *Enumeration of minimal transversals of hypergraphs of bounded VC-dimension*, arXiv:2407.00694, first posted June 30, 2024, https://arxiv.org/abs/2407.00694.
