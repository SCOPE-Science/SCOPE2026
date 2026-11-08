# A Poisson law for simultaneous adjacent-swap robustness under common matching priorities

## Finding

**Theorem.** In the complete two-sided stable-marriage market defined below, let \(X_n\) count the baseline-pivotal adjacent swaps and \(Q_n\) be the probability that the unique stable matching is unchanged after all \(n\) independent perturbations. For every integer \(n\ge2\),

\[
\mathbb E[z^{X_n}]=\prod_{k=2}^{n}\left(1+\frac{k(z-1)}{n(n-1)}\right),\qquad
Q_n=\Pr(X_n=0)=\prod_{k=2}^{n}\left(1-\frac{k}{n(n-1)}\right).
\]

The indicators that constitute \(X_n\) are **mutually independent** despite the endogenous allocation of available partners. Moreover,

\[
\mathbb E X_n=\frac{n+2}{2n},\qquad X_n\xrightarrow{d}\operatorname{Poisson}(1/2),\qquad Q_n\longrightarrow e^{-1/2}.
\]

The total-variation distance of \(X_n\) to a Poisson random variable of mean \(1/2\) is \(O(1/n)\). More precisely, for \(n\to\infty\),
\[
Q_n=e^{-1/2}\left(1-\frac{7}{6n}+O(n^{-2})\right).
\]

In particular \(Q_2=0\), \(Q_3=1/3\), and \(Q_4=5/12\). A positive limiting survival probability is possible even though **every** proposer independently changes a preference comparison.

## Assumptions and scope

There are \(n\ge2\) men and \(n\) women, with strict complete preference lists. Every woman has the same fixed strict ranking of the men, \(1\succ2\succ\cdots\succ n\). Each man's **baseline** preference order over the \(n\) women is independently uniformly sampled from all \(n!\) permutations, independent of other men. Independently for each man, choose one position uniformly from \(\{1,\ldots,n-1\}\), and transpose the women at this position and the next position in his own ranking. The women's rankings do not change. All probability statements average over original rankings and the independent swap locations.

Because all women share one strict order of men, a matching is stable if and only if it is the serial-dictatorship matching: man \(1\) obtains his highest-ranked available woman, man \(2\) his highest-ranked remaining woman, and so forth. Both baseline and perturbed markets have precisely one stable matching.

Let \(R_i\) denote the women available when man \(i\) chooses in the **baseline** serial-dictatorship sequence; its size is \(k_i=n-i+1\). A swap is called *baseline-pivotal* for man \(i\) if, holding \(R_i\) fixed, the swap changes which woman he would select from \(R_i\). Write \(I_i\in\{0,1\}\) for this event and \(X_n=\sum_{i=1}^n I_i\). This variable is **not** defined as the number of agents whose partners change in the perturbed matching.

## Proof

**Step 1: Uniqueness and the sequential matching.** Man \(1\) is preferred to all other men by every woman. If a stable matching assigned him someone other than his first choice, he and that first choice would block. Remove their pair and repeat for man \(2\) among the remaining women, inductively. This forces the unique stable matching, the priority-order serial-dictatorship allocation; the same proof applies after the men's swaps.

**Step 2: One conditional pivotal probability.** Fix any subset \(R\) of \(k\ge2\) available women and one uniform independent ranking of all \(n\) women. A swap can change the first-ranked member of \(R\) exactly when the first two members of \(R\), in the full ranking, occupy adjacent positions and that adjacent position is swapped. The set of their \(k\) full-ranking positions is a uniformly random \(k\)-subset of \(\{1,\ldots,n\}\). Its first two positions are consecutive with probability
\[
\frac{\sum_{j=1}^{n-1}\binom{n-j-1}{k-2}}{\binom nk}
=\frac{\binom{n-1}{k-1}}{\binom nk}=\frac{k}{n}.
\]
Given consecutiveness, the required adjacent-swap position is one of the \(n-1\) equally likely locations. Therefore, \(\Pr(I_i=1\mid R_i=R)=k/[n(n-1)]\). If \(k=1\), the selected woman cannot change, so this conditional probability is zero. Notice that the conditional probability does **not** depend on the identity of the women in \(R\).

**Step 3: Independence.** Expose men's original lists and swap locations in priority order. The random subset \(R_i\) depends only on previous men's original lists, and is independent of man \(i\)'s original list and swap position. As \(|R_i|=n-i+1\) deterministically, Step 2 gives
\[
\Pr(I_i=1\mid\text{all preceding lists and swaps})=
\begin{cases}\frac{n-i+1}{n(n-1)},&i<n,\\0,&i=n.\end{cases}
\]
The conditional Bernoulli probability is constant, hence by induction \(I_1,\ldots,I_n\) are mutually independent. Multiplying their generating polynomials gives the stated generating function.

