# A sharp three-class alias for paired environmental-DNA detection, and a one-ratio remedy

## Finding

A continuum of equal-effort host–parasite binary co-detection surveys need not identify which latent ecological shedding profiles go together. Within the finite equally weighted latent-class model below, one and two classes are identifiable, but three classes suffice for two distinct pairings to produce *identical full four-cell detection distributions at every positive effort*. A second continuum of paired assays at a single suitably chosen, unequal host-to-parasite effort ratio recovers the pairing uniquely for any finite number of classes.

The three-class alias is explicit. In model I, the host and parasite Poisson rates are the pairs
\[
(6,1),\quad(2,3),\quad(4,5),
\]
while in model II they are
\[
(6,3),\quad(2,5),\quad(4,1).
\]
Each pair has probability \(1/3\). In the former model, two latent classes have parasite rate exceeding host rate; in the latter, only one does. Yet every equal-effort binary detection law agrees. Changing the parasite effort to \(3/2\) times the host effort separates these two models, and in fact resolves every possible pairing of these same rate lists.

## Assumptions and scope

Let \(n\geq1\) be a *known* finite class count. A sampling site belongs to a latent class \(I\), uniform on \(\{1,\ldots,n\}\). All classes have both targets present, and there are no false positives. Class \(i\) has a positive host-DNA Poisson count rate \(a_i\) and parasite-DNA Poisson count rate \(b_{\pi(i)}\), where \(\pi\) is an unknown permutation; the two rate lists are individually pairwise distinct. Conditional on \(I=i\), the marker counts are independent, and for host effort \(t>0\) and parasite effort \(s>0\), their respective means are \(a_i t\) and \(b_{\pi(i)}s\). Only the zero-versus-positive indicators are retained. Each putative effort condition samples the same stable class mixture independently. No inference is claimed from a finite number of noisy observations or without the model assumptions.

The observation at any effort pair is the entire joint probability distribution of the two binary indicators, not merely their covariance or a single marginal. Classes are considered equivalent under simultaneous relabeling, while host and parasite markers remain named and distinguishable. Equal-effort data mean the distribution is theoretically known for *all* \(t>0\) at \(s=t\).

## Proof

**Reduction to three exponential mixtures.** Define the zero-detection transforms
\[
L_A(t)=\frac1n\sum_{i=1}^n e^{-a_i t},\qquad
L_B(s)=\frac1n\sum_{i=1}^n e^{-b_i s},\qquad
L_\pi(t,s)=\frac1n\sum_{i=1}^n e^{-a_i t-b_{\pi(i)}s}.
\]
Conditional Poisson independence yields, with \(0\) denoting no detection,
\[
\begin{aligned}
\Pr(0,0)&=L_\pi(t,s),\\
\Pr(1,0)&=L_B(s)-L_\pi(t,s),\\
\Pr(0,1)&=L_A(t)-L_\pi(t,s),\\
\Pr(1,1)&=1-L_A(t)-L_B(s)+L_\pi(t,s).
\end{aligned}
\]
Consequently, on the diagonal \(s=t\) the complete family of observed binary laws is precisely equivalent to knowledge of the three rate multisets \(\{a_i\}\), \(\{b_i\}\), and \(\{a_i+b_{\pi(i)}\}\). To justify the equivalence, a finite positive exponential mixture determines its distinct exponents and their multiplicities: order its exponents, multiply the mixture by the exponential of its smallest exponent, take \(t\to\infty\), read off the leading coefficient, subtract that component, and iterate. This also handles repeated sums through their positive multiplicities.

**One and two classes.** For one class the pairing is unique. For two classes, after recovering the two named rate multisets, there are only the identity and swapped pairings. Equality of their sum multisets would imply equality of the sums of squared paired sums; subtracting gives
\[
2(a_1-a_2)(b_1-b_2)=0.
\]
Both factors are nonzero by hypothesis. Thus the two pairings cannot be observationally equal. This proves global pairing identifiability for \(n\leq2\).

**Three-class obstruction.** Both explicit models in the Finding section have host multiset \(\{2,4,6\}\) and parasite multiset \(\{1,3,5\}\). Their paired-sum multisets are identically \(\{5,7,9\}\). The three transforms on the diagonal are therefore, in both models,
\[
\begin{aligned}
L_A(t)&=(e^{-2t}+e^{-4t}+e^{-6t})/3,\\
L_B(t)&=(e^{-t}+e^{-3t}+e^{-5t})/3,\\
L_\pi(t,t)&=(e^{-5t}+e^{-7t}+e^{-9t})/3.
\end{aligned}
\]
The displayed joint-probability identities establish identical complete binary detection data for every \(t>0\). Yet the paired sets differ, and even the number of classes in which the parasite rate exceeds the host rate differs (two versus one). Therefore the failure first becomes possible at three classes in this model family.

