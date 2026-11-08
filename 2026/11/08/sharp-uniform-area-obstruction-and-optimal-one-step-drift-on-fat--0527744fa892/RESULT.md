# Sharp uniform-area obstruction and optimal one-step drift on fat Sierpinski triangles

## Finding
Let \(P\) be the position Markov operator of the random fat-Sierpinski \(\beta\)-transformation described below and let \(\lambda_\beta\) be normalized area on its triangular attractor. The following conclusions hold:

1. For every \(1<\beta\le3/2\), every binary overlap probability \(p\in(0,1)\), and every triple-overlap probability vector \((s,t,u)\) with positive entries summing to one, \(P\lambda_\beta\ne\lambda_\beta\). Thus its existing absolutely continuous stationary law is never the constant-density law.
2. At the geometrically distinguished parameter \(\beta=\sqrt2\),
\[
\min_{0<p<1,\ s,t,u>0,\ s+t+u=1}
\|P\lambda_{\sqrt2}-\lambda_{\sqrt2}\|_{\mathrm{TV}}
=17-12\sqrt2.
\]
The complete set of minimizers is \(p=1/2\) with *arbitrary* positive triple-coin weights \((s,t,u)\).
3. Every stationary position probability measure \(\mu\) for the same \(\beta=\sqrt2\) system satisfies
\[
\|\mu-\lambda_{\sqrt2}\|_{\mathrm{TV}}\ge \frac{17-12\sqrt2}{2}.
\]
The third conclusion is a lower bound, not an assertion of sharp stationary-measure separation.

## Assumptions and scope
For \(1<\beta\le3/2\), put \(L=1/(\beta-1)\) and
\[\Delta_\beta=\{(x,y):x\ge0,\ y\ge0,\ x+y\le L\}.\]
Its normalized planar Lebesgue probability is \(\lambda_\beta\), with \(\operatorname{area}(\Delta_\beta)=L^2/2\). Write \(q_0=(0,0)\), \(q_1=(1,0)\), \(q_2=(0,1)\). At \(z\in\Delta_\beta\), a digit \(i\in\{0,1,2\}\) is admissible when \(\beta z-q_i\in\Delta_\beta\). If exactly one digit is admissible it is chosen; if exactly two are admissible, choose the smaller index with probability \(p\) and the larger with probability \(1-p\); if all three are admissible, choose digits \(0,1,2\) with probabilities \(s,t,u\), respectively. The next position is \(\beta z-q_i\). Assume \(0<p<1\), \(s,t,u>0\), \(s+t+u=1\). Boundary tie-breaking does not affect any absolutely continuous measure. Set \(P\nu\) to be the resulting one-step distribution from initial law \(\nu\). Our convention is \(\|\mu-\nu\|_{\mathrm{TV}}=\sup_B|\mu(B)-\nu(B)|\).

This is the position process underlying the random \(\beta\)-transformation of Zhang, Dajani and Li, rather than a claim about the product-coin shift as a different measure space. The initial position is exactly normalized area and independent of the coins.

## Proof
**Transfer density.** For each \(w=(x,y)\in\Delta_\beta\), all three points \(z_i=(w+q_i)/\beta\) lie in \(\Delta_\beta\). The probability of selecting digit \(i\) from \(z_i\) is denoted by \(c_i(w)\). Every branch has determinant \(\beta^2\); therefore
\[
\frac{d(P\lambda_\beta)}{d\lambda_\beta}(w)
=\frac{K(w)}{\beta^2},\qquad K(w)=\sum_{i=0}^2c_i(w).
\]
At \(z_i\), digit \(j\) is admissible exactly when \(w+q_i-q_j\in\Delta_\beta\). Thus the inverse-branch admissibility is determined by the signs of \(x-1\), \(y-1\), and \(x+y-(L-1)\); no unproved ergodicity assertion is involved.

**Global noninvariance.** The open triangle near \((0,0)\) where \(x<1\), \(y<1\), and \(x+y<L-1\) has
\[K(w)=1+(1-p)+(1-p)=3-2p.\]
The open triangle near the upper vertex \((0,L)\) where \(x<1\), \(y>1\), and \(x+y>L-1\) has
\[K(w)=p+p+1=1+2p.\]
Both regions have positive area throughout \(1<\beta\le3/2\). If normalized area were stationary, then the density would be one almost everywhere, forcing \(3-2p=\beta^2=1+2p\), whence \(p=1/2\) and \(\beta=\sqrt2\). At this remaining parameter, the open region
\[G=\{(x,y):0<x<1,\ 0<y<1,\ x+y>\sqrt2\}\]
consists of points whose three inverse images each have exactly one admissible digit. Consequently \(K(w)=3\), the pushed-forward density equals \(3/2\) on \(G\), and normalized area is not stationary. This argument also handles the endpoint \(\beta=3/2\); all regions used have positive planar area.

