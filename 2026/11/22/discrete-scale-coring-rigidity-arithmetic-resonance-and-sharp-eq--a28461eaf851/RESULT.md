# Discrete-scale coring rigidity, arithmetic resonance and sharp equatorial regularity

## Finding
Let a centrally symmetric solid of revolution be cored by a coaxial cylindrical drill after selected homothetic dilations. It is not necessary to test every dilation in order to recognize a spheroid: testing any two dilation factors \(s_1,s_2>1\) satisfying \(\log(s_1)/\log(s_2)\notin\mathbb Q\) suffices, provided each test checks every common bore height. In particular, scales \(2\) and \(3\) suffice. If the two logarithms are rationally related, there are non-spheroidal, strictly convex \(C^{1,1}\) solids that pass both tests. A single scale suffices if the squared profile has a second-order Taylor expansion at the equator.

Precisely, with \(q(t)=f(t)^2\), define \(P(y)=e^{2y}[q(e^{-y})-q(0)]\). Then the entire equal-height condition at scale \(s>1\) is equivalent to \(P\) having period \(\log s\). This exhibits the arithmetic-versus-regularity dichotomy and classifies the full continuous-profile solution set to each finite collection of tests through their common logarithmic periods.

## Assumptions and scope
Take a continuous strictly decreasing \(f:[0,1]\to[0,\infty)\) such that \(f(0)=b>0\) and \(f(1)=0\), and define
\[
K_f=\{(x,y,z)\in\mathbb R^3: |x|\le1,\quad y^2+z^2\le f(|x|)^2\}.
\]
The general scale-test classification needs continuity and strict decrease, not differentiability or convexity. The explicit false-positive solids are strictly convex. For a scale \(s\ge1\), drill the solid \(sK_f\) using the coaxial cylindrical radius \(s f(u/s)\), giving axial internal-wall height \(2u\). Require the volume identity for every \(u\in(0,1)\). These are comparisons of separate drilled specimens at the **same absolute** wall-height, not at equal relative height.

