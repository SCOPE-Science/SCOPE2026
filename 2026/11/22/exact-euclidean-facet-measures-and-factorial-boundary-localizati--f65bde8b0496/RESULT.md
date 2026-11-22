# Exact Euclidean facet measures and factorial boundary localization for cube–simplex Cayley polytopes

## Finding
For each integer \(n\ge 2\), let \(Q_n=[0,1]^n\), \(\Delta_n=\operatorname{conv}(0,e_1,\ldots,e_n)\), and define the full-dimensional Euclidean Cayley polytope
\[
C_n=\operatorname{conv}\bigl((Q_n,0)\cup(\Delta_n,1)\bigr)\subset\mathbb R^{n+1}.
\]
Let \(S_n=\mathcal H^n(\partial C_n)\) be its intrinsic Euclidean boundary measure and \(V_n=\operatorname{Vol}_{n+1}(C_n)\). Its \(2^n+n+1\) facets, including all exact Euclidean \(n\)-dimensional areas, are as follows:

* The lower height facet \(t=0\) has area \(1\); the upper height facet \(t=1\) has area \(1/n!\).
* Each of the \(n\) coordinate facets \(x_i=0\) has area \(\frac1n\sum_{j=0}^{n-1}1/j!\).
* For each nonempty \(S\subseteq[n]\) of size \(k\), the facet \(\sum_{i\in S}x_i+(k-1)t=k\) has area
\[
A_{n,k}=\sqrt{k^2-k+1}\,\frac{(n-k)!}{n!}.
\]

Writing \(E_r=\sum_{j=0}^{r}1/j!\) and \(a_k=\sqrt{k^2-k+1}/k!\), the total boundary area and volume are
\[
\boxed{S_n=1+\frac1{n!}+E_{n-1}+\sum_{k=1}^{n}a_k,\qquad V_n=\frac{E_n}{n+1}.}
\]
The volume identity is included as a normalization and is a specialization of a preexisting Cayley-polytope normalized-volume result; novelty is claimed only for the Euclidean facet-area spectrum and its boundary consequences.

There is a strict and rapidly convergent dimension law:
\[
S_{n+1}-S_n=\frac{1+\sqrt{n^2+n+1}}{(n+1)!}>0,
\qquad S_n\nearrow S_\infty=1+e+\sum_{k=1}^{\infty}a_k
=6.222933015013\ldots,
\]
with \(S_\infty-S_n\sim 1/n!\).

If a facet is selected with probability proportional to its Euclidean area, the limiting probabilities of the lower height facet, the collection of all coordinate facets, and the collection of size-\(k\) subset facets are respectively
\[
\frac1{S_\infty},\qquad \frac{e}{S_\infty},\qquad \frac{a_k}{S_\infty}\ (k\ge1).
\]
The upper height facet receives vanishing mass. More precisely, at finite \(n\) the four facet-family probability assignments are exactly \(1/S_n\) (bottom), \(1/(n!S_n)\) (top), \(E_{n-1}/S_n\) (all coordinate facets), and \(a_k/S_n\) for each subset rank \(1\) through \(n\). The subset-rank law is tight with factorial tail: for each integer \(1\le K<n\), the total area of subset facets above rank \(K\), divided by \(S_n\), is at most \(S_n^{-1}\sum_{j=K}^{\infty}1/j!\). This contrasts with the uniformly counted subset facet, whose rank is asymptotic to \(n/2\). In particular, for every \(\varepsilon>0\), there is a fixed \(K\) such that at most \(1+n+\sum_{k=1}^{K}\binom nk=O_K(n^K)\) of the \(2^n+n+1\) facets carry a limiting fraction greater than \(1-\varepsilon\) of the total Euclidean boundary area.

## Assumptions and scope
Coordinates \((x_1,\ldots,x_n,t)\) carry the *standard*, unrescaled Euclidean metric. The statements concern all integers \(n\ge2\), ordinary Hausdorff facet measure, and the exact two-layer Cayley placement at heights \(0\) and \(1\). An arbitrary affine or unimodular transformation need not preserve any of the stated Euclidean areas. The results are not claims about arbitrary Cayley sums, unequal cube side lengths, or differently positioned simplices.

## Proof
**1. Facet description.** The horizontal slice at height \(t\in[0,1]\) is
\[
C_n(t)=(1-t)Q_n+t\Delta_n.
\]
For \(a=1-t\ge0\) and \(b=t\ge0\), a point \(x\) lies in \(aQ_n+b\Delta_n\) exactly when \(x_i\ge0\) for all \(i\) and \(\sum_i(x_i-a)_+\le b\): choose the cube part \(y_i=\min(x_i,a)\), leaving \((x_i-a)_+\) for the simplex part. The positive-part sum equals \(\max_{S\subseteq[n]}\sum_{i\in S}(x_i-a)\). This proves the full inequality description
\[
0\le t\le1,\quad x_i\ge0,\quad
\sum_{i\in S}x_i+(|S|-1)t\le |S|\quad (\varnothing\ne S\subseteq[n]).
\]
No listed hyperplane is redundant: both height slices are \(n\)-dimensional; on \(x_i=0\), the nontrivial horizontal slices are \((n-1)\)-dimensional; and for \(|S|=k\), the supporting slice is the Cartesian product of a \((k-1)\)-simplex (in the \(S\) coordinates) and an \((n-k)\)-cube (in its complement). Its dimension is \(n-1\), and varying \(t\) supplies one additional independent dimension. Thus every listed inequality defines a distinct facet and the displayed list is exhaustive.

