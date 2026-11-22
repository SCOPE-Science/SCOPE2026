# Simple-permutation rigidity of extremal external neighbourhood profiles

## Finding

Fix an integer \(m\ge4\) and a permutation \(\pi\) of \(\{1,\ldots,m\}\). Place \(m\) marked segments across two parallel lines, in upper order \(1,\ldots,m\) and lower order \(\pi(1),\ldots,\pi(m)\). For any finite extension by additional unmarked segments, count the different sets \(N_G(v)\cap A\) over unmarked vertices \(v\notin A\). Write \(T(\pi)\) for the maximum possible count over such extensions.

**Extremal-rigidity theorem.** We have
\[
T(\pi)=m^2-1\quad\Longleftrightarrow\quad\pi\text{ is simple}.
\]
Here simplicity means that no proper block of consecutive positions of length between \(2\) and \(m-1\) has consecutive values. Furthermore,
\[
\max_{\pi\ \mathrm{not\ simple}}T(\pi)=m^2-2.
\]
Both maxima are attained for every \(m\ge4\). The sharp unrestricted numerical value, and the sufficiency of simple marked permutations, are prior results [2,4]; the contribution is the converse classification and the exact non-simple boundary. This is a theorem about **specified two-line representations**, not a statement that a permutation graph has a unique representation or a classification of graph isomorphism types.

## Assumptions and scope

All graphs are finite simple undirected permutation graphs, represented by straight segments between two parallel lines with distinct endpoints. We consider only unmarked witnessing vertices and ordinary open-neighbourhood traces. The positions and values of the marked permutation are one-based. Define
\[
P_i=\{1,\ldots,i\},\qquad Q_j=\{a:\pi(a)\le j\},\quad0\le i,j\le m.
\]
A new segment placed in upper gap \(i\) and lower gap \(j\) has trace \(X_{i,j}=P_i\mathbin{\triangle}Q_j\). Every gap-pair can be populated by unmarked segments, with all endpoints distinct. Hence
\[
T(\pi)=\bigl|\{X_{i,j}:0\le i,j\le m\}\bigr|.
\]
No ambient graph-size bound is assumed. The trace sets from marked vertices themselves are not included in the definition; they are among the external possible traces, so the same upper capacity holds even when marked witnesses are allowed.

## Proof

**1. Collision geometry.** For two distinct cells \((i,j)\) and \((i',j')\), equality of traces means
\[
P_i\triangle P_{i'}=Q_j\triangle Q_{j'}.
\]
Neither coordinate difference can vanish alone. The two nonempty sides are precisely the marked elements in a consecutive interval of positions and a consecutive interval of ranks, respectively. Thus collisions are exactly pairs of endpoints of *common intervals* of the marked permutation. Each common interval with top positions \([a,b]\) and bottom ranks \([c,d]\) gives two equality edges in the grid of cells:
\[
(a-1,c-1)\sim(b,d),\qquad (a-1,d)\sim(b,c-1).
\]
In particular, for each singleton \(a\), write \(c=\pi(a)\); then the edges are \((a-1,c-1)\sim(a,c)\) and \((a-1,c)\sim(a,c-1)\). The full marked set yields \((0,0)\sim(m,m)\) and \((0,m)\sim(m,0)\). These \(2m+2\) equality edges form a graph \(H_0\) on the \((m+1)^2\) cells.

**2. The baseline graph.** Singleton edges are unit diagonals. Two singleton edges share a vertex only when they have the same slope and arise from consecutive positions whose values are consecutive in the matching direction. A maximal connected singleton-edge component therefore follows a monotone run of adjacent values; opposite slopes never share vertices. Adding the two full-set edges joins only the positive diagonal components incident with \((0,0)\), \((m,m)\), or the negative diagonal components incident with \((0,m)\), \((m,0)\). For every nonmonotone \(\pi\), \(H_0\) is a forest with exactly \(2m+2\) edges; a cycle using a full edge would require the whole permutation to be monotone in the corresponding direction. Because equality holds along every edge, this yields
\[
T(\pi)\le (m+1)^2-(2m+2)=m^2-1.
\]
If \(\pi\) is simple, there are no additional common intervals, and \(H_0\) is the complete equality graph. Thus \(T(\pi)=m^2-1\).

