# Exact all-rate commuter optimization and a two-threshold outbreak window

## Finding

In the two-patch SIR commuting model of Rapaport and Mimouni [1], assume two strictly positive patch populations, positive departure/return rates and recovery rate, and unequal intrinsic reproduction numbers \(0<\mathcal R_1<\mathcal R_2\). The exact basic reproduction number \(\mathcal R(x,y)\), with \(x\) and \(y\) the numbers eligible to commute from the lower- and higher-transmission patches, has the following properties **without any fast-movement or slow-recovery assumption**:

1. For every fixed \(x\in[0,N_1]\), \(\mathcal R(x,y)\) strictly decreases with \(y\in[0,N_2]\). Consequently, every global minimizer has \(y=N_2\).
2. For every fixed \(y>0\), the function \(x\mapsto\mathcal R(x,y)\) on \([0,N_1]\) is strictly decreasing, strictly increasing, or strictly decreasing and then strictly increasing with **exactly one** interior turning point. An interior turning point is always a nondegenerate strict minimum. In particular the global minimizer on the rectangle is unique, possibly on a boundary.
3. With the entirely rational parameters
   \[
   N_1=2,\quad N_2=1,\quad
   \lambda_1=\mu_1=\gamma=2,\quad
   \lambda_2=\mu_2=\tfrac12,\quad
   \beta_1=\tfrac32,\quad\beta_2=\tfrac{12}{5},
   \]
   the high-transmission patch's commuting participation is \(y=1\) and the exact **strictly subcritical** interval of the lower-transmission patch's participation is
   \[
   \boxed{\frac{7-\sqrt{33}}8<x<\frac{7+\sqrt{33}}8.}
   \]
   Thus both extremes \(x=0\) and \(x=2\) have \(\mathcal R(x,1)>1\), whereas precisely the indicated intermediate interval has \(\mathcal R(x,1)<1\). At the two endpoints of that interval \(\mathcal R(x,1)=1\). The result classifies linear invasion of the disease-free state, not epidemic final size at the neutral boundary.

## Assumptions and scope

Let \(N_1,N_2,\lambda_i,\mu_i,\gamma,\beta_i>0\), and put \(\mathcal R_i=\beta_i/\gamma\). Patch \(i\) has \(N_i\) persons attached to it; \(x=N_{1c}\in[0,N_1]\) and \(y=N_{2c}\in[0,N_2]\) are the numbers who can commute. For commuters from patch \(i\), departure from home occurs at rate \(\lambda_i\) and return at rate \(\mu_i\); the location composition is at its stationary demographic balance, as in [1]. The infection dynamics are the frequency-dependent two-patch SIR model of [1], with patch-dependent transmission and common recovery.

Define the stationary away-from-home shares and the two positive residence-time coefficients
\[
 e_i=\frac{\lambda_i}{\lambda_i+\mu_i},\qquad
 k_i=\frac{\lambda_i\mu_i}{(\lambda_i+\mu_i)(\gamma+\lambda_i+\mu_i)}.
\]
Also set
\[
 P_1=N_1-e_1x+e_2y,\quad
 P_2=N_2+e_1x-e_2y,\quad
 S=k_1x+k_2y,\quad u=S/P_1,\quad v=S/P_2.
\]
Both \(P_i\) are strictly positive throughout the closed parameter rectangle, and \(S>0\) away from \((0,0)\). The exact two-by-two next-generation reduction from [1, Proposition 1] is
\[
 Q=\begin{pmatrix}
 \mathcal R_1(1-u)&\mathcal R_2v\\
 \mathcal R_1u&\mathcal R_2(1-v)
 \end{pmatrix},\qquad \mathcal R(x,y)=\rho(Q).
\]
The entries \(Q_{12}\) and \(Q_{21}\) are strictly positive when \(S>0\), and the two column sums are \(\mathcal R_1\) and \(\mathcal R_2\). Therefore the Perron root \(L=\mathcal R(x,y)\) lies strictly between the two isolated-patch reproduction numbers when \(S>0\). At \((0,0)\) it equals \(\mathcal R_2\).

## Proof

