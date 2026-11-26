# Geometric-payoff stability on a periodically renewing resource

## Finding

For the type-II discrete eco-evolutionary game map defined below, a resource period-two orbit on the defector-only face has an exact transverse invasion multiplier
\[
\Lambda_x=\overline{S}^{\,2}-(S_1-S_0)^2\frac{(A-3)(A+1)}{4A^2},
\qquad
\overline{S}=S_0+(S_1-S_0)\frac{A+1}{2A}.
\]
In the resource-stable period-two window \(3<A<1+\sqrt 6\), the boundary two-cycle is locally asymptotically attracting if \(\Lambda_x<1\), and transversely unstable if \(\Lambda_x>1\). The equality case is not classified by linearization. For any resource period-\(p\) orbit on that face, the exact transverse multiplier is \(\prod_{j=1}^p S(n_j)\), not the \(p\)th power of the payoff at the mean resource abundance.

In particular, a nonempty open interval of strictly positive, physically admissible payoffs has \(\overline S>1\) but \(\Lambda_x<1\): the arithmetic-mean game favors invasion by rare cooperators even though the actual oscillating resource and defector population form a locally attracting two-cycle. In the explicit family below this discrepancy holds throughout the **sharp interval**
\[
1<m<\frac{\sqrt{277}}{16}.
\]

## Assumptions and scope

Let \(x\in[0,1]\) denote cooperator frequency, \(n\in[0,1]\) normalized resource abundance, and \(r,e_L,e_H>0\) the resource growth and two harvesting coefficients. The two-step coupled update is
\[
\begin{aligned}
n'&=n\{(r-e_H)+(e_H-e_L)x-(r-e_H)n\},\\
x'&=\frac{x f_C(x,n)}{x f_C(x,n)+(1-x)f_D(x,n)},\\
f_C(x,n)&=2x+S(n)(1-x),\\
f_D(x,n)&=T(n)x+(1-x),\\
S(n)&=(1-n)S_0+nS_1,\quad T(n)=(1-n)T_0+nT_1.
\end{aligned}
\]
This is the normalized resource equation and positive-fitness type-II replicator map of Mondal, Ray, and Chakraborty (2024), with environmental payoff matrices \(U_i=\begin{pmatrix}2&S_i\\T_i&1\end{pmatrix}\). Assume \(0<e_L<e_H<r\), \(S_0,S_1,T_0,T_1>0\), and parameters for which the biological square is forward-invariant. Set \(A=r-e_H\), and assume \(3<A<1+\sqrt6\) for the period-two conclusions. These restrictions are fulfilled strictly by the explicit family below.

The exact counterexample family fixes
\[
r=\frac{37}{10},\quad e_L=\frac14,\quad e_H=\frac12,\quad
T_0=\frac32,\quad T_1=3,\quad
S_0=m+\frac{21}{16},\quad S_1=m-\frac{11}{16},
\]
with \(1<m<\sqrt{277}/16\). The resource-poor matrix is a harmony game; the resource-rich matrix is a prisoner's dilemma. All payoffs are strictly positive. Both the biological square and the resource two-cycle lie in the stated domain.

## Proof

**1. Resident resource dynamics.** Because \(x=0\) is invariant, its resource coordinate follows the logistic map \(g(n)=An(1-n)\). For \(3<A<1+\sqrt6\), the two distinct positive points of its primitive period-two orbit are
\[
n_\pm=\frac{A+1\pm\sqrt{(A-3)(A+1)}}{2A}.
\]
Direct substitution gives \(g(n_-)=n_+\) and \(g(n_+)=n_-\). Their average and two-point variance are
\[
\bar n=\frac{A+1}{2A},\qquad
V_n=\frac{(A-3)(A+1)}{4A^2}.
\]
The product of the two derivatives of \(g\) is
\[
\Lambda_n=g'(n_-)g'(n_+)=-A^2+2A+4,
\]
which lies strictly between \(-1\) and \(1\) in the specified period-two window.

**2. Exact transverse multiplier.** At \(x=0\) the fitnesses satisfy \(f_C(0,n)=S(n)\) and \(f_D(0,n)=1\). The derivative of the cooperator update with respect to \(x\) therefore equals \(S(n)>0\); its partial derivative with respect to \(n\) vanishes because of the leading factor \(x\). Thus the one-step Jacobian along the resident face is triangular, and the two-step Jacobian has diagonal entries \(S(n_-)S(n_+)\) and \(\Lambda_n\). Since \(S\) is affine,
\[
S(n_-)S(n_+)=\left(\frac{S(n_-)+S(n_+)}2\right)^2
-\left(\frac{S(n_-)-S(n_+)}2\right)^2
=\overline S^{\,2}-(S_1-S_0)^2V_n.
\]
The discrete local stability theorem gives attraction when both multipliers have modulus less than one; \(S(n_-)S(n_+)>1\) produces transverse instability. The same triangular-product argument proves the stated period-\(p\) formula. With positive \(S(n_j)\), arithmetic–geometric mean implies \(\frac1p\sum_jS(n_j)<1\) is sufficient but not necessary for contraction. Equality of the product to one is a nonhyperbolic case and is deliberately excluded from stability conclusions.

