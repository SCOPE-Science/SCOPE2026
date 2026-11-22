# An exact global separatrix and two expanding scales in a three-dimensional parabolic map

## Finding

Consider the polynomial self-map of the full real space introduced in Wang et al. (2023), restricted to the natural parameter surface \(c=1\):
\[
F_{a,b}(x,y,z)=\bigl(a y^2,\ b y(1-z),\ 1-x\bigr),\qquad a,b>0.
\]
Let \(r\in(1,2)\) be the unique real root of \(r^3-r^2-2=0\), and put \(s=\sqrt{2/r}>1\). Define the nonnegative, continuous function
\[
H_{a,b}(x,y,z)=(ab)^{r^2/2}b^{r+1}|x|\,|y|^{r^2}|1-z|^r.
\]
Then the exact nonlinear identity
\[
\boxed{\ H_{a,b}(F_{a,b}(p))=H_{a,b}(p)^r\ }
\]
holds on all of \(\mathbb R^3\), including the coordinate-zero sets (where \(0^r=0\)). The following is a *complete global forward-orbit trichotomy*.

**Extinction:** For \(H_{a,b}(p)<1\), every forward orbit converges to \(E_0=(0,0,1)\).

**Escape:** For \(H_{a,b}(p)>1\), every forward orbit satisfies \(|y_n|\to\infty\), \(x_n\to+\infty\), and \(z_n\to-\infty\).

**Critical surface:** For \(H_{a,b}(p)=1\), precisely the eight points with
\[
\bigl(|x|,|y|,|1-z|\bigr)=\left(\frac1b,\frac1{\sqrt{ab}},\frac1b\right)
\]
are eventually fixed; each reaches, within two iterations, one of the two nonzero equilibria
\[
E_\pm=\left(\frac1b,\ \pm\frac1{\sqrt{ab}},\ 1-\frac1b\right).
\]
Every other critical orbit has simultaneously
\[
\boxed{\ \liminf_{n\to\infty}|y_n|=0,\qquad \limsup_{n\to\infty}|y_n|=+\infty.\ }
\]
Thus the unbounded, nonconvergent critical oscillations occur *exactly on the boundary* between extinction and coherent escape, except for eight preperiodic points. More precisely, writing \(L_n=\log(\sqrt{ab}\,|y_n|)\) for any orbit with \(H(p)>0\),
\[
L_n=\frac{\log H(p)}{3r^2-2r}\,r^n+O_p(s^n),\qquad n\to\infty,
\]
while on the nonexceptional critical surface there are real \(A,B\), not both zero, and \(\theta\in(0,\pi)\) determined by the complex roots of \(\lambda^3-\lambda^2-2\), such that the *exact* identity \(L_n=s^n(A\cos n\theta+B\sin n\theta)\) holds for every \(n\ge0\).

The only recurrent points are the three equilibria \(E_0,E_+,E_-\). Every invariant Borel probability measure on \(\mathbb R^3\) is therefore precisely a convex combination of their Dirac masses; in particular, there are no nontrivial periodic orbits. Both nonzero equilibria are hyperbolic repellers, whereas \(E_0\) has nilpotent derivative and basin of attraction exactly \(\{H<1\}\).

## Assumptions and scope

The parameters \(a,b\) are arbitrary positive real numbers; the third parameter \(c\) of the 2023 three-dimensional parabolic map is **exactly one**, not a small nonzero perturbation. All claims concern deterministic forward iterates on **all** real initial states. Define \((x_n,y_n,z_n)=F_{a,b}^n(x_0,y_0,z_0)\), with \(F^0\) the identity. Every iterate exists because the map is polynomial. The function \(H\) uses the usual nonnegative real fractional powers, and logarithmic expressions are used only when \(H>0\) (equivalently \(x_0y_0(1-z_0)\ne0\)). The notation \(O_p(s^n)\) allows a constant dependent on the particular starting state and on \(a,b\), but not on \(n\).

For fixed \(y_0\ne0\) and \(z_0\ne1\), the sharp extinction–escape threshold for the remaining initial coordinate is
\[
X_c(y_0,z_0)=(ab)^{-r^2/2}b^{-(r+1)}|y_0|^{-r^2}|1-z_0|^{-r}.
\]
Specifically \(|x_0|<X_c\) implies extinction, \(|x_0|>X_c\) implies escape, and equality gives the critical cases described above. The threshold is nontrivial: both sides are nonempty, and every strictly positive point of the critical surface is a nonstationary oscillatory point except where it equals \(E_+\).

## Proof

**1. Eliminate the delayed coordinates.** The third equation gives \(1-z_{n+1}=x_n\). Consequently,
\[
y_{n+3}=b y_{n+2}(1-z_{n+2})=b y_{n+2}x_{n+1}=ab\,y_{n+2}y_n^2\qquad(n\ge0).
\]
The first three data in this exact scalar recurrence are
\[
y_0=y_0,\quad y_1=b y_0(1-z_0),\quad y_2=b^2y_0(1-z_0)x_0.
\]
If one of \(x_0,y_0,1-z_0\) vanishes, a term among \(y_0,y_1,y_2\) vanishes and the recurrence shows that \(y_n=0\) for all sufficiently large \(n\). The first and third map equations then yield convergence (indeed finite-time arrival) at \(E_0\). These are exactly the points with \(H=0\).

