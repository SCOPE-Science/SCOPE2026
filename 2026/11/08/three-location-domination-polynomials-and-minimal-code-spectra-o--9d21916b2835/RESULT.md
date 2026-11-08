# Three location-domination polynomials and minimal-code spectra of complete prisms

## Finding
For every integer \(n\ge4\), let \(G_n=K_2\square K_n\), with cliques \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), joined by the matching edges \(a_ib_i\). Write \(L_n(z)\), \(D_n(z)\), and \(S_n(z)\) for the cardinality generating polynomials of all ordinary locating-dominating, solid-locating-dominating, and self-locating-dominating codes, respectively. Then
\[
\begin{aligned}
L_n(z)&=(2z+z^2)^n+n(2z+z^2)^{n-1}-2nz^{n-1},\\
D_n(z)&=(2z+z^2)^n-2nz^n+nz^{2n-2},\\
S_n(z)&=(2z+z^2)^n-2(n+1)z^n-2nz^{n+1}.
\end{aligned}
\]
If \(M^L_n(z),M^D_n(z),M^S_n(z)\) count *inclusion-minimal* codes of the respective types, then
\[
\begin{aligned}
M^L_n(z)&=n(2^{n-1}-2)z^{n-1}+2z^n,\\
M^D_n(z)&=(2^n-2n)z^n+nz^{2n-2},\\
M^S_n(z)&=(2^n-2n-2)z^n.
\end{aligned}
\]
In particular, the largest inclusion-minimal solid-locating-dominating codes have \(2n-2\) vertices, with exactly \(n\) such codes; every inclusion-minimal self-locating-dominating code has the known minimum size \(n\). The full-polynomial difference is
\[
D_n(z)-S_n(z)=2z^n+2nz^{n+1}+nz^{2n-2}.
\]
The minimum *cardinalities* \(n-1\), \(n\), and \(n\) were previously established; the enumerators and inclusion-minimal spectra are the contributions here.

## Assumptions and scope
All graphs are finite, simple, undirected, and labelled. The scope is \(n\ge4\); the smaller cases are not asserted. For a code \(C\subseteq V(G_n)\) and any vertex \(u\), put \(I_C(u)=N[u]\cap C\), where \(N[u]\) is the closed neighborhood. Every vertex outside \(C\) must have a nonempty identifying set. Ordinary locating domination additionally requires distinct identifying sets for distinct vertices outside \(C\). Solid locating domination requires \(I_C(u)\setminus I_C(v)\ne\varnothing\) for every ordered pair of distinct vertices outside \(C\). Self locating domination requires \(\bigcap_{c\in I_C(u)}N[c]=\{u\}\) for every vertex \(u\notin C\). Inclusion-minimal means deleting any selected vertex destroys the corresponding property; it does not mean globally minimum cardinality.

Write \(A_C=C\cap A\) and \(B_C=C\cap B\). Encode each matched column \(\{a_i,b_i\}\) as \(0\) (neither codeword), \(\mathrm A\) (only \(a_i\)), \(\mathrm B\) (only \(b_i\)), or \(\mathrm D\) (both), and let \(e,a,b,c\) be the numbers of these states. Thus \(e+a+b+c=n\), and every code has size \(a+b+2c\).

## Proof
**Identifying sets and the three all-code classifications.** For any unselected vertex, the rook-graph adjacency gives the exact identities
\[
I_C(a_i)=A_C\cup(\{b_i\}\cap C),\qquad
I_C(b_i)=B_C\cup(\{a_i\}\cap C).
\]
Two empty columns would give two unselected vertices in the same clique with equal identifying sets. Thus an ordinary code has \(e\le1\). If \(e=1\), nonempty identifying sets at the empty column require \(|A_C|,|B_C|\ge1\). Conversely, if \(e=0\), missing vertices in a fixed clique are distinguished by their respective selected matching mates. If \(e=1\) and both shores are represented, this is still true: the empty-column signature lacks the matched extra codeword present at the other missing vertices. For missing vertices on opposite shores, equality of signatures would force \(A_C\) and \(B_C\) each to contain at most one codeword; this is impossible because \(n-1\ge3\) matched columns are nonempty. This proves
\[
C\text{ is ordinary locating-dominating}\iff e=0\text{, or }e=1\text{ with }|A_C|,|B_C|\ge1.
\]

