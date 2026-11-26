# Supercritical invariant circles in the minimal oriented logistic network

## Finding
Consider a three-site cyclic logistic map with balanced oriented interactions, as defined below. Put \(s=3a^2\) for its interaction strength \(a>0\), and \(r_c=1+2/(1+s)\). For every fixed \(a>0\) with \(s\notin\{1/3,1\}\), the positive homogeneous equilibrium is locally asymptotically stable for \(1<r<r_c\), loses stability at \(r=r_c\) through a **supercritical Neimark–Sacker bifurcation**, and is unstable just above \(r_c\). For all sufficiently small \(\varepsilon=r-r_c>0\), there exists an attracting invariant simple closed curve entirely in the interior of the state cube.

Writing a state on this curve uniquely as \(x_j=x_*+m+z\omega^j+\bar z\omega^{-j}\), with \(x_*=1-1/r\), \(\omega=e^{2\pi i/3}\), \(m\in\mathbb R\), and \(z\in\mathbb C\), its small-curve amplitude and spatial mean satisfy, **uniformly along the curve**,
\[
|z|^2=\frac{(1+s)^2}{(3+s)^3}\varepsilon+o(\varepsilon),\qquad
m=-\frac{(1+s)^2}{(3+s)^2}\varepsilon+o(\varepsilon).
\]
In the corresponding Fourier-normalized center coordinate, the exact cubic radial coefficient at onset is \(-(s+3)^3/(s+1)^2<0\). This is a constructive, all-coupling-range classification except for the explicitly excluded strong resonances.

## Assumptions and scope
Let \(H(u)=\min\{1,\max\{0,u\}\}\). For \(r>1\) and \(a>0\), define \(F_{r,a}:[0,1]^3\to[0,1]^3\) by
\[
(F_{r,a}(x))_j=H\!\left(r x_j[1-x_j+a(x_{j+1}-x_{j-1})]\right),\quad j\in\{0,1,2\},
\]
where subscripts are modulo three. The result concerns local dynamics about \(x_*\mathbf 1\), where \(x_*=1-1/r\in(0,1)\), so clipping is inactive in a neighborhood. All assertions hold for each fixed \(a\) satisfying \(a>0\), \(a\ne1/3\), and \(a\ne1/\sqrt3\); the required positive \(\varepsilon\) can depend on \(a\). We make no assertion about invariant circles at the two excluded resonances, global basins, nor global invariance of the unclipped polynomial outside the local neighborhood.

## Proof
**1. Exact Fourier reduction.** Write \(u_j=x_j-x_*\). The oriented matrix \((Au)_j=a(u_{j+1}-u_{j-1})\) is skew-symmetric, vanishes on constants, and has eigenvalues \(\pm i\sqrt{s}\) on the nonconstant Fourier modes. Thus, uniquely,
\[
u_j=m+z\omega^j+\bar z\omega^{-j},\qquad \omega=e^{2\pi i/3}.
\]
Expanding the polynomial update near \(x_*\mathbf1\), Fourier orthogonality and \(\sum_j u_j(Au)_j=0\) give the **exact** local equations
\[
\begin{split}
m^+&=(2-r)m-rm^2-2r|z|^2,\\
z^+&=[2-r+i\sqrt{s}(r-1)]z+r(-2+i\sqrt{s})mz+r(-1-i\sqrt{s})\bar z^2.
\end{split}
\]
The scalar multiplier is \(b=2-r\); the pair is \(\lambda,\bar\lambda\), where \(\lambda=2-r+i\sqrt{s}(r-1)\). If \(\delta=r-1\), then
\[
|\lambda|^2=1-2\delta+(1+s)\delta^2.
\]
Consequently the pair is strictly inside the unit circle for \(0<\delta<2/(1+s)\), reaches it at \(r_c=1+2/(1+s)\), and crosses outward with \(\frac{d}{dr}|\lambda|_{r=r_c}=1\). The third multiplier there is \((s-1)/(s+1)\), strictly inside the unit circle for \(s>0\); on the entire interval \(1<r<r_c<3\) it is also strictly inside. This proves the stated linear stability range and crossing.

**2. Resonances.** At onset,
\[
\lambda_c=\frac{s-1+2i\sqrt{s}}{s+1}.
\]
For finite \(s>0\) its imaginary part is positive. Its only possible resonances of orders two, three, or four occur at \(s=1/3\) (order three) and \(s=1\) (order four); order two never occurs. These values are excluded. The center pair therefore satisfies the low-order nonresonance hypotheses of the classical Neimark–Sacker theorem.

