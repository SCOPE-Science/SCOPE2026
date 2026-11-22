# A topology-controlled activity-noise optimum in the complete three-particle tandem exclusion sectors

## Finding

For the tandem exclusion process on a periodic ring of \(n\) sites with exactly three indistinguishable hard-core particles, the local moves are \(110\to101\) at rate \(\alpha>0\) and \(101\to011\) at rate \(\beta>0\), all words interpreted cyclically. Set \(q=\beta/\alpha>0\), and let \(Q_t\) count **every successful clockwise hop**, without counting rejected attempts. For each \(n\in\{4,5,6,7,8\}\), the full three-particle configuration space is irreducible, and

\[
J_n(q)=\lim_{t\to\infty}\frac{\mathbb E Q_t}{\alpha t},\qquad
F_n(q)=\lim_{t\to\infty}\frac{\operatorname{Var}(Q_t)}{\mathbb E Q_t}
\]

exist and have the following exact values (these count *all* jumps on the ring, not just one bond):

\[
\begin{aligned}
J_4&=q+1,&F_4&=1,\\
J_5&=\frac{3q+1}{q+1},&F_5&=\frac{11q^3+7q^2+5q+1}{(q+1)^2(3q+1)},\\
J_6&=\frac{9q(q+1)}{3q^2+6q+1},&F_6&=\frac{3(9q^4+18q^3+12q^2+2q+1)}{(3q^2+6q+1)^2},\\
J_7&=\frac{q(3q+5)}{q^2+3q+1},&F_7&=\frac{9q^6+54q^5+128q^4+146q^3+80q^2+38q+13}{(q+1)(3q+5)(q^2+3q+1)^2},\\
J_8&=\frac{q(3q+7)}{q^2+4q+2},&F_8&=\frac{9q^6+78q^5+245q^4+378q^3+294q^2+210q+86}{(q+1)(3q+7)(q^2+4q+2)^2}.
\end{aligned}
\]

Each mean \(J_n(q)\) strictly increases with \(q\). Yet the activity noise has a sharp ring-size-dependent classification: \(F_4\) is exactly Poissonian; \(F_5>1\) is strictly increasing; and for each \(n\in\{6,7,8\}\), \(F_n>1\) has **exactly one** global minimum on \(q>0\). Those unique minima lie respectively within the rational intervals

\[
\begin{aligned}
q_6&\in(0.376,0.377),\\
q_7&\in(0.576,0.578),\\
q_8&\in(0.878,0.880).
\end{aligned}
\]

Consequently, six sites are the first in this *complete, fully active, three-particle family* where increasing the follower-to-leader rate first suppresses and later amplifies relative integrated-activity noise, while increasing the mean hop rate throughout. This is a finite-ring theorem, not a thermodynamic-limit claim.

## Assumptions and scope

Take \(n\in\{4,5,6,7,8\}\) and three particles on labeled sites \(\mathbb Z/n\mathbb Z\), with no entry, exit, exchange against the drive, or independent background hopping. For an allowed particle hop from site \(i\) to \(i+1\), its total rate is \(\alpha\eta_{i-1}+\beta\eta_{i+2}\), provided \(\eta_i=1\), \(\eta_{i+1}=0\). If both local patterns enable the same hop, their independent channels add. All rates are strictly positive, and \(Q_t\) counts one per actual successful move. The reference stationary law is the unique invariant law on the full three-particle sector. Its existence and uniqueness also follow directly from the finite irreducible generator. For \(n\ge9\), three particles can be arranged with no occupied sites within distance two; such frozen states make the full sector nonirreducible, so this full-sector classification stops naturally at \(n=8\). The rate \(\alpha\) sets the time scale and does not change the Fano ratios.

For a single fixed bond, the long-time mean count per unit time is \(\alpha J_n/n\), and its long-time Fano ratio equals \(F_n/n\). Thus the strict super-Poisson statement here refers specifically to the **total successful-hop count**.

## Proof

**1. Exact finite generator and full active range.** Let \(\Omega_n=\{\eta\in\{0,1\}^n:\sum_i\eta_i=3\}\). At time scale \(\alpha^{-1}\), the tilted backward generator acting on functions is

