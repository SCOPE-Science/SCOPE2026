# Inverse-block-size balancing and exact deep holes of synchronized parity-code polytopes

## Finding
Let \(r\ge3\), let \(q_1,\ldots,q_r\) be positive integers, and partition the coordinates of \(\mathbb R^n\), \(n=\sum_jq_j\), into nonempty blocks \(B_1,\ldots,B_r\) of those sizes. Let \(C_{\mathbf q}\subseteq\{0,1\}^n\) consist of exactly those binary vectors whose coordinate sums in all \(r\) blocks have **the same parity**, and put \(P_{\mathbf q}=\operatorname{conv}(C_{\mathbf q})\). This is the codeword polytope of the binary repetition code pulled back through the block parity maps, not a Cartesian product of independent parity polytopes.

Put \(w_j=1/q_j\), \(S=\sum_{j=1}^r w_j\), and \(W_T=\sum_{j\in T}w_j\) for \(T\subseteq[r]\). With the ordinary Euclidean metric on \(\mathbb R^n\), the **exact Hausdorff distance** is
\[
 d_H([0,1]^n,P_{\mathbf q})^2
 =\max_{\varnothing\ne T\subsetneqq[r]}\frac{W_T(S-W_T)}S
 =\frac S4-\frac1S\min_{T\subseteq[r]}\left(W_T-\frac S2\right)^2.
\]
The empty or full subset never minimizes the displayed squared imbalance when \(r\ge3\), since any positive proper subset improves upon either. Thus either maximum can be taken over nonempty proper subsets.

For a cube vertex \(x\), let \(T=T(x)\) be its set of blocks having odd coordinate sum. If \(T\) is empty or full, then \(x\in P_{\mathbf q}\). Otherwise the squared distance is exactly \(W_T(S-W_T)/S\), and its **unique** closest point \(\pi(x)\in P_{\mathbf q}\) is given coordinatewise by
\[
 \pi(x)_i=x_i+(1-2x_i)\delta_j\quad(i\in B_j),\qquad
 \delta_j=\begin{cases}
 (S-W_T)/(S q_j),&j\in T,\\
 W_T/(S q_j),&j\notin T.
 \end{cases}
\]
All farthest points of the **entire cube** are vertices, exactly those with \(T(x)\) minimizing \(\lvert W_T-S/2\rvert\). If \(\mathcal T\) denotes the collection of such parity patterns, their number is exactly \(2^{n-r}|\mathcal T|\). No nonvertex point is farthest.

For \(r\) equally sized blocks, \(q_j=q\), the squared distance and farthest-vertex count simplify to
\[
 d_H^2=\frac{\lfloor r^2/4\rfloor}{rq},\qquad
 \#\mathrm{farthest}=2^{r(q-1)}\begin{cases}
 \binom r{r/2},&r\text{ even},\\
 2\binom r{(r-1)/2},&r\text{ odd}.
 \end{cases}
\]
In contrast, the Cartesian product of the \(r\) independent even-parity block polytopes has squared Hausdorff distance \(r/q\) from the same cube. Thus synchronizing all block parities reduces squared worst-case error to \(\lfloor r^2/4\rfloor/r^2\) of that independent-block benchmark, approaching a factor of \(1/4\).

If a block \(i\) satisfies \(w_i\ge S/2\), the only farthest parity patterns are \(\{i\}\) and its complement. Thus at this sharp sufficient dominance threshold the deepest cube vertices localize to precisely two parity-pattern classes, rather than to the balanced many-pattern families of equal-sized blocks.

## Assumptions and scope
All block sizes are positive integers; the genuinely high-dimensional case \(q_j\ge2\) for every block is included. The polytope is the **convex hull of all codewords satisfying simultaneous parity equalities**; it is not the intersection of individual single-check parity-polytope relaxations unless that intersection happens to be integral. The distance is ambient \(\ell_2\) Hausdorff distance, with the natural unscaled cube coordinates. The claim concerns this explicitly defined code family, not arbitrary binary linear codes or all points' nearest-codeword (Hamming) decoding.

## Proof
**1. Reduce a cube vertex to a two-slice parity coset.** Fix a binary cube vertex \(x\). Coordinate reflections \(z_i\mapsto|z_i-x_i|\) form a Euclidean isometry sending \(x\) to zero and \(C_{\mathbf q}\) to a set \(D_x\). Let \(T\) be the odd-block set of \(x\). Every vector in \(D_x\) has within-block parity pattern either the indicator of \(T\), or the indicator of its complement: the original codeword has either even parity in every block or odd parity in every block. Write these two nonempty binary sets as \(D_T\) and \(D_{T^c}\). The formula is trivial when \(T=\varnothing\) or \(T=[r]\), since then \(x\) itself is a codeword. Hence assume \(\varnothing\ne T\subsetneqq[r]\).

**2. Universal lower bound.** Any point \(y\in\operatorname{conv}(D_x)\) can be written as \(\lambda u+(1-\lambda)v\) with \(0\le\lambda\le1\), \(u\in\operatorname{conv}(D_T)\), and \(v\in\operatorname{conv}(D_{T^c})\). In every binary vector in \(D_T\), a block in \(T\) has at least one flipped bit. Consequently \(\sum_{i\in B_j}y_i\ge\lambda\) for \(j\in T\). Similarly \(\sum_{i\in B_j}y_i\ge1-\lambda\) for \(j\notin T\). All \(y_i\) are nonnegative. Cauchy--Schwarz in each block yields
\[
 \|y\|_2^2\ge\sum_j\frac{(\sum_{i\in B_j}y_i)^2}{q_j}
 \ge\lambda^2W_T+(1-\lambda)^2(S-W_T).
\]
The right side has its unique minimum at \(\lambda_*=(S-W_T)/S\), with minimum \(W_T(S-W_T)/S\).

