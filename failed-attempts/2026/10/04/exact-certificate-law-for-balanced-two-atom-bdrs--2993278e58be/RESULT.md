# Exact certificate law for balanced two-atom BDRS
## Finding
Consider balanced two-atom optimal transport with
\[
r=c=(1/2,1/2),\qquad
C=\begin{pmatrix}0&\Delta\\ \Delta&0\end{pmatrix},\qquad \Delta>0,
\]
and let \(\eta>0\) be the initial temperature parameter. For the Chin--Schiffer certificate, write
\[
p=k+1
\]
for BDRS and
\[
p=\lambda k+1
\]
for O-BDRS with \(\lambda\in[1,2)\). Their effective temperature is then \(\varepsilon=\eta/p\).

From the stated all-ones initialization, symmetry is preserved by every row scaling, column scaling, momentum extrapolation, and overrelaxation. Hence the incoming column scaling at any certificate step is a scalar multiple of the all-ones vector. Put
\[
z=e^{-p\Delta/\eta}.
\]
Then the intermediate plan used by the certificate is exactly
\[
Z(p)=\frac{1}{2(1+z)}
\begin{pmatrix}1&z\\ z&1\end{pmatrix}.
\]
This plan already has row and column marginals \((1/2,1/2)\), so the feasibility-repair term of the certificate is identically zero.

The unregularized optimum is the diagonal coupling and has cost zero. The exact primal upper bound, dual lower bound, and certified gap are
\[
U(p)=\frac{\Delta z}{1+z},
\]
\[
L(p)=-\frac{\eta}{p}\log(1+z),
\]
and
\[
G(p)=U(p)-L(p)
=\frac{\Delta e^{-p\Delta/\eta}}{1+e^{-p\Delta/\eta}}
+\frac{\eta}{p}\log\!\left(1+e^{-p\Delta/\eta}\right).
\]
The function \(G\) is strictly decreasing on \((0,\infty)\). Moreover,
\[
G(p)-U(p)=\frac{\eta}{p}\log(1+z),
\]
and
\[
\frac{G(p)}{U(p)}-1
=\frac{\eta}{p\Delta}\frac{(1+z)\log(1+z)}{z}
=\frac{\eta}{p\Delta}+o(p^{-1}).
\]
Thus the certificate is asymptotically sharp on this benchmark.

For a tolerance \(0<\tau<G(1)\), let \(p_\tau>1\) be the unique solution of \(G(p_\tau)=\tau\). The first certified iteration is exactly
\[
N_1(\tau)=\left\lceil p_\tau-1\right\rceil
\]
for BDRS and
\[
N_\lambda(\tau)=\left\lceil\frac{p_\tau-1}{\lambda}\right\rceil
\]
for O-BDRS. Therefore
\[
\frac{N_\lambda(\tau)}{N_1(\tau)}\longrightarrow\frac1\lambda
\qquad\text{as }\tau\downarrow0.
\]

## Assumptions and scope
The claim uses the certificate equations and effective temperatures stated for BDRS and O-BDRS in arXiv:2609.33814v1. Marginals are strictly positive and normalized. The cost matrix is the natural balanced two-site metric with one nonzero cost scale \(\Delta\). The O-BDRS relaxation parameter lies in the paper's range \(\lambda\in[1,2)\).

The conclusion is a calibration theorem for this benchmark. It is not a claim that arbitrary transport instances have zero repair error, that their certificate gap depends only on effective temperature, or that O-BDRS has no acceleration mechanism beyond cooling on other instances.

## Proof
At certificate iteration \(k\), equation (14) of the source gives effective temperature \(\varepsilon=\eta/p\), with \(p=k+1\) for BDRS and \(p=\lambda k+1\) for O-BDRS. The Gibbs kernel is
\[
K_\varepsilon=
\begin{pmatrix}1&z\\ z&1\end{pmatrix},
\qquad z=e^{-\Delta/\varepsilon}=e^{-p\Delta/\eta}.
\]

The algorithm starts with all scaling vectors equal to the all-ones vector. Because both marginals and the kernel are invariant under interchange of the two sites, induction through the row update, column update, momentum extrapolation, and O-BDRS relaxation shows that every scaling vector remains a scalar multiple of the all-ones vector. Write the incoming column scaling in equation (15) as \(t=q\mathbf 1\) with \(q>0\).

Equation (15) gives
\[
A=\frac{1}{2q(1+z)}\mathbf 1.
\]
A second scaling then gives
\[
B=q\mathbf 1=t.
\]
Therefore equation (16) yields
\[
Z=\operatorname{diag}(A)K_\varepsilon\operatorname{diag}(t)
=\frac{1}{2(1+z)}
\begin{pmatrix}1&z\\ z&1\end{pmatrix}.
\]
Its two row sums and two column sums are all \(1/2\), so in equation (19) the marginal defect is \(\delta=0\). No rounding or repair cost is needed.

The cost of \(Z\) is the total off-diagonal mass times \(\Delta\):
\[
U=\langle C,Z\rangle=\frac{\Delta z}{1+z}.
\]
The diagonal coupling is feasible for the unregularized problem and has zero cost, while all costs are nonnegative, so the exact unregularized optimum is \(p^\star=0\).