\[
(\mathcal L_z f)(\eta)=\sum_{i\in\mathbb Z/n\mathbb Z}
\eta_i(1-\eta_{i+1})(\eta_{i-1}+q\eta_{i+2})
\left[e^z f(\eta^{i,i+1})-f(\eta)\right].
\]

There are \(\binom n3\) configurations: respectively \(4,10,20,35,56\). All configurations admit transitions when \(n<9\), and the exact directed graph enumeration in `verify.py` checks strong connectivity of each full graph (both forward and reversed reachability from a state), with all edges independent of the positive value of \(q\). Since frozen configurations exist when \(3\times3\le n\), this is precisely the complete no-frozen range with three particles and at least one vacancy. In particular, the stationary Perron eigenvalue at \(z=0\) is simple and its analytic continuation generates the long-time cumulants.

**2. Rotation quotient and a finite exact certificate.** The tilted generator commutes with ring rotation. The positive principal eigenvalue and stationary eigenvectors are invariant under rotation, so their first two derivatives are found from rotation-orbit classes alone, of respective sizes \(1,2,4,5,7\) for \(n=4,5,6,7,8\). Enumerate all binary configurations with three occupied sites, choose the lexicographically least cyclic rotation of each as its orbit representative, and sum the transition rates to each destination orbit. This constructs a symbolic matrix \(L\) and its marked-jump derivative matrix \(B\); the matrix \(B\) includes marked jumps that stay within a rotation orbit, even when their quotient entry is diagonal. Let \(p\) be the unique vector satisfying \(Lp=0\) and \(\mathbf1^Tp=1\). With \(j=\mathbf1^TBp\), solve the unique mean-zero Poisson equation

\[
-Lv=Bp-jp,\qquad \mathbf1^Tv=0.
\]

Exact differentiation of the tilted eigenvalue yields

\[
J_n=j,\qquad
\lim_{t\to\infty}\frac{\operatorname{Var}(Q_t)}{\alpha t}
=j+2\mathbf1^TBv,\qquad
F_n=1+\frac{2\mathbf1^TBv}{j}.
\]

The complete symbolic quotient construction and rational linear solves in `verify.py` give all five displayed rational functions. It also reconstructs the full labeled generators at the independent exact rates \(q=1/2\) and \(q=2\), verifies the stationary Gibbs weights \(p(\eta)\propto q^{\sum_i\eta_i\eta_{i+1}}\), and solves the **full-space** Poisson equations for both cumulants. These are exact rational checks, not floating-point fits. For finite \(n\), the combinatorial enumeration and rational-polynomial identities are exhaustive.

**3. Strict super-Poisson property.** By direct exact subtraction,

\[
\begin{aligned}
F_5-1&=\frac{8q^3}{(q+1)^2(3q+1)},\\
F_6-1&=\frac{2(9q^4+9q^3-3q^2-3q+1)}{(3q^2+6q+1)^2},\\
F_7-1&=\frac{2(3q^6+14q^5+21q^4+5q^3-13q^2+4)}{(q+1)(3q+5)(q^2+3q+1)^2},\\
F_8-1&=\frac{2(3q^6+22q^5+49q^4+37q^3-9q^2+29q+29)}{(q+1)(3q+7)(q^2+4q+2)^2}.
\end{aligned}
\]

All denominators are strictly positive. For \(n=7\), the only potentially nonpositive group is \(21q^4-13q^2+4\), a positive quadratic in \(q^2\) because its discriminant is \(-167\); for \(n=8\), use the positive quadratic \(49q^4-9q^2+29\). For \(n=6\), the quartic \(P(q)=9q^4+9q^3-3q^2-3q+1\) has a Sturm chain whose signs at \(q=0\) are \((+,-,-,+,+)\), and at positive infinity are \((+,+,+,-,+)\); each sequence has two sign variations. Hence it has no positive zero; as \(P(0)=1\), it stays strictly positive for \(q>0\). This proves every strict noise inequality.

**4. Unique optimum and critical ring length.** Differentiating the exact functions gives strictly positive denominators and numerators, up to positive numerical factors, as follows:

