# Two-scale conditional localization at the first random lattice-disk coverage transition

## Finding

Let \(U=(U_1,U_2)\) be uniform on \([0,1)^2\). For \(0<\varepsilon<1/16\), write \(R_\varepsilon=\sqrt{1/2+\varepsilon}\) and let \(N_\varepsilon\) be the number of square-lattice points lying in the closed disk of radius \(R_\varepsilon\) centered at \(U\). Define folded coordinates \(s=|U_1-1/2|\) and \(t=|U_2-1/2|\). The first positive-area digitization occurs when \(N_\varepsilon\ge3\); the square digitization occurs when \(N_\varepsilon=4\).

**Conditional three-point localization.** On \(N_\varepsilon\ge3\), set
\[
X_\varepsilon=\frac{s+t}{2\sqrt\varepsilon},\qquad
Y_\varepsilon=\frac{s-t}{\varepsilon}.
\]
Their exact conditional joint law is uniform on
\[
H_\varepsilon=\left\{(x,y):x\ge\frac{\sqrt\varepsilon}{2}|y|,\quad
|y|+2x^2+\frac\varepsilon2y^2\le1\right\}.
\]
For \(N_\varepsilon=3\), their exact law is uniform on the subset \(H_\varepsilon\setminus F_\varepsilon\), where \(F_\varepsilon\) is the image of the four-point event under the same transformation. Both conditional laws converge **in total variation** to the uniform distribution \(\mathsf U(H)\) on the *parabolic cap*
\[
H=\{(x,y):x\ge0,\quad |y|+2x^2\le1\},\qquad |H|=\frac4{3\sqrt2}.
\]
The convergence is sharp, with distinct first-order constants:
\[
\boxed{\begin{aligned}
d_{\rm TV}(\mathcal L((X_\varepsilon,Y_\varepsilon)\mid N_\varepsilon\ge3),\mathsf U(H))
 &=\frac{3\sqrt2}{8}\sqrt\varepsilon+O(\varepsilon),\\
d_{\rm TV}(\mathcal L((X_\varepsilon,Y_\varepsilon)\mid N_\varepsilon=3),\mathsf U(H))
 &=\frac{3\sqrt2}{4}\sqrt\varepsilon+O(\varepsilon).
\end{aligned}}
\]
Consequently, conditioned on either event, the rescaled Euclidean distance of the disk center from the square center, \(\|U-(1/2,1/2)\|_2/\sqrt\varepsilon\), converges weakly to a variable \(Z\) with density
\[
\boxed{f_Z(z)=\tfrac32(1-z^2)\mathbf1_{\{0\le z\le1\}}.}
\]

**Conditional four-point localization.** On \(N_\varepsilon=4\), put
\[
S_\varepsilon=s/\varepsilon,\qquad T_\varepsilon=t/\varepsilon.
\]
The exact joint law is uniform on
\[
K_\varepsilon=\{(r,q):r,q\ge0,\quad r+q+\varepsilon(r^2+q^2)\le1\}.
\]
It converges in total variation to \(\mathsf U(K)\), uniform on the triangle \(K=\{r,q\ge0:r+q\le1\}\), with the **sharper linear rate**
\[
\boxed{d_{\rm TV}(\mathcal L((S_\varepsilon,T_\varepsilon)\mid N_\varepsilon=4),\mathsf U(K))
=\frac43\varepsilon+O(\varepsilon^2).}
\]
The reflected coordinate signs are independent fair signs under each conditioning event, and independent of the folded coordinates. Thus these distributions also describe the full conditional spatial locations after a uniform choice of quadrant. The finding separates a square-root longitudinal and linear transverse spatial scale for triangles from two linear scales for squares, rather than merely distinguishing their known occurrence probabilities.

## Assumptions and scope

All lattice points on the closed disk boundary are counted; this convention changes only a null set of uniform shifts. The lattice is \(\mathbb Z^2\) with Euclidean unit spacing. The restrictions \(0<\varepsilon<1/16\) ensure \(R_\varepsilon<1\) and keep the displayed critical regions inside the fundamental square. Conditional distributions refer only to events of positive probability; for this range all three events \(N_\varepsilon\ge3\), \(N_\varepsilon=3\), and \(N_\varepsilon=4\) have positive probability. Total-variation distance is \(\sup_B|\mu(B)-\nu(B)|\), equal to half the \(L^1\) distance of densities. The random shift, not the lattice, is uniform; uniform lattice rotations are immaterial for a round disk.

## Proof

