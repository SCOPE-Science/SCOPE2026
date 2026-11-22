# Exact enumeration of minimum two-rainbow independent dominating functions on cycle prisms

## Finding

For each integer \(n\ge4\), write \(Y_n=C_n\square K_2\). The number of minimum two-rainbow independent dominating functions on the **labelled** graph \(Y_n\), with the two positive colours distinguished, is

\[
a_n=2^n+3(-1)^n+4\mathbf 1_{\{4\mid n\}}+u_n,
\quad u_0=2,\quad u_1=1,\quad u_{n+2}=u_{n+1}-2u_n.
\]

Every minimum assignment has weight \(n\). Equivalently, \(u_n=\alpha^n+\overline\alpha^n\) with \(\alpha=(1+i\sqrt7)/2\). In particular, \(a_n=2^n+O(2^{n/2})\). The first counts, for \(n=4,5,6,7,8,9,10,11,12\), are \(24,40,76,112,232,504,1084,2112,4056\).

## Assumptions and scope

The vertices are \((j,r)\), with \(j\in\mathbb Z/n\mathbb Z\) and \(r\in\{0,1\}\). Each \((j,r)\) is adjacent to \((j-1,r)\), \((j+1,r)\), and \((j,1-r)\). A two-rainbow independent dominating function \(f\) takes values in \(\{0,1,2\}\), the sets of vertices labelled \(1\) and \(2\) are **separately independent**, and each vertex labelled \(0\) has a neighbour of colour \(1\) and a neighbour of colour \(2\). The weight is the number of vertices with nonzero label. Colour names are not identified under interchange, nor are graphs quotiented by automorphisms.

## Proof

Write the column at coordinate \(j\) as a word \(b_j\in\{0,1,2\}^2\), in upper/lower order. Since a column has a vertical edge, neither \(11\) nor \(22\) is permitted; exactly seven column words remain:

\[
\mathcal S=\{00,01,02,10,12,20,21\}.
\]

Two words are *compatible* when no coordinate has the same nonzero colour in both. The set \(\mathcal P\) of ordered compatible pairs \((a,b)\) has exactly \(35\) members. Let \((a,b)\to(b,c)\) be a legal directed arc if \(b,c\) are compatible and, for each row \(r\) with \(b_r=0\), the three adjacent labels \(a_r,b_{1-r},c_r\) contain both \(1\) and \(2\). There are exactly \(70\) legal arcs, and every valid function on \(Y_n\) corresponds bijectively to a closed directed walk of length \(n\), starting with the prescribed indexed column. The arc's cost is \(w(b)=\mathbf1_{\{b_0\ne0\}}+\mathbf1_{\{b_1\ne0\}}\); summing costs counts the positive vertices exactly once.

Define an integer potential on states by

\[
\phi(a,b)=\begin{cases}-1,&a=00\text{ and }b\in\{12,21\},\\0,&\text{otherwise}.\end{cases}
\]

For every one of the \(70\) legal arcs, direct finite inspection gives the reduced cost

\[
\delta((a,b),(b,c))=w(b)-1+\phi(a,b)-\phi(b,c)\in\{0,1\}.
\]

Precisely \(46\) arcs have reduced cost zero and \(24\) have reduced cost one. The two potential terms telescope on each closed walk, proving its weight is at least \(n\). Consequently a valid assignment has weight exactly \(n\) if and only if its walk uses only zero-reduced-cost arcs. The proof uses an explicitly exhaustive \(35\)-state, \(70\)-arc certificate, not an unverified heuristic.

Let \(B\) be the \(35\times35\) integer zero–one adjacency matrix retaining just these \(46\) tight arcs, in the lexicographic pair ordering determined above. Because each fixed indexed cyclic assignment gives one closed walk rooted at column zero,

\[
a_n=\operatorname{tr}(B^n).
\]

Exact rational/integer characteristic-polynomial computation gives

\[
\chi_B(t)=t^{25}(t-2)(t-1)(t+1)^4(t^2+1)(t^2-t+2).
\]

