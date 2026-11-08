# A positive inverse-strength shift of the period-two Floquet boundary in a saturating predator-prey map

## Finding

For the logarithmic predator-prey return map
\[
f_{p,q}(x)=x-p+\frac{q}{1+e^x},\qquad p>2,\quad q>\frac{p^2}{p-2},
\]
there is exactly one prime period-two orbit. Let \(M(p,q)\) be its two-step multiplier. A unique positive \(\theta_*\) solves
\[
\theta_* P'(\theta_*)=1,\qquad P(\theta)=2\theta\coth\theta,
\]
and define \(p_*=P(\theta_*)\). Near this threshold, for all sufficiently large \(q\), the level \(M=-1\) is a unique smooth graph \(p=p_{\mathrm{flip}}(q)\), with **strictly positive** first finite-strength correction:
\[
\boxed{p_{\mathrm{flip}}(q)=p_*+\frac{\mathcal S}{q}+O(q^{-2})},\quad
p_*\approx 2.526467725853819,
\quad\mathcal S\approx 6.745591544665048.
\]
In a fixed neighborhood of \(p_*\), for sufficiently large \(q\), the prime two-cycle is hyperbolically attracting for \(p<p_{\mathrm{flip}}(q)\), and repelling for \(p>p_{\mathrm{flip}}(q)\). At equality its multiplier is exactly \(-1\); this work does not assert a nondegenerate period-doubling theorem. In particular, at the limiting Ricker threshold \(p=p_*\) the **finite-strength** two-cycle is attracting for every sufficiently large finite \(q\), even though the limit has multiplier \(-1\).

