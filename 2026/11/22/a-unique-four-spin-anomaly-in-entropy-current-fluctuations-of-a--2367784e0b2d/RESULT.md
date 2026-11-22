# A unique four-spin anomaly in entropy-current fluctuations of a nonreciprocal kinetic Ising ring

## Finding

For the stationary, periodically closed continuous-time nonreciprocal kinetic Ising chain with **zero symmetric nearest-neighbor coupling**, the long-time variance rate of the pathwise entropy production has the exact all-size law

\[
\lim_{t\to\infty}\frac{\operatorname{Var}(S_t)}{t}
= N\eta^2\begin{cases}1+\delta^2/2,&N=4,\\1+\delta^2/4,&N\ge5,\end{cases}
\qquad \eta=\operatorname{artanh}(\delta).
\]

Here \(N\ge4\) is the number of sites and \(-1<\delta<1\) is the directional-bias coefficient. The corresponding mean-rate identity, already accessible from established stationary-current formulas, is

\[
\lim_{t\to\infty}\frac{\mathbb E S_t}{t}=\frac{N}{2}\delta\eta.
\]

Consequently, four sites are the **unique** ring size \(N\ge4\) at which the bias-dependent correction to the entropy-variance density is doubled. This enhancement comes from the coincidence of the two sites at displacement \(\pm2\) on a four-cycle. It is absent on all rings of at least five sites. The formula includes \(\delta=0\), where the entropy production is identically zero.

## Assumptions and scope

Let \(s=(s_0,\ldots,s_{N-1})\in\{-1,+1\}^N\), with all indices taken modulo \(N\), and \(N\ge4\). Only one spin flips at each transition, with rate

\[
 w_i(s)=\frac12\left[1-\frac{\delta}{2}s_i(s_{i-1}-s_{i+1})\right],\qquad -1<\delta<1.
\]

This is the zero-reciprocal-coupling line \(\gamma_e=0\) of the standard nearest-neighbor nonreciprocal kinetic Ising model. The rates are strictly positive, so its finite-state Markov chain is irreducible. If \(s^{(i)}\) is obtained by flipping site \(i\), define the stationary path entropy

\[
 S_t=\sum_{0<u\le t}\log\frac{\pi(s_{u-})w_{i_u}(s_{u-})}{\pi(s_u)w_{i_u}(s_u)},
\]

where \(i_u\) is the site flipped at jump time \(u\), and \(\pi(s)=2^{-N}\) is the unique stationary measure. This is dimensionless path entropy in natural logarithms; it is not an arbitrary time-symmetric activity, and the continuous-time unit is the one in the displayed rate. The asserted variance coefficient is for a stationary process and \(t\to\infty\) with fixed finite \(N\).

## Proof

**1. Stationarity and edge entropy.** Put \(T_i(s)=s_i(s_{i-1}-s_{i+1})\), which belongs to \(\{-2,0,2\}\). The reverse rate after flipping \(i\) is \(w_i(s^{(i)})=(1+\delta T_i(s)/2)/2\). Since \(\sum_i T_i(s)=0\) by cyclic telescoping, \(\sum_i[w_i(s^{(i)})-w_i(s)]=0\); hence \(\pi(s)=2^{-N}\) satisfies the forward stationary equation. Strictly positive rates imply uniqueness. The entropy of one flip is

\[
 a_i(s)=\log\frac{w_i(s)}{w_i(s^{(i)})}=-\eta T_i(s),\qquad \eta=\operatorname{artanh}(\delta).
\]

**2. The exact current eigenobservable.** Define the distance-two spin sum \(Q(s)=\sum_i s_i s_{i+2}\). The Markov generator \(Lf=\sum_i w_i(s)[f(s^{(i)})-f(s)]\) satisfies

\[
 LQ=-2Q.
\]

Indeed, each two-spin product loses its two constituent spins at total base rate two; the remaining \(\delta\)-dependent terms cancel in the cyclic sum. This identity holds even when \(N=4\), where a distance-two unordered pair occurs twice. The instantaneous entropy drift is

\[
 j(s)=\sum_i w_i(s)a_i(s)=\frac{\delta\eta}{2}[N-Q(s)],
\]

since \(\sum_iT_i=0\) and \(\sum_iT_i^2=2[N-Q(s)]\). The uniform stationary distribution has \(\mathbb E_\pi Q=0\), so \(\bar j=N\delta\eta/2\).

**3. Exact Poisson corrector.** Set \(h(s)=-\delta\eta Q(s)/4\). Then \(Lh=-(j-\bar j)\). Consequently

