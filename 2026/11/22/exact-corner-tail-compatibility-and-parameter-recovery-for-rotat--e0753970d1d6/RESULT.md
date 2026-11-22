# Exact corner-tail compatibility and parameter recovery for rotated Clayton mixtures

## Finding

Fix an integer \(m\ge 3\). For every orientation \(s\in\{0,1\}^m\) and every coordinate \(i\in\{1,\ldots,m\}\), let \(\Lambda_s^{(i)}\) be the limiting probability that coordinate \(i\) lies in its designated extreme tail, conditioned on the other \(m-1\) coordinates all lying in their designated extreme tails, with every tail band having width \(t\downarrow0\).

For the full-support mixture of all coordinate rotations of the \(m\)-variate Clayton copula with **one common parameter** \(\theta>0\) and orientation weights \(\pi_s>0\), \(\sum_s\pi_s=1\), the limits exist and satisfy

\[
\boxed{\Lambda_s^{(i)}=h\frac{\pi_s}{\pi_s+\pi_{s\oplus e_i}},\qquad h=\left(\frac{m-1}{m}\right)^{1/\theta}.}
\]

Here \(e_i\) flips the \(i\)-th bit; \(\oplus\) denotes bitwise exclusive-or. **Conversely**, a real array \(L_s^{(i)}\), with all coordinates indexed as above, is exactly the corner-tail array of some such mixture if and only if:

1. Each \(L_s^{(i)}>0\).
2. There is one number \(h\in(0,1)\) such that \(L_s^{(i)}+L_{s\oplus e_i}^{(i)}=h\) for every \(s,i\).
3. Writing \(R_s^{(i)}=L_{s\oplus e_i}^{(i)}/L_s^{(i)}\), every coordinate square satisfies

   \[
   R_s^{(i)}R_{s\oplus e_i}^{(j)}=R_s^{(j)}R_{s\oplus e_j}^{(i)}
   \qquad(i\ne j).
   \]

When they hold, **both the common parameter and every orientation weight are uniquely determined**. The parameter is

\[
\boxed{\theta=\frac{\log((m-1)/m)}{\log h}}.
\]

For the weights, set \(w_{(0,\ldots,0)}=1\), transport \(w_{s\oplus e_i}=w_sR_s^{(i)}\) along any hypercube path, and normalize \(\pi_s=w_s/\sum_vw_v\); the square identities make this independent of the chosen path. Thus a positive corner-tail table can fail to arise from the model even if all of its opposite-end edge sums agree.

## Assumptions and scope

Let \(V=(V_1,\ldots,V_m)\) have the Clayton copula

\[
C_\theta(v_1,\ldots,v_m)=\left(\sum_{k=1}^{m}v_k^{-\theta}-m+1\right)^{-1/\theta},\quad 0<v_k\le1,\quad\theta>0.
\]

Draw an orientation \(S\) independently with \(\Pr(S=s)=\pi_s\), and conditionally set \(U_k=V_k\) if \(s_k=0\), or \(U_k=1-V_k\) if \(s_k=1\). The distribution of \(U\) is a genuine copula and its margins are uniform. For \(0<t<1/2\), put \(B_0(t)=[0,t]\), \(B_1(t)=[1-t,1]\) and

\[
\Lambda_s^{(i)}=\lim_{t\downarrow0}
\Pr\left(U_i\in B_{s_i}(t)\,\middle|\, U_k\in B_{s_k}(t)\ \text{for every }k\ne i\right).
\]

The claim concerns this exact conditional extreme-tail definition and the common-parameter full-support subfamily. It does not classify the unrestricted family with separate Clayton parameters at each orientation. The assumptions \(m\ge3\), \(\theta>0\), and strict positivity of all \(\pi_s\) are material; boundary tables arise as limits but are excluded from the exact full-support statement.

## Proof

**1. Same-corner estimates.** For \(r\ge2\) coordinates in the lower \(t\)-tail of an unrotated Clayton vector, the exact probability is

