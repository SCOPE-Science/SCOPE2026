# Sharp factorial tails and an extreme-run law for nearest-predecessor genealogies

## Finding

For the seedless nearest-predecessor genealogy on the infinite \(d\)-regular tree, \(d\ge3\), the number \(L(v)\) of consecutive *original-tree edges* at the start of the ancestral path of a fixed vertex has an exact distribution, a sharp harmonic-number factorial tail, and a corresponding almost-sure extremal law.

Write \(H_j=\sum_{i=1}^j1/i\) and define, for each integer \(m\ge0\),
\[
h_m(t)=\int_0^1(1-t+tu)^m\,du
=\begin{cases}\dfrac{1-(1-t)^{m+1}}{(m+1)t},&t>0,\\1,&t=0.\end{cases}
\]
Set \(F(t)=\int_0^t h_{d-2}(u)\,du\) and \(b=F(1)=H_{d-1}/(d-1)\). For every integer \(k\ge1\),
\[
\boxed{\mathbb P(L(v)\ge k)=
\frac{d(d-1)^{k-1}}{(k-1)!}
\int_0^1h_{d-1}(t)\int_0^t[F(t)-F(s)]^{k-1}\,ds\,dt.}
\tag{1}
\]
All values in (1) are rational. Furthermore, at fixed \(d\) as \(k\to\infty\),
\[
\boxed{\mathbb P(L(v)\ge k)=
\frac{H_{d-1}}{d-1}\frac{H_{d-1}^{\,k}}{(k+1)!}
\left(1+O_d(k^{-1})\right).}
\tag{2}
\]
In particular, \(L(v)<\infty\) almost surely. For degree \(d=3\), the first three nonzero tails are \(3/4\), \(31/90\), and \(31/252\), and the leading tail is \((3/4)(3/2)^k/(k+1)!\).

Fix a reference vertex \(o\), put \(B_R=B(o,R)\), and let \(M_R=\max_{v\in B_R}L(v)\). Then
\[
\boxed{\lim_{R\to\infty}\frac{M_R\log\log|B_R|}{\log|B_R|}=1\quad\text{almost surely}.}
\tag{3}
\]
Thus the maximum uninterrupted original-edge ancestry in a growing ball has scale \(\log|B_R|/\log\log|B_R|\), even though the individual ancestral line in the full genealogy is infinite.

## Assumptions and scope

Let \(\mathcal T_d\) be the countably infinite homogeneous tree of degree \(d\ge3\), with ordinary graph distance. Assign independent uniform \((0,1)\) arrival marks \((\tau_v)_{v\in\mathcal T_d}\). Each vertex chooses as parent a vertex having strictly smaller arrival mark and minimal graph distance; ties are resolved uniformly, independently at different vertices (equivalently, by independent random distance-ordered neighbor rankings). Almost surely such a parent exists for every vertex. This is the seedless infinite-tree genealogy in Basdevant–Singh's model, not a coloring with initial seeds.

Let \(v=v_0,v_1,v_2,\ldots\) be the successive parents of \(v\). Define \(L(v)\) as the largest integer \(k\ge0\) for which \(v_0v_1,\ldots,v_{k-1}v_k\) are all edges of the underlying tree, with \(L(v)=\infty\) if every ancestral edge is local. Because arrival marks strictly decrease along the ancestry, a contiguous local segment is a non-backtracking self-avoiding path. Both the degree and the distribution of marks are fixed with \(R\to\infty\); uniform marks can be replaced by any common atomless law using probability integral transforms.

## Proof

