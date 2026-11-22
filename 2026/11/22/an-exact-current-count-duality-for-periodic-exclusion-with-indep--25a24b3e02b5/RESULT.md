# An exact current-count duality for periodic exclusion with independent dynamic obstacles

## Finding

For every periodic ring of \(L\ge2\) sites, every fixed particle number \(0\le M\le L\), and every pair of strictly positive obstacle binding and unbinding rates, the independent-defect totally asymmetric exclusion model has an **exact pathwise duality** between the \(M\)-particle and \((L-M)\)-particle sectors. The duality preserves the full successful-hop counting process, not just its stationary average.

In particular, if \(J_L(M)\) is the unique stationary mean particle current per bond, then
\[
J_L(M)=J_L(L-M)\qquad (0\le M\le L).
\]
The total hop-count distributions, all their finite-time moments and cumulants, and all corresponding scaled cumulant-generating functions agree at complementary particle numbers under the mapped initial laws. This proves at every finite ring size the current-density symmetry proposed numerically by Szavits-Nossan and Waclaw, while adding a fluctuation-level prediction.

## Assumptions and scope

Index sites by \(\mathbb Z/L\mathbb Z\). Let \(\eta_i\in\{0,1\}\) indicate a hard-core particle, and \(\sigma_i\in\{0,1\}\) indicate an obstacle. Obstacle births \(0\to1\) occur at rate \(k_+>0\), and deaths \(1\to0\) at rate \(k_->0\), independently at every site and irrespective of any particle occupancy. A particle at site \(i\) jumps clockwise to \(i+1\), only if \(\eta_i=1\) and \(\eta_{i+1}=0\), at rate \(g(\sigma_{i+\delta})\), where \(\delta=0\) means the obstacle at the departure site and \(\delta=1\) the obstacle at the arrival site. Assume \(g(0)=p>0\), \(g(1)=p_d\ge0\), with rates spatially homogeneous. Full blocking \(p_d=0\) and partial hindrance \(p_d>0\) are included. All indices below are modulo \(L\).

Define the map \(\Theta_\delta\) by
\[
 (\Theta_\delta\eta)_j=1-\eta_{-j},\qquad
 (\Theta_\delta\sigma)_j=\sigma_{2\delta-1-j}.
\]
Let \(N_i(t)\) count successful particle crossings of the oriented bond \(i\to i+1\), and \(N(t)=\sum_i N_i(t)\). The assertion is equality in law for the entire càdlàg marked path \(\{N_i(t)\}_{i,t\ge0}\) and its mapped complementary process, with \(N_i(t)\) paired to \(N_{-i-1}(t)\). In particular \(N(t)\) is preserved **pathwise** in a coupling for all \(t\ge0\), provided initial conditions are paired by \(\Theta_\delta\). The unique stationary laws also correspond.

## Proof

**Step 1: the involution and sectors.** Applying \(\Theta_\delta\) twice fixes every particle and obstacle bit, because \(-(-j)=j\) and \((2\delta-1)-(2\delta-1-j)=j\). Thus it is an involutive bijection; the particle-number sector \(M\) is mapped onto \(L-M\).

**Step 2: clockwise jumps remain clockwise with unchanged rates.** Consider a legal hop \(i\to i+1\), so \((\eta_i,\eta_{i+1})=(1,0)\). Set \(j=-i-1\). Then for the transformed particle configuration,
\[
 ((\Theta_\delta\eta)_j,(\Theta_\delta\eta)_{j+1})
 =(1-\eta_{i+1},1-\eta_i)=(1,0).
\]
The transformed hop \(j\to j+1\) is therefore legal. It ends at \(\Theta_\delta\) of the old post-jump configuration. Moreover its rate is **exactly** the original rate since
\[
 (\Theta_\delta\sigma)_{j+\delta}
 =\sigma_{2\delta-1-(-i-1+\delta)}
 =\sigma_{i+\delta}.
\]
Hence the labelled original jump at bond \(i\) is paired bijectively, with unchanged rate, to the labelled transformed jump at bond \(-i-1\).

**Step 3: obstacle transitions.** An obstacle flip at site \(i\) maps to the same type of flip at \(j=2\delta-1-i\). The bit before the flip is unchanged by relabelling, so the transformed flip has exactly the same binding or unbinding rate. Independence of these rates from \(\eta\) is essential here.

