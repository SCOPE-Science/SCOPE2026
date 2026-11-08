# Exact absorption kernel and square-root hub loyalty in asynchronous friendship-graph majority dynamics

## Finding

For each integer \(k\geq1\), let the friendship graph \(F_k=K_1\vee(kK_2)\) have a designated hub \(o\) and \(k\) disjoint pairs of outer vertices. Start with any binary labeling and update one uniformly random vertex per discrete step. An update replaces its label by the strict majority among *open-neighborhood* labels, retaining its current label when those counts tie.

The process almost surely reaches a fixed configuration. The complete distribution over **labeled final configurations**, conditional on any labeled initial configuration, is as follows. Write \(h\in\{0,1\}\) for the initial hub label; let \(a\) be the number of outer pairs both labeled \(h\), \(b\) the number both labeled \(1-h\), and \(j\) the number of mixed pairs, so \(a+b+j=k\). Set \(d=b-a\) and \(q=\min\{j+1,\max(0,d)\}\).

With probability \(1-q/(j+1)\), the hub never changes and every mixed pair becomes \((h,h)\). For each integer \(r\) with \(1\leq r\leq q\), and for each specified subset \(S\) of exactly \(r-1\) of the \(j\) initially mixed pairs, there is probability

\[
\frac{1}{(j+1)\binom{j}{r-1}}
\]

that the hub changes once, exactly the pairs indexed by \(S\) finish as \((h,h)\), and every other initially mixed pair finishes as \((1-h,1-h)\). All initially homogeneous pairs retain their original labels, and these cases exhaust the terminal law. In particular, the conditional probability that the hub ever changes is \(q/(j+1)\).

If all \(2k+1\) initial labels are independent unbiased bits, write \(p_k\) for the probability the final hub differs from the initial hub. Then the exact all-size formula is

\[
p_k=\frac{1}{4^k}\sum_{\substack{a,b,j\geq0\\a+b+j=k\\b>a}}
\frac{k!\,2^j}{a!\,b!\,j!}\;
\frac{\min(b-a,j+1)}{j+1},
\]

and the sharp asymptotic law is

\[
\boxed{\lim_{k\to\infty}\sqrt{\pi k}\,p_k=1.}
\]

The probability that the **entire graph** ends in unanimous consensus is, by contrast,

\[
\boxed{c_k=\frac{3^k}{4^k}+\frac{3^{k+1}-1-2^{k+1}}{2(k+1)4^k}
\sim\left(\frac34\right)^k.}
\]

Hence center-opinion reversal has polynomial probability \(\sim1/\sqrt{\pi k}\) while full consensus has exponentially small probability \(\sim(3/4)^k\).

## Assumptions and scope

The vertices are labeled; the center is designated even when \(k=1\), where the graph is a triangle. All edges are undirected and unweighted. No vertex has a self-loop. At each discrete step one of all \(2k+1\) vertices is selected independently and uniformly, including vertices whose update leaves the configuration unchanged. Exact equality of neighbor counts is a tie and preserves the current bit. All probabilities concern this random update schedule and initial configurations as specified, not deterministic schedules or a rule that randomly flips on a tie. The formula for the full terminal law applies to **every deterministic initial labeling**; the averaging and asymptotics use independent fair initial bits.

## Proof

**Pair invariant and convergence.** As long as the hub label remains \(h\), an initially homogeneous outer pair stays homogeneous, even if its label opposes \(h\): each of its vertices sees one neighbor of each label or two supporting its current label. A mixed outer pair has exactly one vertex opposing the hub. That vertex sees two neighbors labeled \(h\) and hence changes to \(h\) the first time it is selected; the other vertex is never unhappy. Thus each initially mixed pair resolves once, and no other outer vertex changes before any hub switch.

Initially the hub sees \(2b+j\) opposing bits and \(2a+j\) supporting bits. When \(t\) mixed pairs have resolved to \(h\), these become \(2b+j-t\) and \(2a+j+t\). The hub is unhappy exactly when \(t<b-a=d\). Ignoring inert selections, the next relevant vertex is uniformly drawn from the hub and the one unhappy outer vertex of each unresolved mixed pair. Equivalently, assign independent equal-rate exponential clocks to these \(j+1\) initially relevant vertices. The relative rank \(R\) of the hub is uniform on \(\{1,\ldots,j+1\}\), and the \(R-1\) mixed pairs resolving before it form a uniformly random subset of that size. If \(R\leq d\), the hub changes; otherwise it stays forever because subsequent pair resolutions only increase its support.

If the hub changes, every *still mixed* pair now has exactly one vertex opposing the new hub and resolves in favor of the new hub. Pairs previously made homogeneous remain frozen, as do initially homogeneous pairs. At the switching moment the new hub already has a strict majority of supporting neighbor labels; subsequent resolutions can only reinforce that majority. It therefore never switches back. Finally, every unresolved mixed pair is selected eventually with probability one. This proves almost-sure fixation, hub-switch uniqueness, and the complete terminal distribution by the uniform rank and uniform subset laws.

