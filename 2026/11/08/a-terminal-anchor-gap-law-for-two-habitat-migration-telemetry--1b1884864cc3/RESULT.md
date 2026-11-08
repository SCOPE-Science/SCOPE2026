# A terminal-anchor gap law for two-habitat migration telemetry

## Finding

For a symmetric continuous-time two-habitat migration process with unknown common transition rate \(\kappa>0\), require exactly \(m+1\) exact location readings at \(0=t_0<t_1<\cdots<t_m=T\), with both endpoints mandatory and \(m\ge2\) fixed. The initial state distribution is independent of \(\kappa\); optimize the scalar local Fisher information about \(\kappa\) at a specified nominal rate. Write \(u_i=4\kappa(t_i-t_{i-1})\), \(H=4\kappa T\), and
\[
f(u)=\frac{u^2}{e^u-1},\qquad
J_m(H)=\max_{u_i>0,\;\sum_{i=1}^m u_i=H}\sum_{i=1}^m f(u_i).
\]
The total Fisher information equals \(J_m(H)/(4\kappa^2)\). There is a unique \(a\in(1,2)\) satisfying \(2(1-e^{-a})=a\), approximately \(a=1.5936242600\).

**Sharp endpoint-induced dichotomy.** For all sufficiently small \(H>0\), the unique maximizer is equally spaced: \(u_i=H/m\). For each fixed \(m\ge2\), for all sufficiently large \(H\), every optimal schedule is a permutation of \(m-1\) equal short gaps \(s_H>a\) and one long gap \(B_H=H-(m-1)s_H\). The short gap is the unique root near \(a\) of
\[
f'(s_H)=f'\bigl(H-(m-1)s_H\bigr).
\]
In particular, with \(R_H=H-(m-1)a\),
\[
 s_H-a\sim \frac{-R_H^2e^{-R_H}}{f''(a)},\qquad
 f''(a)=\frac{2(1-a)(2-a)}a<0,
\]
\[
 J_m(H)=(m-1)f(a)+R_H^2e^{-R_H}(1+o(1)).
\]
Equal spacing instead provides \(J_m^{\rm eq}(H)=mf(H/m)\), so
\[
\frac{J_m(H)}{J_m^{\rm eq}(H)}\sim
\frac{m(m-1)f(a)}{H^2}e^{H/m}.
\]
Thus the gain in information over compulsory-endpoint equal spacing grows exponentially as the deployment horizon increases at fixed observation budget.

**Finite exact witness.** At \(\kappa=1\), \(T=2\), and \(m=2\), equal unit gaps give information \(8/(e^4-1)\), while gaps \((1/2,3/2)\) give \(1/(e^2-1)+9/(e^6-1)\), which is strictly larger; the ratio is approximately \(1.198467\). The comparison follows from the exact factorization in the proof, without relying on rounding.

## Assumptions and scope

The process has generator
\[
Q_\kappa=\kappa\begin{pmatrix}-1&1\\1&-1\end{pmatrix}.
\]
The two habitats are observed without state misclassification. The sample size \(m+1\) and terminal time \(T\) are fixed, with exactly one reading at each endpoint and strict temporal ordering. Designs are chosen in advance and optimized *locally* at a nominal \(\kappa\), not adaptively or robustly across unknown parameter values. There are no travel, battery-discharge, missing-fix or reading-error effects. The initial distribution does not carry information about \(\kappa\). Every assertion about sufficiently large or small \(H\) means: for each fixed integer \(m\ge2\), a finite threshold exists, with no explicit globally sharp threshold claimed. The elementary limiting maximum \(f(a)\) for unconstrained single gaps is prior mathematics and is not claimed as new.

## Proof

**Step 1 — exact information.** A time interval \(\Delta>0\) preserves the habitat with probability \((1+e^{-2\kappa\Delta})/2\) and flips it with probability \((1-e^{-2\kappa\Delta})/2\). The flip indicator has a Bernoulli law independent of the preceding habitat; successive flip indicators are independent (their conditional laws do not depend on previous states). Its one-gap Fisher information is
\[
\frac{4\Delta^2 e^{-4\kappa\Delta}}{1-e^{-4\kappa\Delta}}
=\frac{4\Delta^2}{e^{4\kappa\Delta}-1}
=\frac{f(4\kappa\Delta)}{4\kappa^2}.
\]
Independence of flip events and the parameter-free initial distribution make total information the sum of these terms.