As a second exact check of this factorisation, the directed tight graph has \(19\) singleton strongly connected components and precisely two nontrivial components. The \(12\)-state component has characteristic polynomial \(t^6(t-2)(t+1)^3(t^2-t+2)\); the \(4\)-state component is a directed four-cycle and has polynomial \(t^4-1\). These block factors multiply to the displayed polynomial. The nonzero eigenvalues yield

\[
\operatorname{tr}(B^n)=2^n+3(-1)^n+4\mathbf 1_{\{4\mid n\}}+\alpha^n+\overline\alpha^n.
\]

There is at least one tight closed walk for every \(n\ge4\): the formula is positive at \(n=4,5\), and for \(n\ge6\) it is bounded below by \(2^n-2(\sqrt2)^n-3>0\). Thus the minimum weight is indeed \(n\), and all its optimal configurations have been counted. The four-cycle component accounts for exactly the exceptional extra four functions when \(4\mid n\).

## Verification

The standalone source file `transfer_certificate.py` constructs the seven words, all \(35\) pair states, \(70\) legal arcs and reduced costs, then recomputes the exact \(35\)-dimensional characteristic polynomial and both nontrivial strongly connected component polynomials. It checks the formula against exact matrix traces for every \(1\le n\le40\). Run: `python3 transfer_certificate.py` (requires Python 3 and SymPy).

The independent program `direct_bruteforce.cpp` tests all \(3^{2n}\) vertex labelings for each \(3\le n\le7\), using direct three-neighbour conditions and without importing the transfer matrix. Run: `g++ -std=c++17 -O2 direct_bruteforce.cpp -o verify && ./verify`. The separate `independent_dp.py` implements a direct compatible-column dynamic program and checks \(3\le n\le11\). Run: `python3 independent_dp.py`. Text output files contain the exact expected program outputs. Finite samples corroborate the result but are not used in place of the all-order transfer proof.

## Relationship to prior work

Kraner Šumenjak, Rall and Tepeh introduced the rainbow independent domination invariant. Gabrovšek, Peperko and Žerovnik (2023, Theorem 1.6) proved the minimum-weight statement \(\gamma_{ri2}(C_n\square P_2)=n\) for \(n\ge4\) using a tropical minimum-weight transfer framework; they explicitly credited a 2021 conference announcement of such minimum values. These minimum-weight results and the general auxiliary-graph framework are **prior work**, not discoveries here. The claimed addition is an exact **multiplicity** formula for every optimum with named colours, the nontrivial correction recurrence, and the independently exhibited recurrent-state decomposition. The published tropical minimum-trace formula does not itself assert a count of minimising walks; the enumeration requires identifying all zero-reduced-cost arcs and analysing their ordinary integer spectrum. No identical counting formula was identified in the checked material.

## Limitations

The formula covers ordinary cyclic prisms for \(n\ge4\) only, two singleton positive colour labels, and **minimum-weight** functions, not the full weight polynomial. For the triangular prism \(n=3\), exhaustive checking gives minimum weight \(4\) with \(18\) functions, so the statement cannot be extended to \(n=3\). Earlier conference proceedings, unindexed computational catalogues, and unrelated family results may affect historical priority. No independent external mathematical audit has been performed.

## References

1. T. Kraner Šumenjak, D. F. Rall and A. Tepeh, *On \(k\)-rainbow independent domination in graphs*, arXiv:1709.08966 (first public 2017-09-26); subsequently *Applied Mathematics and Computation* 333 (2018), 353–361. https://arxiv.org/abs/1709.08966
2. B. Gabrovšek, A. Peperko and J. Žerovnik, *On the 2-rainbow independent domination numbers of some graphs*, *Central European Journal of Operations Research* 31 (2023), 817–831, first published online 2023-02-15, DOI:10.1007/s10100-023-00840-w. https://link.springer.com/article/10.1007/s10100-023-00840-w
3. B. Gabrovšek, A. Peperko and J. Žerovnik, 2021 SOR conference precursor (cited by the 2023 article); only an indexed bibliographic description was accessible. https://eurekamag.com/research/097/247/097247928.php
