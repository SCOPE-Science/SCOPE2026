# An exact global separatrix and two expanding scales in a three-dimensional parabolic map

## Finding

Consider the polynomial self-map of \(\mathbb R^3\) introduced in Wang et al. (2023), restricted to the parameter surface \(c=1\):
\[
F_{a,b}(x,y,z)=\bigl(a y^2,\ b y(1-z),\ 1-x\bigr),\qquad a,b>0.
\]
Let \(r\in(1,2)\) be the unique real root of \(r^3-r^2-2=0\), let \(s=\sqrt{2/r}>1\), and define
\[
H_{a,b}(x,y,z)=(ab)^{r^2/2}b^{r+1}|x|\,|y|^{r^2}|1-z|^r.
\]
Then \(H_{a,b}(F_{a,b}(p))=H_{a,b}(p)^r\) on all of \(\mathbb R^3\), including the zero sets. The complete forward-orbit classification is as follows.

- **Extinction:** If \(H(p)<1\), the orbit converges to \(E_0=(0,0,1)\).
- **Escape:** If \(H(p)>1\), then \(|y_n|\to\infty\), \(x_n\to+\infty\), and \(z_n\to-\infty\).
- **Critical surface:** If \(H(p)=1\), precisely the eight points with \((|x|,|y|,|1-z|)=(1/b,1/\sqrt{ab},1/b)\) are eventually fixed. Each reaches one of \(E_\pm=(1/b,\pm1/\sqrt{ab},1-1/b)\) within two iterations. Every other critical orbit has \(\liminf |y_n|=0\) and \(\limsup |y_n|=+\infty\).

The critical surface is exactly the common boundary between the open extinction and escape sets. Writing \(L_n=\log(\sqrt{ab}\,|y_n|)\) for \(H(p)>0\), we have
\[
L_n=\frac{\log H(p)}{3r^2-2r}\,r^n+O_p(s^n).
\]
On the nonexceptional critical surface, \(L_n=s^n(A\cos n\theta+B\sin n\theta)\) exactly for all \(n\ge0\); here \(A,B\) are real, not both zero, and \(s e^{i\theta}\) is the root of \(\lambda^3-\lambda^2-2=0\) with positive imaginary part. The only recurrent points are \(E_0,E_+,E_-\). Consequently every invariant Borel probability measure is a convex combination of their Dirac masses, and there are no other periodic orbits. Both nonzero equilibria are hyperbolic repellers. At \(E_0\) the derivative is nilpotent and the basin is exactly \(\{H<1\}\).

## Assumptions and scope

The parameter \(c\) is exactly one, \(a,b\) are arbitrary strictly positive real numbers, and all claims concern deterministic forward iterates from real initial states. The constant in \(O_p(s^n)\) may depend on the parameters and starting state but not on \(n\). Logarithms are taken only when \(x_0y_0(1-z_0)\ne0\).

For fixed \(y_0\ne0\) and \(z_0\ne1\), the exact threshold for \(|x_0|\) is
\[
X_c(y_0,z_0)=(ab)^{-r^2/2}b^{-(r+1)}|y_0|^{-r^2}|1-z_0|^{-r}.
\]
Strict inequality below or above the threshold gives extinction or escape, respectively; equality gives the critical cases. In the original positive octant \(x_0,y_0,z_0>0\), the exceptional critical points are \((1/b,1/\sqrt{ab},1+1/b)\), which maps to \(E_-\) in one step, and \(E_+\) when \(b>1\). All other critical points in that octant oscillate in the stated sense.

## Proof

**1. Scalar reduction and the zero sets.** Since \(1-z_{n+1}=x_n\) and \(x_{n+1}=a y_n^2\),
\[
y_{n+3}=ab\,y_{n+2}y_n^2,\qquad y_1=b y_0(1-z_0),\qquad y_2=b^2 y_0(1-z_0)x_0.
\]
If \(H(p)=0\), one of \(y_0,y_1,y_2\) vanishes. The recurrence gives a zero at that index plus three, and any zero at index at least two propagates to all subsequent indices. Thus the orbit reaches \(E_0\) in finite time. If \(H(p)>0\), every term is nonzero.

**2. Logarithmic linearization.** The normalization \(L_n=\log(\sqrt{ab}|y_n|)\) gives \(L_{n+3}=L_{n+2}+2L_n\). For \(U_n=(L_n,L_{n+1},L_{n+2})^{\mathsf T}\), the transition matrix is
\[
M=\begin{pmatrix}0&1&0\\0&0&1\\2&0&1\end{pmatrix},\qquad \det(\lambda I-M)=\lambda^3-\lambda^2-2.
\]
The two real stationary values of the polynomial are negative, and the polynomial changes sign between 1 and 2. Thus its roots are the simple real root \(r\in(1,2)\) and a nonreal conjugate pair \(\zeta,\bar\zeta\), whose modulus is \(s=\sqrt{2/r}\) by the product of the roots. In particular \(1<s<r\), the latter inequality following from \(r^3>2\).

The left and right eigenvectors at \(r\) may be taken as \(w=(r^2-r,r-1,1)\) and \(v=(1,r,r^2)^{\mathsf T}\). Substitution gives \(wv=3r^2-2r\) and \(wU_0=\log H(p)\), using the initial data in Step 1. Since \(wU_n=r^n wU_0\), the identity \(H(Fp)=H(p)^r\) follows, including across the zero sets by continuity. Projection onto the \(r\)-eigenspace followed by taking the first coordinate gives the asserted expansion for \(L_n\).

