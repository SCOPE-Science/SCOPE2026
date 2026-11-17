# The first odd temporal clock of elementary Rule 18: a universal nine-step exclusion and an eleven-site onset

## Finding

Consider synchronous binary elementary cellular automaton Rule 18 with cyclic boundary conditions. For every circumference \(n\ge3\), the all-zero state is the *only* state fixed by any temporal iterate \(F_n^t\) at \(t\in\{1,3,5,7,9\}\). Nevertheless, the eleven-cell ring has exactly two primitive temporal eleven-orbits. Moreover, rings of sizes \(3\le n\le10\) have no nontrivial primitive odd temporal orbit of *any* length. Hence eleven is simultaneously the least nontrivial odd temporal period occurring on a finite ring and the least ring circumference supporting a nontrivial odd period.

A sample eleven-site starting state is the binary word `01001000011` (the integer 579 with site 0 represented by the least significant bit); it has exact temporal period eleven. States are indexed by sites: rotations are **not** quotiented out when counting orbits. There are exactly \(22\) eleven-periodic configurations on the eleven-site ring, arranged in two temporal orbits.

## Assumptions and scope

For \(n\ge3\), set \(X_n=\{0,1\}^{\mathbb Z/n\mathbb Z}\). Define \(F_n:X_n\to X_n\) by the Rule 18 local map

\[
 (F_n(x))_i=(1-x_i)(x_{i-1}\mathbin{\mathrm{xor}}x_{i+1}),\qquad i\in\mathbb Z/n\mathbb Z.
\]

The rule produces a one precisely for neighborhoods `001` and `100`, and zero otherwise. The least temporal period of a recurrent state is the least positive \(p\) such that \(F_n^p(x)=x\). A primitive temporal \(p\)-orbit is its set of \(p\) distinct successive configurations, without modding out spatial translations or reflections. The finite directed-state claims below are about *all* ring circumferences in this domain, not a numerical sample. No claim is made about dynamics on the bi-infinite lattice or about attraction basins.

## Proof

**Temporal-history transfer lemma.** Fix a time height \(t\ge1\). Encode the successive time values of each spatial site in a putative \(t\)-periodic history as a word \(m\in\{0,1\}^t\), with temporal indices modulo \(t\). Construct a spatial graph \(G_t\) whose vertices are ordered pairs of time words \((l,m)\). It contains the directed edge

\[
 (l,m)\longrightarrow(m,r)
\]

if and only if, at *every* temporal coordinate \(j\),

\[
 m_{j+1}=(1-m_j)(l_j\mathbin{\mathrm{xor}}r_j).
\]

For every \(n\ge3\), configurations fixed by \(F_n^t\) are in one-to-one correspondence with length-\(n\) closed directed walks in \(G_t\) with a specified starting spatial site. Indeed, assigning the middle time word to each site yields the entire \(t\)-by-\(n\) space-time torus; the edge condition is exactly the local update constraint, including time closure. Conversely, the time histories of any \(F_n^t\)-fixed configuration give such a walk.

**Explicit finite edge rule.** Identify each time word with its \(t\)-bit integer, and write \(T(m)\) for the cyclic rotation whose bit \(j\) equals bit \(j+1\) of \(m\). If \(m\mathbin{\&}T(m)\ne0\), then no edge leaves \((l,m)\), because a one cannot be followed immediately by another one at the same site. Otherwise, the bits of \(r\) at coordinates where \(m_j=0\) are forced by \(r_j=l_j\mathbin{\mathrm{xor}}T(m)_j\). On coordinates where \(m_j=1\), the bits of \(r\) are arbitrary. This generates exactly all edges, without heuristic pruning.

**Complete short-odd-height certificate.** `check_transfer.cpp` constructs these edges exactly and computes every strongly connected component using full reverse-graph traversal. The results are:

| \(t\) | Active vertices | Edges | Components containing a directed cycle | Vertices in cyclic components |
|---:|---:|---:|---:|---:|
| 1 | 3 | 2 | 1 | 1 |
| 3 | 48 | 56 | 1 | 1 |
| 5 | 583 | 992 | 1 | 1 |
| 7 | 6,583 | 16,256 | 1 | 1 |
| 9 | 72,048 | 261,632 | 1 | 1 |

