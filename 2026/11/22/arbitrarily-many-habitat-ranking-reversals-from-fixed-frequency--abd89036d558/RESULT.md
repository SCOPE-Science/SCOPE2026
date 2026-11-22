# Arbitrarily many habitat-ranking reversals from fixed-frequency behavioral switching

## Finding

Consider an individual moving between two habitats, A and B, in one of \(m\ge1\) behavioral modes. Its behavior is an autonomous, irreducible continuous-time Markov chain with generator \(sQ\), where the common switching-speed multiplier satisfies \(s>0\). In mode \(i\), movement from A to B occurs at rate \(u_i>0\), and movement from B to A at rate \(v_i>0\). Behavioral changes leave the habitat unchanged; movement leaves the behavior unchanged. All rates are time-homogeneous.

Let \(p_A(s)\) be the unique stationary fraction of time spent in habitat A. Fix any benchmark \(c\in(0,1)\). Then either \(p_A(s)=c\) for every \(s>0\), or the equation \(p_A(s)=c\) has at most \(m-1\) positive solutions, counted with multiplicity. **The bound is sharp for every number of modes:** for any integer \(m\ge2\), any \(c\in(0,1)\), and any prescribed distinct positive switching speeds \(0<t_1<\cdots<t_{m-1}\), strictly positive movement rates can be chosen so that \(p_A(s)-c\) reverses sign at precisely these speeds and nowhere else. The behavioral-state stationary frequencies remain uniform, independent of \(s\), in this construction.

For an explicit three-mode example, let the behavior generator have unit rates between every pair of distinct modes, and take the A-to-B rates and B-to-A rates, respectively, to be
\[
(u_1,u_2,u_3)=\left(\frac3{32},\frac{233}{128},\frac{25}{16}\right),\qquad
(v_1,v_2,v_3)=\left(\frac{29}{32},\frac{23}{128},\frac{39}{16}\right).
\]
Then
\[
p_A(s)=\frac12+\frac{9(s-1)(s-4)}{128(21s^2+28s+8)}.
\]
Thus habitat A has greater stationary occupancy for \(0<s<1\) and for \(s>4\), whereas habitat B has greater occupancy for \(1<s<4\); equality holds only at \(s=1,4\). Meanwhile, every mode has stationary frequency \(1/3\) at every speed. A weighted mixture of the three mode-isolated occupancy fractions is the fixed number \(137/256>1/2\) and therefore misses the intermediate reversal.

## Assumptions and scope

The joint state space has \(2m\) states \((A,i)\), \((B,i)\), \(i=1,\ldots,m\). The row generator \(Q\) satisfies \(Q\mathbf 1=0\), has nonnegative off-diagonal entries, and is irreducible. The only switching-speed dependence is the factor \(s>0\) multiplying \(Q\); in particular, behavioral switching rates do not depend on the current habitat. The site-movement rates \(u_i,v_i\) are positive and are independent of \(s\). Let \(\pi\) be the unique positive probability column vector satisfying \(Q^\top\pi=0\).

The result is about a single stationary habitat probability and its crossings of an arbitrary fixed benchmark; it does not claim that \(p_A(s)\) has at most \(m-1\) extrema, nor does it address three or more habitats, habitat-dependent behavioral switches, or transient occupancies. The value \(s=0\) is excluded because the joint chain need not be irreducible there.

## Proof

Write \(r_i=u_i+v_i\) and \(D=\operatorname{diag}(r_1,\ldots,r_m)\). Let \(x_i(s)\) be the joint stationary mass of state \((A,i)\). Because behavioral switching is autonomous, the joint stationary behavior marginal is \(\pi\), so the mass of \((B,i)\) is \(\pi_i-x_i\). Habitat-A stationarity therefore gives
\[
(D-sQ^\top)x=\operatorname{diag}(v_1,\ldots,v_m)\pi.
\]
The matrix \(M(s)=D-sQ^\top\) is invertible for every \(s>0\): it is the negative transpose of the generator of a behavior chain killed at mode-dependent positive rates \(r_i\). More explicitly, its inverse equals \(\int_0^\infty\exp[(sQ^\top-D)t]\,dt\), a convergent nonnegative matrix. Since \(M(0)=D\) has positive determinant and \(M(s)\) is nonsingular throughout \(s\ge0\), its determinant is strictly positive throughout that range.

For a prescribed \(c\in(0,1)\), define \(g_i=v_i-cr_i\) and \(z=x-c\pi\). Since \(Q^\top\pi=0\),
\[
M(s)z=\operatorname{diag}(\pi_1,\ldots,\pi_m)g,
\qquad
p_A(s)-c=\frac{\mathbf1^\top\operatorname{adj}(M(s))\operatorname{diag}(\pi)g}{\det M(s)}.
\]
The numerator is a polynomial of degree at most \(m-1\), because every adjugate entry is an \((m-1)\)-square minor of a matrix affine in \(s\). Also, \(\det M(s)\) has degree at most \(m-1\), since the coefficient of \(s^m\) is \(\det(-Q^\top)=0\). As the denominator is strictly positive, the numerator is either identically zero or has at most \(m-1\) positive zeros with multiplicity. This proves the universal bound.

