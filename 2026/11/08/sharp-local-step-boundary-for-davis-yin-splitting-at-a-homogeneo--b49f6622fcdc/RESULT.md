# Sharp local step boundary for Davis–Yin splitting at a homogeneous graph Gross–Pitaevskii ground state

## Finding

Consider the unmodified DYS I map of Li–Zheng–Zhang [1] with implicit kinetic matrix \(K=aI+G\), no separate potential, and explicit defocusing cubic nonlinearity. Here \(G\) is a connected undirected weighted-graph Laplacian on \(n\ge2\) vertices, \(a\ge0\), and \(\beta>0\). Put \(b=\beta/n\), \(c=a+b\), and let \(\Lambda>0\) be the largest eigenvalue of \(G\). For each step \(0<\gamma<1/c\), the positive homogeneous ground state corresponds to the fixed point \(z_\star=(1-\gamma c)n^{-1/2}\mathbf 1\).

Define the explicit critical step
\[
\gamma_\star=\frac{\Lambda-4b+\sqrt{(\Lambda-4b)^2+16(a+\Lambda)c}}{4(a+\Lambda)c}.
\]
The fixed point is locally linearly attracting for \(0<\gamma<\gamma_\star\), has a Jacobian eigenvalue \(-1\) at \(\gamma=\gamma_\star\), and is linearly unstable for \(\gamma_\star<\gamma<1/c\). For \(a>0\), only the top-Laplacian eigenspace reaches \(-1\) at the threshold and \(1/(2c)<\gamma_\star<1/c\). For \(a=0\), the critical step has the graph-independent closed form \(\gamma_\star=n/(2\beta)\): **every nonconstant graph eigenmode reaches \(-1\) simultaneously**, independent of edge weights and the largest graph frequency.

These are exact local properties of the auxiliary-variable fixed point, not unconditional or global convergence statements. Behavior precisely at the neutral eigenvalue \(-1\) is not classified nonlinearly.

## Assumptions and scope

Let \(G\in\mathbb R^{n\times n}\) be symmetric with nonpositive off-diagonal entries, zero row sums, and a connected graph of strictly positive edge weights. Consequently \(G\succeq0\) with \(\ker G=\operatorname{span}\{\mathbf1\}\). Let \(a\ge0\), \(\beta>0\), \(K=aI+G\). Work in exact real arithmetic and Euclidean normalization (unit diagonal mass matrix). Define the energy on the unit sphere by
\[
E(u)=\tfrac12u^{\mathsf T}Ku+\tfrac\beta4\sum_{i=1}^{n}u_i^4,\qquad\|u\|_2=1.
\]
For \(z\ne0\), write \(u(z)=z/\|z\|_2\) and use the DYS I iteration [1, Eq. (1.6)]
\[
F_\gamma(z)=z+(I+\gamma K)^{-1}\bigl(2u(z)-z-\gamma\beta u(z)^{\odot3}\bigr)-u(z).
\]
No linear potential is treated explicitly. The shift \(aI\) is part of the implicit matrix \(K\), modelling uniform killing or Dirichlet leakage. The case \(a=0\) is the connected graph/Neumann analogue, for which \(K\) is singular but \(I+\gamma K\) is invertible. We restrict to \(\gamma c<1\), which gives the positive fixed-point radius.

## Proof

**1. Ground state and fixed point.** Set \(e=n^{-1/2}\mathbf1\). Because \(Ge=0\), the Laplacian contribution is nonnegative and vanishes exactly on constant vectors. For all unit vectors, the power-mean/Cauchy–Schwarz inequality gives \(\sum_i u_i^4\ge1/n\), with equality exactly when all component magnitudes agree. Therefore \(\pm e\) are the only global energy minimizers, and \(e\) is the unique positive one. Also \(Ke=ae\) and \(e^{\odot3}=e/n\). For \(s=1-\gamma c>0\), substitution of \(z=se\) into \(F_\gamma\) yields \(F_\gamma(se)=se\). This proves the fixed-point assertion.

**2. Complete Jacobian spectrum.** Put \(P=I-ee^{\mathsf T}\), \(M=I+\gamma K\). The normalization derivative at \(se\) is \(Du(se)=P/s\), and the derivative of the cubic is \(3\operatorname{diag}(e_i^2)P/s=3P/(ns)\). Thus
\[
DF_\gamma(se)=I-M^{-1}+s^{-1}\bigl((2-3\gamma b)M^{-1}-I\bigr)P.
\]
The matrices \(G,M,P\) commute and share an orthonormal eigenbasis. On the radial vector \(e\) the eigenvalue is
\[
r_0(\gamma)=\frac{\gamma a}{1+\gamma a}\in[0,1).
\]
For every eigenvector of \(G\) orthogonal to \(e\), with \(Gv=\lambda v\), \(\lambda>0\), the eigenvalue is
\[
m_\lambda(\gamma)
=1-\frac{\gamma(\lambda+2b)}{(1-\gamma c)(1+\gamma(a+\lambda))}.
\]
The denominator is positive throughout the stated step interval. Hence \(m_\lambda<1\) always. Moreover
\[
(1+m_\lambda)(1-\gamma c)(1+\gamma(a+\lambda))
=P_\lambda(\gamma),\quad
P_\lambda(\gamma)=2+\gamma(\lambda-4b)-2\gamma^2(a+\lambda)c.
\]
Consequently the Jacobian is a strict Euclidean contraction exactly when \(P_\lambda(\gamma)>0\) for every nonzero Laplacian eigenvalue.