For each height the sole cyclic component is the zero pair \((0,0)\) with its self-loop, and no nonzero vertex lies on a directed cycle. A closed walk lies entirely in cyclic strongly connected components; therefore any closed walk must be identically zero. By the transfer lemma, \(\operatorname{Fix}(F_n^t)=\{0^n\}\) for all \(n\ge3\) at the five listed heights. In particular, no nontrivial primitive temporal odd period less than eleven is possible.

**First occurrence.** The independent direct-state program `check_rings.py` exhaustively constructs the full deterministic state map for every \(3\le n\le11\), following each path until it meets a previously seen state. It finds no odd primitive orbit except the fixed zero state for any \(3\le n\le10\). At \(n=11\) it finds precisely two eleven-orbits, with smallest binary-integer representatives 75 and 105; its orbit verification checks that the first return occurs exactly at step eleven. The displayed integer 579 belongs to one such orbit. Because these are complete finite spaces of respectively \(2^n\) states, not partial searches, the spatial minimum and the exact count at \(n=11\) follow.

## Verification

All computations use integers and deterministic exhaustive algorithms, without numerical tolerances or randomness. Compile `check_transfer.cpp` with `g++ -std=c++17 -O2 -Wall -Wextra check_transfer.cpp -o check_transfer` and run `./check_transfer`; compare the exact output to `transfer_output.txt`. Independently run `python3 check_rings.py` and compare to `rings_output.txt`. The two programs use different representations: temporal-history graph SCCs versus direct local-rule state evolution. The transfer certificate exhausts the \(4^t\)-vertex possibility space (edges on reachable portions); the direct program exhausts every \(2^n\)-state ring space for the stated small circumferences. The two mechanisms support different parts of the theorem, and neither treats sampling as universal proof.

## Relationship to prior work

Wolfram (1983) established the Rule 18/domain-wall framework and its correspondence with Rule 90 on suitable domain configurations. Hanson and Crutchfield (1991) developed a regular-language and attractor-basin account, including finite periodic boundary conditions and rare spatially periodic states. Their domain-statistical and language-attractor results do not give the present all-circumference five-height temporal exclusion or the exact first odd ring. Sabrié and Törmä (arXiv preprint 2023; 2026 journal version) analyze the limit, generic limit and measure limit sets and kink behavior; their stated results do not classify the first primitive odd ring clock. Stricker's 2022 Rule 18 numerical question studies evolution from a restricted two-live-cell initial family, not an exhaustive census over all configurations. Earlier exact Rule 18 one-step-image and temporal-two results concern different return predicates and do not imply an odd-eleven threshold.

This is an exact finite-certificate result for one natural threshold, not a complete temporal zeta function. The general idea of constructing a de Bruijn-style time-column graph is standard; the claimed result is the exhaustive short-odd obstruction paired with the sharp eleven-site occurrence.

## Limitations

The graph certificate excludes only temporal fixed points at the odd heights 1, 3, 5, 7 and 9. It does not rule out longer odd periods, classify all even periods, or count eleven-orbits for general \(n\). The spatial minimum proof uses complete enumeration only through eleven sites; this is sufficient for its bounded claim. External priority against less visible historical catalogues and an inaccessible thesis containing finite-period tables is uncertain. Reproduction of the embedded programs is not independent external mathematical validation.

## References

1. S. Wolfram, “Statistical mechanics of cellular automata,” *Reviews of Modern Physics* **55** (1983), 601–644, https://doi.org/10.1103/RevModPhys.55.601. Publisher first publication: 1983-07-01. Author-hosted full text: https://content.wolfram.com/sw-publications/2020/08/statistical-mechanics-cellular-automata.pdf.
2. J. E. Hanson and J. P. Crutchfield, “The Attractor-Basin Portrait of a Cellular Automaton,” Santa Fe Institute working paper 1991-02-012, https://sfi-edu.s3.amazonaws.com/sfi-edu/production/uploads/sfi-com/dev/uploads/filer/aa/5a/aa5a7d95-aa45-4ca8-a057-c2b154d34d12/91-02-012.pdf.
3. E. Sabrié and I. Törmä, “Limit dynamics of elementary cellular automaton 18,” arXiv:2308.12744 (2023), journal DOI https://doi.org/10.1017/etds.2026.10300.
4. H.-P. Stricker, “Mysteries of Wolfram's rule 18,” MathOverflow question, 2022-09-06, https://mathoverflow.net/questions/429911/mysteries-of-wolframs-rule-18.