**2. Exact logarithmic linearization on the nonzero locus.** Put \(\kappa=\sqrt{ab}\) and \(L_n=\log(\kappa|y_n|)\); nonzero initial coordinates ensure no \(y_n\) vanishes. The scalar recurrence becomes
\[
L_{n+3}=L_{n+2}+2L_n.
\]
For \(U_n=(L_n,L_{n+1},L_{n+2})^\mathsf T\), the transition is \(U_{n+1}=MU_n\), where
\[
M=\begin{pmatrix}0&1&0\\0&0&1\\2&0&1\end{pmatrix},\qquad
\det(\lambda I-M)=\lambda^3-\lambda^2-2.
\]
The polynomial is negative at its two real critical points and changes sign from negative at \(1\) to positive at \(2\). Hence it has exactly one real root \(r\in(1,2)\); its other roots are a nonreal conjugate pair \(\zeta,\overline\zeta\). Their product gives \(|\zeta|=s=\sqrt{2/r}>1\). Also \(s<r\) since \(r^3=r^2+2>2\).

The positive left Perron eigenvector is \(w=(r^2-r,r-1,1)\), and the corresponding right eigenvector is \(v=(1,r,r^2)\). Direct multiplication, using the root equation, gives \(wM=rw\), \(Mv=rv\), and \(w\cdot v=3r^2-2r>0\). Thus the real number \(\Phi=w\cdot U_0\) obeys \(w\cdot U_n=r^n\Phi\). Expanding \(U_0\) in terms of \(x_0,y_0,z_0\), one obtains the exact formula
\[
\begin{aligned}
\Phi&=(r^2-r)L_0+(r-1)L_1+L_2\\
&=\log\bigl((ab)^{r^2/2}b^{r+1}|x_0|\,|y_0|^{r^2}|1-z_0|^r\bigr)=\log H(p).
\end{aligned}
\]
Since the Perron eigenvalue is simple and dominates the other two in modulus, the exact spectral decomposition gives
\[
L_n=\frac{\Phi}{w\cdot v}r^n+O_p(s^n).
\]
The same eigenvector identity applied at \(F(p)\) gives \(\log H(Fp)=r\log H(p)\) on the nonzero locus, and continuity of \(H\), \(F\) and the nonnegative power function extends \(H(Fp)=H(p)^r\) over the coordinate-zero sets.

**3. The strict regions and their physical coordinates.** If \(0<H(p)<1\), then \(\Phi<0\); the spectral estimate and \(s<r\) force \(L_n\to-\infty\), so \(y_n\to0\). The exact map identities \(x_{n+1}=a y_n^2\) and \(z_{n+1}=1-x_n\) then yield \((x_n,y_n,z_n)\to E_0\). The case \(H=0\) was resolved in Step 1. If \(H(p)>1\), then \(\Phi>0\), hence \(L_n\to+\infty\), \(|y_n|\to\infty\), \(x_n\to+\infty\), and \(z_n\to-\infty\). This proves the sharp basin assertion and the double-exponential logarithmic growth law.

**4. The entire critical surface.** Suppose \(H(p)=1\), so \(\Phi=0\). The real spectral subspace \(\ker w\) is exactly the span of the complex-eigenvalue pair, and \(M\) acts there as a real linear conjugate of multiplication by \(\zeta=s e^{i\theta}\), with \(0<\theta<\pi\). If \(U_0\ne0\), the real scalar coordinate of the iterates has the exact form
\[
L_n=s^n\bigl(A\cos(n\theta)+B\sin(n\theta)\bigr),
\]
with \((A,B)\ne(0,0)\); otherwise \(L_n\equiv0\) and \(U_0=0\). The oscillating factor takes values greater than a fixed positive \(\delta\) and smaller than \(-\delta\) for infinitely many positive integers \(n\). If \(\theta/(2\pi)\) is irrational this follows from density of circle rotations; if rational, it follows because the nonzero cosine function has zero average over its finite orbit and is not identically zero (the rotation has order at least three, since \(\zeta\) is nonreal). Since \(s>1\), the positive and negative subsequences of \(L_n\) diverge in opposite directions. Exponentiation proves the asserted \(\liminf\) and \(\limsup\) of \(|y_n|\).

If \(U_0=0\), then \(|y_0|=|y_1|=|y_2|=1/\kappa\). Substitution into the initial-data identities in Step 1 gives \(|x_0|=|1-z_0|=1/b\). Conversely all eight independent sign choices of \(x_0,y_0,1-z_0\) with those magnitudes give \(U_0=0\); after two iterations, the state has \(x_2=1/b\), \(1-z_2=1/b\), \(|y_2|=1/\kappa\), which is precisely \(E_+\) or \(E_-\). Thus there are exactly eight exceptional critical initial states, and all remaining critical states exhibit the claimed infinite oscillatory bursts.

