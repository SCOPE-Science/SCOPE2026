# Locating-domination and all minimal codes in matching-deleted complete bipartite graphs

## Finding
For an integer \(n\ge4\), let the *crown graph* \(\operatorname{Cr}_n\) have vertices \(a_1,\ldots,a_n,b_1,\ldots,b_n\), with \(a_i b_j\) an edge exactly when \(i\ne j\). A vertex set \(S\) is locating-dominating if each vertex outside \(S\) has a nonempty open neighborhood in \(S\), and those neighborhoods are pairwise different.

Define \(L_n(z)=\sum_{S\text{ locating-dominating}}z^{|S|}\) and \(M_n(z)=\sum_{S\text{ inclusion-minimal locating-dominating}}z^{|S|}\). For all \(n\ge4\),
\[
L_n(z)=z^n(2+z)^n+n z^{n-1}(2+z)^{n-1}-2n^2z^{n-1}-2nz^n.
\]
The complete inclusion-minimal polynomial is
\[
M_n(z)=\begin{cases}
56z^4,&n=4,\\
n(2^{n-1}-2n)z^{n-1}+(2n(n-1)+2)z^n,&n\ge5.
\end{cases}
\]
Consequently, the minimum locating-domination number is \(4\) for \(n=4\) and \(n-1\) for \(n\ge5\), and the upper locating-domination number (the maximum size of an inclusion-minimal code) is \(n\) for every \(n\ge4\). For \(n\ge5\), the only possible minimal-code sizes are \(n-1\) and \(n\).

## Assumptions and scope
All graphs are finite, undirected, and simple. The complementary matching has the prescribed indexed pairs \(a_i,b_i\). We use ordinary open-neighborhood location-domination: distinct vertices *outside* the code must have distinct, nonempty signatures; selected vertices are not required to be distinguished. The two vertex shores and their labels are fixed for counting, and each subset of the \(2n\) vertices is counted once.

Put \(I=\{i:a_i\in S\}\) and \(J=\{j:b_j\in S\}\). The following criterion completely characterizes the codes for \(n\ge4\):

* If \(|I|,|J|\ge2\), the set is locating-dominating precisely when \(|I\cup J|\ge n-1\).
* If \(J=\varnothing\), it is a code precisely when \(I=[n]\), and symmetrically with the shores exchanged.
* If \(|J|=1\), say \(J=\{j\}\), it is a code precisely when either \(I=[n]\), or \(|I|=n-1\) with \(j\in I\); and symmetrically for \(|I|=1\).
* No further cases occur.

For \(n\ge5\), all inclusion-minimal codes are *exactly* (a) the disjoint two-shore assignments \(I\cap J=\varnothing\), \(|I\cup J|=n-1\), \(|I|,|J|\ge2\); (b) either entire shore; and (c) the sets with \(|I|=n-1\), \(J=\{j\}\subset I\), or their shore reversals. At \(n=4\) all minimal codes have size four; the two-shore ones have \(|I|=|J|=2\), \(|I\cup J|\ge3\), while the one-shore and one-singleton patterns remain as above.

## Proof
**1. The signature criterion.** For every unselected vertex, its signature in the selected set is
\[
N(a_i)\cap S=\{b_j:j\in J\setminus\{i\}\},\qquad
N(b_j)\cap S=\{a_i:i\in I\setminus\{j\}\}.
\]
If both shores contribute at least two selected vertices, all such signatures are nonempty. Among unselected vertices on the \(a\)-shore, two signatures are equal precisely when their indices are both absent from \(J\). There are \(n-|I\cup J|\) such vertices. The same statement holds on the \(b\)-shore. Signatures from opposite shores cannot coincide, because they are nonempty and belong to disjoint selected shores. This proves the first bullet of the criterion.

If \(J\) is empty, an unselected \(a\)-vertex has an empty signature, so every \(a\)-vertex must be selected. With \(I=[n]\), the signatures of the unselected \(b_j\) are \(I\setminus\{j\}\), distinct and nonempty. If \(J=\{j\}\), the unselected \(a\)-vertices can only have the signatures \(\varnothing\) or \(\{b_j\}\). Nonemptiness forces \(j\in I\); uniqueness forces at most one vertex outside \(I\). For \(n\ge4\), the remaining unselected \(b\)-signatures are then distinct and nonempty. The symmetric case completes the characterization.

**2. Counting all codes.** For codes using at least two vertices from each shore, record for each matched index whether \(a_i\), \(b_i\), or both are selected, with at most one index selecting neither. The unfiltered one-variable enumerator is
\[
F_n(z)=z^n(2+z)^n+n z^{n-1}(2+z)^{n-1}.
\]
Among these assignments, the ones selecting at most one \(a\)-vertex contribute
\[
n^2z^{n-1}+(n^2+1)z^n+n z^{n+1}.
\]
There is the same contribution for the \(b\)-shore. For \(n\ge4\), these two excluded classes are disjoint: at most one vertex per shore cannot cover at least \(n-1\ge3\) matched indices. Finally add the one-shore exceptions: two complete shores; \(2n(n-1)\) configurations with \(n-1\) vertices on one shore and one compatible vertex on the other; and \(2n\) configurations with a complete shore and one additional vertex. Their polynomial is
\[
(2+2n(n-1))z^n+2nz^{n+1}.
\]
Subtracting the excluded classes from \(F_n\), then adding these exceptions, gives exactly the stated \(L_n(z)\).