The coefficient is explicitly
\[
\mathcal S=\frac{4(p_*^3-3p_*^2+4p_*-1)}{2\{1+\theta_*P''(\theta_*)/P'(\theta_*)\}}>0.
\]

## Assumptions and scope

All variables are real. The parameters \(p,q\) are independent positive real numbers in the indicated region; the asymptotic statement takes \(q\to+\infty\) at \(p\) in a neighborhood of \(p_*\), with an analytic continuation of the two-cycle. The physical state \(x\in\mathbb R\). A two-cycle means distinct points \(x<y\) satisfying \(f(x)=y\), \(f(y)=x\). The multiplier is \(f'(x)f'(y)\). Hyperbolic attraction and repulsion refer to local dynamics of the second iterate.

## Proof

**1. Complete two-cycle parameterization.** Set \(d=y-x>0\). Both period-two equations give
\[
e^x=\frac{q-p-d}{p+d},\quad e^y=\frac{q-p+d}{p-d},\quad 0<d<p.
\]
Putting \(A=e^d(p-d)\) and \(B=p+d\), the identity \(e^y/e^x=e^d\) gives
\[
q=Q_p(d):=p+d\frac{A+B}{A-B}.
\]
Let \(u(d)=d/2-\operatorname{artanh}(d/p)\). The denominator \(A-B\) is positive exactly when \(u>0\). Since \(u(d)/d=1/2-\operatorname{artanh}(d/p)/d\) strictly decreases from \(1/2-1/p\) to a negative value as \(d\uparrow p\), it vanishes at a unique \(d_\infty(p)\in(0,p)\). Hence precisely \(0<d<d_\infty\) is admissible. Moreover
\[
Q_p(d)=p+\frac{d}{\tanh u(d)}.
\]
Because \(d u'(d)<u(d)\) and \(u<\sinh u\cosh u\) for \(u>0\), the ratio \(\tanh u(d)/d\) strictly decreases; consequently \(Q_p\) strictly increases from \(p^2/(p-2)\) to \(+\infty\). This proves uniqueness and existence for the asserted region without assuming a numerical orbit census. The endpoint satisfies \(d_\infty=2\theta\), with \(p=P(\theta)=2\theta\coth\theta\).

**2. Exact multiplier and Ricker limit.** At the two points, direct differentiation gives
\[
f'(x)=1-(p+d)+\frac{(p+d)^2}{q},\qquad
f'(y)=1-(p-d)+\frac{(p-d)^2}{q}.
\]
At fixed \(p>2\), \(d\uparrow d_\infty=2\theta\) as \(q\to\infty\), so
\[
M_\infty(p)=(1-p)^2-d_\infty^2=1-2\theta P'(\theta).
\]
Here
\[
P'(\theta)=2(\coth\theta-\theta\operatorname{csch}^2\theta)>0,\quad
P''(\theta)=4\operatorname{csch}^2\theta(\theta\coth\theta-1)>0.
\]
Thus \(\theta P'(\theta)\) grows strictly from zero to infinity; \(M_\infty\) decreases strictly from \(1\) to \(-\infty\), crossing \(-1\) exactly once at \(\theta_*\). Under the rescaling \(z=q e^{-x}\), the original map is conjugate to
\[
z\mapsto z\exp\!\left(p-\frac{z}{1+z/q}\right),
\]
which converges locally smoothly to the classical Ricker map \(z\mapsto z e^{p-z}\). The limiting threshold itself is a Ricker phenomenon and is not asserted to be new.

**3. First nonzero finite-strength correction.** Write \(d_\infty=d_\infty(p)\) and \(D=2p-p^2+d_\infty^2=2\theta P'(\theta)>0\). The equation for \(Q_p(d)\) has a simple pole at \(d=d_\infty\). Expanding its denominator, or using the implicit function theorem with \(t=1/q\), yields locally analytically
\[
d(p,q)=d_\infty-\frac{K(p)}q+O(q^{-2}),\qquad
K(p)=\frac{2d_\infty(p^2-d_\infty^2)}{D}>0.
\]
Expanding the exact multiplier (not a fitted numerical interpolation) gives
\[
M(p,q)=M_\infty(p)+\frac{C(p)}q+O(q^{-2}),
\]
\[
C(p)=2d_\infty K+2\bigl[p^2(1-p)+d_\infty^2(1+p)\bigr].
\]
At the unique crossing \(p=p_*\), the identities \(D=2\) and \(d_\infty^2=p_*^2-2p_*+2\) simplify this to
\[
C(p_*)=4(p_*^3-3p_*^2+4p_*-1)>0.
\]
Indeed \(p_*>2\), and the cubic has positive derivative \(3p^2-6p+4>0\) and positive value at \(p=2\). Finally
\[
\frac{dM_\infty}{dp}(p_*)=-2\left(1+\frac{\theta_*P''(\theta_*)}{P'(\theta_*)}\right)<0.
\]
The analytic implicit function theorem applied to \(M(p,1/t)=-1\) at \((p_*,0)\) proves the unique local smooth critical curve and its coefficient \(\mathcal S=-C(p_*)/M_\infty'(p_*)>0\). Continuity of the multiplier and its strictly negative \(p\)-derivative in a sufficiently small neighborhood proves the asserted hyperbolic stability on either side.

## Verification

The included standalone `verify.py` performs arbitrary-precision checks of the parameterized orbit equations and multipliers, of the identity \(M_\infty=1-2\theta P'(\theta)\), of the strictly positive derivatives, and of the positive first-order shift. Its finite test points are supplementary; the infinite-parametric conclusion follows from the proof above. Numerical values are display approximations only.

## Relationship to prior work

The 2021 analysis of the same predator-prey map established the unique period-two orbit in the relevant parameter domain (Lemmas 1 and 3) and described richer higher-period structures. The 2025 study introduced rigorous computer-assisted continuation of its finite-parameter period-doubling curves (Sections 2.2 and 3); it does not state the positive inverse-strength correction at the infinite-strength endpoint. The Ricker model and its period-doubling cascade are classical; our transformation explicitly identifies this **known** leading-order limit. The specific finite-strength drift coefficient and the consequent attracting-versus-neutral distinction at the Ricker threshold are the narrower result. No definitive publication-priority claim is made.

## Limitations

This is a local hyperbolic classification near the **second** flip threshold and at sufficiently strong predation; it does not classify arbitrary \(p,q\), global basins, subsequent periods, or the underlying continuous-time three-species model. In particular, the equality multiplier \(-1\) alone does not verify nondegeneracy of a period-four bifurcation. The finite-strength correction need not be universal under other saturating functional responses. Independent scientific review has not been performed.

## References

1. L. Alonso Mozo, O. Hénot and P. Lappicy, *A Practical Guide to Rigorously Locate Periodic Orbits in Discrete Dynamics*, arXiv:2510.06373v1 (first submitted 2025-10-07), https://arxiv.org/html/2510.06373v1.
2. *Bistability in a one-dimensional model of a two-predators-one-prey population dynamics system*, arXiv:2108.06739 (2021), https://arxiv.org/abs/2108.06739.
3. E. Braverman and J. Haroutunian, *Chaotic and stable perturbed maps: 2-cycles and spatial models*, Chaos 20, 023114 (2010), DOI:10.1063/1.3404774 (Ricker background; abstract consulted).
