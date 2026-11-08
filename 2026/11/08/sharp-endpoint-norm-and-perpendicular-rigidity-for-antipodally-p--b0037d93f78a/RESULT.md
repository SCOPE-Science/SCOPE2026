# Sharp endpoint norm and perpendicular rigidity for antipodally perturbed trigonometric least squares

## Finding
Let \(\sigma\) be normalized angular Lebesgue measure on the unit circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\). For \(0<w<1\), define
\[
\mu_w=(1-w)\sigma+\frac w2(\delta_0+\delta_\pi),\qquad
V=\operatorname{span}_{\mathbb R}\{1,\cos\theta,\sin\theta\}.
\]
Let \(P_w:L^2(\mu_w;\mathbb R)\to V\) be orthogonal projection, restricted as a bounded map on \(L^\infty(\mu_w;\mathbb R)\). Then its **sharp endpoint norm**, for every \(0<w<1\), is
\[
\boxed{\ \|P_w\|_{L^\infty(\mu_w)\to L^\infty(\mu_w)}
=w+\frac2\pi\left[\sqrt{4-(1-w)^2}+(1-w)\arcsin\frac{1-w}{2}\right].\ }
\]
Its only norming evaluation locations are the two points perpendicular to the atomic diameter, \(\theta=\pi/2\) and \(\theta=3\pi/2\). At either location the unique norming input up to an overall sign, modulo null sets, is the sign of that evaluation's reproducing kernel. In particular, at \(\pi/2\) it is \(\operatorname{sgn}(1+2\sin\phi/(1-w))\), which is \(+1\) at both atoms.

The norm is strictly increasing and strictly convex as a function of \(w\); more precisely
\[
\frac{d}{dw}\|P_w\|=1-\frac2\pi\arcsin\frac{1-w}{2}\in(2/3,1),
\qquad
\frac{d^2}{dw^2}\|P_w\|=\frac{1}{\pi\sqrt{1-(1-w)^2/4}}>0.
\]
Its one-sided endpoint limits are \(1/3+2\sqrt3/\pi\) at \(w\downarrow0\) and \(1+4/\pi\) at \(w\uparrow1\). The second number is a one-sided limit only; the degree-one projection is not well-defined as a three-dimensional subspace of \(L^2(\mu_1)\).

## Assumptions and scope
All functions and operators are real. The continuous component has positive mass \(1-w>0\), so \(1,\cos\theta,\sin\theta\) remain linearly independent in \(L^2(\mu_w)\). Norms and signs refer to \(\mu_w\)-almost-everywhere equivalence classes. The signed kernel vanishes at at most two non-atomic points, which do not affect uniqueness of norming inputs. The comparison concerns exactly the pair of equal masses placed at antipodal points; rotating the pair gives an equivalent statement.

## Proof
Set \(p=1+w\), \(q=1-w\), \(a=2/p\), and \(b=2/q\). The basis has Gram matrix \(\operatorname{diag}(1,p/2,q/2)\) and no mixed entries. Consequently the reproducing kernel is
\[
K_w(\theta,\phi)=1+a\cos\theta\cos\phi+b\sin\theta\sin\phi.
\]
For each evaluation \(\theta\), the sharp absolute input bound is its row \(L^1(\mu_w)\) norm. Because the continuous measure has full support and \(P_wf\) is continuous, the operator norm is the maximum of these row norms. The atomic contribution is \(w\max(1,a|\cos\theta|)\).

For \(R\ge1\), direct integration over a circle gives
\[
I(R):=\int_{\mathbb T}|1+R\cos\phi|\,d\sigma(\phi)
=\frac2\pi\left(\sqrt{R^2-1}+\arcsin\frac1R\right),
\qquad
I'(R)=\frac2\pi\frac{\sqrt{R^2-1}}R.
\]
Writing \(t=|\cos\theta|\in[0,1]\), the full row norm is
\[
J_w(t)=q I\!\left(\sqrt{b^2-(b^2-a^2)t^2}\right)+w\max\{1,at\}.
\]
The radicand is always at least \(a^2>1\). Since \(b>a\), the first term strictly decreases with \(t>0\), while the second is constant for \(0\le t\le p/2\). Thus \(J_w\) is strictly smaller than \(J_w(0)\) on \((0,p/2]\).

