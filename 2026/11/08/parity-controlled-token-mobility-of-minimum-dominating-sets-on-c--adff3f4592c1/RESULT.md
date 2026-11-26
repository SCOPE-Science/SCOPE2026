# Slide-frozen minimum dominating sets with a cyclic jump graph on prisms of length 1 modulo 4

## Finding

Let \(P_n=C_n\square K_2\) for \(n\ge5\) with \(n\equiv1\pmod4\). Let \(\mathcal J_n\) be the graph of labeled minimum dominating sets, with two sets adjacent if one can be obtained from the other by replacing a single vertex. Let \(\mathcal T_n\) use the same adjacency but require the departing and arriving vertices to be adjacent in \(P_n\). Then
\[
\mathcal J_n\cong C_{2n},\qquad \mathcal T_n\cong 2n K_1.
\]
Thus every minimum dominating set is frozen under token slides, whereas exactly two jumps are available from every state, and all states can be reached by jumps. The jump graph has radius and diameter \(n\).

## Assumptions and scope

The host is a finite simple undirected graph with a top and bottom vertex in every cyclic column \(i\in\mathbb Z/n\mathbb Z\). Edges are rungs within columns and same-row edges between consecutive columns. Domination means coverage by closed neighborhoods; a dominating set need not be independent. Both move graphs keep cardinality fixed at the minimum. The minimum size and state count are background. The claim is the exact move graphs and jump distances for the residue class stated above.

## Proof

**1. The minimum words.** Write \(n=2m-1\), so \(m\ge3\) is odd. Since every closed neighborhood has size four, a dominating set needs at least \(m\) tokens. Denote a top-only column by \(A\), a bottom-only column by \(B\), and an empty column by \(C\). A dominating word with \(m\) tokens and only these three letters exists: put a pair of \(A\)'s at columns \(0,1\), then alternate empty and singleton columns around the rest of the cycle. Starting from column 1, change the singleton color each time a \(C\) is crossed. There are \(m-1\) empty columns, an even number, so this instruction returns to \(A\) at column 0. Each empty column sees tokens of both colors, and every occupied column is dominated by its own token via the rung. The minimum size is therefore \(m\).

In any minimum set the excess number of neighborhood incidences above one per vertex is \(4m-2n=2\). If both vertices of column 0 are selected, their neighborhoods already use both excess incidences at column 0, and together cover both rows of columns \(-1,0,1\). Any further selected vertex in columns \(-2,-1,1,2\) would overlap that union and exceed the budget. The two vertices of column 2 could then only be dominated by selecting both vertices of column 3. For \(n=5\), column 3 is itself forbidden; for \(n\ge9\), the two selected vertices in column 3 would use additional excess incidences. Thus all occupied columns are singletons.

Consecutive empty columns are impossible: dominating the first of such a pair would require both tokens in the preceding column. Since there are \(m\) singleton and \(m-1\) empty columns, exactly one interval between cyclically consecutive empty columns contains two singletons and the others contain one. Write \(i,i+1\) for the distinguished consecutive singleton pair. Each empty column must have one \(A\) and one \(B\) as flanks. Because the path of singles around the other way between the pair members crosses \(m-1\) empty columns, both members of the pair have the same color. Choosing \(i\) and that color determines the entire word. In particular these ordinary minima are not independent.

**2. Exactly two moves.** At a fixed column support the two colorings are complementary, differing at all \(m\) tokens, so no one-token move keeps the support. Removing a singleton outside the distinguished pair creates two empty–empty edges, one on either side of the vacated column. Filling either neighboring empty column leaves the other empty–empty edge, and filling any other column leaves both. A replacement is therefore impossible there. Removing the left member at \(i\) forces a token into the empty column \(i-1\); removing the right member at \(i+1\) forces a token into \(i+2\).

In the left move, the old color of the token at \(i+1\) determines the new token at \(i-1\): it must be the opposite color to dominate the newly empty column \(i\). Every other remaining empty column keeps its valid flanks. Thus the new token is in the opposite row from the departing one, and this move is a jump but not a slide. The right move is its reflected counterpart and is likewise a jump but not a slide. The new pair after the left move starts at \(i-2\), whose original color is opposite to the old pair's color. Hence the left move maps \((i,x)\) to \((i-2,\bar x)\), and the right move is the inverse. Since \(n\) is odd, subtracting 2 visits every column, and after \(n\) moves the starting column is recovered with its color flipped. The permutation is a single cycle of order \(2n\). Its two neighbors are distinct, so the undirected jump graph is \(C_{2n}\); the slide graph has no edges. The farthest vertex from any point on this jump cycle is at distance \(n\).

## Verification

The bundled finite tests can be run from the package root with `python3 verification/verify_prism_direct.py` and `python3 verification/verify_prism_language.py`. The first exhaustively checked minimum-size subsets and explicit moves for a small range, including \(n=5,9\); the second constructed the forced word families and compared every pair for one-token exchanges through \(n=129\), including all lengths in the present class in that interval. The recorded outputs include other residues for comparison. These checks are finite and neither are needed to infer the all-size claim, proved above.

## Relationship to prior work

Allagan [1, Theorem 3.1 and §3.3] gives the minimum-set count and cyclic-word approach; in the residue here the forced word language provides the input for analyzing exchanges. The additional step is to exclude every move except the two opposite-row exchanges, compute their action on the exceptional pair, and determine exact connectedness and distances. The numerical overlap index in [1, §4.2] does not classify these edges. Addition/deletion reconfiguration [2] uses an adjacency of a different kind.

The independent-domination exchange theorem [3] already gives both move graphs for the ordinary minima when \(4\mid n\) and when \(n\equiv3\pmod4,\ n\ge7\): in those classes the ordinary minimum words are independent and the two optima coincide. Indeed, when \(4\mid n\) disjoint closed neighborhoods exclude adjacent tokens. In the odd class with \(n\equiv3\pmod4,\ n\ge7\), the same incidence argument excludes double columns and the forced pair has opposite colors since there are \((n-1)/2\) empty columns, an odd number. In every graph, a one-token exchange between independent dominating sets moves along an edge, because the new vertex is dominated before the move but is adjacent to none of the retained vertices. These other residues are therefore background, not new claims. For \(n\equiv1\pmod4\), independent domination needs one more token and cannot give the ordinary minimum move graph by that equivalence.

## Limitations

No new claim is made for other residues, nonminimum sets, or other host graphs. The bounded literature comparison is not a guarantee of priority.

## References

1. J. Allagan, *Exact Dominion of the Prism Graph: Enumeration by Congruence Class via Cyclic Words*, arXiv:2601.03488v1, https://arxiv.org/abs/2601.03488v1.
2. A. Suzuki, A. E. Mouawad and N. Nishimura, *Reconfiguration of Dominating Sets*, arXiv:1401.5714, https://arxiv.org/abs/1401.5714.
3. *Minimum independent-domination reconfiguration on circular ladders*, Resultary, 2026-10-26, https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-minimum-independent-domination-reconfiguration-on-circular-ladde--5713d863fdac/RESULT.md.
