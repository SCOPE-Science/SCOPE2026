# Sharp phase transition for near-perfect packing in charge-selected adsorption

## Finding
Consider irreversible deposition of identical unit rods in a finite interval. Every admissible gap is eventually processed; when a rod is placed in a gap of length \(x>1\), its left endpoint has density
\[
 f_x(u)=\frac{u^{q-1}(x-1-u)^{q-1}}{(x-1)^{2q-1}\mathrm B(q,q)},\qquad 0<u<x-1,
\]
with fixed \(0<q\leq1\). Daughter gaps then evolve independently under the same rule. This is the self-renewing attractive dipolar channel of the charge-conditioned beta-kernel adsorption model: every rod has left charge \(+\), right charge \(-\), the exterior gap charges are \((- ,+)\), and \(q=1-\lambda\) for interaction strength \(0\leq\lambda<1\). Both daughter gaps again have charges \((- ,+)\).

Let \(N_x\) be the terminal number of rods, let \(n\geq2\) be any fixed integer, and set \(F_n(\varepsilon)=\Pr(N_{n+\varepsilon}=n)\) for \(0<\varepsilon<1\). Then there are strictly positive, recursively explicit constants \(C_n(q)\) such that
\[
 F_n(\varepsilon)\sim C_n(q)\varepsilon^{E_n(q)}\quad(\varepsilon\downarrow0),
\]
with the **sharp complete exponent classification**
\[
 E_n(q)=\begin{cases}
 (n-1)q,&0<q\leq\tfrac12,\\
 \lfloor(n-1)/2\rfloor+q\bigl((n-1)\bmod2\bigr),&\tfrac12\leq q\leq1.
 \end{cases}
\]
The formulas agree at \(q=1/2\). Equivalently, the optimal rare-event history changes at \(\lambda=1/2\): boundary-cascade histories dominate for \(\lambda>1/2\), maximally branching histories dominate for \(\lambda<1/2\), and every admissible history-tree topology contributes at the transition.

For the first nontrivial example \(n=3\), write \(B_q=\mathrm B(q,q)\). The two geometrically distinct event classes have the separate sharp expansions
\[
 F_3(\varepsilon)=\frac{2^{1-2q}}{B_q}\varepsilon[1+O(\varepsilon)]
 +\frac{2^{1-q}}{qB_q}\varepsilon^{2q}[1+O(\varepsilon)],
\]
where the first term comes from a central first rod, while the second comes from an edge first rod followed by two placements in one daughter gap. At the critical bias \(q=1/2\),
\[
 F_3(\varepsilon)\sim\frac{1+2\sqrt2}{\pi}\varepsilon.
\]

## Assumptions and scope
The model is one-dimensional, rods have exact length one, every nonempty placeable gap is processed until jammed, and each new placement uses an independent beta variable with common parameter \(q\). Branch scheduling cannot affect the terminal law because separate daughter gaps use independent randomness and are eventually exhausted. All limits are taken at fixed integer \(n\) and fixed \(q\) before \(\varepsilon\downarrow0\). The endpoint \(q=0\) is excluded. In particular, the result does not assert a uniform joint limit as \(n\to\infty\) or \(q\to0\).

## Proof
Define \(F_0(t)=F_1(t)=1\) for \(0\leq t<1\), and let
\[
 g_{n,\varepsilon}(u)=\frac{u^{q-1}(n-1+\varepsilon-u)^{q-1}}
 {(n-1+\varepsilon)^{2q-1}B_q}.
\]
For \(0<\varepsilon<1\), maximal packing with \(n\) rods is possible after the first deposition only when its left endpoint falls in exactly one of the disjoint windows \([k,k+\varepsilon]\), for \(k=0,\ldots,n-1\). In that event, the daughter lengths are \(k+t\) and \(n-1-k+\varepsilon-t\). Conditional independence yields the **exact** identity
\[
 F_n(\varepsilon)=\sum_{k=0}^{n-1}\int_0^\varepsilon
 g_{n,\varepsilon}(k+t)F_k(t)F_{n-1-k}(\varepsilon-t)\,dt.
 \tag{1}
\]
This is a probability identity rather than a finite enumeration approximation.