**3. Strict regions and the boundary.** If \(0<H(p)<1\), the negative leading coefficient and \(s<r\) give \(L_n\to-\infty\), hence \(y_n\to0\) and \(p_n\to E_0\). If \(H(p)>1\), the positive coefficient forces \(L_n\to+\infty\), and the same delayed-coordinate identities give the claimed escape. The zero case was treated in Step 1. By continuity the strict regions are open and their boundaries are contained in \(H=1\). At any point with \(H=1\), a small change in \(|x_0|\) in either direction gives a point in the corresponding strict region, so the full level set is the common boundary.

**4. The critical orbits.** For \(H(p)=1\), \(U_0\) lies in \(\ker w\), on which \(M\) is linearly conjugate to the expanding rotation with complex multiplier \(\zeta=s e^{i\theta}\), \(0<\theta<\pi\). This gives the exact scalar sine-cosine representation of \(L_n\). If both coefficients vanish then the first three entries \(L_0,L_1,L_2\) vanish, so \(U_0=0\). Otherwise the sinusoidal factor is bounded above a positive constant and below a negative constant on two infinite subsequences. For an irrational rotation this follows from density; for a rational rotation the factor averages to zero over its finite orbit, which has at least three distinct points and on which the nonzero sinusoid cannot vanish identically. Since \(s>1\), these subsequences give the asserted liminf and limsup after exponentiation.

The equation \(U_0=0\) is equivalent to \(|y_0|=|y_1|=|y_2|=1/\sqrt{ab}\); the initial identities then give \(|x_0|=|1-z_0|=1/b\). Conversely all eight independent sign choices give those logarithmic zeros, and by time two \(x_2=1/b\), \(1-z_2=1/b\), and \(|y_2|=1/\sqrt{ab}\), giving one of \(E_\pm\). For original coordinates all positive, \(x_0,y_0\) must have positive signs; \(z_0=1+1/b\) is always positive, whereas \(z_0=1-1/b\) is positive only if \(b>1\). Substituting the first of these sign choices into \(F\) gives \(E_-\) in one step.

**5. Recurrence, invariant measures and stability.** At a fixed point \(x=a y^2\), \(z=1-x\), and \(y=bxy\), which give exactly \(E_0,E_+,E_-\). Any strict-region point other than \(E_0\) is nonrecurrent by its limit or escape. At a nonexceptional critical point, \(\|M^n U_0\|\) grows at least as a positive constant times \(s^n\) because the action on \(\ker w\) is conjugate to an expanding rotation. Were physical iterates to return to the point along a subsequence, the continuous functions giving the next three nonzero middle coordinates and their logarithms in a neighborhood of that point would yield a bounded subsequence of \(U_n\), a contradiction. The six nonfixed exceptional points cannot recur since they become fixed at a different point. By Poincaré recurrence and a countable basis of \(\mathbb R^3\), any invariant probability assigns full mass to the three recurrent points; conversely all their convex combinations are invariant.

At \(E_0\) the only nonzero derivative entry is the \(-1\) in the third row and first column; the derivative is nilpotent. At \(E_\pm\), the characteristic polynomial is \(\lambda^3-\lambda^2-2\); for example the sign-adjusted logarithmic coordinates \(\log(b|x|),\log(\sqrt{ab}|y|),\log(b|1-z|)\) form a smooth local chart at either fixed point, in which the derivative is the linear transformation \((u,v,w)\mapsto(2v,v+w,u)\). All three eigenvalues have modulus greater than one, giving hyperbolic repellers.

## Verification

The standard-library `checker.py` tests exact rational instances of the scalar recurrence, the eigenfunction identity, the eight exceptional sign patterns, two strict-side examples and a high-precision critical oscillation. The package reports 336 rational recurrence comparisons, 401 log-eigenfunction tests and 12 threshold/exception tests, with \(r\approx1.695620769559862\), \(s\approx1.086052035863345\). These finite checks do not establish the universal conclusions, which follow from the analytic proof. The positive-octant assertion follows by the explicit sign enumeration above.

## Relationship to prior work

Wang et al. (2023), Section 2.1, Equation (3), introduced the three-dimensional map and analyzed fixed points, local stability and numerical bifurcations before studying a separate four-dimensional memristive extension. Their local analysis is not the exact global \(c=1\) classification. The October 2026 finding *A golden-ratio sink boundary and complete primitive two-cycle census for a three-dimensional parabolic map* studies primitive two-cycles and local Floquet boundaries in this same map; it rules out primitive two-cycles on this slice but does not give the global orbit and invariant-probability census. Meng, Bao and Xu (2011) treat a different two-dimensional parabolic map. Log-linearization of monomial maps and the recurrence/spectral techniques are standard; no general priority claim is made for these methods.

## Limitations

For \(c\ne1\), the delayed-coordinate identity used in the proof no longer holds. The classification does not extend here to perturbations in \(c\), the four-dimensional model, or any cryptographic application. On \(H=1\), the nonexceptional result gives diverging and vanishing subsequences of the absolute middle coordinate, not a limiting distribution. Equivalent model-specific statements outside the inspected literature are not ruled out.

## References

1. M. Wang, L. Tong, C. Li, X. Zhang, H. H.-C. Iu and Z. Li, “A Novel Four-Dimensional Memristive Hyperchaotic Map Based on a Three-Dimensional Parabolic Chaotic Map with a Discrete Memristor,” *Symmetry* **15** (2023), 1879. https://doi.org/10.3390/sym15101879
2. “A golden-ratio sink boundary and complete primitive two-cycle census for a three-dimensional parabolic map,” October 18, 2026. https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-a-golden-ratio-sink-boundary-and-complete-primitive-two-cycle-ce--37fa6309f5c1/RESULT.md
3. J.-D. Meng, B.-C. Bao and Q. Xu, “Dynamics of two-dimensional parabolic discrete map,” *Acta Physica Sinica* **60** (2011), 010504. https://doi.org/10.7498/aps.60.010504
