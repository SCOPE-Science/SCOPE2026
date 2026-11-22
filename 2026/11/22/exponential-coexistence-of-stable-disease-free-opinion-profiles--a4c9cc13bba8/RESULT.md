# Exponential coexistence of stable disease-free opinion profiles on epidemic–opinion stars

## Finding
In the higher-order SIS–opinion model described below, a star with \(m\ge1\) leaves admits, for every opinion-edge weight \(w\ge m+3\), **exactly**
\[
N_m=\begin{cases}2^m,&m\text{ even},\\2^m-\binom m{(m-1)/2},&m\text{ odd},\end{cases}
\]
distinct disease-free equilibria. Each has nonzero opinion in every community and is locally exponentially attracting for the **full** epidemic–opinion system. Nonetheless the infection fractions converge exponentially to zero from every admissible initial condition. The exact sign-sector inequalities below also classify every non-switching disease-free equilibrium at any \(w>0\). In particular, the three-leaf star at \(w=2\) has exactly five locally exponentially attracting disease-free equilibria. These statements are deterministic, with no claim of convergence of every opinion trajectory.

## Assumptions and scope
Fix an integer \(m\ge1\), let \(n=m+1\), and label the center \(0\) and leaves \(1,\ldots,m\). Let \(A\) be the adjacency matrix of the undirected unweighted star \(K_{1,m}\); let \(L_A\) be its combinatorial Laplacian, and let the unsigned opinion adjacency matrix be \(wA\) with \(w>0\). At each target vertex \(i\), set the quadratic exposure matrix \(B_i\) to have \((B_i)_{ii}=1\) and all other entries zero, so \(\mathcal A_2(x)_i=x_i^2\). These repeated-source quadratic terms are permitted in the originating model.

Choose strictly positive epidemic parameters
\[
\gamma^{\min}=1,\qquad \gamma_i=1+\frac1{8m},\qquad
\beta_{i1}=\beta_{i2}=\frac1{4m},\qquad
\beta_1^{\min}=\beta_2^{\min}=\frac1{8m}
\]
for every vertex. Define \(q_i=o_i+1/2\), \(d_i(o)=1+q_i/(8m)\), and \(b_i(o)=1/(4m)-q_i/(8m)\). The state \((x,o)\) ranges over \([0,1]^n\times[-1/2,1/2]^n\) and satisfies
\[
\dot x_i=-d_i(o)x_i+(1-x_i)b_i(o)\left(\sum_j A_{ij}x_j+x_i^2\right),
\qquad
\dot o=x-o-\tfrac12\mathbf1-\Phi(o)wL_A\Phi(o)o,
\]
where \(\Phi(o)_{ii}=1\) for \(o_i\ge0\) and \(-1\) for \(o_i<0\). The assertions about local smoothness and linear stability concern equilibria with \(o_i\ne0\), avoiding the sign-switching surfaces. Equilibria on those surfaces at isolated threshold weights are not counted by the generic sign-sector classification; for \(w\ge m+3\) none exists.

## Proof
**1. Epidemic extinction despite positive higher-order transmission.** For \(0\le x_i,q_i\le1\), \(d_i(o)\ge1\) and \(0<b_i(o)\le1/(4m)\); also \(x_i^2\le x_i\). Componentwise,
\[
\dot x\le\left[-I+\frac{A+I}{4m}\right]x.
\]
The matrix in brackets is Metzler and has spectral abscissa \(-1+(\sqrt m+1)/(4m)<0\), since the star adjacency eigenvalues are \(\sqrt m,-\sqrt m,0,\ldots,0\). Positive-system comparison therefore yields exponential decay of all infections from every admissible initial state. This is also a special case of the source's eradication criterion \(\rho(\Gamma_{\min}^{-1}(\beta_1 A+\beta_2 C))<1\), here with \(C=I\).

