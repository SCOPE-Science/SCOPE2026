# Three-to-five-window variation stability transition for local ROF smoothing

## Finding

For an odd integer \(w\ge1\) and \(\lambda>0\), let \(P_{w,\lambda}:\mathbb R^w\to\mathbb R^w\) be the unique minimizer
\[
P_{w,\lambda}(v)=\operatorname*{argmin}_{u\in\mathbb R^w}
\left\{\frac12\sum_{j=1}^w(u_j-v_j)^2+\lambda\sum_{j=1}^{w-1}|u_{j+1}-u_j|\right\}.
\]
For each real input \(x\in\mathbb R^N\), \(N\ge w\), define the **interior-window local ROF filter** \(T_{w,\lambda}^{(N)}x\in\mathbb R^{N-w+1}\) by taking the central coordinate of \(P_{w,\lambda}\) applied independently to each consecutive length-\(w\) window. Define \(V_m(z)=\sum_{j=1}^{m-1}|z_{j+1}-z_j|\), with \(V_1=0\).

**Three-site sharp contraction.** For every \(N\ge4\), every \(\lambda>0\), and every \(x,y\in\mathbb R^N\),
\[
V_{N-2}(T_{3,\lambda}^{(N)}x-T_{3,\lambda}^{(N)}y)\le V_N(x-y),
\]
and the optimal two-input Lipschitz constant is exactly \(1\), attained by finite pairs. At \(N=3\) the constant is \(0\), since the output has one coordinate. The width-one operator is the identity and has coefficient \(1\) for \(N\ge2\).

**Five-site amplification.** For every \(\lambda>0\) and \(N\ge10\), there are finite pairs \(x,y\in\mathbb R^N\) with
\[
V_{N-4}(T_{5,\lambda}^{(N)}x-T_{5,\lambda}^{(N)}y)
\ge \frac73 V_N(x-y)>V_N(x-y).
\]
For \(N=10\) the displayed ratio \(7/3\) is realized exactly by the rational pair in the proof. Thus among centered odd window widths \(1,3,5\), the first width permitting two-input variation amplification for this unweighted local ROF construction is **five**. The number \(7/3\) is a certified lower bound, **not** a claim of the exact global five-site coefficient.

## Assumptions and scope

All signals are real, the fidelity masses are equal, the path-edge TV penalty is unweighted, and \(\lambda\) is positive and fixed. Each window is independently optimized, with its own two free path endpoints; only its fitted central coordinate is kept. The output contains **only complete interior windows**, with no padding, reflection or periodic closing edge. The perturbation seminorm is ordinary open-path adjacent variation of the difference between two inputs or two outputs, not the variation of either signal separately.

## Proof

**1. Local affine structure.** The strictly convex quadratic plus polyhedral TV penalty gives a continuous piecewise-affine proximal map. On every full-dimensional active region its derivative is orthogonal projection onto vectors constant on each fused consecutive block. Indeed, writing \((Du)_j=u_{j+1}-u_j\), the KKT equations are \(y-u=\lambda D^{\mathsf T}s\), where \(|s_j|\le1\) and \(s_j=\operatorname{sgn}((Du)_j)\) on nonzero edges. Keeping the fused-edge equalities and the signs of the other edges fixed, the linear part averages over each consecutive block. The central-output derivative for a three-site window is therefore precisely one of
\[
(0,1,0),\qquad (1/2,1/2,0),\qquad
(0,1/2,1/2),\qquad (1/3,1/3,1/3).
\]
This list is exhaustive, regardless of which branches are realized together in overlapping windows.

**2. Why every three-site derivative contracts variation.** At any generic \(x\), let \(M\) be the \((N-2)\)-by-\(N\) Jacobian of the complete three-site filter. Every row is a nonnegative probability row on three consecutive sites and has both outer coefficients at most \(1/2\). For the unit step \(h^{(k)}\), zero through input site \(k\) and one thereafter, the sequence \(Mh^{(k)}\) is zero before its transition and one after. At the only two possible intermediate output centers \(k\) and \(k+1\), its values are respectively at most \(1/2\) and at least \(1/2\). Hence \(Mh^{(k)}\) is nondecreasing, with variation at most one, including truncated boundary transitions. Any perturbation \(h\) has the exact decomposition
\[
h=h_1\mathbf1+\sum_{k=1}^{N-1}(h_{k+1}-h_k)h^{(k)},
\]
while \(M\mathbf1=\mathbf1\). The triangle inequality therefore gives
\[
V_{N-2}(Mh)\le\sum_{k=1}^{N-1}|h_{k+1}-h_k|=V_N(h).
\]
Integrate these derivative inequalities along a generic line segment from \(x\) to \(y\); continuity and density extend the inequality to every pair, including trajectories on active-region boundaries. To attain coefficient one, take \(x_j=10\lambda j\) and perturb it by \(\varepsilon h^{(2)}\) for sufficiently small positive \(\varepsilon\). No local window fuses an edge, so the central fitted values equal the original central values and the output perturbation retains the sole jump between centers two and three. This works for every \(N\ge4\).

**3. An exact five-site witness.** At \(N=10\) and \(\lambda=1\), take
\[
x=\tfrac1{10}(18,-11,-5,18,0,-6,-18,1,3,-3),
\quad h=(0,0,0,0,0,1,1,1,1,1),\quad y=x+\tfrac1{1000}h.
\]
The six complete windows, indexed \(i=1,\ldots,6\), have the following center-containing fused blocks \(B_i\) (local window coordinates are one-based), and exact center-output response coefficients \(g_i\):

