# The concave-envelope law for sharp weighted-variation sensitivity of isotonic projection

## Finding
For every integer \(n\ge2\), positive observation masses \(m_1,\ldots,m_n\), and positive variation weights \(w_1,\ldots,w_{n-1}\), let \(Q_m\) be the weighted least-squares projection of real data onto nondecreasing sequences. Write
\[
V_w(h)=\sum_{j=1}^{n-1}w_j|h_{j+1}-h_j|,
\qquad T_j=\sum_{i=1}^j m_i,\quad T_0=0,
\qquad w_0=w_n=0.
\]
Let \(\widehat w\) be the least concave majorant of the finite points \((T_j,w_j)\), for \(0\le j\le n\), evaluated on \([T_0,T_n]\). Then the **exact attained two-input weighted-variation Lipschitz modulus** is
\[
\boxed{\mathcal K(m,w)=\sup_{V_w(x-y)>0}\frac{V_w(Q_mx-Q_my)}{V_w(x-y)}
=\max_{1\le j<n}\frac{\widehat w(T_j)}{w_j}.}
\]
In particular, \(Q_m\) is nonexpansive in \(V_w\) if and only if the edge weights are concave as a function of cumulative observation mass:
\[
\boxed{\frac{w_j-w_{j-1}}{m_j}\ge\frac{w_{j+1}-w_j}{m_{j+1}}
\quad (1\le j<n).}
\]
The least concave majorant is also the **coordinatewise smallest stabilizing enlargement** of the specified variation weights. The exact modulus is computable from a one-dimensional upper concave hull, and sharpness is realized by an arbitrarily small single-jump perturbation around a fitted pooled block.

## Assumptions and scope
All inputs and outputs are real \(n\)-vectors, with \(n\ge2\), \(m_i>0\), and \(w_j>0\). The projection is the unique minimizer
\[
Q_m(x)=\operatorname*{argmin}_{z_1\le\cdots\le z_n}
\frac12\sum_{i=1}^n m_i(z_i-x_i)^2.
\]
The variation seminorm is **open-path** variation: no edge connects the first and last sites. Constants form its kernel. Translation covariance \(Q_m(x+c\mathbf1)=Q_m(x)+c\mathbf1\) makes the two-input quotient well defined. The weights \(w_0=w_n=0\) are auxiliary boundary values, not additional edges. The least concave majorant refers to interpolation on the strictly increasing knots \(T_0,\ldots,T_n\).

For reproducibility, its value at an interior knot has the explicit finite formula
\[
\widehat w(T_j)=\max\left\{w_j,\ \max_{0\le p<j<q\le n}
\frac{(T_q-T_j)w_p+(T_j-T_p)w_q}{T_q-T_p}\right\}.
\]

## Proof
**1. Active blocks and their linearizations.** The order cone is polyhedral. On every full-dimensional active-set region, the fitted values consist of contiguous blocks \(B\) having strictly increasing block levels; within each block the fit equals the \(m\)-weighted mean. Thus the linear part \(E_{\mathcal B}\) sends a perturbation to its weighted block means. The map \(Q_m\) is continuous and piecewise linear, and every one of these local linearizations fixes constants.

Every contiguous-block partition is realized on a nonempty open region. To see this, choose a nondecreasing vector \(z\) constant on each desired block and strictly increasing across block boundaries. Set \(\lambda_j>0\) at every internal block edge and \(\lambda_j=0\) at boundaries, and define
\[
x_i=z_i+\frac{\lambda_i-\lambda_{i-1}}{m_i},\qquad \lambda_0=\lambda_n=0.
\]
The Karush–Kuhn–Tucker equations and complementary slackness imply \(Q_mx=z\). Strict complementarity internally and strict fitted gaps between blocks persist for sufficiently small perturbations. Therefore the corresponding \(E_{\mathcal B}\) really occurs as a Jacobian and determines attained local two-input Lipschitz ratios.

**2. Step-column reduction.** Let \(H^{(j)}_i=0\) for \(i\le j\) and \(H^{(j)}_i=1\) for \(i>j\). Any perturbation has the decomposition
\[
h=h_1\mathbf1+\sum_{j=1}^{n-1}(h_{j+1}-h_j)H^{(j)}.
\]
For every linear block-averager \(E_{\mathcal B}\), which fixes constants, the sharp operator seminorm is consequently
\[
\|E_{\mathcal B}\|_{V_w}=
\max_{1\le j<n}\frac{V_w(E_{\mathcal B}H^{(j)})}{w_j}.
\]
The triangle inequality proves the upper bound and choosing a step \(H^{(j)}\) proves equality.

**3. The two boundary jumps of a pooled step.** If the cut after site \(j\) is a boundary of \(\mathcal B\), the block-averaged step is unchanged and its variation is \(w_j\). Otherwise the unique block crossing the cut has the form \(B=\{p+1,\ldots,q\}\) with \(0\le p<j<q\le n\). On this block its weighted mean is \(r=(T_q-T_j)/(T_q-T_p)\), with output zero before and one after. Hence its only possible nonzero edge jumps are at \(p\) and \(q\), and
\[
V_w(E_{\mathcal B}H^{(j)})=
\frac{(T_q-T_j)w_p+(T_j-T_p)w_q}{T_q-T_p}.
\]
The formula includes pooled blocks meeting either physical endpoint because \(w_0=w_n=0\).

