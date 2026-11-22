# Bipartite condensation and the first odd-cycle defect in Henson tuple types

## Finding
Let \(\mathcal H_3\) be the countable universal homogeneous triangle-free graph. For each integer \(n\ge1\), pointwise name an induced complete bipartite parameter graph \(K_{n,n}\). Fix an integer \(r\ge1\), and choose uniformly from all complete types of ordered, pairwise distinct \(r\)-tuples of new vertices, none equal to a parameter. Write \(G_{n,r}\) for the graph induced on the \(r\) labelled new vertices. For any graph \(F\) on \([r]\), let \(N_{n,r}(F)\) be the number of these types with induced new graph exactly \(F\), and put \(T_{n,r}=\sum_F N_{n,r}(F)\).

**Fixed-arity condensation theorem.** For every fixed \(r\), uniformly over labelled graphs \(F\) on \([r]\),
\[
N_{n,r}(F)=\chi_F(2)\,2^{rn}+O_r\!\left((3\cdot2^{r-2})^n\right),
\]
where \(\chi_F(2)\) is the number of proper two-colourings of \(F\); when \(F\) contains a triangle both sides are interpreted as zero. Consequently
\[
T_{n,r}=\Theta_r\,2^{rn}+O_r\!\left((3\cdot2^{r-2})^n\right),\qquad
\Theta_r=\sum_{j=0}^{r}\binom rj 2^{j(r-j)},
\]
and \(G_{n,r}\) converges in total variation, at rate \(O_r((3/4)^n)\), to the probability law
\[
\Pr(G_r=F)=\frac{\chi_F(2)}{\Theta_r}.
\]
Equivalently, draw a two-colouring \(\sigma\) of \([r]\) with probability proportional to \(2^{a(r-a)}\), where \(a\) is the number of vertices of the first colour, and then include each cross-colour edge independently with probability \(1/2\). Thus the limit is bipartite even though \(\mathcal H_3\) itself has induced odd cycles.

**Universal sharp odd-cycle rarity.** For every fixed \(r\), define the finite integer
\[
A_r=\sum_{\substack{F\text{ labelled triangle-free}\\F\text{ non-bipartite}}}
\#\{\sigma:[r]\to\{A,B\}:\text{exactly one edge of }F\text{ is monochromatic}\}.
\]
The probability of a non-bipartite induced new graph has the *sharp all-arity* expansion
\[
\Pr(G_{n,r}\text{ is non-bipartite})
=\frac{A_r}{\Theta_r}\left(\frac34\right)^n
+O_r\!\left((5/8)^n\right).
\]
Here \(A_r=0\) and the probability is exactly zero for \(r\le4\); for every \(r\ge5\), \(A_r>0\). For example \(A_5=120\), \(A_6=6120\), and \(A_6/\Theta_6=340/1017\). The exponential base \(3/4\) is therefore optimal at every fixed arity at which odd cycles are possible.

**Sharp first odd-cycle event.** At arity five the only non-bipartite triangle-free new graph is a five-cycle. Its exact probability obeys
\[
\Pr(G_{n,5}\cong C_5)=\frac{60}{721}\left(\frac34\right)^n
\left(1+O\!\left((3/4)^n\right)\right).
\]
For one *fixed* labelled five-cycle \(F\), the number of types is
\[
\begin{aligned}
N_{n,5}(F)={}&10\cdot24^n+10\cdot15^n-30\cdot12^n+2\cdot11^n
-20\cdot10^n-10\cdot9^n\\
&+20\cdot8^n+40\cdot6^n+10\cdot5^n-30\cdot4^n
-10\cdot3^n+10\cdot2^n-1.
\end{aligned}
\]
In particular \(N_{n,5}(F)=10\cdot24^n+O(15^n)\).

**Conditional one-defect geometry.** Conditional on \(G_{n,5}=F\), let \(D_i\) count named-base neighbours of new vertex \(i\). As \(n\to\infty\), the vector \((D_1/n,\ldots,D_5/n)\) converges in distribution to the uniform distribution on five vectors indexed by the five edges \(e\) of \(F\): the two endpoints of \(e\) have coordinate \(1/3\), and the other three coordinates equal \(1/2\). Thus precisely one uniformly random cycle edge is the asymptotic low-neighbourhood pair.

