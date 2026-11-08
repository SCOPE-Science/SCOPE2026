# Donor-abundance rescue has a universal fractional-power threshold in a nonlinear Allee metapopulation

## Finding

**Theorem.** Consider the two-patch nonlinear-dispersal population system of Xia, Chen, Srivastava and Parshad [1],
\[
\dot u=u\left(\frac{u}{m+u}-e-hu+\delta(v-u)\right),\qquad
\dot v=v\left(s(1-v)+\delta(u-v)\right).
\]
Assume \(s,\delta,h,m>0\), define \(B=s\delta/(s+\delta)\), and impose the strictly bistable conditions
\[
0<B<e<\min\{1,s\},\qquad
0<m<m_*:=\frac{(1-\sqrt{e-B})^2}{h+B}.
\]
Let \(a<b\) be the two positive roots of
\[
(h+B)z^2+\bigl[m(h+B)+e-B-1\bigr]z+m(e-B)=0,
\]
and put \(v_a=(s+\delta a)/(s+\delta)\), \(v_b=(s+\delta b)/(s+\delta)\), and \(v_0=s/(s+\delta)\).

For **every** donor-patch initial population \(V\ge v_a\), there is a unique rescue threshold \(\psi(V)\in(0,a]\), with \(\psi(v_a)=a\). For the solution with \((u(0),v(0))=(U,V)\) and \(U>0\), its limit is
\[
\begin{cases}
(0,v_0),&0<U<\psi(V),\\
(a,v_a),&U=\psi(V),\\
(b,v_b),&U>\psi(V).
\end{cases}
\]
The function \(\psi\) is smooth and strictly decreasing for \(V>v_a\). Writing \(p=\delta/(s+\delta)\in(0,1)\), there exists a finite, strictly positive constant \(C=C(s,\delta,e,h,m)\) such that
\[
\boxed{\quad
\psi(V)=CV^{-p}\left[1-\frac{e-B}{(s+\delta)V}+O(V^{-1-p})\right]
\quad (V\to\infty).\quad}
\]
The coefficient is uniquely characterized by \(C=\lim_{V\to\infty}V^p\psi(V)>a v_a^p\). Thus a donor population increased by a factor \(r\) eventually reduces the minimum founding population by a factor approaching \(r^{-p}\). The exponent depends only on the relative nonlinear dispersal intensity, not on the Allee-growth parameters. The second relative correction is explicit.

## Assumptions and scope

The variables \(u,v\) are strictly positive initial densities, not individual counts. The first patch experiences an Allee effect; the second has logistic growth. The theorem is for the published **nonlinear** migration terms \(\delta u(v-u)\) and \(\delta v(u-v)\), not for linear migration. Its basin classification covers all \(U>0\) for each \(V\ge v_a\), rather than all donor values. The restriction \(e<s\) provides a uniform planar no-cycle argument. At the stated strict inequalities all three equilibria are distinct and hyperbolic. Equality and parameter regimes outside the statement are not asserted.

## Proof

**1. Positivity, boundedness and equilibria.** Both axes are invariant. For positive data, both coordinates stay positive for finite forward time. At a coordinate attaining the maximum of \(u,v\), its derivative is negative if that maximum exceeds \(\max\{1,(1-e)/h\}\): for the first coordinate use \(u/(m+u)\le1\) and \(v\le u\); for the second use \(u\le v\). This bounds all forward trajectories. Also \(\dot v\ge v[s-(s+\delta)v]\), so \(v(t)\) is bounded away from zero for all large \(t\).

Set \(p=\delta/(s+\delta)\) and \(E=e-B>0\), \(L=h+B\). The exact cancellation
\[
\frac{d}{dt}\log(uv^p)=\frac{u}{m+u}-E-Lu=:f(u)
\tag{1}
\]
holds for every positive solution. At a positive equilibrium, \(v=(s+\delta u)/(s+\delta)\) and \(f(u)=0\). The stated conditions make the two roots \(a<b\) distinct and positive. The remaining equilibrium in the nonnegative region with \(v>0\) is \((0,v_0)\). In particular \(f(u)<0\) for \(0<u<a\), and \(f(u)>0\) for \(a<u<b\).