**1. Exact path probabilities.** For \(m\ge0\), let \(J\sim\mathrm{Binomial}(m,t)\). The identity \(1/(1+j)=\int_0^1u^j\,du\) gives
\[
\mathbb E\frac1{1+J}=\int_0^1(1-t+tu)^m\,du=h_m(t).
\]
For any prescribed length-\(k\) non-backtracking path \(v_0,\ldots,v_k\), the first \(k\) parent choices follow this path only if their arrival marks are strictly decreasing, say \(t_0>\cdots>t_k\). Under this ordering, the first vertex has \(d-1\) other neighbors that might have arrived earlier than \(t_0\). Every later interior vertex has its preceding path neighbor later than itself, and \(d-2\) side neighbors that might have arrived earlier. The side-neighbor sets at different path vertices are disjoint because the base graph is a tree. Independent marks and tie rankings therefore give conditional selection probability
\[
h_{d-1}(t_0)\prod_{i=1}^{k-1}h_{d-2}(t_i).
\]
There are exactly \(d(d-1)^{k-1}\) possible non-backtracking paths from \(v_0\), and distinct chosen-path events are disjoint. Integrating over ordered uniform marks, then setting \(s=t_k\), the intermediate ordered integrals of identical factors contribute
\[
\frac1{(k-1)!}\left(\int_s^t h_{d-2}(u)\,du\right)^{k-1}.
\]
This proves (1), including \(k=1\). In that case direct integration yields \(\mathbb P(L\ge1)=d/(d+1)\), hence \(\mathbb P(L=0)=1/(d+1)\). Since the \(h_m\) are rational-coefficient polynomials, (1) is rational for every integer \(d,k\).

**2. The sharp factorial constant.** Let \(F\) and \(b\) be as above. Integrating \(h_{d-2}\) after substituting \(u=1-t\) shows
\[
b=\frac{1}{d-1}\int_0^1\frac{1-u^{d-1}}{1-u}\,du=\frac{H_{d-1}}{d-1}.
\]
Use the change of variables \(x=F(s)\), \(y=F(t)\) in (1). The resulting integral is
\[
I_k=\int_{0<x<y<b}\alpha(y)\beta(x)(y-x)^{k-1}\,dx\,dy,
\]
where \(\alpha(y)=h_{d-1}(F^{-1}(y))/h_{d-2}(F^{-1}(y))\) and \(\beta(x)=1/h_{d-2}(F^{-1}(x))\). These are bounded positive Lipschitz functions on \([0,b]\), and
\[
\alpha(b)=\frac{d-1}{d},\qquad\beta(0)=1,\qquad
\int_{0<x<y<b}(y-x)^{k-1}\,dx\,dy=\frac{b^{k+1}}{k(k+1)}.
\]
Under the probability kernel proportional to \((y-x)^{k-1}\) on this triangle, \(\mathbb E x=\mathbb E(b-y)=b/(k+2)\). The Lipschitz property therefore gives
\[
I_k=\frac{b^{k+1}}{k(k+1)}\left(\frac{d-1}{d}+O_d(k^{-1})\right).
\]
Substituting into (1) proves (2), since \((d-1)b=H_{d-1}\). Its right-hand side tends to zero, proving \(L(v)<\infty\) almost surely.

**3. Almost-sure maxima.** For \(N_R=|B_R|=1+d((d-1)^R-1)/(d-2)\), set \(a_R=\log N_R/\log\log N_R\). By (2) and Stirling's formula, for every fixed \(0<\varepsilon<1\),
\[
\mathbb P(L(v)\ge\lceil(1+\varepsilon)a_R\rceil)
=N_R^{-(1+\varepsilon)+o(1)},
\]
and similarly with \(1-\varepsilon\). The union bound shows that
\[
\mathbb P(M_R\ge\lceil(1+\varepsilon)a_R\rceil)
\le N_R^{-\varepsilon+o(1)}.
\]
This is summable over integer \(R\), since \(N_R\) grows exponentially.

