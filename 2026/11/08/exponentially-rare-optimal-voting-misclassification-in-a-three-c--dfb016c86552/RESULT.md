# Exponentially rare optimal voting misclassification in a three-class flip game

## Finding

Consider the three-class simple voting game \(\widetilde G_m\) introduced by Einy and Haimanko, with \(m\geq5\) interchangeable voters in each of three classes. Its winning rule is a near-quota flip of weights \(20,15,12\), as defined below. Let \(\delta(\widetilde G_m)\) be the smallest fraction of coalitions incorrectly classified by **any** nonnegative weighted-majority rule with an arbitrary real quota. Then for every integer \(m\geq9\),

\[
\frac{\binom{m}{3}}{20\,2^{3m}}\ \leq\ \delta(\widetilde G_m)\ \leq\ \frac{\binom{m}{3}}{2^{3m}}.
\]

The upper bound is attained exactly by the minimum-error rule **among rules with equal weights within each class**. In particular,

\[
\delta(\widetilde G_m)=\Theta\!\left(\frac{m^3}{8^m}\right),\qquad
\lim_{m\to\infty}-\frac{\log_2\delta(\widetilde G_m)}{m}=3.
\]

The original paper independently establishes \(\varepsilon^*(\widetilde G_m)=1/(47m)>0\) for a *different* normalization-based measure of distance from weightedness. Our assertion is about the **asymptotically tight exponential order of the minimum coalition misclassification probability**, not about that previously known value of \(\varepsilon^*\). We do not determine the leading constant for unrestricted (possibly asymmetric) weighted-majority rules.

## Assumptions and scope

Fix an integer \(m\geq5\) and disjoint classes \(N_1,N_2,N_3\) of cardinality \(m\). For each coalition \(S\), let \(a=|S\cap N_1|\), \(b=|S\cap N_2|\), \(c=|S\cap N_3|\), and let

\[
H(S)=20a+15b+12c.
\]

A coalition is winning if and only if \(H(S)=59\) or \(H(S)\geq61\); otherwise it is losing. This is the original three-class flip game in Definition 17 of [1], with its quota convention from Definition 15. Define

\[
\delta(\widetilde G_m)=2^{-3m}\min_{w_i\geq0,\,q\in\mathbb R}
\left|\left\{S\subseteq N: \mathbf1\{\sum_{i\in S}w_i\geq q\}\ne\mathbf1\{S\text{ wins}\}\right\}\right|.
\]

The **class-symmetric** version restricts \(w_i\) to be constant on each of \(N_1,N_2,N_3\). All counting is over the \(2^{3m}\) labeled coalitions, each equally likely. The lower bound concerns every nonnegative weight vector, including those that break all class symmetries.

## Proof

**1. The four critical profiles.** The Diophantine equations \(20a+15b+12c=59\) and \(20a+15b+12c=60\) have, respectively, exactly the solutions

\[
\mathcal A=(1,1,2)\quad\text{(winning)},\qquad
\mathcal B_1=(3,0,0),\quad\mathcal B_2=(0,4,0),\quad\mathcal B_3=(0,0,5)\quad\text{(losing)}.
\]

Their labeled coalition multiplicities are

\[
M=m^2\binom m2,\qquad B_1=\binom m3,\qquad B_2=\binom m4,\qquad B_3=\binom m5.
\]