## Assumptions and scope
The base vertices are individually named, so tuple types distinguish their adjacency patterns to each old vertex. The two base shores both have exactly \(n\) vertices. The \(r\) new coordinates are ordered and required pairwise distinct and distinct from the base. Only first-order complete types in the graph language are counted, not arbitrary non-complete formulas. All limits are for \(n\to\infty\) with \(r\) fixed. The theorem makes no uniform assertion when \(r\) grows with \(n\).

For a finite graph \(Q\), write \(I(Q)\) for the number of independent vertex subsets, including the empty subset. Set \(I(\varnothing)=1\). Write \([r]=\{1,\ldots,r\}\).

## Proof
**1. Types and neighbourhoods.** Quantifier elimination and homogeneity of \(\mathcal H_3\) identify each prescribed injective tuple type with its finite triangle-free diagram over the named base. An individual new vertex has a neighbourhood that is an independent subset of \(K_{n,n}\), hence is either empty or is contained uniquely in one shore. For a fixed triangle-free internal new graph \(F\), the chosen neighbourhoods \(S_i\) satisfy exactly the additional restrictions \(S_i\cap S_j=\varnothing\) for every edge \(ij\in E(F)\). Conversely these conditions preclude all triangles, so the finite extension is realized. If \(F\) contains a triangle, no type is realizable.

**2. Auxiliary shore assignments.** Temporarily give each new coordinate one of two shore labels \(\sigma:[r]\to\{A,B\}\), even if its chosen old neighbourhood is empty. For fixed \(\sigma\), put \(X=\sigma^{-1}(A)\), \(Y=\sigma^{-1}(B)\). For each of the \(n\) old vertices in shore \(A\), the subset of new vertices adjacent to it must be an independent subset of \(F[X]\). Choices at distinct old vertices are independent. The analogous statement holds for shore \(B\). Hence the number of decorated extensions is exactly
\[
B_F(\sigma)^n,\qquad B_F(\sigma)=I(F[X])I(F[Y]).
\]
If a genuine type has \(z\) new coordinates with no old neighbours, it is counted \(2^z\) times in the decorated sum and otherwise once. Since any one new coordinate has at most \(2^{n+1}-1\) admissible old neighbourhoods, for fixed \(r\),
\[
0\le\sum_{\sigma}B_F(\sigma)^n-N_{n,r}(F)
\le (2^r-1)r(2^{n+1}-1)^{r-1}
=O_r(2^{(r-1)n}).
\]
This bound remains valid after imposing all internal-edge constraints.

**3. Leading terms.** If \(\sigma\) is a proper two-colouring of \(F\), its two induced same-colour graphs are edgeless, so \(B_F(\sigma)=2^r\). If \(\sigma\) is not proper, one colour class contains an edge, and the independent subsets of that class omit at least one quarter of all subsets. Thus \(B_F(\sigma)\le3\cdot2^{r-2}\). Summing the finitely many decorated assignments and using \(2^{r-1}\le3\cdot2^{r-2}\) for \(r\ge2\) gives the stated uniform error. The case \(r=1\) follows directly from \(N_{n,1}(F)=2^{n+1}-1\), with constant error. Proper colourings do not exist when \(F\) is non-bipartite.

Summing \(\chi_F(2)\) over all labelled graphs \(F\) on \([r]\), one may choose a two-colouring having shore sizes \(j,r-j\) and any subset of its \(j(r-j)\) cross edges. Therefore
\[
\sum_F\chi_F(2)=\sum_{j=0}^{r}\binom rj 2^{j(r-j)}=\Theta_r.
\]
As there are finitely many graphs at fixed \(r\), the asserted total-variation rate and the generative description follow.

