# Universal inverse-sheet crossover and two-term branch law in a quadratic-memristor sine map

## Finding
For real \(a>0\), \(\omega>0\), and \(b\ge0\), consider the quadratic-memristor sine map
\[
F_b(x,q)=\bigl(a\sin(\omega x(1+b-bq^2)),\ q+x\bigr),\qquad (x,q)\in\mathbb R^2.
\]
For a target \((u,v)\) and \(R>0\), let \(N_b(R;u,v)\) be the number of **distinct real** inverse states satisfying \(F_b(x,q)=(u,v)\) and \(|x|\le R\). The exact image for every \(b\ge0\) is \([-a,a]\times\mathbb R\), and every target inside the image has countably infinitely many inverse states in the full plane.

Set \(\kappa(u)=1\) if \(|u|<a\), and \(\kappa(u)=1/2\) if \(|u|=a\). For every fixed \(b>0\) and every target \(|u|\le a\),
\[
N_b(R;u,v)=\frac{2\kappa(u)\omega b}{\pi}R^3
 -\frac{2\kappa(u)\omega(1+b-bv^2)}{\pi}R+O_{a,\omega,b,u,v}(1),\quad R\to\infty.
\]
At \(b=0\), by contrast, \(N_0(R;u,v)=2\kappa(u)\omega R/\pi+O(1)\). Thus the inverse-sheet growth order changes from linear to cubic at every positive memory coupling. The absence of a quadratic term in the fixed-coupling two-term count is exact, despite the target-dependent quadratic phase coefficient.

The transition has a universal crossover at \(R=t/\sqrt b\): for every fixed \(t>0\), \(v\in\mathbb R\), and \(|u|\le a\),
\[
\lim_{b\downarrow0}\sqrt b\,N_b(t/\sqrt b;u,v)
 =\frac{\kappa(u)\omega}{\pi}\,\Psi(t),\qquad
\Psi(t)=\begin{cases}
2(t-t^3),&0<t\le1/\sqrt3,\\
2(t^3-t+4/(3\sqrt3)),&t\ge1/\sqrt3.
\end{cases}
\]
The crossover is independent of the observed charge \(v\) and the sine-level \(u\) apart from the endpoint half-density. Its unique stationary-slope transition occurs at \(t=1/\sqrt3\).

For \(b>0\), let
\[
x_\pm(v)=\frac{2v\pm\sqrt{v^2+3(1+b)/b}}3,
\qquad \Phi_{b,v}(x)=\omega[-bx^3+2bv x^2+(1+b-bv^2)x].
\]
For every interior target \(|u|<a\), the only possible critical inverse states are among the two points \((x_\pm(v),v-x_\pm(v))\); they occur precisely when \(u=a\sin\Phi_{b,v}(x_\pm(v))\). All other inverse states are regular, and hence there are infinitely many regular inverses. Every inverse state above either boundary level \(u=\pm a\) is critical. For \(b=0\), every interior inverse state is regular.

## Assumptions and scope
All states and targets are real, and no restriction is imposed on the **prior-state** signal \(x\) or charge \(q\). Only the first inverse coordinate is truncated by \(|x|\le R\); since \(q=v-x\), this also bounds the prior charge for fixed target \(v\). The fixed-coupling expansion takes \(R\to\infty\) with \(b>0\) held fixed; the crossover takes \(b\downarrow0\) with \(R=t/\sqrt b\), \(t>0\) fixed. These are different limits. The result is about the one-step map on \(\mathbb R^2\), **not** a claim that every inverse state is reachable from an indefinitely long trajectory: on any forward trajectory after one step, \(|x|\le a\). No topological entropy, chaotic attractor, or cryptographic security statement is asserted.

## Proof
**1. Exact scalar inverse problem.** Fix \((u,v)\). The second output equation forces \(q=v-x\), and the first becomes
\[
\sin\Phi_{b,v}(x)=u/a,\qquad
\Phi_{b,v}(x)=\omega x(1+b-b(v-x)^2)
=\omega[-bx^3+2bv x^2+(1+b-bv^2)x].
\]
For \(|u|>a\) there is no inverse. For \(|u|\le a\), \(\Phi_{b,v}\) is surjective: linear with nonzero slope if \(b=0\), and a real cubic with negative leading coefficient if \(b>0\). Each sine level has an unbounded discrete set of phase values, and each such value has at least one polynomial inverse. Distinct phases yield distinct \(x\). A nonzero polynomial has finitely many roots for each phase, hence the resulting inverse fiber is countably infinite.

**2. Uniform sine-crossing count.** For a real phase interval of length \(L\ge0\), the number of **distinct** solutions \(\theta\) to \(\sin\theta=u/a\) in that interval is \(\kappa(u)L/\pi+O(1)\), with an absolute remainder (at most two for any interval). Indeed, interior levels are two arithmetic progressions with step \(2\pi\), while each endpoint level is one such progression. Any real cubic has at most two turning points. Splitting \([-R,R]\) into at most three intervals on which \(\Phi_{b,v}\) is monotone and removing possible duplicated turning-point solutions proves
\[
N_b(R;u,v)=\frac{\kappa(u)}\pi
\operatorname{Var}_{[-R,R]}\Phi_{b,v}+O(1),
\]
where variation means the sum of the absolute phase increments on the monotone pieces. The remainder is bounded uniformly in \(b,R,v,u\) for the family because there are at most three pieces; the two endpoint sine levels also obey this estimate. The same estimate is immediate for \(b=0\).

