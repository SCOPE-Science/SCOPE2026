# Unbounded minimal matching obstructions on three-row rectangular grids

## Finding

Let \(n\ge2\) and let \(G_n=P_3\square P_{2n}\), the simple three-row, \(2n\)-column Cartesian grid. Write \(\Delta_n\) for its *perfect-matching extendability complex*: its vertices are grid edges, and an edge subset is a face precisely when it is contained in a perfect matching of \(G_n\). A *minimal nonface* is a set not contained in any perfect matching although every proper subset is.

There are **eight explicitly described, distinct minimal nonfaces of cardinality \(n+1\)** for every \(n\ge2\). They are precisely the nonextendable configurations within a natural family of sixteen boundary-decorated matchings constructed below; the other eight configurations in that family extend to perfect matchings. Consequently, for every \(n\ge2\), the Stanley–Reisner ideal of \(\Delta_n\) has at least eight squarefree minimal monomial generators of degree \(n+1\). In particular the cardinalities of minimal nonfaces are unbounded as the length increases, even at the fixed grid width three. No claim is made that these eight are the only minimal nonfaces of this cardinality or that \(n+1\) is the globally largest possible cardinality.

## Assumptions and scope

All graphs are finite and simple. The vertices of \(G_n\) are \((r,c)\) with \(r\in\{1,2,3\}\) and \(1\le c\le2n\); vertices at Manhattan distance one are adjacent. A matching is an edge set without shared endpoints. An edge subset is extendable if a perfect matching contains it. The complex \(\Delta_n\) consists of *extendable* edge sets, not all partial matchings.

For \(j=1,\ldots,n-1\), set \(d_j=\{(2,2j),(2,2j+1)\}\). Let \(D=\{d_1,\ldots,d_{n-1}\}\), the central spine covering every middle-row vertex except the two ends.

At the left boundary define four permissible edges: \(\mathrm{UV}_L=\{(1,1),(2,1)\}\), \(\mathrm{BV}_L=\{(2,1),(3,1)\}\), \(\mathrm{UH}_L=\{(1,1),(1,2)\}\), \(\mathrm{BH}_L=\{(3,1),(3,2)\}\). The corresponding four right-boundary edges \(\mathrm{UV}_R,\mathrm{BV}_R,\mathrm{UH}_R,\mathrm{BH}_R\) are their reflections under \(c\mapsto2n+1-c\).

Partition the four choices at each boundary into \(A=\{\mathrm{UV},\mathrm{BH}\}\) and \(B=\{\mathrm{UH},\mathrm{BV}\}\). For every left choice \(\ell\) and right choice \(r\), put \(S(\ell,r)=D\cup\{\ell,r\}\). The sixteen sets \(S(\ell,r)\) are distinct matchings, each of size \(n+1\).

## Proof

**Boundary parity lemma.** With all edges of \(D\) fixed, the middle-row endpoints \((2,1)\) and \((2,2n)\) must be covered at their respective boundary: a chosen vertical edge already covers one, whereas a chosen top horizontal edge forces the bottom vertical edge at that end, and a chosen bottom horizontal edge forces the top vertical edge. No other middle-row vertices are available for vertical edges.

After these forced end completions, only horizontal pairings of consecutive free vertices in the top and bottom rows remain. At the left, a type-\(A\) edge leaves the top row's first free column equal to \(2\) and the bottom row's first free column odd (\(1\) or \(3\)); a type-\(B\) edge leaves the top row's first free column odd (\(1\) or \(3\)) and the bottom row's first free column equal to \(2\). At the right, a type-\(A\) edge leaves the top row's last free column odd (\(2n-1\)) and the bottom row's last free column even (\(2n\) or \(2n-2\)); a type-\(B\) edge leaves the top row's last free column even (\(2n\) or \(2n-2\)) and the bottom row's last free column odd (\(2n-1\)). Empty intervals are allowed.

Therefore, if left and right phases agree, each residual interval in each outer row has even length and can be tiled uniquely by horizontal grid edges. The matching \(S(\ell,r)\) extends. If the phases disagree, each residual interval has odd length: for \(A\) on the left and \(B\) on the right the top free interval has even-numbered endpoints and the bottom has odd-numbered endpoints; for \(B\) then \(A\) the parities reverse. No extension is possible. Exactly \(2\cdot2\cdot2=8\) of the sixteen choices have mismatched phases.