**1. Exact coverage inequalities.** Because \(R_\varepsilon<1\), the disk cannot contain a lattice point outside the four corners of the fundamental unit square. The four squared corner distances, in descending order, are
\[
\frac12+s^2+t^2+s+t,\quad
\frac12+s^2+t^2+|s-t|,\quad
\frac12+s^2+t^2-|s-t|,\quad
\frac12+s^2+t^2-s-t.
\]
Therefore
\[
N_\varepsilon\ge3\iff s^2+t^2+|s-t|\le\varepsilon,
\qquad
N_\varepsilon=4\iff s^2+t^2+s+t\le\varepsilon.
\]
These are necessary and sufficient for every admissible \(\varepsilon\), not approximations. The four sign quadrants of \(U-(1/2,1/2)\) contribute equally by reflection symmetry. Conditional on the folded pair \((s,t)\), the signs are independent fair bits. The folded density is the constant four on \([0,1/2]^2\).

**2. Exact scaled conditional distributions.** The invertible linear transformation on folded coordinates for three-point localization has
\[
s=\sqrt\varepsilon\,x+\tfrac\varepsilon2y,\qquad
t=\sqrt\varepsilon\,x-\tfrac\varepsilon2y,
\qquad |\det(\partial(s,t)/\partial(x,y))|=\varepsilon^{3/2}.
\]
Substitution into the first coverage inequality gives exactly \(H_\varepsilon\), and its boundary constraints imply \(0\le s,t<1/2\). Because the Jacobian and folded density are constant, conditioning yields the uniform law on \(H_\varepsilon\). Let \(F_\varepsilon\subset H_\varepsilon\) be the image of the four-point event; removing it yields the exact three-point law. For the four-point event, write \(s=\varepsilon r,t=\varepsilon q\); the second coverage inequality becomes exactly \(K_\varepsilon\), again with constant Jacobian. Thus all three laws are uniform on the stated domains.

**3. Geometry and sharp area expansions.** All the sets are nested inside their limiting shapes: \(H_\varepsilon\subset H\), \(H_\varepsilon\setminus F_\varepsilon\subset H\), and \(K_\varepsilon\subset K\). Direct integration gives \(|H|=4/(3\sqrt2)\) and \(|K|=1/2\). For \(0\le y\le y_\varepsilon=2/(1+\sqrt{1+4\varepsilon})\), the positive-\(y\) slice of \(H_\varepsilon\) runs from \(x=\sqrt\varepsilon\,y/2\) to \(x=\sqrt{(1-y-\varepsilon y^2/2)/2}\). Consequently,
\[
|H_\varepsilon|=2\int_0^{y_\varepsilon}
\left[\sqrt{\frac{1-y-\varepsilon y^2/2}{2}}-\frac{\sqrt\varepsilon}{2}y\right]\,dy
=\frac4{3\sqrt2}-\frac12\sqrt\varepsilon+O(\varepsilon).
\]
The integral's square-root term changes by \(O(\varepsilon)\) from its value at zero, by integrable endpoint comparison, while the lower boundary contributes exactly \(-\sqrt\varepsilon\,y_\varepsilon^2/2=-\sqrt\varepsilon/2+O(\varepsilon^{3/2})\).

For the four-point region, solve the top boundary \(q+\varepsilon q^2=1-r-\varepsilon r^2\). Its first-order displacement from \(q=1-r\) is \(-\varepsilon[r^2+(1-r)^2]\). Integrating the displacement and bounding the endpoint correction, which is \(O(\varepsilon^2)\), gives
\[
|K_\varepsilon|=\frac12-\varepsilon\int_0^1\bigl(r^2+(1-r)^2\bigr)\,dr+O(\varepsilon^2)
=\frac12-\frac23\varepsilon+O(\varepsilon^2).
\]
The transformation from four-point \((r,q)\) to three-point \((x,y)\) coordinates is \(x=\sqrt\varepsilon(r+q)/2,\ y=r-q\), with absolute determinant \(\sqrt\varepsilon\). Hence \(|F_\varepsilon|=\sqrt\varepsilon\,|K_\varepsilon|\). In particular,
\[
|H_\varepsilon\setminus F_\varepsilon|=\frac4{3\sqrt2}-\sqrt\varepsilon+O(\varepsilon).
\]

