# Equilibrium rigidity and a sharp stability boundary in a Hermitian matrix logistic map

## Finding

Let \(N\geq1\) and let \(B=B^*>0\) be a complex Hermitian matrix with \(B\leq2I\). On the Hermitian order interval \(\mathcal K=\{X=X^*:0\leq X\leq I\}\), consider the matrix logistic map
\[
\Phi_B(X)=BX(I-X)B.
\]
**Fixed-point classification.** Every fixed point commutes with \(B\). Precisely,
\[
\operatorname{Fix}(\Phi_B)=\{(I-B^{-2})P:P=P^*=P^2,\ [P,B]=0,\ \operatorname{ran}P\subseteq\mathbf1_{(1,2]}(B)\mathbb C^N\}.
\]
If the distinct eigenvalues of \(B\) greater than one have multiplicities \(m_b\), the fixed-point space is the disjoint union of smooth compact components
\[
\operatorname{Fix}(\Phi_B)\simeq\prod_{b>1}\left(\bigsqcup_{r=0}^{m_b}\operatorname{Gr}_{\mathbb C}(r,m_b)\right).
\]
The empty product is one point. In particular, if the eligible eigenvalues are all simple, there are exactly \(2^k\) fixed points for \(k\) eligible eigenvalues. Repeated eligible eigenvalues give entire positive-dimensional manifolds of fixed points, although fixed points never mix distinct eigenspaces of \(B\).

**Sharp exponentially attracting equilibrium criterion.** Define \(X_*=(I-B^{-2})_+\), the spectral positive part. There exists a locally exponentially attracting fixed point in the Hermitian matrix space **if and only if** every eigenvalue \(b\) of \(B\) lies in
\[
(0,1)\cup(1,\sqrt3).
\]
When this condition holds, \(X_*\) is the unique such equilibrium, and every other fixed point is linearly unstable. If it fails, no fixed point is locally exponentially attracting. Here exponential attraction means an estimate \(\|\Phi_B^n(Y)-X\|\leq Cq^n\|Y-X\|\) on a neighborhood for some \(q<1\), in a fixed matrix norm.

## Assumptions and scope

The dimension is finite but arbitrary; matrices are complex Hermitian. Positive definiteness of the *coupling* \(B\), not just of \(BB^*\), is essential. We assume its eigenvalues lie in \((0,2]\), so the state interval is invariant. A spectral projection \(P\) commuting with \(B\) may choose any subspace inside a repeated eigenspace. The symbol \((\cdot)_+\) means the spectral positive part, and \(\operatorname{Gr}_{\mathbb C}(r,m)\) is the complex Grassmannian of \(r\)-planes in \(\mathbb C^m\). The classification includes all boundary and degenerate eigenspaces.

## Proof

**1. Forward invariance.** If \(0\leq X\leq I\), functional calculus gives \(0\leq X-X^2\leq I/4\). Hence \(0\leq\Phi_B(X)\leq B^2/4\leq I\).

**2. No unit eigenvalue at a fixed point.** Let \(X\) be fixed and put \(C=B^{-1}>0\), so \(CXC=X-X^2\). If \(Xv=v\) for a nonzero vector \(v\), then
\[
0=\langle v,(X-X^2)v\rangle=\langle Cv,X Cv\rangle.
\]
Positivity of \(X\) implies \(Cv\in\ker X\); since \(v\in\operatorname{ran}X\), one gets \(\langle v,Cv\rangle=0\), contradicting positive definiteness of \(C\). Thus all nonzero eigenvalues of \(X\) lie strictly between zero and one.

**3. Support invariance and a unique positive square root.** Let \(S=\operatorname{ran}X\). Because \(X-X^2\) has exactly the same support as \(X\), while \(\operatorname{ran}(CXC)=C S\), equality forces \(CS=S\). The self-adjoint matrix \(C\) reduces \(S\) and its orthogonal complement. On \(S\), \(X_S>0\); with \(W=X_S^{1/2}C_S X_S^{1/2}>0\),
\[
W^2=X_S^{1/2}(C_S X_S C_S)X_S^{1/2}=X_S^2(I_S-X_S).
\]
The **unique positive** square root is \(W=X_S(I_S-X_S)^{1/2}\), since the two factors on the right commute. Therefore \(C_S=(I_S-X_S)^{1/2}\), and
\[
X_S=I_S-C_S^2=I_S-B_S^{-2}.
\]
On \(S^\perp\), \(X\) vanishes; thus \(X\) commutes with \(B\), and \(S\) is contained in the direct sum of eigenspaces having \(b>1\). Conversely every such commuting projection \(P\) produces a fixed point. Within each eigenspace of dimension \(m_b\), rank-\(r\) orthogonal projections form \(\operatorname{Gr}_{\mathbb C}(r,m_b)\), proving the exact classification.

