# A supercritical Hopf threshold for periodic coexistence in a predator-dependent replicator

## Finding

Consider the three-population predator-dependent replicator of Cruz and Neves, based on Braga and Wardil, with the strictly positive reproductive and capture payoff matrices
\[
M_R=\begin{pmatrix}13/8&9/8\\9/8&5/8\end{pmatrix},\qquad
M_P=\begin{pmatrix}1&3/2\\1/2&1\end{pmatrix},
\]
and predator mortality parameter \(\beta=1\). Vary only the carrying-capacity parameter \(K>0\). At the exact value \(K_*=8\), the unique equilibrium in which both prey types and the predator coexist undergoes a **nondegenerate supercritical Hopf bifurcation**. More precisely, there is \(\varepsilon>0\) such that, for \(8-\varepsilon<K<8\), the positive equilibrium is locally asymptotically stable, whereas for \(8<K<8+\varepsilon\) it is unstable and a locally unique (up to phase), orbitally asymptotically stable periodic orbit lies entirely in the biological interior.

With the multilinear Hopf normalization specified below, the first Lyapunov coefficient is exactly
\[
\ell_1=-\frac{369}{66820}<0,
\]
and the real part of the critical eigenvalue pair crosses the imaginary axis with positive derivative \(1/130\) with respect to \(K\). Thus the attracting cycle and its location on the \(K>8\) side follow from the nondegenerate Hopf theorem, rather than numerical simulation.

## Assumptions and scope

Let \(A,B>0\) be the two prey populations and \(Y>0\) the rescaled predator population. Write \(x=A/(A+B)\in(0,1)\), \(P=A+B>0\), and \(k=1/K\). With the above matrices the exact population equations are
\[
\begin{aligned}
\dot x&=\tfrac12 x(1-x)(1-Y),\\
\dot P&=P(\tfrac58+x-kP-Y),\\
\dot Y&=Y(P-1).
\end{aligned}
\]
The coordinate change \((A,B,Y)\leftrightarrow(x,P,Y)\) is smooth and invertible whenever \(A,B>0\). The theorem concerns the continuous-time deterministic ODE with all matrix entries strictly positive, and only a sufficiently small neighborhood of \(K=8\). All statements of uniqueness concern equilibria in the interior or periodic solutions in a neighborhood of the Hopf point, not global attractors.

## Proof

**Payoff reduction.** The two reproduction rates are \(f_A^R=9/8+x/2\) and \(f_B^R=5/8+x/2\), so their difference is \(1/2\), and their population average is \(r(x)=5/8+x\). The two capture rates are \(g_A=3/2-x/2\) and \(g_B=1-x/2\), so their difference is \(1/2\), and their population average is exactly \(\delta(x)=1\). Substitution into the original replicator–predator equations yields the displayed system, with no approximation.

**Positive equilibrium and Jacobian.** Interior equilibrium requires \(Y=1\) from the first equation and \(P=1\) from the third; the second then forces
\[
x_*=\tfrac38+k,\qquad P_*=Y_*=1.
\]
It lies in the biological interior exactly for \(0<k<5/8\). Its Jacobian and characteristic polynomial are
\[
J(k)=\begin{pmatrix}
0&0&-x_*(1-x_*)/2\\
1&-k&-1\\
0&1&0
\end{pmatrix},\qquad
\chi(\lambda,k)=\lambda^3+k\lambda^2+\lambda+\tfrac12x_*(1-x_*).
\]
For a cubic with strictly positive coefficients, the Routh–Hurwitz condition for all eigenvalues to have negative real parts is \(k>x_*(1-x_*)/2\). Here
\[
k-\tfrac12x_*(1-x_*)=(k-\tfrac18)+\tfrac12(k-\tfrac18)^2.
\]
Consequently, the equilibrium is attracting for \(k>1/8\) sufficiently close and unstable for \(k<1/8\) sufficiently close. At \(k_*=1/8\), \(x_*=1/2\) and
\[
\chi(\lambda,k_*)=(\lambda+\tfrac18)(\lambda^2+1),
\]
so the spectrum is the simple set \(\{-1/8,+i,-i\}\). Implicit differentiation of \(\chi(\lambda(k),k)=0\) at \(\lambda=i\) gives
\[
\frac{d\lambda}{dk}\bigg|_{k_*}=-\frac{32}{65}-\frac{4i}{65},\qquad
\frac{d\operatorname{Re}\lambda}{dK}\bigg|_{K=8}=\frac1{130}>0.
\]
Thus the Hopf crossing is transverse and the third direction is strictly stable.

