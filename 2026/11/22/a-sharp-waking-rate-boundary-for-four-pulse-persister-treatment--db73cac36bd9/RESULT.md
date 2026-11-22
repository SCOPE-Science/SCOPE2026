# A sharp waking-rate boundary for four-pulse persister treatment schedules

## Finding
Consider two bacterial phenotypes, susceptible/active and tolerant/persister, in the linear, density-independent, drug-on/drug-off model
\[
\dot x=A_zx\quad\text{(on)},\qquad \dot x=Bx\quad\text{(off)},
\]
where
\[
A_z=\begin{pmatrix}-a-d&z\\a&-z\end{pmatrix},\qquad
B=\begin{pmatrix}g-a&b\\a&-b\end{pmatrix},
\quad a,b,d,g,z>0.
\]
Here \(a\) is active-to-persister switching, \(b\) is off-treatment waking, \(z\) is on-treatment waking, \(d\) is active-cell killing during treatment, and \(g\) is active-cell growth without treatment. Both phenotypes have zero intrinsic reproduction in the persister state; no direct persister killing is assumed. Let \(u,v>0\) be on- and off-segment lengths, \(X=e^{uA_z}\), \(Y=e^{vB}\). Two periodically repeated, equally budgeted four-segment schedules have monodromies \(G=X^2Y^2\) (grouped) and \(T=(XY)^2\) (alternating). Their order within a period is immaterial up to cyclic rotation for the Floquet multiplier.

Let \(\lambda>0\) be the Perron eigenvalue of \(B\):
\[
\lambda=\frac{g-a-b+\sqrt{(g-a-b)^2+4gb}}2,
\qquad
\boxed{z_*=b+\left(1+\frac dg\right)\lambda}.
\]
**Theorem (sharp all-duration order phase).** For every \(a,b,d,g,u,v,z>0\),
\[
\begin{array}{c|c}
0<z<z_*&\rho(T)<\rho(G)\\
z=z_*&\rho(T)=\rho(G)\\
z>z_*&\rho(G)<\rho(T).
\end{array}
\]
The comparison is strict away from the unique threshold and **independent of both positive segment lengths**. Moreover \(b<z_*<b+d+g\), so in particular drug-on suppression of waking (\(z\le b\)) always favors alternation in asymptotic growth, while sufficiently strong drug-on waking enhancement reverses that preference.

At \(z=z_*\), a stronger invariance holds: for **every finite ordering and every positive duration** of the two phases, the monodromy has Perron multiplier
\[
\boxed{\rho=\exp\!\left[\frac\lambda g\bigl(gT_{\rm off}-dT_{\rm on}\bigr)\right]},
\]
where \(T_{\rm on}\) and \(T_{\rm off}\) are their total durations, irrespective of the number or order of switches. Thus equal total growth and killing budgets, \(gT_{\rm off}=dT_{\rm on}\), produce neutral Perron growth at the crossover in this idealized linear model. Four segments are the minimum number needed for a spectral order distinction with the same counts of on and off segments. For any \(z\ne z_*\), an equal additional scalar loss \(\kappa>0\) in both phenotypes and both phases can, with suitable positive \(u,v\), make the grouped schedule grow while alternation decays when \(z<z_*\), and reverse these fates when \(z>z_*\).

For the normalized benchmark \(a=b=d=g=1\), \(\lambda=(\sqrt5-1)/2\), and the exact crossing is \(z_*=\sqrt5\). This is an illustration of the general threshold, not a fitted biological rate.

## Assumptions and scope
All five basic rates and both segment lengths are strictly positive, and both phases have a common active-to-persister switching rate \(a\). The drug-on waking rate \(z\) is allowed to exceed the off rate \(b\); this is a mathematical possibility, not a claim that a particular antibiotic increases waking. Drug effects on awakening may depend on substrate or adjunct treatments. The two types remain linear, well mixed, and uncoupled from density limits, resistance evolution, mutation, spatial biofilms and pharmacokinetics. Asymptotic growth means the spectral radius of the periodically repeated finite-period linear propagator, not the population size after one arbitrary initial condition or clinical eradication. At \(z=z_*\), the all-order assertion applies to each finite product of strictly positive on/off propagators; no optimality claim is made for unequal budgets or arbitrary continuously graded drug concentrations. Adding a common scalar loss \(-\kappa I\) is only a comparative stability illustration and does not change ordering.

