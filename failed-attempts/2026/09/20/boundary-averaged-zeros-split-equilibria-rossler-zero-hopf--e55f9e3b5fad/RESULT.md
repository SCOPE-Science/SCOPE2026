# Boundary averaged zeros shadow split equilibria in the classical Rössler zero-Hopf unfolding

## Statement

Consider the classical Rössler system
\[
\dot x=-y-z,\qquad
\dot y=x+ay,\qquad
\dot z=b+z(x-c),
\]
and the zero-Hopf unfolding used in arXiv:2609.17336v1,
\[
b=a+\varepsilon^2b_1,\qquad
c=2a+\varepsilon^2c_1,\qquad
|a|<\sqrt2,\qquad a(c_1-b_1)>0.
\]
Set
\[
\omega=\sqrt{2-a^2},\qquad \delta=c_1-b_1,\qquad k=\sqrt{a\delta}>0.
\]
The source applies first-order averaging after a linear change of variables, polar coordinates
\(u=r\cos\theta,\ v=r\sin\theta\), and the blow-up \(r=\varepsilon R,\ w=\varepsilon W\).  Its first averaged field has one interior zero \(P_0\) with \(R>0\) and two boundary zeros
\[
P_s=\left(0,s\frac{\omega^2 k}{a^2}\right),\qquad s=\pm1,
\]
and the source counts all three simple zeros as generators of distinct nontrivial periodic-orbit families.

The two boundary zeros have a different interpretation.  They are exactly the leading scaled images of the two equilibrium branches into which the zero-Hopf equilibrium splits.  Moreover, the two eigenvalues of the averaged Jacobian at each boundary zero exactly reproduce, after the natural time rescaling, the first-order real spectral drift rates of the corresponding split equilibrium.  Thus the boundary zeros do not by themselves certify two additional nonconstant periodic orbits.

The conclusion is deliberately limited: this does **not** prove that no smaller-amplitude periodic orbits exist near those branches by a higher-order or different-coordinate argument.  It shows that the first-order boundary-zero argument used in arXiv:2609.17336v1 does not distinguish such cycles from the exact split equilibria.

## 1. Exact equilibrium splitting

Every equilibrium with \(a\ne0\) satisfies
\[
y=-\frac{x}{a},\qquad z=\frac{x}{a},
\]
and the remaining equation reduces to
\[
x^2-cx+ab=0.
\]
Hence the two exact equilibrium branches are
\[
q_\sigma=(x_\sigma,-x_\sigma/a,x_\sigma/a),\qquad
x_\sigma=\frac{c+\sigma\sqrt{c^2-4ab}}2,\qquad \sigma\in\{+1,-1\}.
\]
For the source unfolding,
\[
c^2-4ab
=4a\varepsilon^2(c_1-b_1)+\varepsilon^4c_1^2
=4k^2\varepsilon^2+\varepsilon^4c_1^2.
\]
For \(\varepsilon>0\),
\[
\boxed{
 x_\sigma
 =a+\sigma k\varepsilon+\frac{c_1}{2}\varepsilon^2+O(\varepsilon^3).
}
\]
Thus the double equilibrium at \((a,-1,1)\) splits at order \(\varepsilon\), although the parameters themselves are perturbed only at order \(\varepsilon^2\).

## 2. The boundary averaged zeros are the scaled equilibrium branches

The source translates
\[
X=x-a,\qquad Y=y+1,\qquad Z=z-1
\]
and uses the linear coordinates
\[
X=u+\frac a\omega v-\frac{a^2}{\omega^2}w,
\]
\[
Y=-au+\frac{1-a^2}{\omega}v+\frac a{\omega^2}w,
\]
\[
Z=\frac1\omega v-\frac a{\omega^2}w.
\]
On either exact equilibrium branch, \(Y=-X/a\) and \(Z=X/a\).  Solving the displayed linear relations gives identically
\[
\boxed{u=v=0,\qquad w=-\frac{\omega^2}{a^2}(x-a).}
\]
Therefore every split equilibrium lies exactly on the polar axis \(r=0\).  In the source blow-up \(w=\varepsilon W\),
\[
W_\sigma(\varepsilon)
=-\frac{\omega^2}{2a^2}
\left(
\varepsilon c_1+\sigma\sqrt{4a(c_1-b_1)+\varepsilon^2c_1^2}
\right),
\]
so
\[
\boxed{
W_\sigma(\varepsilon)
=-\sigma\frac{\omega^2k}{a^2}+O(\varepsilon).
}
\]
Consequently
\[
\boxed{q_\sigma\longmapsto P_{-\sigma}\quad\text{as }\varepsilon\to0^+.}
\]
The two simple averaged zeros with \(R=0\) are therefore not merely located on the polar-coordinate singular set; their leading coordinates are precisely those of the two exact equilibrium branches.