**Sharp variation at \(\sqrt2\).** Here \(L=1+\sqrt2\). The region \(G\) is a right triangle with area \((2-\sqrt2)^2/2\), whereas \(\Delta_\beta\) has area \((1+\sqrt2)^2/2\). For arbitrary admissible coins, the pushed-forward density has excess \(1/2\) on \(G\), so by the positive-part formula for total variation,
\[
\|P\lambda_{\sqrt2}-\lambda_{\sqrt2}\|_{\mathrm{TV}}
\ge \frac12\lambda_{\sqrt2}(G)
=\frac{(2-\sqrt2)^2}{2(1+\sqrt2)^2}
=17-12\sqrt2.
\]
For a proof that this lower bound is attained, partition \(\Delta_{\sqrt2}\) up to line boundaries by the inequalities \(x<1\), \(y<1\), and \(x+y<\sqrt2\). Put \(u=1-s-t\). The seven nonempty open regions have the following values of \(K\):

| Region | \(K\) |
| --- | --- |
| \(x<1,y<1,x+y<\sqrt2\) | \(3-2p\) |
| \(x<1,y<1,x+y>\sqrt2\) (the region \(G\)) | \(3\) |
| \(x>1,y<1,x+y<\sqrt2\) | \(1+u\) |
| \(x>1,y<1,x+y>\sqrt2\) | \(2\) |
| \(x<1,y>1,x+y<\sqrt2\) | \(1+t\) |
| \(x<1,y>1,x+y>\sqrt2\) | \(1+2p\) |
| \(x>1,y>1\) | \(1+s\) |

The final region automatically has \(x+y>\sqrt2\). When \(p=1/2\), every entry outside \(G\) is at most \(2\), because \(0<s,t,u<1\). Hence the pushed-forward density is never above one outside \(G\), and its *entire* positive deviation is the excess already computed. This proves equality for every admissible triple-coin distribution. If \(p<1/2\), the first region has positive area with \(K>2\); if \(p>1/2\), the sixth region has positive area with \(K>2\). These produce additional positive deviation beyond that on \(G\), proving that equality occurs only at \(p=1/2\).

**Stationary separation.** For any stationary position law \(P\mu=\mu\), total variation contracts under Markov kernels, and
\[\|P\lambda-\lambda\|_{\mathrm{TV}}
\le\|P\lambda-P\mu\|_{\mathrm{TV}}+\|\mu-\lambda\|_{\mathrm{TV}}
\le2\|\mu-\lambda\|_{\mathrm{TV}}.\]
Apply the just-proved sharp one-step lower bound at \(\beta=\sqrt2\).

## Verification
The standalone `verify_density.py` checks the inverse-branch admissibility against the seven-region formula using high-precision decimal arithmetic and strictly interior rational test points, with several independent coin laws and seven geometric parameters. It also checks the exact radical simplification and the area ratio. The mathematical proof above establishes the statements for all admissible real parameters; the finite checker is only corroboration. The displayed proof uses exact area and transfer-operator identities and does not extrapolate finite experiments.

## Relationship to prior work
Zhang, Dajani and Li introduce the three-digit triangular random \(\beta\)-transformation and establish existence of an absolutely continuous position-stationary measure. Their original 2022 preprint and the 2024 account do not give the present exact best possible variation distance from normalized area at \(\beta=\sqrt2\), the complete minimizing coin family, or the general flat-density exclusion. The earlier one-dimensional invariant-density theory for random \(\beta\)-expansions does not determine this two-dimensional three-digit triangular inverse-branch table. The present theorem is an explicit quantitative statement about a single pushforward and a consequent necessary separation of stationary measures, not a construction or uniqueness theorem for the stationary density.

## Limitations
The total-variation minimum is proved specifically for the one-step defect at \(\beta=\sqrt2\), not for arbitrary \(\beta\), multiple steps, or the stationary-measure distance itself. The lower bound for stationary measures need not be sharp. The theorem concerns the constant-probability binary and triple selection mechanism stated above, not all conceivable position-dependent digit-selection policies, nor triangular gaskets with \(\beta>3/2\). It does not compute the stationary density or its correlations. Publication-priority uncertainty remains for results outside the inspected literature.

## References
Zhang, T., Dajani, K., and Li, W., *Random \(\beta\)-transformation on fat Sierpinski gasket*, arXiv:2201.07560v1, first posted 2022-01-19, especially the inverse-branch construction and the existence proof for an absolutely continuous invariant measure (Sections 4–5): https://arxiv.org/abs/2201.07560.

Dajani, K., Li, W., and Zhang, T., *Random beta-transformations on fat Sierpinski gaskets*, Contemporary Mathematics 797 (2024), 15–35, DOI 10.1090/conm/797/15932. The revised formulation supplies the position-dependent transfer-operator setup: https://doi.org/10.1090/conm/797/15932.

Dajani, K. and de Vries, M., *Invariant densities for random \(\beta\)-expansions*, Journal of the European Mathematical Society 9 (2007), 157–176, DOI 10.4171/JEMS/76: https://doi.org/10.4171/JEMS/76.
