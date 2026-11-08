# Increasing reset hazards exactly characterize universal quantum channel divisibility

## Finding

Consider a discrete-time renewal resetting protocol on any finite-dimensional quantum system. Between resets a fixed completely positive trace-preserving (CPTP) map \(\mathcal E\) acts; each reset replaces the state with a fixed density operator \(\sigma\). When the elapsed number of steps since the last reset equals \(j\geq1\), the reset probability is \(r_j\), with \(0<r_j<1\). Initially there has been no reset after time zero. Let \(\Phi_t\) denote the ensemble-averaged channel from time zero to integer time \(t\geq0\).

**Universal divisibility criterion.** The following conditions are equivalent:

1. The sequence \((r_j)_{j\geq1}\) is nondecreasing.
2. For every finite Hilbert-space dimension, every CPTP step map \(\mathcal E\), and every reset density operator \(\sigma\), the channel sequence \((\Phi_t)_{t\geq0}\) is CP-divisible: for all integers \(s<t\), some CPTP channel \(\Lambda_{t,s}\) satisfies \(\Phi_t=\Lambda_{t,s}\circ\Phi_s\).
3. The analogous universal statement with positive trace-preserving intermediate maps holds.

The sufficient direction has explicit channels. Write \(S_0=1\), \(S_j=\prod_{a=1}^j(1-r_a)\), and let \(\nu_m\) be the probability that a reset occurs at step \(m\) (so \(\nu_1=r_1\)). For every \(t\geq0\), define
\[
 c_{t,0}=\nu_{t+1},\qquad
 c_{t,a}=\nu_{t+1-a}S_{a-1}(r_{t+1}-r_a),\quad 1\leq a\leq t.
\]
Then \(\sum_{a=0}^t c_{t,a}=r_{t+1}\), and when hazards are nondecreasing all the coefficients are nonnegative. With \(\mathcal P_\tau(X)=\operatorname{Tr}(X)\tau\),
\[
 \Lambda_{t+1,t}=(1-r_{t+1})\mathcal E+
    \sum_{a=0}^t c_{t,a}\,\mathcal P_{\mathcal E^a(\sigma)}
\]
is a CPTP propagator satisfying \(\Phi_{t+1}=\Lambda_{t+1,t}\circ\Phi_t\).

The converse is quantitatively witnessed at **each strict adjacent hazard decline** \(r_{t+1}<r_t\), where \(t\geq1\). There is an explicit unitary step map and a pure reset state in dimension \(t+1\) for which the unique intermediate map \(\Phi_{t+1}\Phi_t^{-1}\) is not even positive. On a particular rank-one input its output has a negative diagonal entry equal to
\[
 -r_1 S_{t-1}(r_t-r_{t+1})<0.
\]
Thus the nondecreasing-hazard condition cannot be weakened if divisibility is required uniformly over all quantum systems. It does **not** assert that every fixed system becomes indivisible when its hazard decreases.

## Assumptions and scope

Time is discrete and starts at \(t=0\). The reset age is the count of steps since the preceding reset or the initialization at zero. The hazard \(r_j\) applies at age \(j\); it is strictly between zero and one for every integer \(j\geq1\). Waiting times in successive renewal cycles are independent with this same age-dependent hazard law. The quantum step channel \(\mathcal E\) is fixed, linear, CPTP, and acts on a finite-dimensional Hilbert space; the same \(\sigma\) is used at every reset. A step either performs \(\mathcal E\) or replaces the state by \(\sigma\), not both. All statements concern finite-time averaged channels and do not require an invariant state or an almost-sure eventual reset when the hazard decreases.

A sequence is CP-divisible if all later averaged channels factor through earlier ones by CPTP maps; P-divisibility instead requires positive trace-preserving maps. The word *universal* means for every dimension, step channel and reset state, not for a fixed realization or individual sampled trajectory.

## Proof

