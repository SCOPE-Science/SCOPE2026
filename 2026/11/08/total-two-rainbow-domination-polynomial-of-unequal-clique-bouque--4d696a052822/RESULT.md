# Total two-rainbow domination polynomial of unequal clique bouquets

## Finding

For any integer \(r\ge2\) and positive integers \(m_1,\ldots,m_r\), let the clique bouquet
\[
W=K_1\vee\left(K_{m_1}\sqcup\cdots\sqcup K_{m_r}\right),\qquad N=\sum_{i=1}^r m_i.
\]
The single vertex of \(K_1\) is the center, and the \(r\) mutually nonadjacent cliques are petals. All vertices are individually distinguishable; the two colors are named.

Let \(\mathcal T_W(z)=\sum_f z^{w(f)}\), where the sum is over all total two-rainbow dominating functions \(f\) and \(w(f)=\sum_{v\in V(W)}|f(v)|\). Set, for every integer \(m\ge1\),
\[
B_m(z)=(1+z)^{2m}-(1+z)^m+z^m,
\]
and
\[
D_m(z)=\begin{cases}
0,&m=1,\\
(1+z)^{2m}-2(1+z)^m+1-mz^2+2z^m,&m\ge2.
\end{cases}
\]
Then the full weight polynomial is
\[
\boxed{\mathcal T_W(z)=z^2\big((1+z)^{2N}-1\big)+2z\prod_{i=1}^r B_{m_i}(z)+E_W(z),}
\]
where
\[
E_W(z)=\begin{cases}
0,&\min_i m_i=1,\\
\prod_{i=1}^r D_{m_i}(z)-2z^N,&\min_i m_i\ge2.
\end{cases}
\]
The three summands count, respectively, assignments in which the center has both colors, exactly one color, or no color. In particular, every coefficient is a nonnegative integer, even though the displayed expression contains subtractions.

Every bouquet in this domain has total two-rainbow domination number \(3\). If \(b_1=2\) and \(b_m=m\) for \(m\ge2\), then the number of minimum-weight assignments is exactly
\[
[z^3]\mathcal T_W(z)=\begin{cases}
2N+2b_{m_1}b_{m_2},&r=2,\\
2N,&r\ge3.
\end{cases}
\]
Thus the two-petal case has an additional family of minimum configurations that disappears as soon as a third petal is attached.

The polynomial also gives exact independent-color reliability. If each of two colors is assigned independently at every vertex with probability \(p\), then
\[
\Pr(\text{total two-rainbow domination})=(1-p)^{2(N+1)}\mathcal T_W\!\left(\frac{p}{1-p}\right),\qquad 0<p<1.
\]
For fixed petal order \(m\ge1\), fixed \(0<p<1\), and \(W_r=K_1\vee rK_m\),
\[
\lim_{r\to\infty}\Pr(\text{total two-rainbow domination on }W_r)=p^2.
\]

## Assumptions and scope

Graphs are finite, simple, and undirected. A total two-rainbow dominating function is \(f:V(W)\to\{\varnothing,\{1\},\{2\},\{1,2\}\}\) satisfying: every empty-labeled vertex sees both colors in its open neighborhood, and every nonempty-labeled vertex has a nonempty-labeled neighbor. The polynomial counts functions, not unlabeled orbits or sets of positively labeled vertices. Petal sizes can differ, including size one. The asymptotic statement fixes \(m,p\) before increasing the number of petals; it does not claim uniformity when petal sizes grow.

## Proof

Write \(c\) for the center. The weight-generating polynomial for one unconstrained vertex is \(1+2z+z^2=(1+z)^2\); for one nonempty-labeled vertex it is \(2z+z^2\).

**Case 1: \(f(c)=\{1,2\}\).** Every empty petal vertex is protected by the center and every positive petal vertex is adjacent to it. The center itself must have at least one positive petal neighbor. Hence every peripheral assignment is allowed except the all-empty assignment, contributing \(z^2((1+z)^{2N}-1)\).

**Case 2: \(f(c)=\{1\}\), and symmetrically \(\{2\}\).** On a petal of order \(m\), an assignment is feasible if some vertex carries color 2, or all vertices are nonempty and carry only color 1. The first family has polynomial \((1+z)^{2m}-(1+z)^m\), and the remaining all-\(\{1\}\) assignment adds \(z^m\). This is precisely \(B_m(z)\). Each petal has a positive vertex, automatically supporting the center. Petals are independent given the center, and the choice of center singleton color gives \(2z\prod_i B_{m_i}(z)\).

