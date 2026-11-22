# Sharp weighted-variation Lipschitz constant of finite-chain isotonic regression

## Finding
Let \(n\ge2\). Choose positive observation masses \(a_1,\ldots,a_n\) and positive edge-variation weights \(w_1,\ldots,w_{n-1}\). Let \(P_a\) be weighted least-squares projection onto the cone of nondecreasing real sequences, and let
\[
 V_w(h)=\sum_{i=1}^{n-1}w_i|h_{i+1}-h_i|.
\]
Set \(Q_0=0\), \(Q_j=\sum_{k=1}^{j}a_k\), \(w_0=w_n=0\). Let \(\widehat w\) be the least concave majorant of the finite points \((Q_i,w_i)\), linearly interpolated across the interval \([0,Q_n]\). Then the exact two-input coefficient is
\[
 \boxed{\sup_{y,z:\,V_w(y-z)>0}\frac{V_w(P_a(y)-P_a(z))}{V_w(y-z)}
 =\max_{1\le i<n}\frac{\widehat w(Q_i)}{w_i}.}
\]
In particular, the projection is nonexpansive in \(V_w\) exactly when the weights are concave with respect to cumulative observation masses, i.e.
\[
 \frac{w_i-w_{i-1}}{a_i}\ge\frac{w_{i+1}-w_i}{a_{i+1}}
 \quad(1\le i<n).
\]
All constants are attained locally by arbitrarily close inputs. The bound can be arbitrarily large, even at four observations.

## Assumptions and scope
The observations and fitted values are arbitrary real vectors of length \(n\). All observation masses and all interior edge weights are strictly positive. The fitted vector is the unique minimizer
\[
 P_a(y)=\operatorname*{argmin}_{x_1\le\cdots\le x_n}
 \frac12\sum_{j=1}^n a_j(x_j-y_j)^2.
\]
Both inputs and output differences are measured by the same weighted *edge total-variation seminorm* \(V_w\), which vanishes only for constant vectors. The map \(P_a\) is translation-equivariant, so input differences of zero variation also give zero output variation. Its metric is weighted Euclidean, but the claimed stability metric is the unrelated weighted variation seminorm.

For direct computation, the concave-majorant ordinate can be written without constructing a hull:
\[
 \widehat w(Q_i)=\max_{\substack{0\le p\le i\le q\le n\\p<q}}
 \left(\frac{Q_q-Q_i}{Q_q-Q_p}w_p+
 \frac{Q_i-Q_p}{Q_q-Q_p}w_q\right).
\]
The conventions \(w_0=w_n=0\) matter for boundary pooling. Chords with \(p=i\) or \(q=i\) include the original ordinate.

## Proof
**1. Linear cells.** The weighted isotonic projector is continuous and piecewise linear. In every full-dimensional active-set cell, its derivative \(E_{\mathcal B}\) averages coordinates over each block of some partition \(\mathcal B\) into contiguous intervals, weighted by \(a_j\). Explicitly, for a block \([l,r]\),
\[
 (E_{\mathcal B}h)_j=\frac{\sum_{k=l}^r a_kh_k}{\sum_{k=l}^ra_k}
 \quad(l\le j\le r).
\]
This follows directly from the first-order conditions on a fixed set of active order equalities. Every contiguous-block partition occurs on an open cell: choose data strictly decreasing inside each nonsingleton block, with prescribed block means increasing strictly and separated by sufficiently large gaps. Strict complementarity of the active inequalities and strict slackness across blocks then persist under small perturbations. In a block with strictly decreasing data, every proper prefix weighted mean exceeds the full-block mean, giving strictly positive active multipliers.

**2. Sharp linear-piece norms.** Put \(s^{(i)}_j=\mathbf 1_{\{j>i\}}\) for \(1\le i<n\). Each vector \(h\) has the decomposition
\[
 h=h_1\mathbf1+\sum_{i=1}^{n-1}(h_{i+1}-h_i)s^{(i)}.
\]
Since \(E_{\mathcal B}\mathbf1=\mathbf1\), the triangle inequality shows
\[
 \|E_{\mathcal B}\|_{V_w\to V_w}
 =\max_{1\le i<n}\frac{V_w(E_{\mathcal B}s^{(i)})}{w_i};
\]
the reverse inequality follows by testing a single step \(s^{(i)}\), whose input variation is exactly \(w_i\).

If edge \(i\) separates two blocks, \(E_{\mathcal B}s^{(i)}=s^{(i)}\), so its output variation is \(w_i\). Otherwise edge \(i\) is strictly inside a pooled block \([l,r]\) with \(l\le i<r\). Write \(A_L=\sum_{k=l}^{i}a_k\), \(A_R=\sum_{k=i+1}^{r}a_k\). The step's block average is \(A_R/(A_L+A_R)\); all preceding blocks have value zero and succeeding blocks have value one. Therefore the only possibly nonzero output jumps are at the two outer boundaries, giving
\[
 V_w(E_{\mathcal B}s^{(i)})
 =\frac{A_Rw_{l-1}+A_Lw_r}{A_L+A_R}
 =\frac{(Q_r-Q_i)w_{l-1}+(Q_i-Q_{l-1})w_r}{Q_r-Q_{l-1}}.
\]
If \(l=1\) or \(r=n\), the corresponding nonexistent outside edge contributes the zero endpoint weight. Hence every linear-piece norm is bounded by the displayed chord maximum.