For solid location domination, if \(e=1\) and another column has state \(\mathrm A\) or \(\mathrm B\), a missing vertex in the same shore has a signature properly containing that of the missing vertex in the empty column, which violates solid location domination. Hence the only solid codes with \(e=1\) have all other columns in state \(\mathrm D\), and these do satisfy the condition. Suppose \(e=0\). Signatures of different missing vertices within a fixed shore are incomparable because each has a distinct selected matching mate. A missing \(a_i\) (state \(\mathrm B\)) and a missing \(b_j\) (state \(\mathrm A\)) have incomparable signatures exactly when \(|A_C|\ge2\) and \(|B_C|\ge2\). If \(c>0\) and there are missing vertices on both shores, these inequalities hold automatically. If \(c=0\), they fail precisely for singleton transversals with \(a=1\) or \(b=1\). Therefore
\[
C\text{ is solid}\iff [e=0\text{ and not }(c=0\text{ and }(a=1\text{ or }b=1))]\text{ or }[e=1,c=n-1].
\]

A self-locating code cannot have an empty column: an unselected vertex there would be identified only by selected vertices in its own clique, whose closed neighborhoods intersect in a set containing that entire clique (or a larger set). With \(e=0\), every unselected \(a_i\) has its matching \(b_i\) selected, and intersection with \(N[b_i]\) reduces its identifying intersection to \(\{a_i\}\) precisely when \(|A_C|\ge2\); with only one selected \(a_j\), the intersection \(N[a_j]\cap N[b_i]\) also contains \(b_j\). The analogous condition for missing vertices of \(B\) is \(|B_C|\ge2\). If one shore has no unselected vertices, its own condition holds automatically because that shore contains \(n\ge4\) selected vertices; the opposite-shore test remains necessary. Hence
\[
C\text{ is self-locating}\iff e=0,\quad |A_C|=a+c\ge2,\quad |B_C|=b+c\ge2.
\]

**All-code generating polynomials.** The nonempty-column configurations have weight enumerator \(F_n(z)=(2z+z^2)^n\). For ordinary codes, add the \(nF_{n-1}(z)\) configurations with exactly one empty column, then exclude the two monochromatic singleton configurations for each empty column, giving \(L_n\). For solid codes, remove from \(F_n\) the \(2n\) singleton transversals with exactly one selected vertex on one shore, and add the \(n\) configurations with one empty column and all remaining columns double, giving \(D_n\). For self-locating codes, the prohibited nonempty-column choices with at most one selected vertex in the \(A\)-shore have weight \((n+1)z^n+nz^{n+1}\): all \(B\)-only, exactly one \(A\)-only, or exactly one double column. The same holds for the \(B\)-shore, and for \(n\ge4\) the two forbidden families are disjoint. Subtracting them gives \(S_n\).

**Inclusion-minimal ordinary codes.** An ordinary code with an empty column and a double column is not inclusion-minimal: a selected vertex in a double column can be deleted while retaining both represented shores. Thus the inclusion-minimal codes with \(e=1\) have every remaining column singleton and use both shores; there are \(n(2^{n-1}-2)\) of size \(n-1\). With \(e=0\), any double column permits deletion without destroying ordinary location domination. For an all-singleton transversal using both shores, delete a vertex from a shore represented at least twice; the remaining configuration has one empty column and both shores represented. The only minimal cases are the two monochromatic singleton transversals, of size \(n\). This gives \(M_n^L\).

