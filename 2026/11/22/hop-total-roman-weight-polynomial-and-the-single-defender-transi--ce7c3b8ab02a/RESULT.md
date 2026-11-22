# Hop-total-Roman weight polynomial and the single-defender transition on clique bouquets

## Finding
For any integer \(q\ge2\) and integers \(s_1,\ldots,s_q\ge2\), put
\[
G=K_1\vee\left(K_{s_1}\sqcup\cdots\sqcup K_{s_q}\right),\qquad M=\sum_{i=1}^{q}s_i.
\]
Let \(H_G(z)=\sum_f z^{\omega(f)}\), summing over all hop-total-Roman functions \(f:V(G)\to\{0,1,2\}\) with weight \(\omega(f)=\sum_v f(v)\). Here every zero-labeled vertex must have a *distance-exactly-two* neighbor labeled two, and the subgraph induced by all positively labeled vertices must have no isolated vertices.

Define the following four integer polynomials for each petal:
\[
A_i=(1+z+z^2)^{s_i},\quad B_i=(1+z)^{s_i},\quad
C_i=A_i-B_i,\quad D_i=(z+z^2)^{s_i}-z^{s_i}.
\]
Then the complete labeled weight polynomial is
\[
\boxed{H_G(z)=(z+z^2)\left[z^M+\sum_{i=1}^q D_i\prod_{j\ne i}B_j+\prod_{i=1}^q A_i-\prod_{i=1}^q B_i-\sum_{i=1}^q C_i\prod_{j\ne i}B_j\right].}
\]
Every coefficient is nonnegative; the subtractions are simply an exact partition by how many petals contain a two-labeled vertex. The total number of functions also has the explicit closed expression
\[
\boxed{H_G(1)=2\left[1+3^M-2^M+\sum_{i=1}^{q}(2^{s_i+1}-3^{s_i}-1)\,2^{M-s_i}\right].}
\]
Writing \(r_t=|\{i:s_i=t\}|\), the minimum and its exact multiplicity are
\[
\boxed{\gamma_{htR}(G)=\begin{cases}4,&r_2>0,\\5,&r_2=0,\end{cases}\qquad
[z^{\gamma_{htR}(G)}]H_G(z)=\begin{cases}
2r_2,&r_2>0,\\
3r_3+\sum_{1\le i<j\le q}s_is_j,&r_2=0.
\end{cases}}
\]
In the weight-four case, the optimal functions consist exactly of a center label one, one size-two petal labeled \((2,1)\) in either order, and zeros elsewhere. When every petal has order at least three, the optimal functions consist exactly of either (a) a center label one and a single three-vertex petal carrying one two and two ones, or (b) a center label one and one two in each of two distinct petals; in either case all unspecified vertices have label zero.

Finally **every integer weight** between the minimum \(\gamma_{htR}(G)\) and the maximum \(2(M+1)\), inclusive, is achieved. Thus the complete weight spectrum is an interval, despite a sharp change in the form and number of minimizers at petal size two.

## Assumptions and scope
All graphs are finite, simple, undirected and labeled. The \(q\) clique petals are pairwise vertex-disjoint; no edges join distinct petals except through the single universal center. The center is included in the weight. We use graph *distance exactly two* for the hop condition and minimum degree at least one in the induced positive support for totality. Color labels are numeric (not interchangeable colors), and functions are counted individually, not modulo automorphism. The proof requires \(q\ge2\) and \(s_i\ge2\) for each \(i\); no claim is made for a single clique or for arbitrary block graphs.

## Proof
Let \(c\) be the center. Since \(c\) is universal, it has no vertex at distance two, so every admissible function necessarily has \(f(c)>0\). For peripheral vertices, distance exactly two occurs *precisely* between vertices in distinct petals: vertices in a given petal are adjacent, and different petals are connected by a shortest path through \(c\). Therefore a zero in petal \(i\) can be defended by a two only in a different petal. Whenever at least one peripheral vertex is positive, the positive support has no isolated vertex: every positive peripheral vertex is adjacent to \(c\), while \(c\) has a positive peripheral neighbor. All cases below satisfy this support requirement.

Partition peripheral labelings according to the number \(k\) of petals containing at least one two-labeled vertex.

- If \(k=0\), no peripheral zero can be defended. Every peripheral vertex must have label one, yielding \(z^M\).
- If \(k=1\), say petal \(i\) is the unique two-containing petal, it cannot contain a zero, because its zero would require a two in a different petal. This petal is fully positive with at least one two, counted by \(D_i=(z+z^2)^{s_i}-z^{s_i}\). Every other petal uses only zero and one, freely, counted by \(\prod_{j\ne i}B_j\). There is no overcount: the unique two-containing petal is determined by the labeling.
- If \(k\ge2\), every zero in any petal has a two-labeled defender in another petal, and all peripheral labels are otherwise free. Counting all peripheral ternary assignments and removing those with zero or exactly one two-containing petal gives \(\prod_i A_i-\prod_i B_i-\sum_i C_i\prod_{j\ne i}B_j\), where \(C_i=A_i-B_i\).