Suppose inductively that \(F_j(t)\sim C_j t^{E_j}\) for all \(j<n\), with positive \(C_j\). At an endpoint window, \(k=0\) or \(k=n-1\), the density has a power singularity. Substituting \(t=\varepsilon v\) and applying dominated convergence to the beta integral gives each endpoint contribution
\[
 \frac{(n-1)^{-q}}{B_q}C_{n-1}\mathrm B(q,E_{n-1}+1)
 \varepsilon^{q+E_{n-1}}[1+o(1)].
 \tag{2}
\]
For an interior window \(1\leq k\leq n-2\), the density converges uniformly to the strictly positive number
\[
 d_{n,k}=\frac{k^{q-1}(n-1-k)^{q-1}}{(n-1)^{2q-1}B_q}.
\]
The interior contribution is therefore
\[
 d_{n,k} C_k C_{n-1-k}\mathrm B(E_k+1,E_{n-1-k}+1)
 \varepsilon^{1+E_k+E_{n-1-k}}[1+o(1)].
 \tag{3}
\]
All coefficients are positive, so there is no cancellation, and the leading exponent is the minimum of those displayed in (2)–(3). This inductively proves existence of the positive sharp asymptotic and gives the explicit coefficient recursion, with \(E_0=E_1=0\), \(C_0=C_1=1\):
\[
 \begin{split}
 E_n&=\min\left\{q+E_{n-1},\ \min_{1\leq k\leq n-2}(1+E_k+E_{n-1-k})\right\},\\
 C_n&=\mathbf1_{q+E_{n-1}=E_n}\frac{2(n-1)^{-q}}{B_q}C_{n-1}\mathrm B(q,E_{n-1}+1)\\
 &\quad+\sum_{\substack{1\leq k\leq n-2\\1+E_k+E_{n-1-k}=E_n}}
 d_{n,k}C_kC_{n-1-k}\mathrm B(E_k+1,E_{n-1-k}+1).
 \end{split}
 \tag{4}
\]
The indicator expresses exact equality of the analytically defined exponents, not numerical tolerance.

To solve the exponent recurrence simultaneously for **all** finite \(n\), associate to each successful deposition history a rooted tree: a deposition vertex has zero, one or two nonempty descendant subgaps, and thus zero, one or two child deposition vertices. A one-child vertex arises from a boundary window and contributes exponent \(q\); a two-child vertex arises from an interior window and contributes exponent one; a leaf contributes zero. If the tree has \(n\) vertices, \(s\) one-child vertices and \(b\) two-child vertices, counting edges yields \(s+2b=n-1\). Its exponent is therefore
\[
 qs+b=q(n-1)+(1-2q)b.
\]
Every integer \(0\leq b\leq\lfloor(n-1)/2\rfloor\) is achievable by an ordered rooted tree with \(n\) vertices: start from a chain and replace two successive one-child vertices by a two-child vertex and a leaf, as needed. If \(q<1/2\), the cost increases with \(b\) and is minimized by the unary chain; if \(q>1/2\), the cost decreases with \(b\) and is minimized by the maximally branched trees; at \(q=1/2\), every topology ties. This is exactly the stated piecewise formula and completes the proof.

For \(n=3\), the interior term of (1) has constant \(2^{1-2q}/B_q\). The two endpoint terms use \(F_2(t)\sim2t^q/(qB_q)\) and \(\mathrm B(q,q+1)=B_q/2\), giving \(2^{1-q}/(qB_q)\). Smoothness away from the singular endpoints, together with beta-tail expansions, supplies the displayed relative \(O(\varepsilon)\) remainders separately.

## Verification
The companion `CHECK.py` verifies the exponent recurrence against the closed formula for all integers \(2\leq n\leq35\) at a representative range of bias parameters; computes the positive coefficients from (4), independently checks the \(n=2,3\) formulas, and quadratures the exact \(n=3\) integral to verify its central and edge terms separately. The proof above, not the finite calculation, establishes the result for every fixed integer \(n\).

## Relationship to prior work
Palacios and Macêdo (arXiv:2608.28289v1, first public August 28, 2026) introduce the charge-conditioned beta placement kernel and full-counting-statistics recurrence and investigate mean and variance, including finite-shell examples. The present statement uses their self-renewing single-orientation specialization and asks a different question: the sharp near-integer maximal-occupancy rarity, for every integer target occupancy, including a nonanalytic change in the optimizing deposition-tree topology and a recursively explicit leading coefficient. Their general recurrence motivates (1) but alone does not state the all-occupancy exponent phase classification. The classical Rényi car-parking problem is recovered at \(q=1\); established work on large-interval density and gaps concerns distinct limits.

## Limitations
This is a fixed-\(n\) small-excess-length theorem, not a thermodynamic limit, a finite-time deposition rate result, or a statement about mixtures of different incoming charge types. The original motivating manuscript's full later sections were not accessible during the present literature comparison, so possible implicit or explicit coverage in its finite-shell calculations remains a priority risk; the inspected abstract and model sections do not establish the all-\(n\) phase classification. The coefficient recursion requires evaluating finite beta-function sums; no elementary formula for all coefficients is claimed. No independent scientific validation is asserted.

## References
1. G. Palacios and A. M. S. Macêdo, *A Generalized Model for Disordered Random Sequential Adsorption with Charge-Dependent Deposition*, arXiv:2608.28289v1 (first public August 28, 2026). https://arxiv.org/abs/2608.28289
2. A. Rényi, *On a one-dimensional problem concerning random space filling*, Publ. Math. Inst. Hungar. Acad. Sci. 3 (1958), 109–127.
3. *A unified model for Kakutani's interval splitting and Rényi's random packing*, Advances in Applied Probability 24 (1992), 502–505. https://doi.org/10.2307/1427704
4. L. Gerin, *The Page–Rényi Parking Process*, Electronic Journal of Combinatorics 22(4) (2015), P4.4. https://doi.org/10.37236/5150
