# Sharp two-atom placement and stability for weighted-mean periodic Sobolev evaluation

## Finding

The sharp real mean-zero periodic Sobolev evaluation norm on a circle with arclength background and two positive atomic masses is determined exactly. In particular, under a fixed total atomic mass, balanced antipodal placements are the unique best-conditioned arrangement and the excess embedding constant splits into a sharp imbalance defect and a sharp separation defect.

Write \(S=\alpha+\beta\), \(M=1+S\), and \(d\in[0,1/2]\). Then
\[
\boxed{\mathcal K(\alpha,\beta,d)=\frac{1}{12M^2}+\frac S{4M}-\frac{\alpha\beta\,d(d+S)}{SM^2}.}
\]
For fixed \(S\), the global minimum is
\[
\boxed{\mathcal K_*(S)=\frac{4+9S+6S^2}{48(1+S)^2},}
\]
and the full quantitative remainder is
\[
\boxed{\mathcal K-\mathcal K_*=
\frac{(\alpha-\beta)^2(\frac14+\frac S2)}{4SM^2}+
\frac{\alpha\beta(\frac12-d)(\frac12+d+S)}{SM^2}.}
\]
Every term on the right is nonnegative, with simultaneous vanishing exactly for equal antipodal atomic masses.

## Assumptions and scope