\[
\Pr(V_1\le t,\ldots,V_r\le t)
=t\bigl(r-(r-1)t^\theta\bigr)^{-1/\theta}
=r^{-1/\theta}t+o(t).
\]

This follows by setting all remaining Clayton-CDF arguments to one. It applies to every subset of \(r\) coordinates, since all lower-dimensional margins are Clayton with the same parameter.

**2. Mixed-corner events are negligible at first order.** For two coordinates, the event with one coordinate below \(t\) and another above \(1-t\) has probability

\[
 t-C_\theta(t,1-t)
 =t\left[1-\left(1+t^\theta\bigl((1-t)^{-\theta}-1\bigr)\right)^{-1/\theta}\right]
 =O(t^{2+\theta})=o(t).
\]

For two coordinates both above \(1-t\), the joint event has probability \(O(t^2)\), because the bivariate Clayton density is continuous and bounded on a neighborhood of \((1,1)\) for fixed \(\theta>0\). Every specified corner event involving at least two coordinates that is not the all-lower corner for the unrotated Clayton law contains either a mixed lower/upper pair or an upper/upper pair. Consequently its probability is \(o(t)\). This argument also applies to any rotated component after expressing the requested events in the component's unrotated coordinates.

**3. Mixture numerator and denominator.** Given target corner \(s\), only the mixture component rotated by \(s\) contributes at order \(t\) to the event that *all* \(m\) coordinates fall in the target corner. Hence

\[
\Pr(U_k\in B_{s_k}(t)\text{ for all }k)
=\pi_s m^{-1/\theta}t+o(t).
\]

When coordinate \(i\) is omitted from conditioning, exactly two rotations agree with the remaining \(m-1\) target bits: \(s\) and \(s\oplus e_i\). Since \(m-1\ge2\), step 2 eliminates every other component at first order. Therefore

\[
\Pr(U_k\in B_{s_k}(t)\text{ for all }k\ne i)
=(\pi_s+\pi_{s\oplus e_i})(m-1)^{-1/\theta}t+o(t).
\]

The denominator has a strictly positive leading coefficient. Dividing proves the boxed corner-tail formula.

**4. Necessity of compatibility.** For each undirected hypercube edge \(\{s,s\oplus e_i\}\), the two corner probabilities share the same denominator, and their numerators sum to that denominator multiplied by \(h\). Thus their sum equals \(h\), strictly between zero and one. Also \(R_s^{(i)}=\pi_{s\oplus e_i}/\pi_s\), so multiplying ratios around any square gives one, yielding the displayed square identities.

**5. Sufficiency and uniqueness.** Suppose the three stated conditions hold. Since \(L_s^{(i)}\) and \(L_{s\oplus e_i}^{(i)}\) are positive and sum to \(h\), all edge odds are positive and satisfy \(R_{s\oplus e_i}^{(i)}=1/R_s^{(i)}\). The square identities permit adjacent coordinate flips to commute in any path product. Any finite walk on the binary cube is reduced to a path in which each coordinate is flipped either zero or one time by canceling repeated flips and commuting adjacent flips. Thus products are path independent. The resulting positive vertex weights \(w_s\), normalized to \(\pi_s\), obey \(R_s^{(i)}=\pi_{s\oplus e_i}/\pi_s\). Taking \(\theta=\log((m-1)/m)/\log h>0\) yields

\[
 h\frac{\pi_s}{\pi_s+\pi_{s\oplus e_i}}=\frac{h}{1+R_s^{(i)}}=L_s^{(i)}.
\]

Step 3 now proves that the constructed mixture has exactly the requested corner-tail array. The common edge sum fixes \(\theta\), and the connected cube's edge odds fix all \(\pi_s\) up to a single positive factor; normalization removes that factor. This proves existence, necessity, and uniqueness.

