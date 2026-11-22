# Three species are sharp for reversing community stability by swapping fast life-stage turnover

## Finding
A stage-structured ecological community can have exactly zero *aggregate* interspecies effects and yet its local coexistence stability can change when the relative speeds of juvenile replenishment and adult replenishment are exchanged. For every finite species count \(S\), the high-turnover stability matrix is exactly \(-2I+\delta C\), with \(\delta=(b-a)/(a+b)\). Three species are necessary and sufficient for changing the *limiting* stability verdict merely by switching \(a\) and \(b\). An explicit three-species cycle changes from a saddle to a strict local sink; the change is certified already at turnover scale \(L=50\).

## Assumptions and scope
Fix \(S\ge1\), \(a,b>0\), and \(L>0\). Each species \(i\) has positive stage populations \(x_{i1},x_{i2}\). For \(\alpha\in\{1,2\}\), write \(\bar\alpha=3-\alpha\) and let \(r_1=aL\), \(r_2=bL\). Consider the ODE
\[
\dot x_{i\alpha}=\mu_{i\alpha}x_{i\alpha}+r_\alpha x_{i\bar\alpha}-x_{i\alpha}(x_{i1}+x_{i2})+x_{i\alpha}\sum_{j\ne i}\sum_{\beta=1}^2B_{ij}^{\alpha\beta}x_{j\beta}.
\]
The real interspecies coefficients are independent of \(L\) and obey \(\sum_{\alpha,\beta}B_{ij}^{\alpha\beta}=0\) for every directed pair \(i\ne j\). Set \(\mu_{i\alpha}=2-r_\alpha-\sum_{j\ne i,\beta}B_{ij}^{\alpha\beta}\); for sufficiently large \(L\), all these rates are negative, and the strictly positive state \(x_{i\alpha}=1\) is an equilibrium. The influx terms allow stage mixing; these are not unidirectional maturation-only equations. Define the zero-diagonal matrix \(C\) by \(C_{ij}=B_{ij}^{11}+B_{ij}^{12}\) for distinct \(i,j\). The condition of zero aggregate interaction forces \(B_{ij}^{21}+B_{ij}^{22}=-C_{ij}\). Define \(\delta=(b-a)/(a+b)\). No symmetry, sign or randomness assumption is imposed on \(C\).

## Proof
**Exact Jacobian.** At the prescribed coexistence point, the within-species block of the Jacobian is
\[
D_L=\begin{pmatrix}-1-aL&-1+aL\\-1+bL&-1-bL\end{pmatrix},
\]
while the off-species block from \(j\) to \(i\) is \(B_{ij}\). Direct differentiation of the stated ODE yields this matrix, not merely an assumed linearization.

**Separation into slow and fast modes.** Write the full matrix as \(J_L=LM+H\), where \(M\) is block diagonal with identical blocks \(\begin{psmallmatrix}-a&a\\b&-b\end{psmallmatrix}\). This block has a simple zero eigenvalue, right eigenvector \(v=(1,1)^\mathsf T\), normalized left eigenvector \(w=(b,a)^\mathsf T/(a+b)\), and another eigenvalue \(-(a+b)\). Thus the zero eigenvalue of \(M\) is semisimple of multiplicity \(S\). The standard finite-dimensional Schur-complement expansion around its spectral subspace gives \(S\) slow eigenvalues converging (with algebraic multiplicity) to those of the compressed matrix \(P H P\), and \(S\) eigenvalues equal to \(-(a+b)L+O(1)\). No large-\(S\) or random-matrix limit is needed. The self block of \(H\) has row sums \(-2\), hence contributes \(-2\); the \((i,j)\) entry for \(i\ne j\) is
\[
w^\mathsf T B_{ij}v=\frac{b(B_{ij}^{11}+B_{ij}^{12})+a(B_{ij}^{21}+B_{ij}^{22})}{a+b}=\delta C_{ij}.
\]
Consequently the limiting slow matrix is \(-2I+\delta C\). Strict inequalities between spectral abscissa and zero are preserved for all sufficiently large \(L\); no claim is made at the nonhyperbolic limiting threshold.

**Sharp minimum of three species.** For \(S=1\), \(C=0\). For \(S=2\), its zero diagonal implies \(\chi_C(z)=z^2-C_{12}C_{21}\), which is unchanged under replacing \(C\) by \(-C\). Interchanging \(a,b\) replaces \(\delta\) by \(-\delta\), so the limiting slow spectra, and therefore strict stability verdicts, agree for \(S\le2\).

