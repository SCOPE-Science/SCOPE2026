# Signed pentads and frozen metric-basis slides in the five-dimensional hypercube

## Finding

Let \(Q_5\) be the binary five-dimensional hypercube with labelled vertices \(\{0,1\}^5\), Hamming distance \(d_H\), and adjacency at Hamming distance one. A *metric basis* is a smallest vertex set whose distances distinguish every two vertices. One *jump* replaces a single chosen landmark with any unchosen vertex, provided the new set is again a metric basis. One *slide* is such a jump constrained to an edge of \(Q_5\).

**Theorem.** Every metric basis has four vertices. Let \(\overline{x}=x\oplus(1,1,1,1,1)\) be the antipode and let \(\pi(x)\) be the unique even-parity member of \(\{x,\overline x\}\). There are exactly sixteen five-element sets (called *pentads*) of even-parity vectors in which every two distinct members have Hamming distance two. A four-vertex set \(S\) is a metric basis of \(Q_5\) if and only if \(\pi\) is injective on \(S\) and \(\pi(S)\) consists of four members of precisely one pentad. Every choice of the four antipodal representatives is allowed. Consequently there are exactly \(16\binom54 2^4=1280\) metric bases.

The jump graph of these bases is the disjoint union of sixteen isomorphic, connected, twelve-regular, eighty-vertex graphs. In each component, label a configuration by a missing position \(a\in\{1,2,3,4,5\}\) and a sign for each of the other four positions. Adjacent states either flip one occupied sign, or change the missing position to an occupied position while freely choosing the sign at the newly occupied position. For two such states \(U,V\), with missing positions \(a,b\), the exact distance is

\[
 d_J(U,V)=\mathbf1_{a\ne b}+\bigl|\{i\notin\{a,b\}:\epsilon_U(i)\ne\epsilon_V(i)\}\bigr|.
\]

Each component has 480 edges and both radius and diameter four. From every state, the numbers at respective distances zero through four are \((1,12,30,28,9)\). The entire jump graph has 7,680 edges. **The slide graph has no edges:** each of the 1,280 optimum configurations is isolated under a single adjacency-constrained landmark move.

## Assumptions and scope

All vertices are distinctly labelled binary vectors; no quotient by graph automorphisms is taken when counting bases or edges. Distance resolution is the *ordinary vertex-metric* criterion: for all distinct \(u,v\in\{0,1\}^5\), at least one landmark \(w\) must satisfy \(d_H(u,w)\ne d_H(v,w)\). The two reconfiguration graphs have exactly the minimum bases as vertices; each allowable replacement counts once as an undirected edge. The theorem is specific to dimension five. No conclusion is asserted about other dimensions, nonminimum resolving sets, or simultaneous multi-landmark moves.

## Proof

### 1. Resolving sets and ternary kernels

For \(u,v,w\in\{0,1\}^5\), direct coordinate expansion gives

\[
 d_H(u,w)-d_H(v,w)=\sum_{i=1}^5(u_i-v_i)(1-2w_i).
\]

Write \(r(w)=(1-2w_1,\ldots,1-2w_5)\) and let \(R(S)\) be the matrix with rows \(r(w)\), \(w\in S\). Every vector \(\delta\in\{-1,0,1\}^5\) occurs as \(u-v\) for some binary \(u,v\). Hence \(S\) is resolving if and only if there is **no nonzero** \(\delta\in\{-1,0,1\}^5\) satisfying \(R(S)\delta=0\). This uses the ternary restriction, not merely the real rank of \(R(S)\).

If \(|S|\le3\), the five columns of \(R(S)\) lie in \(\{\pm1\}^{|S|}\). There are at most \(2^{|S|-1}\le4\) distinct columns up to global negation. Thus two columns are equal or negatives, producing a kernel vector \(e_i-e_j\) or \(e_i+e_j\), respectively. No set of at most three landmarks resolves \(Q_5\).

Antipodal replacement changes one row of \(R(S)\) by its negative and therefore leaves resolvability unchanged. A four-vertex resolving set cannot use two antipodal landmarks: deleting one would retain all conditions, contradicting the lower bound. Every four-element basis consequently has four distinct antipodal classes, represented uniquely by four even-parity words.

### 2. Classification of the even-parity four-sets

