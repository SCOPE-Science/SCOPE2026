# Exact girth trichotomy for shifted geometric supports and Abelian pattern Sturmian words

## Finding
Let \(b\ge 2\) be an integer and \(c\ge0\) a nonnegative integer. Define
\[
E_{b,c}=\{b^j+c:j\ge0\}\subseteq\mathbb N_0,
\]
and let \(u^{(b,c)}\) be the binary characteristic word of this set. Let \(\Gamma_{b,c}\) be the simple bipartite graph with two separate copies \(L_r,R_s\) of each nonnegative integer, and an edge \(L_rR_s\) precisely when \(r+s\in E_{b,c}\). Define the girth of a forest to be \(\infty\).

The **exact graph-girth trichotomy** is
\[
\operatorname{girth}(\Gamma_{b,c})=
\begin{cases}
\infty, & 0\le c<b(b-2),\\
2b+2, & b(b-2)\le c<b^2-b-1,\\
6, & c\ge b^2-b-1.
\end{cases}
\]
The middle interval is a singleton when \(b=2\), and is nonempty for every integer \(b\ge2\).

By the published incidence-forest characterization of Abelian pattern Sturmian words, \(u^{(b,c)}\) attains the minimal possible Abelian maximal pattern complexity at **every** pattern length if and only if
\[
0\le c<b(b-2).
\]
In particular, unshifted powers of base \(b\) have this property precisely for \(b\ge3\); the boundary shift \(c=b(b-2)\) creates a cycle of length \(2b+2\). At the second threshold \(c=b^2-b-1\), the girth is six (a strict decrease for \(b\ge3\); for \(b=2\), both finite branches have girth six).

## Assumptions and scope
Every parameter is an integer, \(b\ge2,c\ge0\). All vertices have nonnegative integer indices. Girth refers to finite simple cycles, not to closed walks or cycles in a finite truncation. Each \(b^j+c\) contributes a matching, as each fixed left vertex has at most one right neighbor with that specified edge sum. We use the standard Abelian maximal pattern complexity
\[
p^{*\mathrm{ab}}_u(k)=\sup_{S\subset\mathbb N_0,\ |S|=k}\left|\left\{\sum_{s\in S}u_{t+s}:t\ge0\right\}\right|,\qquad k\ge1.
\]
The cited incidence-forest theorem characterizes the words for which this equals the least integer \(m\ge1\) with \(\binom m2\ge k\) for every \(k\ge1\).

## Proof
Write \(d=b-1\) and \(s_j=b^j+c\). The three smallest allowed edge sums are \(a=s_0=c+1\), \(h=s_1=a+d\), and \(s_2=h+bd\). Every graph edge has a unique weight \(s_j\). Two adjacent distinct edges have different weights because, from one endpoint, specifying a weight uniquely determines the opposite endpoint.

**1. No cycles below the first threshold.** Two distinct weights \(a,h\) by themselves form two matchings, whose union has no finite cycle: weights around any hypothetical cycle must alternate, while the alternating-sum identity for a bipartite cycle would yield equal multiples of \(a\) and \(h\), a contradiction. If \(c<b(b-2)\), then for all \(j\ge2\),
\[
s_j-2s_{j-1}=(b-2)b^{j-1}-c\ge b(b-2)-c>0.
\]
In a hypothetical cycle whose largest edge weight is \(s_j\), \(j\ge2\), take an edge \(L_xR_y\) of this weight. Since \(x+y=s_j>2s_{j-1}\), one of \(x,y\) exceeds \(s_{j-1}\). Such a vertex cannot be incident to any lower-weight edge, nor to another edge of weight \(s_j\). It would have degree one among edges of weight at most \(s_j\), contradicting its presence on a cycle. Thus the graph is a forest.

**2. A \((2b+2)\)-cycle at and above the first threshold.** Suppose \(c\ge b(b-2)\), equivalently \(a\ge d^2\). The edges
\[
L_hR_0,\quad L_aR_0,\quad
L_{a-jd}R_{(j+1)d}\ (0\le j\le b-1),\quad
L_{a-(j+1)d}R_{(j+1)d}\ (0\le j\le b-2),\quad
L_hR_{bd}
\]
form a simple cycle in the listed path order. The first edge and each edge in the first indexed family have sum \(h\); the second edge and each edge in the second indexed family have sum \(a\); and the closing edge has sum \(h+bd=s_2\). All indices are nonnegative, the left indices strictly decrease along the interior path, and the right indices strictly increase. There are \(2b+2\) distinct edges and vertices on the cycle. Hence the girth is finite and at most \(2b+2\).

**3. There are no four-cycles.** In a four-cycle, the sums of the weights on opposite edges are equal. Cancelling the common shift yields \(b^i+b^j=b^k+b^\ell\). For any integer base \(b\ge2\), equality of sums of two powers forces equality of the unordered exponent pairs. To see uniqueness, divide an equality of two such sums by the smallest power of \(b\) occurring, and compare its least nonzero base-\(b\) digits, allowing the carry of \(1+1=2\) when \(b=2\); equivalently, sort each exponent pair and compare first its larger exponent and then its smaller exponent. The only possible equality has the same unordered exponent pair. The resulting equality of opposite-weight multisets is incompatible with the fact that adjacent edges of a cycle have different weights. Thus four-cycles never occur. Bipartiteness also excludes odd cycles.

