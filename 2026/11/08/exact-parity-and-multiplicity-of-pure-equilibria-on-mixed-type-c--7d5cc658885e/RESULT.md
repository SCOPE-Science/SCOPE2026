# Exact parity and multiplicity of pure equilibria on mixed-type complete bipartite networks

## Finding

Let \(K_{a,b}\) be the complete bipartite graph with nonempty labeled sides \(A\) and \(B\) of sizes \(a\) and \(b\). Each vertex is independently assigned one of two *fixed behavioral types*, conformist or rebel. Let \(c\) of the vertices in \(A\), and \(d\) in \(B\), be conformists; all others are rebels. Each player chooses an action in \(\{-1,+1\}\). A conformist wants to match as many neighbors as possible, and a rebel wants to mismatch as many as possible. Either action is optimal when the two yield equal utility.

Define
\[
 Z_n=\begin{cases}\binom{n}{n/2},&n\text{ even},\\0,&n\text{ odd},\end{cases}
 \qquad \Delta_A=2c-a,\quad\Delta_B=2d-b.
\]
The total number of labeled pure Nash equilibria (PNEs) is exactly
\[
 \boxed{ E(a,b;c,d)=Z_aZ_b
 +\mathbf{1}_{\{\Delta_A=0\}}(2^b-Z_b)
 +\mathbf{1}_{\{\Delta_B=0\}}(2^a-Z_a)
 +2\mathbf{1}_{\{\Delta_A\Delta_B>0\}}. }
\]
The expression depends only on the two side sizes and the two conformist counts, not on the positions of the types within a side.

Three consequences hold for all positive side sizes. First, for even \(a\) and even \(b\), every assignment of types admits a PNE; the smallest possible count is \(Z_aZ_b\), attained, for example, when all of \(A\) are conformists and all of \(B\) are rebels. Second, if at least one side is odd, PNE nonexistence is equivalent to \(\Delta_A\Delta_B<0\). Third, if types are sampled independently with conformist probability \(1/2\), then
\[
 \Pr(E=0)=
 \begin{cases}
 0,&a,b\text{ both even},\\
 \tfrac12(1-Z_a/2^a)(1-Z_b/2^b),&\text{otherwise}.
 \end{cases}
\]
In particular, if both sides are odd this probability equals exactly \(1/2\), for every choice of their sizes.

## Assumptions and scope

The graph is simple, unweighted, complete bipartite, and has at least one vertex on each side. Types are fixed before actions are chosen; they may occur in arbitrary mixtures on either side. Agents simultaneously choose one of exactly two actions and are allowed to retain an action in a best-response tie (the standard weak pure-Nash convention). A conformist's utility is the count of neighbors matching her action; a rebel's utility is the count of neighbors not matching her action. There are no intrinsic action biases, stubborn players, or edge weights. Profiles are counted with the original vertex labels fixed. The random-type corollary concerns *types*, not random actions or random interaction graphs.

## Proof

Write \(s_i\in\{-1,+1\}\) for each player's action, and \(t_i=+1\) for a conformist and \(t_i=-1\) for a rebel. Put \(S_A=\sum_{i\in A}s_i\) and \(S_B=\sum_{j\in B}s_j\). Given all other actions, the difference in utility between action \(+1\) and action \(-1\) for a player in \(A\) has the sign of \(t_iS_B\); the analogous difference for a player in \(B\) has the sign of \(t_iS_A\). Hence a profile is a PNE if and only if
\[
 t_i s_iS_B\ge0\quad(i\in A),\qquad t_j s_jS_A\ge0\quad(j\in B).
\]

There are four disjoint classes, according to whether the two action sums are zero.

**Both sums zero.** Every player is indifferent, so all and only profiles with half \(+1\) actions in each side qualify. There are \(Z_aZ_b\) such labeled profiles.

**Left sum zero and right sum nonzero.** Each left action is uniquely forced to be \(s_i=t_i\operatorname{sgn}(S_B)\), and so \(S_A=\Delta_A\operatorname{sgn}(S_B)\). Thus the left sum vanishes exactly when \(\Delta_A=0\). Every right action is then a best response, and exactly \(2^b-Z_b\) right profiles have nonzero sum. This contributes \(\mathbf 1_{\{\Delta_A=0\}}(2^b-Z_b)\).

**Right sum zero and left sum nonzero.** The symmetric argument contributes \(\mathbf 1_{\{\Delta_B=0\}}(2^a-Z_a)\).

