# Exact single-crossing law for one-edge delegation under two signal states

## Finding

For every odd electorate size \(n=2h+1\), \(h\ge1\), one fixed delegation from voter \(i\) to voter \(j\) has the following exact change in the probability of a correct majority decision:

\[
\Delta_h=\binom{2h-1}{h-1}\sum_{s=0}^{1}\pi_s A_s r_s^{h-1},\qquad
A_s=(1-q_s)v_s(1-u_s)-q_su_s(1-v_s),\quad r_s=q_s(1-q_s).
\]

Here \(u_s,v_s,q_s\in(0,1)\) are the state-conditional correctness probabilities of \(i\), \(j\), and each of the \(2h-1\) remaining voters, and \(\pi_s>0\), \(\pi_0+\pi_1=1\). In particular, the sign of \(\Delta_h\), as the positive integer \(h\) varies, can change **at most once**. When the two values \(r_0,r_1\) coincide, its sign is independent of population size. For fixed parameters with \(r_0>r_1\) and \(A_0\ne0\), the eventual sign agrees with \(A_0\).

The single-state condition for nonnegative gain, for any odd population size, is exactly

\[
\frac{v_s}{1-v_s}\ge\frac{u_s}{1-u_s}\frac{q_s}{1-q_s}.
\]

The one-crossing law is sharp in both directions even when the recipient is strictly more accurate than the donor in *both* states. Explicit examples are provided below.

## Assumptions and scope

The decision is binary and one alternative is objectively correct. A binary public signal \(s\in\{0,1\}\) is realized **after** the delegation decision and **before** the vote. Conditional on \(s\), individual correctness indicators are mutually independent. The donor has competence \(u_s\), the recipient competence \(v_s\), and the remaining \(2h-1\) voters are conditionally independent and identically distributed with competence \(q_s\). The signal prior is \(\Pr(s)=\pi_s\). All probabilities are strictly between zero and one; the two priors are positive.

The direct rule counts every voter's ballot with weight one. The alternative rule fixes exactly one edge \(i\to j\) before signal realization: \(i\)'s independent ballot is discarded, \(j\)'s ballot receives weight two, and all other ballots receive weight one. The resulting total weight is the odd integer \(2h+1\), so no voting ties occur. There are no other delegations or strategic responses. The population-size comparison fixes the six statewise competence parameters and the two priors while increasing the number of exchangeable background voters.

\(\Delta_h\) means the ex-ante correct-majority probability under this delegation minus the corresponding probability under direct voting. “Sign change” means a reversal between strictly positive and strictly negative values; a single zero at the transition is permitted.

## Proof

Condition on a signal state \(s\). Write \(X\) for the donor's correct-vote indicator, \(Y\) for the recipient's, and \(S\) for the total correct votes among the remaining \(2h-1\) voters. Then

\[
X\sim\operatorname{Bernoulli}(u_s),\quad
Y\sim\operatorname{Bernoulli}(v_s),\quad
S\sim\operatorname{Binomial}(2h-1,q_s),
\]

independently. Direct voting succeeds exactly when \(S+X+Y\ge h+1\), whereas delegated voting succeeds exactly when \(S+2Y\ge h+1\). If \(X=Y\), these decisions coincide. If \((X,Y)=(0,1)\), delegation changes an incorrect majority into a correct one precisely at \(S=h-1\). If \((X,Y)=(1,0)\), it changes a correct majority into an incorrect one precisely at \(S=h\). Therefore the exact conditional difference is

\[
\Delta_h^{(s)}=v_s(1-u_s)\Pr(S=h-1)-u_s(1-v_s)\Pr(S=h).
\]

The two central binomial coefficients are equal:

\[
\binom{2h-1}{h-1}=\binom{2h-1}{h}.
\]

Extracting the positive factor \(\binom{2h-1}{h-1}[q_s(1-q_s)]^{h-1}\) yields \(\Delta_h^{(s)}=\binom{2h-1}{h-1}A_s r_s^{h-1}\). Averaging with weights \(\pi_0,\pi_1\) proves the displayed formula. Since all odds denominators are positive, \(A_s\ge0\) is equivalent to the stated odds inequality.

For the crossing assertion, divide by the strictly positive factor \(\binom{2h-1}{h-1}r_0^{h-1}\). If \(r_0=r_1\), the remaining expression is \(\pi_0A_0+\pi_1A_1\), independent of \(h\). If \(r_0>r_1\), it is

\[
B_h=\pi_0A_0+\pi_1A_1\left(\frac{r_1}{r_0}\right)^{h-1}.
\]