**Reduction from the six demographic groups.** At demographic balance, the source model has \(N_{11}=\mu_1x/(\lambda_1+\mu_1)\), \(N_{12}=\lambda_1x/(\lambda_1+\mu_1)\), \(N_{22}=\mu_2y/(\lambda_2+\mu_2)\), and \(N_{21}=\lambda_2y/(\lambda_2+\mu_2)\). In [1, equation (3)], the cross-patch entries are
\[
 q_{21}=\mathcal R_1\left(\frac{N_{11}\lambda_1}{P_1(\gamma+\lambda_1+\mu_1)}+\frac{N_{21}\mu_2}{P_1(\gamma+\lambda_2+\mu_2)}\right),
\]
\[
 q_{12}=\mathcal R_2\left(\frac{N_{12}\mu_1}{P_2(\gamma+\lambda_1+\mu_1)}+\frac{N_{22}\lambda_2}{P_2(\gamma+\lambda_2+\mu_2)}\right).
\]
Both numerators contain **the same** \(S\), so \(q_{21}=\mathcal R_1u\) and \(q_{12}=\mathcal R_2v\). The column-sum identities in [1, Corollary 3] then give the stated \(Q\). This algebra is exact for every \(\gamma>0\); no approximation is taken.

**A Perron-root identity.** Since \(S>0\), the Perron root \(L\) is simple, and \(\mathcal R_1<L<\mathcal R_2\). Put \(a=L-\mathcal R_1>0\) and \(b=\mathcal R_2-L>0\). The characteristic polynomial is
\[
 F(L,x,y)=(L-\mathcal R_1)(L-\mathcal R_2)
 +\mathcal R_1u(L-\mathcal R_2)
 +\mathcal R_2v(L-\mathcal R_1).
\]
The equation \(F=0\) implies
\[
 \mathcal R_2av=b(a+\mathcal R_1u).\tag{1}
\]
Moreover \(F_L=L-L_- >0\), where \(L_-\) is the other eigenvalue. Implicit differentiation yields \(L_z=-F_z/F_L\) for \(z=x,y\).

**Strict benefit of increased high-transmission commuting.** At fixed \(x\), the derivatives are
\[
 v_y=\frac{k_2P_2+e_2S}{P_2^2}>0,\qquad
 u_y=\frac{k_2P_1-e_2S}{P_1^2}.
\]
Their exact Wronskian satisfies
\[
 u v_y-vu_y=uv e_2\left(\frac1{P_1}+\frac1{P_2}\right)>0.
\]
Using (1),
\[
 v F_y=b\big[a v_y+\mathcal R_1(u v_y-vu_y)\big]>0.
\]
Hence \(L_y<0\) wherever \(S>0\). At the single uncoupled corner, continuity and the strict Perron column-sum bound give the same strict decrease upon increasing \(y\). Thus the minimizer in \(y\) is always \(N_2\).

**One-valley structure in lower-transmission commuting.** At fixed \(y>0\),
\[
 u_x=\frac{k_1P_1+e_1S}{P_1^2}>0,\qquad
 v_x=\frac{k_1P_2-e_1S}{P_2^2}.
\]
If \(L_x=0\), then \(F_x=-\mathcal R_1b u_x+\mathcal R_2a v_x=0\), which forces \(v_x>0\). With \(L\) held fixed, the second derivatives at such a point satisfy
\[
 u_{xx}=\frac{2e_1u_x}{P_1}>0,\qquad
 v_{xx}=-\frac{2e_1v_x}{P_2}<0.
\]
Therefore
\[
 F_{xx}=-\mathcal R_1b u_{xx}+\mathcal R_2a v_{xx}<0,
 \qquad L_{xx}=-F_{xx}/F_L>0.
\]
Every stationary point is thus nondegenerate and strictly minimizing. Two stationary minima would require an intervening stationary point that is not a minimum; this is impossible. Consequently the profile has at most one stationary point, with the stated complete trichotomy. Taking \(y=N_2>0\) proves uniqueness of the full rectangle minimizer.