Conversely, the event \(\{L(v)\ge k\}\) depends only on the arrival marks and tie choices in \(B(v,k)\): to test the first \(k\) local choices, all competing neighbors lie within this ball. Choose a deterministic set \(W_R\subset B_R\) whose pairwise distances exceed \(2k\), with \(k=\lfloor(1-\varepsilon)a_R\rfloor\), by greedy packing. The events at points of \(W_R\) are independent, and
\[
|W_R|\ge\frac{N_R}{|B_{2k}|}=N_R^{1-o(1)}.
\]
Thus
\[
\mathbb P(M_R<k)
\le (1-\mathbb P(L(v)\ge k))^{|W_R|}
\le\exp\bigl(-N_R^{\varepsilon+o(1)}\bigr),
\]
again summable. Borel–Cantelli for both bounds and a countable sequence of \(\varepsilon\downarrow0\) yields (3).

## Verification

The bundled `verify.py` requires only Python 3 standard libraries and is run by `python3 verify.py`. It computes exact rational values of (1) using polynomial recursions, and independently enumerates every ordering of the arrival marks within the relevant path-neighborhood for degrees \(3,4\) and short paths. Its recorded results match \(\mathbb P_3(L\ge1)=3/4\), \(\mathbb P_3(L\ge2)=31/90\), \(\mathbb P_3(L\ge3)=31/252\), \(\mathbb P_4(L\ge1)=4/5\), and \(\mathbb P_4(L\ge2)=1471/3360\). Further finite checks confirm monotonicity through eleven local steps for degrees \(2\) through \(7\) and track the factorial ratio through length \(30\) in degree \(3\). A seeded simulation of 100,000 independent local runs independently checks the first five degree-three tails.

These finite checks verify special cases and program consistency; they do not establish (2) or (3). Those infinite claims follow from the explicit Lipschitz boundary integral estimate and the packing/Borel–Cantelli argument above.

## Relationship to prior work

Basdevant and Singh (2026) define this exact nearest-predecessor genealogy, prove global structure and local-limit results, and give a lower-record construction of ancestral exploration (notably their Section 2.1 and Lemma 10). The new assertion is the evaluated distribution of the *initial uninterrupted length-one ancestor run*, its degree-dependent sharp harmonic factorial prefactor, and the extremal law over expanding balls. An ancestry construction specifies the process but does not itself supply these evaluated formulas or an extreme-run theorem. Independent tie rankings and local tree geometry are essential to the evaluation.

Angel, Ferber, Sudakov and Tassion (2019) study monotone **edge-label** paths/trails in randomly ordered graphs, not nearest-earlier **vertex** genealogy or its tie-biased local run. Aldous (2018) studies Poissonian coloring in Euclidean space, rather than tree-based uninterrupted ancestral edges. Their results are not substitutes for equations (1)–(3). Existing general order-statistic and Borel–Cantelli tools are used transparently, without claiming them as inventions.

## Limitations

The law concerns the length of the *initial* consecutive string of ancestral edges that remain actual edges of the base tree; it does not give the length of the full ancestral line, nonlocal jump sizes, component sizes, or analogous extremes for a finite seeded coloring. The degree \(d\) is fixed. Formula (3) is a first-order almost-sure law; no centered limiting law for the maximum is asserted. The search for earlier equivalent priority claims is necessarily non-exhaustive; closest accessible published work was compared at the level of models and conclusions, but independent bibliographic and mathematical validation has not been performed.

## References

1. A.-L. Basdevant and A. Singh, *Random sequential nearest-neighbor coloring on trees*, arXiv:2606.24793v1, first posted June 23, 2026. https://arxiv.org/abs/2606.24793 and https://arxiv.org/html/2606.24793 .
2. O. Angel, A. Ferber, B. Sudakov and V. Tassion, *Long monotone trails in random edge-labellings of random graphs*, arXiv:1808.07351, *Combinatorics, Probability and Computing* (2019). https://arxiv.org/abs/1808.07351 .
3. D. J. Aldous, *Random partitions of the plane via Poissonian coloring and a self-similar process of coalescing planar partitions*, *Annals of Probability* 46 (2018), 2000–2037, DOI:10.1214/17-AOP1218. https://doi.org/10.1214/17-AOP1218 .
