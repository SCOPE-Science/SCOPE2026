# Eight-to-two positive inverse branches near extinction in a cyclic Lotka–Volterra map

## Finding

For the cyclic three-species discrete Lotka–Volterra map, the positive inverse multiplicity of sufficiently small **strictly positive** observations is exactly eight in the weak-competition chamber and two whenever at least one interaction coefficient is above one, away from the coordinate transition surfaces. The extinction observation itself can have eight nonnegative inverse images in **both** the weak- and strong-competition chambers. Thus eight boundary inverse states in the strong-competition chamber collapse to only two biologically positive inverse states for *every* sufficiently small positive observation.

Precisely, let
\[
F_{R,\alpha,\beta}(x,y,z)=\begin{pmatrix}
x[1+R(1-x-\alpha y-\beta z)]\\
y[1+R(1-\beta x-y-\alpha z)]\\
z[1+R(1-\alpha x-\beta y-z)]
\end{pmatrix},\quad h=1+R^{-1}.
\]
For each fixed \(R,\alpha,\beta>0\), with \(\alpha\ne1\), \(\beta\ne1\), there exists \(\varepsilon>0\) such that
\[
\#\{p\in(0,\infty)^3:F_{R,\alpha,\beta}(p)=u\}
=\begin{cases}
8,&0<\alpha<1,\quad0<\beta<1,\\
2,&\max\{\alpha,\beta\}>1,
\end{cases}
\]
for **every** \(u\in(0,\infty)^3\) with \(\|u\|_\infty<\varepsilon\). In contrast,
\[
\#\left(F^{-1}_{R,\alpha,\beta}(0)\cap[0,\infty)^3\right)
=\begin{cases}
8,&(\alpha-1)(\beta-1)>0,\\
5,&(\alpha-1)(\beta-1)<0.
\end{cases}
\]
At \(\alpha=\beta=1\), the zero fiber is the origin together with the entire nonnegative triangle \(x+y+z=h\), whereas every sufficiently small strictly positive output still has exactly two strictly positive inverse images.

## Assumptions and scope

All parameters \(R,\alpha,\beta\) are fixed real positive numbers and the domain of the inverse problem is the **nonnegative** or **strictly positive** octant as explicitly indicated. The near-zero uniformity means that one \(\varepsilon>0\), depending on the parameters, works for every positive output in that cube; there is no asserted uniformity when parameters approach \(\alpha=1\) or \(\beta=1\). The mixed cases with one interaction exactly one and the other different are not classified. The assertion concerns one-step inverse images, not all real preimages, not their dynamical basins, and not a forward-invariant positive domain.

## Proof

**1. Exact zero fiber.** Write \(p=(x,y,z)\), and let
\[
C=\begin{pmatrix}1&\alpha&\beta\\\beta&1&\alpha\\\alpha&\beta&1\end{pmatrix}.
\]
Each component is \(F_i(p)=R p_i(h-(Cp)_i)\). Thus a nonnegative zero preimage has, for each coordinate, either \(p_i=0\) or \((Cp)_i=h\). Its support partitions the solution into four types.

For empty support there is only \(0\). On each of the three singleton supports there is the axial point \(h e_i\). On the support \(z=0\), \(x,y>0\), the two equations yield
\[
x=\frac{h(1-\alpha)}{1-\alpha\beta},\qquad
y=\frac{h(1-\beta)}{1-\alpha\beta}.
\]
The other two pairs are obtained by cyclic rotation. They exist precisely when both \(\alpha,\beta<1\) or both \(\alpha,\beta>1\). When \(\alpha\beta=1\) and \(\alpha\ne1\), the two support equations are inconsistent. Finally, on full support, \(Cp=h\mathbf 1\). Since
\[
\det C=(1+\alpha+\beta)\,D,\qquad
D=\frac{(\alpha-1)^2+(\beta-1)^2+(\alpha-\beta)^2}{2},
\]
for \((\alpha,\beta)\ne(1,1)\) there is exactly one full-support point \(p_*=(h,h,h)/(1+\alpha+\beta)\), which is positive. This proves the zero-fiber counts \(1+3+3+1=8\) or \(1+3+0+1=5\).

**2. Regularity and signs of the local inverse sheets.** The Jacobian is
\[
(DF(p))_{ij}=R\delta_{ij}(h-(Cp)_i)-R p_i C_{ij}.
\]
At the origin it equals \((R+1)I\). At an axial preimage, the two zero-coordinate diagonal Jacobian entries are \((R+1)(1-\alpha)\) and \((R+1)(1-\beta)\), while its occupied-coordinate diagonal is \(-(R+1)\); the matrix is triangular up to simultaneous permutation. For a nearby target \(u>0\), each missing coordinate satisfies the exact identity \(p_i=u_i/[R(h-(Cp)_i)]\). The bracket stays of the same nonzero sign as at the axial root. Hence both missing coordinates are positive exactly if \(\alpha,\beta<1\); if a coefficient exceeds one, a missing coordinate is negative for every strictly positive small target, irrespective of how small its individual components are relative to each other.