**Step 4: Matching survival.** If every \(I_i=0\), both serial dictatorships choose identically at each stage by induction on priority, so their stable matchings coincide. Conversely, suppose some \(I_i=1\) and take the smallest such \(i\). Until stage \(i\), the two algorithms choose identical women; at stage \(i\), their remaining sets therefore coincide with \(R_i\), but their selections differ by the definition of \(I_i\). The matchings are consequently distinct. Thus **the matchings coincide if and only if \(X_n=0\)**, proving the product formula for \(Q_n\).

**Step 5: The limit.** The sum of Bernoulli parameters is
\[
\lambda_n=\sum_{k=2}^n\frac{k}{n(n-1)}=rac{n+2}{2n}.
\]
The sum of their squares is \(O(1/n)\), because every parameter is at most \(1/(n-1)\). The standard elementary Poisson approximation for independent Bernoulli variables gives total-variation error at most a constant multiple of this square sum relative to \(\operatorname{Poisson}(\lambda_n)\); moving its mean to \(1/2\) changes the bound by at most \(1/n\). Alternatively, take logarithms of the probability-generating function. Hence \(X_n\) converges to \(\operatorname{Poisson}(1/2)\), giving \(Q_n\to e^{-1/2}\).

For the expansion, \(\sum p_k=1/2+1/n\) and \(\sum p_k^2=1/(3n)+O(n^{-2})\); also \(\sum p_k^3=O(n^{-2})\). Thus \(\log Q_n=-1/2-7/(6n)+O(n^{-2})\) and exponentiation yields the stated refinement.

## Verification

The standalone program `check_adjacent.cpp` independently enumerates all \((n!)^n(n-1)^n\) equally likely combinations of baseline preference profiles and adjacent-swap choices for \(n=2,3,4\), calculates the baseline and perturbed serial-dictatorship matchings, and separately counts baseline-pivotal swaps. It verifies the exact all-sizes small-case product coefficients and survival event equivalence. Observed totals and unchanged outcomes are \((4,0)\), \((1728,576)\), and \((26873856,11197440)\). For \(n=4\), the pivotal count frequencies for \(0,1,2,3\) are \(11197440,11570688,3732480,373248\). The infinite-family result and Poisson limit follow from the proof, not from these finite checks.

Run with `g++ -std=c++17 -O3 -Wall -Wextra -pedantic check_adjacent.cpp -o check_adjacent && ./check_adjacent` on an ordinary C++17 compiler.

## Relationship to prior work

Gangam, Mai, Raju and Vazirani (2026) develop structural and algorithmic results for robust stable matchings under changes to one or multiple agents' preferences. They do not state the independent pivotal-event distribution or the exact probability that the stable matching survives one simultaneous random adjacent swap per proposer. Mai and Vazirani (2018) optimize robustness to a *single* selected input error rather than one independent swap by every proposer. Irving, Manlove and Scott (2008) analyze stable marriage with master preference lists, establishing the natural market restriction employed here. Their results concern structural and computational properties, rather than this distributional robustness law. These comparisons are by scientific statement and assumptions, not merely by title.

## Limitations

The proof requires a complete balanced market, a single **strict common ranking on one side**, independent uniform complete preferences on the other side, and independent uniformly chosen adjacent positions for each man. It makes no assertion for different distributional choices, correlated preferences, incomplete rankings, nonidentical women's rankings, or multiple swaps per man. \(X_n\) is the count of *baseline-pivotal swap events*, which need not equal the number of changed partnerships. Source inspection and record search cannot exclude unpublished or unindexed equivalent formulas; independent expert assessment is outstanding.

## References

1. R. R. Gangam, T. Mai, N. Raju, V. V. Vazirani, “Robust Stable Matchings: Dealing with Changes in Preferences,” arXiv:2601.07959v1, first posted January 12, 2026. https://arxiv.org/abs/2601.07959
2. T. Mai, V. V. Vazirani, “Finding Stable Matchings that are Robust to Errors in the Input,” arXiv:1804.00553, 2018. https://arxiv.org/abs/1804.00553
3. R. W. Irving, D. F. Manlove, S. Scott, “The Stable Marriage Problem with Master Preference Lists,” *Discrete Applied Mathematics* 156 (2008), 2959–2977. https://eprints.gla.ac.uk/25737/1/25737.pdf