**2. One algebraic candidate per sign pattern.** At \(x=0\) the opinion equation becomes \(\dot o=-o-\mathbf1/2-\Phi(o)wL_A\Phi(o)o\). Fix a vector \(\sigma\in\{-1,+1\}^n\), and restrict attention to the open orthant with \(\operatorname{sgn}(o_i)=\sigma_i\). Writing \(z_i=\sigma_i o_i=|o_i|\), the equilibrium equation is
\[
(I+wL_A)z=-\tfrac12\sigma.
\]
Since \(I+wL_A\) is positive definite, the candidate is unique. It is a genuine regular equilibrium **if and only if** every coordinate of its solution \(z\) is strictly positive. (The inverse is nonnegative with row sums one, so the resulting coordinates also lie within the physical opinion interval.) On its sign sector the transformed dynamics is linear with Jacobian \(-(I+wL_A)\).

**3. Exact star formulas and sign tests.** Write \(s=\sigma_0\in\{-1,+1\}\), and let \(P\in\{0,\ldots,m\}\) be the number of positive-sign leaves. Every such leaf has common candidate magnitude \(z_+\), and every negative-sign leaf has common magnitude \(z_-\). Elementary elimination of the leaf equations gives
\[
D=1+(m+1)w,\quad z_0=-\frac{(1+w)s+w(2P-m)}{2D},\quad
z_+=\frac{wz_0-1/2}{1+w},\quad z_-=\frac{wz_0+1/2}{1+w}.
\]
For a negative center (\(s=-1\)), \(P=0\) is always feasible and gives \(o=-\mathbf1/2\). For \(P\ge1\), feasibility is exactly
\[
w^2(m+1-2P)-mw-1>0.
\]
For a positive center (\(s=+1\)), \(P=0\) is feasible exactly when \(w(m-1)>1\). For \(P\ge1\), feasibility is exactly
\[
w^2(m-2P-1)-(m+2)w-1>0.
\]
Indeed, each stated positive inequality implies \(z_0>0\) and, when positive leaves occur, \(z_+>0\); then \(z_->0\) automatically. Conversely those inequalities follow from the required positive magnitudes. For each permitted \(P\), there are precisely \(\binom mP\) different labeled leaf-sign choices.

**4. The exact large-weight census.** At \(w\ge m+3\), the negative-center feasible choices are exactly \(0\le P\le\lfloor m/2\rfloor\). Positive-center choices are exactly \(0\le P\le\lfloor(m-2)/2\rfloor\) (the interval is empty for \(m=1\)). For the permitted cases the smallest positive quadratic coefficient is one; at \(w=m+3\), even the stronger inequality \(w^2-(m+2)w-1>0\) holds. Disallowed cases have nonpositive quadratic coefficient and are impossible for every positive \(w\). All sign boundaries occur below \(m+3\), so there are no switching-surface equilibria at or above this bound. Summing the binomial choices and using symmetry of binomial coefficients yields
\[
\sum_{P=0}^{\lfloor m/2\rfloor}\binom mP
+\sum_{P=0}^{\lfloor(m-2)/2\rfloor}\binom mP=N_m.
\]
Because every regular sign sector has only one candidate, this also proves no other regular disease-free equilibria exist; the preceding boundary observation makes the count exact for all disease-free equilibria in the stated high-weight regime.

**5. Full-system local exponential attraction.** At every regular disease-free equilibrium the Jacobian, with epidemic coordinates preceding opinion coordinates, is lower block triangular: its epidemic block is \(-\operatorname{diag}(d_i(o^*))+\operatorname{diag}(b_i(o^*))A\), its upper-right block is zero, and its opinion block is \(-I-\Phi(o^*)wL_A\Phi(o^*)\). The epidemic block is Metzler with diagonal entries at most \(-1\) and off-diagonal row sums at most \(m/(4m)=1/4\); it is Hurwitz by strict row diagonal dominance. The opinion block is symmetric negative definite because \(\Phi L_A\Phi\) is positive semidefinite. Hence all full-system eigenvalues have strictly negative real parts. Each sign is fixed in a neighborhood of the equilibrium; local exponential attraction follows from the standard smooth linearization theorem, relative to the admissible state domain.