**3. Any proper nonmonotone common interval produces an extra collapse.** Let \([a,b]\) be a proper common interval of length \(\ell\ge3\), with lower ranks \([c,d]\). Within \(H_0\), a path joining the endpoints of its positive-slope equality edge must be either a contiguous increasing singleton path, or use the full positive diagonal edge. The former is impossible because the interval is not increasing; the latter requires the relevant prefix and suffix to be increasing and, in particular, forces \(c=a\). A path joining the endpoints of its negative-slope equality edge similarly must use the full negative edge (since the interval is not decreasing); this forces a descending prefix with its first value \(m\) if \(a>1\). The positive-edge route forces the first value \(1\) if \(a>1\), a contradiction. If \(a=1\), the two full-edge routes instead force \(c=1\) and \(d=m\), which makes the interval all of \(\{1,\ldots,m\}\), contrary to properness. Consequently at least one of the two extra equality edges connects different components of \(H_0\). Hence \(T(\pi)\le m^2-2\).

**4. Proper monotone intervals also force a new collapse.** A proper increasing or decreasing common interval of length at least three contains two consecutive length-two common intervals (bonds). For an increasing bond starting at top position \(a\), its ranks are \(c,c+1\). Its *negative* equality edge is
\[
(a-1,c+1)\sim(a+1,c-1).
\]
This cannot lie within a singleton component of \(H_0\). It can be connected through the full negative edge only if \(a+c=m\) and the positions strictly before the bond form a decreasing run of the largest ranks, while those strictly after form a decreasing run of the smallest ranks. Two adjacent increasing bonds have the respective sums of top starts and lower minima differing by two, so at least one of them gives an additional collapse. For decreasing bonds, reverse the lower line: the operation complements all external traces, preserves their number and converts decreasing bonds into increasing ones. This proves the assertion for all proper monotone common intervals of length at least three.

It remains to handle a permutation having a length-two common interval and no longer interval. For an increasing bond, if its negative equality edge is not already connected in \(H_0\), we are done. Otherwise the prefix and suffix have the descending form described above. Since they contain altogether \(m-2\) marked elements, at least one contains two consecutive elements for \(m\ge5\). This creates a decreasing bond at the extreme first or last positions. Its positive equality edge cannot be connected through the full positive edge: for the first two positions, its top start is \(1\) while its lower-rank start is \(m-1\); for the last two, these starts are \(m-1\) and \(1\). Neither equality is possible when \(m\ge4\), so an extra collapse follows. For \(m=4\), the sole residual configuration, with one element on each side of the ascending bond, is the permutation \((4,2,3,1)\); its first three positions form a proper nonmonotone common interval, covered by Step 3. Reflecting the lower order handles decreasing bonds.

If the whole permutation is increasing or decreasing, then the traces are the empty set and all contiguous intervals of the marked order (or their complements). Their number is \(1+m(m+1)/2<m^2-1\) for \(m\ge4\). Every nonsimple permutation therefore has \(T(\pi)\le m^2-2\).

**5. Sharpness of both strata.** Simple permutations exist at each size \(m\ge4\): at even length \(2k\), take \((2,4,\ldots,2k,1,3,\ldots,2k-1)\); at odd length \(2k+1\), take \((2,4,\ldots,2k,1,3,\ldots,2k-3,2k+1,2k-1)\). An internal block within either parity run skips intervening ranks; any boundary-crossing block includes distant ranks, and neither of the two length-\(m-1\) blocks has consecutive ranks. These permutations have no proper common interval, giving the top value.