**Step 2 — shape of the one-gap objective.** Extend \(f(0)=0\) continuously. Its expansion is \(f(u)=u-u^2/2+O(u^3)\), hence \(f'(0)=1\), \(f''(0)=-1\). For \(u>0\),
\[
f'(u)=\frac{u[2(e^u-1)-u e^u]}{(e^u-1)^2}.
\]
The sign is that of \(g(u)=2(1-e^{-u})-u\). Because \(g(0)=0\), \(g'(u)=2e^{-u}-1\), \(g(1)>0\), and \(g(2)<0\), exactly one positive root \(a\in(1,2)\) exists. Consequently \(f\) strictly increases to its unique global maximum \(f(a)>0\), then strictly decreases to zero. Differentiating at the root and using \(e^a=2/(2-a)\) gives \(f''(a)=2(1-a)(2-a)/a<0\). Additionally,
\[
1-f'(u)=\frac{(e^u-1-u)^2+u^2(e^u-1)}{(e^u-1)^2}>0\quad(u>0).
\]
This inequality shows that any maximizer on the closed simplex has all gaps strictly positive: shifting a small amount from a positive gap into a zero gap improves the objective. Thus the stated strict-inequality maximum is attained. Since \(f''<0\) on a short interval starting at zero, strict Jensen concavity gives the unique equal-gap optimum for sufficiently small \(H\).

**Step 3 — all large-horizon maximizers have exactly one long gap.** Fix \(m\ge2\) and let \(H\to\infty\). At least one gap of any maximizing vector is at least \(H/m\), so that contribution tends to zero. Therefore \(\limsup J_m(H)\le(m-1)f(a)\). Conversely, placing \(m-1\) gaps at \(a\) and the final gap at \(R_H=H-(m-1)a\) gives \(J_m(H)\ge(m-1)f(a)+f(R_H)\); hence \(J_m(H)\to(m-1)f(a)\). For any sequence of maximizing vectors, pass to a subsequence and reorder to put the largest gap first. If two gaps diverged, the limiting objective would be at most \((m-2)f(a)\), a contradiction. If any one of the remaining bounded gaps failed to tend to \(a\), strict uniqueness of the maximizer of \(f\) would again keep the limit below \((m-1)f(a)\). Therefore, uniformly over all maximizers, exactly one gap tends to infinity and all remaining gaps tend to \(a\).

**Step 4 — exact short-gap equality and unique branch.** At every interior maximum, Lagrange multipliers give a common value of \(f'(u_i)\). Because \(f''(a)<0\), \(f'\) is strictly decreasing in a fixed neighborhood of \(a\). By Step 3, for all sufficiently large \(H\), all \(m-1\) short gaps lie in that neighborhood and hence are exactly equal, say to \(s_H\). The remaining gap is \(B_H=H-(m-1)s_H\). Since \(B_H>a\), \(f'(B_H)<0\), which forces \(s_H>a\). The scalar equation in the statement holds. For a fixed sufficiently small \(\varepsilon>0\), on \([a,a+\varepsilon]\) its left-minus-right derivative is
\[
f''(s)+(m-1)f''(H-(m-1)s)<0
\]
for all sufficiently large \(H\), because \(f''(s)\) is uniformly negative and the second derivative at the long argument tends to zero. Its value is positive at \(s=a\) and negative at \(s=a+\varepsilon\), so exactly one root exists in this neighborhood. Every global maximizer must be one of its \(m\) permutations; existence from Step 3 then proves these permutations are exactly all the global maximizers.

**Step 5 — sharp asymptotics.** The explicit formula for \(f'\) gives \(f'(u)=-u^2e^{-u}(1+o(1))\) as \(u\to\infty\); also \(f(u)=u^2e^{-u}(1+o(1))\). With \(\delta_H=s_H-a\to0\) and \(B_H=R_H-(m-1)\delta_H\), the equal-slope equation and Taylor expansion yield
\[
f''(a)\delta_H(1+o(1))=-R_H^2e^{-R_H}(1+o(1)).
\]
The shift of \(m-1\) short terms changes their total value by \(O(\delta_H^2)\); the change from \(f(R_H)\) to \(f(B_H)\) is \(O(R_H^2e^{-R_H}\delta_H)\). Both are \(O(R_H^4e^{-2R_H})=o(R_H^2e^{-R_H})\). This establishes the asserted expansion for \(J_m(H)\). Finally \(mf(H/m)\sim(H^2/m)e^{-H/m}\), giving the information ratio.

**Step 6 — exact strict finite witness.** Set \(z=e^2\). The unequal-minus-equal information is
\[
\frac1{z-1}+\frac9{z^3-1}-\frac8{z^2-1}
=\frac{z^2-5z-2}{(z+1)(z^2+z+1)}.
\]
The numerator is positive for \(z\ge7\), while \(e^2>1+2+2+4/3+2/3=7\) by the positive exponential Taylor-series tail. All denominators are positive.

## Verification

Run `python3 verify.py` with only the Python standard library. It independently checks the Bernoulli-information identity, the exact polynomial witness, the unique one-gap optimum, the small-horizon concavity regime, the one-long-gap critical equation, asymptotic approach and the relative-efficiency law. Tests include rational arithmetic and numerical stress samples. They corroborate the derivations; they do not replace the all-\(H\) analysis.

## Relationship to prior work

Cook, Gibson and Gilligan (first published 28 November 2007) introduced information-based selection of observation times for stochastic epidemic experiments. Pagendam and Ross (2011) studied optimal GPS schedules for migration on habitat networks, with a three-parameter model and battery-power constraints; the present two-habitat exact-rate specialization is within that broader ecological motivation but employs a distinct compulsory-terminal-time and fixed-number-of-intervals constraint. Parker, Gilmour and Schormans (2011) established general Fisher-information additivity and order invariance of sampled Markov gaps and gave irregular schedules in discrete-state packet-buffer systems; these properties are not new here. Michel (2018) already derived the local best *single repeated interval* for precisely the symmetric two-state CTMC, and its optimum is the \(a/(4\kappa)\) used above; that component is explicitly not new. The additional result is a theorem for **all** fixed budgets \(m\ge2\) in the opposite limit of **growing compulsory terminal horizon**: the unique asymptotic one-long-gap arrangement, its exact short-gap correction and an exponential relative-information law. No earlier equivalent theorem was established in the inspected material, but historical priority is not independently certified.

## Limitations

The rate is unknown in applications, so the stated optimum is locally parameter-dependent. A priori estimation uncertainty, noisy states, multiple independent individuals, adaptive schedules, changing habitat-specific rates, costs of readings and moving endpoints are excluded. Inferences about actual animal tracking effectiveness beyond this observation model would require further validation. A 2013 article by Pagendam and Ross on GPS transmitters was located but its full text could not be inspected because institutional access was unavailable, leaving a residual risk of historical overlap. The main large-\(H\) theorem is asymptotic and does not assert a sharp finite transition point.

## References

- Cook, A. R., Gibson, G. J. and Gilligan, C. A. (2008), "Optimal Observation Times in Experimental Epidemic Processes," *Biometrics* 64, 860–868. First publicly online 2007-11-28. https://doi.org/10.1111/j.1541-0420.2007.00931.x
- Pagendam, D. E. and Ross, J. V. (2011), "Optimal GPS tracking for estimating species movements," *MODSIM 2011*, 2261–2267. https://mssanz.org.au/modsim2011/E11/pagendam.pdf
- Parker, B. M., Gilmour, S. G. and Schormans, J. A. (2011), "Design of Experiments for Categorical Repeated Measurements in Packet Communication Networks," *Technometrics* 53(4), 339–352. https://doi.org/10.1198/TECH.2011.10052
- Michel, J. (2018), "Optimal adaptive sampling for a symmetric two-state continuous time Markov chain," publicly accessible preprint. https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/6/56774/files/2017/12/optimal_sampling_design_ctmc9-1nt190d.pdf
- Pagendam, D. E. and Ross, J. V. (2013), "Optimal use of GPS transmitters for estimating species migration rates," *Ecological Modelling*. https://doi.org/10.1016/j.ecolmodel.2012.07.007 (abstract consulted; complete text unavailable).
