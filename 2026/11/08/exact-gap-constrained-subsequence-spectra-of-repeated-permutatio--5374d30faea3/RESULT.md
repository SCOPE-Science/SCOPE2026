# Exact gap-constrained subsequence spectra of repeated permutation words

## Finding

Fix integers \(q\ge 2\), \(k\ge 1\), \(h\ge 1\), and a permutation \(P\) of \(q\) different symbols. Let \(W=P^k\), with positions numbered \(0,\ldots,qk-1\). For each \(i=1,\ldots,h-1\), fix arbitrary integer bounds \(1\le a_i\le b_i\). Let \(\mathcal G_h(W;\mathbf a,\mathbf b)\) be the set of **distinct** length-\(h\) words \(u\) admitting positions \(0\le t_0<\cdots<t_{h-1}<qk\) with \(W[t_i]=u_i\) and \(a_i\le t_i-t_{i-1}\le b_i\) for all \(i\ge 1\). The bounds concern successive selected **position differences**, rather than numbers of skipped letters.

Put \(s_i=\min\{q,b_i-a_i+1\}\) and
\[
Q(z)=\left(\sum_{x=0}^{q-1}z^x\right)
\prod_{i=1}^{h-1}\left(\sum_{d=a_i}^{a_i+s_i-1}z^d\right).
\]
Then the complete distinct-language cardinality is
\[
\boxed{\left|\mathcal G_h(W;\mathbf a,\mathbf b)\right|
=\sum_{j=0}^{qk-1}[z^j]Q(z).}
\]
More strongly, for each length-\(h\) query that can be embedded into the *infinite* repetition \(P^\omega\) with the prescribed gaps, there is a unique componentwise-earliest valid embedding, and \(Q(z)\) is the exact generating polynomial of the endpoints of these earliest embeddings, one contribution per **distinct query**.

There are exactly \(q\prod_{i=1}^{h-1}s_i\) such locally admissible infinite-host queries. All of them occur in \(P^k\) if and only if
\[
\boxed{qk\ge q+\sum_{i=1}^{h-1}(a_i+s_i-1).}
\]
In particular, the finite word \(P^k\) is universal for *all* length-\(h\) queries under these gap constraints precisely when every \(s_i=q\) and
\[
\boxed{qk\ge q+\sum_{i=1}^{h-1}(a_i+q-1).}
\]
The empty product makes these conclusions valid for \(h=1\), when all \(q\) single-letter queries always occur.

For uniform bounds \(a_i=a\) and \(b_i=b\), write \(s=\min(q,b-a+1)\) and \(T=qk-1-a(h-1)\). There is also a finite alternating-binomial evaluation:
\[
\boxed{\left|\mathcal G_h\right|=
\sum_{j=0}^{1}\sum_{r=0}^{h-1}(-1)^{j+r}
\binom{h-1}{r}\binom{T-jq-rs+h}{h},}
\]
where a binomial coefficient with upper argument smaller than its nonnegative lower argument is interpreted as zero. For example, \(q=3\), \(k=3\), \(h=3\), and position differences in \([2,4]\) give exactly \(23\) distinct valid length-three queries out of \(27\); four repetitions give all \(27\).

## Assumptions and scope

Each alphabet symbol appears exactly once in the period \(P\), and the same period is repeated \(k\) times. No restriction is imposed on how the intervals \([a_i,b_i]\) vary with the query position. Their endpoints are positive integers, ensuring strictly increasing embedding positions. Distinct queries are counted once, regardless of how many embeddings they have. The conclusion is not asserted for periodic words with repeated letters in a period, noninterval gap sets, symbol-dependent gap rules, or constraints between nonadjacent selected positions.

## Proof

**Phase normalization.** Relabel the distinct symbols in the order in which they occur in \(P\) as \(0,1,\ldots,q-1\). Then the letter at source position \(t\) is \(t\bmod q\). The earliest occurrence of query letter \(u_0\) is \(t_0=u_0\), with \(0\le u_0\le q-1\).

**Local greedy step.** Suppose an embedding has selected letter \(x\) at position \(t\), with residue \(x\bmod q\). To select the next required letter \(y\), a permitted position difference \(d\) must satisfy both \(a_i\le d\le b_i\) and \(d\equiv y-x\pmod q\). This set is nonempty if and only if the required residue is represented in the first \(s_i\) consecutive integers \(a_i,\ldots,a_i+s_i-1\). Indeed, the first \(q\) consecutive integers realize all residue classes exactly once, and an interval shorter than \(q\) realizes its residue classes exactly once. If the set is nonempty, the **least** permitted difference \(d_i\) is uniquely determined in this first interval.