For \(m\ge5\), prepend a new common minimum, \(\pi=(1,\sigma(1)+1,\ldots,\sigma(m-1)+1)\), where \(\sigma\) is a simple permutation of length \(m-1\). The traces not containing the first marked element are exactly the \(T(\sigma)=(m-1)^2-1\) traces of the tail. Traces containing it are the distinct nonempty/empty prefixes of the upper and lower tail orders, together \(2m-2\) traces, because the two prefix chains intersect only in the empty and full tail sets (simplicity excludes any proper common initial block). Thus
\[
T(\pi)=(m-1)^2-1+2m-2=m^2-2.
\]
For \(m=4\), the nonsimple permutation \((1,3,4,2)\) has exactly \(14=m^2-2\) traces. In each case populate one gap pair per distinct trace to realize the stated count in a finite permutation graph.

## Verification

Run `python3 verify.py` with the accompanying self-contained checker. It independently constructs every cut-pair trace by exact bitmasks, cross-checks the inversion test for all gap pairs through four elements, exhausts all permutations through eight elements, compares the extremal criterion with simplicity, and checks the sharp non-simple second extremum. It also checks explicit constructive permutations through thirty elements. Its successful exit prints `VERIFY_OK`. These finite experiments support but do not substitute for the all-length argument above.

## Relationship to prior work

Foucaud, Mertzios, Naserasr, Parreau and Valicov [2], especially Theorem 13 and Proposition 14, already establish the sharp locating-domination scale for permutation graphs and provide a tight construction from marked paths. In their language, each external trace except the empty trace corresponds to a potentially located vertex. Their result implies the sharp capacity \(m^2-1\) after allowing the empty trace. The existence of simple marked extremizers and the upper capacity are also established in earlier related analysis [4]. Neither assertion by itself proves that **only** simple marked representations attain equality. The new claim is this converse plus the exact sharp loss for non-simple marked permutations; there is no claim to rediscover the 2017 numerical bound, the representation method, or simple permutations.

Berthe, Foucaud, Lehtilä and Parreau [1] motivate the modern parameter-neighborhood viewpoint, with sharp results for treewidth/pathwidth rather than this permutation-representation equality class. Classical simple-permutation theory [3] supplies the definition and existence of simple permutations, not this graph-neighborhood equality criterion. Distinct graph representations can induce different marked permutations; our conclusion is representation-specific, not an isomorphism classification.

## Limitations

This result is about external *open* adjacency profiles on ordinary finite permutation graphs. It does not count vertex-distinct witness realizations beyond one per trace, assert representation uniqueness, or classify minimum ambient graph order. The numeric extremum is pre-existing; only the necessity and sharp nonsimple boundary are proposed as new. An unlocated older equality-case analysis in locating-domination or permutation-pattern literature could still cover the claim, so historical-priority assessment remains provisional. Independent validation has not been performed.

## References

1. G. Berthe, F. Foucaud, T. Lehtilä, A. Parreau, *Neighbourhood complexity and identification problems for graphs of bounded treewidth and pathwidth*, arXiv:2607.16889v1 (2026-07-18), https://arxiv.org/abs/2607.16889 .
2. F. Foucaud, G. B. Mertzios, R. Naserasr, A. Parreau, P. Valicov, *Identification, location-domination and metric dimension on interval and permutation graphs. I. Bounds*, Theoret. Comput. Sci. 668 (2017), 43–58; first publicly posted arXiv:1507.08164v1 (2015-07-29), https://arxiv.org/abs/1507.08164 ; open article: https://perso.limos.fr/ffoucaud/Publications/Papers/J21_ID-interval-permut-1-bounds_TCS_2017.pdf .
3. R. Brignall, *A Survey of Simple Permutations*, in *Permutation Patterns*, Cambridge University Press (2010), https://www.cambridge.org/core/books/abs/permutation-patterns/survey-of-simple-permutations/6685D741BEEE34FB394751B550C9DEDB .
4. *Sharp open-neighborhood trace complexity of permutation graphs*, pre-existing mathematical record, statement and derivation compared for overlap; numerical bound, sufficient simple witnesses and the three-dimensional VC threshold are prior results. The new theorem only adds the converse and the sharp nonsimple boundary.