At \((z,v_z)\) the Jacobian satisfies
\[
\det J=-(s+\delta)zv_z f'(z),\qquad
J_{12}=\delta z>0,\quad J_{21}=\delta v_z>0.
\]
The smaller root has \(f'(a)>0\), hence \((a,v_a)\) is a saddle. At the larger root \(f'(b)<0\); its Jacobian has both diagonal entries negative, so \((b,v_b)\) is a sink. The boundary equilibrium \((0,v_0)\) has eigenvalues \(-E\) and \(-s\) and is a sink in the positive quadrant. The saddle's stable eigenvector has components of opposite signs, while its unstable eigenvector has both components positive.

**2. Only equilibrium omega-limits for positive data.** Apply the Bendixson--Dulac multiplier \(1/(u^2v^2)\). Its divergence is exactly
\[
\frac{e-s-\delta(u+v)-u^2/(m+u)^2}{u^2v^2}<0
\tag{2}
\]
throughout the positive quadrant, since \(e<s\). This excludes periodic or polycyclic limit sets there. Together with boundedness, finitely many isolated equilibria and the lower bound on \(v\), planar limit-set theory gives convergence to one of the three equilibria above. This is a classification of **interior** trajectories; no assertion about solutions started on \(v=0\) is needed.

**3. The northwestern stable separatrix.** The stable-manifold theorem at \((a,v_a)\) provides a smooth local stable branch with \(u<a\), \(v>v_a\). Follow this branch in backward time \(\tau=-t\). As long as \(0<u<a\) and \(v>v_a\),
\[
\frac{dv}{d\tau}=v\bigl[(s+\delta)v-s-\delta u\bigr]>0.
\]
Initially \(du/d\tau<0\). Define \(G(u,v)=u/(m+u)-e-(h+\delta)u+\delta v\), so \(du/d\tau=-uG\). At any possible zero of \(G\) in the region, \(dG/d\tau=\delta\,dv/d\tau>0\). It is therefore impossible for \(G\), initially positive, to cross from positive to negative: \(du/d\tau\) remains strictly negative. Thus the backward branch remains inside \((0,a)\times(v_a,\infty)\), with \(u\) decreasing and \(v\) increasing.

If its backward \(v\) remained bounded, monotonicity and smoothness would force a limiting equilibrium in the closure of that rectangle. None exists: the only positive roots are \(a,b\), and the boundary equilibrium has \(v=v_0<v_a\). Hence \(v\to\infty\); in fact \(dv/d\tau\) is eventually at least \((s+\delta)v^2/2\), so the backward trajectory reaches infinity in finite backward time. This branch is therefore a graph \(u=\psi(V)\) at **every** \(V\ge v_a\), decreasing smoothly from \(\psi(v_a)=a\) toward zero. The stable manifold's opposite branch, with \(u>a,v<v_a\), remains below \(v_a\) in backward time and cannot create another threshold at \(V\ge v_a\).

The system is strictly cooperative in the interior (both off-diagonal Jacobian entries are positive). The two forward unstable branches of the saddle point into the northeast and southwest directions. By order preservation and Step 2, the northeast branch tends to \((b,v_b)\) and the southwest branch to \((0,v_0)\). Near the saddle, the local stable manifold separates their basins. Pulling this separation back along the global stable branch, and using order preservation and the absence of another stable-manifold intersection on each horizontal slice, gives the three outcomes asserted in the theorem for any fixed \(V\ge v_a\).

**4. The donor-abundance asymptotic.** Along the backward branch parameterized by its increasing \(V=v\), set \(H(V)=\psi(V)V^p\). The identity (1) and the reverse-time \(v\) equation give the exact derivative
\[
\frac{d}{dV}\log H(V)
=\frac{E+L\psi(V)-\psi(V)/(m+\psi(V))}
{V[(s+\delta)V-s-\delta\psi(V)]}.
\tag{3}
\]
The numerator is \(-f(\psi(V))>0\), bounded because \(0<\psi(V)\le a\). The denominator is asymptotic to \((s+\delta)V^2\). Thus the derivative is integrable at infinity and \(H\) rises to a finite positive \(C>a v_a^p\). Consequently \(\psi(V)=CV^{-p}(1+o(1))\).