**Fair-bit averaging.** Conditional on the initial hub label, outer pairs are independent with probability \(1/4\) of being homogeneous and supportive, probability \(1/4\) of being homogeneous and opposing, and probability \(1/2\) of being mixed. The event \((a,b,j)\) has probability \(4^{-k}k!2^j/(a!b!j!)\). Substituting the conditional switching probability \(\min\{j+1,(b-a)_+\}/(j+1)\) gives the displayed exact sum, including all parity cases.

For the consensus probability, either \(b=0\), in which case the initial hub does not switch and every mixed pair adopts its label, or \(a=0\), \(b\geq1\), and the hub is the first among the \(j+1\) relevant vertices, in which case it switches before any mixed pair resolves. These disjoint events have respective probabilities

\[
\left(\frac34\right)^k,
\qquad
\frac{1}{4^k}\sum_{j=0}^{k-1}\binom{k}{j}\frac{2^j}{j+1}.
\]

Integrating \((1+2u)^k\) over \(0\leq u\leq1\) evaluates the second expression as \((3^{k+1}-1-2^{k+1})/[2(k+1)4^k]\), proving the formula and its exponential asymptotics.

**Sharp hub-switch asymptotics.** Under the independent fair-pair law write \(D_k=b-a\) and \(J_k=j\). Express \(D_k\) as a sum of \(k\) independent random variables with values \(-1,0,+1\) of probabilities \(1/4,1/2,1/4\). Thus

\[
\frac{D_k}{\sqrt{k}}\ \Longrightarrow\ Z,\qquad Z\sim N(0,1/2),
\quad\text{and}\quad\frac{J_k}{k}\ \xrightarrow{\mathbb P}\frac12.
\]

The conditional switching probability is \(\min\{1,(D_k)_+/(J_k+1)\}\). Therefore

\[
\sqrt{k}\min\!\left\{1,\frac{(D_k)_+}{J_k+1}\right\}
\ \Longrightarrow\ 2Z_+.
\]

Expectations converge as well. Indeed, on \(J_k\geq k/4\), the displayed nonnegative variable is bounded by \(4|D_k|/\sqrt{k}\), whose second moments are bounded uniformly because \(\mathbb E D_k^2=k/2\). The complement has exponentially small probability by a binomial Chernoff bound, and the variable is at most \(\sqrt{k}\) there. Uniform integrability follows. Finally \(2\mathbb E Z_+=1/\sqrt{\pi}\), which establishes the sharp limit.

## Verification

The standalone script `verify_absorption.py` independently computes exact terminal probability distributions via recursion over every labelled configuration of \(F_k\) for \(1\leq k\leq6\), without relying on the permutation proof. Its comparison with the proposed terminal law checks all \(10,920\) labelled starting states and every nonzero terminal probability. For those instances it also checks the hub-flip and consensus probabilities. The separate `verify_formula.py` evaluates the multinomial formula and the consensus identity with exact rational arithmetic through \(k=160\); its numerical normalized hub-flip values approach one. Outputs are stored as `absorption_output.txt` and `formula_output.txt`. All-size results follow from the preceding proof, not from finite tests.

For reproducibility, run each Python script using an ordinary Python 3 interpreter. No third-party packages or external data are required.

## Relationship to prior work

Auletta, Caragiannis, Ferraioli, Galdi and Persiano (arXiv:1402.4050, first submitted 2014-02-17) study sequential majority updates with current-opinion tie retention and characterize when some *choice of update sequence* can change an initial majority; their study does not evaluate the probability law of randomly chosen updates on the friendship family. Mossel, Neeman and Tamuz (arXiv:1207.0893, first submitted 2012-07-04) study information aggregation primarily under synchronous majority dynamics, which does not fix the random sequential absorption kernel. Feldman, Immorlica, Lucier and Weinberg (arXiv:1408.5192, first submitted 2014-08-22) study a different asynchronous model with initially unannounced private signals and private-signal tie breaking; it does not imply the law for initially fully announced binary configurations with current-opinion tie retention. The result here is the explicit random-update distribution, its all-size hub-switch law, and the asymptotic separation of hub reversal from unanimity.

## Limitations

The theorem does not give the distribution of the number of attempted updates before absorption, and does not apply to random tie flips, private-signal tie breaking, nonuniform update rates, or a different graph family without a new argument. The exact terminal kernel implies the displayed aggregate statistics, but does not by itself establish historical priority among all unindexed published material. Independent scientific validation has not been performed.

## References

1. E. Mossel, J. Neeman, and O. Tamuz, *Majority Dynamics and Aggregation of Information in Social Networks*, arXiv:1207.0893, first public version 2012-07-04. https://arxiv.org/abs/1207.0893
2. V. Auletta, I. Caragiannis, D. Ferraioli, C. Galdi, and G. Persiano, *Minority Becomes Majority in Social Networks*, arXiv:1402.4050, first public version 2014-02-17. https://arxiv.org/abs/1402.4050
3. M. Feldman, N. Immorlica, B. Lucier, and S. M. Weinberg, *Reaching Consensus via non-Bayesian Asynchronous Learning in Social Networks*, arXiv:1408.5192, first public version 2014-08-22. https://arxiv.org/abs/1408.5192