**Step 4: generator and path identity.** Every allowed transition of the full finite-state continuous-time Markov chain is paired with one transition of the dual chain, preserving its rate and identifying each particle-hop bond. The maps are inverse because \(\Theta_\delta^2=\mathrm{id}\). The marked generators are therefore conjugate. Starting from mapped initial conditions, construct both chains with matching exponential clocks across the paired events. Their states remain related by \(\Theta_\delta\) and their cumulative hop counts satisfy \(N_i(t)=N'_{-i-1}(t)\) simultaneously for every time \(t\), almost surely.

**Step 5: stationary consequence.** Because \(k_+,k_->0\), every obstacle pattern communicates with the all-clear pattern. Since \(p>0\), with all obstacles temporarily cleared clockwise exclusion hops connect all configurations in each nontrivial particle-number sector. Thus the finite chain is irreducible (at \(M=0,L\) only the obstacle chain remains), and the stationary distribution is unique. Conjugacy maps stationary measures into each other. Taking the mean number of successful hops per unit time and dividing by \(L\) yields \(J_L(M)=J_L(L-M)\). Equality of the full marked counting laws follows already from Step 4; no hypothesis about independent particles or a product-form stationary measure has been used.

## Verification

A standalone pure-Python checker `check_duality.py` exhaustively compares every labelled transition and its exactly transformed counterpart, with rational arithmetic, for each \(L=2,3,4,5,6,7\), both placements \(\delta=0,1\), and three nontrivial parameter sets including complete blocking, partial blocking and no hindrance. Replay with `python check_duality.py`. It reports **87,360** involution/sector assertions, **131,040** generator-row comparisons and **1,055,832** labelled event-rate comparisons. These finite checks corroborate the all-size algebraic proof; they do not substitute for it.

## Relationship to prior work

Waclaw, Cholewa-Waclaw and Greulich (2018 preprint; 2019 journal) introduced sitewise dynamic obstacles and reported a nearly symmetric current-density relation when obstacle binding is independent of particle occupancy, while showing asymmetry under constrained obstacle binding. Szavits-Nossan and Waclaw (2020), in their model with source-site full blocking, obtained numerical evidence of an apparently exact symmetry \(J(\rho)=J(1-\rho)\). Their conclusion explicitly describes its origin as unclear, and their Appendix C **assumes**, rather than establishes, the symmetry.

The present result supplies the missing reflection-plus-complement state-space isomorphism, for both source- and arrival-site gating, and upgrades the mean-current symmetry to all finite-time jump-counting statistics. The mechanism differs from an unshifted particle-hole swap: the obstacle field must also be reflected about the appropriate half-integer center. Other exclusion models with different blocking or feedback rules need not have this symmetry.

## Limitations

The duality uses periodic boundaries, homogeneous site rates and obstacle clocks unaffected by particles. It is not asserted for open systems with entry and exit, site-heterogeneous clocks, or models where obstacles cannot bind to occupied particle sites. It proves symmetry, not a closed-form nonparabolic current-density curve or an explicit invariant measure. The statement concerns the full joint process and exactly coupled starting conditions; independently selected nondual initial conditions need not give identical finite-time counts. Prior work explicitly posed the symmetry question, but broader implicit symmetry theory could contain equivalent formulations; publication-priority assessment is not independent.

## References

1. B. Waclaw, J. Cholewa-Waclaw and P. Greulich, *Totally asymmetric exclusion process with site-wise dynamic disorder*, arXiv:1809.05441 (first posted 2018-09-14); journal version J. Phys. A **52**, 065002 (2019). https://arxiv.org/abs/1809.05441 ; lawful author manuscript https://www.pure.ed.ac.uk/ws/portalfiles/portal/82236921/TASEP_annealed_disorder_accepted.pdf (Sec. 2, Sec. 3.1, Sec. 3.3, Conclusions).
2. J. Szavits-Nossan and B. Waclaw, *Current-density relation in the exclusion process with dynamic obstacles*, arXiv:2006.14474 (first posted 2020-06-25); Phys. Rev. E **102**, 042117 (2020). https://arxiv.org/abs/2006.14474 ; lawful author manuscript https://www.pure.ed.ac.uk/ws/portalfiles/portal/166991367/ET12056.pdf (Sec. II, Sec. VII, Conclusions, Appendix C).
