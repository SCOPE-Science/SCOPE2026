# Two reversals of infection-risk ordering under strategy-based Fermi vaccination updates

## Finding

For the strategy-based risk-assessment (SB-RA) Fermi vaccination equation of Ma, Xu and Huang [1], there exist two fixed infection risks with a **strictly increasing, positive expected individual advantage of vaccination** for which increasing risk *reduces* instantaneous vaccination growth at intermediate selection noise but *increases* it at both low and high noise. In particular, take vaccination coverage \(x=1/20\), effectiveness \(e=1/20\), vaccination cost \(c=1/20\), infected-vaccinee relative treatment cost \(p=2/3\), and infection cost normalized to one. Let the conditional infection risks be \(q_-=3/20\) and \(q_+=3/5\). With Fermi noise \(\kappa>0\), define \(G_\kappa(q)\) below and \(D(\kappa)=G_\kappa(q_-)-G_\kappa(q_+)\). Then

\[
\lim_{\kappa\downarrow0}D(\kappa)=-\frac9{400}<0,\qquad
D(1/40)>\frac{37327}{240000}>0,\qquad
\lim_{\kappa\to\infty}4\kappa D(\kappa)=-\frac{2313}{4000}<0.
\]

Consequently, there are **at least two distinct** positive values \(0<\kappa_1<1/40<\kappa_2\) at which the sign of this risk comparison vanishes. This is a statement about the instantaneous vaccination-behavior vector field at fixed coverage, **not** a statement about long-run coupled epidemic trajectories or uniqueness of the two zeroes.

## Assumptions and scope

Normalize the cost of infection for an unvaccinated person to \(C_I=1\). A healthy unvaccinated person pays nothing; an infected unvaccinated person pays \(1\). A vaccinated individual always pays \(c\), and if an ineffective vaccine fails to prevent infection the person also pays \(p\), with \(0<p<1\). Let \(x\in(0,1)\) be the proportion attempting vaccination, \(e\in(0,1)\) the probability of effective immunity, and \(q=h(ex)/(1-ex)\in[0,1]\) the infection probability conditional on not having effective immunity. Treat \(x\) and \(q\) as fixed coordinates when comparing noise intensities; different \(q\) values represent different feasible contemporaneous prevalence states.

Write \(\lambda=1-e\) and \(\sigma(z)=1/(1+e^{-z})\). The source model averages payoffs **by strategy over the population** (not conditional on already choosing the strategy). Its vaccination and nonvaccination averages are

\[
\Pi_V=-cx-\lambda p xq,\qquad \Pi_N=-(1-x)q.
\]

The Fermi imitation drift for the strategy-based payoff comparisons is \(\dot x=x(1-x)G_\kappa(q)\), where

\[
\begin{aligned}
G_\kappa(q)={}&(1-q)\sigma(\Pi_V/\kappa)
+q\sigma((\Pi_V+1)/\kappa)\\
&-(1-\lambda q)\sigma((\Pi_N+c)/\kappa)
-\lambda q\sigma((\Pi_N+c+p)/\kappa).
\end{aligned}
\]

The four terms arise, respectively, from healthy/infected nonvaccinees switching to vaccination and healthy/infected vaccinees switching away. Multiplication by the common strictly positive \(x(1-x)\) does not alter the risk ranking.

## Proof

**Expected private incentive.** At any conditional risk \(q\), the expected payoff from choosing vaccination is \(-c-\lambda pq\), versus \(-q\) without vaccination. Thus the private advantage is \(\Delta(q)=(1-\lambda p)q-c=(11/30)q-1/20\). It is strictly increasing in risk, with \(\Delta(q_-)=1/200\) and \(\Delta(q_+)=17/100\). Furthermore, even an infected vaccinee's treatment-plus-vaccine cost \(c+p=43/60\) is lower than an infected nonvaccinee's unit cost.

**Low-noise endpoint.** At both specified risks, \(\Pi_V<0<\Pi_V+1\) and \(\Pi_N+c<0<\Pi_N+c+p\). Therefore, taking \(\kappa\downarrow0\) in each Fermi factor gives \(G_\kappa(q)\to q-\lambda q=eq\). Consequently \(D(0+)=e(q_--q_+)=-9/400\).

**High-noise endpoint.** The Taylor expansion \(\sigma(z/\kappa)=1/2+z/(4\kappa)+O(\kappa^{-3})\) holds for every fixed finite payoff argument. Substitute the four arguments and simplify:

\[
4\kappa G_\kappa(q)\longrightarrow -c(1+x)+q[2-x-\lambda p(1+x)].
\]

