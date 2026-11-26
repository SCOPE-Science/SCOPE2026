# Complete strong-majority edge-colouring classification of \(K_{m,n}\)

## Finding
For every pair of integers \(2\le m\le n\), let \(\operatorname{Maj}'(K_{m,n})\) be the least number of edge colours such that, for every edge and every colour, no more than half of the edges adjacent to that edge have that colour. Then
\[
\operatorname{Maj}'(K_{m,n})=\begin{cases}
2,&m=2\text{ and }2\mid n,\\
4,&(m,n)\in\{(3,4),(4,5)\},\\
3,&\text{otherwise}.
\end{cases}
\]
The number of successful edge assignments using two *named* colours equals \(4\) if \((m,n)=(2,2)\), equals \(\binom{n}{n/2}\) when \(m=2\) and \(n\ge4\) is even, and equals zero in all other cases. These assertions jointly specify a complete two-parameter family, including the two known four-colour obstructions.

## Assumptions and scope
Graphs are finite and simple. The bipartition of \(K_{m,n}\) has labelled vertices \(u_0,\ldots,u_{m-1}\) and \(v_0,\ldots,v_{n-1}\), with \(2\le m\le n\). An edge-colouring is *not* required to be proper. Two edges are adjacent when they share a vertex and are distinct. The edge \(u_iv_j\) has \(m+n-2\) neighbours. A colour is legal there if it occurs among those neighbours at most \(\lfloor (m+n-2)/2\rfloor\) times. Named two-colour assignments distinguish the two colour names. A monochromatic assignment cannot be legal because every edge has at least two neighbours.

## Proof
**Two-colour rigidity.** In a red/blue colouring, let \(x_{ij}\in\{0,1\}\) indicate red, \(r_i=\sum_jx_{ij}\), and \(s_j=\sum_ix_{ij}\). At every edge, the red and blue counts in its edge-neighbourhood must each equal half of its \(m+n-2\) neighbours, because each is at most half and together they account for all neighbours. Thus \(m+n\) is even and
\[
r_i+s_j-2x_{ij}=(m+n-2)/2.\tag{1}
\]
Summing (1) over columns gives \((n-2)r_i\) independent of \(i\); summing over rows gives \((m-2)s_j\) independent of \(j\). For \(m,n\ge3\), both row and column counts are therefore constant and (1) makes every \(x_{ij}\) identical, impossible. For \(m=2<n\), all row red counts coincide, and (1) makes each column monochromatic. If \(t\) columns are red, then an edge in a red column has \(t\) red neighbours, while an edge in a blue column has \(n-t\) blue neighbours. The condition forces \(t=n/2\). This establishes existence exactly when \(n\) is even, and the \(\binom{n}{n/2}\) count. For \((m,n)=(2,2)\), direct inspection gives four solutions: the two ways to monochromatize rows and the two ways to monochromatize columns.

**Three-colour templates.** For any \(m,n\), let \(a_{ij}=(i+j)\bmod3\). Each row contains any colour at most \(\lceil n/3\rceil\) times, and each column at most \(\lceil m/3\rceil\) times. For an edge and any colour *other than its own*, the adjacent multiplicity is at most the sum of these ceilings; for its own colour subtract two. Thus the template works whenever
\[
\lceil m/3\rceil+\lceil n/3\rceil\le\lfloor(m+n-2)/2\rfloor.\tag{2}
\]
For \(m,n\ge5\), (2) follows separately from \(\lceil q/3\rceil\le(q-1)/2\) for all integers \(q\ge5\). It also holds for \(m=4,n=6\) and for \(m=4,n\ge8\). When \(m=3\), each column of the cyclic template contains three different colours; an edge has at most \(\lceil n/3\rceil+1\) neighbours in a different colour, hence the template is valid for \(n=3\) and every \(n\ge5\). For \(m=2\), colour every column monochromatically, distributing its \(n\) columns as evenly as possible over three colour names. Every edge then sees at most \(\lceil n/3\rceil\) neighbours of a given colour, which is at most \(\lfloor n/2\rfloor\) whenever \(n\ge3\). The \(n=2\) case has a two-colouring already.

**Three exceptional explicit upper bounds.** Rows of each matrix below represent the edge colours of the corresponding \(K_{m,n}\):

For \(K_{4,4}\) a legal three-colouring is
```text
0 1 0 0
2 2 0 1
0 1 1 2
2 2 1 0
```
For \(K_{4,7}\) a legal three-colouring is
```text
2 1 1 2 2 0 0
0 1 2 0 2 1 1
1 0 0 1 0 2 2
2 0 0 2 0 1 1
```
For \(K_{4,5}\) a legal four-colouring is
```text
3 3 2 3 0
2 0 1 2 1
3 0 1 1 2
1 3 1 2 0
```
Each satisfies the defining edge-neighbourhood inequalities by direct counting. A four-colouring of \(K_{3,4}\) uses the four distinct colour names on its four columns, with each column monochromatic: any edge then sees two neighbours of its column colour and one neighbour of each other colour.

**Lower bounds at the four-colour exceptions.** The impossibility of a three-colouring of \(K_{3,4}\) is established in Observation 9 of Pękała–Przybyło, arXiv:2608.04122. Independently, it has a short finite exhaustion: no row can use a colour three times, since an edge of a different colour would see three same-colour neighbours (and a completely monochromatic row would make each edge see three). Up to permuting columns and colour names the first row must thus be \((0,0,1,1)\) or \((0,0,1,2)\). The remaining two rows each have \(3^4\) possibilities. The enclosed verifier tests all \(2\cdot3^8=13122\) canonical matrices and finds none legal.

For \(K_{4,5}\), every edge has seven neighbours, so each colour may occur on at most three of them. Fix a single colour class \(F\), and let \(r_i,s_j\) denote its row and column degrees. For a cell outside \(F\), \(r_i+s_j\le3\); for a cell inside \(F\), \(r_i+s_j\le5\). No row can have degree four (a missing cell would contradict the first bound) or degree five (any cell would have four same-colour neighbours). If a row has degree three, the other two columns are empty and each of its three selected columns has degree at most two; hence \(|F|\le6\). Otherwise all four row degrees are at most two. If \(|F|\ge7\), their degree pattern must be \((2,2,2,2)\) or \((2,2,2,1)\). A column of degree at least two must then be present in *every* degree-two row, since its omission gives \(r_i+s_j\ge4\). Such a column exists because seven edges cannot occupy five columns with degrees at most one. In the first pattern the column has degree four, contradicting the inside bound for degree-two rows. In the second pattern the column has degree at least three and must also meet the degree-one row (otherwise its missing cell has degree sum at least four); again the column has degree four, a contradiction. Therefore \(|F|\le6\) for every colour. Three colours cover at most eighteen of the twenty edges, so a three-colouring is impossible. This obstruction is also contained as the \(k=2\) instance of the earlier generalized threshold result cited below; it is included here for a self-contained proof, not claimed as new.

Together the constructions, the two-colour rigidity, and the two four-colour lower bounds prove the asserted classification and count.

## Verification
Run `python3 verify.py`. It independently checks the explicit matrices and all construction cases \(2\le m\le15\), \(m\le n\le23\), exhausts the \(13122\) canonical three-colour matrices for \(K_{3,4}\), and exhausts all \(2^{20}\) individual-colour subsets for the \(K_{4,5}\) bound. Output is recorded in `verify_output.txt`. These are finite corroborations; the claims for unbounded orders rest on the preceding inequalities and explicit constructions.

## Relationship to prior work
Kalinowski, Kamyczura, Pilśniak and Woźniak introduced the strong majority edge index and established general bounds (arXiv:2605.23828, Section 3). Pękała and Przybyło proved that minimum degree at least five guarantees three colours, and proved \(K_{3,4}\) requires four (arXiv:2608.04122, Theorem 4 and Observation 9). A subsequently publicized generalized bipartite threshold result proves the \(K_{4,5}\) three-colour obstruction and the sharp minimum-degree-five threshold (published-finding corpus identifier `2026/9/17/SCOPE005`). Those prior conclusions are **not** presented as novel here. The additional contribution is a full two-parameter classification, including the two-colour rigidity/count and constructive resolution of the remaining degree-two, degree-three and degree-four complete-bipartite regimes (not implied by either global minimum-degree theorem).

## Limitations
The theorem applies only to complete bipartite simple graphs with both part sizes at least two. It does not provide counts of optimal three- or four-colourings. The small matrix verifications are not proofs for arbitrarily large orders; the infinite constructions are established algebraically. Bibliographic overlap remains possible for equivalent classifications under other terminology. No independent validation has been performed.

## References
1. R. Kalinowski, M. Kamyczura, M. Pilśniak, M. Woźniak, *Strong majority colorings of graphs*, arXiv:2605.23828, first posted 2026-05-22, https://arxiv.org/abs/2605.23828.
2. P. Pękała, J. Przybyło, *On Strong Majority Edge Colourings with Few Colours*, arXiv:2608.04122, first posted 2026-08-04, https://arxiv.org/abs/2608.04122.
3. *Exact bipartite threshold for generalized strong-majority edge colouring*, published-finding corpus, identifier `2026/9/17/SCOPE005`, https://github.com/Resultary/2026/blob/main/2026/9/17/SCOPE005/RESULT.md.
4. S. Antoniuk, M. Prorok, N. Salia, *Strong Majority Edge-Coloring*, arXiv:2607.00212, first posted 2026-06-30, https://arxiv.org/abs/2607.00212.