\[
 M_t=S_t-\bar jt+h(s_t)-h(s_0)
\]

is a square-integrable martingale with jump increment \(a_i(s)+h(s^{(i)})-h(s)\). The corrector is bounded on the finite state space; therefore \(\operatorname{Var}(S_t)/t\) and \(\operatorname{Var}(M_t)/t\) have the same limit (the cross term is bounded by a constant times \(t^{-1/2}\)). The martingale bracket and stationarity yield

\[
 \lim_{t\to\infty}\frac{\operatorname{Var}(S_t)}{t}
 =\mathbb E_\pi\sum_i w_i(s)[a_i(s)+\Delta_i h(s)]^2.
\]

**4. The unique four-cycle coincidence.** Because

\[
 \Delta_iQ=-2s_i(s_{i-2}+s_{i+2}),
\]

we obtain

\[
 a_i+\Delta_ih=\eta s_i\left[-(s_{i-1}-s_{i+1})+\frac{\delta}{2}(s_{i-2}+s_{i+2})\right].
\]

Its square does not involve \(s_i\). Conditional on all other spins under the uniform product law, averaging \(w_i\) over \(s_i\) gives \(1/2\). The cross term between \(s_{i-1}-s_{i+1}\) and \(s_{i-2}+s_{i+2}\) has zero mean for every \(N\ge4\). Moreover,

\[
 \mathbb E_\pi(s_{i-1}-s_{i+1})^2=2,\qquad
 \mathbb E_\pi(s_{i-2}+s_{i+2})^2=
 \begin{cases}4,&N=4,\\2,&N\ge5.\end{cases}
\]

The second expectation equals four exactly at \(N=4\) because \(i-2\equiv i+2\pmod4\); no other \(N\ge4\) has this coincidence. Substitution in the bracket completes the stated piecewise identity and the uniqueness assertion.

## Verification

Run `python3 checker.py` using the standard library. It evaluates the complete finite-state stationary generator, corrector identity, and rational bracket formula exactly for sizes three through nine and five values of the bias. Size three is only a consistency check and is not included in the new claim. With NumPy installed, it additionally tests the independent tilted-generator principal-eigenvalue curvature at sizes four through six. The saved run passed 132,990 exact rational assertions plus three numerical spectral comparisons. Those finite checks support but do not replace the all-size proof above.

## Relationship to prior work

The model, its master-equation rates, and its solvability were established in [1–3]. The companion treatment [1] also analyzes finite periodic chains and parity-sensitive relaxation, but not the long-time variance of stochastic path entropy. General entropy production for asymmetric kinetic Ising models and directed networks was investigated in [4–5]; these do not provide the displayed all-size continuous-time entropy-current variance formula. A previously published exact three-spin path-entropy result gives the corresponding \(N=3\) coefficient, and prior work gives the mean dissipation; neither is claimed as new here. The additional \(N=4\) variance term, and its uniqueness among all \(N\ge4\), are the new assessed assertions.

## Limitations

The formula concerns only the zero-symmetric-coupling slice and the second asymptotic cumulant. It does not give an arbitrary-temperature variance, a full tilted spectral law, or finite-time entropy distributions. The distinction from general path-fluctuation theory is the explicit all-size evaluation with an exceptional four-site correction, not the Poisson-equation method itself. Absence of a comparable formula in the inspected papers does not guarantee publication priority; broader or unindexed work could imply it.

## References

[1] G. A. Weiderpass, M. Sharma and S. Sethi, "Solving the Kinetic Ising Model with Non-Reciprocity", arXiv:2410.23615v1 (2024-10-31), https://arxiv.org/abs/2410.23615 ; Sections 2--4 and appendices (later v2 also inspected).
[2] G. Weiderpass, M. Sharma and S. Sethi, "An Exact Solution for the Kinetic Ising Model with Non-Reciprocity", arXiv:2411.00059v1 (2024-10-31), https://arxiv.org/html/2411.00059v1 .
[3] C. Godrèche, "Dynamics of the directed Ising chain", arXiv:1102.0141 (2011-02-01), https://arxiv.org/abs/1102.0141 .
[4] M. Aguilera, S. A. Moosavi and H. Shimazaki, "A unifying framework for mean-field theories of asymmetric kinetic Ising systems", Nature Communications 12, 1197 (2021), https://doi.org/10.1038/s41467-021-20890-5 .
[5] R. Nartallo-Kaluarachchi et al., "Broken detailed balance and entropy production in directed networks", Physical Review E 110, 034313 (2024), https://arxiv.org/abs/2402.19157 .
