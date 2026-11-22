# Fibonacci extremizers for two-colour equivalence extension rank

## Finding

Consider the hereditary class of all finite, possibly empty, equivalence relations with exactly one named unary colour predicate. Each vertex is **red** if it satisfies the predicate, and **blue** otherwise; the two colours are named, not interchangeable. Rank means the one-point-extension rank relative to this entire coloured equivalence class.

**Theorem.** For every integer \(t\geq0\), the minimum size of a finite host \(X\) with \(\operatorname{rk}(X)\geq t\) is exactly
\[
N_t=t(t+1).
\]
At this minimum size the number of *unlabelled colour-preserving isomorphism types* is exactly \(F_{t+2}\), where \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). All the minimum hosts have rank exactly \(t\).

Moreover, every minimum host is obtained uniquely by the following recursive construction, interpreted as a multiset of equivalence-class **colour-count pairs** \((r,b)\):

- The empty host is the sole level-zero host.
- At level one, the two hosts are \(\{(1,1)\}\) and \(\{(1,0),(0,1)\}\).
- At level \(t\geq2\), either append a single class \((t,t)\) to a level-\(t-1\) host, or append the two classes \((t,t-1)\) and \((t-1,t)\) to a level-\(t-2\) host.

The classification is exact. In particular, all minimum hosts have precisely \(t(t+1)/2\) red vertices and the same number of blue vertices, yet only the recursive couplings of the two marginal staircases have full rank. The extremal counts for levels \(0\) through \(5\) are \(1,2,3,5,8,13\).

## Assumptions and scope

Let \(X=(V,E,P)\), where \(V\) is finite and \(E\) is an equivalence relation. A **prime extension** adds one vertex of a specified colour, either to one existing \(E\)-class of the current finite marked substructure or to a wholly new \(E\)-class. For \(F\subseteq X\), define \(\operatorname{rk}_X(F)\geq0\), and recursively define \(\operatorname{rk}_X(F)\geq k+1\) when every prime-extension type of \(F\) has some realization inside \(X\), over the fixed marked vertices, of rank at least \(k\). Put \(\operatorname{rk}(X)=\operatorname{rk}_X(\varnothing)\).

For an \(E\)-class \(C\) meeting \(F\), let \(r_C,b_C\) denote the numbers of unused red and blue vertices of \(C\). Let \(U\) be the induced union of all classes of \(X\) disjoint from \(F\). Empty structures and empty residual parts are allowed. No bound on class sizes or number of classes is assumed.

## Proof

**1. Relative separation lemma.** For every finite \(X\), marked induced \(F\), and integer \(k\geq0\),
\[
\operatorname{rk}_X(F)\geq k
\quad\Longleftrightarrow\quad
\bigl(\forall C\cap F\ne\varnothing:\ r_C\geq k\text{ and }b_C\geq k\bigr)
\quad\text{and}\quad \operatorname{rk}(U)\geq k.
\tag{1}
\]
Proof is by induction on \(k\). It is immediate at \(k=0\). Suppose the statement holds at \(k-1\). If the rank at \(F\) is at least \(k\), a request to append either colour to each specified marked class must be realized with rank at least \(k-1\). Applying the induction hypothesis after that move forces both initial spare colour counts in that class to be at least \(k\). Moreover, for each request to open a fresh class, the realization lies in \(U\); applying induction to the resulting marked position shows its rank inside \(U\) is at least \(k-1\). Hence \(\operatorname{rk}(U)\geq k\).

Conversely, assume the right side of (1). A move inside an existing marked class leaves at least \(k-1\) spare points of *each* colour there, while \(U\) continues to have rank at least \(k-1\). A request for a new class is met using the rank-\(k\) strategy inside \(U\); applying the induction hypothesis within \(U\) gives at least \(k-1\) spare vertices of either colour in the newly marked class and rank at least \(k-1\) in its residual unmarked classes. The original marked classes still have at least \(k-1\) spare points of each colour. In both cases the new full position has rank at least \(k-1\) by induction. Thus (1) holds.

