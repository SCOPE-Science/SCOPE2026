# Exact ten-period locating-total domination law for circular prisms

## Finding
Let \(Y_n=C_n\square K_2\) be the circular prism, with \(n\ge 3\). A locating-total dominating set \(S\) has a selected neighbor at **every** vertex, including selected vertices, and has distinct selected open-neighborhood signatures \(N(u)\cap S\) for distinct vertices \(u\notin S\). Its minimum size is exactly
\[
\boxed{\gamma_t^L(Y_n)=\left\lceil\frac{4n}{5}\right\rceil+\mathbf{1}_{\{n\equiv6\pmod{10}\}}\qquad(n\ge3).}
\]
Equivalently, the usual cubic lower bound is sharp in every residue class except \(n\equiv6\pmod{10}\), where precisely one extra landmark is necessary. The result corrects the proposed five-residue formula in Raza–Iqbal–Khan–Botmart (2021): its \(n\equiv3\pmod5\) branch is too large, and its \(n\equiv1\pmod5\) branch is too large when \(n\equiv1\pmod{10}\). An infinite subfamily in the first branch was established previously; the result here gives the complete all-order law, including its exceptional class.

## Assumptions and scope
For every integer \(n\ge3\), \(Y_n\) has vertices \((i,r)\) with \(i\in\mathbb Z/n\mathbb Z\) and \(r\in\{0,1\}\); vertices \((i,r)\) are adjacent to \((i-1,r),(i+1,r),(i,1-r)\). For each \(S\subseteq V(Y_n)\), write \(\sigma_S(v)=N(v)\cap S\). The property used throughout is
\[
\sigma_S(v)\ne\varnothing\quad\text{for all }v,
\qquad
\sigma_S(u)\ne\sigma_S(v)\quad\text{for all distinct }u,v\notin S.
\]
This is ordinary locating-total domination, not an identifying code (which distinguishes selected vertices as well), and not ordinary or open locating domination. All graphs are finite, simple, labelled circular prisms; no assumptions on primality or parity are made.

## Proof
**Lemma 1 (local-window test).** For \(n\ge5\), encode a selected subset by a cyclic word \(c_0\cdots c_{n-1}\) on the alphabet \(\{0,1,2,3\}\): the two binary digits of \(c_i\) record the selected vertices in column \(i\). A word is locating-total dominating if and only if, at each column \(i\), the following five-column test succeeds in the ordered window \((c_{i-1},c_i,c_{i+1},c_{i+2},c_{i+3})\):

(a) each of the two vertices in the center column \(i\) has a selected neighbor among its three possible neighbors;

(b) for every unselected center-column vertex \((i,r)\), its selected-neighborhood signature differs from that of every other unselected vertex \((j,s)\) with \(j=i,i+1,i+2\), excluding the center vertex itself and checking the other vertex in column \(i\) once.

Indeed, (a) is precisely total domination. If two unselected vertices have equal nonempty signatures then their selected-neighbor sets intersect, so their graph distance is at most two. In a prism this implies their cyclic column distance is at most two. Hence every forbidden pair is captured by the oriented center-to-forward comparison in (b). Conversely all these comparisons are required by locating-total domination. Five consecutive columns are distinct for \(n\ge5\), and every neighbor used by the test lies inside the window. This proves both directions.

**Lemma 2 (finite-state exact optimization).** Let the 256 states be four-column words \(s=(a,b,c,d)\in\{0,1,2,3\}^4\). For every fifth symbol \(e\), put a directed transition from \(s\) to \(t=(b,c,d,e)\) if the five-column test of Lemma 1 succeeds on \((a,b,c,d,e)\). Give that transition weight \(w(e)\), the number of 1-bits of \(e\); put weight \(\infty\) if no transition is present. Denote the resulting \(256\times256\) min-plus matrix by \(T\), where multiplication uses \(\min\) in place of addition and addition in place of multiplication. The exact minimum is
\[
\gamma_t^L(Y_n)=\min_{s\in\{0,1,2,3\}^4}(T^{\otimes n})_{s,s}\qquad(n\ge5).
\]
A cyclic word produces a unique closed walk of length \(n\) by reading consecutive four-column windows. Its transitions impose precisely the tests in Lemma 1; the walk's weight is \(\sum_i w(c_i)=|S|\). Conversely, for \(n\ge5\) any such closed walk is the consecutive-window presentation of a unique cyclic word, since the overlapping four-symbol states enforce agreement. Therefore taking the minimum diagonal entry performs **exact** optimization, not sampling.

