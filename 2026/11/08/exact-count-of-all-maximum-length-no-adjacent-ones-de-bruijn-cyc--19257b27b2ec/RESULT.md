# Exact count of all maximum-length no-adjacent-ones de Bruijn cycles

## Finding

The known maximum-length constrained de Bruijn cycles for binary words without adjacent `11` contain precisely the cyclically admissible length-\(n\) words, whose number is the Lucas number \(L_n=F_{n-1}+F_{n+1}\). Their maximum size and uniquely determined factor support are **previous results** of Chee and collaborators (2024, after complementing the bits), not claims made here.

**Enumeration theorem.** For every integer \(n\ge2\), let \(C_n\) be the number of *all* maximum-length circular binary words, modulo cyclic rotation only, whose length-\(n\) windows are distinct and contain no internal `11`. Define the branch set
\[
B_n=\{v\in\{0,1\}^{n-1}:v\text{ has no internal `11` and starts and ends in }0\},
\qquad r=0^{n-1}.
\]
For each \(v\in B_n\) and bit \(b\in\{0,1\}\), create a distinguishable directed arc from \(v\) to the next branch vertex reached after shifting the bits of \(v\) left by one and appending \(b\), then repeatedly shifting left and appending `0` as long as the state is not in \(B_n\). Let \(A_n\) be the adjacency matrix of this directed multigraph, including multiplicity of parallel arcs. Then
\[
\boxed{\displaystyle C_n=\det\left((2I-A_n)_{B_n\setminus\{r\},\,B_n\setminus\{r\}}\right).}
\]
The determinant is exactly an integer and has order \(F_{n-1}-1\), instead of the \(F_{n+1}-1\) order of the uncontracted overlap graph. The convention for a zero-dimensional determinant gives \(C_2=1\). It computes the complete multiplicity of optimal cycles, not a lower bound or a subset of algorithmically constructed cycles.

Exact values through length \(15\), independently reproduced from the complete supplied artifacts, include:

| \(n\) | Already-known maximum cycle length \(L_n\) | Number of optimal cycles \(C_n\) |
|---:|---:|---:|
| 2 | 3 | 1 |
| 3 | 4 | 1 |
| 4 | 7 | 1 |
| 5 | 11 | 2 |
| 6 | 18 | 2 |
| 7 | 29 | 28 |
| 8 | 47 | 216 |
| 9 | 76 | 65,200 |
| 10 | 123 | 167,084,480 |
| 11 | 199 | 516,281,370,178,432 |
| 12 | 322 | 1,168,266,109,839,628,752,446,464 |

The exact large-integer counts for lengths \(13,14,15\) and all intermediate branch sizes appear in `counts.csv`. The cofactor counts for all lengths; the evaluated numerical census covers precisely \(2\le n\le15\).

## Assumptions and scope

Use the alphabet \(\{0,1\}\) with `11` forbidden as an adjacent pair inside each length-\(n\) window. In any *maximum-length* cycle, the factor set is the known complete set of length-\(n\) binary words having no `11` even across their own first/last boundary. The number \(C_n\) identifies cycles up to rotation but not reversal, complement, or transformations of labels. Distinct length-\(n\) words induce distinct labeled edges of the overlap graph. For the use of the directed matrix-tree and BEST theorems, repeated successor endpoints retain distinguishable arcs; this matters especially for small orders.

## Proof

**Known optimal support.** For reference, the result of Chee et al. (Corollaries 2.12 and 2.14 of arXiv:2403.01454, with zeros and ones complemented) says that the largest circuit containing distinct linearly no-`11` windows has length \(L_n\), and that every maximum circuit consists of exactly the cyclically admissible length-\(n\) factors. Hence the count of all optimal cycles is the count of Euler circuits of the *fixed* overlap digraph \(G_n\), which has vertices equal to linear length-\((n-1)\) no-`11` words and one arc per cyclically admissible length-\(n\) word. The earlier maximum/support statement is used as a premise rather than an original lemma.

**Degrees and forced transitions.** In \(G_n\), the indegree and outdegree of a vertex \(v\) both equal \(2\) if \(v\) begins and ends in `0`, and otherwise both equal \(1\). In the latter case its unique outgoing arc appends `0`. Following such forced arcs necessarily reaches the all-zero word after at most \(n-1\) appends, so it cannot loop indefinitely outside the branch set \(B_n\). The graph is strongly connected: from any vertex append zeros to reach \(r\), and from \(r\) append the symbols of any target length-\((n-1)\) no-`11` word; the intermediate length-\(n\) windows are all cyclically admissible. Standard Fibonacci counting gives \(|B_n|=F_{n-1}\).