**Exact nonlinear coefficient.** Put \(X=x-1/2\), \(U=P-1\), \(V=Y-1\) at \(k=k_*\). The complete vector field in these centered coordinates is the following cubic polynomial, with no discarded terms:
\[
\begin{aligned}
\dot X&=-V/8+X^2V/2,\\
\dot U&=X-U/8-V+XU-U^2/8-UV,\\
\dot V&=U+UV.
\end{aligned}
\]
Let \(J_0=J(k_*)\), and let \(B=D^2F(0)\), \(C=D^3F(0)\) be the bilinear and trilinear derivatives (without factorial rescaling). Use the normalized right eigenvector and left eigenrow
\[
q=(i/8,i,1)^T,\qquad
\ell^T=\big((-32-4i)/65,\ (4-32i)/65,\ 1/2\big),
\]
which satisfy \(J_0q=iq\), \(\ell^TJ_0=i\ell^T\), and \(\ell^Tq=1\). Direct differentiation of the cubic field gives \(B(q,\bar q)=0\) and the exact Hopf contraction
\[
\begin{aligned}
G_{21}&=\ell^T\Big(C(q,q,\bar q)-2B(q,J_0^{-1}B(q,\bar q))\\
&\qquad\qquad+B(\bar q,(2iI-J_0)^{-1}B(q,q))\Big)\\
&=-\frac{369}{33410}-\frac{521107}{801840}i.
\end{aligned}
\]
Under the usual unit-frequency convention \(\ell_1=\operatorname{Re}G_{21}/(2\omega)\), \(\omega=1\), this yields \(\ell_1=-369/66820<0\). The exact contraction can be reconstructed from the self-contained accompanying symbolic checker; it computes the derivatives and both complex resolvents directly from the three displayed polynomials.

**Bifurcation and positivity.** The vector field is analytic in phase variables and \(K\) near the interior equilibrium, the critical pair is simple, no other eigenvalues have zero real part, the crossing is transverse, and \(\ell_1\ne0\). The classical nondegenerate Hopf theorem therefore produces a locally unique branch of small-amplitude periodic orbits on the side where the equilibrium's critical real part is positive, namely \(K>8\). Because \(\ell_1<0\), those cycles are orbitally asymptotically stable in the center directions, while the remaining real eigendirection stays exponentially contracting. The cycles shrink to the strictly positive equilibrium \((x,P,Y)=(1/2,1,1)\), hence remain in \(0<x<1\), \(P,Y>0\), and therefore have \(A=xP>0\) and \(B=(1-x)P>0\), for all sufficiently small positive \(K-8\).

## Verification

Run the accompanying `verify_hopf.py` with Python 3 and SymPy. It independently constructs the payoff-averaged ODE from both payoff matrices, verifies the interior equilibrium, computes the full characteristic polynomial and spectral crossing, differentiates all quadratic and cubic terms, normalizes the complex eigenvectors, and reproduces the exact number \(-369/66820\). The checker is a transparent exact-symbolic reproduction of specified algebra, not a substitute for the Hopf theorem or a global dynamical proof.

## Relationship to prior work

Cruz and Neves, arXiv:2607.13281 (first posted 2026-07-14), reformulate the Braga–Wardil predator-dependent replicator, derive equilibria and several stability and bifurcation results, and in Section 7 provide numerical evidence of stable three-population cycles. They explicitly state that those Hopf/periodic-orbit observations do not yet have proofs. The present result supplies an exact, different strictly-positive-payoff witness for which the full supercritical Hopf hypotheses and the stability of the generated periodic orbit are proved. The 2022 Braga–Wardil foundational analysis establishes the ecological model and its qualitative scenarios. Other published mathematical findings on this model address stability exchange at boundary collisions and constant-payoff neutral selection; neither implies the present nonzero imaginary-pair crossing or cubic Hopf coefficient. The standard Hopf theorem itself is classical, and only its model-specific verification is asserted here.

## Limitations

Only the chosen rational matrices and parameter neighborhood are treated. The theorem neither proves the existence or stability of the particular numerically observed cycles in the source paper's other payoff choices, nor classifies all possible equilibria, periodic orbits, basins or global persistence for arbitrary parameter values. No independent scientific audit or exhaustive priority search has been performed. Literature comparison is bounded to accessible primary sources and indexed published findings.

## References

1. H. M. Cruz and A. G. M. Neves, *Predator-dependent replicator dynamics or a predator-prey model with two prey types and frequency dependence*, arXiv:2607.13281, v1 publicly posted 2026-07-14, especially equations (6), (8)–(15) and Section 7. https://arxiv.org/abs/2607.13281 . Accessible author-posted full text: https://www.researchgate.net/publication/410160623_Predator-dependent_replicator_dynamics_or_a_predator-prey_model_with_two_prey_types_and_frequency_dependence .
2. G. Braga and M. Wardil, *The predator-dependent replicator dynamics*, Journal of Physics A: Mathematical and Theoretical 55 (2022), 025601. https://www.researchgate.net/publication/356867039_The_predator-dependent_replicator_dynamics .
3. Classical nondegenerate Hopf-bifurcation theorem and its standard multilinear first-Lyapunov-coefficient formula, used with the normalization specified in the proof.
