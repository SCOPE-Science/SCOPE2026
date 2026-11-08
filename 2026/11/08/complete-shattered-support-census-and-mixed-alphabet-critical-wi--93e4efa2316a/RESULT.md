# Complete shattered-support census and mixed-alphabet critical window for categorical subcubes

## Finding
Let \(d\ge1\) and let \(E_1,\ldots,E_d\) be finite sets with \(q_i=|E_i|\ge2\). Put \(X=\prod_{i=1}^d E_i\) and \(Q=\prod_{i=1}^d q_i\). A *categorical subcube* is a nonempty Cartesian cell \(C=\prod_{i=1}^d C_i\), where each \(C_i\) is either \(E_i\) or a singleton. The family \(\mathcal C(X)\) comprises all such cells, including \(X\) and all singleton points. Let \(s_m(X)\) count the unordered \(m\)-point subsets of \(X\) shattered by this family.

**Complete exact census.** The coefficients are \(s_0=1\), \(s_1=Q\), and
\[
s_2=\begin{cases}\binom Q2,&Q>2,\\0,&Q=2.\end{cases}
\]
For every integer \(m\ge3\),
\[
\boxed{\displaystyle
s_m(X)=\frac1{m!}\sum_{j=0}^m(-1)^j\binom mj
\prod_{i=1}^d\bigl(q_i^m-jq_i(q_i-1)\bigr).}
\]
In particular \(s_m(X)=0\) for \(m>d\) when \(m\ge3\), while for \(d\ge3\),
\[
\boxed{\displaystyle s_d(X)=\prod_{i=1}^d q_i(q_i-1).}
\]
The VC dimension equals \(d\) for \(d\ge3\), equals \(2\) for \(d=2\), and equals \(2\) for \(d=1,q_1\ge3\) but \(1\) for \(d=1,q_1=2\).

**Universal critical window.** For each \(m\ge3\), let the number of coordinates and their alphabet sizes be \(d_m\) and \(q_{m,i}\ge2\), and draw \(m\) independent uniformly distributed points from the corresponding product \(X_m\), with replacement. Define
\[
p_{m,i}=\frac{q_{m,i}-1}{q_{m,i}^{m-1}},\qquad
\mu_m=\sum_{i=1}^{d_m}p_{m,i}.
\]
If \(\mu_m-\log m\to c\in\mathbb R\), then
\[
\boxed{\displaystyle
\Pr(\text{the sampled points are distinct and shattered by }\mathcal C(X_m))
\longrightarrow\exp(-e^{-c}).}
\]
No bound on the variation of alphabet sizes is needed beyond \(q_{m,i}\ge2\). For constant \(q\), one may take \(d_m=\lfloor q^{m-1}(\log m+c)/(q-1)\rfloor\).

## Assumptions and scope
All alphabets are arbitrary finite sets of size at least two. Coordinates may have different alphabet sizes; no field, order, or probability measure on the symbols is used for the finite census. A cell fixes any chosen coordinates to individual symbols and leaves all other coordinates free; neither an empty cell nor a disjunction of cells is included. Shattering requires that all traces, including the empty trace, occur. The asymptotic statement concerns independent uniform samples with replacement, and conditions on no fixed growth rate for \(d_m\) except the stated critical-window relation.

## Proof
**Private-coordinate lemma.** Let \(S\subseteq X\) have \(m\ge3\) distinct points. Then \(S\) is shattered if and only if, for each \(x\in S\), there exists a coordinate \(i\) and symbols \(a\ne b\) such that \(x_i=b\) and \(y_i=a\) for every \(y\in S\setminus\{x\}\).

Necessity: the trace \(S\setminus\{x\}\) must be produced by some cell. The cell contains all other points but excludes \(x\), so at least one of its fixed coordinates is common to the other points and different at \(x\). Sufficiency: for a nonempty \(T\subseteq S\), fix, for each \(x\in S\setminus T\), one such coordinate to the symbol shared by \(S\setminus\{x\}\). All of \(T\) obey every condition, and each excluded \(x\) violates its own condition. Thus the resulting nonempty cell has trace exactly \(T\). In particular, \(X\) realizes \(S\). A single coordinate cannot privately distinguish two different rows when \(m\ge3\): if it did, the row private to either would have to share the other rows' symbol, contradicting distinct private symbols. Hence at least \(m\) coordinates are necessary and \(d\ge m\). Consequently \(Q\ge2^d\ge2^m>m\), so a singleton cell at a point outside \(S\) realizes the empty trace. This proves the lemma.