For the lower bound, equation (18) gives
\[
f=\varepsilon\log A,
\qquad
g=\varepsilon\log(B\oslash c).
\]
Both are constant across their two coordinates. Since each marginal has total mass one,
\[
L=\varepsilon\log\!\left(\frac{1}{2q(1+z)}\right)
+\varepsilon\log(2q)
=-\varepsilon\log(1+z).
\]
Substituting \(\varepsilon=\eta/p\) proves the displayed formula for \(G=U-L\).

For monotonicity, put \(a=\Delta/\eta>0\), so \(z=e^{-ap}\). Differentiating gives
\[
G'(p)
=-\frac{a\Delta z}{(1+z)^2}
-\frac{\eta}{p^2}\log(1+z)
-\frac{\eta a z}{p(1+z)}<0.
\]
Thus \(G\) is strictly decreasing. Since \(z\to0\), the expansion \(\log(1+z)=z+O(z^2)\) gives
\[
\frac{G(p)-U(p)}{U(p)}
=\frac{\eta}{p\Delta}\frac{(1+z)\log(1+z)}{z}
=\frac{\eta}{p\Delta}+o(p^{-1}),
\]
which proves asymptotic sharpness.

Finally, strict monotonicity makes \(G(p)\le\tau\) equivalent to \(p\ge p_\tau\). Substituting the two affine schedules for \(p\) gives the exact ceiling formulas for \(N_1\) and \(N_\lambda\). Because \(p_\tau\to\infty\) as \(\tau\downarrow0\), the ceiling terms are negligible relative to \(p_\tau\), proving the ratio limit \(1/\lambda\).

## Verification
The accompanying `verify.py` independently reconstructs the scalar certificate equations from equation (15), verifies both marginals of \(Z\), compares the direct certificate with the closed form for several parameter choices, checks strict decrease on fine deterministic grids, and numerically verifies the exact stopping-index ceiling formulas. The symbolic proof above establishes the infinite statements; the finite computation is supplementary.

The proof also checks all boundary conditions used by the claim: \(\Delta>0\), \(\eta>0\), \(p>0\), \(\lambda\in[1,2)\), and \(0<\tau<G(1)\). No numerical approximation is used to infer monotonicity or the asymptotic limit.

## Relationship to prior work
Chin and Schiffer identify BDRS with an annealed Sinkhorn mechanism, introduce O-BDRS, and state effective temperatures \(\eta/(k+1)\) and \(\eta/(\lambda k+1)\). Their Proposition 3 supplies the general primal-dual certificate. Their experiments further report that much of O-BDRS's common-\(\eta\) advantage is explained by reaching lower effective temperatures sooner, and that O-BDRS at roughly \(k/\lambda\) iterations tracks later BDRS objective values. The inspected paper does not state the balanced two-atom closed form above, the exact vanishing of the repair term on every certificate step, the exact certificate slack, or the resulting exact stopping-count formulas.

Chizat's annealed-Sinkhorn analysis supplies the standard entropic scaling representation and studies regularization paths and annealing errors. Thibault--Chizat--Dossal--Papadakis study overrelaxation for fixed-temperature Sinkhorn and establish convergence and local acceleration regimes. Xie--Wang--Wang--Zha introduce IPOT for exact Wasserstein distance, while Ma--Xiao--Zhao introduce BDRS and discuss its transport specialization. These works motivate the objects but do not contain the 2026 certificate being calibrated here.

Targeted semantic searches for balanced two-point BDRS certificates, binary uniform-marginal certificate formulas, and exact O-BDRS tolerance stopping laws returned no statement matching the formula. The closest retrieved transport records concerned conditioning of quadratically regularized OT rather than this entropy-based certificate. Search absence is not treated as a proof of originality; the claim is supported by direct statement-level comparison with the primary full text and the closest older methods.

## Limitations
The theorem concerns a highly symmetric two-atom benchmark. Its value is diagnostic: it isolates certificate conservatism from marginal-repair error and gives an exact unit-test law for the new stopping certificate. It does not predict behavior for unequal marginals, nonsymmetric costs, larger supports, or instances where the intermediate plan is infeasible and the repair term is active.

The balanced two-atom entropic plan itself is elementary and may appear implicitly in older matrix-scaling literature. The claimed contribution is the exact specialization of the new 2026 BDRS/O-BDRS certificate, including its slack and stopping-index consequence. An older or unindexed source could contain an equivalent benchmark calculation under different terminology; no such statement was found in the inspected sources or searches.

## References
1. S. J. K. Chin and M. Schiffer, *Annealed Sinkhorn with Momentum: Certified Unregularized Optimal Transport in Linear Memory*, arXiv:2609.33814v1, 2026. See Proposition 2, equations (14)--(22), Algorithm 1, and Section 4.
2. L. Chizat, *Annealed Sinkhorn for Optimal Transport: convergence, regularization path and debiasing*, arXiv:2408.11620v1, 2024.
3. A. Thibault, L. Chizat, C. Dossal, and N. Papadakis, *Overrelaxed Sinkhorn--Knopp Algorithm for Regularized Optimal Transport*, Algorithms 14(5):143, 2021, DOI:10.3390/a14050143.
4. Y. Xie, X. Wang, R. Wang, and H. Zha, *A Fast Proximal Point Method for Computing Exact Wasserstein Distance*, PMLR 115:433--453, 2020.
5. S. Ma, L. Xiao, and R. Zhao, *Bregman Douglas-Rachford Splitting Method*, arXiv:2509.08739v1, 2025.