## Proof
**1. Reduction to one functional equation.** The bore meets the profile at axial points \(\pm u\), and the disk-washer formula is
\[
V_s(u)=2\pi\int_0^u s^2\left[q(t/s)-q(u/s)\right]\,dt.
\]
Therefore \(V_1(u)=V_s(u)\) for all \(u\in(0,1)\) is equivalent to
\[
\int_0^u H_s(t)\,dt=u H_s(u),\qquad H_s(t):=q(t)-s^2q(t/s).
\]
Because \(H_s\) is continuous, the displayed identity makes \(uH_s(u)\) differentiable on the open interval. Differentiation shows \(u H_s'(u)=0\), whence \(H_s\) is constant. Its value at zero is \((1-s^2)q(0)\). Thus the identity is exactly
\[
q(t)-q(0)=s^2\,[q(t/s)-q(0)],\qquad 0<t<1.\tag{1}
\]
This is an individual-scale functional equation also obtainable from the volume calculation in Coll and Dodd's 2010 treatment; it is not claimed as an original lemma.

**2. Period classification.** Define \(P(y)=e^{2y}(q(e^{-y})-q(0))\) for \(y\ge0\). On substituting \(t=e^{-y}\), equation (1) becomes
\[
P(y+\log s)=P(y),\qquad y\ge0.\tag{2}
\]
Conversely equation (2) gives equation (1), making the equivalence exact. A continuous function on a half-line with positive period extends continuously to the real line by periodicity. Two incommensurate periods generate a dense additive subgroup of \(\mathbb R\); continuity makes that extension constant. Hence if \(\log s_1/\log s_2\) is irrational, \(P(y)\equiv c\), so \(q(t)=q(0)+ct^2\). Since \(q(1)=0\), \(c=-q(0)\), giving the spheroid \(q(t)=b^2(1-t^2)\). Conversely this profile passes every dilation test. Irrationality for scales \(2\) and \(3\) follows because any equation \(2^m=3^n\) with positive integers \(m,n\) contradicts unique prime factorization.

**3. Sharp commensurate counterexample.** When \(\log s_1/\log s_2\in\mathbb Q\), choose \(h>0\) so that each logarithm is a positive integer multiple of \(h\), put \(\omega=2\pi/h\), and define, for \(0<t\le1\),
\[
q_\varepsilon(t)=1-t^2\left[1+\varepsilon\sin(\omega\log t)\right],\qquad q_\varepsilon(0)=1.
\]
Take \(0<\varepsilon<2/\sqrt{(2-\omega^2)^2+9\omega^2}\). Direct differentiation on \(t>0\) gives
\[
q_\varepsilon''(t)=-2-\varepsilon\big[(2-\omega^2)\sin(\omega\log t)+3\omega\cos(\omega\log t)\big]<0.
\]
Also \(q_\varepsilon'(0)=0\), so \(q_\varepsilon\) strictly decreases from \(1\) to \(0\); strict concavity and the endpoint values imply positivity in \((0,1)\). The function \(f_\varepsilon=\sqrt{q_\varepsilon}\) is strictly concave (composition of increasing concave square root with strictly concave positive \(q_\varepsilon\)), so its even extension produces a strictly convex solid of revolution. Its \(P(y)=-[1-\varepsilon\sin(\omega y)]\) has period \(h\), so both specified tests are passed by equation (2), but \(q_\varepsilon\) is not quadratic. For example, scales \(2\) and \(4\) work with \(h=\log2\), while scale \(3\) detects the failure.

**4. Regularity threshold.** If \(q\) has a second-order Taylor expansion at \(0\), then \(q(t)=q(0)+at+ct^2+o(t^2)\). Equation (1), for one fixed \(s>1\), gives \(a=sa\), forcing \(a=0\). Therefore \(P(y)\to c\) as \(y\to\infty\); a continuous periodic function with a limit at infinity is constant. The spheroid conclusion follows. On the other hand, the example has bounded second derivative wherever \(t>0\), and \(q_\varepsilon'\) is Lipschitz through \(0\), but \(q_\varepsilon''(t)\) oscillates without a limit at \(0\); there is no second-order Taylor coefficient there. The even surface is \(C^{1,1}\) near the equator because \(f_\varepsilon=\sqrt{q_\varepsilon}\) has bounded second derivative there; away from the equator it is smooth, including at the two tips by solving locally for the axial coordinate as a smooth function of squared cylindrical radius (since \(q_\varepsilon'(1)<0\)). Thus \(C^{1,1}\) of the full solid boundary does not suffice for one-scale rigidity.

## Verification
The included standalone Python script `check_discrete_coring.py` independently evaluates the disk-washer formula by Simpson quadrature for 50 common heights and scales \(2\) and \(4\), checks the derivative signs for 3000 interior radii, verifies 6000 discrete-dilation identities, and checks that scale \(3\) gives a definite discrepancy. It prints the maximum numerical mismatch; the numerical tests are diagnostics, not substitutes for the analytic equivalence and curvature bound.

## Relationship to prior work
Coll and Dodd proved the all-scale coring characterization for centrally symmetric surfaces of revolution and analyzed nonsymmetric profiles. Their individual-scale volume identity is the starting algebraic equation here; their hypothesis assumes invariance over the entire continuous family of dilations, whereas the present theorem characterizes arbitrary *individual* scale tests and proves a two-scale arithmetic rigidity boundary, including strictly convex false positives for commensurate tests and a sharp one-scale regularity threshold. The elementary sphere example also appears in standard integration texts. The 1996 dated column cited by Coll and Dodd supplies an earlier public discussion of the classical phenomenon, not a claim of priority for the present discrete-scale theorem.

## Limitations
The two-scale conclusion requires equality of the entire ring-volume **function of height** at both scales, not equality for finitely many selected heights or approximate noisy measurements. It assumes an axially symmetric profile monotone from the equator to the tips. The theorem does not classify nonsymmetric meridians, non-coaxial bores, or stability under approximate equalities. Its priority is provisional: the volume equation is classical, and relevant results on multiplicative functional equations may imply some aspects of its discrete-period refinement. Independent validation has not been performed.

## References
1. V. Coll and J. Dodd, *Which Surfaces of Revolution Core Like a Sphere?*, Mathematics Magazine **83** (2010), 191–199, DOI 10.4169/002557010X494832. Full-text transcription: https://www.academia.edu/90112758/Which_Surfaces_of_Revolution_Core_Like_a_Sphere
2. M. vos Savant, *Ask Marilyn*, Parade Magazine, October 20, 1996, and December 15, 1996, as bibliographically cited by Coll and Dodd; the original column was not inspected directly.
3. University of Kentucky, *Calculus II: Volumes*, Example 1.6.7, https://clp.math.uky.edu/clp2/sec_int_volumes.html (classical napkin-ring example).
