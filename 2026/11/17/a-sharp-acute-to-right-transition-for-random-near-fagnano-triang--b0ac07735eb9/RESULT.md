# A sharp acute-to-right transition for random near-Fagnano triangles

## Finding
Let \(T=ABC\) be a fixed nondegenerate Euclidean triangle. Choose \(X\in BC\), \(Y\in CA\), and \(Z\in AB\) independently and uniformly in arclength, and let \(P=|XY|+|YZ|+|ZX|\). This statement concerns the **small perimeter excess** of this side-stratified geometric sample, not the classical identification of a minimum-perimeter inscribed triangle.

**Acute triangles.** Write \(a=|BC|\), \(b=|CA|\), \(c=|AB|\), and denote the interior angles by \(A,B,C\), all strictly between zero and \(\pi/2\). The minimum is \(p_*=a\cos A+b\cos B+c\cos C\), attained at the orthic triangle. For every fixed such parent triangle, as \(t\downarrow0\),
\[
\Pr(P<p_*+t)\sim K_{\mathrm{ac}}(T)t^{3/2},\qquad
K_{\mathrm{ac}}(T)=\frac{4\pi\sqrt2}{3}\,
\frac{\sqrt{\cos A\cos B\cos C}}{\sqrt{abc}\,\sin A\sin B\sin C}.
\]
Parametrize the positions on their respective sides by signed arclength displacements \(s=(s_1,s_2,s_3)\) from the three altitude feet, with positive directions \(B\to C\), \(C\to A\), and \(A\to B\). Put
\[
\xi=\frac{H^{1/2}s}{\sqrt{2t}},\qquad
H=\operatorname{diag}(\sin A,\sin B,\sin C)
\begin{pmatrix}
q+r&q&r\\q&q+p&p\\r&p&p+r
\end{pmatrix}
\operatorname{diag}(\sin A,\sin B,\sin C),
\]
where \(p=(a\cos A)^{-1}\), \(q=(c\cos C)^{-1}\), and \(r=(b\cos B)^{-1}\). Conditioned on \(P<p_*+t\), the law of \(\xi\) converges **in total variation** to the uniform law on the Euclidean unit ball in \(\mathbb R^3\). In particular, the conditional rescaled perimeter excess \((P-p_*)/t\) converges to \(\operatorname{Beta}(3/2,1)\).

**Right triangles.** Suppose instead that \(A=\pi/2\), with legs \(\beta=|AB|\), \(\gamma=|AC|\), hypotenuse \(a=|BC|\), and altitude \(h=\beta\gamma/a\) from \(A\) to \(BC\). The perimeter infimum is \(p_*=2h\), attained in the closure at \(Y=Z=A\) and \(X\) equal to the altitude foot. Its near-minimum law has a **different exponent**:
\[
\Pr(P<2h+t)\sim K_{\mathrm{rt}}(T)t^{7/4},\qquad
K_{\mathrm{rt}}(T)=\frac{8\pi\sqrt2}{21\sqrt a\,h^{5/4}}.
\]
This is an asymptotic for each fixed right triangle, not a uniform estimate as the parent shape approaches a right angle.

For a marked version, put \(A=(0,0)\), \(B=(\beta,0)\), and \(C=(0,\gamma)\). Let \(X_0\) be the altitude foot; write \(X=X_0+u(-\beta,\gamma)/a\), \(Z=(x,0)\), and \(Y=(0,y)\). Set \(r_0=\sqrt{x^2+y^2}\), \(\varphi=\operatorname{atan2}(y,x)\), \(\varphi_0=\operatorname{atan2}(\beta,\gamma)\), \(\kappa=h/a\), and
\[
U_t=\frac{u}{\sqrt{ht}},\qquad
R_t=\frac{\kappa r_0}{\sqrt{ht}},\qquad
\Theta_t=\sqrt{\frac{r_0}{2t}}(\varphi-\varphi_0).
\]
Conditioned on \(P<2h+t\), the joint law of \((U_t,R_t,\Theta_t)\) converges **in total variation** to the density
\[
\frac{21}{8\pi}\,R^{1/2}
\mathbf1_{\{R>0,\ U^2+R^2+\Theta^2<1\}}
\quad\text{with respect to }dU\,dR\,d\Theta.
\]
Consequently \((P-2h)/t\), conditionally on \(P<2h+t\), converges to \(\operatorname{Beta}(7/4,1)\).

## Assumptions and scope
All three points are sampled independently from normalized one-dimensional arclength on their **specified** sides; this is not the sampling law for three independent points on the whole boundary. The parent triangle is fixed, with strictly positive side lengths. The acute and right cases are distinct assertions. No statement is made here for obtuse parent triangles, for shape-varying uniformity, or for independence of the three side lengths of the sampled triangle. Events using strict rather than non-strict inequalities have the same probabilities because the sampled perimeter has no atom at the minimum.