**4. Linearization.** The derivative at every fixed point is
\[
D\Phi_B(X)[H]=B(H-XH-HX)B.
\]
Choose a common orthonormal eigenbasis of \(B\) and \(X\); write \(B=\operatorname{diag}(b_i)\) and \(X=\operatorname{diag}(x_i)\). For each Hermitian matrix unit (one diagonal real mode, or two real modes on an off-diagonal pair), the derivative multiplier is
\[
\lambda_{ij}=b_i b_j(1-x_i-x_j),\qquad 1\leq i\leq j\leq N.
\]
For \(X_*\), the diagonal entries are \(x_i=0\) for \(b_i\leq1\), and \(x_i=1-b_i^{-2}\) for \(b_i>1\). The multiplier is \(b_i b_j\) if both are inactive, \(b_{\rm inactive}/b_{\rm active}\) if exactly one is active, and \((b_i^2+b_j^2-b_i^2b_j^2)/(b_ib_j)\) if both are active.

**5. Sufficiency of the stated spectral gap.** If all \(b_i\in(0,1)\cup(1,\sqrt3)\), then both-inactive and mixed multipliers lie in \((0,1)\). For two active values \(a,b\in(1,\sqrt3)\), the numerator \(a^2+b^2-a^2b^2=1-(a^2-1)(b^2-1)<1<ab\). For the other bound, let
\[
g(a,b)=a^2+b^2+ab-a^2b^2.
\]
For fixed \(a>1\), this is concave in \(b\); its minimum for \(1\leq b\leq\sqrt3\) lies at an endpoint. At \(b=1\), \(g=1+a>0\); at \(b=\sqrt3\), \(g=3+\sqrt3a-2a^2\), a concave function of \(a\in[1,\sqrt3]\) whose endpoint values are \(1+\sqrt3\) and \(0\). Thus \(g>0\) in the open square. This is exactly the strict lower bound \(\lambda_{ij}>-1\). All eigenvalues of the derivative at \(X_*\) therefore have modulus less than one, implying local exponential attraction by a finite-dimensional contraction argument.

**6. Necessity and uniqueness.** If a fixed point leaves an eigenvector of \(B\) with \(b>1\) unoccupied, its diagonal rank-one perturbation has derivative multiplier \(b^2>1\). Hence every candidate attracting fixed point must occupy **all** eigenspaces with \(b>1\), and so must equal \(X_*\). If a \(b=1\) mode occurs, \(X_*\) has multiplier \(+1\); if a \(b=\sqrt3\) mode occurs, its multiplier is \(-1\); if a \(b>\sqrt3\) mode occurs, its multiplier \(2-b^2<-1\). In the neutral cases an exponential estimate would force \(\rho(D\Phi_B(X_*))<1\), an impossibility. Thus the spectral condition is also necessary and there is exactly one exponentially attracting fixed point when it holds.

## Verification

The self-contained \(CHECK.py\) uses exact rational arithmetic to check four simultaneously admissible fixed points in a three-mode coupling, a rank-one **nondiagonal** fixed matrix at a repeated coupling eigenvalue, instability of partial selections, exact subcritical/supercritical diagonal multipliers, and a grid of mixed-mode multipliers. Invoke \(python CHECK.py\) from the extracted package. All checks passed. These finitely many examples are consistency checks; the six proof steps above establish the arbitrary-dimensional claims.

## Relationship to prior work

Pawela and Życzkowski introduced the general map \(X\mapsto BX(I-X)B^*\) and studied scalar-coupling invariant spectral measures, non-Hermitian analogues, and directed-graph propagation of chaos [1]. Section V and Appendix C discuss general and diagonal two-node couplings; they do not state the all-dimensional positive-self-adjoint equilibrium classification or sharp stable-equilibrium criterion shown here. Scalar logistic fixed points alone do not imply that an arbitrary **noncommuting** stationary matrix must commute with its coupling: that conclusion requires the support and positive-square-root argument above. Earlier matrix-logistic research analyzed scalar-multiple coupling and two-by-two idempotent eigenvalue dynamics [2]; these results do not imply commutation with an anisotropic positive coupling.

## Limitations

The theorem is about fixed points and their local **exponential** attraction, not global convergence or a full periodic-orbit census. A unit-modulus derivative at the boundary excludes exponential attraction but is not asserted to rule out slower nonlinear convergence. Non-self-adjoint, singular, or non-positive couplings are not classified. The smooth Grassmannian components need not consist of attracting fixed points. Independent mathematical validation has not been performed.

## References

[1] Ł. Pawela and K. Życzkowski, *Matrix logistic map: fractal spectral distributions and transfer of chaos*, arXiv:2303.06176 (first public version 10 March 2023), https://arxiv.org/abs/2303.06176 ; revised HTML text https://arxiv.org/html/2303.06176v2 .

[2] Z. Navickas, R. Smidtaite, A. Vainoras and M. Ragulskis, *The logistic map of matrices*, Discrete and Continuous Dynamical Systems B **16** (2011), 927–944, https://doi.org/10.3934/dcdsb.2011.16.927 .