**2. Volume and coordinate facets.** Partition \(aQ_n+b\Delta_n\) according to the set of coordinates exceeding \(a\). If exactly \(j\) coordinates exceed \(a\), the excess vector lies in a \(j\)-simplex of volume \(b^j/j!\), while the remaining \(n-j\) coordinates each have interval length \(a\). Consequently,
\[
\operatorname{Vol}_n(aQ_n+b\Delta_n)
=\sum_{j=0}^{n}\binom nj a^{n-j}\frac{b^j}{j!}.
\]
Integrating at \(a=1-t,b=t\) and using the beta integral gives \(V_n=E_n/(n+1)\). The facet \(x_i=0\) is isometric to the dimension-\(n\) Cayley polytope \(C_{n-1}\), so its area is \(E_{n-1}/n\). The height facets have the stated cube and simplex volumes.

**3. Every subset facet.** Fix \(S\ne\varnothing\), \(k=|S|\). At a fixed interior height \(t\), its \((n-1)\)-dimensional slice is the orthogonal product
\[
\bigl((1-t)\mathbf 1_S+t\operatorname{conv}\{e_i:i\in S\}\bigr)
\times (1-t)[0,1]^{n-k}.
\]
The regular \((k-1)\)-simplex spanned by coordinate vectors has volume \(\sqrt{k}/(k-1)!\); hence this slice has area \(\frac{\sqrt{k}}{(k-1)!}t^{k-1}(1-t)^{n-k}\). In the facet hyperplane with normal \(N_S=(\mathbf 1_S,k-1)\), the tangential gradient of \(t\) has norm
\[
\lVert\nabla_{F_S}t\rVert=\sqrt{\frac{k}{k^2-k+1}}.
\]
The coarea formula therefore yields
\[
\mathcal H^n(F_S)
=\frac{\sqrt{k^2-k+1}}{(k-1)!}
\int_0^1 t^{k-1}(1-t)^{n-k}\,dt
=\sqrt{k^2-k+1}\frac{(n-k)!}{n!}.
\]
For each fixed \(k\), there are \(\binom nk\) such facets, so their **combined** area is exactly \(a_k\), independent of \(n\) once \(n\ge k\). Summing the four facet families proves the formula for \(S_n\).

**4. Boundary concentration.** Subtraction of successive exact expressions gives the strict increment formula. Since \(\sqrt{k^2-k+1}\le k\), the series \(\sum_{k\ge1}a_k\) converges with tail bounded by \(\sum_{j\ge K}1/j!\), proving factorial tightness of the subset-rank boundary measure. The exact layer weights converge to the claimed atoms. The tail after the \(n\)-th boundary area satisfies
\[
S_\infty-S_n=\sum_{r=n}^{\infty}\frac{1+\sqrt{r^2+r+1}}{(r+1)!}\sim\frac1{n!},
\]
as the first summand dominates the remaining factorial tail. Among the \(2^n-1\) subset facets, a uniformly counted subset has cardinality distributed as \(\operatorname{Binomial}(n,1/2)\) conditioned to be positive; its rank divided by \(n\) converges in probability to \(1/2\), unlike area-weighted rank. For fixed \(K\), including the bottom and all \(n\) coordinate facets plus the subset facets of rank at most \(K\) gives limiting area proportion
\[
\frac{1+e+\sum_{k=1}^K a_k}{S_\infty}.
\]
This tends to one as \(K\to\infty\), while the number of retained facets is only polynomial in \(n\) for fixed \(K\).

## Verification
The attached `check.py` constructs the genuine vertices of \(C_n\), independently computes convex hulls and their Euclidean surface measures using SciPy/Qhull for \(1\le n\le6\), matches each computed supporting hyperplane against the exact facet description, and checks volume and surface-area formulas. It completed with `CAYLEY_CUBE_SIMPLEX_HULL_FACET_AREA_PASS`. These are finite diagnostic checks, not a replacement for the all-dimensional proof above. A separate direct symbolic beta-integral reduction proves the volume; the coarea argument proves all facet areas.

## Relationship to prior work
Hibi, Ohsugi and Tsuchiya (arXiv:1807.05989; first posted 2018-07-16) established regular unimodular triangulations, integer decomposition and a general normalized-volume framework for Cayley sums of order and stable-set polytopes. Their Corollary 4.2 covers the normalized volume here after identifying the cube as the order polytope of an antichain and the simplex as the stable-set polytope of a complete graph (equivalently, the chain polytope of a total order); thus the volume is expressly **not** claimed original. Their work does not state the native-coordinate Euclidean area of every lateral facet or the factorial boundary-area localization. Other indexed results concerning geometric facet-area concentration address different polytope families and do not imply the particular facet coarea identity here. Exact historical priority beyond the located sources remains uncertain.

## Limitations
The result is metric: deforming the embedding changes the areas. The area-weighted limiting law concerns the facet supporting a boundary-uniform point, not uniformly sampled facets. The numerical checker covers only \(n\le6\); all-\(n\) validity rests on the explicit facet and coarea proof. The literature search cannot exclude a previously unindexed equivalent computation. No independent external mathematical audit has been performed.

## References
1. T. Hibi, H. Ohsugi and A. Tsuchiya, *Integer decomposition property for Cayley sums of order and stable set polytopes*, arXiv:1807.05989 (initial public version 2018-07-16), https://arxiv.org/abs/1807.05989. In particular Theorem 0.4, Corollary 4.2 and Section 6.
2. Standard simplex-volume, beta-integral and polyhedral coarea identities, used explicitly and proved or specialized in the steps above. MSC2020 code `52B11` denotes \(n\)-dimensional polytopes: https://mathscinet.ams.org/msc/msc2020.html?t=52B99.