## Proof
### Acute case: exact local quadratic geometry
Let \(X_0,Y_0,Z_0\) be the altitude feet. Fagnano's classical theorem proves that these form the unique global minimizer over the compact product of sides. Because the parent triangle is strictly acute, all three feet are interior and the three chords joining them have positive lengths. Thus the perimeter is smooth near the minimizing triple and has vanishing first derivatives there.

For a moving chord joining points with unit tangent directions \(v_i,v_j\), with length \(\ell>0\) and unit chord direction \(e\), its contribution to the second variation is the rank-one form \(\ell^{-1}\langle (I-ee^{\mathsf T})(v_i\,ds_i-v_j\,ds_j),v_i\,ds_i-v_j\,ds_j\rangle\). At the altitude feet the three chord lengths, in cyclic order, are \(c\cos C\), \(a\cos A\), and \(b\cos B\). Their transverse tangent components have magnitudes \((\sin A,\sin B)\), \((\sin B,\sin C)\), and \((\sin C,\sin A)\), respectively, with opposite signs at the two endpoints of each chord under the chosen cyclic side coordinates. Summing these three second variations gives exactly the matrix \(H\) displayed in the finding.

Set \(D=\operatorname{diag}(\sin A,\sin B,\sin C)\) and let \(M=D^{-1}HD^{-1}\). Its leading principal minors are \(q+r>0\), \(pq+pr+qr>0\), and \(\det M=4pqr>0\); hence \(H\) is positive definite. Moreover
\[
\det H=\frac{4\sin^2 A\sin^2 B\sin^2 C}{abc\cos A\cos B\cos C}.
\]
Consequently \(P-p_*=\tfrac12s^{\mathsf T}Hs+O_T(\|s\|^3)\). Uniqueness and compactness exclude competing near-minimizers outside a neighborhood of the orthic triple. The side-arclength density is \((abc)^{-1}\). Under \(s=\sqrt{2t}\,H^{-1/2}\xi\), the event region tends to the unit ball, and its rescaled indicator converges in \(L^1\), since positive definiteness bounds all sufficiently small sublevel sets inside a fixed ball. The transformed Jacobian is \((2t)^{3/2}/\sqrt{\det H}\). Multiplication by the unit-ball volume \(4\pi/3\) yields \(K_{\mathrm{ac}}(T)\). The same \(L^1\) convergence of conditional densities proves total variation. Uniform ball volume ratios give the \(\operatorname{Beta}(3/2,1)\) excess law.

### Right case: singular boundary layer
Use the coordinates in the finding and write \(n=(\gamma/a,\beta/a)\) and \(e=(-\beta/a,\gamma/a)\). Thus \(X_0=hn\) and \(X=hn+ue\). The exact perimeter is
\[
P=\sqrt{X_1^2+(X_2-y)^2}+\sqrt{(X_1-x)^2+X_2^2}+\sqrt{x^2+y^2}.
\]
The classical right-angle limiting form of Fagnano's bound gives \(P\ge2h\), with equality in the compact closure only at \((X,Y,Z)=(X_0,A,A)\). Hence all sufficiently small sublevel sets concentrate at this configuration. Writing \(x=r_0\cos\varphi\), \(y=r_0\sin\varphi\) and \(\kappa=n_1n_2=h/a\), a Taylor expansion of the first two square roots about this configuration, followed by the exact last square root, gives
\[
P-2h=\frac{u^2}{h}+\frac{r_0}{2}(\varphi-\varphi_0)^2
+\frac{\kappa^2r_0^2}{h}
+o\!\left(u^2+r_0(\varphi-\varphi_0)^2+r_0^2\right)
\]
as \((u,r_0,\varphi-\varphi_0)\to(0,0,0)\), with \(r_0\ge0\). The expansion can be checked directly using \(\sqrt{r_0^2}=r_0\): its first-order angular term is \(r_0[1-\cos(\varphi-\varphi_0)]\), and the quadratic radial term is \(\kappa^2r_0^2/h\). There is no leading mixed \(ur_0\) term because \(e\cdot n=0\).

For completeness, localization does not rely solely on this formal expansion. The reflection inequality \(P\ge2|AX|=2\sqrt{h^2+u^2}\) implies \(u=O(\sqrt t)\) on \(P<2h+t\). For \(|u|\) and \(r_0\) small, expanding the two nonvanishing distances while retaining the exact \(r_0\) gives \(P-2|AX|\ge c_T r_0^2+c_T r_0(\varphi-\arg X)^2\) for a positive constant \(c_T\). Thus \(r_0=O(\sqrt t)\), and the angular localization follows. For \(r_0\) smaller than a fixed fraction of \(\sqrt t\), its contribution to the normalized probability is controlled by \(C_T\int_0^\eta R^{1/2}dR\), which tends to zero with \(\eta\). On the complement the rescaled expansion is uniform.

