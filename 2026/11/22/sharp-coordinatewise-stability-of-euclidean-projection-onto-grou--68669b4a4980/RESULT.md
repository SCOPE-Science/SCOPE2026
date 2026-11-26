# Sharp coordinatewise stability of Euclidean projection onto group-maximum balls

## Finding

Partition a finite real coordinate set into \(m\ge1\) nonempty blocks \(G_i\), with sizes \(d_i\). For \(R>0\), let \(P_R\) denote Euclidean projection onto \(K_R=\{x:\sum_i\|x_{G_i}\|_\infty\le R\}\). Measure input and output differences in the coordinate maximum norm. With sizes sorted as \(d_{(1)}\ge\cdots\ge d_{(m)}\), the sharp coefficient is
\[
\operatorname{Lip}_\infty(P_R)=
\begin{cases}
1,&1\le m\le2,\\
\displaystyle 1+\max_{2\le k\le m-1}\frac{k-1}{1+\sum_{j=1}^k d_{(j)}^{-1}},&m\ge3.
\end{cases}
\]
A pair of distinct finite inputs in a common open affine region attains the coefficient. Nonexpansivity in the coordinate maximum norm holds exactly when \(m\le2\). Sorting and a prefix scan give one \(O(m\log m)\) method to evaluate the formula.

For \(m\ge3\) equally sized blocks of size \(q\), the value is \(1+q(m-2)/(q+m-1)\) and approaches \(m-1\) as \(q\to\infty\). If all blocks are singletons, the value is \(2-2/m\) for \(m\ge2\) and \(1\) for \(m=1\). The radius does not enter the formula.

## Assumptions and scope

The groups are disjoint and cover the coordinates; distance in the projection problem is unweighted Euclidean distance. The perturbation norm is coordinatewise \(\ell_\infty\), not the mixed norm defining the target ball. At \(R=0\), excluded from the theorem, the map is zero. Overlapping or weighted groups are not covered.

## Proof

**Clipping formulation.** Sign symmetry reduces the local calculation to nonnegative inputs \(y\). For inputs in the ball the projection is the identity. Otherwise choose caps \(t_i\ge0\) with \(\sum_i t_i=R\). For fixed caps, the optimal output is \(x_{ij}=\min(y_{ij},t_i)\); the optimal caps minimize \(\frac12\sum_{i,j\in G_i}(y_{ij}-t_i)_+^2\). This follows by projecting onto the product of the cap boxes and minimizing over caps; the mixed norm is active outside the ball. In a strict exterior cell, the multiplier \(\lambda\) of the cap budget is positive. In an inactive block \(t_i=0\), the KKT inequality is \(\sum_{j\in G_i}y_{ij}\le\lambda\).

**Cell derivatives.** Let \(A\) consist of the groups with positive cap, \(r=|A|\), and set \(S_i=\{j\in G_i:y_{ij}>t_i\}\), \(k_i=|S_i|\ge1\) for \(i\in A\). In a cell where these sets are fixed and strict, stationarity gives
\[
 k_it_i=\sum_{j\in S_i}y_{ij}-\lambda,\quad H=\sum_{h\in A}k_h^{-1},\quad
 \lambda=\frac{\sum_{h\in A}k_h^{-1}\sum_{j\in S_h}y_{hj}-R}{H}.
\]
For a clipped output in group \(i\), the derivative with respect to any clipped input in group \(h\) is \(\mathbf1_{h=i}/k_i-1/(k_i k_h H)\); derivatives with respect to other inputs vanish. If \(r\ge2\), the row has nonnegative coefficients within \(S_i\) and negative coefficients in other clipped groups. Its absolute sum is \(1-1/(k_iH)+(r-1)/(k_iH)=1+(r-2)/(k_iH)\). When \(r=1\) it is zero. Unclipped active outputs have identity rows, and inactive output rows vanish. Fixed input signs conjugate the Jacobian by diagonal sign matrices and preserve row sums in absolute value.