**3. Exact cubic coefficient.** At onset, the invariant center manifold has quadratic graph \(m=h|z|^2+O(|z|^3)\). Substitution into the first exact equation gives
\[
h=\frac{-2r_c}{1-(2-r_c)}=-(s+3).
\]
The restricted center map is, up to cubic order,
\[
z^+=\lambda_c z+\beta\bar z^2+\gamma z|z|^2+O(|z|^4),
\]
where \(\beta=r_c(-1-i\sqrt{s})\), \(\gamma=r_c(-2+i\sqrt{s})h\). Since \(s\ne1/3\), the nonresonant quadratic term is eliminated by \(z=w+k\bar w^2\), with
\[
k=\frac{\beta}{\bar\lambda_c^2-\lambda_c}=\frac{(1+s)(3+s)}{2(3s-1)}\in\mathbb R.
\]
Comparison of cubic terms gives
\[
w^+=\lambda_c w+C w^2\bar w+O(|w|^4),\qquad C=\gamma+2\beta\bar k.
\]
There are no other cubic monomials allowed by threefold cyclic equivariance. Direct algebra yields
\[
\operatorname{Re}(\bar\lambda_c C)=-\frac{(s+3)^3}{(s+1)^2}<0.
\]
The low-order nonresonance, transverse outward crossing, and strictly negative cubic radial coefficient are precisely the nondegeneracy and supercriticality hypotheses for the Neimark–Sacker theorem. Hence a locally attracting invariant Jordan curve appears for all sufficiently small \(r-r_c>0\). It lies in the unclipped interior because the equilibrium is interior and its diameter tends to zero. No statement is made that its rotation number must be irrational at every nearby parameter.

**4. Sharp leading profiles.** The normal form radial equation is
\[
|w^+|=|w|\bigl(1+\varepsilon-\frac{(s+3)^3}{(s+1)^2}|w|^2+o(\varepsilon+|w|^2)\bigr).
\]
The small invariant circle thus has \(|w|^2=(s+1)^2\varepsilon/(s+3)^3+o(\varepsilon)\), uniformly in its angle. The quadratic change \(z=w+O(|w|^2)\) leaves this leading squared amplitude unchanged; using \(m=h|z|^2+O(|z|^3)\) gives the asserted spatial-mean deficit. This establishes both asymptotics.

## Verification
The standalone `verify_exact.py` reconstructs the onset multipliers, the center-manifold graph coefficient, the quadratic conjugacy, the exact cubic coefficient, and the mean/amplitude constants symbolically for a free positive parameter \(s\). It independently compares the exact Fourier recurrence with direct updates for three nonsymmetric sample states and runs a numerical bifurcation-amplitude diagnostic at \(a=1/2\). The diagnostic is an illustration, not a proof of an invariant circle. Its observed amplitude agrees with the leading prediction to within the stated tolerance. Reproduce by running `python verify_exact.py` with SymPy available.

## Relationship to prior work
Baron and Galla, *The disordered logistic map* (arXiv:2609.24402, posted September 21, 2026), introduce the clipped multiplicatively coupled logistic update and analyze random interactions, instability spectra, and disorder-driven high-dimensional chaos. The present deterministic, balanced oriented three-site interaction is a specific admissible matrix choice, **not an iid disorder realization**; the exact family-wide supercriticality coefficient and local attracting curves are additional claims not implied by their large-random-network analysis. Mareno and English (2020) prove flip and Neimark–Sacker bifurcations for a distinct two-map strongly coupled system, illustrating the established theory; their model, fixed-point branches, and coefficient do not supply this three-site oriented-ring theorem. Classical Neimark–Sacker bifurcation theory and Fourier decomposition are used without novelty claims. No exact statement covering the present map and coefficient was identified in the inspected literature or research-index results, but exhaustive historical priority is not established.

## Limitations
The excluded resonances \(s=1/3\) and \(s=1\) are not classified. There is no claim about global attractors, chaos, or an invariant curve for every parameter above onset; the result is local and perturbative in \(r-r_c\). Resonance tongues may give periodic dynamics on the new invariant curve. The historical-priority assessment depends on the accessible sources inspected and is not an independent audit.

## References
1. J. W. Baron and T. Galla, *The disordered logistic map*, arXiv:2609.24402 (first posted 2026-09-21). https://arxiv.org/abs/2609.24402
2. A. Mareno and L. Q. English, *Flip and Neimark–Sacker Bifurcations in a Coupled Logistic Map System*, Discrete Dynamics in Nature and Society 2020, 4103606, https://doi.org/10.1155/2020/4103606.
3. Standard Neimark–Sacker local bifurcation theorem as restated in Mareno and English (2020), §4.2; the present proof verifies its nondegeneracy hypotheses explicitly.
