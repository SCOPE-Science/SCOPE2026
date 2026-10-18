# Corrected Floquet multiplier for bilateral Leslie–Gower control
## Finding

Consider the bilateral state-feedback system in which the continuous dynamics are
\[
\dot x=P(x,y),\qquad \dot y=Q(x,y),
\]
with an upper intervention at \(x=h_2\),
\[
(x,y)\mapsto\bigl((1-p_2)x,\;y+\tau_2\bigr),
\]
and a lower intervention at \(x=h_1\),
\[
(x,y)\mapsto\bigl((1+p_1)x,\;y-\tau_1\bigr).
\]
For every transversal order-2 periodic orbit with the source's labeling
\[
A_4\longrightarrow B_4\longmapsto C_4\longrightarrow D_4\longmapsto A_4,
\]
the derivative of the scalar Poincaré return map is
\[
\mu=
\frac{P(C_4)}{P(B_4)}
\frac{P(A_4)}{P(D_4)}
\exp\!\left(
\int_0^{T_1+T_2}
(P_x+Q_y)(x(t),y(t))\,dt
\right).
\]
Here
\[
B_4=(h_2,y_{B_4}),\quad
C_4=((1-p_2)h_2,y_{B_4}+\tau_2),
\]
and
\[
D_4=(h_1,y_{D_4}),\quad
A_4=((1+p_1)h_1,y_{D_4}-\tau_1).
\]
Therefore the lower post-jump factor is necessarily
\[
P(A_4)=P\!\left((1+p_1)h_1,\;y_{D_4}-\tau_1\right).
\]

The explicit expansion of \(P^+(A_4)\) printed in Theorem 3.5 of the source instead uses \(\tau_2\) in the predator coordinate and also mixes a \(D_3\) index into the expression. That expansion is not the vector field at the stated post-jump point whenever the two predator impulses differ. The abstract quotient \(\Delta_2=P(A_4)/P(D_4)\) remains valid when evaluated at the actual point \(A_4\).

For the source's Example 4.3 parameter set
\[
(h_1,h_2,p_1,p_2,\tau_1,\tau_2)
=(30,65,0.45,0.4,2,5),
\]
a high-accuracy shooting reconstruction gives
\[
A_4\approx(43.5,47.18576312),\quad
B_4\approx(65,60.39077878),
\]
\[
C_4\approx(39,65.39077878),\quad
D_4\approx(30,49.18576312).
\]
The corrected multiplier is
\[
\mu\approx0.19233304.
\]
A centered finite-difference derivative of the Poincaré return map gives \(0.19233303\), while evaluating the lower post-jump prey velocity with the printed \(\tau_2\) substitution gives approximately \(0.40351843\). The cycle therefore remains orbitally stable in this example, but the printed explicit stability margin is wrong by more than a factor of two.

## Assumptions and scope

The result concerns the deterministic bilateral impulsive system (2.1) in Xu, Shen, and Cao (2026). The continuous vector field is continuously differentiable along the periodic orbit, and both threshold crossings are transversal:
\[
P(B_4)\ne0,\qquad P(D_4)\ne0.
\]
The reset maps are exactly those printed for the upper and lower interventions. The exact formula is independent of the numerical Example 4.3 reconstruction. The numerical values are a reproducibility check for the published parameter set, not a proof of the generic formula.

## Proof

For a threshold surface \(x=h\), the normal vector is \(n=(1,0)^T\). Let a reset have the form
\[
R(x,y)=(c x,\;y+d),
\]
where \(c>0\) and \(d\) is constant. Its derivative is
\[
DR=\begin{pmatrix}c&0\\0&1\end{pmatrix}.
\]
At a transversal impact, the saltation matrix is
\[
S=DR+\frac{(f^+-DR\,f^-)n^T}{n^Tf^-},
\qquad f=(P,Q)^T.
\]
The matrix determinant lemma gives
\[
\det S
=\det(DR)\left(
1+\frac{n^TDR^{-1}(f^+-DRf^-)}{n^Tf^-}
\right)
=\frac{P^+}{P^-}.
\]
Thus the upper jump contributes \(P(C_4)/P(B_4)\), and the lower jump contributes \(P(A_4)/P(D_4)\).