**Exact enumeration.** Temporarily label \(m\ge3\) rows and view a tuple of elements of \(X\) as a matrix with \(d\) columns. At coordinate \(i\), there are \(q_i^m\) column patterns. For a specified row there are exactly \(q_i(q_i-1)\) patterns in which it is the sole exceptional symbol and the other \(m-1\) rows agree. These pattern classes are pairwise disjoint for different rows. Thus, for any fixed set of \(j\) rows, exactly \(q_i^m-jq_i(q_i-1)\) patterns fail to mark all of these \(j\) rows as private. Independence across coordinates and inclusion–exclusion give the displayed ordered-tuple count. The private-coordinate condition already forces all rows to be distinct, so division by \(m!\) is valid and yields the formula.

For \(m=1\), all points are shattered because \(Q\ge2\). For \(m=2\), every distinct pair admits its two singleton traces and its full trace, and it has an empty trace precisely if a third point exists in \(X\). This establishes the low-degree cases. For \(d\ge3\) and \(m=d\), each coordinate must privately mark a different row, giving \(d!\prod_i q_i(q_i-1)\) ordered matrices, hence the leading coefficient. Such matrices exist because \(q_i\ge2\). This also proves the claimed VC-dimension cases.

**Critical window.** Let \(W_m\) count the sampled rows that lack a private coordinate. For \(m\ge3\), each coordinate privately marks row \(r\) with probability \(p_{m,i}\), and the marking events for different rows within the same coordinate are disjoint. Thus for every fixed positive integer \(k\),
\[
\mathbb E[(W_m)_k]=(m)_k\prod_{i=1}^{d_m}(1-kp_{m,i}),
\]
where \((u)_k\) is the falling factorial. For \(m\ge3\), \(p_{m,i}\le2^{1-m}\). The assumed relation implies \(\sum_i p_{m,i}^2\le2^{1-m}\mu_m=o(1)\). Expanding logarithms uniformly for fixed \(k\) gives
\[
\prod_i(1-kp_{m,i})=\exp(-k\mu_m+o(1))
=m^{-k}e^{-kc}(1+o(1)).
\]
Hence \(\mathbb E[(W_m)_k]\to e^{-kc}\) for each \(k\), establishing \(W_m\Rightarrow\mathrm{Poisson}(e^{-c})\) by the factorial-moment criterion. The critical relation also forces \(d_m\ge2^{m-1}(\log m+O(1))\), so \(|X_m|\ge2^{d_m}>m\) eventually. The lemma therefore identifies the sample-shattering event exactly with \(W_m=0\) for all sufficiently large \(m\), proving the asserted limit. For fixed \(q\), the stated choice of \(d_m\) ensures \(\mu_m=\log m+c+o(1)\).

## Verification
The standalone file `verify.py` enumerates every categorical cell and every candidate support of the reported small grids, checking shattering by all traces independently of the formula. On thirteen grids it checks 22,061 supports and exactly matches every reported coefficient through the stated sizes. Its output is recorded in `verification_output.txt`. In particular, the complete polynomial on the binary four-cube is \(1+16z+120z^2+160z^3+16z^4\); the mixed grid with sizes \((2,2,3)\) has \(1+12z+66z^2+24z^3\). Finite computations verify instances, not the asymptotic theorem or all-dimensional formula; those depend on the proof above.

## Relationship to prior work
Gopalan, Levin and Wieder (arXiv:1911.07378, first submitted November 18, 2019) study categorical subcubes as distributional anomaly detectors and analyze counts of *skewed cells*, not the number of point supports shattered by all cells. Their formal definition of coordinate-restricted subcubes motivates the object considered here. Paszke and Pilipczuk (arXiv:2003.14177) establish general VC-density bounds for logics definable in classes of graphs of bounded width; their theorem does not determine the finite coefficient sequence or the random critical window for these product cells. Gillibert, Lachmann and Müllner (arXiv:2004.13861) study continuous torus boxes, a different set system allowing interval restrictions rather than singleton categorical restrictions. No equivalent mixed-alphabet exact enumerator or critical-window theorem was identified in the searched literature. Absence of an identified match is not a proof of historical priority; another description under the language of conjunction classes or covering arrays could exist.

## Limitations
The result concerns unbounded-codimension categorical subcubes; it does not handle restricted-width conjunctions, arbitrary coordinate subsets, nonuniform coordinate sampling, or distributions with dependence between coordinates. The critical window assumes independent uniform sample entries. No independent scientific audit or comprehensive historical-priority certification has been performed. The proof is self-contained; finite checks do not certify arbitrary dimensions or infinite limits.

## References
1. P. Gopalan, R. Levin, and U. Wieder, *Finding Skewed Subcubes Under a Distribution*, arXiv:1911.07378 (2019), https://arxiv.org/abs/1911.07378.
2. A. Paszke and M. Pilipczuk, *VC Density of Set Systems Definable in Tree-Like Graphs*, arXiv:2003.14177 (2020), https://arxiv.org/abs/2003.14177.
3. P. Gillibert, T. Lachmann, and C. Müllner, *The VC-Dimension of Axis-Parallel Boxes on the Torus*, arXiv:2004.13861 (2020), https://arxiv.org/abs/2004.13861.