**Bijection of rooted arborescences.** Fix \(r\) as root. In every directed in-arborescence of \(G_n\) directed toward \(r\), every nonbranch vertex necessarily selects its unique outgoing arc; the remaining choice is one of the two outgoing arcs from each nonroot branch. Following the forced corridor after each branch choice gives the two distinguishable arcs of the compressed graph \(H_n\). Conversely, any directed in-arborescence of \(H_n\) prescribes exactly one outgoing arc at each nonroot branch and all forced outgoing arcs elsewhere. It is acyclic and reaches \(r\): a directed cycle in the original mapping would include a branch, since forced-only paths reach a branch, and would project to a cycle of the compressed mapping. This is a genuine bijection of rooted in-arborescences even when two corridors merge or when compressed arcs are parallel.

**From trees to cycles.** Every vertex of \(G_n\) has outdegree \(1\) or \(2\), so the directed BEST theorem gives the number of edge-distinguished Euler circuits modulo choice of the starting edge as
\[
t_r(G_n)\prod_{v\in V(G_n)}(d^+(v)-1)!=t_r(G_n).
\]
Every Euler circuit spells exactly one circular binary word up to rotation; conversely the distinct cyclic factors determine one labeled-edge Euler circuit. The directed matrix-tree theorem and the arborescence bijection give
\[
t_r(G_n)=t_r(H_n)=\det((2I-A_n)_{\widehat r}),
\]
which is the asserted formula for \(C_n\). No finite search is used to establish this all-order identity.

## Verification

The embedded `count_cycles.cpp` independently builds the contracted graph using bit masks and computes its determinant modulo successive primes. CRT reconstruction stops only after the modulus product exceeds the rigorously proved bound \(2^{|B_n|-1}\) on the number of in-arborescences, making all reported integers exact. The program was compiled with a C++17 compiler and Boost.Multiprecision and generated the supplied `counts.csv` through order \(15\).

The separate Python `verify.py` has a string-based compressed graph and integer Bareiss determinant (reproducing all rows through \(15\)), an **uncontracted** integer Bareiss determinant (orders \(2\) through \(12\)), exhaustive minimum-deletion-support checks (orders \(2\) through \(7\), checking a known structural fact), and direct circular binary word enumeration up to order \(6\). These independent-method numerical checks passed. See `VERIFICATION.md` for exact replay commands.

## Relationship to prior work

Moreno–Matamala (2004 conference, 2007 arXiv manuscript) and Sawada–Williams–Wong (2016) supply the prescribed restricted-language universal-cycle context. **Chee, Etzion, Nguyen, Ta, Tran and Vu (2024) prove the full maximum-length and uniquely determined support theorem that was needed here**, including a specialized Fibonacci/Lucas size expression. Their Section 3 gives constructions of *many* optimal cycles and Section 4 enumerates their lengths and allowed words/necklaces; the inspected paper does **not** give an exact count of **all** optimal cycles. Thus neither their known maximum nor their uniqueness result is claimed here as a discovery. The ordinary BEST and matrix-tree formulas are also classical.

The new assessed contribution is the explicit all-order **forced-corridor compressed determinant for the complete population of optimal cyclic words**, with a direct bijective proof and an independently evaluated integer census. The 2024 construction lower bound on the number of sequences does not imply this exact distribution or the numerical count. An unindexed older full-tour census or an existing specialized cofactor simplification could still affect historical priority.

## Limitations

This is an exact *enumeration*, not a new characterization of maximum length or factor support. The count formula is determinant-defined rather than an elementary product. Numerical values are verified through order \(15\) only; larger orders are covered by the mathematical formula but not by this fixed-range implementation. All cycles are identified modulo rotation and retain other symmetries. The broader cases of longer forbidden runs and larger alphabets are not treated. Historical-priority comparison cannot rule out unindexed existing enumerations.

## References

1. E. Moreno and M. Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings*, arXiv:0711.1695, first version publicly submitted 2007-11-12. https://arxiv.org/abs/0711.1695 . Earlier conference antecedent: *Minimal de Bruijn Sequence in a Language with Forbidden Substrings*, WG 2004, DOI 10.1007/978-3-540-30559-0_14.
2. J. Sawada, A. Williams and D. Wong, *Generalizing the Classic Greedy and Necklace Constructions of de Bruijn Sequences and Universal Cycles*, Electronic Journal of Combinatorics 23(1), P1.24 (2016). https://doi.org/10.37236/5517 .
3. Y. M. Chee, T. Etzion, T. L. Nguyen, D. H. Ta, V. D. Tran and V. K. Vu, *Maximum Length RLL Sequences in de Bruijn Graph*, arXiv:2403.01454, first version 2024-03-03, especially Corollaries 2.12 and 2.14, Theorem 3.1 and Section 4. https://arxiv.org/abs/2403.01454 .
4. Directed BEST theorem and directed matrix-tree theorem (standard count-of-Euler-circuits and arborescence tools).