**Both sums nonzero.** Both sides' actions are forced. Their action sums satisfy
\[
 S_A=\Delta_A\operatorname{sgn}(S_B),\qquad
 S_B=\Delta_B\operatorname{sgn}(S_A).
\]
Two compatible choices of the two signs exist exactly when \(\Delta_A\Delta_B>0\), yielding two action profiles, related by global action reversal. Otherwise there is none. The four disjoint contributions give the displayed formula.

If both sizes are even, the first contribution is positive, and taking \(\Delta_A\Delta_B<0\) with both imbalances nonzero removes all other contributions; the lower bound is sharp. If at least one side size is odd, the double-zero contribution disappears. When \(\Delta_A\Delta_B=0\), at least one nonzero single-zero contribution exists because the other part has positive size, proving the stated zero-count criterion. When the product is positive there are precisely two nonzero-sum profiles; when negative none.

For random types, \(c\sim\operatorname{Binomial}(a,1/2)\) and \(d\sim\operatorname{Binomial}(b,1/2)\) independently. By symmetry, each side has equal probability of a positive or negative type imbalance, namely \((1-Z_n/2^n)/2\). Thus
\[
\Pr(\Delta_A\Delta_B<0)
=2\cdot\frac{1-Z_a/2^a}{2}\cdot\frac{1-Z_b/2^b}{2}
=\tfrac12(1-Z_a/2^a)(1-Z_b/2^b).
\]
For even-even sizes such opposing type imbalances still leave the double-zero equilibria; otherwise the expression is exactly the no-equilibrium probability. This completes the proof.

## Verification

The included `verify.py` is a standalone Python 3 checker. For all \(1\le a,b\le5\), all \(0\le c\le a\), and all \(0\le d\le b\), it independently enumerates every action profile and tests all individual payoff inequalities, without invoking the four-class counting proof. It confirms 400 type-count configurations and 102,400 labeled action-profile evaluations. Separately, it checks the random-type probability formula using exact rational arithmetic for all \(1\le a,b\le8\). Run `python verify.py`. These finite checks are reproducibility tests, not a substitute for the preceding proof for arbitrary sizes.

## Relationship to prior work

Pei, Cao, and Zhang (arXiv:2607.10997v1, July 13, 2026) give in their Result 3 a divisibility criterion for a complete bipartite conformist/rebel graph when one entire side consists of conformists and the other of rebels. Their proof assumes precisely those unmixed sides: the conformist payoff is indexed by rebel choices and vice versa. Our identity includes that case by substituting \(c=a\) and \(d=0\); then it gives the stronger exact count \(Z_aZ_b\), and additionally treats arbitrary mixes of both types on both sides and the induced random-type law. The earlier fashion-game paper of Cao and Yang (2014) establishes the general evenness of PNE counts and an odd-degree obstruction for the role-segregated bipartite case, but not the mixed-side enumerator. Cao, Sánchez, and Zhang (arXiv:2607.05932v1, July 7, 2026) study heterogeneous graphical games and general sufficient existence conditions, not this exact count. Shen and Lin (2020) study a max-min utility objective for fashion games on other listed graph families. These comparisons concern mathematical statements and the available full texts, not merely titles.

## Limitations

The formula uses exactly two actions, unweighted complete bipartite interactions, and weak (tie-allowing) PNE. It does not extend without additional work to weighted, noncomplete, multi-action, stubborn-agent, or dynamics models; no convergence or mixed-equilibrium assertions are made. The originality comparison is confined to accessible source texts and recovered literature: equivalent unpublished or unindexed work, and revisions not inspected in full, remain possible. The result has received no independent audit or validation.

## References

1. Shan Pei, Wenjie Cao, Boyu Zhang, *Network games with three types of players*, arXiv:2607.10997v1 (first posted July 13, 2026), https://arxiv.org/abs/2607.10997. Full available manuscript text: https://www.researchgate.net/publication/409443985_Network_games_with_three_types_of_players.
2. Zhigang Cao, Xiaoguang Yang, *The fashion game: Network extension of Matching Pennies*, Theoretical Computer Science 540–541 (2014), 169–181, https://doi.org/10.1016/j.tcs.2014.05.009. Available text: https://ml2.inf.ethz.ch/courses/tcsod/TCS-Seminar-papers/The%20fashion%20game%3A%20Network%20extension%20of%20Matching%20Pennies.pdf.
3. Wenjie Cao, Ángel Sánchez, Boyu Zhang, *Network games with heterogeneous players*, arXiv:2607.05932v1 (first posted July 7, 2026), https://arxiv.org/abs/2607.05932.
4. Chenli Shen, Wensong Lin, *Fashion game on graphs*, Discrete Optimization 38 (2020), article 100606, https://doi.org/10.1016/j.disopt.2020.100606.