For \(p/2<t\le1\), put \(R^2=b^2-(b^2-a^2)t^2\) and \(f(s)=\sqrt{s-1}/s\). Differentiation gives
\[
J'_w(t)=wa-\frac{2q(b^2-a^2)}\pi\,t f(R^2).
\]
Because \(b^2-a^2=16w/(p^2q^2)\), the derivative is negative exactly when
\[
t f(R^2)>\frac{\pi pq}{16}.
\]
Now \(f'(s)=(2-s)/(2s^2\sqrt{s-1})\), so on the closed interval \([a^2,b^2]\) its minimum is attained at an endpoint. Both endpoints obey the strict uniform bound \(f(a^2),f(b^2)>\pi q/8\). Indeed
\[
f(b^2)=\frac{q\sqrt{4-q^2}}4>\frac{\pi q}{8},
\qquad
f(a^2)=\frac{p\sqrt{4-p^2}}4>\frac{\pi q}{8}.
\]
The first inequality uses \(2\sqrt3>\pi\). For the second, \(4-p^2=q(2+p)\), \(p\ge1\), and \(0<q<1\) imply \(p\sqrt{4-p^2}\ge\sqrt3 q\), again giving \(2\sqrt3>\pi\). As \(t\ge p/2\), we obtain \(tf(R^2)>\pi pq/16\). Hence \(J'_w(t)<0\) throughout its second branch. We have proved \(J_w(t)<J_w(0)\) for all \(t>0\), with no exceptional parameter range.

At \(t=0\), \(R=b=2/q\) and \(\max(1,at)=1\). Substituting into \(J_w(0)=qI(2/q)+w\) yields the stated closed form. Taking \(\operatorname{sgn}K_w(\pi/2,\cdot)\) gives exact equality. Conversely any norming input must saturate an evaluation row bound at one of the two perpendicular points. Equality in the absolute-integral triangle inequality then forces that sign function, modulo the two zero points and an overall sign.

Finally, differentiating the closed form proves both derivative identities and the endpoint limits.

## Verification
Run `python3 check_circle.py` using Python's standard library. It checks the mixed Gram identities with exact fractions; evaluates the kernel by independent midpoint integration at multiple atomic weights and evaluation angles; tests the perpendicular sign witnesses; checks the analytic angular-derivative margin for several parameters; and verifies the first derivative and endpoint formulas. Numerical angular tests are corroboration only: the universal proof is the exact inequality \(2\sqrt3>\pi\) and its endpoint comparison above.

## Relationship to prior work
Finite-mass Uvarov modifications and reproducing-kernel updates are established: Delgado, Fernández, Pérez and Piñar (arXiv:1601.07194, Section 3 and Theorem 3.4) give the general rank-update relation. Witte (arXiv:0811.4027, Sections 1 and 3) gives the wider circle orthogonal-polynomial transform framework. Neither inspected source establishes the specified real three-dimensional mixed-measure \(L^\infty\) projection norm or its rigid norming locations. Classical Fourier projection Lebesgue-constant formulas cover the unperturbed case only; in particular \(w=0\) here recovers \(1/3+2\sqrt3/\pi\). The contribution is the exact all-weights optimization and rigidity, not the existence of a mass-update formula.

## Limitations
Only the equal antipodal two-atom perturbation and the real first trigonometric degree are treated. The corresponding norm for unequal atoms, nonantipodal atoms, higher Fourier degree, or nonuniform continuous densities is not determined. The parameter \(w=1\) is excluded, and the formula's limit is not asserted to be an operator norm for the resulting two-atom measure. Historical or unindexed special-case formulas could still have appeared outside the inspected primary literature; independent external review has not been performed.

## References
1. N. S. Witte, *Bi-orthogonal systems on the unit circle, Regular Semi-Classical Weights and Integrable Systems – II*, arXiv:0811.4027 (first posted 2008-11-25), https://arxiv.org/abs/0811.4027.
2. A. M. Delgado, L. Fernández, T. E. Pérez and M. A. Piñar, *Multivariate Orthogonal Polynomials and Modified Moment Functionals*, arXiv:1601.07194 (first posted 2016-01-26), https://arxiv.org/abs/1601.07194.
3. U. Luther and G. Mastroianni, *Fourier Projections in Weighted \(L^\infty\)-Spaces*, TU Chemnitz preprint 99-10 (month evidence 1999-12), https://www.tu-chemnitz.de/mathematik/preprint/1999/PREPRINT_10.php; bibliographic abstract examined, complete text not available in the inspected material.