To attain any \(m-1\) prescribed distinct positive crossings, choose distinct positive \(r_1,\ldots,r_m\) and the complete-graph behavioral generator \(Q=\mathbf1\mathbf1^\top-mI\). It has unit off-diagonal rates and stationary marginal \(\pi_i=1/m\), for every \(s>0\). The matrix is
\[
M(s)=\operatorname{diag}(r_i+ms)-s\mathbf1\mathbf1^\top.
\]
The rank-one inverse formula gives
\[
p_A(s)-c=\frac{\displaystyle\frac1m\sum_{i=1}^m\frac{g_i}{r_i+ms}}{\displaystyle1-s\sum_{i=1}^m\frac1{r_i+ms}}.
\]
Its denominator is strictly positive, because each summand \(s/(r_i+ms)\) is strictly less than \(1/m\).

Define \(P(s)=\prod_{j=1}^{m-1}(s-t_j)\) and
\[
a_i=\frac{P(-r_i/m)}{\prod_{k\ne i}(r_k-r_i)}.
\]
The two polynomials of degree at most \(m-1\),
\[
\sum_{i=1}^m a_i\prod_{k\ne i}(r_k+ms)\quad\text{and}\quad P(s),
\]
agree at all \(m\) distinct points \(s=-r_i/m\), and hence are identical. Choose \(\varepsilon>0\) sufficiently small that \(-cr_i<\varepsilon a_i<(1-c)r_i\) for each \(i\), and set \(v_i=cr_i+\varepsilon a_i\) and \(u_i=(1-c)r_i-\varepsilon a_i\). These rates are strictly positive. Substitution shows that the sign of \(p_A(s)-c\), for every positive \(s\), is exactly the sign of \(P(s)\): all factors in its denominator are strictly positive. The \(m-1\) simple positive roots are precisely the prescribed \(t_j\) and the sign changes at every one. For \(m=1\), the stationary occupancy is \(v_1/(u_1+v_1)\), independent of \(s\). This completes the proof.

For the explicit example, take \(c=1/2\), \((r_1,r_2,r_3)=(1,2,4)\), \((t_1,t_2)=(1,4)\), and \(\varepsilon=27/128\). The interpolation formula yields \((g_1,g_2,g_3)=(13/32,-105/128,7/16)\). The above rank-one identity simplifies to the displayed rational formula. Its quadratic denominator is strictly positive for all \(s>0\), so the two crossings and their signs are exact, not numerical inferences.

## Verification

Run `python check.py` with Python 3 and SymPy. The script reconstructs the exact six-state equilibrium at ten rational switching speeds, checks both crossover roots and three sign regimes, verifies the construction by exact polynomial interpolation for mode counts from two through eight, and checks the polynomial-degree bound on additional generic rational examples. The observed output is `PASS: 116 supplementary exact-arithmetic assertions`. These finite checks supplement but do not replace the all-parameter algebraic proof above.

## Relationship to prior work

McClintock and Lander (2023) develop behavior-specific continuous-space Langevin movement inference and explicitly distinguish stationary behavioral frequencies from an empirical weighted mixture of behavior-specific utilization distributions. Klappstein, Thomas and Michelot (2023) use integrated behavior-specific step-selection models and simulated overall utilization distributions. Their underlying processes and objectives differ from the present finite-state, stationary two-habitat threshold theorem; neither inspected text presents its sharp mode-count law or prescribed-crossover realization.

Economou (2005), extending earlier product-form conditions, treats Markov chains in autonomous random environments and proves a criterion for factorized stationary distributions. In the two-habitat model, equal isolated habitat preferences \(v_i/u_i\) across all modes constitute the factorized special case; the strictly positive constructed examples have differing preferences and are not covered by that factorization criterion. General matrix-tree, adjugate, and resolvent methods are prior mathematics used in the proof. The particular sharpened crossing bound and positivity-preserving inverse design are the mathematical content claimed here. Research-record comparisons were made against related Markov occupation, switching-ratchet current, and patch-dispersal results; these have different observables or generators, and no implication to the exact stated claim was established from the inspected material.

## Limitations

The model is intentionally two-habitat, continuous-time, memoryless and finite-state. Its autonomous behavior-switching assumption is essential to the \(m-1\) bound; arbitrary habitat-dependent switching is outside the theorem. No field data, parameter calibration, transient dynamics, or statistical identifiability and robustness under observation noise are asserted. The crossover examples are theoretical constructions, not ecological prescriptions. Although no covering statement was located in inspected sources, an older general rational-interpolation treatment of Markov-modulated two-state processes may exist; historical priority is not independently certified.

## References

- McClintock, B. T., and M. E. Lander (2023). *A multistate Langevin diffusion for inferring behavior-specific habitat selection and utilization distributions*. Ecology, DOI: https://doi.org/10.1002/ecy.4186. First publicly available accepted manuscript: 2023-10-05.
- Klappstein, N. J., L. Thomas, and T. Michelot (2023). *Flexible hidden Markov models for behaviour-dependent habitat selection*. Movement Ecology 11, 30. https://doi.org/10.1186/s40462-023-00392-3.
- Economou, A. (2005). *Generalized product-form stationary distributions for Markov chains in random environments with queueing applications*. Advances in Applied Probability 37, 185–211. https://doi.org/10.1239/aap/1113402405.