**6. Strictly local feasibility does not ensure global feasibility.** For \(m=3\), start with the uniform weights and \(\theta=1\), producing \(h=2/3\) and \(L_s^{(i)}=1/3\) on all directed edges. Replace just the two values along the edge \(000\leftrightarrow100\) by \(1/4\) and \(5/12\). Their sum remains \(2/3\), and every directed entry stays strictly between zero and \(h\), but the odds on this one edge become unequal to one while those on the three other edges of any adjacent square remain one. The square condition fails; no common-parameter rotated-Clayton mixture realizes this table.

## Verification

The standalone standard-library script `verify.py` checks six distinct positive exact-rational weight assignments in dimensions three and four, with \(\theta=1\). It tests the constant edge sums, 360 square identities, exact recovery of weights, and rejection of the explicit incompatible table. It also computes exact rational finite-tail conditional probabilities by inclusion–exclusion for three decreasing thresholds in dimension three; the largest absolute discrepancies from the proved limits are approximately \(0.00860510\), \(0.000879344\), and \(0.0000881267\).

Run with `python verify.py` from a directory containing this document and the script. No nonstandard packages or external files are required. The exact-arithmetic tests do not replace the proof of convergence or the all-dimensional characterization.

## Relationship to prior work

Pan, Nieto-Barajas and Craiu first publicly posted the **bivariate** four-rotation construction on 19 March 2024 (arXiv:2403.12789v1); their **multivariate** \(2^m\)-rotation extension appeared in version 3 on 10 February 2025. Version 3 defines an all-other-extremes conditional tail coefficient but also gives a linear component-mixture expression for it. The linear expression cannot in general describe these conditional probabilities: in dimension three with uniform rotation weights and \(\theta=1\), that expression gives \(1/12\), whereas the defining conditional probability has limit \(1/3\), by the numerator and denominator expansions proved above. (Bivariate corner coefficients are different because their conditioning event is one marginal tail with probability \(t\), independent of the mixture.) The present theorem computes the correctly normalized conditional multivariate limit and characterizes the entire realizable array, including a unique inverse map and an explicit incompatible table. It does not claim to have originated the rotated-mixture construction.

Fiebig, Strokorb and Schlather, and independently Shyamalkumar and Tao, developed polyhedral realization problems for **pairwise** tail-dependence matrices. Those results concern symmetric pairwise tail coefficients, rather than the directed conditional all-other-extremes array and its cube-edge inverse map in the named parametric family. The new claim does not assert a new general tail-matrix or binary correlation polytope theorem.

## Limitations

The statement is a population-level exact characterization, not a finite-sample statistical consistency or efficiency theorem. Estimation of conditional probabilities at rare extreme events may be unstable, especially as \(\theta\downarrow0\) or some weights approach zero. The formula and recovery proof do not cover dimension two, zero mixture weights, the independence parameter, mixtures with heterogeneous Clayton parameters, or arbitrary non-Clayton copulas. No claim of independent validation or exhaustive historical priority is made.

## References

1. Pan, R., Nieto-Barajas, L. E. and Craiu, R., *Bivariate temporal dependence via mixtures of rotated copulas*, arXiv:2403.12789v1, posted 19 March 2024. https://arxiv.org/html/2403.12789v1
2. Pan, R., Nieto-Barajas, L. E. and Craiu, R., *Multivariate temporal dependence via mixtures of rotated copulas*, arXiv:2403.12789v3, multivariate revision posted 10 February 2025. https://arxiv.org/html/2403.12789v3
3. Fiebig, U.-R., Strokorb, K. and Schlather, M., *The realization problem for tail correlation functions*, arXiv:1405.6876; *Extremes* 20 (2017), 121–168. https://arxiv.org/abs/1405.6876
4. Shyamalkumar, N. D. and Tao, S., *On tail dependence matrices: The realization problem for parametric families*, arXiv:1901.02157. https://arxiv.org/abs/1901.02157
5. Nelsen, R. B., *An Introduction to Copulas*, 2nd ed., Springer, 2006 (standard definitions and Clayton family).
