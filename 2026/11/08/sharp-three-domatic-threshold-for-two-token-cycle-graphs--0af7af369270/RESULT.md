# Sharp three-domatic threshold for two-token cycle graphs

## Finding
For every integer \(n\ge3\), let \(F_2(C_n)\) be the graph of unordered two-vertex subsets of the labelled cycle \(C_n\), with two subsets adjacent if one token can slide along a cycle edge into an unoccupied vertex. Its ordinary domatic number is
\[
\operatorname{dom}(F_2(C_n))=
\begin{cases}
2,&n=4\text{ or }n=5,\\
3,&n=3\text{ or }n\ge6.
\end{cases}
\]
Moreover, for every \(n\ge6\), an explicit three-domatic partition is obtained from the modular pair-sum colouring by recolouring **at most four** token configurations. No recolouring is needed when \(3\mid n\).

## Assumptions and scope
All graphs are finite, simple, and undirected. The cycle \(C_n\) has vertex set \(\mathbb Z/n\mathbb Z\), and in formulas pairs are represented uniquely as \((i,j)\) with \(0\le i<j<n\). The two-token graph has one vertex per unordered pair. An ordinary domatic \(k\)-colouring is a map \(c:V(F_2(C_n))\to\{0,\ldots,k-1\}\) whose every closed neighbourhood contains all \(k\) colours; its colour classes form a partition into dominating sets. This is **not** a proper graph colouring and is **not** the two-player domatic game.

For a token pair \(p=(i,j)\), set \(b_n(p)=(i+j)\bmod3\). Write \(c_n=b_n\) except for these entries when \(n\ge6\):

- If \(n\equiv0\pmod3\), leave every pair unchanged.
- If \(n\equiv1\pmod3\) (thus \(n\ge7\)), set \(c_n(0,1)=0\), \(c_n(0,n-2)=0\), \(c_n(0,n-1)=2\), and \(c_n(2,n-1)=1\).
- If \(n\equiv2\pmod3\) (thus \(n\ge8\)), set \(c_n(0,n-3)=0\), \(c_n(0,n-2)=2\), \(c_n(1,n-1)=0\), and \(c_n(2,n-1)=2\).

This construction uses the integer labels and produces a particular partition; it does not classify all domatic partitions.

## Proof
**Universal upper bound.** For \(n\ge4\), an adjacent token pair has precisely two neighbours: one token may move outwards at either end, but neither may move into the other occupied site. Every nonadjacent pair has four neighbours. Thus the minimum degree is two, and a domatic partition has at most three classes (every class must meet the closed neighbourhood of a degree-two vertex). For \(n=3\), the two-token graph is \(K_3\), also giving three as both upper and lower bound.

**The baseline colouring and its only possible obstructions.** When \(n\equiv0\pmod3\), \(b_n\) already gives three distinct closed-neighbourhood colours at every token pair. More generally, consider an unmodified pair. If its tokens are nonadjacent in \(C_n\), at least one token is at an integer position strictly between \(0\) and \(n-1\), and it may move both directions without collision; these two neighbours have baseline colours \(b_n(p)-1\) and \(b_n(p)+1\) modulo three. If its tokens are adjacent, the two outward moves similarly give the two other colours, except possibly at \((0,1)\) and \((n-2,n-1)\), whose outward moves cross the chosen integer-label cut. The wrap-adjacent pair \((0,n-1)\) has ordinary inward moves in opposite directions and is not an exception. When \(3\mid n\), even the two exceptional pairs have opposite-colour outward moves because the wrap increment \(n-1\) is \(-1\) modulo three. The baseline is therefore a three-domatic colouring for every multiple of three.

**A finite-boundary argument for the other residues.** Let \(P_n\) be the four entries changed in the displayed rule, and let \(T_n\) comprise \((0,1)\), \((n-2,n-1)\), and the closed neighbourhoods of all members of \(P_n\). Every token pair outside \(T_n\) retains its entire baseline-coloured closed neighbourhood, so the preceding paragraph proves its three-colour condition. It remains to check \(T_n\).

For \(n\equiv1\pmod3\) and \(n\ge10\), the members of \(T_n\) are exactly
\[
\begin{gathered}
(0,1),(0,2),(0,n-3),(0,n-2),(0,n-1),\\
(1,n-2),(1,n-1),(2,n-2),(2,n-1),(3,n-1),(n-2,n-1).
\end{gathered}
\]
For \(n\equiv2\pmod3\) and \(n\ge11\), they are exactly
\[
\begin{gathered}
(0,1),(0,2),(0,n-4),(0,n-3),(0,n-2),(0,n-1),\\
(1,n-3),(1,n-2),(1,n-1),(2,n-2),(2,n-1),\\
(3,n-1),(n-3,n-1),(n-2,n-1).
\end{gathered}
\]
These expressions are obtained by listing the at most four token moves from each changed pair, plus the two cut-adjacent pairs. For fixed residue, increasing \(n\) by three and replacing every near-right-end index \(n-j\) by \(n+3-j\) is a bijection of these lists and identifies their closed-neighbourhood colour multisets: each token move retains its type, while every baseline integer sum changes by a multiple of three. This applies from \(n=10\) and \(n=11\), respectively, since then left and right boundary sites in the displayed lists are separated. Hence one exact boundary check at each of those two lengths proves the corresponding statement for all higher lengths in the same residue. The two remaining lengths \(n=7,8\) are checked directly.

