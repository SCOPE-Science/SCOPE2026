# Entropy-gauge and corner-minimization obstructions in entropy-based local characteristic decomposition

## Result

The recent entropy-based local characteristic decomposition (ELCD) of Chu, Herty, and Kurganov (arXiv:2609.19838v1) proposes, for the ideal-gas Euler equations, to choose an interface state by minimizing the mathematical entropy
\[
\eta_0(\rho,p)=-\frac{\rho}{\gamma-1}\log\!\left(\frac{p}{\rho^\gamma}\right),\qquad \rho,p>0,\quad \gamma>1,
\]
over the rectangle whose density and pressure coordinates are supplied by the two neighboring states. The paper then evaluates only the four rectangle corners, invoking convexity of \(\eta_0\).

Two structural obstructions follow.

### 1. Convexity does not reduce the rectangle minimum to the corners

The entropy is indeed strictly convex in \((\rho,p)\):
\[
\nabla^2\eta_0=
\frac1{\gamma-1}
\begin{pmatrix}
\gamma/\rho & -1/p\\
-1/p & \rho/p^2
\end{pmatrix},
\qquad
\det\nabla^2\eta_0=\frac1{(\gamma-1)p^2}>0.
\]
But convexity is compatible with an interior minimum; it is maxima, not minima, for which extreme-point arguments are available on a polytope.

Let
\[
R=[\rho_-,\rho_+]\times[p_-,p_+],\qquad 0<\rho_-<\rho_+,
\quad 0<p_-<p_+.
\]
Since
\[
\partial_p\eta_0=-\frac{\rho}{(\gamma-1)p}<0,
\]
the exact minimizer always lies on the upper pressure edge \(p=p_+\). Along that edge,
\[
\partial_\rho\eta_0=\frac{\gamma\log\rho+\gamma-\log p_+}{\gamma-1},
\]
so the unique continuous minimizer is
\[
\boxed{
(\widehat\rho,\widehat p)=
\left(
\Pi_{[\rho_-,\rho_+]}
\left(e^{-1}p_+^{1/\gamma}\right),\ p_+
\right),
}
\]
where \(\Pi\) denotes scalar clipping. Whenever
\[
\rho_-<e^{-1}p_+^{1/\gamma}<\rho_+,
\]
the stated rectangle minimizer lies strictly inside an edge and is therefore missed by every four-corner rule.

The excess entropy at any density \(\rho\) on the upper edge, when the unconstrained minimizer \(\rho_* =e^{-1}p_+^{1/\gamma}\) lies inside the interval, is exactly
\[
\boxed{
\eta_0(\rho,p_+)-\eta_0(\rho_*,p_+)
=
\frac{\gamma}{\gamma-1}
\left[
\rho\log\frac{\rho}{\rho_*}-\rho+\rho_*
\right]>0
}
\]
for \(\rho\ne\rho_*\).

For example, with \(\gamma=1.4\) and
\[
R=[0.2,0.6]\times[0.5,1],
\]
the continuous minimizer is
\[
(\rho_*,p_+)=(e^{-1},1)=(0.367879441171\ldots,1),
\]
with \(\eta_0=-1.287578044100\ldots\). The best corner is \((0.2,1)\), with \(\eta_0=-1.126606538704\ldots\), leaving a strict gap \(0.160971505396\ldots\).

Thus Algorithm 1 is a discrete four-candidate selector, but it is not in general the minimizer of the continuous rectangle problem stated immediately before it.

### 2. The selected ELCD state depends on an arbitrary entropy gauge

For the Euler equations, adding a constant multiple of mass density to an entropy density produces an equivalent entropy pair. If \((\eta,q)\) is an entropy pair, then for any \(c\in\mathbb R\),
\[
\eta_c(U)=\eta(U)+c\rho,
\qquad
q_c(U)=q(U)+c\rho u
\]
in the \(x\)-direction (and analogously in other directions) differs from \((\eta,q)\) only by \(c\) times the mass conservation law. Its Hessian is unchanged, so convexity and the entropy inequality are unchanged as well.

For the ideal-gas entropy used by ELCD this freedom is also the ordinary arbitrary reference constant of specific entropy. Equivalently, replacing the logarithm by
\[
\eta_A(\rho,p)=
-\frac{\rho}{\gamma-1}
\log\!\left(A\frac{p}{\rho^\gamma}\right),
\qquad A>0,
\]
gives
\[
\eta_A=\eta_0+c\rho,
\qquad
c=-\frac{\log A}{\gamma-1}.
\]

This gauge freedom changes the ELCD ranking whenever candidate densities differ. For any finite candidate family with scores
\[
s_i(c)=\eta_0(U_i)+c\rho_i,
\]
as \(c\to+\infty\) minimizers are forced toward the smallest candidate density, while as \(c\to-\infty\) they are forced toward the largest candidate density. Hence a candidate selector based on the absolute entropy density cannot be invariant under the admissible mass-affine entropy gauge unless all candidate densities agree.