**3. Fixed-memory two-term count.** For \(b>0\),
\[
\Phi'_{b,v}(x)=\omega(1+b-bv^2+4bvx-3bx^2)
\]
has exactly two distinct real zeros, namely \(x_-<x_+\) displayed above. Its sign is negative, then positive, then negative. When \(R\) exceeds both turning-point absolute values, the exact phase variation is
\[
\operatorname{Var}_{[-R,R]}\Phi_{b,v}
=\Phi_{b,v}(-R)-\Phi_{b,v}(R)
+2[\Phi_{b,v}(x_+)-\Phi_{b,v}(x_-)].
\]
The middle term in brackets is independent of \(R\), while direct expansion gives
\[
\Phi_{b,v}(-R)-\Phi_{b,v}(R)
=2\omega bR^3-2\omega(1+b-bv^2)R.
\]
The \(R^2\) terms cancel identically. The variation crossing estimate proves the stated two-term law. When \(b=0\), the phase is \(\omega x\), giving its linear count directly.

**4. Universal crossover.** Put \(R=t/\sqrt b\) and set \(s=\sqrt b\,x\). The phase-variation formula yields exactly
\[
\sqrt b\operatorname{Var}_{[-t/\sqrt b,t/\sqrt b]}\Phi_{b,v}
=\omega\int_{-t}^t\left|1-3s^2+4v\sqrt b\,s+b(1-v^2)\right|ds.
\]
As \(b\downarrow0\), uniform convergence of the integrand on the fixed compact interval gives \(\omega\int_{-t}^t|1-3s^2|ds\). The sine-crossing error remains \(O(1)\) uniformly in \(b\), so multiplication by \(\sqrt b\) removes it. Direct integration of \(|1-3s^2|\), splitting at \(s=\pm1/\sqrt3\), yields \(\Psi(t)\) and proves the limit, including the boundary half-density.

**5. Critical inverse classification.** The derivative matrix is
\[
DF_b(x,q)=\begin{pmatrix}
 a\omega(1+b-bq^2)\cos\Theta&-2a\omega bqx\cos\Theta\\
 1&1
\end{pmatrix},\quad\Theta=\omega x(1+b-bq^2),
\]
so its determinant is
\[
\det DF_b(x,q)=a\omega\cos\Theta(1+b-bq^2+2bqx).
\]
On the fiber \(q=v-x\), the final factor equals \(\Phi'_{b,v}(x)/\omega\). For interior levels \(|u|<a\), \(\cos\Theta\ne0\), so critical inverses occur precisely at the two turning points when their phase values hit the target. On boundary levels \(u=\pm a\), \(\cos\Theta=0\) at every inverse. For \(b=0\), the determinant is \(a\omega\cos\Theta\), so interior inverses are all regular.

## Verification
The standalone `verify.py` uses exact SymPy identities to check the cubic phase, its derivative, both phase endpoints, and the determinant. It counts sine-level solutions by exact arithmetic-progressions floors on the at most three monotone phase intervals, checks against total phase variation at a fixed explicit error bound, and samples the crossover at three small couplings and six scaled radii. Running `python verify.py` with Python 3 and SymPy prints a PASS line. These finite checks exercise the algebra and counting formulas; the proof above supplies the unbounded-\(R\) and small-\(b\) quantifiers.

## Relationship to prior work
Yihyis, He, Tang and Wang (2023), equations (1), (7), and Table 1 Model 1, introduce this exact quadratic-memristor perturbed sine map and study numerical attractors, Lyapunov exponents, and bifurcation diagrams. The present theorem addresses its full one-step inverse fibers, caustics, quantitative inverse-sheet growth and a singular coupling-scale limit. It does not rely on numerical claims of chaos. A published indexed inverse-valence study of a **different cosine-flux Chialvo map** counts linearly growing inverse branches, but its map, zero-coupling fibers and limiting geometry differ. Other comparisons with a proper cosine-memristor plane map and a bounded-square coupled sine map are not implications of this polynomial-phase theorem. The counting technique is the standard level-crossing count for sine; its combination with the exact charge elimination and two limiting regimes is map-specific.

## Limitations
The invariant forward signal bound \(|x_{n+1}|\le a\) means most of the large-\(R\) inverse branches cannot occur as states along a bi-infinite orbit. The theorem measures one-step inverse geometry over the unrestricted real plane, not inverse multiplicity within a maximal invariant attractor. The fixed-\(b\) remainder depends on target and parameters, and the crossover assumes fixed finite observed charge \(v\), not \(v\) diverging with \(b^{-1/2}\). Publication priority cannot be guaranteed against unindexed equivalent work; an independent mathematical audit has not been performed.

## References
1. W. A. Yihyis, S. He, Z. Tang, H. Wang, "A Class of Discrete Memristor Chaotic Maps Based on the Internal Perturbation," *Symmetry* **15** (2023), 1574; first public publication 2023-08-12, https://doi.org/10.3390/sym15081574 . See full-text equations (1), (7), and Table 1, Model 1.
2. S. Yi, H. Wang, K. Sun, "A modular-bias-sin chaotification method for enhanced discrete memristor chaotic maps," *Chinese Physics B* **35** (2026), 070504, https://doi.org/10.1088/1674-1056/ae181e . Distinct modular model, compared as adjacent literature rather than a basis for this proof.
