# The smallest identical-replacement networks with opposite rare-volunteer fixation verdicts

## Finding

Under a common anonymous independent-site mobility law, an evolutionary replacement matrix can be insufficient to predict whether a rare volunteer is more or less likely than neutral to fixate. In the model below the first such reversal occurs with \(N=3\) individuals and \(M=3\) sites. Two strictly positive site laws yield precisely the same replacement matrix but give \(\rho_C<1/3\) and \(\rho_C>1/3\), respectively, **for every** selection intensity \(0<w\le1\). With two individuals, or with three individuals and at most two sites, this phenomenon is impossible under the stated assumptions.

The two site laws, in the order of three labelled places, are
\[
p^{(A)}=(11,11,35)/57,\qquad p^{(B)}=(26,26,5)/57.
\]
In both cases the evolutionary replacement weights satisfy
\[
W_{ii}=\frac{21164}{61731},\qquad W_{ij}=\frac12\left(1-\frac{21164}{61731}\right)\quad(i\ne j).
\]
Nevertheless, a rare cooperator fixes with probability below the neutral probability \(1/3\) under \(p^{(A)}\) and above it under \(p^{(B)}\), at all admissible positive selection intensities.

## Assumptions and scope

There are \(N\ge2\) individuals and \(M\ge1\) possible interaction sites. At each interaction episode, each individual chooses site \(m\) independently with the same probability \(p_m\), where \(p_m\ge0\), \(\sum_m p_m=1\). The three-individual witness has strictly positive entries. An individual interacts with exactly those individuals occupying its chosen site. All interaction payoffs depend only on the focal strategy and the composition of this group, never on the label of the site.

The replacement matrix follows the group-normalized encounter rule: an individual alone gives itself replacement weight one, while an individual in a group of size \(g\ge2\) assigns weight \(1/(g-1)\) to each *other* group member. The weights are averaged over independent site configurations. In the BDB evolutionary update, a parent is chosen proportional to its strictly positive mean fitness, then its offspring replaces a recipient according to that parent's row of \(W\). Fitness is \(F=1-w+w\pi\), with \(0<w\le1\); the average payoff \(\pi\) is evaluated over the site distribution before updating. In the volunteer game with \(V=1\) and \(K=49/100\), every cooperator produces the common good and earns \(V-K\) even when alone; a defector earns \(V\) precisely when it shares its site with at least one cooperator, and zero otherwise. These payoffs make all required fitnesses strictly positive.

The conclusion compares the fixation probability \(\rho_C\) of a single cooperator in two defectors with the neutral probability \(1/3\). It does *not* assert that the two-sided criterion \(\rho_C>1/3>\rho_D\) holds, nor does it assert any conclusion for other games, conditional movement, or population sizes beyond the minimality statements.

## Proof

**1. Replacement matrices for three independent identical movers.** Put
\[
s_2(p)=\sum_{m=1}^{M}p_m^2,\qquad u(p)=\sum_{m=1}^{M}p_m(1-p_m)^2.
\]
The probability that a given individual is alone is \(u\), so its self-replacement weight is \(W_{ii}=u\). Since the three individuals are exchangeable and every row sums to one, each off-diagonal entry equals \((1-u)/2\). In particular, the entire replacement matrix depends only on \(u\), not separately on \(s_2\).

For a law \(p=(a,a,1-2a)\), direct expansion gives
\[
u(p)=2a-6a^3,\qquad s_2(p)=1-4a+6a^2.
\]
For \(a=11/57\) and \(b=26/57\), the relation \(a^2+ab+b^2=1/3\) yields \(u(a)=u(b)\). Explicitly,
\[
u(p^{(A)})=u(p^{(B)})=\frac{21164}{61731},\qquad
s_2(p^{(A)})=\frac{163}{361},\quad s_2(p^{(B)})=\frac{153}{361}.
\]
Thus the full replacement matrices coincide even though pairwise co-occupation probabilities differ.

**2. Exact fixation formula.** In a state with one cooperator, a defector meets that cooperator with probability \(s_2\), so the defector payoff is \(s_2\). In a state with two cooperators, the sole defector has no cooperator at its site with probability \(u\), so its payoff is \(1-u\). Every cooperator has payoff \(1-K\). Hence
\[
F_C=1-Kw,\qquad F_{D,1}=1-(1-s_2)w,\qquad F_{D,2}=1-uw.
\]
When there are \(j=1,2\) cooperators, the probability of gaining one cooperator divided into that of losing one is \(F_C/F_{D,j}\): indeed, the shared factor \(j(3-j)W_{12}\) cancels in the two BDB transitions. Solving the ordinary two-interior-state absorbing birth–death recurrence gives
\[
\rho_C=\frac{F_C^2}{F_C^2+F_{D,1}F_C+F_{D,1}F_{D,2}}.
\]
Consequently, since the denominator is positive, the sign of \(\rho_C-1/3\) is the sign of
\[
2F_C^2-F_{D,1}(F_C+F_{D,2})
=w(L+Qw),
\]
where \(a_*=1-s_2\), \(b_*=u\), and
\[
L=b_*+2a_*-3K,\qquad Q=2K^2-a_*(K+b_*).
\]
At \(K=49/100\), exact reduction gives the following rational coefficients:
\[
\begin{array}{c|cc}
&L&Q\\\hline
p^{(A)}&-186457/6173100&289772799/12380495000\\
p^{(B)}&155543/6173100&37345691/111424455000
\end{array}.
\]
For \(p^{(A)}\) one has \(L<0<Q\) and \(L+Q<0\), so \(L+Qw<0\) throughout \(0<w\le1\). For \(p^{(B)}\), both \(L\) and \(Q\) are positive. This proves the strict inequalities at *every* selection intensity in the claimed range.