For the parameters above, the coefficient of \(q\) equals \(257/200\). Hence \(4\kappa D(\kappa)\to(q_--q_+)257/200=-2313/4000\).

**Strict intermediate reversal using only rational bounds.** At \(\kappa=1/40\), the four Fermi arguments for \(q_-\) are
\[
-29/100,\quad3971/100,\quad -37/10,\quad689/30,
\]
while for \(q_+\) they are
\[
-43/50,\quad1957/50,\quad -104/5,\quad88/15.
\]

Use these elementary strict bounds: \(\sigma(-29/100)>2/5\), \(\sigma(3971/100)>99/100\), \(\sigma(-37/10)<1/40\), \(\sigma(-43/50)<1/3\), and \(\sigma(88/15)>99/100\). Every logistic value is strictly between zero and one. The five nontrivial bounds follow from \(e^{29/100}<100/71<3/2\), \(e^5>99\), \(e^{37/10}>39\), \(e^{43/50}>2\), and \(88/15>5\), respectively. The positive exponential lower bounds are certified by finite sums of the nonnegative Taylor series; the first exponential upper bound follows from \(e^z\leq1/(1-z)\) for \(0<z<1\). All rational inequalities are reproduced in `checker.py`.

Consequently,
\[
\begin{aligned}
G_{1/40}(q_-)&>\frac{17}{20}\frac25+\frac3{20}\frac{99}{100}-\frac{343}{400}\frac1{40}-\frac{57}{400}=\frac{5193}{16000},\\
G_{1/40}(q_+)&<\frac25\frac13+\frac35-\frac{57}{100}\frac{99}{100}=\frac{5071}{30000}.
\end{aligned}
\]
Thus \(D(1/40)>37327/240000>0\). Continuity in positive \(\kappa\) and the two negative endpoint limits establish at least two distinct zeroes, one on each side of \(1/40\), by the intermediate value theorem. No numerical root-finding or finite enumeration is needed for this existence proof.

## Verification

Execute `python checker.py` with Python 3.10 or later. It independently recomputes the integer-rational payoff arguments, strict Taylor-series exponential bounds, the rational gap \(37327/240000\), both analytic endpoint coefficients, all payoff-sign preconditions, and sample floating-point drifts. The checker prints `PASS` on success. Floating-point checks are corroboration only; rational bounds and the analytic limiting calculations prove the infinite statement.

## Relationship to prior work

Ma, Xu and Huang [1], published online 27 January 2026, give the age-structured epidemic and voluntary vaccination SB-RA payoff dynamics, and study vaccination cost and effectiveness largely using simulations. Their equations motivate the fixed-coverage comparison, but their reported results do not state a two-crossing dependence of the *ranking of two infection risks* on selection noise. Fukuda et al. [2] introduced strategy-based risk assessment, comparing against a population-level strategy payoff; their accessible abstract describes simulation comparisons across social network structures, not the exact statement proved here. Fu, Zhuo and Chen [3] study vaccine beliefs and payoff imitation, including hysteresis, but use a different behavioral model. Their results do not directly imply the four-term strategy-average drift inequalities above. The present novelty assessment is literature-bounded and not a priority guarantee.

## Limitations

The theorem is an explicit counterexample for a fixed instant and a fixed vaccination fraction. It does not assert that the two risk states belong to one trajectory, that the infection risks can be freely controlled by a policymaker, that exactly two crossing values exist, or that long-run vaccination coverage reverses. Neither behavioral validity in human populations nor robustness under alternative normalized payoff definitions is claimed. Earlier literature on strategy-based risk assessment, especially the complete text of [2], could contain a historical analogue not visible from accessible material. Independent priority and scientific review remain outstanding.

## References

[1] Q. Ma, J. Xu and G. Huang, *Dynamical analysis of an age-structured COVID-19 transmission model with voluntary vaccination strategies and evolutionary game*, Journal of Biological Dynamics 20 (2026), article 2620176. First public online publication: 27 January 2026. DOI: https://doi.org/10.1080/17513758.2026.2620176.

[2] E. Fukuda, S. Kokubo, J. Tanimoto, Z. Wang, A. Hagishima and N. Ikegaya, *Risk assessment for infectious disease and its impact on voluntary vaccination behavior in social networks*, Chaos, Solitons & Fractals 68 (2014), 1–9. DOI: https://doi.org/10.1016/j.chaos.2014.07.004.

[3] F. Fu, R. Zhuo and X. Chen, *Social imitation dynamics of vaccination driven by vaccine effectiveness and beliefs*, PLOS Computational Biology 21 (2025), e1013586. DOI: https://doi.org/10.1371/journal.pcbi.1013586.