Substituting this back into (3), using \(0<p<1\), yields
\[
\frac{d}{dV}\log H(V)
=\frac{E}{(s+\delta)V^2}+O(V^{-2-p}).
\]
Integration from \(V\) to infinity gives \(\log C-\log H(V)=E/[(s+\delta)V]+O(V^{-1-p})\). Exponentiating, with \(V^{-2}=O(V^{-1-p})\), proves the two-term formula.

## Verification

Run `python verify.py` (Python standard library only). The checker evaluates the weighted-logarithmic cancellation with exact rational arithmetic, checks equilibrium and Jacobian identities for three parameter sets, and integrates the saddle stable-manifold graph with fourth-order Runge--Kutta to examine the predicted power law and first correction. It reports `VERIFY_OK 2292 exact rational and numerical checks` for the packaged version. The computations do not certify the global statements; Steps 1--4 constitute their proof.

For example, \((s,\delta,e,h,m)=(0.8,0.4,0.5,0.3,0.2)\) has \(p=1/3\), \(a\approx0.0765051915\), \(v_a\approx0.6921683972\), and numerical separatrix amplitude \(C\approx0.0735577741\). These figures are illustrative, not additional asserted exact constants.

## Relationship to prior work

Xia et al. [1,2] derive this model's equilibrium conditions, their local stability, saddle-node onset, and a global-extinction parameter criterion (their Theorems 2.2--2.8). Those results are fully credited. Their numerical phase portraits display competing attraction basins in the bistable chamber, but the inspected accessible preprint does not give an all-large-donor analytical threshold graph or its fractional-power and correction law. The geometric-logarithmic cancellation is an algebraic tool, not itself asserted novel; an earlier analysis of a distinct critical parameter slice of the same system also uses it. Related linear-dispersal two-patch analyses [3] and general cooperative ecological geometry [4] do not imply the present nonlinear-dispersal exponent without additional model-specific work. Works on founding population thresholds [5] address a different spatial integrodifference mechanism.

## Limitations

The constant \(C\) is defined intrinsically by the saddle separatrix and has no claimed elementary closed form. This is a deterministic continuous-density model, not a demographic-stochastic survival probability. The theorem does not extend by assertion to linear dispersal, to the PDE version, to \(V<v_a\), or to parameter boundaries. Numerical values are reproducibility checks only. The accessible full preprint was read in the relevant sections; the publisher's complete HTML body was not exposed by the available text interface, so an equivalent statement in the journal revision remains a publication-priority risk. Broader unindexed separatrix literature may contain related results. An independent external audit is not claimed.

## References

[1] Y. Xia, L. Chen, V. Srivastava, R. D. Parshad, *Stability and bifurcation analysis of a two-patch model with Allee effect and dispersal*, arXiv:2310.10558v1, publicly submitted 16 October 2023. https://arxiv.org/html/2310.10558v1

[2] Y. Xia et al., *Stability and bifurcation analysis of a two-patch model with the Allee effect and dispersal*, Mathematical Biosciences and Engineering 20 (2023), 19781--19807, doi:10.3934/mbe.2023876. https://www.aimspress.com/article/doi/10.3934/mbe.2023876

[3] L. Chen, T. Liu, F. Chen, *Stability and bifurcation in a two-patch model with additive Allee effect*, AIMS Mathematics 7 (2022), 536--551, doi:10.3934/math.2022034. https://aimspress.com/article/doi/10.3934/math.2022034

[4] A. Ching and S. Baigent, *Manifolds of balance in planar ecological systems*, Applied Mathematics and Computation 358 (2019), 204--215, doi:10.1016/j.amc.2019.04.047. https://discovery.ucl.ac.uk/id/eprint/10072840/

[5] D. W. Goodsman and M. A. Lewis, *The minimum founding population in dispersing organisms subject to strong Allee effects*, Methods in Ecology and Evolution 7 (2016), 1100--1109, doi:10.1111/2041-210X.12573. https://onlinelibrary.wiley.com/doi/10.1111/2041-210X.12573/full