**4. A sharp general odd-cycle expansion.** Fix a triangle-free non-bipartite internal graph \(F\). Every two-shore assignment has at least one monochromatic internal edge. If exactly one edge is monochromatic, its assignment weight is \(3\cdot2^{r-2}\) because only one pair is forbidden to be selected simultaneously at any old vertex. If there are two or more monochromatic edges, choose two of them. If they share a vertex, at most five of eight subsets of their three vertices are independent, giving weight at most \((5/8)2^r\); if they are disjoint, at most nine of sixteen subsets of four vertices are independent, giving the even smaller \((9/16)2^r\). These statements remain true when the two edges belong to different shore classes. Using the empty-neighbourhood correction from Step 2 (whose base \(2^{r-1}\) is smaller than \((5/8)2^r\)), we obtain
\[
N_{n,r}(F)=a(F)(3\cdot2^{r-2})^n
+O_r\!\left((5\cdot2^{r-3})^n\right),
\]
where \(a(F)\) counts shore assignments having exactly one monochromatic edge. Sum over all labelled triangle-free non-bipartite \(F\) and divide by \(T_{n,r}\). The denominator has relative error \(O_r((3/4)^n)\), whose effect on the leading rare term is \(O_r((9/16)^n)\), smaller than \(O_r((5/8)^n)\). This proves the universal rarity formula. A five-cycle together with \(r-5\) isolated new vertices has a one-defect shore assignment, so \(A_r>0\) for every \(r\ge5\). The first two constants can also be counted structurally. For five labels there are twelve pentagons, each with ten one-defect colourings, giving \(A_5=120\). On six labels every triangle-free non-bipartite graph is a pentagon plus one vertex with zero, one, or two neighbours on it (two neighbours must be nonconsecutive). These give respectively \(72\), \(360\), and \(180\) labelled graphs; graphs in the last case contain two pentagons and so are counted twice before the division. Their one-defect colourings number respectively \(20\), \(10\), and \(6\), hence \(A_6=72\cdot20+360\cdot10+180\cdot6=6120\). The finite classification is independently enumerated by `verify.py`.

**5. The exceptional five-cycle.** A triangle-free non-bipartite graph on exactly five vertices must be a cycle \(C_5\). There are \(5!/10=12\) such labelled graphs. For any fixed one, direct enumeration of its \(32\) shore assignments by \(B_F(\sigma)\) gives exactly ten values of \(24\), ten of \(16\), ten of \(15\), and two of \(11\). The ten highest assignments are precisely the two-shore assignments with *exactly one* monochromatic cycle edge; each of the five edges has two such assignments. The undecorated correction in Step 2 is \(O(16^n)\) when \(r=5\). Consequently \(N_{n,5}(F)=10\cdot24^n+O(16^n)\). At \(r=5\), the normalization from Step 3 is \(\Theta_5=1442\). Therefore
\[
\frac{12N_{n,5}(F)}{T_{n,5}}
=\frac{120}{1442}\left(\frac{24}{32}\right)^n
\left(1+O((3/4)^n)\right),
\]
which gives the claimed constant.

For completeness, the exact exponential polynomial stated in the Finding follows from an integer inclusion-exclusion identity, not from extrapolation of sampled values. For disjoint \(X,Y\subseteq[5]\), let
\[
Q_n(X)=\sum_{Z\subseteq X}(-1)^{|X|-|Z|}I(F[Z])^n.
\]
This counts the choices of independent subsets at every old vertex of one shore for which *every* new label in \(X\) receives at least one old neighbour. Assign each nonempty new neighbourhood to its unique shore and leave other new coordinates unassigned. It follows exactly that
\[
N_{n,5}(F)=\sum_{X\cap Y=\varnothing}Q_n(X)Q_n(Y).
\]
Expand this finite sum and collect the coefficients of \(b^n\) for each distinct integer base \(b=I(F[Z])I(F[W])\). The nonzero coefficient pairs \((b,c_b)\), in ascending base order, are
\[
(1,-1),(2,10),(3,-10),(4,-30),(5,10),(6,40),(8,20),(9,-10),
(10,-20),(11,2),(12,-30),(15,10),(24,10).
\]
This recovers the displayed identity for every \(n\ge0\), including the \(O(15^n)\) remainder.

