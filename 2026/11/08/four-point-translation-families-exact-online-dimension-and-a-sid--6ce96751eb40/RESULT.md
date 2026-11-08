# Four-point translation families: exact online dimension and a Sidon boundary

## Finding

Let \(G\) be a finite abelian group of order \(N\ge8\) and let \(A\subset G\) have exactly four elements. Write \(\mathcal T(A)=\{A+g:g\in G\}\) for the membership concept class on \(G\), identifying equal translates. Put
\[
H_A=\{g\in G:A+g=A\},\quad h=|H_A|,\quad r_A(t)=|A\cap(A+t)|.
\]
The complete Littlestone-dimension classification is
\[
\boxed{\operatorname{Ldim}(\mathcal T(A))=
\begin{cases}
1,&h=4,\\
3,&h=1\text{ and }r_A(t)=2\text{ for some }t\ne0,\\
2,&\text{otherwise}.
\end{cases}}
\]
For prime \(p\ge11\), every four-point subset of \(\mathbb Z/p\mathbb Z\) is aperiodic, and the formula becomes the sharp Sidon dichotomy: the online dimension is \(2\) exactly when its twelve ordered nonzero differences are pairwise distinct, and is \(3\) otherwise. At \(p=11\), all \(330\) four-point subsets have dimension \(3\); at \(p=13\), exactly \(52\) of the \(715\) subsets have dimension \(2\), and the other \(663\) have dimension \(3\). Thus \(13\) is the smallest prime admitting the four-point Sidon obstruction.

In \(\mathbb Z/13\mathbb Z\), the Sidon support \(\{0,1,3,9\}\) has VC dimension \(2\) and Littlestone dimension \(2\), whereas the consecutive support \(\{0,1,2,3\}\) has the same VC dimension \(2\) but Littlestone dimension \(3\). These examples demonstrate a static/adaptive separation within four-point translation classes, not a new result about the online dimension of consecutive windows.

## Assumptions and scope

The group is finite, abelian, of order at least eight, with additive notation; the seed has cardinality exactly four. The membership label on input \(x\in G\) for a hypothesis \(A+g\) is one precisely when \(x\in A+g\). The Littlestone dimension is the maximum integer \(d\) for which a full binary decision tree of depth \(d\) can be labeled by points of \(G\), with every binary root-to-leaf path realized by a distinct hypothesis. Repeated translates count once. The stabilizer size divides four, so \(h\in\{1,2,4\}\). All quantified dimensions are exact, not finite approximations.

## Proof

**Translate orbit and root populations.** Orbit–stabilizer gives \(|\mathcal T(A)|=N/h\). For any fixed point \(x\in G\), the number of distinct translating concepts containing \(x\) is exactly \(4/h\), because there are exactly four shifts \(g=x-a\) with \(a\in A\), each orbit concept occurring \(h\) times. The number avoiding \(x\) is \((N-4)/h\).

**Global upper bound.** A full depth-three tree requires at least four distinct hypotheses under either outcome of its root query. Therefore its root's positive branch requires \(4/h\ge4\), so \(h=1\). In that case a depth-three tree rooted at \(x\) requires a depth-two subtree within its positive branch of four hypotheses. Any query \(y\) at that branch's next node must split those four hypotheses into two and two. The number of hypotheses containing both \(x\) and \(y\) is \(r_A(y-x)\); hence some nonzero \(t=y-x\) must satisfy \(r_A(t)=2\). A depth-four tree is impossible even with \(h=1\), since its positive root branch would require at least eight hypotheses and always contains only four. Thus the stated condition for dimension three is necessary, and dimension is universally at most three.

**Constructive lower bounds.** If \(h=1\) and \(r_A(t)=2\), take a root query \(x\) and use the same second-level query \(y=x+t\) on both branches. The four sets of concepts having label pairs \((1,1),(1,0),(0,1),(0,0)\) have respective cardinalities \(2,2,2,N-6\). Since \(N\ge8\), each set contains at least two distinct hypotheses. Two distinct Boolean membership concepts disagree on some query point, so each of these four version spaces supports a final split. This explicitly builds a complete depth-three decision tree.

If \(h\in\{1,2\}\), each root branch contains at least two distinct hypotheses because \(4/h\ge2\) and \((N-4)/h\ge2\). In either branch choose two different translates and a point where they disagree. This builds a complete depth-two tree. If \(h=4\), the root's positive branch always has just one distinct hypothesis, so depth two is impossible. Since \(N\ge8\), there are at least two different cosets of the four-element subgroup \(A-A\), so dimension one is attained. These constructions prove the complete classification.