The continuous rectangle problem exhibits the same defect. For \(\eta_c\), its exact minimizer is
\[
\boxed{
\widehat\rho_c=
\Pi_{[\rho_-,\rho_+]}
\left(
 e^{-1-(\gamma-1)c/\gamma}p_+^{1/\gamma}
\right),
\qquad
\widehat p_c=p_+.
}
\]
For every desired interior density \(\rho_0\in(\rho_-,\rho_+)\), choosing
\[
\boxed{
 c=
 \frac{\log p_+-\gamma(\log\rho_0+1)}{\gamma-1}
}
\]
makes \(\rho_0\) the unique entropy minimizer. Thus even the continuous minimizer is not an intrinsic object until an entropy gauge is fixed.

A small explicit branch flip occurs already for \(\gamma=1.4\), equal pressures \(p_L=p_R=1\), and densities
\[
\rho_L=0.25,
\qquad
\rho_R=1.
\]
At \(c=0\),
\[
\eta_0(\rho_L,1)=-1.213007565980\ldots<0=\eta_0(\rho_R,1),
\]
so Algorithm 1 selects the left density. At the equivalent gauge \(c=-2\),
\[
\eta_{-2}(\rho_L,1)=-1.713007565980\ldots>
-2=\eta_{-2}(\rho_R,1),
\]
so it selects the right density. The switch threshold is
\[
 c_*=-1.617343421307\ldots,
\]
corresponding to the modest logarithmic reference factor
\[
 A_*=e^{-(\gamma-1)c_*}=1.909683207821\ldots.
\]
If the two cells have velocities \(u_L=-2\) and \(u_R=2\), Algorithm 1 also switches which cell velocity is used. The corresponding \(x\)-Jacobian characteristic speeds change from
\[
(-4.366431913240,-2,-2,0.366431913240)
\]
to
\[
(0.816784043380,2,2,3.183215956620),
\]
although the Euler equations and admissible entropy inequality are unchanged.

## A gauge-invariant diagnostic

Dividing by density removes exactly this mass-affine ambiguity:
\[
\frac{\eta_c}{\rho}=\frac{\eta_0}{\rho}+c.
\]
Therefore rankings by the specific mathematical entropy \(\eta/\rho\) are invariant under \(\eta\mapsto\eta+c\rho\). For the ideal-gas formula,
\[
\frac{\eta_0}{\rho}
=-\frac1{\gamma-1}\log\!\left(\frac{p}{\rho^\gamma}\right),
\]
which is strictly increasing in \(\rho\) and strictly decreasing in \(p\); its rectangle minimizer is simply \((\rho_-,p_+)\). This observation gives a cheap gauge-invariant alternative score, but no claim is made here that it improves ELCD accuracy or shock resolution.

## Verification

The accompanying script checks strict convexity, the exact interior rectangle minimizer, the four-corner gap, the gauge-induced branch flip and threshold, invariance of the specific-entropy ranking, and the ability to place the continuous minimizer at an arbitrary interior density by choosing an equivalent gauge.

## Originality boundary and limitations

The following facts are prior art and are not claimed as new: convex functions may have interior minima; Euler specific entropy is defined only up to an additive constant; affine conserved quantities may be added to entropy pairs; and compressible Euler admits a broad family of generalized entropy densities. Harten, Lax, Levermore, and Morokoff explicitly discuss the additive constant in specific entropy and the generalized family \(\rho f(\sigma)\). Classical minimum-entropy principles concern specific entropy and are likewise not new here.

The claimed contribution is source-specific: the rectangle-minimization statement in arXiv:2609.19838v1 is not implemented by its corner test; the exact continuous minimizer is given above; and the proposed absolute-entropy ranking can switch its selected density and characteristic linearization under the standard entropy-reference freedom. Searches by the paper title, arXiv identifier, corner-minimization formulation, and entropy-gauge terminology did not locate an existing correction or an overlapping SCOPE record.

This result does not show that the published ELCD experiments are inaccurate, unstable, or lower order. A fixed entropy normalization makes Algorithm 1 perfectly well-defined as a four-candidate heuristic, and its empirical benefits may persist. The result only shows that the stated continuous minimization justification is mathematically incorrect and that the selection is not invariant under equivalent entropy representatives. The proposed specific-entropy score is an invariance repair, not a demonstrated replacement method.

## References

1. S. Chu, M. Herty, A. Kurganov, *Entropy-Based Local Characteristic Decomposition*, arXiv:2609.19838v1 (2026).
2. A. Harten, P. D. Lax, C. D. Levermore, W. J. Morokoff, *Convex Entropies and Hyperbolicity for General Euler Equations*, SIAM J. Numer. Anal. 35 (1998), 2117–2127, DOI: 10.1137/S0036142997316700.
3. E. Tadmor, *A Minimum Entropy Principle in the Gas Dynamics Equations*, Applied Numerical Mathematics 2 (1986), 211–219.
4. C. Berthon, B. Dubroca, A. Sangam, *A Local Entropy Minimum Principle for Deriving Entropy Preserving Schemes*, SIAM J. Numer. Anal. 50 (2012), 468–491, DOI: 10.1137/100814445.