**Case 3: \(f(c)=\varnothing\).** No petal vertex can obtain support from the center. In each petal there must be at least two positive vertices, and if the petal contains an empty vertex, its positive vertices must collectively carry both colors. A petal of order one cannot satisfy these conditions, hence contributes zero. For \(m\ge2\), the local generating polynomial is
\[
(2z+z^2)^m+\sum_{k=2}^{m-1}\binom{m}{k}\left((2z+z^2)^k-2z^k\right).
\]
In the first term all \(m\) vertices are positive (so all colors are permitted); in the sum exactly \(k<m\) are positive and both colors must occur. The binomial theorem reduces this expression to \(D_m(z)\) above. Finally the empty center must see both colors across all petals. The only locally permissible configurations failing this last requirement are the assignment \(\{1\}\) everywhere and the assignment \(\{2\}\) everywhere. Subtract \(2z^N\). The three center cases partition all assignments, proving the formula.

**Minimum coefficient.** In Case 1 the minimum weight is three, with \(2N\) choices (one singleton color on one of the \(N\) peripheral vertices). In Case 2, each petal has minimum weight one, realized in \(b_m\) ways: either singleton color on its unique vertex when \(m=1\), or a single complementary-colored vertex when \(m\ge2\). Therefore the minimum weight of Case 2 is \(r+1\), with \(2\prod_i b_{m_i}\) assignments. In Case 3 every petal has at least two positive vertices, so the minimum weight is at least \(2r\), if the case is feasible at all. Since \(r\ge2\), precisely the stated Case-1 and (only for \(r=2\)) Case-2 configurations contribute at weight three.

**Reliability limit.** The substitution converts each weight-\(w\) function into the probability \(p^w(1-p)^{2(N+1)-w}\). Conditional on two colors at the center, total domination holds unless all peripheral vertices get the empty label, an event with probability \((1-p)^{2mr}\). For either other center label, each fixed petal independently has a strictly positive chance of an all-empty assignment, which is locally invalid; thus the conditional success probability is at most \((1-(1-p)^{2m})^r\). Consequently the unconditional success probability tends to the probability \(p^2\) of both colors appearing at the center.

## Verification

The accompanying standalone `verify_total_rainbow_windmills.py` enumerates every assignment of the four possible labels and checks the original neighborhood requirements directly. It compares the entire coefficient vectors against the displayed polynomial and its minimum coefficient on 126 distinguishable clique-bouquet instances, checking 5,197,632 assignments, of which 2,461,279 satisfy total two-rainbow domination. The verifier outputs `VERIFY_OK`; all comparisons passed. These finite computations corroborate, but do not replace, the proof for arbitrary petal counts and sizes.

## Relationship to prior work

The total rainbow domination framework originates with Abdollahzadeh Ahangar, Amjadi, Jafari Rad, and Samodivkin (2018). Jiang and Rao (2022) study total two-rainbow domination, establish hardness on several graph classes, and provide an algorithm for trees. The present claim enumerates all feasible colored functions, including nonminimum ones, on bouquets of cliques of arbitrary unequal sizes. It does not follow merely from a minimum-weight theorem or a tree algorithm: bouquets with clique petals of size at least two contain triangles. Literature and indexed research comparisons found work on rainbow domination of complete multipartite graphs and other polynomial enumerators for generalized windmills, but those treat different graph classes or different constraints. The formula for the present problem is asserted only to the extent supported by the inspections summarized in REVIEW.md and AUDIT.json; publication priority remains provisional.

## Limitations

No general statement is made for arbitrary block graphs or for larger color palettes. The formula requires a *single* universal center and pairwise nonadjacent clique petals; an arbitrary block-cut tree has interactions absent here. The random-color limit assumes fixed petal order and fixed assignment probability. The earlier foundational 2018 publication was compared through bibliographic/abstract material rather than a verified page-by-page full-text reading, which is a residual priority risk. Independent mathematical audit has not been performed.

## References

1. H. Jiang and Y. Rao, "Total 2-Rainbow Domination in Graphs," *Mathematics* **10** (2022), 2059. DOI: 10.3390/math10122059. First publicly dated source used here: 2022-06-14.
2. H. Abdollahzadeh Ahangar, J. Amjadi, N. Jafari Rad, V. Samodivkin, "Total \(k\)-Rainbow Domination Numbers in Graphs," *Communications in Combinatorics and Optimization* **3** (2018), 37–50. DOI: 10.22049/CCO.2018.25719.1021. Earlier work; day-level first-public evidence not established in this inspection.
3. Q. Kang, V. Samodivkin, Z. Shao, S. M. Sheikholeslami, M. Soroudi, "Outer-independent \(k\)-rainbow domination," *Journal of Taibah University for Science* **13** (2019), 883–891. DOI: 10.1080/16583655.2019.1655255. Distinct non-total variant used for comparison only.
