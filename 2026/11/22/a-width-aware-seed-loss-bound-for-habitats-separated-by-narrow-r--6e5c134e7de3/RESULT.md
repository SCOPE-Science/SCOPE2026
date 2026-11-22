# A width-aware seed-loss bound for habitats separated by narrow roadways

## Finding

For a rectangular habitat cut into disjoint full-height strips by finitely many nonviable roadways, the fraction of seeds lost after isotropic dispersal has an explicit, *width-aware* upper bound requiring only the mean dispersal distance, rectangle dimensions, and roadway widths. Unlike the perimeter-only estimate, this bound does not charge a narrow roadway as if its two sides were independent outer boundaries. The bound is asymptotically sharp in the simultaneous small-dispersal, narrow-road limit, with an exact second-order formula for fixed-distance dispersal.

Write the overall rectangle as \([0,L]\times[0,H]\), and remove \(m\geq1\) disjoint, strictly positive-width full-height roads \((a_i,a_i+w_i)\times[0,H]\), where the remaining \(m+1\) habitat intervals all have positive width. Set \(W=L-\sum_{i=1}^m w_i>0\). Let \(X\) be uniform on the viable habitat and let the independent displacement \(D\) have rotationally invariant law with \(0<\mu=\mathbb E\|D\|<\infty\). The loss probability is \(p=\Pr(X+D\notin \mathcal H)\).

Define the continuous response function, for \(r>0\) and \(w\geq0\),
\[
F(r,w)=\frac2\pi\int_0^{\pi/2}\min\{r\cos\theta,w\}\,d\theta
=\begin{cases}
\frac{2r}{\pi},&w\geq r,\\
\frac2\pi\left[w\arccos(w/r)+r\left(1-\sqrt{1-(w/r)^2}\right)\right],&0\leq w<r.
\end{cases}
\]
Extend this function continuously by \(F(0,w)=0\) for all \(w\geq0\). Then the new mean-only inequality is
\[
\boxed{\displaystyle
p\leq B_\mu:=\frac{2\mu}{\pi}\left(\frac1W+\frac1H\right)
       +\frac1W\sum_{i=1}^m F(\mu,w_i)
\leq \frac{\mu\,\operatorname{Per}(\mathcal H)}{\pi\,|\mathcal H|}
=\frac{2\mu}{\pi}\left(\frac{m+1}W+\frac1H\right).}
\]
The final inequality is strict whenever some \(w_i<\mu\). One may additionally replace \(B_\mu\) by \(\min\{1,B_\mu\}\) for a probability bound.

**Joint-limit sharpness and exact correction.** Fix \(L,H>0\), a finite number of fixed, distinct interior road locations, and positive constants \(\lambda_i\). For \(\mu>0\) sufficiently small, give each road width \(w_i=\lambda_i\mu\), with every occupied interval longer than \(\mu\), and take \(D=\mu(\cos\Theta,\sin\Theta)\) for a uniform angle \(\Theta\). Put \(t_i=\min\{1,\lambda_i\}\). Then the *exact* seed-loss probability is
\[
\boxed{p_\mu=B_\mu-\frac{\mu^2}{\pi WH}\left[1+\sum_{i=1}^m(2t_i-t_i^2)\right].}
\]
Consequently \(p_\mu/B_\mu\to1\) as \(\mu\downarrow0\); the width-aware coefficient is sharp to leading order for every prescribed collection of finite positive road-width-to-dispersal ratios. In contrast, the perimeter-only bound differs at first order whenever some \(\lambda_i<1\).

## Assumptions and scope

All habitat strips have the same finite height \(H\) and collectively span the rectangle except for full-height roads. The uniform source assumption includes *all* viable strips; a seed landing in any viable strip counts as retained, even if it crosses a road in one displacement. The roads do not modify the displacement distribution. Rotational invariance of \(D\) is allowed without any density; fixed-distance movement and mixtures of radii are included. The theorem makes no assertion for partial-height roads, irregular boundaries, spatially varying source densities, directionally biased dispersal, or movement conditioned on road encounters.

## Proof

**1. Geometric loss decomposition.** Let \(S\subset[0,L]\) be the union of occupied horizontal intervals. For a signed displacement \((u,v)\), define \(\ell_x(u)=|\{x\in S:x+u\notin S\}|\) and \(\ell_y(v)=\min\{|v|,H\}\). Uniform independent horizontal and vertical source coordinates yield the exact conditional identity
\[
\Pr(X+(u,v)\notin\mathcal H\mid D=(u,v))
=\frac{\ell_x(u)}W+\frac{\ell_y(v)}H-\frac{\ell_x(u)\ell_y(v)}{WH}.
\]
An arrival outside \(S\) lies either beyond the outer hull or in one of the roads. For any signed \(u\), the first event accounts for at most \(|u|\) of source length; the \(i\)-th road accounts for at most \(\min\{|u|,w_i\}\). Thus
\[
\ell_x(u)\leq |u|+\sum_i\min\{|u|,w_i\}.
\]
Dropping the nonnegative last term in the conditional identity and using \(\ell_y(v)\leq|v|\) gives
\[
p\leq\frac{\mathbb E|D_x|}{W}+\frac{\mathbb E|D_y|}{H}
  +\frac1W\sum_i\mathbb E\min\{|D_x|,w_i\}.
\]