\[
\begin{aligned}
D_5(q)&=q^2(7q+3),\\
D_6(q)&=27q^4+36q^3+18q^2-5,\\
D_7(q)&=36q^8+282q^7+955q^6+1829q^5+2020q^4+945q^3-333q^2-522q-152,\\
D_8(q)&=36q^8+444q^7+2123q^6+5332q^5+7238q^4+3020q^3-4571q^2-5704q-1798.
\end{aligned}
\]

The polynomial \(D_5\) is positive for \(q>0\). Each of \(D_6,D_7,D_8\) has exactly one sign change in its nonzero coefficient list from constant to leading term; Descartes' rule gives at most one positive root. Each is negative at zero and tends to positive infinity, so it has exactly one positive root, and the derivative changes from negative to positive there. Exact substitution at the rational endpoints above brackets each unique root and proves the claims without relying on numerical root finding. Direct differentiation of the five \(J_n\) expressions gives positive rational derivatives for all \(q>0\), proving strict mean monotonicity.

## Verification

Run `python verify.py` after installing the dependency in `requirements.txt`. The checker constructs each local-move graph from scratch and verifies strong connectivity; reconstructs exact symbolic lumped generators and both cumulants; checks analytic derivative numerator identities, Sturm variations and rational critical-point brackets; then independently solves full labeled stationary Poisson problems at two exact recovery ratios for each ring. Its last line is `All exact symbolic, full-state and sign certificates PASS`. The calculation uses exact integer and rational algebra. The finite computer enumeration proves only the explicitly finite cases \(n=4,5,6,7,8\); neither simulation nor asymptotic extrapolation is used to claim a theorem beyond them.

## Relationship to prior work

Nguyen Ngoc, Nhung and Thi introduce the tandem process, establish its active-sector Gibbs stationary distribution, and derive stationary *mean* current and spatial correlations. Those formulas and the model definition are prior results and are not claimed here. The new statement is a complete finite-size classification of the **time-integrated activity variance-to-mean ratio** and its unique finite-rate minima in the nonfrozen full three-particle range.

The tilted-generator method itself is classical, including the activity-cumulant treatment of symmetric exclusion by Appert-Rolland, Derrida, Lecomte and van Wijland. Published finite-graph Poisson-activity classification results apply to reversible symmetric exclusion, not the directed tandem kinetic constraint. Published two-particle tandem results concern its alternating-cycle spectrum, and the recent strong-recovery tandem intermittency result concerns instantaneous stationary jump intensity, explicitly not long-time integrated count variance. Those respective statements do not imply the rational formulas or their global derivative classification above.

## Limitations

This result neither describes rings with nine or more sites in their nonfrozen active classes nor addresses particle counts other than three. For those larger rings, the presence of frozen configurations prohibits a theorem about a unique stationary distribution on the **entire** three-particle sector. These formulas concern asymptotic cumulant rates, not finite-time Poisson distributions: \(F_4=1\) also happens to arise from a constant-rate counting process, but equality of Fano ratios in other models need not imply exact Poisson laws. The theorem does not claim universal super-Poisson noise in arbitrary cooperative exclusion processes or any thermodynamic scaling. An unindexed equivalent finite-state calculation or broader theorem could supersede the originality claim.

## References

1. N. P. Nguyen Ngoc, L. T. Nhung and H. A. Thi, *Tandem Exclusion Process*, arXiv:2606.01568v1, first publicly posted 2026-06-01 UTC, https://arxiv.org/abs/2606.01568 .
2. C. Appert-Rolland, B. Derrida, V. Lecomte and F. van Wijland, *Universal cumulants of the current in diffusive systems on a ring*, arXiv:0804.2590 (2008), https://arxiv.org/abs/0804.2590 .
3. *Exact parity-selected exceptional points in two-particle tandem exclusion*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-parity-selected-exceptional-points-in-two-particle-tandem--d964f86bf714 .
4. *Critical finite-ring intermittency in the tandem exclusion process*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-critical-finite-ring-intermittency-in-the-tandem-exclusion-proce--28e127e9bdda .
5. *Poisson activity on finite exclusion networks: a complete graph classification*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-poisson-activity-on-finite-exclusion-networks-a-complete-graph-c--016805168b38 .