**3. Every chord is sharp.** For any \(0\le p\le i\le q\le n\) with \(p<q\), when \(p<i<q\), use the contiguous partition whose only nonsingleton block is \([p+1,q]\), and whose other vertices are singletons. The test step \(s^{(i)}\) produces exactly the chord between \((Q_p,w_p)\) and \((Q_q,w_q)\). For \(p=i\) or \(q=i\), the chord equals \(w_i\), achieved by the all-singleton partition. By Step 1 these partitions are realized on open cells, and perturbations in their step directions approach or attain the stated ratio. Thus the supremum across all linear-piece norms is precisely the chord maximum.

**4. Globalization.** The line segment connecting any two data vectors intersects finitely many polyhedral cells, and the isotonic projector is continuous and piecewise affine along the segment. Summing its linear variations on those subsegments and using the triangle inequality yields the bound with the maximal derivative coefficient. The local sharpness of Step 3 supplies the reverse bound. Finally, the least concave majorant ordinate at each \(Q_i\) equals the maximum interpolated chord ordinate containing that abscissa (upper hull of finitely many planar points). Therefore the chord formula is exactly \(\max_i\widehat w(Q_i)/w_i\).

The coefficient is one if and only if every original weight ordinate already equals its least concave majorant, which is equivalent to the displayed adjacent secant-slope inequalities. This proves all assertions.

## Verification
The standalone standard-library `verify.py` performs exact-rational checks. It enumerates all contiguous partitions for \(2\le n\le7\), several nonconstant positive observation-mass and variation-weight profiles, computes the actual step responses of each weighted averaging operator, and compares their largest quotient with the finite chord formula. It also compares the concavity criterion and performs independent weighted-PAVA perturbation tests, including perturbations that change pooling regimes. It passes 8,680 exact-rational comparisons under Python 3.

For an explicit sharp example, let \(n=4\), all observation masses equal one, and variation weights \((1,1/4,1)\). Then \(\widehat w(Q_2)=1\), while \(w_2=1/4\), hence the coefficient is \(4\). Set \(y=(0,3,1,5)\) and \(z=(0,3,3/2,11/2)\). Their isotonic projections are respectively \((0,2,2,5)\) and \((0,9/4,9/4,11/2)\). Direct substitution gives
\[
 V_w(P_a(z)-P_a(y))=\frac12,
 \qquad V_w(z-y)=\frac18.
\]
The exact quotient is four. The checker is corroborative; the all-dimensional theorem follows from Steps 1–4.

## Relationship to prior work
Yang and Barber (2017), Theorem 1, give a necessary-and-sufficient neighbor-averaging criterion (NUNA) for *unit-observation-mass* isotonic projection to be contractive in a given seminorm. Its implication of a criterion for \(V_w\)-nonexpansivity with uniform observation masses is prior, not claimed as new. The present result instead computes the **exact best coefficient even when it exceeds one**, for **arbitrary independent positive observation masses and edge-variation weights**, with a closed concave-majorant formula and matching witnesses. NUNA alone neither states that coefficient nor treats the heterogeneous-mass averaging geometry in its theorem.

Chen, Li and Su (2023) study an active-set method for generalized convex isotonic regression on directed trees; the chain quadratic model is a special case of their optimization setting. Their paper treats algorithmic structure, not the stated exact two-input variation modulus. A related published result on isotonic projections for posets with a *cycle* as their undirected Hasse cover graph establishes rigidity of nonexpansivity to uniform variation weights, but it has no chain chord formula and its cover topology excludes the present path. The published \(\ell_p\)-isotonic stability result uses a different seminorm and cannot give the claimed coefficient by implication alone.

## Limitations
The theorem concerns finite chains with strictly positive masses and interior weights, quadratic least-squares isotonic regression, and real scalar data. It does not assert sharp constants for general posets, weighted projections with vanishing masses, or other loss functions. The equality is for a two-input *seminorm* and cannot be interpreted as a coordinatewise or Euclidean operator norm. Source inspection and semantic searches cannot establish absolute historical novelty; older order-restricted inference literature could express the same sharp chord law implicitly. Independent mathematical validation has not occurred.

## References
- F. Yang and R. Foygel Barber, *Contraction and uniform convergence of isotonic regression*, arXiv:1706.01852 (first public June 6, 2017), Theorem 1 and Section 6, https://arxiv.org/html/1706.01852v3.
- X. Chen, X. Li and Y. Su, *An active-set based recursive approach for solving convex isotonic regression with generalized order restrictions*, arXiv:2304.00244 (first public April 1, 2023), https://arxiv.org/abs/2304.00244.
- *Cyclic-cover rigidity of weighted-variation stability for isotonic regression*, published research result, November 2, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-cyclic-cover-rigidity-of-weighted-variation-stability-for-isoton--c6a0693fe803.