**4. Upper concave envelope and exact global norm.** Among all block partitions, every pair \(p<j<q\) is attainable by making \(\{p+1,\ldots,q\}\) one pooled block and the remaining sites singletons. Together with the strictly increasing region (identity Jacobian), Step 3 makes the maximal local Jacobian norm exactly the maximum of the displayed chord ratios and one. The expression for \(\widehat w(T_j)\) follows from the one-dimensional convex-hull representation of the least concave majorant: a maximal convex combination at a specified abscissa requires at most two original points, one on either side.

Along the line segment between any real inputs, the continuous piecewise-linear map \(Q_m\) traverses finitely many regions. Summing the variations of the linearized increments gives the same bound globally. Conversely, Step 1 realizes a maximizing block Jacobian in a neighborhood; two points in that neighborhood separated by \(\varepsilon H^{(j)}\), with sufficiently small \(\varepsilon>0\), attain the maximal column ratio exactly. This proves the claimed sharp equality and attainment for all positive real masses and weights.

**5. Contractivity and least stabilizing enlargement.** A discrete profile on the increasing abscissae \(T_j\) coincides with its least concave majorant exactly when all successive slopes are nonincreasing. Those slopes are \((w_j-w_{j-1})/m_j\) and \((w_{j+1}-w_j)/m_{j+1}\), including both zero boundary weights. Therefore \(\mathcal K=1\) precisely under the stated inequalities. Every concave profile majorizing the original samples must also majorize \(\widehat w\), by its defining minimality; this proves the stabilizing-enlargement characterization.

**Exact examples.** With four equal masses and \((w_1,w_2,w_3)=(1,1/2,1)\), the chord joining the first and third edge weights has height \(1\) at the middle edge, so \(\mathcal K=2\). For an explicit attaining pair, set \(x=(0,2,0,2)\) and \(x'=x+\varepsilon(0,0,1,1)\), with \(0<\varepsilon<1\). Their fitted difference is \((0,\varepsilon/2,\varepsilon/2,\varepsilon)\), whose weighted variation is \(\varepsilon\), while the input difference has weighted variation \(\varepsilon/2\). With masses \((1,2,3,4)\) and variation weights \((2,1,1)\), the sharp factor is \(8/5\), showing the dependence on observation mass geometry.

## Verification
Run `python verify.py` with Python 3 and only the standard library. It uses exact rational arithmetic to check the chord-envelope identity against every contiguous-block averaging Jacobian on \(2\) through \(8\) sites for 112 mass/weight profiles (4,064 partitions), explicitly constructs and verifies 112 KKT-attaining input pairs, tests the four-site exact factor \(2\), confirms stable mass-coordinate-concave profiles, and checks 1,394 two-input PAVA inequalities. These finite checks supplement, rather than replace, the all-dimensional analytical proof in Steps 1–5.

## Relationship to prior work
Németh and Németh (2012, 2015) establish structural order-isotonicity of monotone-cone and weighted regression projections, not the weighted-variation modulus. Yang and Barber (2017) prove a general **contractivity criterion** for ordinary Euclidean isotonic projection using neighbor averaging; the theorem does not specify exact expansion factors above one or the dependence on arbitrary observation masses. A published study of isotonic projection on cycle-shaped cover graphs classifies **when** anisotropic edge variation is contractive on cycles; its covering graph is not an open path, and it does not calculate the present sharp amplification profile. The new quantitative envelope law is more specific than these broad qualitative stability principles, and is not stated as a historical-priority certification.

## Limitations
The result applies to finite real one-dimensional total orders with positive observation and variation weights and weighted squared-error projection. It does not assert analogous formulas for branched partial orders, cycles, other fidelity losses, or continuous-domain isotonic projection. The qualitative concavity boundary is related to known averaging-contractivity criteria; the new contribution is the **exact above-threshold Lipschitz constant**, its concave-envelope representation, and attained witnesses for every weight profile. Historical equivalences may exist outside inspected literature. Independent validation has not been performed.

## References
- A. B. Németh and S. Z. Németh, *Isotonicity of the projection onto the monotone cone*, arXiv:1201.4677 (first publicly posted January 23, 2012), https://arxiv.org/abs/1201.4677.
- A. B. Németh and S. Z. Németh, *Isotonic regression and isotonic projection*, arXiv:1503.08458 (first publicly posted March 29, 2015), https://arxiv.org/abs/1503.08458.
- F. Yang and R. F. Barber, *Contraction and uniform convergence of isotonic regression*, arXiv:1706.01852 (first publicly posted June 6, 2017), https://arxiv.org/html/1706.01852v3.
- *Cyclic-cover rigidity of weighted-variation stability for isotonic regression*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-cyclic-cover-rigidity-of-weighted-variation-stability-for-isoton--c6a0693fe803 (published comparison of distinct graph topology).