**Inclusion-minimal solid codes.** Every solid code with \(e=1\) has \(c=n-1\); deleting a codeword creates an \(\mathrm A\) or \(\mathrm B\) column and destroys solid location domination. Thus the \(n\) such codes, of size \(2n-2\), are minimal. In a solid code with \(e=0,c\ge1\), a selected vertex of a double column can be deleted while retaining solid domination. If \(c\ge2\), any such deletion leaves a double column. If \(c=1\), choose which of its two codewords to delete so that the resulting singleton transversal is not a one-color-singleton exceptional case; one of the two choices always works since \(n\ge4\). Hence the only other minimal solid codes are the all-singleton transversals except the \(2n\) forbidden ones, giving \(M_n^D\).

**Inclusion-minimal self-locating codes.** If a self-locating code has \(c\ge1\), then it has at least \(n+1\ge5\) selected vertices, so one shore contains at least three selected vertices. Deleting one selected vertex of a double column in that shore preserves at least two codewords per shore, and hence preserves self location domination. Conversely, every singleton transversal with at least two selected vertices on each shore is self-locating, and deleting any selected vertex creates an empty column. Its number is \(2^n-2n-2\). This yields \(M_n^S\) and completes all claims.

## Verification
The accompanying standalone `verify_complete_prism_location.py` implements the original three code definitions from closed neighborhoods and directly enumerates all \(2^{2n}\) labelled subsets for every \(4\le n\le8\). It checks the four-state characterization, every coefficient of all three full polynomials, and every coefficient of all three inclusion-minimal spectra by literal one-codeword deletion. All \(87{,}296\) subsets across the five profiles matched. Finite verification corroborates, but does not establish, the results for unrestricted \(n\); those follow from the proof above. Run with `python3 verify_complete_prism_location.py` in the directory containing this document and the script.

## Relationship to prior work
Junnila, Laihonen and Lehtilä determined the ordinary, solid and self location-domination **numbers** of general rook graphs, including the minimum cardinalities \(n-1,n,n\) here (Theorems 12–14 of the first reference). Those minima are not claimed as new. The second reference supplies general inequalities and Cartesian-product analyses for stronger locating codes, but no complete cardinality enumerator or inclusion-minimal spectrum for this complete-prism family was identified in its relevant sections. An earlier open-neighborhood locating-domination study of the complementary crown graph is a distinct code condition: for the crown complement \(H=\overline{G_n}\), the prism identifying set is \(I_{G_n,C}(u)=C\setminus(N_H(u)\cap C)\), whereas crown open locating domination requires those open traces to be **nonempty**, rather than requiring their complements in \(C\) to be nonempty. Therefore its polynomial does not directly specialize to the stated three polynomials. A complete equivalence search beyond inspected sources is not a proof of global publication priority.

## Limitations
Only \(n\ge4\) and labelled code subsets are covered; the smaller exceptional graphs and equivalence modulo automorphisms are excluded. The scientific statements have been internally checked but not independently mathematically audited. The possibility of an equivalent enumeration under alternate naming, a published complement transformation, or an incompletely indexed source remains open. Numerical tests cover only finite orders.

## References
1. V. Junnila, T. Laihonen and T. Lehtilä, *On Regular and New Types of Codes for Location-Domination*, Discrete Applied Mathematics 247 (2018), 225–241, DOI 10.1016/j.dam.2018.03.050. Full open manuscript: https://www.utupub.fi/bitstream/handle/10024/155895/On%20Regular%20and%20New%20Types%20of%20Codes%20for%20Location-Domination.pdf?sequence=1.
2. V. Junnila, T. Laihonen, T. Lehtilä and M. L. Puertas, *On Stronger Types of Locating-Dominating Codes*, arXiv:1808.06891v1 (first public submission 2018-08-21), later DMTCS 21:1 (2019), DOI 10.23638/DMTCS-21-1-1; https://arxiv.org/abs/1808.06891.
