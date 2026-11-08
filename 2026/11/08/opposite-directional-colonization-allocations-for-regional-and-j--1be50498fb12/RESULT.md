# Opposite directional colonization allocations for regional and joint persistence

## Finding

In the four-state continuous-time occupancy model defined below, suppose both patches receive the same independent external immigration intensity \(\lambda>0\), their extinction rates are \(e_1,e_2>0\), and a fixed directed colonization-rate budget \(M>0\) is split as \(m_{12}=m\) and \(m_{21}=M-m\), with \(0\le m\le M\). Let \(m_{\mathrm R}\) uniquely maximize the stationary probability of **at least one patch occupied**, and let \(m_{\mathrm J}\) uniquely maximize the stationary probability of **both patches occupied**. Then

\[
\begin{aligned}
e_1>e_2&\implies m_{\mathrm J}<M/2<m_{\mathrm R},\\
e_1<e_2&\implies m_{\mathrm R}<M/2<m_{\mathrm J},\\
e_1=e_2&\implies m_{\mathrm J}=m_{\mathrm R}=M/2.
\end{aligned}
\]

In particular, whenever the extinction rates differ, the two long-run ecological objectives require strictly opposite biases in the allocation of the *same* colonization budget. The regional-persistence optimum is explicit:

\[
m_{\mathrm R}=\min\!\left\{M,\max\!\left\{0,\frac M2+\frac{e_1-e_2}{4}\right\}\right\}.
\]

The joint-occupancy optimum is also completely specified. Define \(\delta=e_1-e_2\), \(C=2\lambda+M+e_1+e_2\), \(h=\lambda(e_1+e_2)+e_1e_2\), \(k=\lambda(\lambda+M/2)\), and \(t=m-M/2\). Put

\[
G(t)=-\lambda\left[\delta C(h+2k)+4Ch t+4\lambda\delta t^2\right].
\]

If \(G(-M/2)\le0\), then \(m_{\mathrm J}=0\). If \(G(M/2)\ge0\), then \(m_{\mathrm J}=M\). Otherwise \(m_{\mathrm J}=M/2+t_*\), where \(t_*\) is the unique root of \(G(t)=0\) in \((-M/2,M/2)\). These alternatives are exhaustive, with coincident endpoint equalities handled by the endpoint cases.

For \((\lambda,e_1,e_2,M)=(1,2,1,4)\), the respective optima are \(m_{\mathrm R}=9/4\) and \(m_{\mathrm J}=(-41+3\sqrt{214})/2\approx1.4431082575\). The regional optimum gives stationary regional occupancy approximately \(0.7504332756\), while the joint optimum gives stationary joint occupancy approximately \(0.3803381871\). Each optimum is unique, and the other objective strictly prefers its own different choice.

## Assumptions and scope

The state is \((X_1,X_2)\in\{0,1\}^2\), where \(X_i=1\) means patch \(i\) is occupied. Each occupied patch independently becomes empty at its own constant extinction rate \(e_i\). Each empty patch independently receives successful immigrants from an external mainland at rate \(\lambda\). In addition, an occupied patch 1 colonizes an empty patch 2 at rate \(m\), and an occupied patch 2 colonizes an empty patch 1 at rate \(M-m\). Transitions occur one patch at a time, with exponential clocks, and the rates do not depend on calendar time. No migration event removes the donor population. The budget is in *effective successful-colonization rates*, not a cost with asymmetric conversion factors. External immigration makes the chain irreducible for every allowed allocation, so a unique strictly positive stationary distribution exists.

The objectives are stationary probabilities, not expected absorption times, finite-time survival probabilities, or quasi-stationary probabilities of a closed metapopulation. In particular, the empty state here is not absorbing. The labels 1 and 2 are fixed: \(m=m_{12}\) always means colonization *from* patch 1 *to* patch 2.

## Proof

Use the state ordering \(00,10,01,11\). The nonzero off-diagonal generator rates are

