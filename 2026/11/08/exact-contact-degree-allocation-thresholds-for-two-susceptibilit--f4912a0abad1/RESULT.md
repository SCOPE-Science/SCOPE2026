# Exact contact-degree allocation thresholds for two susceptibility classes in a configuration-model SIR epidemic

## Finding

Consider equal-sized high- and low-susceptibility classes in an uncorrelated configuration-model contact network. Every high-class vertex has integer degree \(d_H\geq1\), every low-class vertex has integer degree \(d_L\geq1\), and the fixed mean degree is an integer \(K\geq2\), so \(d_H+d_L=2K\). Transmission across each directed infectious contact succeeds independently with probability \(\beta\psi_j\) depending only on the recipient class \(j\), where \(0<\psi_L<\psi_H\) and \(0<\beta\psi_H\leq1\). Put \(\rho=\psi_H/\psi_L>1\).

**Theorem (complete discrete allocation phase diagram).** The early-outbreak reproduction number is
\[
\mathcal R(d_H,d_L)=\frac{\beta}{2K}\left(\psi_Hd_H(d_H-1)+\psi_Ld_L(d_L-1)\right).
\]
Every minimizing allocation has \(d_H\leq d_L\). Writing \(d_H=K-r\), \(d_L=K+r\), with \(r\in\{0,\ldots,K-1\}\), define the strictly increasing critical ratios
\[
\rho_j=\frac{K+j}{K-j-1},\qquad j=0,\ldots,K-2.
\]
For \(1<\rho<\rho_0\), the homogeneous assignment \(r=0\) uniquely minimizes \(\mathcal R\). At \(\rho=\rho_j\), precisely \(r=j\) and \(r=j+1\) minimize \(\mathcal R\). Between successive ratios \(\rho_{j-1}<\rho<\rho_j\), precisely \(r=j\) minimizes. For \(\rho>\rho_{K-2}=2K-2\), precisely \(r=K-1\) minimizes. Equivalently, all minimizing \(r\)'s are the nearest admissible integers to
\[
r_c=\frac{(2K-1)(\rho-1)}{2(\rho+1)}.
\]

In particular, degree reassignment strictly lowers the homogeneous reproduction number **if and only if** \(\rho>K/(K-1)\). For \(\rho>2K-2\), every high-susceptibility vertex optimally has degree one, and the minimized reproduction number is independent of the high susceptibility:
\[
\mathcal R_{\min}=\beta\psi_L\frac{(2K-1)(2K-2)}{2K}.
\]
The same value is attained by degree-one high-susceptibility vertices at \(\rho=2K-2\), where one neighboring allocation ties. The maximum epidemic transmission-scale threshold within this class-regular design family is \(\beta_c=2K/[\psi_Hd_H^*(d_H^*-1)+\psi_Ld_L^*(d_L^*-1)]\), where the asterisks denote any minimizing allocation. The optimally designed early-invasion branching process is strictly subcritical exactly when \(\beta<\beta_c\), critical at equality, and supercritical above it.

A concrete example is \(K=3\), \(\beta=\psi_H=1\), and \(\psi_L=1/20\). The homogeneous assignment \((d_H,d_L)=(3,3)\) gives \(\mathcal R=21/20>1\), whereas the optimal degree-preserving assignment \((1,5)\) gives \(\mathcal R=1/6<1\). Thus the same mean degree can lie on opposite sides of the branching threshold merely by assigning its contacts differently between the two susceptibility classes.

## Assumptions and scope

The result concerns the asymptotic early-invasion threshold of a locally tree-like configuration-model sequence with equal class frequencies, deterministic class-specific degrees, uniform random stub pairing, and independent susceptible-recipient-specific per-edge infection trials. Integers \(d_H,d_L\) are at least one, and total degree is fixed at \(2K\). Take sequence sizes with feasible even stub totals. The reproduction number is the Perron root of the multitype forward-infection branching matrix. The result does **not** optimize arbitrary networks, assortative mixing, class proportions, or intervention costs, and does not equate a finite-network epidemic outcome to its infinite-network branching approximation.

## Proof

**Branching calculation.** In a uniform random pairing, a randomly encountered neighbor belongs to class \(j\) with size-biased probability \(d_j/(d_H+d_L)=d_j/(2K)\). When a newly infected class-\(i\) vertex was reached along one edge, it has \(d_i-1\) unused edges. Therefore the next-generation matrix, with rows indexed by infectious source type and columns by newly infected recipient type, is
\[
M_{ij}=(d_i-1)\frac{d_j}{2K}\beta\psi_j.
\]
It is a nonnegative rank-one matrix, an outer product of the vectors \(((d_i-1))\) and \(((d_j\beta\psi_j/(2K)))\). Its eigenvalues are zero and its trace, the latter equaling the displayed \(\mathcal R\). All quantifiers above include the case \(d_H=1\), when its entire offspring row vanishes.