The standalone `boundary_certificate.tsv` lists **all** 50 pairs in \(T_7,T_8,T_{10},T_{11}\), their assigned colours, and their computed sets of colours in the closed neighbourhood. Every last field equals `012`. Its rows can be checked directly by the token-move definition, independently of any asymptotic computation. This proves the explicit three-domatic construction at every \(n\ge6\).

**The two small exceptions.** The graph \(F_2(C_4)\) is \(K_{2,4}\), where its four degree-two vertices have the same two neighbours (the two remaining token pairs). A three-domatic colouring would require those two common neighbours to take distinct colours and all four degree-two vertices to take the third colour. But then the closed neighbourhood of either common neighbour misses the other common neighbour's colour. Thus three classes are impossible.

For \(n=5\), denote the five adjacent token pairs by \(A_i=\{i,i+1\}\) and the five other pairs by \(B_i=\{i,i+2\}\), with indices modulo five. The closed neighbourhood of \(A_i\) is exactly \(\{A_i,B_{i-1},B_i\}\). Three-domaticity would require all three colours there, hence the cyclic sequence of colours on \(B_i\) must be a proper three-colouring of a five-cycle. Every such colouring is equivalent, under cyclic relabelling and colour permutation, to \((0,1,0,1,2)\): a proper three-colouring uses class sizes \((2,2,1)\), and fixing the unique singleton leaves one alternating pattern on the other four vertices. The forced sequence on \(A_i\) is then \((1,2,2,2,0)\). Yet \(B_1\) has closed-neighbourhood vertices \(\{B_1,B_3,B_4,A_1,A_2\}\), with colours \(\{1,1,2,2,2\}\). It misses colour zero, a contradiction.

Finally, every connected graph with at least two vertices has a domatic two-partition: choose a maximal independent set and its complement. Indeed, maximality makes the independent set dominating, and the complement dominates all its vertices since there are no isolated vertices. This supplies the lower bound two for the two exceptional graphs. Together all cases establish the formula.

## Verification
Run `python3 verify.py` with `boundary_certificate.tsv` in the same directory. The script uses only the Python 3 standard library. It (i) constructs the two-token graph from legal token moves and checks the explicit three-colouring for \(n=3\) and all \(6\le n\le140\); (ii) independently regenerates every row of the 50-line boundary certificate and checks near-boundary stability under adding three cycle sites; and (iii) exhaustively tests all \(3^6=729\) colour assignments for \(F_2(C_4)\) and all \(3^{10}=59049\) for \(F_2(C_5)\), confirming that none is three-domatic. These bounded calculations are supplementary to the unrestricted proof above; sampling lengths through 140 alone would not prove the infinite claim.

## Relationship to prior work
The two-token graph (also called the double-vertex graph or symmetric square) is standard. Acosta Troncoso and Rivera (2026) determine the **minimum size of one dominating set** in the two-token graph of a path, not the maximum number of disjoint dominating classes in the two-token graph of a cycle. Fabila-Monroy and Gómez-Galicia (2025) investigate domination numbers of token graphs of stars and complete graphs. Prabhu and Manjula (2019) derive bounds for the domination number of general double-vertex graphs. Audenaert, Godsil, Royle, and Rudolph (2005) study spectra of symmetric squares, the same graph construction under another name, not domatic partitions. Hartnell and Rall (2025) study an adversarial domatic **game**, which is not the ordinary domatic invariant determined here. Searches of the ordinary-domatic and two-token-cycle terminology did not locate a prior statement of this exact sharp threshold or the four-entry modular construction. This is a best-knowledge comparison, not a claim of certified historical priority.

## Limitations
The theorem is restricted to the ordinary domatic number of two-token graphs of **simple cycles**. The four recolourings are an existence construction, not a classification of all partitions or a minimum recolouring-distance assertion. The formula says nothing about general token numbers, general host graphs, domatic games, or total domatic partitions. The finite verification and self-review are not independent mathematical certification. Priority remains provisional because historical indexing and inaccessible literature may be incomplete.

## References
1. E. Acosta Troncoso and L. M. Rivera, *The domination number of the 2-token graph of path graphs*, arXiv:2610.11265v1, first public October 8, 2026. https://arxiv.org/abs/2610.11265
2. R. Fabila-Monroy and S. G. Gómez-Galicia, *Domination number of Token Graphs*, arXiv:2509.16448v1, September 19, 2025. https://arxiv.org/abs/2509.16448
3. R. Prabhu and K. Manjula, *Domination in Double Vertex Graphs*, Journal of Informatics and Mathematical Sciences 11 (2019), 339–343, DOI:10.26713/jims.v11i3-4.1308.
4. J. Hartnell and D. Rall, *The domatic number game played on graphs*, Ars Combinatoria 165 (2025), 31–43, DOI:10.61091/ars165-03.
5. K. Audenaert, C. Godsil, G. Royle, and T. Rudolph, *Symmetric Squares of Graphs*, arXiv:math/0507251v1, July 12, 2005. https://arxiv.org/abs/math/0507251
