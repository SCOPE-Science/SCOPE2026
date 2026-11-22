# Score-polarized rare exceptions to universal kingship in fair random tournaments

## Finding

Independently orient every edge of the complete labeled graph on \(n\ge3\) vertices fairly. Write \(d(v)\) for its outdegree and say that \(x\) *covers* \(y\) if \(x\to y\) and \(y\to z\) implies \(x\to z\) for every other vertex \(z\). Let \(F_n\) be the event that at least one covering pair exists, equivalently that the uncovered set is not the full vertex set. On \(F_n\), choose the unique covering pair \((X_n,Y_n)\) if it exists; if multiple exist, make any deterministic choice among them.

**Marked rare-exception theorem.** Conditional on \(F_n\), the selected pair is unique with probability \(1-O(n(5/6)^n+n^2(3/4)^n)\). Define, for each remaining vertex \(z\), its two-bit win pattern \((\mathbf1\{X_n\to z\},\mathbf1\{Y_n\to z\})\). The total-variation distance between the conditional joint law of the selected ordered pair and its complete \(n-2\) pattern array and the reference experiment below is
\[
 O\!\left(n(5/6)^n+n^2(3/4)^n\right).
\]
In the reference experiment, the ordered pair is uniformly distributed over all \(n(n-1)\) distinct labels and the remaining vertices independently receive the three patterns \((1,1),(1,0),(0,0)\), each with probability \(1/3\). In particular, for the reference law, letting \((A,B,C)\) count these three patterns,
\[
 (A,B,C)\sim\operatorname{Multinomial}(n-2;1/3,1/3,1/3),\quad
 (d(X_n),d(Y_n))=(1+A+B,A).
\]
Consequently, conditional on \(F_n\),
\[
 \left(\frac{d(X_n)}n,\frac{d(Y_n)}n\right)\xrightarrow{\mathbb P}(2/3,1/3),
\]
and
\[
 \sqrt n\left(\frac{d(X_n)}n-\frac23,\frac{d(Y_n)}n-\frac13\right)
 \xrightarrow{d}N_2\!\left(0,\frac19\begin{pmatrix}2&1\\1&2\end{pmatrix}\right).
\]
With conditional probability tending to one, \(X_n\) is the **unique maximum-outdegree vertex**, \(Y_n\) is the **unique minimum-outdegree vertex**, and \(Y_n\) is the **only vertex outside the uncovered set**. Thus a rare failure of universal kingship is, asymptotically, identifiable from the two extreme scores alone.

## Assumptions and scope

The graph is a *strict tournament*: every pair has exactly one orientation, independently with probabilities \(1/2,1/2\). All limits refer to integer \(n\to\infty\); the conditional assertions require \(F_n\), which has positive probability for every \(n\ge3\). Labels remain fixed; exchangeability permits uniform selection of the unique exceptional ordered pair. The total-variation statement concerns the entire marked orientation array, not just finitely many marginal coordinates. The finite-sample reference multinomial law is exact only when conditioning on a **specified** covering pair, not on the existence of some pair; the error term explicitly accounts for this distinction.

## Proof

**Fixed-pair conditional law.** For distinct fixed vertices \(x,y\), let \(E_{xy}\) be the covering event. It requires \(x\to y\). Independently for each other \(z\), the edge pattern \((\mathbf1\{x\to z\},\mathbf1\{y\to z\})\) is uniform over all four binary pairs before conditioning. The forbidden pattern is \((0,1)\). Therefore
\[
 p_n:=\Pr(E_{xy})=\tfrac12(3/4)^{n-2}.
\]
Conditioning on \(E_{xy}\) leaves all \(n-2\) allowed patterns independent and equiprobable, while all edges with neither endpoint \(x\) nor \(y\) remain independent fair orientations. The displayed multinomial score formula follows directly.

**Rare-event change of measure.** Let \(W_n=\sum_{x\ne y}\mathbf1_{E_{xy}}\), \(\mu_n=\mathbb EW_n=n(n-1)p_n\), and \(S_{2,n}=\sum_{\{(x,y),(u,v)\}}\Pr(E_{xy}\cap E_{uv})\), the sum over unordered distinct covering-event pairs. Classify them by the number and roles of shared endpoints. Two events sharing a coverer or a covered vertex have intersection probability \(\frac14(5/8)^{n-3}\): the common endpoint imposes two implications, satisfied by five of eight local edge patterns. Two chain-linked events have probability at most \((1/2)^{n-3}\) (indeed the consistent chain has an additional constant factor), opposite events are incompatible, and two events with four distinct endpoints have intersection probability at most \((9/16)^{n-4}\). Counting each class yields, for an absolute constant \(K\),
\[
 S_{2,n}\le K\{n^3(5/8)^{n-3}+n^3(1/2)^{n-3}+n^4(9/16)^{n-4}\},
\quad\frac{S_{2,n}}{\mu_n}=O\!\left(n(5/6)^n+n^2(3/4)^n\right)=:\varepsilon_n.
\]
The first two Bonferroni inequalities give \(\mu_n-S_{2,n}\le\Pr(F_n)\le\mu_n\) and \(\Pr(W_n\ge2)\le S_{2,n}\). Thus the conditional multiple-pair probability is \(O(\varepsilon_n)\).