**Exact outbreak interval.** For the rational parameters in the finding, \(\mathcal R_1=3/4\), \(\mathcal R_2=6/5\), and \(y=1\). The reduced quantities become
\[
 P_1=\frac{5-x}{2},\qquad
 P_2=\frac{1+x}{2},\qquad
 S=\frac{1+2x}{12}.
\]
Direct substitution into the preceding characteristic polynomial gives
\[
 \det(I-Q)=F(1,x,1)
 =\frac{4x^2-7x+1}{40(x-5)(x+1)}.\tag{2}
\]
The smaller eigenvalue is strictly smaller than the first diagonal entry of \(Q\), hence is below \(\mathcal R_1=3/4<1\). Thus the sign of \(\det(I-Q)=(1-L)(1-L_-)\) is precisely the sign of \(1-L\). The denominator in (2) is negative for \(0\le x\le2\); the numerator has precisely the two roots \((7\pm\sqrt{33})/8\), both in \((0,2)\). It follows that \(L<1\) exactly between these roots, \(L=1\) at them, and \(L>1\) elsewhere on the physical interval. This proves all three assertions.

## Verification

Run `python3 verify.py` with Python's standard library. It compares the source's unreduced six-group formula against the reduced \(Q\) using 200 independent exact-rational parameter instances; verifies the three rational signs \(F(1,0,1)=-1/200\), \(F(1,3/4,1)=4/595\), and \(F(1,2,1)=-1/120\); checks the degree-two numerator identity at three points (sufficient because the cleared expression has degree at most two); and performs numerical monotonicity smoke tests. It prints `VERIFY_OK` on successful completion. The universal derivative conclusions are proved above analytically, not inferred from these finite tests.

## Relationship to prior work

Rapaport and Mimouni [1], which has verified primary MSC2020 code 92D30, establishes the exact reproduction-number matrix and investigates the minimization problem in its Section 4. Its Propositions 4 and 5 analyze the **fast-commuting approximation** obtained by setting the recovery rate to zero inside the residence-time fractions; Proposition 6 transfers a trichotomy to the exact model only when recovery is sufficiently small relative to commuting rates. The present result retains the **original positive recovery rate without any scale separation**, proves the full global one-valley optimization theorem, and supplies an exact non-asymptotic intervention interval where recovery is as large as the largest departure/return rates. The qualitative benefit of high-risk travelers commuting to the safer patch and the possibility of an interior optimum were already known from [1] and are not presented as newly discovered phenomena.

Citron et al. [2] compares Eulerian-flow and home-based-trip epidemic models and demonstrates the dependence of outcomes on travel-time representation. It does not optimize the resident/commuter partition of the distinct six-group model in [1] for all positive recovery rates. Search and record comparisons found no published source that implies the exact all-rate theorem and the rational interval in this model; absence from an index alone is not a proof of global priority.

## Limitations

This concerns the exact linear invasion threshold of the given stationary-demography two-patch SIR model. It does not describe transient populations before commuting balance, stochastic extinction, total outbreak size, the neutral case \(\mathcal R=1\), arbitrary multi-patch networks, or globally optimal movement when the departure and return rates themselves are control variables. The example allows all residents of the high-transmission patch to be eligible commuters; they still spend a strictly positive fraction of time at home. Independent external validation and an exhaustive check of unindexed equivalent literature have not been performed.

## References

[1] A. Rapaport and I. Mimouni, *The Role of Permanently Resident Populations in the Two-Patches SIR Model with Commuters*, arXiv:2211.16137, first made public 2022-11-29; *Bulletin of Mathematical Biology* **85** (2023), article 3. https://arxiv.org/abs/2211.16137 ; https://doi.org/10.1007/s11538-022-01111-6 . Source equations (1)--(3), Corollary 3, Propositions 4--6, and Section 5.

[2] D. T. Citron et al., *Comparing metapopulation dynamics of infectious diseases under different models of human movement*, *PNAS* **118** (2021), e2007488118. https://doi.org/10.1073/pnas.2007488118 ; accessible full text https://pmc.ncbi.nlm.nih.gov/articles/PMC8106338/ . Sections on SIR dynamics and travel-time constraints.
