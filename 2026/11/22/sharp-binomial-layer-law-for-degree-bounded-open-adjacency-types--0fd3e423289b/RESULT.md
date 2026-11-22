# Sharp binomial-layer law for degree-bounded open-adjacency types

## Finding

For a finite simple undirected graph \(G\) and marked vertices \(A\subseteq V(G)\), the *open-adjacency trace family* is
\[
\mathcal T(G,A)=\{N_G(v)\cap A:v\in V(G)\}.
\]
Let \(\pi_d(m)\) be the maximum of \(|\mathcal T(G,A)|\) over all finite simple graphs of maximum vertex degree at most \(d\) and all \(m\)-element marked sets. The two parameters \(m\ge1\) and \(d\ge0\) are arbitrary integers.

For \(d=0\), \(\pi_0(m)=1\). For \(d\ge1\), define the binomial incidence thresholds
\[
B_j(m)=\sum_{i=0}^{j-1}\binom{m-1}{i}\quad(1\le j\le m),
\]
let \(r\) be the largest integer in \(\{1,\ldots,m\}\) with \(B_r(m)\le d\), and put \(\rho=d-B_r(m)\) if \(r<m\). Then
\[
\boxed{\displaystyle\pi_d(m)=1+\sum_{j=1}^{r}\binom mj+\begin{cases}
\left\lfloor\dfrac{m\rho}{r+1}\right\rfloor,&r<m,\\
0,&r=m.
\end{cases}}
\]
The maximum is attained by a graph with **exactly \(\pi_d(m)\) vertices**, whose vertices have pairwise different traces on the specified marked set. Thus this host size is the smallest possible for an extremizer (for positive \(d\)); when \(d=0\), the smallest host has \(m\) vertices.

In particular, when \(m\ge d\ge1\),
\[
\pi_d(m)=1+\left\lfloor\frac{m(d+1)}{2}\right\rfloor.
\]
The maximum size of a shattered marked set in graphs of maximum degree at most \(d\ge1\), equivalently the VC dimension of the class of open-neighborhood concepts across all such graphs, is precisely \(1+\lfloor\log_2d\rfloor\); its VC density is one for every fixed positive degree bound. At every exact threshold \(d=B_r(m)\), an extremal trace family necessarily consists of **all subsets of \(A\) of size at most \(r\)**.

## Assumptions and scope

Graphs are finite, loopless, undirected and without multiple edges, but need not be connected. The maximum degree is a bound, not an exact-degree requirement; \(G\) is allowed to depend on \(m,d\). Marked vertices themselves contribute traces, and the neighborhoods are *open* (the vertex itself is not a neighbor). Empty traces count once. The extremal host may contain additional unmarked vertices. The minimum-host statement concerns all host vertices, including the marked set, and does not assert uniqueness of extremizing graphs or of non-threshold trace families.

## Proof

**1. Incidence-budget upper bound.** Fix \(G,A\). For each distinct nonempty trace \(S\in\mathcal T(G,A)\), choose one realizing vertex \(v_S\). These vertices are distinct, hence
\[
\sum_{\substack{S\in\mathcal T(G,A)\\S\ne\varnothing}}|S|
=\sum_{a\in A}|\{S:a\in S\}|\le\sum_{a\in A}\deg_G(a)\le md.
\]
Among all distinct nonempty subsets of an \(m\)-set, a family with the largest possible number subject to this *total incidence budget* uses all smaller cardinalities before any larger ones. The total cost of the entire layers of cardinalities \(1,\ldots,r\) is
\[
\sum_{j=1}^{r}j\binom mj=m\sum_{i=0}^{r-1}\binom{m-1}{i}=mB_r(m).
\]
If \(r<m\), the remaining budget \(m\rho\) pays for at most \(\lfloor m\rho/(r+1)\rfloor\) sets in the next layer. If \(r=m\), every subset is already present. An empty trace costs zero and can contribute at most one. This gives the asserted upper bound, including the \(d=0\) case.

**2. Equitable uniform-family lemma.** Given integers \(m\ge k\ge1\) and \(0\le e\le\binom mk\), there is a family \(\mathcal H\) of \(e\) *distinct* \(k\)-subsets of \(\{1,\ldots,m\}\) whose vertex degrees differ by at most one. For a proof, start with any such family minimizing the sum of squares of its \(m\) vertex degrees. If \(u,v\) have degrees with \(\deg(u)\ge\deg(v)+2\), consider the two collections of \((k-1)\)-subsets \(Q\) disjoint from \(\{u,v\}\) for which \(Q\cup\{u\}\in\mathcal H\) and \(Q\cup\{v\}\in\mathcal H\), respectively. Their cardinality difference is \(\deg(u)-\deg(v)>0\); therefore for some \(Q\), \(Q\cup\{u\}\) is present but \(Q\cup\{v\}\) is absent. Swapping them preserves distinctness and decreases the square-sum by at least two, a contradiction. Consequently the maximum degree equals \(\lceil ke/m\rceil\).

**3. Realizing the cheapest set family.** For \(d\ge1\), form \(\mathcal F\subseteq2^A\) from the empty set, all subsets of size \(1\) through \(r\), and, when \(r<m\), precisely
\[
e=\left\lfloor\frac{m\rho}{r+1}\right\rfloor
\]
subsets of size \(r+1\) chosen via the equitable lemma. Their latter per-point incidence is at most
\[
\left\lceil\frac{(r+1)e}{m}\right\rceil\le\rho,
\]
so for every marked vertex \(a\), the number of sets of \(\mathcal F\) containing \(a\) is at most \(B_r(m)+\rho=d\). In addition every set in \(\mathcal F\) has cardinality at most \(d\): the largest cardinality is either \(r\le B_r(m)\le d\), or \(r+1\le d\) when an extra-layer set occurs (an extra set requires \(\rho\ge1\)).