The power of \(r_1/r_0\in(0,1)\) is strictly decreasing, and hence \(B_h\) is monotone (strictly unless \(A_1=0\)). A monotone real sequence cannot change sign twice. If \(r_1>r_0\), exchange the two labels. The limiting assertion follows as the smaller-base term vanishes, and the zero-coefficient boundary cases follow directly from the same formula.

**Witness: harmful to helpful.** Set \(\pi_0=\pi_1=1/2\), \(q_0=3/5\), \(q_1=9/10\), and

\[
(u_0,v_0)=(3/5,3/4),\qquad (u_1,v_1)=(3/5,7/10).
\]

Then \(A_0=3/100>0\), \(A_1=-67/500<0\), and \(r_0/r_1=8/3\). The exact comparison is \((8/3)^{h-1}>67/15\); it fails at \(h=1,2\) and holds at every \(h\ge3\). Consequently \(\Delta_1=-13/250\), \(\Delta_2=-729/100000\), and \(\Delta_3=3213/1000000\); the edge is harmful at populations three and five but beneficial for all odd populations from seven onward.

**Witness: helpful to harmful.** Keep the same priors, background probabilities, and donor competences, but take

\[
(u_0,v_0)=(3/5,13/20),\qquad (u_1,v_1)=(3/5,49/50).
\]

Now \(A_0=-11/500<0\) and \(A_1=71/2500>0\). The difference is positive at \(h=1\), with \(\Delta_1=2/625\). For every \(h\ge2\), the inequality \((3/8)^{h-1}<55/71\) proves negativity; in particular \(\Delta_2=-2043/500000\). In both witnesses, \(v_s>u_s>1/2\) in each state and \(q_s>1/2\).

## Verification

A reproducible Python 3 standard-library program, `verify.py`, computes both majority success probabilities by independent Bernoulli convolution using exact rational arithmetic and compares their difference with the displayed closed form. It checks 4,800 seeded parameter sets, 2,916 fully enumerated modest-grid cases, and the two rational witness families for odd sizes from three through seventeen. All tests agree. The finite program validates instances and formulas, but the universal crossing assertion rests on the preceding analytical proof.

## Relationship to prior work

Gilbert, Schmid, Schnell, Svoboda, and Yeo (2026) introduce the binary post-delegation common-signal model and develop asymptotic, local-mechanism, and concentration-based guarantees. Their full text includes some exact finite-size illustrations of other, many-edge constructions, but it does not state the exact one-edge homogeneous-background pivot formula or its complete odd-population sign-transition classification. Chatterjee and coauthors (2025) analyze how delegation-induced variance affects correctness across graph families. Bloembergen, Grossi, and Lackner (2018) study strategic delegation and accuracy, including simulation. Armstrong and Larson (2024) study classifier-ensemble pruning by liquid democracy, with a different empirical target and without this two-signal finite-population law. A related two-faction study uses strategic preference competition without an objectively correct alternative, so it does not imply the present epistemic result.

## Limitations

The theorem concerns a single fixed delegation, one homogeneous background competence within each of two states, a binary correct alternative, odd unweighted electorates before delegation, and independent votes conditional on the signal. It does not classify multiple delegation edges, heterogeneous background voters, even total voting weights, nonlinear aggregation, or strategic behavior. The two-state condition is sufficient for at most one size reversal; it is not asserted for three or more signal states. The literature comparison cannot rule out unindexed equivalent prior derivations; no independent external audit has been performed.

## References

1. S. Gilbert, S. Schmid, S. Schnell, J. Svoboda, and M. Yeo, *Liquid democracy under vote correlation: On the fallacies of averaging and the excluded middle*, arXiv:2608.16738, first public 2026-08-17. https://arxiv.org/abs/2608.16738
2. K. Chatterjee, S. Gilbert, S. Schmid, J. Svoboda, and M. Yeo, *When is liquid democracy possible? On the manipulation of variance*, PODC 2025. https://schmiste.github.io/podc25gov.pdf
3. D. Bloembergen, D. Grossi, and M. Lackner, *On Rational Delegations in Liquid Democracy*, arXiv:1802.08020 (2018). https://arxiv.org/abs/1802.08020
4. B. Armstrong and K. Larson, *Liquid Democracy for Low-Cost Ensemble Pruning*, arXiv:2401.17443 (2024). https://arxiv.org/abs/2401.17443
5. K. Chatterjee, S. Gilbert, S. Schmid, J. Svoboda, and M. Yeo, *Liquid Democracy With Two Opposing Factions*, IACR ePrint 2026/375. https://eprint.iacr.org/2026/375