**2. Rotational average and the mean-only reduction.** Write \(D=R(\cos\Theta,\sin\Theta)\), with \(\Theta\) uniform and independent of the nonnegative radius \(R\) (including a possible atom at zero). Then \(\mathbb E|D_x|=\mathbb E|D_y|=2\mu/\pi\) and
\[
\mathbb E\min\{|D_x|,w_i\}=\mathbb E F(R,w_i).
\]
For fixed \(w\), the function \(r\mapsto\min\{r\cos\theta,w\}\) is concave on \(r\geq0\) for every angle in the first quadrant. Angular averaging preserves concavity, so Jensen's inequality implies \(\mathbb EF(R,w)\leq F(\mathbb ER,w)=F(\mu,w)\). Directly integrating the two angular regimes gives the displayed explicit formula. Also \(F(\mu,w)\leq2\mu/\pi\), with strict inequality for \(0\leq w<\mu\), proving both bounds. The perimeter identity follows from \(\operatorname{Per}(\mathcal H)=2W+2(m+1)H\) and \(|\mathcal H|=WH\).

**3. Exact small-displacement identity.** For sufficiently small \(\mu\), all viable horizontal intervals and the vertical interval exceed the maximum displacement length \(\mu\). In that regime the road-loss pieces and outer-boundary loss do not overlap, for either displacement sign, hence
\[
\ell_x(u)=|u|+\sum_i\min\{|u|,w_i\},\qquad \ell_y(v)=|v|.
\]
With \(w_i=\lambda_i\mu\), the first two terms of the exact conditional identity average to \(B_\mu\) because \(R\equiv\mu\), so Jensen is equality. Finally, elementary quadrant integration gives
\[
\mathbb E|D_xD_y|=\frac{\mu^2}{\pi},\qquad
\mathbb E\big[\min\{|D_x|,w_i\}|D_y|\big]
=\frac{\mu^2}{\pi}(2t_i-t_i^2).
\]
Substitution yields the exact correction. Since \(B_\mu\) is positive and of order \(\mu\), whereas the correction is of order \(\mu^2\), the stated relative sharpness follows. This proof uses no finite-case extrapolation.

## Verification

The standalone `verify_gap.py` performs numerical checks of the exact two-dimensional Gaussian retention integral against the width-aware and original perimeter upper bounds for 600 randomly generated geometries; verifies 100 radial-mixture Jensen comparisons; checks nine Gaussian small-width scalings and six Gaussian crossover quadratures; and compares nine direct angular quadratures with the exact fixed-radius second-order formula. Those checks passed. The theorem's universal statements come from the analytic proof above, not from these finite tests.

For one road \((0.5,0.505)\) in \([0,1]\times[0,4]\), with independent Gaussian coordinate displacements of standard deviation \(0.02\), direct Gaussian integration gives \(p\approx0.024471799238\). The mean-radius-only bound gives \(B_\mu\approx0.024732294769\), versus the established perimeter bound \(0.036065184042\). The new bound is approximately \(31.42\%\) lower. An intermediate bound that uses the known Gaussian radial kernel is \(0.024553839390\), but the claimed theorem does **not** require that extra kernel information.

Reproduce with `python verify_gap.py`; the verification code requires Python 3 and SciPy. Printed decimal values are numerical comparisons, not rigorous decimal certificates. The exact main claim and correction are proved symbolically above.

## Relationship to prior work

Hafner and Meyer (2024) prove the isotropic mean-distance perimeter bound \(p\leq\mu\operatorname{Per}(\mathcal H)/(\pi|\mathcal H|)\) and explicitly observe in Section 6.2 that a very narrow road can double-count boundaries and overestimate loss. Their bound and this modeling caveat are prior work, not new claims. The present result supplies a finite-width correction and a sharp simultaneous thin-road/short-dispersal law for the rectangular multi-road geometry. The older Chisholm–Lichstein (2009) work develops a perimeter approximation and Gaussian formulas for connected square and circular plots, not the mean-only road-width refinement. The general nonlocal-perimeter framework of Cygan and Grzywny (2023) and the heat-content framework of Mazón, Rossi, and Toledo (2017) encompass the underlying overlap integral; those general identities are also prior mathematical tools, not claimed as new. The width-resolved mean-only majorant and joint-limit coefficient were not located in the inspected works; priority remains subject to broader literature checking.

## Limitations

Roads must cross the full rectangular height, and all strips share the same height. The bound may exceed one for large dispersal and should then be capped at one. First-order optimality is only claimed along fixed-distance dispersal families with road widths proportional to their displacement radius and fixed nondegenerate inter-road spacing. No general sharpness is asserted for arbitrary fixed geometry, all radial distributions with a given mean, repeated dispersal generations, or interacting ecological dynamics. Field effects of roads on movement and establishment are excluded. Numerical tests cannot establish historical originality; priority remains provisional and no independent external audit has been performed.

## References

1. B. Hafner and K. Meyer, *Bounding Seed Loss from Isolated Habitat Patches*, first public preprint April 15, 2024, https://arxiv.org/abs/2404.09947; *Bulletin of Mathematical Biology* 86 (2024), article 141, https://doi.org/10.1007/s11538-024-01367-0. In particular Section 6.2 and its narrow-roadway limitation.
2. W. Cygan and T. Grzywny, *Asymptotics of non-local perimeters*, *Annali di Matematica Pura ed Applicata* 202 (2023), 2629–2651, https://doi.org/10.1007/s10231-023-01332-z.
3. J. M. Mazón, J. D. Rossi, and J. Toledo, *The Heat Content for Nonlocal Diffusion with Non-singular Kernels*, *Advanced Nonlinear Studies* 17 (2017), 255–268, https://doi.org/10.1515/ans-2017-0005.
4. R. A. Chisholm and J. W. Lichstein, *Linking dispersal, immigration and scale in the neutral theory of biodiversity*, *Ecology Letters* 12 (2009), 1385–1393, https://doi.org/10.1111/j.1461-0248.2009.01389.x.