**3. Exact construction and unique projection.** Within each block in \(T\), uniformly choose exactly one coordinate to flip, independently across blocks, and flip nothing elsewhere. The mean of these binary vectors belongs to \(\operatorname{conv}(D_T)\) and has coordinates \(1/q_j\) in the prescribed odd blocks and zero elsewhere. Do the complementary construction for \(D_{T^c}\), and combine their means with weights \(\lambda_*\) and \(1-\lambda_*\). This produces \(y_*\in\operatorname{conv}(D_x)\) with coordinate values \(\lambda_*/q_j\) in blocks \(T\) and \((1-\lambda_*)/q_j\) elsewhere; equality holds in both lower bounds. Therefore \(y_*\) is the Euclidean projection of zero. Uniqueness follows from strict convexity of squared Euclidean norm on a convex set. Undoing the coordinate reflections gives the stated \(\pi(x)\), its uniqueness and the vertex distance formula.

**4. From cube vertices to the whole cube.** Squared distance to any nonempty closed convex set is a convex function. Hence its maximum over the cube is achieved at a binary vertex. To rule out *additional nonvertex maximizers*, write any cube point as a convex combination \(z=\sum_a\theta_av_a\) of binary vertices and let \(p_a\) be their unique projections onto \(P_{\mathbf q}\). Convexity of \(P_{\mathbf q}\) and the Hilbert-space variance identity give
\[
 \operatorname{dist}(z,P_{\mathbf q})^2
 \le\left\|\sum_a\theta_a(v_a-p_a)\right\|^2
 =\sum_a\theta_a\|v_a-p_a\|^2
 -\sum_{a<b}\theta_a\theta_b\|(v_a-p_a)-(v_b-p_b)\|^2.
\]
For a noncode binary vertex, every coordinate of its residual \(v_a-p_a\) is nonzero, with positive sign at a \(1\)-coordinate and negative sign at a \(0\)-coordinate, by the strict positivity of both reciprocal-weight portions in Step 3. Distinct noncode vertices differ in some bit, so their residual vectors differ. Code vertices have zero residual and cannot be farthest since the Hausdorff distance is positive. Therefore a convex combination of two or more distinct vertices has strictly submaximal distance; every farthest point is a cube vertex.

**5. Arithmetic optimization and counts.** The vertex formula is \(W_T(S-W_T)/S=S/4-(W_T-S/2)^2/S\), so the worst cosets are precisely the reciprocal-block-weight subsets nearest half of \(S\). Every parity pattern occurs at exactly \(\prod_j2^{q_j-1}=2^{n-r}\) binary vertices. This proves the general counting formula. For equal sizes, \(W_T=|T|/q\), and integer maximization of \(|T|(r-|T|)\) proves the displayed formulas and equality cases. For independent even-parity blocks, each odd block has projection squared distance \(1/q\) (the same one-bit averaging argument), and Cartesian-product squared distances add. If \(w_i\ge S/2\), among all subset weights the closest possible to \(S/2\) are uniquely \(w_i\) and \(S-w_i\), establishing the stated localized regime.

## Verification
The standalone standard-library script `verify_block_parity.py` computes exact rational projections, checks their normal-cone optimality inequalities against every codeword for ten small parameter vectors, verifies the extremal parity balance and vertex counts, and prints `PARITY_BLOCK_HAUSDORFF_KKT_PASS`. A second, independent convex-combination quadratic-programming implementation `verify_qp.py` uses NumPy and SciPy to optimize over codeword barycentric coefficients at all violating cube vertices in four configurations and prints `PARITY_BLOCK_INDEPENDENT_QP_PASS`. The complete tested configurations, finite scope and numeric tolerances are in `VERIFICATION.md`. Neither finite verification constitutes the all-parameter proof: the proof is the five-step exact argument above.

## Relationship to prior work
Ermel--Walter (2018) study the *single global even-parity* polytope with within-block ordering constraints, giving its extended formulation and linear inequality description. That is not the simultaneous equality of **unconstrained block parities** used here. Gensheimer--Dietz--Kraft--Ruzika--Wehn (2019) give an efficient projection algorithm for a *single-check* even/odd parity polytope, not the exact ambient cube-to-multicheck-codeword-polytope Hausdorff radius or farthest-vertex spectrum. For \(r=2\), equal block parities are equivalent to a single global even-parity check and the squared radius simplifies to the familiar \(1/n\); the new phenomenon is the \(r\ge3\) simultaneous-check case and the inverse-block-size arithmetic balancing law. Related later work on demihypercubes likewise concerns single parity rather than the multi-block coupling. Searches did not identify a prior theorem implying the displayed general distance, extremizers, and explicit projections; this does not establish historical priority.

## Limitations
This is a self-contained mathematical proof with finite corroboration, not independent external validation. Priority under other terminology (codeword polytope, repeated parity checking, block-syndrome hull, or Euclidean convex-hull decoding) remains a residual bibliographic risk. No hardness result for the subset-balancing step, general binary-code extension, or claim about other norms is made. The source date below is the first public posting of the motivating 2018 paper, not a claimed publication date for this finding.

## References
1. D. Ermel and M. Walter, *Parity Polytopes and Binarization*, arXiv:1803.10561v1, first publicly submitted 2018-03-28; see especially Sections 1--4 of the open arXiv HTML version, https://arxiv.org/html/1803.10561v2 .
2. F. Gensheimer, T. Dietz, K. Kraft, S. Ruzika and N. Wehn, *A Reduced-Complexity Projection Algorithm for ADMM-based LP Decoding*, arXiv:1901.03240v1, first publicly submitted 2019-01-10; Sections IV--VIII address projections onto even/odd single-parity polytopes, https://arxiv.org/abs/1901.03240 .