**3. Classifying inclusion-minimal codes.** Location-domination is upward-closed under adding selected vertices: vertices newly selected cease to require identification, and existing distinct nonempty signatures remain so after restricting to the larger selected set. If \(n\ge5\), the criterion shows that no locating-dominating set has fewer than \(n-1\) vertices. Let \(S\) use at least two vertices from each shore and satisfy \(|I\cup J|\ge n-1\). Choose a subset \(U\subseteq I\cup J\) of cardinality \(n-1\) such that \(|I\cap U|,|J\cap U|\ge2\). This is possible: when \(|I\cup J|=n\), omit an index so neither shore falls below two (both shores cannot consist of just two indices because \(n\ge5\)). By Hall's marriage condition applied to two requests for each shore, \(U\) has disjoint two-element subsets \(I_0\subseteq I\) and \(J_0\subseteq J\). (The relevant Hall conditions are \(|I\cap U|\ge2\), \(|J\cap U|\ge2\), and \(|(I\cup J)\cap U|=n-1\ge4\).) Assign all remaining elements of \(U\) to a shore that contains them, giving disjoint \(I'\subseteq I\), \(J'\subseteq J\), each of size at least two and with union \(U\). The associated subset \(S'\subseteq S\) has \(n-1\) vertices and is locating-dominating. Therefore \(S\) is inclusion-minimal exactly when \(S=S'\); equivalently, \(I\cap J=\varnothing\), \(|I\cup J|=n-1\), and both cardinalities are at least two.

The one-shore cases from Step 1 are inclusion-minimal precisely for a full shore or \(n-1\) vertices of one shore together with its compatible opposite-shore singleton. Every proper deletion of either type fails the signature criterion. The size-\(n-1\) two-shore sets are automatically inclusion-minimal because they achieve the minimum cardinality.

The disjoint two-shore types are counted by choosing the one omitted matched index (\(n\) choices) and assigning each of the remaining \(n-1\) indices to one shore, with at least two assigned to each. The count is \(n(2^{n-1}-2n)\). The other two families contribute \(2+2n(n-1)\) sets, all of cardinality \(n\).

For \(n=4\), the criterion implies every code has at least four vertices. The complete 4-vertex codes consist of \(\binom42^2-\binom42=30\) two-shore sets with two vertices per shore and union size at least three, and \(2+2\cdot4\cdot3=26\) exceptional shore/singleton sets. Every code of larger size contains one of these 56 size-four codes: for a two-shore code select two vertices from each shore while retaining union size at least three, and for an exceptional code delete the unnecessary singleton. Hence the size-four codes are exactly the minimal ones. This finishes the proof.

## Verification
Run \(\texttt{python3 verify_crown_ld.py}\) with Python 3 and no third-party packages. The verifier uses only direct adjacency signatures and proper one-vertex deletion tests, rather than accepting the theoretical criterion as the definition. For each \(4\le n\le9\) it checks every subset of the \(2n\) vertices, the criterion, both polynomials, and the full minimal-code classification. These finite calculations corroborate the proof but do not establish the unrestricted statement without the foregoing argument.

## Relationship to prior work
Murtaza, Fazil, Javaid and Benish study locating-dominating sets of functigraphs of complete graphs, including the identity matching construction \(K_n\square K_2=\overline{\operatorname{Cr}_n}\), and establish its minimum location-domination number \(n-1\) for \(n\ge4\). That graph is the **complement**, not the crown graph considered here; its minimum number does not imply the full crown polynomial or its inclusion-minimal structures. Fazil, Hussain, Akbar and Ali introduce the location-domination polynomial and explicitly count it for complete multipartite graphs, the Petersen graph, and some lexicographic products. The crown graph is not complete multipartite and is not one of those counted families. Related work on metric/metro domination occasionally calls the sunlet \(C_n\circ K_1\) a "crown graph"; it is a different graph.

## Limitations
The result is limited to the ordinary, open-neighborhood locating-dominating definition for matching-deleted \(K_{n,n}\) with \(n\ge4\). It does not assert analogous results for identifying codes, locating-total codes, arbitrary deleted matchings, or the complement graph. The work has undergone only self-review and finite computational checks, not independent audit. Publication priority is provisional; search is not proof that no equivalent unpublished or unindexed theorem exists.

## References
1. M. Murtaza, M. Fazil, I. Javaid and H. Benish, *Locating-Dominating Sets of Functigraphs*, arXiv:1709.05152v1 (first posted 15 September 2017), Sections 1 and 3, especially Lemma 3.3. https://arxiv.org/abs/1709.05152
2. M. Fazil, I. F. Hussain, A. Akbar and U. Ali, *On Some Variations of Dominating Identification in Graphs*, Kuwait Journal of Science **49**(4) (2022), DOI:10.48129/KJS.13175, Sections 2–3 (location-domination polynomials of other graph families). https://doi.org/10.48129/KJS.13175
3. V. Kumar M., N. B. K. and S. Lakshminarayana, *Metro Domination Number of Friendship Graph and Crown Graph*, JETIR **6**(5) (2019), 570–574. https://www.jetir.org/papers/JETIR1905F87.pdf (the paper defines its "crown graph" as the sunlet, not \(K_{n,n}-M_n\)).