To compare complete marked laws, first choose \((x,y)\) uniformly and then sample the tournament conditional on \(E_{xy}\). Call the resulting marked experiment \(Q_n\). Its unmarked tournament distribution size-biases the original tournament by \(W_n\): \(Q_n(T)=\Pr(T)W_n(T)/\mu_n\). Compare this with the original tournament conditioned on \(F_n\) and marked by its unique covering pair whenever \(W_n=1\). On the common support \(W_n=1\), the two marked measures have proportional weights \(\Pr(T)/\mu_n\) and \(\Pr(T)/\Pr(F_n)\); off that support their total masses are each at most a constant times \(S_{2,n}/\mu_n\). Therefore the marked total-variation distance is \(O(\varepsilon_n)\). By the first paragraph, \(Q_n\) has precisely the claimed uniform-pair/independent-pattern law.

**Scores and exceptional set.** Under \(Q_n\), the pair scores are sums of iid three-valued observations, giving the displayed means, law of large numbers and bivariate central limit theorem with covariance entries \(2/9,1/9,2/9\). For each other vertex \(z\), its score is an independent \(\operatorname{Binomial}(n-3,1/2)\) contribution from the other nonexceptional vertices plus at most two wins against the marked pair. Hoeffding's inequality and a union bound give a constant \(c>0\) such that, with \(Q_n\)-probability at least \(1-O(ne^{-cn})\), the marked upper score exceeds \(5n/8\), the marked lower score is below \(3n/8\), and every other score lies strictly between \(7n/16\) and \(9n/16\), once \(n\) is sufficiently large. Therefore the marked coverer and covered vertex are the unique global degree maximizer and minimizer. A tournament vertex is not a king (not in the uncovered set) exactly when some other vertex covers it. On the event \(W_n=1\), only \(Y_n\) is covered. Transferring via the total-variation bound completes the proof.

## Verification

Running `python3 verify.py` checks all labeled fair tournaments for sizes \(3,4,5,6\) using exact integer counts and rational probabilities. It checks the fixed-pair covering probability, every admissible two-bit word's conditional uniform probability, and the full finite bivariate score law. The code passed 222 exact assertions. These finite computations do not certify the asymptotic bounds or the central limit theorem; those follow from the analytic counting, change-of-measure and concentration steps above.

## Relationship to prior work

Fey's *Choosing from a Large Tournament* (publicly released on 12 October 2007) established that the uncovered set and related tournament solutions typically include all vertices; its accessible full text discusses ordinary Copeland scores, not rare-event conditional score polarization. Saile and Suksompong (2019), and Manurangsi and Suksompong (2022), study probabilities of kings in broader independent-edge models. A particularly close publicly available 2026 result, *Second-order rare-obstruction law for kings in random tournaments*, already proves the leading and second-order probability of the existence of a covering pair and describes multiplicities of rare covering events. **Those prevalence and obstruction-multiplicity statements are credited and are not claimed as new.** They do not state the marked total-variation law, joint Gaussian score profile, or recovery of the exceptional pair by extreme outdegrees, which are the present claim. Conditional on one specified pair, the three-pattern calculation is elementary and is explicitly identified as a proof ingredient, not an independently novel theorem.

## Limitations

The theorem covers only fair, independent orientations. It is an asymptotic conditional statement: for small tournaments, a unique covering pair need not have extremal outdegrees. The stated error is an exponential upper bound, not a proved optimal constant or exact finite conditional law when conditioning on existence. Novelty was assessed against the inspected accessible literature and a close published result; it is not a certified claim of historical priority. The result involves no independently performed mathematical audit.

## References

1. M. Fey, *Choosing from a large tournament*, Social Choice and Welfare 31 (2008), 301–309. First online publication 12 October 2007. DOI: https://doi.org/10.1007/s00355-007-0279-3 ; author-hosted full text: https://www.rochester.edu/college/faculty/markfey/papers/TourneyWeb.pdf .
2. C. Saile and W. Suksompong, *Robust bounds on choosing from large tournaments*, Social Choice and Welfare (2019). https://doi.org/10.1007/s00355-019-01213-6 .
3. P. Manurangsi and W. Suksompong, *Generalized kings and single-elimination winners in random tournaments*, Autonomous Agents and Multi-Agent Systems 36 (2022). https://doi.org/10.1007/s10458-022-09557-7 .
4. *Second-order rare-obstruction law for kings in random tournaments*, published mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-second-order-rare-obstruction-law-for-kings-in-random-tournament--cd69f9872e0a .