**Global greediness.** Every occurrence of a specified letter lies in a single residue class modulo \(q\). Hence each legal embedding of a fixed query uses the same residue at each selected position. When a local step is allowed, its earliest permissible relative difference \(d_i\) is therefore independent of how many complete periods the preceding selected position has been delayed. Inductively, the positions
\[
t_0=u_0,\qquad t_i=t_{i-1}+d_i
\]
form the componentwise-earliest embedding in \(P^\omega\). If any local step is disallowed, no embedding exists even in the infinite repetition. If all steps are allowed, the query embeds in \(P^k\) if and only if its earliest final position \(t_{h-1}\) is smaller than \(qk\). This also proves necessity, rather than merely sufficiency, of the endpoint cutoff.

**Bijection and polynomial.** Choosing an initial phase \(x\in\{0,\ldots,q-1\}\) and a permissible minimal difference \(d_i\in\{a_i,\ldots,a_i+s_i-1\}\) for every \(i\) uniquely constructs the query letters \(u_0=x\) and \(u_i\equiv u_{i-1}+d_i\pmod q\). Conversely, each locally admissible query uniquely recovers its initial phase and each minimal difference from consecutive letter residues. Thus this correspondence is one-to-one: it does not multiply-count query strings with several embeddings. Its earliest endpoint is exactly \(x+\sum_i d_i\). Multiplying the elementary generating polynomials gives \(Q(z)\), and restricting endpoints to at most \(qk-1\) proves the cardinality formula.

**Saturation and universality.** The number of locally admissible queries is the number of parameter tuples in the bijection, namely \(q\prod_i s_i\). Its largest possible earliest endpoint is
\[
(q-1)+\sum_i(a_i+s_i-1),
\]
attained by the unique tuple choosing each component maximally. Consequently every locally admissible query fits if and only if \(qk-1\) is at least this value. All possible \(q^h\) queries are locally admissible if and only if each \(s_i=q\), since every missing residue at one step excludes an actual length-\(h\) query; the choices of the other symbols can be made arbitrarily. Combining these statements gives the sharp universality condition, including \(h=1\).

**Uniform closed form.** When all bounds agree, the endpoint polynomial is
\[
Q(z)=z^{a(h-1)}\frac{1-z^q}{1-z}\left(\frac{1-z^s}{1-z}\right)^{h-1}.
\]
Summing coefficients through \(qk-1\) is the same as extracting \([z^{T}]\) from \((1-z^q)(1-z^s)^{h-1}(1-z)^{-h-1}\). Expanding the two numerator factors by the binomial theorem and using \([z^m](1-z)^{-h-1}=\binom{m+h}{h}\) for \(m\ge0\) gives the stated alternating sum. This completes all claims.

## Verification

The included self-contained `verify.py` separately enumerates query strings and feasible embeddings, then compares counts with polynomial coefficients and sharp thresholds. It tests all small uniform profiles in a bounded exhaustive grid, seeded nonuniform profiles with varying bounds, and the uniform inclusion-exclusion expression. Invoke `python3 verify.py` from the extracted directory. The output lists the exact number of checked configurations. Computations corroborate; the unlimited-parameter statements follow from the proof above.

## Relationship to prior work

Day, Kosche, Manea and Schmid introduce interval and regular constraints on gaps and establish general matching and language-analysis complexity bounds, including hardness of universality. Here the source is restricted to a repeated permutation, but the local intervals may vary arbitrarily; the contribution is the exact distinct-language enumerator and sharp saturation/universality thresholds, not another general decision procedure. Adamson and collaborators consider gap-constrained longest common subsequence algorithms, a different optimization problem. Manea, Richardsen and Schmid treat constraints linking nonadjacent query positions and develop matching-complexity results, rather than the present exact language counts. Previous results on periodic binary bounded-*range* subsequences concern a single global enclosing window and a two-run source, not independent per-gap intervals on a repeated permutation; likewise ordinary subsequence-universality and rotation-complete necklace counts do not cover these claims.

## Limitations

The factorization relies on one occurrence of each letter per period. It does not count the number of embeddings of each query, nor handle arbitrary regular-language gap restrictions. Primary-source and mathematical-record searches did not identify this exact formula, but absence of a match is not a proof of novelty. An equivalent observation could exist in unindexed pattern-mining or automata literature. No independent external validation was performed.

## References

- J. D. Day, M. Kosche, F. Manea, M. L. Schmid, *Subsequences With Gap Constraints: Complexity Bounds for Matching and Analysis Problems*, arXiv:2206.13896v1 (first public 2022-06-28), https://arxiv.org/html/2206.13896v1 ; ISAAC 2022, DOI:10.4230/LIPIcs.ISAAC.2022.64.
- D. Adamson, M. Kosche, T. Koß, F. Manea, S. Siemer, *Longest Common Subsequence with Gap Constraints*, arXiv:2304.05270 (2023-04-11), https://arxiv.org/abs/2304.05270.
- F. Manea, J. Richardsen, M. L. Schmid, *Subsequences With Generalised Gap Constraints: Upper and Lower Complexity Bounds*, arXiv:2404.10497v1 (2024-04-16), https://arxiv.org/html/2404.10497v1.