For clarity, a first realization uses an independent marked set and one extra vertex for each nonempty \(S\in\mathcal F\), adjacent precisely to the marked vertices in \(S\); an isolated vertex realizes the empty trace. Its maximum degree is at most \(d\) and its trace family is exactly \(\mathcal F\). This establishes sharpness without any constraint on host order.

**4. A minimum-order extremizer.** We now realize \(\mathcal F\) on exactly \(|\mathcal F|\) vertices. First choose distinct marked vertices \(A=\{a_1,\ldots,a_m\}\) and impose an internal graph \(H\) whose marked traces are all different and belong to \(\mathcal F\). For \(m=1\), use the isolated vertex; for \(r=1\) and \(m\ge2\), use a matching on \(A\), leaving one vertex unmatched when \(m\) is odd. Its marked traces are distinct singletons, together with the empty set if required. For \(r\ge2\), use a single edge if \(m=2\), a triangle if \(m=3\), and the path \(a_1a_2\cdots a_m\) if \(m\ge4\). These graphs have pairwise distinct open traces of size at most \(r\). (The one-vertex case does not require \(r\ge2\).)

For every \(S\in\mathcal F\) not already realized as \(N_H(a)\cap A\) by one of the marked vertices, add one fresh unmarked vertex adjacent precisely to \(S\), and put no edges between fresh vertices. Exactly one vertex now realizes each trace, hence the host has \(|\mathcal F|\) vertices. At any marked vertex \(a\), each internal marked neighbor accounts for the *unique marked trace containing \(a\)* from that neighbor, and each fresh neighbor accounts for its own trace containing \(a\). Therefore its total degree is exactly \(|\{S\in\mathcal F:a\in S\}|\le d\). Every new vertex has degree \(|S|\le d\). This proves the minimum-host claim.

**5. Two consequences and rigidity.** If \(m\ge d\), the cheapest positive layer has cost one, and the next layer has cost two, giving the stated formula for fixed \(d\) (including \(m=d\), when the entire second layer is selected). A marked \(m\)-set can be shattered only if all \(2^m\) traces occur; their total incidence is \(m2^{m-1}\), so \(d\ge2^{m-1}\) is necessary. It is sufficient by the preceding construction, since in this case \(B_m(m)=2^{m-1}\). The VC-dimension and density statements follow. Finally, when \(d=B_r(m)\), the greedy upper-bound incidence budget is exhausted by the complete size-\(1\) through size-\(r\) layers. Replacing any member by a larger missing subset would strictly exceed the budget. Consequently the only extremal family is the full rank-\(r\) Boolean truncation (including the empty set).

## Verification

`check.py` is a self-contained standard-library checker. Running `python check.py` prints `ALL_CHECKS_OK` after: constructing extremal families for 225 parameter pairs; constructing and checking minimum-host extremizers for 588 pairs; testing 538 equitable uniform-family instances; testing all 32,768 possible families of nonempty subsets on four marks against the claimed incidence-budget optimum; and testing all 2,097,151 graph/marked-set combinations with at most six host vertices. Finite computations independently stress-test boundaries, but the foregoing proofs establish every parameter case.

## Relationship to prior work

Berthe, Foucaud, Lehtilä and Parreau's 2026 treewidth/pathwidth study obtains sharp **closed-neighborhood** complexity bounds from decomposition width, including a sharp forest bound. The present theorem instead concerns **open-neighborhood** types and the completely different restriction of bounded maximum vertex degree. A maximum-degree bound does not bound treewidth, so that paper's exact formulas do not imply this one. Bonnet, Foucaud, Lehtilä and Parreau establish near-tight **twin-width** neighborhood bounds, using a width parameter rather than vertex degree; their stated estimates likewise do not give the exact degree-layer phases, equality rigidity, or minimal host order. More general bounded-expansion/profile-complexity literature motivates why a linear coefficient is relevant, but the claim here is an all-parameter exact expression, not a qualitative linear bound.

## Limitations

No claims are made for directed graphs, loops, closed neighborhoods, higher-distance balls, infinite graphs, or graphs constrained to be connected. Non-threshold extremizers need not have a unique trace family. The result's historical priority is provisional: the inspected literature and searchable records are not an exhaustive proof of novelty, and independent mathematical review has not been conducted.

## References

1. G. Berthe, F. Foucaud, T. Lehtilä, A. Parreau, *Neighbourhood complexity and identification problems for graphs of bounded treewidth and pathwidth*, arXiv:2607.16889 (initial public posting 2026-07-18), https://arxiv.org/abs/2607.16889 ; lawful full-text HTML: https://www.paperpeel.com/paper/2607.16889 .
2. É. Bonnet, F. Foucaud, T. Lehtilä, A. Parreau, *Neighbourhood complexity of graphs of bounded twin-width*, arXiv:2301.04217v2 (2023), https://arxiv.org/html/2301.04217v2 .
3. L. Beaudou, J. Bok, F. Foucaud, D. A. Quiroz, J.-F. Raymond, *Profile and neighbourhood complexity of graphs with excluded minors and tree-structured graphs*, arXiv:2501.08895 (2025), https://arxiv.org/abs/2501.08895 .