**Minimality.** Fix a mismatched-phase \(S(\ell,r)\). If the left boundary edge is removed, choose a new vertical left boundary edge of the *same phase* as the retained right edge: top vertical for phase \(A\), bottom vertical for phase \(B\). The now phase-compatible matching extends by the preceding parity lemma, giving a perfect matching containing \(S\setminus\{\ell\}\). The same argument works after removing the right boundary edge.

Now remove any one spine edge \(d_j\), where \(1\le j\le n-1\). Keep all other spine edges and both boundary edges, including any forced end vertical edges. The two newly free middle-row vertices are at columns \(2j\) and \(2j+1\). If the phases are \(A\) left and \(B\) right, cover the middle-row vertex at \(2j\) with a vertical edge to the top row, and the one at \(2j+1\) with a vertical edge to the bottom row. Each resulting free interval in each outer row has even length, so complete it horizontally. If the phases are \(B\) left and \(A\) right, instead put the top vertical edge at \(2j+1\) and bottom vertical edge at \(2j\); again all outer-row intervals have even length and are horizontally tileable. This also works for \(j=1\) and \(j=n-1\), including when an endpoint horizontal edge forces a separate vertical edge at an extreme column.

Every one-edge deletion therefore extends to a perfect matching. Every proper subset is contained in a one-edge deletion, hence extends. Thus each of the eight incompatible-phase sets is a minimal nonface. They contain \(n-1\) spine edges and two endpoint edges, giving cardinality \(n+1\).

For any field \(\mathbb{K}\), the Stanley–Reisner ideal \(I_{\Delta_n}\subseteq\mathbb{K}[x_e:e\in E(G_n)]\) is generated by squarefree monomials \(\prod_{e\in F}x_e\) indexed by minimal nonfaces \(F\). Hence each of the eight sets supplies a distinct minimal generator of degree \(n+1\). Since \(n\) is arbitrary, no constant upper bound on minimal nonface cardinality is valid for the width-three family. \(\square\)

## Verification

The attached standalone Python program `verify.py` constructs the sixteen boundary-decorated matchings for each of twenty-one widths \(n\in\{2,3,\ldots,18,20,25,30,40\}\). An independent exhaustive recursive perfect-matching search tests all sixteen extension claims at each width and checks that **every** single-edge deletion of each of the eight nonextendable configurations is extendable. It reports `VERIFY_OK`. The finite program is a reproducible corroboration, not an all-\(n\) proof; the all-\(n\) assertion follows from the explicit parity constructions above. Run `python3 verify.py` with Python 3.8 or later and no third-party packages.

## Relationship to prior work

Chandrakar, Chau, Goyal, Karki and Subhash (arXiv:2611.18058v1, posted 2026-11-13) determine the homotopy type of the same perfect-matching complex. In their introduction they contrast two-row grids, whose minimal nonfaces all have two elements, with three-row grids where three-element minimal nonfaces can occur. Their Section 3 treats star decompositions and discrete-Morse-style topological reductions, using a middle-row spine related to \(D\), but does not state the boundary-phase classification or the arbitrarily large minimal-nonface result. That spine overlap is material, and the new claim is not an assertion of a different homotopy type.

Chandrakar and Singh (arXiv:2407.05809; originally posted 2024-07-08) prove a two-edge minimal-obstruction classification for two-row grids in Lemma 3.1; this does not cover the three-row boundary-frustration construction. Available mathematical-result searches did not identify another statement asserting the eight patterns or unbounded minimal nonface sizes for this fixed-width family. The absence of a search hit is not a uniqueness or historical-priority proof.

## Limitations

The theorem does not enumerate all minimal nonfaces, determine their global maximum size, provide a formula for the full Stanley–Reisner ideal, or determine Betti numbers. The eight-family count is exact only *within the stated sixteen boundary-decorated configurations*. The independently verified finite cases do not establish the infinite claim without the parity proof. A related general treatment of forbidden partial domino tilings not located in available searches remains a historical-priority risk. No independent mathematical audit has been performed.

## References

1. H. Chandrakar, T. Chau, S. Goyal, R. Karki, and B. Subhash, *Perfect Matching Complexes of \(3\times2n\) Grid Graph*, arXiv:2611.18058v1 (2026-11-13), https://arxiv.org/abs/2611.18058v1; original PDF https://arxiv.org/pdf/2611.18058v1.
2. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809 (original 2024-07-08), https://arxiv.org/abs/2407.05809.