Consider four even-parity landmarks, and translate all of them by XOR with the first landmark, a parity-preserving graph automorphism. It now suffices to analyze \(S=\{0,p,q,t\}\), where \(p,q,t\) have even nonzero weight. Suppose some pair has Hamming distance four. Translate one of that pair to zero and permute coordinates so the other is \(11110\). A ternary vector orthogonal to these two sign rows necessarily satisfies \(\delta_5=0\) and \(\delta_1+\cdots+\delta_4=0\). For the two other rows, assign to each of the first four coordinates its pair of binary entries, a signature in \(\{0,1\}^2\). If two coordinates have the same signature, their difference vector is a nonzero ternary kernel vector. Otherwise the four signatures are all four corners of the binary square; assigning alternating signs \(+1,-1,-1,+1\) around its corners again gives a nonzero ternary kernel vector. Thus **any two even representatives in a resolving four-set have Hamming distance two**.

Since \(p,q,t\) are now distinct vectors of weight two, pairwise distance two is equivalent to their three supports being pairwise-intersecting two-element subsets of \(\{1,2,3,4,5\}\). These supports either form a triangle (three edges of a three-vertex complete graph) or a three-edge star (three edges incident to one common coordinate). In the triangle case the three support-coordinate entries of a kernel vector must vanish, but the other two coordinates can receive \(+1\) and \(-1\); the set is not resolving.

In the star case rename the center \(i\), its three selected leaves \(j,k,\ell\), and the remaining coordinate \(m\). Orthogonality yields

\[
 \sum_h\delta_h=0,\qquad \delta_i+\delta_j=\delta_i+\delta_k=\delta_i+\delta_\ell=0.
\]

Consequently \(\delta_m=2\delta_i\). Because both entries are ternary, \(\delta_i=\delta_m=0\), forcing the other three entries to be zero. The four-set resolves. This proves that every normalized even-parity resolving four-set is exactly \(\{0,e_i+e_j,e_i+e_k,e_i+e_\ell\}\) for distinct leaves \(j,k,\ell\) and an unused fifth-coordinate leaf \(m\).

### 3. Unique five-member completion

The star extends uniquely by adding \(e_i+e_m\), giving five even-parity points all mutually at distance two. Undoing the translation gives the pentad attached to the resolving four-set. Conversely, any four members of such a pentad form a resolving four-set by the star argument. Three members determine their pentad uniquely: after translating one of the three to zero, the other two corresponding edges have a unique common coordinate, because they are distinct intersecting two-subsets. The only five-member extension has the four pairs incident to that coordinate. Hence distinct pentads cannot share three members.

Explicitly, all pentads have the form

\[
 P(c,i)=\{c\}\cup\{c\oplus e_i\oplus e_j:j\ne i\},
 \qquad c\in\{0,1\}^5\text{ even},\quad 1\le i\le5.
\]

There are \(16\cdot5\) presentations; every pentad has exactly five presentations, one centered at each member, so there are sixteen distinct pentads. Each contributes \(\binom54=5\) projected four-sets, and uniqueness prevents overlap. Independently choosing either antipodal representative in each selected class gives \(2^4\) lifts of each projected set; no other four-set can resolve. Thus \(16\cdot5\cdot16=1280\) metric bases.

### 4. Exchange and sliding geometry

A one-landmark replacement preserves three of the original four antipodal classes. If it changes the set of projected classes, both old and new four-sets belong to pentads having at least three common members. The uniqueness just proved forces those pentads to be equal. If it only changes an antipodal sign, the pentad plainly stays unchanged. Therefore a pentad is invariant under every legal jump, giving at least sixteen components.

Within a fixed pentad, a basis specifies the one omitted class and four independent antipodal signs. Flipping one occupied sign gives four legal jumps. Alternatively, replacing any one of the four occupied classes with either sign of the one omitted class gives eight more. All twelve jumps are distinct, and each preserves a basis. These moves connect the eighty states within that pentad, giving exactly sixteen components and \(16\cdot80\cdot12/2=7680\) undirected jump edges.

For any two states in the same pentad, each disagreeing sign at a class occupied in both states requires at least one move changing that coordinate, and different omitted positions require at least one change of support. Thus the displayed distance formula is a lower bound. It is attained by first flipping exactly the disagreeing shared signs and, when necessary, performing one exchange between the differently omitted positions with the required incoming sign. If the omitted positions coincide, the distance profile is the four-dimensional Hamming binomial profile \((1,4,6,4,1)\). If they differ, there are four possible new missing positions, two choices of the previously unoccupied sign, and three shared sign coordinates, producing additions \((0,8,24,24,8)\) across distances zero to four. The total is \((1,12,30,28,9)\), with radius and diameter four and 480 component edges.

Finally, two representatives of distinct pentad classes have Hamming distance either two or three, because their even representatives have distance two and taking one antipode changes distance to \(5-2=3\). The two representatives of the same class are antipodal, at distance five. Every possible legal jump therefore has underlying Hamming distance two, three, or five, **never one**. Hence there are no legal token slides.