Take \(\mathbb T=\mathbb R/\mathbb Z\) with length one and Lebesgue arclength \(dt\). Fix real numbers \(\alpha,\beta>0\), a separation \(0\le d\le1/2\), and the positive measure
\[
\mu=dt+\alpha\delta_0+\beta\delta_d,\qquad \mu(\mathbb T)=M=1+S,\quad S=\alpha+\beta.
\]
Let \(H_\mu\) be the real periodic Sobolev space of continuous \(H^1\) functions satisfying \(\int_{\mathbb T}f\,d\mu=0\). Its squared norm is \(E(f)=\int_0^1|f'(t)|^2\,dt\); positivity on nonzero \(H_\mu\) follows because constants of weighted mean zero vanish. The exact squared embedding norm is
\[
\mathcal K(\alpha,\beta,d)=\sup_{f\in H_\mu\setminus\{0\}}\frac{\max_{x\in\mathbb T}|f(x)|^2}{E(f)}.
\]
Rotations, reflections, and atom relabeling identify equivalent designs; the distinguished order places \(\alpha\) at \(0\) and \(\beta\) at \(d\).

## Proof

**1. Evaluation kernel.** Write \(R(x,y)=r(1-r)\), where \(r\in[0,1]\) represents \(x-y\pmod 1\). This is the effective resistance between two points on the unit-length circle, and in distributions \(\partial_y^2 R(y,z)=-2+2\delta_z\). For each \(x\), put \(\nu_x=\delta_x-\mu/M\), a signed measure of total mass zero. The centered function
\[
G_x(y)=-\frac12\int_{\mathbb T}R(y,z)\,d\nu_x(z)-c_x,
\qquad
c_x=\frac1M\int_{\mathbb T}\left[-\frac12\int_{\mathbb T}R(y,z)\,d\nu_x(z)\right]d\mu(y)
\]
has zero \(\mu\)-mean and solves \(-G_x''=\nu_x\). Periodic integration by parts gives \(\int f'G_x'=\int f\,d\nu_x=f(x)\) for every \(f\in H_\mu\). Hence Cauchy–Schwarz gives \(|f(x)|^2\le E(f)E(G_x)\), with equality exactly for \(f=cG_x\). Moreover \(E(G_x)=G_x(x)\). Expanding this equality yields the exact pointwise constant
\[
K_\mu(x)=\frac1M\int R(x,y)\,d\mu(y)-\frac1{2M^2}\iint R(y,z)\,d\mu(y)d\mu(z).
\]

**2. Exact integrals and maximizers.** Since \(\int_0^1R(x,t)dt=1/6\) and
\[
\iint R(y,z)\,d\mu(y)d\mu(z)=\frac{1+2S}{6}+2\alpha\beta\,d(1-d),
\]
one obtains
\[
K_\mu(x)=\frac1{12M^2}+\frac{\alpha R(x,0)+\beta R(x,d)}M-\frac{\alpha\beta\,d(1-d)}{M^2}.
\]
Put \(U(x)=\alpha R(x,0)+\beta R(x,d)\). On the longer arc \(d\le x\le1\),
\[
U(x)=-Sx^2+(S+2\beta d)x-\beta d(1+d),
\]
whose unique vertex is \(x_L=\tfrac12+\beta d/S\), and the vertex value is \(U(x_L)=S/4-\alpha\beta d^2/S\). On the shorter arc \(0\le x\le d\), the unconstrained quadratic vertex has value
\[
U_{s,\mathrm{vertex}}=\beta d(1-d)+\frac{(\alpha-\beta+2\beta d)^2}{4S}.
\]
The difference of the two unconstrained vertex values is exactly \(\alpha\beta(1-2d)/S\). Because each piece has strictly negative second derivative \(-2S\), the unique maximum for \(d<1/2\) occurs at \(x_L\); if \(d=1/2\), both vertices are in their respective arcs and are the two distinct maximizers \(\alpha/(2S)\) and \(1-\alpha/(2S)\). At \(d=0\), the coincident-atom case has unique maximizer \(x=1/2\). Substitution and cancellation give
\[
\mathcal K=\frac1{12M^2}+\frac S{4M}-\frac{\alpha\beta\,d(d+S)}{SM^2}.
\]
The exact equality functions are the nonzero scalar multiples of the corresponding \(G_x\) for one of these norming points.

**3. Sharp design and quantitative deficit.** For fixed \(S>0\), the negative correction is strictly increased in magnitude by increasing \(d\in[0,1/2]\) and by maximizing \(\alpha\beta\) subject to \(\alpha+\beta=S\). Both maxima are uniquely at \(d=1/2\) and \(\alpha=\beta=S/2\). This gives \(\mathcal K_*(S)\) as stated. Writing \(S^2-4\alpha\beta=(\alpha-\beta)^2\) and factoring
\[
\frac14\left(\frac12+S\right)-d(d+S)=\left(\frac12-d\right)\left(\frac12+d+S\right)
\]
produces the exact nonnegative deficit identity. Because \(\alpha\beta>0\), the deficit vanishes only at the balanced antipodal design. Every sharp constant and equality condition follows from the Hilbert-space identity and the explicit quadratics, not from numerical sampling.

## Verification

The included `checker.py` uses exact rational arithmetic to reconstruct the periodic derivative-dual evaluation norm directly by interval integration, independent of the resistance-kernel closed formula. It tests all \(125\) profiles formed from two five-element mass sets and five separations, compares \(2765\) evaluation values, confirms each critical-point maximum and the exact design deficit, and verifies the balanced-antipodal instance \(\mathcal K=19/192\) for \(S=1\). Run `python3 checker.py` from the folder containing the file. These finite checks are consistency tests; the preceding analytical proof establishes every real admissible parameter.

## Relationship to prior work

The standard periodic Green/resistance identity and Sobolev Riesz-representation method are established tools and are not asserted to be novel. Hardin–Kendall–Saff prove equal-spacing optimality for a class of *unweighted discrete circle potentials* (arXiv:1208.5261, Theorem 1); that theory anticipates the equal-spacing aspect of some potential comparisons, but it neither supplies this weighted-mean Hilbert evaluation norm with its double-energy correction nor its exact mass/position defect and evaluation-extremizer formulas. Buttazzo–Ruffini–Velichkov study geometric Dirichlet-energy shape optimization for metric graphs, including Sobolev spaces but using prescribed Dirichlet anchors rather than movable mean-constraint atoms. Exner studies ground-state eigenvalues of point-interaction Schrödinger operators, a different functional from the reciprocal point-evaluation energy norm here. These comparisons support, but cannot certify, originality against all unpublished or unindexed work.

## Limitations

The circle has unit arclength background density, the weights are strictly positive, the constraint is *weighted mean zero* rather than Dirichlet pinning, and the energy uses one periodic derivative. Coalescent atoms \(d=0\) are included algebraically. The result does not cover more than two atoms, unequal background densities, higher derivatives, or the classification of optimal designs for other functionals. Independent review has not been performed; related unindexed two-point interpolation literature remains a residual originality risk.

## References

1. D. P. Hardin, A. P. Kendall, E. B. Saff, “Polarization optimality of equally spaced points on the circle for discrete potentials,” arXiv:1208.5261 (first public version 2012-08-26), https://arxiv.org/abs/1208.5261. Theorem 1 and its proof.
2. G. Buttazzo, B. Ruffini, B. Velichkov, “Shape Optimization Problems for Metric Graphs,” publicly deposited 2012-09-21, https://cvgmt.sns.it/paper/1923/, sections 1–4; later ESAIM COCV 20 (2014), 1–22.
3. P. Exner, “An optimization problem for finite point interaction families,” arXiv:1906.01229 (2019), https://arxiv.org/abs/1906.01229; comparison concerns its circle point-interaction eigenvalue objective, not the present energy-evaluation quantity.