**6. Conditional neighbourhood densities.** A uniformly sampled type with internal graph \(F=C_5\) has, with probability tending to one, all five old neighbourhoods nonempty and one of the ten maximum-weight assignments from Step 5. By cycle symmetry, the ten assignments have asymptotically equal probability, leaving a uniformly chosen exceptional cycle edge. Under a fixed maximum assignment, one colour class induces exactly one edge and one isolated vertex, while the other induces two isolated vertices. At each named old vertex of the first shore, the two endpoints of that edge occur as neighbours with marginal probability \(1/3\) each, because the admissible choices on the pair are \(\varnothing\), the first endpoint, or the second endpoint. Each of the other three new coordinates has marginal probability \(1/2\) at each old vertex of its chosen shore. These trials are independent across old vertices. The law of large numbers, followed by the finite mixture over maximum assignments, proves the last assertion.

## Verification
A standalone Python 3 checker performs direct neighbourhood-tuple enumeration for the fixed five-cycle at \(n=0,1,2,3\), independently evaluates the exact shore-assignment inclusion-exclusion, reconstructs the complete thirteen-term exponential polynomial, verifies the ten maximum assignments and five uniform defect edges, enumerates the universal rare-event constants at arities five and six, and compares complete small-arity type totals against direct enumeration of every allowed internal graph. The recorded output is in `verification_output.txt` and the executable implementation is in `verify.py`. These finite tests check calculations but are not substitutes for the all-order arguments in Steps 1–6.

## Relationship to prior work
Henson's homogeneous triangle-free graph and its finite-graph extension property are classical. Conant's *Forking and dividing in Henson graphs* (2014 preprint) provides the quantifier-elimination and graph-diagram setting, but studies dividing and forking rather than these asymptotic tuple-pattern distributions. The published record *Higher-arity Henson type enumeration and exact-counting hardness* (2026), whose complete RESULT.md was inspected, proves the stronger all-base, all-fixed-arity exact identity \(T_r(G)=\sum_F I(G\square F)\) and explicitly identifies \(I(G\square F)\) as the count at each fixed labelled internal graph. Consequently the exact finite five-cycle polynomial displayed here is a specialization of its earlier general enumeration and is **not** advanced as a new counting principle. That prior record gives asymptotics for empty parameter graphs, rather than growing balanced complete bipartite parameters. The claim assessed here is the sharp limiting internal-pattern measure for these biclique bases, the universal first odd-cycle rarity coefficient (including the leading constants), and the conditional one-defect neighbourhood law. The fact that these asymptotics can be deduced by additional analysis of an earlier exact identity is acknowledged; their independent historical priority is not certified.


## Limitations
All asymptotics require fixed tuple arity and equal growing base shores; there is no claim of an analogous limit for imbalanced shores, growing arity, random old bases or other Henson clique thresholds. The proof concerns uniform *types*, not a distribution generated by sampling random vertices from an infinite graph. The exact pentagon polynomial is a finite combinatorial identity and does not by itself constitute independent validation of novelty. The general Cartesian-product identity already subsumes the finite exact-counting framework, and priority for the new fixed-arity asymptotic and conditional distributional deductions requires further independent review.

## References
1. Gabriel Conant, *Forking and dividing in Henson graphs*, arXiv:1401.1570v1, public 2014-01-08, https://arxiv.org/html/1401.1570v1 (especially Section 3).
2. C. Ward Henson, *Countable homogeneous relational structures and \(\aleph_0\)-categorical theories*, Journal of Symbolic Logic 37 (1972), 494–500, https://doi.org/10.2307/2272734.
3. *Higher-arity Henson type enumeration and exact-counting hardness*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-higher-arity-henson-type-enumeration-and-exact-counting-hardness--141a441755d6. The complete public RESULT.md was inspected, including its fixed-internal-graph counting bijection, exact-counting hardness and independent-base asymptotics.