**Prime-order Sidon boundary.** If \(G=\mathbb Z/p\mathbb Z\) for prime \(p\ge11\), then \(h=1\). A four-set is Sidon precisely when \(r_A(t)\le1\) for every \(t\ne0\); this is equivalent to all twelve ordered off-diagonal differences being distinct. If the Sidon condition fails, then some \(r_A(t)\ge2\). If equality holds the theorem gives dimension three. If \(r_A(t)=3\), the directed edges \(a\to a+t\) among the four elements make a length-three path: since the additive order of \(t\) is \(p\ge11\), there can be no shorter cycle. Its two length-two subpaths show \(r_A(2t)\ge2\); with only four vertices, they are exactly the two such ordered pairs, so \(r_A(2t)=2\). Thus every non-Sidon seed has dimension three. Conversely a Sidon seed has no lag with intersection two and therefore has dimension two.

There are at most \(p-1\) possible nonzero ordered differences, while a four-set has twelve, so \(p\ge13\) is necessary for a four-point Sidon set. The set \(\{0,1,3,9\}\subseteq\mathbb Z/13\mathbb Z\) realizes every nonzero difference once, proving attainability at \(p=13\).

**Exact count at thirteen.** Each four-point Sidon seed in \(\mathbb Z/13\mathbb Z\) is a \((13,4,1)\) difference set, so there is a unique ordered pair \((u,v)\) with \(v-u=1\). Translating by \(-u\) uniquely normalizes the seed to \(\{0,1,a,b\}\), \(2\le a<b\le12\). Comparing the twelve ordered differences for these \(\binom{11}{2}=55\) possibilities leaves precisely four normalized sets:
\[
\{0,1,3,9\},\quad\{0,1,4,6\},\quad
\{0,1,5,11\},\quad\{0,1,8,10\}.
\]
The finite list is exhaustively rechecked by the standalone exact verifier. Each normalized set has thirteen distinct translates; uniqueness of the normalized difference-one pair prevents cross-counting. Hence there are exactly \(4\cdot13=52\) Sidon four-sets and \(\binom{13}{4}-52=663\) nonsidon four-sets.

**Equal static dimension, different adaptive dimension.** For the Sidon seed, two points are shattered because their four joint label-pattern counts are \((1,3,3,6)\). No triple is shattered: the traces \(111\) and \(110\) on any shattered triple would force two distinct translates containing the same pair, contradicting that every pair of translates intersects in at most one point. For the consecutive four-point seed, the known cyclic-interval VC dimension is two (it can also be verified directly by examining the endpoint changes of its translates); its ordered difference \(t=2\) has \(r_A(2)=2\), giving online dimension three. Thus the two classes both have VC dimension two.

## Verification

The included standalone `verify_four_translate_online.py` enumerates all four-subsets in every cyclic group of orders eight through sixteen, as well as five noncyclic abelian groups, directly constructs their distinct translate hypotheses, and computes online dimension by the exact recursive full-tree predicate. It compares these independently computed dimensions with the theorem for every seed, including stabilizer cases. It also verifies the four normalized difference sets, the precise \(52/663\) split at thirteen and the equal-VC/different-online example. The program uses only the Python standard library. Run `python verify_four_translate_online.py`; expected complete output is included in `checks_output.txt`.

## Relationship to prior work

The Littlestone dimension is also called online or thicket dimension and is closely related to Shelah's 2-rank; see Chase and Freitag (2018) for this connection and the general theory. General results about online learning and Littlestone dimension do not themselves produce the present exact four-point translate autocorrelation criterion. The relation between Sidon sets and distinct differences is classical, as is the \((13,4,1)\) cyclic difference set. The current assertion is specifically the exact classification of the **online** dimension for **all** four-point translates on finite abelian groups, including the stabilizer and repeated-difference distinctions. An existing exact cyclic-window online-dimension formula covers the consecutive-window comparison and is not claimed as new. Fourier moment studies of cyclic four-sets depend on repeated differences but measure other invariants; no implication of the online classification was identified in the inspected material.

## Limitations

The theorem assumes exactly four seed elements and group order at least eight; it makes no assertion for larger supports or arbitrary nontranslation classes. For composite-order groups, non-Sidon does not always imply online dimension three: for example, \(A=\{0,1,3,6\}\subseteq\mathbb Z/9\mathbb Z\) has intersections of size three at lags three and six, but never two; its online dimension is two. The four-set prime-order dichotomy is therefore not a substitute for the general exact-intersection condition. The computational checks corroborate the universal mathematical proof but are not independent certification. Historical priority under alternative terminology, especially shift or difference-set classes, remains uncertain.

## References

- Hunter Chase and James Freitag, *Model Theory and Machine Learning*, arXiv:1801.06566, first submitted January 19, 2018. Defines and compares Littlestone/thicket dimension and model-theoretic rank.
- Noga Alon, Roi Livni, Maryanthe Malliaris, and Shay Moran, *Private PAC learning implies finite Littlestone dimension*, arXiv:1806.00949, first submitted June 4, 2018. General online-dimension theory.
- Mark Bun, Roi Livni, and Shay Moran, *An Equivalence Between Private Classification and Online Prediction*, arXiv:2003.00563, first submitted March 1, 2020. Generic online-learning and finite hypothesis-class bounds.
- Classical Singer difference-set construction, for the \((13,4,1)\) perfect cyclic difference-set context; the finite enumeration here is proved directly.
