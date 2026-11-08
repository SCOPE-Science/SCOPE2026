# Exact minimal single-defect rectification in a boundary-driven exclusion chain

## Finding

A four-site symmetric exclusion chain with one variable interior residence time already exhibits *rigorously nonzero quadratic rectification at every nontrivial defect strength*. At mean reservoir density one half, the sign is controlled **only by whether the defect is slower or faster than the background**, without further parameter restrictions. Four sites are minimal for this phenomenon among chains with identical clean boundary sites and a single interior defect.

Write the boundary reservoir densities as \(\rho_L=(1+\delta)/2\) and \(\rho_R=(1-\delta)/2\), with \(|\delta|<1\). Let \(a>0\) be the second site's mean residence-time parameter, and let the other three residence times equal one. In the time normalization specified below, the stationary current admits the analytic expansion
\[
J_a(\delta)=c_1(a)\delta+c_2(a)\delta^2+O_a(\delta^3),
\qquad
c_2(a)=-\frac{2a(a-1)P(a)}{(a+1)Q(a)^2}.
\]
The polynomials are
\[
P(a)=15612625a^8+155893675a^7+411771380a^6+510425170a^5+351379457a^4+142316303a^3+33739658a^2+4331572a+232560,
\]
\[
Q(a)=27685a^5+108535a^4+149179a^3+90837a^2+24584a+2380.
\]
Every coefficient in \(P\) and \(Q\) is positive. Consequently \(c_2(a)=0\) precisely at \(a=1\); it is strictly negative for \(a>1\) and strictly positive for \(0<a<1\). Therefore reversing an arbitrarily small nonzero reservoir density gradient changes the magnitude of the stationary current when \(a\ne1\). By contrast, every chain with at most three sites, identical clean boundary sites and at most one interior defect has exactly antisymmetric stationary current under gradient reversal.

## Assumptions and scope