These formulas bound the derivative on the dense open set of strict sign and clipping cells and the interior of the ball. Indeed the candidate cap and multiplier formulas are affine once the positive groups and strictly clipped coordinates are fixed, and their inactive, clipping and sign tests are linear; nontrivial equality tests lie in finitely many hyperplanes. In particular a clipped coordinate equality cannot be an identity in such a formula: \(\partial t_i/\partial y_{ij}<1\); an unclipped coordinate is not in the formula for its cap, and an inactive group is not in the multiplier. The ball is polyhedral and its Euclidean projector is continuous piecewise affine. Splitting a generic segment into cells proves the global bound from the maximal cell norm, and continuity extends it to arbitrary segments.

**Optimization.** For \(r\le2\), every row norm is at most one. For \(r\ge3\), fix a target group \(i\in A\). The denominator \(k_iH=1+\sum_{h\in A\setminus\{i\}} k_i/k_h\) is minimized by setting \(k_i=1\) and \(k_h=d_h\) for the other active groups. For \(k=r-1\le m-1\), choose the \(k\) largest blocks as those other groups; a distinct target group remains. This yields the displayed prefix formula as an upper bound.

**Sharpness.** For any such prefix choose these \(k\) groups and a distinct target, set each of their caps to \(R/(k+1)\), and choose \(\lambda>0\). In the target, give a single input coordinate value \(t_i+\lambda\) and put all others at zero. In another active group \(h\), give every input coordinate value \(t_h+\lambda/d_h\). Set inactive groups' inputs to zero. The KKT conditions hold with strict clipping and inactivity margins, and all active clipped inputs are positive. The affine formula persists on a full open neighborhood even if initially zero inputs change sign: the unclipped rows are identity and the inactive rows stay zero. Add a sufficiently small positive increment at the target clipped input and its negative at the other active clipped inputs. The target row realizes its absolute sum exactly as a finite-difference ratio. Maximizing the prefix gives the asserted attained coefficient. For \(m\le2\), a pair of distinct interior inputs realizes one.

**Special cases.** With equal sizes \(q\), the expression \(1+q(k-1)/(q+k)\) is strictly increasing in \(k\), giving the stated value at \(k=m-1\) for \(m\ge3\). For singleton blocks and \(m\ge3\), insert \(q=1\), so the value is \(2-2/m\); for \(m=2\) this agrees with the first case. For one singleton block the interval projector has coefficient one, not zero.

## Verification and prior work

The attached `checker.py` (Python 3 and NumPy) is supplementary. It compares exact rational face-pattern values with the prefix formula for 340 small block-size tuples and includes numerical finite-pair checks by bisection. The analytic argument covers all block sizes and radii; finite diagnostics do not establish it alone.

The cap and multiplier descriptions of the same mixed-norm ball are prior. The distinction is optimizing all coordinatewise row sums across the strict cells and exhibiting finite attaining pairs for general groups. In the singleton case the map and coefficient reduce to known cross-polytope thresholding and its centering rows. Dual mixed-norm proximal mapping via Moreau decomposition and a weighted \(\ell_1\)-epigraph projector are related but distinct sensitivity questions; firm nonexpansivity in Euclidean norm does not decide the coefficient here.

## References

- A. Quattoni, X. Carreras, M. Collins, T. Darrell, *An Efficient Projection for \(\ell_{1,\infty}\) Regularization*, ICML (2009), DOI 10.1145/1553374.1553484.
- D. Chau, B. Wohlberg, P. Rodriguez, arXiv:1806.10041.
- C. Chu, H. Zhang, J. Sun, R. Tao, *A Semismooth Newton Algorithm for Efficient Projections onto \(\ell_{1,\infty}\)-Norm Ball*, PMLR 119 (2020).
- G. Perez, L. Condat, M. Barlaud, arXiv:2307.09836.
- F. Béjar, I. Dokmanić, R. Vidal, *The Fastest \(\ell_{1,\infty}\) Prox in the West*, arXiv:1910.03749.