## Proof
**1. Positivity and spectral comparison.** Each generator is irreducible Metzler: its off-diagonal entries are positive. For positive times, \(X,Y\) are strictly positive, invertible matrices with positive determinants. Both \(G\) and \(T\) are strictly positive with the same positive determinant, \(\exp[2u\operatorname{tr}A_z+2v\operatorname{tr}B]\). Any strictly positive \(2\times2\) matrix of positive determinant has two distinct positive real eigenvalues, and at fixed determinant its larger eigenvalue strictly increases with the trace. Thus the sign of \(\rho(G)-\rho(T)\) equals that of \(\operatorname{tr}G-\operatorname{tr}T\).

**2. Exact trace gap.** For arbitrary \(2\times2\) matrices \(X,Y\), the commutator \(C=XY-YX\) has trace zero, so \(\operatorname{tr}C^2=-2\det C\). Cyclicity of trace gives \(\operatorname{tr}C^2=2\operatorname{tr}(XYXY)-2\operatorname{tr}(X^2Y^2)\), hence
\[
\operatorname{tr}G-\operatorname{tr}T=\det(XY-YX).
\tag{1}
\]
Because each of \(A_z,B\) has two distinct real eigenvalues \(\xi_+>\xi_-\), its exponential at time \(t>0\) is \(c(t)I+s(t)M\), with \(s(t)=(e^{t\xi_+}-e^{t\xi_-})/(\xi_+-\xi_-)>0\). Therefore \([X,Y]=s_A(u)s_B(v)[A_z,B]\) and
\[
\operatorname{sgn}(\rho(G)-\rho(T))=\operatorname{sgn}\det[A_z,B].
\tag{2}
\]
Direct exact multiplication gives
\[
\det[A_z,B]=aQ(z),\quad
Q(z)=-gz^2+Kz+C,
\]
\[
K=b(g-d)+(g-a)(d+g),\qquad
C=b\bigl[d(b+a+d+g)+ag\bigr]>0.
\tag{3}
\]
Since \(g>0\), \(Q\) has exactly one positive and one negative real zero (its leading coefficient and constant have opposite signs). Consequently its sign on \(z>0\) is positive before its single positive root, and negative after.

**3. Identification of the root and complete all-order resonance.** The determinant of \(B\) is \(-gb<0\), so \(B\) has one positive eigenvalue \(\lambda\) and one negative eigenvalue. Since its positive right Perron vector can be normalized to \(w=(r,1)^{\mathsf T}\), the equations \(Bw=\lambda w\) give \(r=(\lambda+b)/a>0\) and, on summing both coordinates, \(\lambda(r+1)=gr\). In particular \(0<\lambda<g\) and \(r/(r+1)=\lambda/g\). Now
\[
(A_z-B)w=\binom{-(d+g)r+(z-b)}{b-z}.
\]
This is collinear with \(w\) exactly when \((z-b)(r+1)=(d+g)r\), or \(z=z_*\) as displayed. At that value, \(A_{z_*}w=-d(\lambda/g)w\), while \(Bw=\lambda w\). Their commutator annihilates \(w\), so \(Q(z_*)=0\); uniqueness from (3) identifies \(z_*\) as the unique positive zero. The bounds \(b<z_*<b+d+g\) follow from \(0<\lambda/g<1\). Equations (2)–(3) prove the strict three-phase comparison.

For any concatenation of on/off phases of lengths \(t_j>0\), every factor maps the same strictly positive vector \(w\) into itself multiplied by \(e^{-d\lambda t_j/g}\) for on and \(e^{\lambda t_j}\) for off. Therefore the product maps \(w\) to \(\exp[(\lambda/g)(gT_{\rm off}-dT_{\rm on})]w\). A strictly positive eigenvector of a strictly positive matrix belongs to its Perron eigenvalue, proving the exact order-independence expression, even when the two generators do not commute.

**4. Minimality and opposing extinction classifications.** Two words of lengths at most three with the same counts of symbols \(X,Y\) are cyclic rotations of each other, and cyclic rotations of products of invertible matrices are similar. Thus four is the smallest possible length where spectral ordering can matter. At four it does matter for every \(z\ne z_*\) by the strict inequalities already proved. Fix any \(u>0\) and let \(v\to\infty\). From the strictly positive Perron projection \(P\) of \(B\), \(Y=e^{\lambda v}(P+o(1))\); thus \(\log\rho(G)/(2(u+v))\to\lambda>0\), and similarly \(\log\rho(T)/(2(u+v))\to\lambda>0\). For sufficiently large \(v\), both logarithmic growth rates are positive but strictly ordered. Replacing both generators by \(M-\kappa I\) multiplies every four-segment monodromy by \(e^{-2\kappa(u+v)}\). Taking \(\kappa>0\) strictly between the two growth rates makes one Perron multiplier above one and the other below one, in the phase-law directions. This proves existence of genuine opposite Floquet stability classifications, not merely different numeric growth rates.