**1. Renewal decomposition.** The first waiting-time mass at \(j\geq1\) is \(f_j=r_jS_{j-1}\). Define the renewal-event probability
\[
 \nu_j=\sum_{k=1}^j(f^{*k})_j,\qquad j\geq1.
\]
(The convolution is over strictly positive integer times.) At time \(t\), the no-reset probability is \(S_t\); if the most recent reset was at time \(t-a\geq1\), its probability is \(\nu_{t-a}S_a\). Consequently, on every operator \(X\),
\[
 \Phi_t(X)=S_t\mathcal E^t(X)+\operatorname{Tr}(X)B_t,
 \quad B_t=\sum_{a=0}^{t-1}\nu_{t-a}S_a\mathcal E^a(\sigma),
 \quad B_0=0.
\]
The mutually exclusive renewal events partition path space, hence \(\operatorname{Tr}B_t=1-S_t\). This also shows that \(\Phi_t\) is CPTP for every hazard sequence.

**2. An exact factorization valid without monotonicity.** Set \(k_t=S_{t+1}/S_t=1-r_{t+1}\). Consider \(C_t=B_{t+1}-k_t\mathcal E(B_t)\). The age-zero term is \(\nu_{t+1}\sigma\). For every \(1\leq a\leq t\), the coefficient of \(\mathcal E^a(\sigma)\) is
\[
 \nu_{t+1-a}[S_a-k_t S_{a-1}]
 =\nu_{t+1-a}S_{a-1}(r_{t+1}-r_a).
\]
Thus \(C_t=\sum_{a=0}^t c_{t,a}\mathcal E^a(\sigma)\), and trace preservation gives
\[
 \sum_{a=0}^t c_{t,a}=\operatorname{Tr} C_t
 =(1-S_{t+1})-k_t(1-S_t)=r_{t+1}.
\]
For any \(X\), define \(\Lambda_{t+1,t}(X)=k_t\mathcal E(X)+\operatorname{Tr}(X)C_t\). Substitution gives
\[
 \Lambda_{t+1,t}\bigl(\Phi_t(X)\bigr)
 =S_{t+1}\mathcal E^{t+1}(X)
 +\operatorname{Tr}(X)[k_t\mathcal E(B_t)+C_t]
 =\Phi_{t+1}(X).
\]
Here \(\operatorname{Tr}\Phi_t(X)=\operatorname{Tr}X\). This factorization is valid for all CPTP \(\mathcal E\), including noninvertible maps.

**3. Sufficiency.** If \(r_{t+1}\geq r_a\) for every \(a\leq t\), all \(c_{t,a}\geq0\), since renewal masses and survivals are nonnegative. Each \(\mathcal P_{\mathcal E^a(\sigma)}\) is a CPTP replacement channel, and the displayed coefficients are nonnegative and sum with \(k_t\) to one. Hence \(\Lambda_{t+1,t}\) is CPTP. Composition over integer steps proves CP-divisibility. The implications from CP to P are immediate.

**4. Necessity and exact witness.** Suppose \(r_{t+1}<r_t\) at some \(t\geq1\). Choose dimension \(d=t+1\) with basis \(\{|0\rangle,\ldots,|t\rangle\}\), reset state \(\sigma=|0\rangle\langle0|\), and unitary cyclic shift \(U|a\rangle=|a+1\bmod d\rangle\). Let \(\mathcal E=\operatorname{Ad}_U\). In the expression for \(C_t\) all \(\mathcal E^a(\sigma)=|a\rangle\langle a|\), for \(0\leq a\leq t\), are mutually orthogonal. The diagonal entry at \(|t\rangle\) is therefore
\[
 \langle t|C_t|t\rangle
 =c_{t,t}=\nu_1S_{t-1}(r_{t+1}-r_t)
 =-r_1S_{t-1}(r_t-r_{t+1})<0.
\]
Since \(S_t>0\) and \(U\) is unitary, \(\Phi_t\) is invertible as a linear map on all operators: given \(Y=\Phi_t(X)\), one first has \(\operatorname{Tr}X=\operatorname{Tr}Y\), and then
\[
 X=S_t^{-1}\operatorname{Ad}_{U^{-t}}
 \bigl(Y-\operatorname{Tr}(Y)B_t\bigr).
\]
Thus the intermediate map is unique and equals the factorization in Step 2. Applying it to \(|t\rangle\langle t|\), the unitary term is supported on \(|0\rangle\), not on \(|t\rangle\), so its output has strictly negative \(|t\rangle\) diagonal entry. The unique intertwiner is not positive. Therefore universal P-divisibility forces the absence of every adjacent hazard decline. Combining Steps 3 and 4 proves all stated equivalences.