Between jumps, Liouville's formula gives the determinant of the variational flow:
\[
\exp\!\left(
\int(P_x+Q_y)\,dt
\right).
\]
For the planar autonomous hybrid cycle, the nontrivial orbital multiplier is the product of the two saltation determinants and the continuous-flow determinant, yielding the displayed formula.

The lower reset is
\[
(h_1,y_{D_4})
\mapsto
((1+p_1)h_1,y_{D_4}-\tau_1).
\]
Consequently any expansion of \(P(A_4)\) must contain \(y_{D_4}-\tau_1\). The source's use of \(\tau_2\) in this lower post-jump evaluation cannot represent the same reset when \(\tau_1\ne\tau_2\). This establishes the symbolic correction independently of numerical simulation.

## Verification

The accompanying script `verification/reproduce.py` reconstructs Example 4.3 by event-driven numerical integration, solves the scalar return equation by bracketing, integrates the divergence along both flow legs, and evaluates the two saltation ratios. It also differentiates the return map by centered finite differences as an independent numerical check.

The script verifies
\[
\mu_{\mathrm{saltation}}\approx0.19233304
\]
and
\[
\mu_{\mathrm{return}}\approx0.19233303.
\]
It separately evaluates the erroneous lower post-jump substitution \(y_{D_4}-\tau_2\), obtaining approximately \(0.40351843\) after the same remaining factors are applied. The numerical tolerance is deliberately much smaller than the discrepancy between these values.

## Relationship to prior work

Xu, Shen, and Cao derive the bilateral control model, construct the order-2 periodic orbit, and state its orbital-stability criterion. Their own point definitions give
\[
y_{A_4}=y_{D_4}-\tau_1,
\]
while their displayed expansion of \(P^+(A_4)\) uses \(\tau_2\); the present result reconciles the general saltation criterion with the stated reset map.

Earlier bilateral state-feedback work develops general successor-function and Floquet methods for other predator-prey or resource-management systems. In particular, the 2020 resource-control paper cited below gives a general Floquet multiplier framework, and Tian, Liu, and Sun analyze order-2 periodic solutions in a different Allee-effect fishery model. Those results supply methodological context but do not evaluate the 2026 Leslie–Gower orbit or imply the source-specific \(\tau_1\)-versus-\(\tau_2\) correction.

Semantic searches for the source DOI, exact title, order-2 Floquet multiplier, bilateral Leslie–Gower control, and state-dependent impulsive predator-prey stability did not locate a published correction of this expression. General hybrid/Floquet results do not by themselves record which post-jump coordinate the 2026 model must use.

## Limitations

The theorem corrects the explicit Floquet multiplier associated with an already existing transversal order-2 orbit; it does not prove existence of such an orbit outside the source's existence hypotheses. The numerical Example 4.3 reconstruction is approximate and does not certify a global bifurcation diagram. Although the corrected and printed evaluations both predict stability for the published parameter set, their quantitative margins differ substantially, so parameter boundaries obtained from the printed expansion require recomputation. Literature search cannot exclude an unindexed erratum or unpublished correction.

## References

1. Jing Xu, Haoyang Shen, Xinyi Cao, “Dynamics of a modified Leslie–Gower model with dual Allee effects under unilateral and bilateral control,” *AIMS Mathematics* 11(6), 17820–17837 (2026), DOI 10.3934/math.2026726.
2. “Dynamics of Unilateral and Bilateral Control Systems with State Feedback for Renewable Resource Management,” *Complexity* (2020), DOI 10.1155/2020/9453941.
3. Yuan Tian, Yang Liu, Kaibiao Sun, “Complex dynamics of a predator-prey fishery model: The impact of the Allee effect and bilateral intervention,” *Electronic Research Archive* 32(11), 6379–6404 (2024), DOI 10.3934/era.2024297.