| Window \(i\) | Fused center block \(B_i\) | \(g_i\) |
|---:|---|---:|
| 1 | \(\{2,3\}\) | \(0\) |
| 2 | \(\{3,4,5\}\) | \(1/3\) |
| 3 | \(\{3\}\) | \(0\) |
| 4 | \(\{3,4,5\}\) | \(1\) |
| 5 | \(\{1,2,3\}\) | \(2/3\) |
| 6 | \(\{3,4,5\}\) | \(1\) |

These fused partitions remain unchanged between \(x\) and \(y\). Here is an exact certificate for the baseline: on each window the edge-dual \(s\in[-1,1]^4\) is, respectively,
\[
\begin{aligned}
&(-1,3/10,1,-2/5),\quad (4/5,1,-11/15,-2/3),\\
&(13/20,-1,-1,-1),\quad (-1,-1,-5/6,8/15),\\
&(-7/15,-1/3,1,3/5),\quad (-1/10,1,3/5,0).
\end{aligned}
\]
For the perturbed windows the same signed-face descriptions satisfy the KKT equations; the minimum strict slack across all nonzero fitted differences and all fused-edge dual bounds in these twelve window optimizations is \(3/20>0\). The self-contained exact-rational checker calculates every primal and dual coordinate and verifies these conditions, rather than relying on floating-point optimization. On a fused block \(B\) from local coordinates \(a\) to \(b\), the fitted value is independently reconstructible as
\[
u_B=\frac{\sum_{j=a}^{b}y_j+\lambda(s_b-s_{a-1})}{b-a+1},
\]
with missing exterior dual variables zero; the dual coordinates are recovered from \(s_j=\lambda^{-1}\sum_{r=1}^j(u_r-y_r)\). Thus the certificates satisfy stationarity, the TV subgradient conditions and uniqueness.

It follows exactly that
\[
T_{5,1}^{(10)}y-T_{5,1}^{(10)}x
=\tfrac1{1000}(0,1/3,0,1,2/3,1).
\]
The input-difference variation is \(1/1000\), whereas the output-difference variation is \(7/3000\); the ratio is \(7/3\). Multiplying both inputs by \(\lambda\) transfers this witness to any \(\lambda>0\), since \(P_{w,\lambda}(\lambda v)=\lambda P_{w,1}(v)\). For any \(N>10\), append arbitrary baseline coordinates and extend the step perturbation by ones. Its variation remains one unit, the original six output windows are unaffected, and extra output edges only add nonnegative variation. This proves the stated all-\(N\) lower bound.

## Verification

Run `python3 check.py` with standard Python 3 in the directory containing this file. The checker enumerates all \(3^4=81\) five-site dual-edge patterns using exact fractions, determines each candidate primal block mean, verifies stationarity and strict primal-dual complementarity, and checks twelve window solutions at the baseline and perturbed inputs. It verifies the six-component response and exact variation ratio \(7/3\). The exhaustive enumeration applies only to those finite witness windows: the all-length three-site bound rests on Step 2's analytical proof, not enumeration.

## Relationship to prior work

Louchet and Moisan introduced and analyzed local ROF filtering and proved local range and monotonicity principles, but the inspected sections and theorem statements do not yield the present two-input adjacent-variation distinction between window widths three and five. Tibshirani and Taylor's generalized-lasso work supplies the fused-block and polyhedral active-face machinery. Little and Jones survey total-variation denoising and prove **one-input** three-point median variation diminution; that is distinct from **two-input** variation stability of local ROF. A published graph-TV-denoising sensitivity theorem gives an all-graph active-partition formula for the **single global** proximal map, not the row-by-row sliding assembly of independently fitted windows. A published sliding-median theorem concerns order-statistic selection, not TV-regularized least-squares centers. The current finding does not claim those underlying methods or local ROF itself as new; it isolates a stability boundary specific to the sliding local-ROF construction.

## Limitations

No exact sharp coefficient is asserted for five-site windows; \(7/3\) is a rigorous realized lower bound for \(N\ge10\). Dimensions \(N=5,\ldots,9\), widths seven and above, nonuniform fidelity or TV weights, non-interior boundary conventions, and cyclic data are unclassified. The one-dimensional anisotropic path TV norm is essential to the stated proof. Bibliographic checks do not independently certify exhaustive historical priority.

## References

1. C. Louchet and L. Moisan, *Total Variation as a Local Filter*, SIAM Journal on Imaging Sciences 4 (2011), 651–694, DOI 10.1137/100785855, https://helios2.mi.parisdescartes.fr/~moisan/papers/lm_tvmeans_siims11.pdf (published electronically June 21, 2011).
2. R. J. Tibshirani and J. Taylor, *The Solution Path of the Generalized Lasso*, arXiv:1005.1971, initial public posting May 11, 2010, https://arxiv.org/abs/1005.1971.
3. M. A. Little and N. S. Jones, *Generalized Methods and Solvers for Noise Removal from Piecewise Constant Signals*, arXiv:1012.5095, first posted December 22, 2010, https://arxiv.org/abs/1012.5095; expanded Part I, DOI 10.1098/rspa.2010.0671.
4. *Exact graph-variation perturbation modulus of the graph fused-lasso denoiser*, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-graph-variation-perturbation-modulus-of-the-graph-fused-la--b4b1357d8d1c (consulted for the global-versus-local comparison).
5. *Sharp total-variation perturbation constant for sliding median filters*, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-total-variation-perturbation-constant-for-sliding-median-f--9412f0250c25 (consulted for the nonlinear sliding-filter comparison).