**5. Concrete two-level boundary.** For \(r_1=3/4\), \(r_2=1/4\), the first two renewal masses are \(\nu_1=3/4\), \(\nu_2=5/8\). The propagator forced between times one and two for the cyclic qubit gate is
\[
 \Lambda_{2,1}(X)=\tfrac34 U X U^\dagger
 +\operatorname{Tr}(X)\bigl(\tfrac58|0\rangle\langle0|
 -\tfrac38|1\rangle\langle1|\bigr).
\]
It maps \(|1\rangle\langle1|\) to a matrix with eigenvalues \(11/8\) and \(-3/8\). By contrast, increasing hazards \(r_1=1/4\), \(r_2=3/4\) yield nonnegative reset weights \(5/8\) and \(1/8\), and a CPTP intermediate map.

## Verification

Run `python3 verify.py` in the same directory as this file. The standalone standard-library program performs exact-fraction finite renewal-age recursion, constructs the intermediate factorization and checks its composition with each averaged map on all matrix units of small cyclic-shift systems. It tests both increasing and decreasing rational hazard profiles, the coefficient normalization, and the explicit negative witness. The observed run passed 244 finite profiles and 17,476 exact identities/checks. The general iff theorem is established by the symbolic proof above; finite tests are not a substitute for it.

## Relationship to prior work

Carollo and Wald, *Stochastic resetting induces quantum non-Markovianity* (arXiv:2601.13367, first publicly posted 2026-01-19), provide the last-renewal channel equation and investigate divisibility by numerical witnesses as well as an alternating-reset example which is CP-divisible in the Schrödinger picture. The renewal channel equation and examples are prior work. The result here supplies an all-dimension, all-CPTP-step-map **if-and-only-if universal criterion** in terms of monotonicity of the hazard, together with a quantified unitary witness for every hazard decline. Their alternating example is consistent: universal and model-specific divisibility are different statements.

Wald et al., *Stochastic resetting in discrete-time quantum dynamics* (arXiv:2410.11497, 2024), develop the same renewal-age bookkeeping and stationary-state analysis, but their presented results do not give the universal intermediate-channel classification. Vacchini, *Quantum renewal processes* (arXiv:1906.00693, 2019), establishes CPTP evolution maps for broad renewal constructions, a distinct requirement from CP-divisibility **between** times. The classical increasing-failure-rate concept and generic positivity of renewal kernels alone do not furnish the converse quantum unitary witness.

## Limitations

The necessity assertion is **universal**: a decrease is guaranteed to be detectable in some dimension, not in every fixed quantum device. The exhibited dimension grows with the step of the drop. Hazards equal to zero or one are outside the stated domain; in particular, zero survival could destroy invertibility and require separate treatment. The theorem concerns Schrödinger-picture averaged channel divisibility, not divisibility in the Heisenberg-picture convention of the motivating article, nor process-tensor Markovianity or physical classical age memory. The construction involves finite-time channels only; no statement on existence or uniqueness of a long-time steady state is made. Broader quantum semi-Markov divisibility results or unexamined supplements might contain an equivalent classification; publication priority is therefore not independently established.

## References

1. F. Carollo and S. Wald, *Stochastic resetting induces quantum non-Markovianity*, arXiv:2601.13367 (2026), https://arxiv.org/abs/2601.13367 (original public posting 2026-01-19).
2. S. Wald, L. H. Yao, T. Platini, C. Hooley, F. Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497 (2024), https://arxiv.org/abs/2410.11497.
3. B. Vacchini, *Quantum renewal processes*, arXiv:1906.00693 (2019), https://arxiv.org/abs/1906.00693.
4. D. Chruściński, Á. Rivas and E. Størmer, *Divisibility and information flow notions of quantum Markovianity for noninvertible dynamical maps*, arXiv:1710.06771 (2017), https://arxiv.org/abs/1710.06771.