At a two-coordinate preimage the occupied \(2\times2\) Jacobian block equals \(-R\operatorname{diag}(x,y)\begin{pmatrix}1&\alpha\\\beta&1\end{pmatrix}\), with nonzero determinant \(R^2xy(1-\alpha\beta)\). The missing-coordinate multiplier is
\[
\mu_{\rm missing}=(R+1)\frac{D}{1-\alpha\beta}.
\]
It is positive when \(\alpha,\beta<1\) and negative when \(\alpha,\beta>1\). The exact factorization \(u_{\rm missing}=p_{\rm missing}R(h-(Cp)_{\rm missing})\), with the second factor maintaining its nonzero sign near the root, shows that the inverse missing coordinate is respectively positive or negative for **every** small positive target, including targets approaching coordinate faces at arbitrary rates. Both axial and two-coordinate Jacobians are nonsingular for the stipulated noncritical parameters. At the full-support point, \(DF(p_*)=-RhC/(1+\alpha+\beta)\) is nonsingular, and its local inverse stays strictly positive. The inverse near the origin is strictly positive for every small positive output because each exact factor \(R(h-(Cp)_i)\) remains positive near the origin and \(p_i=u_i/[R(h-(Cp)_i)]>0\). This factor argument, rather than a first-order remainder estimate, ensures positivity uniformly over **all** positive target directions. These are the claimed signs and local counts.

**3. No omitted positive inverse branches.** If \(p>0\) and \(F(p)=u>0\), then \((Cp)_i<h\) for all \(i\), since every factor \(p_i\) is positive. Because all entries of \(C\) are positive and \(C_{ii}=1\), necessarily \(0<p_i<h\). Thus all positive preimages lie in the same compact box \([0,h]^3\), independently of the small output. Suppose extra positive preimages existed for a sequence \(u_k\to0\). A subsequence would tend to one of the **finitely many** nonnegative zero preimages found in Step 1, but the inverse-function theorem supplies a unique local inverse in a neighborhood of each such regular root. Choosing disjoint neighborhoods of the finite zero fiber gives a contradiction. Hence the local inverse branches above enumerate all positive preimages, uniformly for sufficiently small positive outputs.

**4. Singular equal-interaction endpoint.** When \(\alpha=\beta=1\), all components share the factor \(q=1+R-R(x+y+z)\). The zero fiber is \(\{0\}\cup\{p\ge0:\sum p_i=h\}\). For a target \(u>0\) with \(T=\sum u_i\), any positive preimage must have \(q>0\) and \(p_i=u_i/q\). Therefore \(q^2-(1+R)q+RT=0\). For \(0<T<(1+R)^2/(4R)\), this quadratic has exactly two positive roots and gives exactly two positive preimages. This verifies the endpoint statement.

## Verification

`CHECK.py` uses only the Python standard library. Run `python3 CHECK.py` in the directory containing this result. It checks the exact rational zero fibers and Jacobian determinants for three parameter chambers, then exercises all local inverse sheets numerically for small positive outputs. The infinite/uniform quantifiers are proved by the compactness and inverse-function argument above, **not** by the finite tests.

## Relationship to prior work

Muni's 2024 three-dimensional cyclic Lotka–Volterra map explicitly raises the noninvertibility question in its model section, while its principal analyses concern torus bifurcations, periodic orbit transitions and hyperchaos. The present calculation answers a different, sharply posed backward-reconstruction question. Bischi and Tramontana (2010) explain inverse-sheet counts and critical sets for general discrete Lotka–Volterra maps, including a planar worked-out calculation; this supplies the conceptual framework but not the positive inverse-sheet count or the strong/weak competition distinction for the stated cyclic map. Prior published results on the same cyclic map's two-cycles and oscillatory instability do not entail the one-step inverse classification.

## Limitations

The result concerns the positive-competition subfamily only; the source's other interaction signs are not covered. No classification is asserted on the two transition hyperplanes with only one coefficient equal to one, nor for negative-coordinate preimages or general non-small targets. For this reason the eight-to-two law is not a global inverse-valence theorem. An unindexed equivalent algebraic analysis of general cyclic quadratic maps may already imply this classification; novelty is evaluated relative to the inspected sources, not certified by absence from searches. Independent mathematical audit has not been performed.

## References

1. S. S. Muni, *Torus and hyperchaos in 3D Lotka-Volterra map*, arXiv:2408.15054v1, public 27 August 2024, https://arxiv.org/pdf/2408.15054, especially §2 and §3–7.
2. G. I. Bischi and F. Tramontana, *Three-dimensional discrete-time Lotka–Volterra models with an application to industrial clusters*, Commun. Nonlinear Sci. Numer. Simul. 15 (2010), 3000–3014, https://doi.org/10.1016/j.cnsns.2009.10.021, especially §5 and Appendix B.
3. D. Blackmore, J. Chen, J. Perez and M. Savescu, *Dynamical properties of discrete Lotka–Volterra equations*, Chaos Solitons Fractals 12 (2001), 2553–2568, https://doi.org/10.1016/S0960-0779(00)00214-9 (planar related model).