**Lemma 3 (finite min-plus identity).** Exact integer operations give
\[
\boxed{(T^{\otimes18})_{s,t}=(T^{\otimes8})_{s,t}+8}
\]
for every state pair whose entry is finite, while the locations of infinite entries in the two matrices coincide. There are exactly 729 finite transitions and exactly 41,728 finite entries in each of these two powers. The accompanying `verify_prism.py` constructs every transition directly from the local predicate, computes both full matrices, and asserts the equality separately at all 65,536 state pairs. These finite integer identities are the computation certificate for the lemma; they are not extrapolated from an observed numerical sequence.

Associativity of min-plus multiplication gives \(T^{\otimes(n+10)}=8\odot T^{\otimes n}\) for all \(n\ge8\), where scalar min-plus multiplication adds eight to every finite entry. Taking minimum diagonals yields
\[
\gamma_t^L(Y_{n+10})=\gamma_t^L(Y_n)+8\qquad(n\ge8).
\]

**Initial cases.** Exact traces of the same matrix give the following values:

| \(n\) | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(\gamma_t^L(Y_n)\) | 4 | 6 | 6 | 7 | 8 | 8 | 9 | 10 | 11 | 12 | 12 | 14 | 14 |

For the two remaining orders, exhaustive whole-graph enumeration gives \(\gamma_t^L(Y_3)=3\) and \(\gamma_t^L(Y_4)=4\). Thus the claimed formula is checked at \(3\le n\le17\), and the ten-step identity proves every remaining order by induction. This completes the proof. As explicit independent witnesses, the cyclic column-mask words `30222030110` and `3003030030330030` give valid locating-total dominating sets with 9 and 14 vertices respectively at circumferences 11 and 16. The verifier checks their full-graph signatures; the matrix certificate supplies the matching lower bounds.

## Verification
Run `python3 verify_prism.py` with Python 3.8 or later; no external packages or network are needed. It performs exact integer full-matrix computation, verifies the complete 729-transition and 41,728-finite-entry certificate, and asserts the thirteen base values at orders 5 through 17. A separate direct whole-graph subset predicate, constructed without the transfer test, exhaustively verifies the minimum size and the number of minimum sets at orders 3 through 8. The required final outputs are `TROPICAL_CERTIFICATE_OK`, `BASE_VALUES_OK`, `INDEPENDENT_BRUTE_OK`, and `VERIFY_OK`. The computations certify finite statements used in the infinite proof, while the two local-to-global lemmas justify their application to all orders.

## Relationship to prior work
Raza, Iqbal, Khan and Botmart (2021), *Computing locating-total domination number in some rotationally symmetric graphs*, Theorem 5 and Conjecture 2, prove upper constructions and propose a five-residue equality law for the same graph family and invariant. Their general cubic lower bound is also used as background. The formula here differs in the \(1\pmod5\) and \(3\pmod5\) cases, while agreeing where their bound is already sharp. A separate published indexed finding, *A sharp infinite counterfamily to the prism locating-total domination conjecture* (2026), established \(\gamma_t^L(C_{8+5t}\square K_2)=7+4t\). That entire infinite subfamily is **prior art**, not a new result here. It does not cover the other residue classes, the sharp \(6\pmod{10}\) obstruction, or a global ten-period law. Results about ordinary domination on circular prisms and locating-total domination on complete prisms concern different optimization predicates or graph families; they do not imply this classification.

## Limitations
The proof has an indispensable computer-checked finite identity rather than a handwritten entry-by-entry derivation of the 256-state min-plus matrix equality. The complete executable certificate is supplied, with exact arithmetic and no random choices. The statement determines minimum **cardinality**, not a closed polynomial counting all locating-total dominating sets or all minimum configurations. It applies only to circular prisms. Literature comparison does not establish absolute priority against unpublished or unindexed work; independent mathematical audit has not been performed.

## References
1. H. Raza, N. Iqbal, H. Khan, T. Botmart, *Computing locating-total domination number in some rotationally symmetric graphs*, Science Progress 104(4), first published online 2021-11-17. DOI: https://doi.org/10.1177/00368504211053417 . See Theorem 5, Conjecture 2, and the discussion of prism graphs.
2. *A sharp infinite counterfamily to the prism locating-total domination conjecture*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-infinite-counterfamily-to-the-prism-locating-total-domin--78f62d2dad3b . Comparison was made with the indexed result summary; its full text was not accessible in this review.
3. M. A. Henning and N. J. Rad, *Locating-total domination in graphs*, Discrete Applied Mathematics 160 (2012), https://doi.org/10.1016/j.dam.2012.04.004 . Definitions and background bounds only.