The three cases are exhaustive, mutually exclusive, and all have a positive peripheral vertex. Multiplying by \(z+z^2\) for the independent center label proves the polynomial. Substitution \(z=1\) uses \(A_i(1)=3^{s_i}\), \(B_i(1)=2^{s_i}\), \(C_i(1)=3^{s_i}-2^{s_i}\), \(D_i(1)=2^{s_i}-1\) and simplifies to the displayed total.

The minimal peripheral weight is \(M\) when \(k=0\), at least \(s_i+1\) when \(k=1\) with unique two-containing petal \(i\), and at least four when \(k\ge2\). The center contributes at least one. As \(M\ge4\), the minimum is four exactly when some \(s_i=2\), and otherwise five. In the weight-four case, the only feasible structure is a size-two petal with exactly one two and the other vertex one, yielding \(2r_2\) choices. With every petal size at least three, weight five arises in precisely two disjoint ways: the unique two-containing petal has size three, with exactly one two and two ones (\(3r_3\) choices), or two distinct petals have exactly one two each (\(\sum_{i<j}s_is_j\) choices). All minimal functions have center label one.

For the full interval of attainable weights, start with any minimum function. Raising the label of any vertex by one, when possible, preserves admissibility: the center remains positive; any newly positive peripheral vertex is adjacent to the center; all previously positive vertices retain their positive neighbors; and raising a label cannot remove an existing distance-two defender from any vertex remaining zero. Repeatedly raising any labels still below two reaches the all-two labeling, of weight \(2(M+1)\), in increments of exactly one. This constructs a feasible function of every intermediate weight, and no function has larger weight. This proves the spectrum assertion.

## Verification
Two distinct programs accompany the proof. `verify_formula.py` computes the polynomial from its integer-polynomial factors. `verify_bruteforce.cpp` builds the graph adjacency matrix from the petal sizes, computes all graph distances by Floyd–Warshall, exhausts all ternary labelings, and tests the original two constraints directly; its method does not use the factorization. `verify_agreement.py` builds the C++ verifier and compares all polynomial coefficients on ten parameter vectors:

\[
(2,2),\ (2,3),\ (3,3),\ (2,2,2),\ (3,4),\ (2,3,3),\ (4,4),\ (2,2,3,3),\ (3,3,3),\ (4,4,4).
\]
All ten coefficient vectors agreed, including all minimum multiplicities. The largest check examined \(3^{13}=1,594,323\) ternary labelings. These are finite consistency checks; the proof for all allowed petal sizes is the preceding disjoint-case argument. The exact finite output is included in `direct_counts.txt`.

## Relationship to prior work
Ahangar, Chellali, Sheikholeslami, and Soroudi introduced hop-total-Roman domination and studied complexity, paths, cycles, and small minimum values (2023). In particular their general four-weight classification may cover the scalar minimum-four subfamily here; **no novelty is claimed for a bare minimum-four classification detached from the present complete enumeration**. The distinguishing claim is the entire weight polynomial with its all-parameter optimal-function classification and uninterrupted spectrum. Their indexed article materials were compared, although the publisher full text could not be retrieved, which remains a priority risk.

Published exact polynomials for *ordinary total Roman domination* on the same unequal clique bouquets have a different condition: zeros require an **adjacent** two-labeled vertex, and the center can be zero. The accessible complete proof of that result decomposes into three center-label cases and gives minimum three, rather than the center-forced-positive, cross-petal, hop-distance behavior here. A published hop-total-Roman polynomial for matching-deleted complete bipartite graphs does use the same labeling predicate, but its distance-two relation is *within* bipartition classes; the graph family is not isomorphic to a clique bouquet and its coefficient formula does not apply. An exact total two-rainbow polynomial of unequal clique bouquets uses four subset-valued labels and a different color-neighborhood condition. Thus these stronger-looking results do not imply the present full function census. All originality statements remain provisional pending broader independent literature review.

## Limitations
The structural proof requires one universal center and at least two clique petals of size at least two. The formulas do not apply unchanged to arbitrary joins, trees, or graphs with several shared hubs. The exact distance-two condition is crucial; replacing it by adjacency changes the theorem. Computational checks cover only the listed finite profiles; they are not an independent proof for arbitrary parameters. The earliest documented source date is the verified 2023 online publication, not evidence that no earlier unpublished or inaccessible version exists. No independent mathematical audit has been performed.

## References
1. H. Abdollahzadeh Ahangar, M. Chellali, S. M. Sheikholeslami and M. Soroudi, “Hop total Roman domination in graphs,” *AKCE International Journal of Graphs and Combinatorics* **20** (2023), 73–78, first published online 2023-03-30, DOI: https://doi.org/10.1080/09728600.2023.2184288.
2. “Total Roman domination polynomial of heterogeneous windmills,” public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-total-roman-domination-polynomial-of-heterogeneous-windmills--5959e7c34d61 (complete `RESULT.md` inspected).
3. “Affine hop-total-Roman weight polynomials under matching deletion from complete bipartite graphs,” public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-affine-hop-total-roman-weight-polynomials-under-matching-deletio--c53bd47d7c27 (complete `RESULT.md` inspected).
4. “Total two-rainbow domination polynomial of unequal clique bouquets,” public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-total-two-rainbow-domination-polynomial-of-unequal-clique-bouque--4d696a052822 (complete `RESULT.md` inspected).