**6. A small exact witness.** For \(m=3,w=2\), the classification permits \((s=-1,P=0)\), \((s=-1,P=1)\) in three labeled ways, and \((s=+1,P=0)\), for exactly five equilibria. In center/leaf order the distinct patterns are: \((-1/2,-1/2,-1/2,-1/2)\); \((1/6,-5/18,-5/18,-5/18)\); and three permutations of \((-5/18,1/54,-19/54,-19/54)\) over the leaf coordinates. All are locally exponentially attracting, while all infections decay globally.

## Verification
The standalone `CHECK.py` reconstructs every signed-orthant equilibrium directly from the exact model; verifies zero vector-field residuals in rational arithmetic; checks the necessary-and-sufficient sign criteria; enumerates all \(2^{m+1}\) sign patterns for \(1\le m\le10\) at \(w=m+3\); and verifies the five-state \(m=3,w=2\) witness. It prints `PASS` with no third-party libraries. This finite check is supplementary: the proofs of the arbitrary-\(m\) count, linear stability, and global infection decay are analytic, not extrapolated from enumeration.

## Relationship to prior work
Samadi, Caiza, Gracy and Paré (2026), *A Networked SIS Epidemic–Opinion Model with Higher-Order Interactions*, supplies the governing equations, a global epidemic-eradication criterion, local stability of the maximally skeptical healthy equilibrium and a synchronous endemic-bistability analysis. The paper explicitly leaves opinion convergence and possible multiple healthy opinion equilibria unresolved (Section III-B) and does not count the stable disease-free belief states on stars. The gauge transformation itself is classical in signed-consensus theory (Altafini 2013; Meng, Meng and Hong 2017), while Zhai and Zheng (2018) examine different state-dependent susceptibility laws with fixed signed adjacency, not this opinion-sign-selected forcing. The new content is the **complete admissible sign census on epidemic–opinion stars, the exponential count and their simultaneous full-system attraction even under global infection eradication**. Related published findings on two-community endemic symmetry breaking and resolvent-consistent platform-opinion equilibria concern different domains and do not imply this census. The comparison is literature-bounded; independently established historical priority is not claimed.

## Limitations
Only local attraction of the enumerated states is proved. The paper does not establish global convergence of opinion trajectories, solution uniqueness at switching surfaces, distribution of basins, stochastic resilience, or behavior under arbitrary graph topology. The epidemic parameters form a specific open-subcritical family; perturbations preserving strict Jacobian inequalities and sign consistency retain the individual local attractors, but the exact large-weight count need not persist outside the stated star construction. Novelty claims remain subject to independent scholarly examination.

## References
1. S. Samadi, J. I. Caiza, S. Gracy and P. E. Paré, *A Networked SIS Epidemic–Opinion Model with Higher-Order Interactions*, arXiv:2608.31032v1 (first public posting 2026-08-31), https://arxiv.org/abs/2608.31032 . Main text Sections II–VI and revised v2 text (2026-09-04) consulted.
2. C. Altafini, *Consensus Problems on Networks With Antagonistic Interactions*, IEEE Transactions on Automatic Control **58** (2013), 935–946, DOI:10.1109/TAC.2012.2224251.
3. D. Meng, Z. Meng and Y. Hong, *A State Transition Matrix-Based Approach to Separation of Cooperations and Antagonisms in Opinion Dynamics*, arXiv:1705.04430 (2017), https://arxiv.org/abs/1705.04430 .
4. S. Zhai and W. X. Zheng, *Generalized Dynamics in Social Networks With Antagonistic Interactions*, arXiv:1801.08713 (2018), https://arxiv.org/abs/1801.08713 .