The configuration space is \(\{0,1\}^4\), with occupation variables \(\eta_i\) and no multiple occupancy. The site residence times are \((\tau_1,\tau_2,\tau_3,\tau_4)=(1,a,1,1)\). A particle at site \(i\) attempts to jump to an empty nearest-neighbor site at rate \(\tau_i^{-1}\). At the left boundary, empty site one receives a particle at rate \(\rho_L\) and occupied site one loses a particle at rate \(1-\rho_L\); at the right boundary the analogous rates are \(\rho_R\) and \(1-\rho_R\). All rates are continuous-time rates; this is a global factor-two time normalization of the setting in Sakai–Akimoto, with equal reservoir and clean-boundary residence times. The current \(J_a\) is the mean net left-reservoir entry rate (equal to each bulk bond's stationary current). Positive current means flow from left to right. The theorem concerns finite chains, strictly positive finite residence times, mean reservoir density exactly one half and the local quadratic coefficient, not large-system scaling or nonperturbative rectification sign for arbitrary gradients.

## Proof

Index configurations by integers \(s\in\{0,\ldots,15\}\), whose binary digits are the site occupations in order. Let \(A(\delta)\) be the column-convention generator, so its off-diagonal entry \(A_{t,s}\) is the transition rate from state \(s\) to \(t\). By the stated rates, \(A(\delta)=A_0+\delta A_1\), with every column sum zero. For \(a>0\), this finite chain is irreducible when \(|\delta|<1\), hence its stationary probability \(p(\delta)\) is uniquely defined and analytic near zero.

At zero gradient, detailed balance gives the exactly normalized product law
\[
p_0(s)=\frac{a^{\eta_2(s)}}{8(1+a)}.
\]
Writing \(p(\delta)=p_0+\delta p_1+\delta^2p_2+O_a(\delta^3)\), the two normalized Poisson equations are
\[
A_0p_1=-A_1p_0,\quad A_0p_2=-A_1p_1,\quad
\mathbf1^Tp_1=\mathbf1^Tp_2=0.
\]
They have unique solutions because \(A_0\) has a one-dimensional stationary nullspace. The left-reservoir current is the injection rate minus occupation,
\[
J_a(\delta)=\rho_L-\sum_{s:\eta_1(s)=1}p_s(\delta),
\]
so \(c_2(a)=-\sum_{s:\eta_1(s)=1}p_{2,s}\). The finite exact elimination above yields
\[
-\sum_{s:\eta_1(s)=1}p_{2,s}
=-\frac{2a(a-1)P(a)}{(a+1)Q(a)^2}.
\]
This equality is an identity in the rational-function field \(\mathbb Q(a)\). All generator entries, the two normalized linear systems and the final identity are explicitly reconstructed and checked by the supplied `verify.py`; the checker performs symbolic rational arithmetic and verifies that the difference has identically zero numerator. It is a reproducible finite polynomial-identity calculation, not an inference from sampled parameter values. Since \(P,Q\) have strictly positive coefficients and \(a>0\), the sign statement follows for *all* admissible \(a\).

For the minimal-size assertion, if the two endpoint sites have identical clean residence times, any chain of at most three sites with a single interior defect is invariant under spatial reflection. Reflection swaps the reservoir densities and reverses current, giving \(J(\delta)=-J(-\delta)\) for every admissible \(\delta\). For four sites, the computed coefficient is nonzero for every \(a\ne1\), completing the minimality statement.

## Verification

Run `python verify.py` with Python 3 and SymPy installed. The program enumerates all sixteen states; independently constructs both generator matrices from transition rules; verifies zero column sums, equilibrium stationarity and normalization; solves both perturbation equations over rational functions; verifies the displayed polynomial identity exactly; checks polynomial coefficient positivity; and compares two exact rational specialization values. It returned `EXACT_IDENTITY_PASS`, `SIGN_AND_HOMOGENEOUS_LIMIT_PASS` and `TWO_EXACT_RATIONAL_SPOT_CHECKS_PASS`. A separate independent direct stationary solve at \(\delta=1/100\) and \(\delta=-1/100\) gave even-current components of opposite signs for \(a=1/2\) and \(a=2\), as predicted. The universal sign follows from the symbolic identity and positive polynomial coefficients, not from the finite evaluations.

## Relationship to prior work

Sakai and Akimoto (2026) introduce this boundary-driven site-disordered exclusion model, give the equilibrium product law, establish reflection as a necessary symmetry constraint, and investigate quadratic rectification using an approximate nonlinear closure. The present result uses exactly that model (after uniform time rescaling), but removes the closure in the smallest possible non-reflection-symmetric single-defect instance, establishing sufficiency and a complete sign classification in this restricted family. It does not claim the general model, approximate mechanisms, equilibrium law or reflection relation as discoveries. Chou (1997/1998) studied transport and defects in single-file pores with different parameterizations and mean-field results; the closest related 2026 field-driven study concerns reversal of an imposed bulk bias rather than exchange of boundary densities.

## Limitations

Only one interior site varies; all other residence times and boundary exchange scales are fixed. The exact finite-size sign classification does not establish that every asymmetric random profile rectifies, a uniform statement over mean reservoir densities, nonzero-gradient global sign, or a macroscopic limit. The small-system rational formula is algebraically lengthy and not asserted to have a simpler closed form. Publication priority remains qualified because broader finite-state nanopore transport results could imply this exact specialization; the highly relevant 2026 paper's later sections and appendices could not be exhaustively reopened during the literature comparison. No independent scientific audit has been performed.

## References

- I. Sakai and T. Akimoto, *Sample-specific rectification-like response in a boundary-driven exclusion process*, arXiv:2609.03560v1 (publicly submitted 2026-09-03). https://arxiv.org/abs/2609.03560
- I. Sakai and T. Akimoto, *Symmetry Breaking of Current Response in Disordered Exclusion Processes*, arXiv:2512.03316v1 (2025). https://arxiv.org/abs/2512.03316
- T. Chou, *How fast can fluids squeeze through micro-pores?*, arXiv:cond-mat/9708223 (1997); *Physical Review Letters* 80, 85 (1998). https://arxiv.org/abs/cond-mat/9708223