## Verification
Run `python verify.py` alongside this document with SymPy and mpmath installed. It checks the exact commutator polynomial and trace identity, the exact common Perron eigenvector in the normalized \(z_*=\sqrt5\) case, the formula for the threshold for a range of rational parameter choices, high-precision four-segment matrix exponentials, and two explicitly separated stability examples after common mortality. Exact algebra and the proof above—not finite samples or floating-point agreement—establish the universal statement. Two benchmark examples are \(a=b=d=g=1\): \(z=1,u=v=1,\kappa=1/20\) yields grouped growth but alternating decline; \(z=3,u=1/2,v=2,\kappa=37/100\) gives the opposite.

## Relationship to prior work
Singh, Orman, Conrad and Nikolaou (2023) use a two-state normal/persister system and a two-phase monodromy to analyze duration ratios and bacterial decline. Their accessible main article, including model equations, results and discussion, does not formulate or prove a complete **equal-budget rearrangement** criterion for grouped versus alternating four-phase schedules, an on-waking phase boundary, or a common-eigenvector all-order resonance. The modeling mechanism (phenotype switching, antibiotic pulses and spectral growth) is prior work, not a novelty claim. Carvalho et al. (2017) explicitly allow antibiotic- and substrate-dependent switching rates; their accessible full text does not give the stated exact universal order comparison.

The \(2\times2\) trace/commutator identities and reversal invariance are classical, and Greene (2014) specifically studies the traces of \(ABAB\) and \(A^2B^2\). Equations (1)–(2) are **not** claimed as new. The specific positive persister kinetics make the sign a one-root polynomial in the waking rate, with an exact biologically interpretable threshold and a whole-family all-schedule invariance at the root. An earlier two-stage population result on rank-one recruitment plus diagonal survival identifies an order crossover and common Perron ray in a different *discrete projection family* and compares perfect alternation with the infinite-block limit; it does not give the finite four-segment treatment-kinetics formula and its all-duration sharp boundary. Another six-season stage-treatment result concerns alternating **different diagonal culling interventions** before a shared positive projection matrix; its determinant-sign law does not imply the present on/off rate-dependent continuous-time claim. General matrix identities may facilitate deriving this result, and historical mathematical priority remains a live risk.

## Limitations
The rate threshold is mathematical, not an experimentally calibrated or clinically recommended dosing rate. Specifically, treatment-enhanced waking \(z>z_*\) may require a resuscitation-promoting adjunct and is not claimed for ordinary antibiotics. The exact results require one common active-to-persister switching rate in both conditions, constant phase parameters, two phenotypes, no saturation, and an ideal switch. Stochastic bacterial extinction is not equivalent to the deterministic Floquet criterion; pharmacokinetics, resistance, biofilm gradients, antibiotic residuals and tolerance heterogeneity are omitted. At \(z=z_*\), equality concerns asymptotic multiplier and the common positive mode, not identical finite-time populations from arbitrary initial vectors. Historical priority is not certified, and independent external review has not occurred.

## References
1. Singh, G., Orman, M. A., Conrad, J. C., and Nikolaou, M. (2023). *Systematic design of pulse dosing to eradicate persister bacteria*. PLOS Computational Biology 19(1):e1010243. First public article 2023-01-17. https://doi.org/10.1371/journal.pcbi.1010243 ; full text https://pmc.ncbi.nlm.nih.gov/articles/PMC9882918/
2. Carvalho, G., Guilhen, C., Balestrino, D., Forestier, C., and Mathias, J.-D. (2017). *Relating switching rates between normal and persister cells to substrate and antibiotic concentrations*. Microbial Biotechnology 10:1616–1627. https://doi.org/10.1111/1751-7915.12739
3. Greene, J. (2014). *Traces of Matrix Products*. Electronic Journal of Linear Algebra 27:716–734. https://doi.org/10.13001/1081-3810.1999 ; full text https://www.d.umn.edu/~jgreene/papers/Traces_Products_EJLA.pdf
4. Published mathematical comparison: *A unique survival threshold reverses the advantage of environmental persistence in a two-stage population* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-unique-survival-threshold-reverses-the-advantage-of-environmen--21d96ab3451f
5. Published mathematical comparison: *A determinant-sign phase law for balanced six-season stage-specific population interventions* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-a-determinant-sign-phase-law-for-balanced-six-season-stage-speci--e0435dfadf65