**Ordering of the degrees.** The function \(f(d)=d(d-1)\) is nondecreasing for integers \(d\geq1\), and strictly increases between distinct positive integer degrees. If \(d_H>d_L\), exchanging the degrees changes the numerator by
\[
(\psi_H-\psi_L)\bigl(f(d_L)-f(d_H)\bigr)<0.
\]
Thus an optimum must have \(d_H\leq d_L\). Parity then forces \(d_H=K-r\), \(d_L=K+r\) for a unique \(r\in\{0,\ldots,K-1\}\).

**All integer transitions.** Divide the objective by \(\beta\psi_L/(2K)>0\) and set
\[
F_K(r)=\rho(K-r)(K-r-1)+(K+r)(K+r-1).
\]
A direct expansion yields
\[
F_K(r)=(1+\rho)r^2-(\rho-1)(2K-1)r+(1+\rho)K(K-1),
\]
so the unique real minimizer is \(r_c\) as given. More importantly, the exact discrete increment is
\[
F_K(r+1)-F_K(r)=2\bigl((K+r)-\rho(K-r-1)\bigr),\qquad0\leq r\leq K-2.
\]
Each increment has sign equal to the sign of \(\rho_r-\rho\), and the critical ratios are strictly increasing because
\[
\rho_{r+1}-\rho_r=\frac{2K-1}{(K-r-2)(K-r-1)}>0\qquad(0\leq r\leq K-3).
\]
The successive increments themselves strictly increase with \(r\), so no nonadjacent allocations can tie for the minimum. This proves the complete staircase and the isolated adjacent ties, including the endpoints \(K=2\) and \(r=K-1\). It also gives the nearest-integer characterization.

**Sharp qualitative boundaries.** Since \(\rho_0=K/(K-1)\), strict improvement over the homogeneous assignment occurs exactly when the first increment is negative. Since \(\rho_{K-2}=2K-2\), beyond that ratio all increments are negative and the optimum is \(r=K-1\), hence \(d_H=1\), \(d_L=2K-1\). Substitution cancels the high-susceptibility term because \(1(1-1)=0\), giving the stated susceptibility-independent plateau. At the last equality, both last allocations minimize. The example follows by substitution, with no numerical approximation.

## Verification

The accompanying standalone `VERIFY.py` recomputes the integer allocation objective using exact rational arithmetic and exhaustively compares every admissible allocation for each \(2\leq K\leq43\) against all predicted phase labels at, above, and below transition ratios. It also checks the rank-one matrix identity and the exact epidemic-threshold example. It reports `PASS: 87475 exact assertions`. These finite computational checks corroborate but do **not** replace the all-parameter algebraic proof.

## Relationship to prior work

Britton, Deijfen, and Liljeros (2011) establish the weighted configuration-model epidemic and multitype reproduction-number framework. Smilkov, Hidalgo, and Kocarev (2014) establish that susceptibility-degree correlation matters in SIS dynamics. Yang, Tang, and Gross (2015) study adaptive two-susceptibility SIS networks. Baxter and Timár (2021, Section 4.2, Equation 46) give the destination-degree-dependent SIR threshold \(\langle k(k-1)T_k\rangle/\langle k\rangle=1\), which directly specializes to the reproduction factor above. **The reproduction formula and the qualitative protective role of negative correlation are prior work, not claimed as new.** The present proposed contribution is the necessary-and-sufficient *integer design* phase diagram under an equal-two-class fixed-degree budget, including all exact adjacent ties, the sharp condition for any improvement over homogeneous degrees, and the degree-one susceptibility-independent plateau. In the primary materials inspected, these exact budget-constrained conclusions were not stated. Priority remains provisional because absence from inspected sources is not proof of worldwide novelty.

## Limitations

The classification is specific to uncorrelated configuration networks with equal numbers of vertices of each susceptibility, class-regular degrees, strictly positive integer contacts, and independent recipient-dependent Reed–Frost transmissions. Changing the class proportions, adding assortative mixing, allowing within-class degree heterogeneity, imposing a lower degree bound above one, or using SIS recurrence changes the optimization. This result concerns invasion thresholds, not epidemic size conditional on spread or the cost and feasibility of redesigning actual contact networks. A zero or negative deterministic epidemic growth rate at a finite population size is not asserted. Historical-priority review is incomplete; independent mathematical audit is not performed.

## References

1. Britton, T., Deijfen, M., and Liljeros, F. (2011). *A weighted configuration model and inhomogeneous epidemics*. https://arxiv.org/abs/1104.5585 (first public 2011-04-29).
2. Smilkov, D., Hidalgo, C. A., and Kocarev, L. (2014). *Beyond network structure: How heterogeneous susceptibility modulates the spread of epidemics*. https://arxiv.org/abs/1403.2708 (first public 2014-03-10).
3. Yang, H., Tang, M., and Gross, T. (2015). *Large epidemic thresholds emerge in heterogeneous networks of heterogeneous nodes*. https://doi.org/10.1038/srep13122 (published 2015-08-21).
4. Baxter, G. J., and Timár, G. (2021). *Degree dependent transmission rates in epidemic processes*. https://arxiv.org/abs/2102.11602 (Section 4.2, Eq. 46; published after the archival source but relevant to the implication comparison).