**2. Upper bound and exact class-symmetric optimum.** Consider the class-symmetric rule assigning per-voter weights \((22,15,12)\) and declaring a coalition winning at total weight at least \(60.5\). Write \(H'=H+2a\). Every original winner with \(H\geq61\) remains winning because \(H'\geq61\), and the exceptional winning profile \(\mathcal A\) has \(H'=61\). Of the three losing profiles of weight \(60\), exactly \(\mathcal B_1\) is incorrectly accepted: their new totals are \(66,60,60\).

For an original loser with \(H\leq58\), if \(a=0\) then \(H'\leq58\). If \(a=1\), the maximal achievable original total not exceeding \(58\) is \(56\), so \(H'\leq58\). If \(a=2\), that maximal original total is \(55\), so \(H'\leq59\). There cannot be \(a\geq3\) with \(H\leq58\). Hence all these coalitions remain losing. The rule therefore makes **exactly** \(\binom m3\) errors for every \(m\geq5\).

To show that it minimizes errors within class-symmetric rules when \(m\geq9\), write their class weights as \(u,v,z\geq0\). Correctly classifying all four critical profiles would require

\[
u+v+2z\geq q,\qquad 3u<q,\quad4v<q,\quad5z<q.
\]

If \(q\leq0\), all \(\mathcal B_1\)-coalitions are wrongly accepted. If \(q>0\), the last three inequalities instead imply

\[
u+v+2z<\left(\frac13+\frac14+\frac25\right)q=\frac{59}{60}q<q,
\]

contradicting the first. Thus at least one entire critical profile must be mislabeled. For \(m\geq9\), its multiplicity is at least \(B_1\). Combined with the preceding construction, this proves the exact class-symmetric minimum \(B_1\).

**3. A balanced multiset obstruction for unrestricted weights.** Choose five distinct voters in each class and label them \(0,1,2,3,4\) within that class. Construct a multiset of **60 winning coalitions** indexed by \(t=0,\ldots,59\), each containing the class-1 voter \(t\bmod5\), the class-2 voter \(t\bmod5\), and the class-3 voters \(t\bmod5\) and \((t+1)\bmod5\). Each winning coalition has profile \(\mathcal A\). Every selected class-1 or class-2 voter occurs exactly 12 times and every selected class-3 voter exactly 24 times.

Construct a multiset of **59 losing coalitions** by taking each of the ten triples of the five class-1 voters twice (20 coalitions), each of the five quadruples of the class-2 voters three times (15 coalitions), and the entire chosen class-3 quintuple 24 times. These have respective profiles \(\mathcal B_1,\mathcal B_2,\mathcal B_3\). Each class-1 and class-2 voter occurs exactly 12 times and each class-3 voter occurs exactly 24 times. Therefore the total incidence vector is identical in the winning and losing multisets.

Take an arbitrary candidate weighted-majority rule with nonnegative voter weights and quota \(q>0\). If it classified all 119 displayed occurrences correctly, the sum of winning-coalition rule weights would be at least \(60q\), whereas the sum of losing-coalition rule weights would be strictly less than \(59q\). These sums are actually equal by incidence balance, giving a contradiction. Thus **every relabeling of this balanced multiset has at least one wrongly classified occurrence**.

Choose a uniformly random injection of the five labels into each of the \(m\)-voter classes, independently across classes. Let \(e_A,e_1,e_2,e_3\) denote the numbers of erroneous labeled coalitions of the four critical profiles. By permutation symmetry each occurrence is uniformly distributed among all coalitions of its profile. The expected number of erroneous occurrences is therefore

\[
60\frac{e_A}{M}+20\frac{e_1}{B_1}+15\frac{e_2}{B_2}+24\frac{e_3}{B_3}\geq1.
\]

For every integer \(m\geq9\), the four coefficients \(60/M,20/B_1,15/B_2,24/B_3\) are each no greater than \(20/B_1\). Consequently, the total number \(e\) of misclassified coalitions satisfies

\[
1\leq\frac{20}{B_1}(e_A+e_1+e_2+e_3)\leq\frac{20e}{B_1},
\qquad e\geq\frac{B_1}{20}.
\]

If \(q\leq0\), every \(\mathcal B_1\)-coalition is already wrongly accepted, yielding the stronger \(e\geq B_1\) without the incidence argument. This proves the lower bound for **all** weighted-majority rules.

**4. Consequence.** Since \(\binom m3=\Theta(m^3)\), the two-sided bounds give the claimed exponential-polynomial order and logarithmic rate. No enumeration of infinitely many class sizes is used in the proof.

## Verification

A standalone standard-library Python script, `check.py`, reproduces finite checks of the assertions. It verifies the 60-to-59 multiset and exact incidence balance; the 56 coalition profiles involving at most five voters; the upper classifier over 3,575,656 class profiles for class sizes 5 through 60; full labeled coalition enumeration at class sizes 5 and 6 (294,912 coalitions total); and 300 seeded randomly relabeled instances of the balanced-multiset obstruction. All checks passed. The infinite quantifiers follow from the displayed analytic arguments rather than those finite tests.

## Relationship to prior work

Einy and Haimanko [1, Definition 17 and Proposition 18, with the Appendix] introduced this **same** three-class flip game and established its \(C\)-completeness and the exact normalized weight-excess \(\varepsilon^*(\widetilde G_m)=1/(47m)\). Their Section 6 introduces the misclassification measure and proves a general \(O(m^{-1/2})\) upper bound for games with boundedly many equal-desirability classes. It does **not**, in the inspected full text, state a sharp coalition-misclassification order for their three-class example. The four critical profiles also occur in their proof of the prior \(\varepsilon^*\) result; they are not newly discovered here. The new contribution is their use to obtain the quantitative **unrestricted misclassification lower bound** via a relabeled 119-occurrence trade and the **matching exponential-polynomial upper bound** and symmetric optimum. Albareda-Sambola, Molinero and Roura [2] study related outlier measures, but the accessible bibliographic and abstract evidence does not establish this specific family-level result.

## Limitations

The exact unrestricted minimum of misclassified coalitions could differ from \(\binom m3\); the result determines its order up to a factor of 20, not its leading constant. The result treats the specific pre-existing flip-game family and uniform sampling over all labeled coalitions; it makes no general exponential claim for arbitrary \(C\)-complete games or nonuniform coalition sampling. An unrestricted literature search cannot rule out all unindexed, unpublished or inaccessible equivalent work. No independent scientific audit has been performed.

## References

[1] E. Einy and O. Haimanko, *Large player classes and approximately weighted voting*, arXiv:2610.08968v1, first submitted October 6, 2026. https://arxiv.org/abs/2610.08968 . Definitions 15, 17, 26; Propositions 18, 27; Sections 4, 6; Appendix 8.6–8.7.

[2] M. Albareda-Sambola, X. Molinero and S. Roura, *Weightedness measures from inequality systems*, International Journal of Approximate Reasoning 182 (2025), 109418, DOI:10.1016/j.ijar.2025.109418. https://doi.org/10.1016/j.ijar.2025.109418 .