This matters because \(\theta\) ceases to be a valid angular variable at \(r=0\).  Extending the reduced formulas analytically to \(R=0\) can be useful algebraically, but a fixed point of that extension is not automatically a nonconstant periodic orbit of the original Cartesian flow.  The exact equilibria provide the concrete competing branches that the boundary calculation must first exclude.

## 3. Exact spectral matching

At an equilibrium \((x,-x/a,x/a)\), the characteristic polynomial of the Cartesian Jacobian is
\[
\boxed{
p(\lambda)
=\lambda^3+(c-a-x)\lambda^2
+\left(1+\frac xa+a(x-c)\right)\lambda+c-2x.
}
\]
Substituting \(x=x_\sigma\) and expanding about the zero-Hopf point yields one real eigenvalue
\[
\boxed{
\lambda_{\mathrm{slow},\sigma}
=\sigma\frac{2k}{\omega^2}\varepsilon+O(\varepsilon^2),
}
\]
and a complex pair
\[
\boxed{
\lambda_{\pm,\sigma}
=\pm i\omega
-\sigma\frac{a^2k}{2\omega^2}\varepsilon
\pm i\,\sigma\frac{k(a+1/a)}{2\omega}\varepsilon
+O(\varepsilon^2).
}
\]
Thus both equilibrium branches are saddle-foci for sufficiently small positive \(\varepsilon\), with opposite stability signatures.

For the source averaged system, the Jacobian eigenvalues at
\[
P_s=\left(0,s\frac{\omega^2k}{a^2}\right)
\]
are
\[
\boxed{
\operatorname{spec}Dg(P_s)
=\left\{
 s\frac{a^2k}{2\omega^3},
 -s\frac{2k}{\omega^3}
\right\}.
}
\]
The equilibrium branch \(q_\sigma\) maps to \(P_{-\sigma}\).  Divide the first-order real parts of the Cartesian eigenvalues by the fast angular frequency \(\omega\):
\[
\left\{
\frac{\operatorname{Re}\lambda_{+,\sigma}}{\varepsilon\omega},
\frac{\lambda_{\mathrm{slow},\sigma}}{\varepsilon\omega}
\right\}
=\left\{
-\sigma\frac{a^2k}{2\omega^3},
\sigma\frac{2k}{\omega^3}
\right\}+O(\varepsilon).
\]
This is exactly
\[
\boxed{\operatorname{spec}Dg(P_{-\sigma})}
\]
at leading order.  The correspondence is therefore not only positional: the averaged linearization at each boundary zero carries the first-order stability data of the split equilibrium that approaches it.

## 4. Consequence for the three-family claim

The source's interior averaged zero \(P_0\) has \(R>0\), so it is not affected by this boundary-axis obstruction.  The issue is specific to \(P_\pm\), where the polar radius vanishes.

The exact equilibrium correspondence implies that the inference
\[
\text{simple averaged zero at }R=0
\quad\Longrightarrow\quad
\text{nontrivial periodic orbit of the original flow}
\]
requires an additional argument.  In this unfolding, there are already exact solution branches with precisely the same leading scaled coordinates and the same leading transverse growth rates.  First-order averaging in the singular polar chart does not separate them from a putative cycle whose oscillatory radius is smaller than the \(r=O(\varepsilon)\) scale.

Accordingly, the first-order computation supports one interior periodic-orbit candidate from \(P_0\), while the two boundary roots \(P_\pm\) cannot on their own establish two additional nonconstant families.  Any claim of such additional families requires, for example, a nonsingular Cartesian reduction, a higher-order radial calculation showing \(r>0\), or direct continuation/shooting that explicitly excludes the equilibrium branches.