**4. Exact girth in the intermediate band.** Assume \(b\ge3\) and
\[
b(b-2)\le c<b(b-2)+d=b^2-b-1.
\]
Put \(\delta=c-b(b-2)\), so \(0\le\delta<d\). For every \(j\ge3\), the inequality \(s_j>2s_{j-1}\) holds because \(c<b^2-b-1<(b-2)b^2\). By the maximum-weight argument in step 1, no cycle uses a weight \(s_j\) with \(j\ge3\).

Any edge of weight \(s_2\) that lies on a cycle must have both endpoint indices at most \(h\), since otherwise one endpoint has no other incident edge among the three smallest weights. Since \(s_2=h+bd\) and \(h=bd+\delta\), the only possible such edges are
\[
L_{bd+r}R_{h-r},\qquad 0\le r\le\delta.
\]
All three sums \(a,h,s_2\) are congruent modulo \(d\). Consequently every component has a fixed residue for its left indices modulo \(d\). The displayed eligible \(s_2\)-edges have distinct left residues because \(0\le r\le\delta<d\); hence a component contains at most one edge of weight \(s_2\) that can participate in a cycle.

After removing that single edge, its component is contained in the graph of the two lower matchings, which is acyclic. The unique path between its endpoints, when present, must start at \(L_{bd+r}\) with a weight-\(h\) edge, and is forced by alternating the two matchings. Its left vertices are \(L_{bd+r}, L_{(b-1)d+r},\ldots,L_r\), and its right vertices are \(R_{\delta-r},R_{d+\delta-r},\ldots,R_{bd+\delta-r}=R_{h-r}\). Thus it contains exactly \(2b+1\) edges; adding the sole weight-\(s_2\) edge closes a cycle of length exactly \(2b+2\). Together with step 2 this proves the claimed girth. For \(b=2\) the intermediate interval consists solely of \(c=0\); its explicit six-cycle from step 2 and the absence of four-cycles prove girth six directly.

**5. Six-cycles at and above the second threshold.** Suppose \(c\ge b^2-b-1\), which is equivalent to \(a\ge bd\). The six distinct vertices
\[
L_{bd},\ R_{a-bd},\ L_{bd+d},\ R_a,\ L_0,\ R_h
\]
form a six-cycle in this cyclic order. Their consecutive edge sums are \(a,h,s_2,a,h,s_2\), respectively. All indices are nonnegative and distinct within their bipartition. Step 3 excludes shorter cycles, so the girth is exactly six.

**6. Passing from graph girth to Abelian pattern complexity.** The cited incidence-forest characterization is applied to the characteristic word of \(E_{b,c}\). Relabeling the binary alphabet could replace \(E_{b,c}\) by its complement, but that complement is never a forest-support: the gaps \(s_{j+1}-s_j\) tend to infinity, so the complement contains three consecutive integers \(t,t+1,t+2\); these give a four-cycle on \(L_0,L_1,R_t,R_{t+1}\). Thus the characterization holds if and only if \(\Gamma_{b,c}\) itself is a forest, precisely in the first regime. This completes the proof.

## Verification
The standalone script `verify.py` constructs bipartite sum-incidence graphs for the three smallest powers. It independently tests the sharp forest cutoff for bases \(2\) through \(15\) and verifies explicit cycle witnesses, covering \(1071\) parameter pairs. The infinite claims and the exact girth bounds follow from the symbolic proof above; the finite tests are corroboration, not a replacement for proof. Run `python3 verify.py`.

## Relationship to prior work
Zeng, Xue and Zeng (2026) prove the general equivalence between Abelian pattern Sturmian words and forest sum-incidence graphs; this result is used as an explicit premise, not claimed here as new. The new contribution is the sharp two-parameter trichotomy for the particular infinite geometric-support family, including the *girth* on both non-forest sides. Earlier work by Kamae, Widmer and Zamboni defines Abelian maximal pattern complexity. A previously reported general support-sparsity envelope and a finite three-mark prefix extension criterion constrain potential forests, but neither alone determines the complete graph girth of this particular infinite family. The relevant examples subsection of the September 2026 source was not fully retrievable during comparison; possible overlap there remains an explicit priority risk.

## Limitations
Only integer bases \(b\ge2\) and nonnegative shifts \(c\) are covered. The statement does not classify arbitrary lacunary supports, negative shifts, or the exact complexity values of non-extremal words outside the forest regime. The proof of the word-complexity equivalence relies on the published incidence-forest characterization, whereas the graph-girth trichotomy is self-contained. An independent scientific audit has not been performed.

## References
1. Qingcheng Zeng, Yumei Xue and Cheng Zeng, *Abelian maximal pattern complexity and extremal words*, arXiv:2609.28059, first public version September 23, 2026, https://arxiv.org/abs/2609.28059 .
2. Teturo Kamae, Steven Widmer and Luca Q. Zamboni, *Abelian maximal pattern complexity of words*, arXiv:1301.5113, published in *Ergodic Theory and Dynamical Systems* 35 (2015), 142–151, https://arxiv.org/abs/1301.5113 .