\[
\begin{array}{c|c}
\text{transition}&\text{rate}\\\hline
00\to10,\ 00\to01&\lambda\ \text{each}\\
10\to00&e_1\\
01\to00&e_2\\
10\to11&\lambda+m\\
01\to11&\lambda+M-m\\
11\to10&e_2\\
11\to01&e_1.
\end{array}
\]

Set \(\delta=e_1-e_2\), \(C=2\lambda+M+e_1+e_2\), \(h=\lambda(e_1+e_2)+e_1e_2\), \(k=\lambda(\lambda+M/2)\), and \(t=m-M/2\in[-M/2,M/2]\). Define

\[
D(t)=C(h+k)+\lambda\delta t-2\lambda t^2,\qquad
N(t)=Ck-\lambda\delta t-2\lambda t^2.
\]

The exact stationary masses are

\[
\begin{aligned}
\pi_{00}&=e_1e_2C/D(t),\\
\pi_{10}&=e_2\lambda(C-2t)/D(t),\\
\pi_{01}&=e_1\lambda(C+2t)/D(t),\\
\pi_{11}&=N(t)/D(t).
\end{aligned}
\]

These follow by substitution into the four generator balance equations, and the numerators sum to \(D(t)\). The algebraic balance identities are reproduced and checked as exact multivariate polynomial identities by `verify.py`; they also follow directly from the displayed rates. Since \(C\pm2t\ge C-M=2\lambda+e_1+e_2>0\), all three first numerators are positive. The remaining numerator is positive by the \(11\)-balance equation: \((e_1+e_2)N=(\lambda+m)e_2\lambda(C-2t)+(\lambda+M-m)e_1\lambda(C+2t)>0\). Thus \(D>0\) on the closed feasible interval.

Regional occupancy is

\[
R(t)=1-\pi_{00}=1-\frac{e_1e_2C}{D(t)}.
\]