For \(S=3\), take a directed cyclic interaction of weight six: \(C_{12}=C_{23}=C_{31}=6\), with all other entries zero. Let \(B_{ij}^{11}=C_{ij}\), \(B_{ij}^{21}=-C_{ij}\), \(B_{ij}^{12}=B_{ij}^{22}=0\). Every pair still has zero aggregate interaction. The eigenvalues of \(C\) are \(6\) and \(-3\pm3\sqrt3\,\mathrm i\). With \((a,b)=(1,3)\), \(\delta=1/2\), so the slow eigenvalues limit to \(1\) and \(-7/2\pm(3\sqrt3/2)\mathrm i\): instability. With \((a,b)=(3,1)\), \(\delta=-1/2\), so they limit to \(-5\) and \(-1/2\mp(3\sqrt3/2)\mathrm i\): asymptotic stability. This is an orientation-of-turnover effect, not a variation in the size of the interaction network.

**Exact finite-rate certification.** At \(L=50\), all \(\mu_{i\alpha}<0\). The characteristic polynomial for \((a,b)=(1,3)\) includes the real-mode factor \(z^2+196z-212\), which has one positive root. For \((a,b)=(3,1)\), the entire characteristic polynomial factors into \((z^2+196z+988)(z^4+410z^3+42264z^2+38168z+270544)\). The quadratic is Hurwitz. For the quartic, its Routh--Hurwitz minors \(BC-AD=17290072\) and \(BCD-AD^2-B^2E=614449021696\) are strictly positive, and all five coefficients are positive (with \(A=1\)). Both conditions are necessary and sufficient for strict Hurwitz stability of this quartic. Hence the positive coexistence equilibrium is a hyperbolic saddle in the first case and a locally exponentially stable sink in the second, with no appeal to floating-point eigenvalues.

## Verification
Run `python check_stage_modes.py` with SymPy available. The checker assembles the exact six-dimensional matrices, verifies their polynomial factorizations and the displayed Routh--Hurwitz minors, and checks the directed three-cycle spectrum. The infinite-turnover statement follows from the explicitly reconstructed Schur projection, not from finite enumeration. The exact finite certificate concerns the specified three-species instance only.

## Relationship to prior work
Garmire and O'Dwyer, *Heterogeneity among and competition between life stages together extend the stability boundary of complex ecological communities* (2026), derive a large-turnover stability boundary using the common fast rate \(\phi_i=\gamma_i=\Delta\), with interaction covariance \(\rho\). Their transformed Jacobian and average-interaction formula already exhibit complete cancellation at the extreme correlation \(\rho=-1/3\). The present result instead varies the **leading ratio** of the two fast demographic rates, allows a deterministic directed interaction tensor with exact zero pairwise averages, identifies its rate-weighted slow spectrum, and proves a sharp minimal three-species stability reversal. The general structured-community-matrix treatment of Giménez-Romero et al. (2025) and the stage-structured mechanism of de Roos (2021) motivate the model, but do not supply the stated turnover-orientation classification. The standard fact of fast--slow spectral compression is not itself claimed as new.

## Limitations
The assertion applies to the indicated stage-exchange gLV equations and local stability at a prescribed feasible equilibrium. The fixed-\(S\) asymptotic cannot be interchanged with growing \(S\) without further estimates. At the limiting spectral boundary equality, no stability verdict is asserted. The signed directed interaction example mixes facilitation and competition and should not be interpreted as pure competition. Global persistence, stochastic robustness, unidirectional maturation and the nonlinear behavior at nonhyperbolic thresholds are not established.

## References
1. G. Garmire and J. P. O'Dwyer, *Heterogeneity among and competition between life stages together extend the stability boundary of complex ecological communities*, arXiv:2610.23557, first posted 2026-10-16. https://arxiv.org/abs/2610.23557
2. À. Giménez-Romero, C. Hernández, M. Genovart and R. Salguero-Gómez, *Population Structure Plays a Key Role in Community Stability*, Ecology Letters 28, e70272 (2025), first published 2025-12-08. https://doi.org/10.1111/ele.70272
3. A. M. de Roos, *Dynamic population stage structure due to juvenile-adult asymmetry stabilizes complex ecological communities*, PNAS 118, e2023709118 (2021). https://doi.org/10.1073/pnas.2023709118