## Verification

The package contains two independently implemented, runnable Python 3 programs using only the standard library. Run `python3 code/check_direct.py` and `python3 code/check_quotient.py`; their deterministic JSON output agrees with `data/check_direct.json` and `data/check_quotient.json`, respectively.

The direct program tests every \(\binom{32}{3}=4960\) triple and every \(\binom{32}{4}=35960\) four-subset against all \(\binom{32}{2}=496\) vertex-pair distance inequalities. It constructs all 1280 bases and every one-landmark jump and slide, independently computes all 16 components, and performs breadth-first shortest-path searches from every vertex in every component. The quotient program separately tests the ternary-kernel criterion on all 1820 even-representative four-sets against 242 nonzero ternary vectors, enumerates the 16 pentads and their unique completions, constructs all 1280 antipodal lifts, and checks the complete signed-state distance distribution. Both programs assert all central enumerations and formulas. They are finite cross-checks; the arguments above establish the structural result without relying on a bounded search for an infinite claim.

## Relationship to prior work

Laird, Tillquist, Becker and Lladser (2019, Section 2) characterize Hamming-graph resolvability by constrained linear systems, supplying a natural methodological foundation and the guiding primary source. Kelenc, Toshi, Škrekovski and Yero (2021, Lemma 5) explicitly proved that replacing a hypercube landmark by its antipode preserves resolving sets; this invariance is therefore **not claimed as new**. Historical research also provides the metric dimension of small hypercubes and symmetry reductions.

A pre-existing exact classification of metric bases of the **five-regular Clebsch graph** identifies eighty four-element bases, each four of the five neighbors of a vertex, with reconfiguration graph \(16K_5\). This is precisely the sixteen-pentad geometry of the projected four-sets when the folded quotient is described on even binary words with distance-four adjacency. The eighty projected sets and their sixteen pentads are **not independently asserted as a new Clebsch result**. The claim here is the nontrivial equivalence between these projected sets and the four-landmark resolving condition **on the 32-vertex cube itself**, together with all sixteen antipodal lifts per projected set, the full 1280-state signed jump graph, its exact distances, and the slide-frozen phenomenon. Clebsch reconfiguration alone neither counts the signed lifts as hypercube metric bases nor determines which one-landmark moves between their sign assignments are allowed.

A separate previous computation for ordinary metric bases of \(Q_4\) gives 928 optimal configurations and a *connected* token-slide graph with diameter ten. The present theorem gives an exact contrasting case: in dimension five no optimal token slides exist. Prior work on zero-forcing reconfiguration defines a related general exchange framework, but is a different feasibility condition. These distinctions concern statements and implications, not merely titles.

## Limitations

The theorem concerns ordinary metric resolving bases of the single finite graph \(Q_5\), not arbitrary hypercubes or all resolving subsets. No independent external audit has been performed. Priority cannot be guaranteed against unindexed historical research or inaccessible full-text papers; in particular, the full text of the hypercube-symmetry article by Nikolić, Čangalović and Grujičić was not accessible, although its publicly available abstract describes heuristics and upper bounds rather than optimum reconfiguration. The established antipodal-invariance lemma and the earlier Clebsch projected classification are not new contributions. The verification programs independently check the finite theorem but are not formal proof assistants.

## References

1. L. Laird, R. C. Tillquist, S. Becker, and M. E. Lladser, *Resolvability of Hamming Graphs*, arXiv:1907.05974v1, first public 2019-07-12, https://arxiv.org/pdf/1907.05974.
2. A. Kelenc, A. T. M. Toshi, R. Škrekovski, and I. G. Yero, *On Metric Dimensions of Hypercubes*, arXiv:2102.10916v1, first public 2021-02-22, https://arxiv.org/pdf/2102.10916.
3. N. Nikolić, M. Čangalović, and I. Grujičić, *Symmetry properties of resolving sets and metric bases in hypercubes*, *Optimization Letters* 11 (2017), 1057–1067, DOI 10.1007/s11590-014-0790-2, repository metadata https://rfos.fon.bg.ac.rs/handle/123456789/1688 (full text restricted).
4. J. Geneson, R. Haas, and L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220v1, first public 2020-09-01, https://arxiv.org/pdf/2009.00220 (related but different invariant).
5. A. Hertz, *An IP-based swapping algorithm for the metric dimension and minimal doubly resolving set problems in hypercubes*, *Optimization Letters*, DOI 10.1007/s11590-017-1184-z (metric optimization, not an exact optimum-preserving reconfiguration census).