**4. Exact total-variation reduction.** If \(B\subset A\) are measurable regions of finite positive area, the total-variation distance between their uniform laws is exactly \(1-|B|/|A|\): integrating the two piecewise-constant densities proves the identity. Apply it to \(H_\varepsilon\subset H\), \(H_\varepsilon\setminus F_\varepsilon\subset H\), and \(K_\varepsilon\subset K\), then substitute the preceding area expansions. This yields respectively \((3\sqrt2/8)\sqrt\varepsilon+O(\varepsilon)\), \((3\sqrt2/4)\sqrt\varepsilon+O(\varepsilon)\), and \((4/3)\varepsilon+O(\varepsilon^2)\). The constants are nonzero, so these rates cannot be improved in order.

**5. Radial and quadrant consequences.** Under \(\mathsf U(H)\), the density of \(X\) is \((3\sqrt2/2)(1-2x^2)\) on \(0\le x\le1/\sqrt2\). Since \(\sqrt{s^2+t^2}/\sqrt\varepsilon=\sqrt{2X_\varepsilon^2+\varepsilon Y_\varepsilon^2/2}\), convergence in total variation of the two-dimensional conditional coordinate laws, together with the uniform bound \(\big|\sqrt{2X_\varepsilon^2+\varepsilon Y_\varepsilon^2/2}-\sqrt2 X_\varepsilon\big|\le\sqrt{\varepsilon/2}\) on \(H_\varepsilon\), imply the weak radial limit \(Z=\sqrt2X\). Its density is \((3/2)(1-z^2)\) on \([0,1]\). Reflection invariance gives the exact independent quadrant-sign assertion.

## Verification

The accompanying stand-alone Python script `verify.py` is standard-library only. It independently enumerates all four corner distances with exact rational arithmetic, comparing the number of covered points with the two derived inequalities on a deterministic grid of parameters. It then numerically integrates the exact critical regions for four decreasing positive values of \(\varepsilon\) and checks their total-variation ratio approaches the three predicted sharp constants. It also independently integrates the limiting parabolic-cap area. Running `python verify.py` prints `GEOMETRIC_TWO_SCALE_CHECKS_PASSED 12697`. The exact rational checks and numerical quadratures are finite corroboration; the proof for all admissible \(\varepsilon\) is the analytical argument above.

## Relationship to prior work

Schlie's 2026 survey of randomized lattice-point counts motivates the random-translation model and emphasizes its geometric aspects. The publicly available result *A three-atom area law and two critical exponents for randomly translated lattice-disk hulls* already gives the exact unconditioned hull-area probabilities for \(1/\sqrt2<R<1\), including the \(\varepsilon^{3/2}\) and \(\varepsilon^2\) onset exponents. Those unconditioned probabilities, the first nondegenerate radius, and the geometric inequalities in that work are **not claimed as new** here. Its full proof was compared: it does not state or establish the two different conditional center-location scaling laws, the parabolic-cap and triangle spatial limits, or the three sharp total-variation convergence coefficients. The new object is the *conditional location distribution*, not the marginal hull area. Earlier large-radius digitization counting and randomized convex-hull asymptotics consider different scales or summaries.

## Limitations

The theorem concerns the first critical radius chamber for the square lattice and a circular disk, and makes no claim about arbitrary lattices, other convex bodies or larger radii. The new conditional laws are elementary consequences of locally quadratic corner-distance geometry, and priority remains uncertain without exhaustive older digital-image literature. A potentially relevant older full text, *Different Digitisations of Displaced Discs* (Huxley and Žunić, 2006), could not be inspected in full: its institutional PDF retrieval required a disconnected VPN. Its accessible abstract concerns numbers of distinct digitizations at large radii, rather than the present conditional near-onset laws, but unexamined content is a residual originality risk. No independent mathematical audit has been performed.

## References

1. Steffen Schlie, *On the randomized lattice-point count problem*, arXiv:2611.16769v1, first public 12 November 2026, https://arxiv.org/abs/2611.16769. Relevant manuscript sections inspected.
2. *A three-atom area law and two critical exponents for randomly translated lattice-disk hulls*, published mathematical record dated November 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-three-atom-area-law-and-two-critical-exponents-for-randomly-tr--1098c654ec0a/RESULT.md. Full result and proof inspected; unconditioned laws credited explicitly.
3. I. Bárány and J. Matoušek, *The Randomized Integer Convex Hull*, Discrete & Computational Geometry 33 (2005), 3–25, DOI 10.1007/s00454-003-0836-1.
4. M. N. Huxley and J. Žunić, *Different Digitisations of Displaced Discs*, Foundations of Computational Mathematics 6 (2006), 255–268, DOI 10.1007/s10208-005-0177-y. Only abstract inspected; no accessible complete PDF.