**3. Determine the sharp boundary.** Rewrite
\[
P_\lambda(\gamma)=2-4\gamma b-2\gamma^2ac+\gamma\lambda(1-2\gamma c).
\]
For \(0<\gamma\le1/(2c)\), the coefficient of \(\lambda\) is nonnegative; the lower bound \(P_\lambda(\gamma)\ge P_0(\gamma)\) is positive for \(a>0\) and \(\gamma\le1/(2c)\), since \(P_0\) strictly decreases to \(3a/(2c)>0\) there. If \(a=0\), direct factorization gives
\[
P_\lambda(\gamma)=(1-2\gamma b)(2+\gamma\lambda),
\]
so the single exact threshold \(\gamma=1/(2b)\) applies to every positive \(\lambda\).

For \(a>0\) and \(\gamma>1/(2c)\), the expression \(P_\lambda\) decreases strictly with \(\lambda\); therefore the first eigenvalue to reach \(-1\) is at \(\lambda=\Lambda\). The concave quadratic \(P_\Lambda(\gamma)\) has \(P_\Lambda(1/(2c))=3a/(2c)>0\), \(P_\Lambda(1/c)=-(\Lambda+2b)/c<0\), and exactly one positive root. Solving that quadratic yields \(\gamma_\star\) as stated. At equality the \(\Lambda\)-eigenspace has eigenvalue \(-1\), while every smaller positive Laplacian eigenspace remains strictly inside the unit disk. Above it and below \(1/c\), \(P_\Lambda<0\), hence \(m_\Lambda<-1\). For \(a=0\), the factorization instead forces all nonconstant modes to equal \(-1\) at \(1/(2b)\).

**4. Dynamical interpretation.** The map is \(C^1\) near \(se\) and the Jacobian is symmetric. When all eigenvalues have modulus below one, continuity of the derivative produces a small invariant Euclidean ball on which the map is a strict contraction; fixed-point iterates starting in that ball converge linearly. When \(m_\Lambda<-1\), the fixed point has a linearly expanding eigenmode and is linearly unstable. At \(m_\Lambda=-1\), the spectral argument proves neither attraction nor nonlinear instability; no stronger boundary assertion is made.

## Verification

Run `python VERIFY.py` with NumPy and SymPy. The script checks the symbolic eigenvalue and phase-polynomial identities, an independent exact-rational three-vertex example, and numerical finite-difference Jacobians on multiple connected graph paths and parameter choices. Its successful run reported 1,208 assertions. Finite sampling is supplementary; the proof above supplies the all-graph and all-step result.

For a three-vertex path with unit edges, \(\sigma(G)=\{0,1,3\}\). At \(a=1\), \(\beta=3\), \(\gamma=1/3\), the radius is \(s=1/3\), the radial multiplier is \(1/4\), the two transverse multipliers are \(-4/5\) and \(-8/7\). The exact threshold is \((\sqrt{129}-1)/32<1/3\). Hence a high-frequency mode is unstable while a lower-frequency mode is stable. With the same graph, \(a=0\), and \(\beta=3\), all transverse eigenvalues equal \(-1\) exactly at \(\gamma=1/2\).

## Relationship to prior work

Li, Zheng, and Zhang [1, Eq. (1.6)] introduce DYS I; their Theorem 3.4 proves global convergence for restricted positive starts under explicit small-step conditions, while their Theorem 5.1 proves a local linear rate using a Lyapunov estimate within those conditions. Neither statement supplies the exact homogeneous-graph Jacobian spectrum or a sharp boundary separating local contraction from instability across the entire positive fixed-point range. Zheng and Zhang [2, Section 4.1] study local Hessian-controlled rates of *Riemannian gradient flows*, a different iteration whose rate theorem does not imply this DYS I spectral boundary. General Davis–Yin splitting principles [3] underpin the algorithm, but the graph-specific simultaneous critical mode and the closed threshold require the present spectral calculation. The use of Cauchy–Schwarz, Laplacian spectral decomposition, and local contraction theory is classical; no claim to those tools is made.

## Limitations

This is a local linear-stability classification of \(F_\gamma\), not global convergence from arbitrary initial data. The \(-1\) boundary may have nonlinear dynamics not determined here. The fixed point and formula are specific to homogeneous cubic coupling, constant implicit shift, connected symmetric graph Laplacians, and Euclidean mass normalization. No conclusions are asserted for nonconstant potentials, weighted mass matrices, nonlinear boundary conditions, changing step sizes, or the source paper's distinct DYS II update. The \(a=0\) singular kinetic matrix is an explicit extension beyond the source's strictly coercive setting. The numerical verifier does not replace the proof. Independent mathematical validation remains outstanding.

## References

[1] J. Li, S. Zheng, and X. Zhang, *Global convergence of an efficient splitting method for the defocusing Gross–Pitaevskii ground state problem*, arXiv:2609.13509v1, first public September 11, 2026. https://arxiv.org/abs/2609.13509

[2] S. Zheng and X. Zhang, *Riemannian Hessian analysis of Sobolev gradient flows for the Gross–Pitaevskii ground state problem*, arXiv:2610.12833v1, first public October 9, 2026. https://arxiv.org/abs/2610.12833

[3] D. Davis and W. Yin, *A Three-Operator Splitting Scheme and Its Optimization Applications*, Set-Valued and Variational Analysis 25 (2017), 829–858; open preprint arXiv:1504.01032 (2015). https://arxiv.org/abs/1504.01032