**An off-diagonal remedy for any finite class count.** The common-effort marginals recover both named rate lists. Consider one new survey family with \(s=ct\), for a fixed positive number \(c\), and define the finite forbidden set
\[
E=\left\{\frac{a_i-a_j}{b_k-b_\ell}>0:
   i\ne j,\ k\ne\ell\right\}.
\]
If \(c\notin E\), all \(n^2\) candidate rates \(a_i+cb_j\) are pairwise distinct. Indeed an equality involving different host and parasite indices would give a ratio in \(E\), while an equality involving only one different index is excluded by distinctness of the rate lists. The observed double-zero probability along this ray is
\[
L_\pi(t,ct)=\frac1n\sum_i e^{-(a_i+cb_{\pi(i)})t}.
\]
Finite-exponential uniqueness recovers its exponent multiset. Since each recovered exponent corresponds to exactly one ordered pair from the known candidate grid, the paired matching \(\pi\) is uniquely determined. The forbidden set is finite, so an admissible positive \(c\) always exists; this is not a claim that one finite observation suffices. For the explicit integer-rate witness, \(E=\{1/2,1,2\}\), so \(c=3/2\) works and all nine candidate sums are distinct.

## Verification

The accompanying Python 3 program `verify_alias.py` uses exact integer and rational arithmetic and no third-party packages. It verifies that the two concrete matchings yield identical three diagonal rate-multisets, enumerates all three-class matchings in the example, verifies separation on the \(3/2\) ray, checks distinctness of all nine grid sums, and tests the two-class result across a finite integer grid. These finite checks supplement, rather than establish, the unrestricted proofs above. Run `python3 verify_alias.py` in a directory containing this document and the checker.

## Relationship to prior work

Tetzlaff et al. (2024) analyze detection/non-detection and occupancy relationships of fish and a parasite in shared environmental-DNA samples. Their ecological model motivates asking whether profiles of shared host–parasite detectability are identifiable from co-detection, but the present theorem is a separate idealized latent-rate inference statement, not a conclusion about their field observations.

Griffiths and Hamza (2019/2020) establish much broader possibilities for distinct joint laws sharing given marginals and sum distributions, including continuous constructions. That work already contains the general *marginals-plus-sum ambiguity* phenomenon. The present narrower contribution is the sharp first admissible number of equally weighted, distinct positive latent rate pairs *under a two-target binary Poisson assay*, an explicit ecologically interpretable ambiguity, and a constructive off-diagonal-effort resolution. It does not claim to originate the general matching-marginals-and-sums phenomenon.

Zhang and Richardson (2024) study sharp bounds on the sum distribution of variables with given marginals, rather than this exact latent finite-permutation identification and remedy. Tahmasebi, Motahari and Maddah-Ali (2018) study identification of finite mixtures of product measures through sufficiently many observed categorical variables; their assumptions and observables do not imply the single shared-effort-ray boundary here. Classical discrete-tomography switching ambiguity is another conceptual antecedent; no new general discrete-tomography uniqueness theorem is claimed.

## Limitations

The inverse problem presupposes *known* finite equal class weights, distinct positive rates within each marker, conditional Poisson independence, no false positives, stable class membership, and exact observation of entire probability curves for all positive efforts. There is no assertion of consistent finite-sample reconstruction, robustness to changing capture probability, or empirical host–parasite causal interpretation. Known rates are not assumed initially; they are identifiable only at the idealized population-curve level. When the assumptions are relaxed, other aliases or identifiability barriers may arise. Historical priority against specialized finite discrete-tomography and co-detection results remains a residual risk; independent external audit has not been performed.

## References

1. Tetzlaff, S. J., Katz, A. D., Johnson, M. D., and Sperry, J. H. (2024). “Community ecology in a bottle: Leveraging eDNA metabarcoding data to predict occupancy of co-occurring species.” *Environmental DNA*. First published 18 June 2024. https://doi.org/10.1002/edn3.579
2. Griffiths, R., and Hamza, K. (2019/2020). “Matching marginals and sums.” https://arxiv.org/abs/1911.07209 ; published version https://doi.org/10.1214/20-ECP357
3. Zhang, R., and Richardson, T. (2024). “Bounds on the Distribution of a Sum of Two Random Variables.” https://arxiv.org/abs/2405.08806
4. Tahmasebi, B., Motahari, S. A., and Maddah-Ali, M. A. (2018). “On the Identifiability of Finite Mixtures of Finite Product Measures.” https://arxiv.org/abs/1807.05444
5. Ceko, M., Hajdu, L., and Tijdeman, R. (2023). “Error Correction for Discrete Tomography.” https://doi.org/10.3233/FI-222154