**3. A sharp physical disagreement interval.** In the explicit family, \(A=16/5\) and
\[
n_\pm=\frac{21\pm\sqrt{21}}{32},\quad
\bar n=\frac{21}{32},\quad V_n=\frac{21}{1024},\quad
S(n)=m+\frac{21}{16}-2n.
\]
Hence \(\overline S=m\), \(\Lambda_x=m^2-21/256\), and \(\Lambda_n=4/25\). For \(1<m<\sqrt{277}/16\), the mean-game cooperator multiplier is strictly above one, but the actual transverse period-return multiplier lies strictly between zero and one. At the upper endpoint the transverse multiplier is exactly one; no nonlinear critical-case assertion is made.

The resource update throughout this family is \(n'=n(16/5+x/4-(16/5)n)\). On the unit square it is nonnegative (its values at \(n=0\) and \(n=1\) are \(0\) and \(x/4\), and it is concave in \(n\)). Its global maximum does not exceed
\[
\frac{(16/5+1/4)^2}{4(16/5)}=\frac{4761}{5120}<1.
\]
Every payoff entry is strictly positive on the stated \(m\)-interval, so the type-II replicator update sends \([0,1]\) into itself. Thus the entire biological square is forward-invariant. The inequalities are strict in the interior of the \(m\)-interval and persist on a nonempty open set of full model parameters.

**4. Exact rational witness.** Taking \(m=403/400\) gives \(S_0=58/25\) and \(S_1=8/25\). The average-game multiplier and the actual two-step eigenvalues are, respectively,
\[
\overline S=\frac{403}{400}>1,
\qquad (\Lambda_x,\Lambda_n)=\left(\frac{37321}{40000},\frac4{25}\right).
\]
Both actual multipliers are strictly inside the unit disk. This proves an attracting resource-oscillatory, all-defector two-cycle despite the opposite prediction from substituting the mean environment into the single-step invasion derivative.

## Verification

The accompanying `verify_oscillatory_selection.py` symbolically reconstructs the normalized resource map, the two-cycle, the two-step Jacobian, its exact eigenvalues, the square-invariance bound, and the symbolic variance identity. It also checks 42 distinct nearby two-dimensional trajectories for convergence to the cycle. Install Python 3 and SymPy and run `python verify_oscillatory_selection.py`; its success message reports exact multipliers \(37321/40000\) and \(4/25\). The finite trajectory experiments are illustrations, not the proof of local attraction.

## Relationship to prior work

Mondal, Ray, and Chakraborty (2024) introduce this discrete ecological replicator family, establish parameter conditions ensuring the physical state domain, numerically examine periodic/chaotic resources, and explicitly propose using the **mean resource state** to judge attraction of boundary strategy manifolds (their Sec. III B and Table I). That paper does not give the stated product-of-multipliers condition, variance-corrected period-two stability boundary, or a fully admissible open parameter interval on which the mean-game criterion reverses the true transverse stability classification. The present result applies standard Floquet reasoning to a different question: the exact model-specific selection threshold under periodic ecological forcing. Periodic-orbit stability and arithmetic/geometric mean inequalities are classical tools, not claimed as new in isolation.

Ito and Yamamichi (2024) classify equilibria and oscillations in a **continuous-time** environmental-feedback evolutionary game based on differential equations, so their classifications do not imply a transverse multiplier for this discrete map. Mukhopadhyay and Chakraborty (2020/2021) study evolutionary stability of periodic orbits of replicator maps, but their cited work does not itself identify the present coupled logistic-resource threshold. Searches of relevant mathematics records and the publicly indexed literature did not identify an implication covering the exact claim; this is a bounded originality assessment, not a proof of exhaustive novelty.

## Limitations

This theorem concerns *local* asymptotic stability of the boundary two-cycle, not global attraction from all positive cooperator fractions, chaotic resource regimes, finite-population fixation, or robustness under exogenous noise. The stability at \(\Lambda_x=1\) is unresolved by the present linear method. The statement assumes the specified positive type-II fitnesses, and the explicit physical family is only one region of the wider parameter space. Comparison with unindexed specialist publications remains an originality risk.

## References

1. S. S. Mondal, A. Ray, and S. Chakraborty, *Hypochaos prevents tragedy of the commons in discrete-time eco-evolutionary game dynamics*, Chaos **34**, 023122 (2024). First public arXiv posting 2024-01-20, arXiv:2401.12245; DOI:10.1063/5.0190800. Author-posted accepted manuscript: https://www.researchgate.net/publication/378339974_Hypochaos_prevents_tragedy_of_the_commons_in_discrete-time_eco-evolutionary_game_dynamics
2. H. Ito and M. Yamamichi, *A complete classification of evolutionary games with environmental feedback*, PNAS Nexus **3**, pgae455 (2024). DOI:10.1093/pnasnexus/pgae455.
3. A. Mukhopadhyay and S. Chakraborty, *Periodic orbit can be evolutionarily stable: Case Study of discrete replicator dynamics*, Journal of Theoretical Biology **497**, 110288 (2020). DOI:10.1016/j.jtbi.2020.110288.