Substitute \(u=\sqrt{ht}\,U\), \(r_0=\sqrt{ht}\,R/\kappa\), and \(\varphi-\varphi_0=\sqrt{2t/r_0}\,\Theta\). The deficit divided by \(t\) tends to \(U^2+R^2+\Theta^2\). In polar coordinates \(dx\,dy=r_0\,dr_0\,d\varphi\); the exact Jacobian is
\[
du\,dx\,dy=
\frac{\sqrt2\,h^{5/4}}{\kappa^{3/2}}\,
 t^{7/4}R^{1/2}\,dU\,dR\,d\Theta.
\]
Because the original uniform density is \((a\beta\gamma)^{-1}\), dominated convergence and the preceding localization reduce the leading coefficient to the integral
\[
\int_{\substack{R>0\\U^2+R^2+\Theta^2<1}}R^{1/2}\,dU\,dR\,d\Theta
=\pi\int_0^1R^{1/2}(1-R^2)\,dR=\frac{8\pi}{21}.
\]
Using \(\beta\gamma=ah\) and \(\kappa=h/a\) gives exactly \(K_{\mathrm{rt}}(T)\). The same change of variables, localization and convergence of normalized indicator densities in \(L^1\) give the asserted total-variation limit. The exponent \(7/4\) also implies the stated conditional beta law by taking ratios of sublevel probabilities.

## Verification
A standalone reproducible program, `verify_fagnano.py`, computes the perimeter Hessian directly from chord geometry, verifies its determinant formula, and uses independently scrambled Sobol samples to integrate the rare-event regions in acute-ellipsoid and right-boundary-layer coordinates. For a unit equilateral parent, the predicted acute coefficient is approximately \(3.2245322\), and for the acute parent \((0,0),(4,0),(1,3)\) it is approximately \(0.4261910\). For the right-isosceles parent with unit legs, the right coefficient is approximately \(2.1949357\). At decreasing thresholds the numerical estimates converge toward these values. Numerical checks are diagnostics, not proofs of any asymptotic statement or independent validation.

## Relationship to prior work
The orthic minimizer, its uniqueness for acute triangles, and the right-triangle boundary infimum are classical and **are not new**. Finbarr Holland (2007, full text inspected) explicitly supplies the sharp deterministic bounds for both acute and nonacute parent triangles and trigonometric square-root identities. Alkoumi–Schlenk (2014, original arXiv text inspected) use Fagnano uniqueness in shortest-billiard-orbit geometry. A separate, publicly indexed result, *Exact remainder and global quadratic stability for Fagnano's theorem* (identifier `a7228c2d2631`, full claim and proof inspected), supplies an exact nonnegative decomposition and global quadratic stability in acute triangles. Its sharp stochastic sublevel-volume coefficient, marked conditional ellipsoid law, and especially the non-Morse right-angle \(7/4\) boundary law are not stated there. The exact remainder is valid background and could be used to rederive the acute Hessian; it does not itself provide the right-angle singular probability analysis.

The contribution is therefore the **two distinct probabilistic small-excess universality classes and their conditional marked laws**, not Fagnano optimality, a stability bound, or the square-root decompositions. Mathematical implication was compared at the level of conclusions, including the fact that a deterministic exact representation determines a distribution implicitly but does not evaluate its sharp singular sublevel asymptotics. No claim of exhaustive historical priority is made.

## Limitations
The asymptotics are for each fixed acute or fixed right parent triangle; they do not describe the joint angle-and-threshold crossover and do not treat obtuse triangles. Complete historical priority is unresolved because unindexed treatments of Fagnano stability or random billiard near-minimizers may exist. A first bibliographic sweep found no equivalent probabilistic theorem, but absence from search results is not proof of novelty. No independent mathematical audit was performed.

## References
1. Finbarr Holland, "Another Verification of Fagnano's Theorem," *Forum Geometricorum* **7** (2007), 207–210; public date 2007-12-05. Full text available in the archived *Forum Geometricorum* volumes.
2. Naeem Alkoumi and Felix Schlenk, "Shortest closed billiard orbits on convex tables," arXiv:1408.5255v1, first public 2014-08-22; later *Manuscripta Mathematica* **147** (2015), 365–380.
3. "Exact remainder and global quadratic stability for Fagnano's theorem," publicly indexed geometrical research finding, identifier `a7228c2d2631` (2026); the deterministic exact remainder is acknowledged as prior coverage.
4. H. S. M. Coxeter and S. L. Greitzer, *Geometry Revisited*, Mathematical Association of America (1967), §4.5 (classical geometrical formulation).