**3. Minimality.** With two individuals and any number of sites, the site-sharing probability is \(s_2\) and the common self-replacement weight is \(u=1-s_2\). Thus the replacement matrix completely determines the two possible group compositions seen by any focal individual, hence all strategy-state payoffs and the BDB fixation law of *any* anonymous group-composition game. In particular, no same-matrix reversal is possible for \(N=2\).

With three individuals at one site there is only one law. At two sites, write the law as \((q,1-q)\). Its three-individual self-replacement weight is exactly \(u=q(1-q)\). Equality of \(u\) for two such laws forces equal unordered pairs of roots of \(z(1-z)=u\); hence the laws differ at most by swapping site labels. Every anonymous group-composition distribution and fixation probability then agrees. The three-individual example with three sites proves both claimed sharp minima.

## Verification

The accompanying `checker.py` uses exact rational arithmetic to enumerate all \(3^3=27\) assignments of the labelled individuals to sites. It checks both full \(3\times3\) replacement matrices against the identical matrix displayed above, the two distinct pair-collision probabilities, the symbolic coefficients \(L,Q\), the rigorous sign inequalities for the entire selection interval, and exact birth–death transition-ratio identities. The proof of the all-intensity sign is analytic; the finite tests merely verify its rational arithmetic. At \(w=1\), the exact fixation probabilities are
\[
\rho_C(p^{(A)},1)=\frac{57963001491}{175404191791}<\frac13,
\qquad\rho_C(p^{(B)},1)=\frac{378843147}{1099341247}>\frac13.
\]
Running `python checker.py` requires only the Python standard library.

## Relationship to prior work

Pires and Broom (2026) supply the general fully independent occupancy and group-normalized replacement formalism, and show how anonymous multiplayer payoffs determine fixation probabilities. Those formulas are used as the starting model here; they are not claimed as new. Their completely mixed benchmark has uniformly visited sites, whereas this result specifically allows **identical individuals but nonuniform common site probabilities**. The new structural statement is that even the *entire* replacement matrix can be observationally insufficient, with a proof of the smallest feasible population and site counts and an exact all-selection-intensity reversal.

Haq, Schimit and Broom (2025) study temperature and mean group size as predictors of fixation in specified coordinated-movement games, with a strong empirical temperature–fixation relationship in a public-goods setting. That does not cover equality of the whole replacement matrix coupled with opposite rare-volunteer invasion verdicts. Ohtsuki, Pacheco and Nowak (2007) distinguish interaction and replacement graphs, a broader conceptual reason why this phenomenon can occur, but do not provide the present sharp identical-independent-site construction and minimality statement. Pires and Broom (2024) analyze an asymptotically isolated-community limit, not these finite nonuniform common site laws. Broom, Erovenko and Rychtář (2020) discuss general multiplayer structure and limits of temperature as a predictor, but not this exact three-individual identifiability threshold.

## Limitations

The result is for a specific volunteer payoff rule and the BDB update with pre-averaged fitness. It establishes only single-cooperator fixation relative to the neutral probability; it does not prove a strict two-way selection advantage, characterize fixation times, or extend to arbitrary correlated movement. Although the structural and numerical claims follow rigorously from the stated model, exhaustive historical priority and independent validation have not been established. In particular, a general fixation formula can computationally recover any fixed finite parameter instance, so originality concerns the sharp identifiability classification and all-intensity sign separation rather than the underlying recurrence.

## References

- D. L. Pires and M. Broom (2026), *Multiplayer social dilemmas in completely mixed populations and networks of mixing communities*, Journal of Mathematical Biology 93, 51, https://doi.org/10.1007/s00285-026-02464-5 . First verified public version: 2026-10-01.
- H. Haq, P. H. T. Schimit and M. Broom (2025), *Predictors of Fixation Probability on Complete Networks Involving Multiplayer Interactions Under Coordinated Movement Systems*, https://doi.org/10.1007/s13235-025-00635-5 .
- D. L. Pires and M. Broom (2024), *The rules of multiplayer cooperation in networks of communities*, PLOS Computational Biology 20, e1012388, https://doi.org/10.1371/journal.pcbi.1012388 .
- M. Broom, I. V. Erovenko and J. Rychtář (2020), *Modelling Evolution in Structured Populations Involving Multiplayer Interactions*, https://doi.org/10.1007/s13235-020-00358-9 .
- H. Ohtsuki, J. M. Pacheco and M. A. Nowak (2007), *Evolutionary graph theory: breaking the symmetry between interaction and replacement*, https://doi.org/10.1016/j.jtbi.2007.01.024 .