It is therefore uniquely maximized where the strictly concave quadratic \(D(t)\) is maximized. Its derivative is \(D'(t)=\lambda\delta-4\lambda t\), yielding the stated projected maximizer. If \(\delta>0\), the projection lies strictly to the right of zero; if \(\delta<0\), strictly to the left; if zero, at the midpoint.

For joint occupancy, put

\[
H(t)=D(t)-N(t)=Ch+2\lambda\delta t.
\]

This is positive throughout the interval: \(h>\lambda|\delta|\) and \(C>M\), so \(H(t)\ge Ch-\lambda|\delta|M>0\). Then

\[
J(t)=\pi_{11}=1-\frac{H(t)}{D(t)},\qquad
J'(t)=\frac{G(t)}{D(t)^2},
\]

where \(G=HD'-H'D\). Direct differentiation gives

\[
G(t)=-\lambda\left[\delta C(h+2k)+4Ch t+4\lambda\delta t^2\right],
\qquad G'(t)=H(t)D''(t)=-4\lambda H(t)<0.
\]

Thus \(G\) is strictly decreasing and \(J\) has exactly one global maximizer, either an endpoint or its unique interior critical point. The displayed endpoint/root rule follows. At equal allocation,

\[
G(0)=-\lambda\delta C(h+2k).
\]

If \(e_1>e_2\), then \(G(0)<0\); strict decrease forces the unique maximum of \(J\) strictly to the left of \(t=0\). If \(e_1<e_2\), the maximum is strictly to the right. If \(e_1=e_2\), then \(G(t)=-4\lambda Ch\,t\), giving the unique maximum at the midpoint. Together with the regional result, this proves the three-case allocation theorem with no unstated large-budget or small-immigration restriction.

For the rational example, \(D=-2m^2+9m+62\), \(N=-2m^2+7m+21\), and the numerator of \(J'(m)\) is \(-4m^2-164m+245\), whose unique root in \([0,4]\) equals \((-41+3\sqrt{214})/2\). The other root is negative. This establishes the example exactly.

## Verification

Run `python3 verify.py` in any standard Python 3 environment. It requires no third-party packages. The script verifies 10 independently expressed multivariate polynomial identities for normalization, all four generator balance equations, and derivative simplifications; it then independently solves the four-state stationary linear system by rational Gaussian elimination at a finite rational parameter grid and compares it with the closed form. It also checks exact signs across symmetric and asymmetric examples and brackets the example's joint optimum using rational arithmetic. In the accompanying run, 12,514 exact assertions passed. The general inequality and uniqueness statements are proved above analytically; the finite grid does not constitute their proof.

## Relationship to prior work

Classical metapopulation literature studies the effect of local extinction, immigration and colonization on persistence. Etienne and Heesterbeek (2001) focus on changing colonization or extinction to improve mean time to metapopulation extinction in a stochastic winking-patch model, not the pair of positive stationary objectives used here. Grilli, Barabás and Allesina (2015), whose full accessible article and methods were inspected, study continuous-time extinction/colonization processes and spatial persistence thresholds in large random landscapes; their unforced finite Markov model has an absorbing empty state and the paper studies quasi-stationarity/spectral criteria rather than the directional-budget stationary allocation theorem. Westphal and collaborators (2003) consider finite-horizon, state-dependent habitat intervention via discrete-time stochastic dynamic programming. McCarthy, Thompson and Possingham (2004 online) compare mean time to extinction with extinction risk for reserve design, rather than regional versus joint stationary patch occupancy.

The present claim applies to the particular equal-external-immigration, asymmetric-extinction, constant-rate four-state model. It does not claim that the basic Markov machinery, dispersal-rescue phenomenon, or differing conservation objectives are new. Existing claims for *closed*, absorbing two-patch systems cannot imply the present stationary positive-occupancy allocation ordering without an additional argument, because their only stationary distribution places all mass on global extinction. This proof supplies that argument in an explicitly different, externally replenished model.

## Limitations

The theorem assumes independent exponential events, identical external immigration rates, only two patches, and a budget on successful colonization rates with no donor cost. If the external immigration rates differ, if colonization simultaneously harms donors, or if immigration stops, the displayed formulas and universal opposite-side conclusion do not automatically apply. Local extinction is independent of occupancy elsewhere; no catastrophic common shocks are included. The stationary objective is appropriate only when the observation horizon is long relative to mixing; the theorem does not compare finite-horizon survival or true extinction times of a closed region. It makes no empirical policy claim. The closest older journal article by Etienne and Heesterbeek could only be checked through accessible abstract material; unexamined detailed appendices and other historical literature remain a priority risk despite the claim-level comparison.

## References

- R. S. Etienne and J. A. P. Heesterbeek (2001), “Rules of Thumb for Conservation of Metapopulations Based on a Stochastic Winking-Patch Model,” *The American Naturalist* 158:389–407. DOI: https://doi.org/10.1086/321986. Accessible abstract: https://pubmed.ncbi.nlm.nih.gov/18707335/.
- J. Grilli, G. Barabás and S. Allesina (2015), “Metapopulation Persistence in Random Fragmented Landscapes,” *PLOS Computational Biology* 11:e1004251, first published 2015-05-20. Full text: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004251.
- M. I. Westphal, M. Pickett, W. M. Getz and H. P. Possingham (2003), “The Use of Stochastic Dynamic Programming in Optimal Landscape Reconstruction for Metapopulations,” *Ecological Applications* 13:543–555. DOI: https://doi.org/10.1890/1051-0761(2003)013[0543:TUOSDP]2.0.CO;2.
- M. A. McCarthy, C. J. Thompson and H. P. Possingham (2005), “Theory for Designing Nature Reserves for Single Species,” *The American Naturalist* 165:250–257, first online 2004-12-22. DOI: https://doi.org/10.1086/427297.
- D. Alonso and A. J. McKane (2002), “Extinction Dynamics in Mainland–Island Metapopulations: An N-Patch Stochastic Model,” *Bulletin of Mathematical Biology* 64:913–958. DOI: https://doi.org/10.1006/bulm.2002.0307.