The same qualification propagates to statements that specifically use \(\Gamma_{P_+ ,\varepsilon}\) or \(\Gamma_{P_- ,\varepsilon}\) as nontrivial periodic orbits in a Poincaré-multiplier argument.  This result does not assert that every non-integrability conclusion in the source fails: an interior periodic orbit may still supply an obstruction, and other arguments may remain valid.

## 5. Source numerical example

For the parameter choice displayed in the source,
\[
a=1,\qquad b_1=1,\qquad c_1=2,\qquad \varepsilon=1/500,
\]
one has \(\omega=1\), \(k=1\), and
\[
c^2-4ab=1.6000064\times10^{-5}.
\]
The exact equilibrium branches are approximately
\[
q_+=(1.002004004,-1.002004004,1.002004004),
\]
\[
q_-=(0.998003996,-0.998003996,0.998003996),
\]
with scaled coordinates
\[
W_+\approx-1.002002,\qquad W_-\approx0.998002,
\]
approaching the two averaged boundary values \(-1\) and \(+1\).  Their eigenvalues have the predicted opposite saddle-focus signatures; the verification artifact records the numerical values.

## Verification

`artifacts/verify_rossler_boundary_zeros.py` symbolically checks the exact equilibrium equations, the linear-coordinate restriction to the equilibrium line, the boundary-zero limit, the Cartesian characteristic polynomial, both first-order eigenvalue expansions, and the equality between the averaged boundary spectrum and the rescaled equilibrium spectral drift.  It also evaluates the source numerical example.  The recorded output is in `artifacts/verification.txt` and ends with `all_symbolic_checks_passed = True`.

## Originality boundary and prior literature

The general facts that polar coordinates are singular at zero radius, that zero-Hopf averaging requires attention to admissible domains, and that Rössler zero-Hopf bifurcations can be analyzed by averaging or normal forms are prior art.  Llibre's earlier zero-Hopf work obtained a periodic orbit through a positive-radius averaged solution.  Cândido, Novaes and Valls developed higher-order averaging results for periodic solutions and invariant tori in Rössler-type zero-Hopf regimes, and Zeng and Yu used normal-form theory to explain cases in which averaging can fail or become degenerate.  None of those general methodological points is claimed here as new.

To the best of our knowledge, the contribution here is the source-specific observation for arXiv:2609.17336v1 that its two new boundary roots \(P_\pm\) are the leading scaled images of the exact equilibrium branches of the same unfolding, together with the exact matching of their averaged Jacobian eigenvalues to the first-order equilibrium spectral drifts.  That correspondence directly changes what the two boundary roots can establish about nontrivial periodic-orbit families.

The literature search was not exhaustive over every Rössler normal-form calculation.  The 2020 Rössler zero-Hopf literature was inspected at the level of its accessible full arXiv text where available, while algebraically equivalent remarks may still occur under different coordinates or terminology.  No broad priority claim is made for the underlying polar-coordinate principle.

## Limitations

This result is a correction of an inference, not a nonexistence theorem for all nearby cycles.  A periodic orbit with oscillatory radius of smaller order than \(\varepsilon\) could in principle exist and require a higher-order calculation.  No computer-assisted exclusion of such cycles is supplied.  The interior root \(P_0\) is not challenged by the boundary argument.  The result also does not independently re-prove or refute every local \(C^1\)-non-integrability conclusion in arXiv:2609.17336v1; only those steps that require the two boundary roots to represent nonconstant periodic orbits need reassessment.

## References

1. J. Llibre, W. Szumiński, *Zero-Hopf bifurcation, periodic orbits and C1 non-integrability of the classical Rössler system*, arXiv:2609.17336v1 (2026). https://arxiv.org/abs/2609.17336v1
2. J. Llibre, *Periodic orbits in the zero-Hopf bifurcation of the Rössler system*, Romanian Astronomical Journal 24 (2014), 49–60.
3. M. R. Cândido, D. D. Novaes, C. Valls, *Periodic solutions and invariant torus in the Rössler system*, Nonlinearity 33 (2020), 4512–4539. https://doi.org/10.1088/1361-6544/ab8bae
4. B. Zeng, P. Yu, *Analysis of Zero-Hopf Bifurcation in Two Rössler Systems Using Normal Form Theory*, International Journal of Bifurcation and Chaos 30 (2020), 2030050. https://doi.org/10.1142/S0218127420300505