**2. One-colour projection and its sharp staircase.** Restrict to the red vertices (respectively the blue vertices) and forget the predicate. An induction on game depth, using only red (respectively blue) prime-extension requests, shows
\[
\operatorname{rk}(X)\geq t\quad\Longrightarrow\quad
\operatorname{rk}(X_{\mathrm R})\geq t
\quad\text{and}\quad \operatorname{rk}(X_{\mathrm B})\geq t.
\tag{2}
\]
For an ordinary uncoloured equivalence structure with positive class sizes \(\lambda_1\geq\cdots\geq\lambda_s\), the one-colour version of (1), applied at the empty marked set, gives the induction
\[
\operatorname{rk}(Y)\geq t\quad\Longleftrightarrow\quad
s\geq t\ \text{ and }\ \lambda_j\geq t-j+1
\ \text{for all }1\leq j\leq t.
\tag{3}
\]
Indeed, at rank \(t\) the newly opened class must have at least \(t\) vertices, and its removal must leave rank at least \(t-1\); among possible choices, removing the largest class gives a componentwise largest sorted residual vector. Thus the least number of vertices is \(1+\cdots+t=t(t+1)/2\), with equality only for class sizes \(t,t-1,\ldots,1\).

Applying (2) and (3) to each named colour yields
\[
|X|=|X_{\mathrm R}|+|X_{\mathrm B}|\geq t(t+1).
\tag{4}
\]
If equality holds and the two-colour rank is at least \(t\), each colour separately occupies exactly \(t\) equivalence classes, with its respective positive class-size multiset \(\{1,2,\ldots,t\}\). Each \(E\)-class is therefore either a coupling of one red size and one blue size, or a class containing vertices of only one colour. In the latter case its unmatched size occurs nowhere else in that colour.

**3. Peeling the two largest marginal classes.** At \(t=1\), equality in (4) means one red and one blue vertex, either in the same class or in different classes: exactly the two stated types. Now let \(t\geq2\) and suppose a minimum host has rank at least \(t\). Write \(C_{\mathrm R}\) for the unique class with \(t\) red vertices and \(C_{\mathrm B}\) for the unique class with \(t\) blue vertices. On a first move that opens a red class, (1) forces the chosen class to contain at least \(t\) reds and at least \(t-1\) blues. Thus this class must be \(C_{\mathrm R}\). By symmetry a first blue move must choose \(C_{\mathrm B}\), which contains at least \(t-1\) reds.

If \(C_{\mathrm R}=C_{\mathrm B}\), this class has pair \((t,t)\). After the first red move the residual unmarked classes must have rank at least \(t-1\) by (1); they have exactly \(t(t-1)\) elements. Hence the remainder is a minimum host of level \(t-1\).

If \(C_{\mathrm R}\ne C_{\mathrm B}\), uniqueness of each colour's largest size forces their pairs to be exactly \((t,t-1)\) and \((t-1,t)\). After the first red move into \(C_{\mathrm R}\), the free part \(C_{\mathrm B}\cup S\) must have rank at least \(t-1\). A red new-class request in this free part can be realized with rank at least \(t-2\) only in \(C_{\mathrm B}\), because every class of \(S\) has fewer than \(t-1\) reds. The relative separation lemma now forces \(\operatorname{rk}(S)\geq t-2\). It has exactly \((t-1)(t-2)\) vertices, so it is a minimum host of level \(t-2\). No other arrangement is possible.

**4. Both recursive constructions suffice.** If a level-\(t-1\) minimum host has rank at least \(t-1\), adjoining \((t,t)\) realizes either initial colour request and leaves a marked class with at least \(t-1\) spare vertices per colour, plus the rank-\(t-1\) free remainder. Equation (1) gives rank at least \(t\).