**5. Recurrent points, invariant measures and linear stability.** The only fixed points are \(E_0,E_+,E_-\): at a fixed point \(x=ay^2\), \(z=1-x\), and \(y=bxy\), forcing either \(y=0\) or \(x=1/b\). The strict-region orbits cannot be recurrent except at \(E_0\). A nonexceptional critical orbit cannot be recurrent either: its nonzero logarithmic three-vector evolves as \(M^nU_0\), whose norm diverges like \(s^n\) because the restriction of \(M\) to \(\ker w\) is conjugate to an expanding rotation. Recurrence in physical coordinates would, by continuity of three successive \(y\)-coordinates and their logarithms near the nonzero initial point, force a bounded subsequence of those logarithmic three-vectors, a contradiction. The remaining six nonfixed exceptional points become fixed after finitely many iterations and are not recurrent. Therefore the recurrent points are exactly the three equilibria, proving also that no other periodic points exist. Poincaré recurrence for any invariant Borel probability on this second-countable space puts full mass on the recurrent set, so every invariant probability is a convex mixture of the three Dirac measures; the converse is immediate.

At \(E_0\), the derivative of \(F\) is nilpotent, with all eigenvalues zero. At either \(E_\pm\), the Jacobian has characteristic polynomial \(\lambda^3-\lambda^2-2\); its eigenvalues are \(r,\zeta,\overline\zeta\), all strictly outside the unit circle because \(r>1\) and \(s>1\). Thus both nonzero equilibria are hyperbolic repellers. This completes the global classification.

## Verification

The standalone `checker.py` requires only Python 3's standard library. From the directory containing this document and the checker, execute `python checker.py`. It reports `PASS: 336 exact rational recurrence comparisons, 401 log-eigenfunction tests, 12 threshold/exception tests` and approximate spectral radii \(r=1.695620769559862\), \(s=1.086052035863345\). The checker compares the exact scalar reduction across 336 rational examples, tests the nonlinear eigenfunction identity numerically, and confirms all eight exceptional sign patterns, two strict-side examples and a high-precision nonexceptional critical oscillation. The last computation uses high-precision decimal arithmetic to avoid artificial growth of the leading Perron mode from rounding. These finite tests are only supplementary; all universal conclusions, including the eight-point exception and invariant-measure census, follow from the analytic proof.

## Relationship to prior work

Wang et al. (2023), Section 2.1 and their Equation (3), define the underlying three-dimensional parabolic map with positive parameters and study fixed points, local linear stability and numerical bifurcations, before coupling the map to a separate four-dimensional memristive model. Their full openly accessible article does not state the \(c=1\) monomial reduction, an exact global basin surface, the two distinct expanding spectral scales, or a critical-orbit and invariant-probability census.

The previously published exact primitive-two-cycle census for the **same three-dimensional map** (published-finding corpus, October 18, 2026) proves sharp two-cycle birth and Floquet boundaries at general positive parameters. Its statement depends on \(t=b(1-c)\); at \(c=1\) it rules out primitive two-cycles, which is consistent with but does **not imply** the present classification of all forward orbits, critical nonperiodic dynamics, and invariant probability measures. Its full RESULT.md has been inspected. Meng, Bao and Xu (2011) investigate a different, two-dimensional parabolic map, without the three-step recurrence here. General theory of monomial recurrences and log-linear dynamics supplies standard methods, not a known published global classification for this specific polynomial map. Publication priority beyond accessible texts and indexed findings is not claimed.

## Limitations

The exact restriction \(c=1\) is essential: for \(c\ne1\), the identity \(1-z_{n+1}=x_n\) no longer holds. No result is claimed for the four-dimensional memristive extension, its cryptographic performance, or small-parameter perturbations of this slice. On \(H=1\), the theorem proves unbounded and vanishing **subsequences** of the absolute middle coordinate, not convergence or a unique limiting distribution. The finite checker is not a computer-assisted infinite proof. Although the exact model-specific global classification was not found in the inspected texts, equivalent results in unindexed literature remain a historical-priority risk.

## References

1. M. Wang, L. Tong, C. Li, X. Zhang, H. H.-C. Iu and Z. Li, “A Novel Four-Dimensional Memristive Hyperchaotic Map Based on a Three-Dimensional Parabolic Chaotic Map with a Discrete Memristor,” *Symmetry* **15** (2023), 1879. Published October 6, 2023. DOI: https://doi.org/10.3390/sym15101879 . Full openly accessible article: https://www.mdpi.com/2073-8994/15/10/1879 , especially Sections 2.1 and 3.1.
2. “A golden-ratio sink boundary and complete primitive two-cycle census for a three-dimensional parabolic map,” published published-finding corpus result (October 18, 2026): https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-a-golden-ratio-sink-boundary-and-complete-primitive-two-cycle-ce--37fa6309f5c1/RESULT.md .
3. J.-D. Meng, B.-C. Bao and Q. Xu, “Dynamics of two-dimensional parabolic discrete map,” *Acta Physica Sinica* **60** (2011), 010504. DOI: https://doi.org/10.7498/aps.60.010504 .