If a level-\(t-2\) minimum host \(S\) has rank at least \(t-2\), then the structure \(S\cup\{(t-1,t)\}\) has rank at least \(t-1\): either initial colour request can use the new class and leaves at least \(t-2\) of each colour, with free part \(S\). Symmetrically \(S\cup\{(t,t-1)\}\) has rank at least \(t-1\). Consequently adjoining both \((t,t-1)\) and \((t-1,t)\) to \(S\) gives rank at least \(t\): a first red request uses the former class, and a first blue request the latter, with the required residual rank by (1).

Thus all and only the stated constructions are minimum hosts. Their outermost configuration is uniquely recoverable from the classes containing the largest colour counts, so the branches do not overlap and the count \(a_t\) satisfies
\[
a_0=1,\qquad a_1=2,\qquad a_t=a_{t-1}+a_{t-2}\quad(t\geq2).
\]
Hence \(a_t=F_{t+2}\). Finally (4) with \(t+1\) proves that an order-\(t(t+1)\) host cannot have rank at least \(t+1\); all listed ranks equal \(t\). This completes the proof.

## Verification

The standalone file `verify_colored_equivalence_rank.py` is pure Python and independently implements the defining extension game on sorted class-capacity states, without invoking formula (1) inside the game implementation. Its second implementation checks the separation criterion at 199,704 marked-position/depth comparisons over all 573 isomorphism types of two-coloured equivalence hosts with at most seven vertices. A separate enumeration constructs every possible partial matching of the two forced marginal staircases through level five and compares its game rank against the recursive canonical classification. The number of candidates and surviving extremizers at levels zero through five are \((1,1),(2,2),(7,3),(34,5),(209,8),(1546,13)\). The script finishes with `ALL_CHECKS_OK`.

Reproduce from the directory containing this result and the script using `python3 verify_colored_equivalence_rank.py`. Finite computations do not establish the all-size recurrence; Steps 1–4 supply its proof.

## Relationship to prior work

López-Callejas and Navarro-Castillo's 2026 paper defines this one-point-extension rank and establishes the Rank Property for free-amalgamation classes, tournaments and linear orders, but its investigated examples and results do not state the coloured-equivalence minimum order or Fibonacci extremal census. The simple uncoloured staircase law is only the projection lower bound (4): it does not classify when the red and blue staircases coexist compatibly. For example, at level three the marginal pairings \(\{(3,3),(2,2),(1,1)\}\) and \(\{(3,1),(2,2),(1,3)\}\) both have the same three-by-three marginal staircases, but only the former achieves rank three.

Two publicly available 2026 studies on finite equivalence relations with one unary predicate classify **ordinary first-order rank-two sentence theories** (207 theories, sharp 13-element logical representative bound). Their full results use two-round Ehrenfeucht–Fraïssé *comparison of two structures*, not the one-host, every-prime-extension rank game, and provide no all-level Fibonacci extremal description. Standard guarded-fragment and quantifier-rank classifications must not be identified with the rank considered here.

## Limitations

The statement is restricted to **finite** structures, one equivalence relation and exactly two **named** colours with one exhaustive unary predicate. It does not give the full rank of every nonminimal coloured host, transfinite ranks of countable hosts, or an analogue for three or more named colours. Historical priority against unindexed literature is provisional. Independent mathematical validation has not been performed.

## References

1. C. López-Callejas and J. Navarro-Castillo, *A rank function for Fraïssé classes and the rank property*, arXiv:2604.14461, first public 2026-04-15; sections 2–6. https://arxiv.org/html/2604.14461v1
2. *A sharp thirteen-element rank-two model bound for unary-coloured equivalence relations*, publicly available mathematical result, 2026-10-18. https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-a-sharp-thirteen-element-rank-two-model-bound-for-unary-coloured--e2acfc789698/RESULT.md
3. *Two-round theories of finite two-coloured equivalence structures*, publicly available mathematical result, 2026-10-25. https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-two-round-theories-of-finite-two-coloured-equivalence-structures--42cafa4a9c35/RESULT.md
