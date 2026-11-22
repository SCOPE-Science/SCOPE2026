# Heavy-tailed insertion-degree deficits in uniform Dyck words

## Finding

Let \(W_n\) be uniformly distributed over all \(C_n=\frac1{n+1}\binom{2n}{n}\) Dyck words with \(n\) up-steps and \(n\) down-steps, for each integer \(n\ge1\). A *Dyck insertion superword* of \(W_n\) is a Dyck word of semilength \(n+1\) containing \(W_n\) as a scattered subsequence; equivalently it is obtained by inserting one up-step and one down-step. Count different resulting words only once, irrespective of insertion positions. Write \(U_n\) for this count and \(Q_n=n^2+1-U_n\) for its deficit from the maximum possible count.

**Theorem.** For every integer \(r\ge0\),
\[
\lim_{n\to\infty}\Pr\left(\frac{Q_n}{n}\le r+\frac12\right)
=\sum_{j=0}^{r}\frac{C_{j+1}}{4^{j+1}}.
\]
In particular, \(Q_n/n\Rightarrow R\) where \(\Pr(R=r)=C_{r+1}/4^{r+1}\). The law has \(\Pr(R=r)\sim(\sqrt\pi\,r^{3/2})^{-1}\) and \(\mathbb E R=\infty\). Nonetheless the *finite-source mean* is exactly
\[
\mathbb E Q_n=\frac{(n+1)4^n}{2\binom{2n}{n}}-\frac{3(n+1)}2+1,
\qquad n\ge1,
\]
and therefore \(\mathbb E Q_n\sim(\sqrt\pi/2)n^{3/2}\). Thus \(Q_n/n\) is tight but its expectation diverges at order \(\sqrt n\). The deficit is tight on the \(n\)-scale (indeed the limiting mass at zero is \(1/4\)), but rare highly fragmented sources produce an order-\(n^{3/2}\) mean.

## Assumptions and scope

A Dyck word is a word on \(\{U,D\}\) whose prefix balances (\(\#U-\#D\)) are nonnegative and whose final balance is zero. A *ground arch* or *irreducible component* is a nonempty Dyck word that returns to balance zero only at its end. Every Dyck word has a unique ordered decomposition into ground arches with positive semilengths \(a_1,\ldots,a_k\), where \(\sum_{i=1}^k a_i=n\). Exactly \(C_{a-1}\) irreducible components have semilength \(a\). The probability space is the uniform distribution on complete Dyck words of fixed semilength, not the uniform distribution on component-size compositions or on insertion positions.

The known source-wise enumeration of Bernini–Ferrari–Pinzani–West, Proposition 2.2 (2013), gives
\[
U_n=1+\sum_{i=1}^k a_i^2+\sum_{1\le i<j\le k}a_i a_j.
\]
This deterministic identity is an explicitly credited premise, **not** an originality claim here. Consequently
\[
Q_n=\sum_{i<j}a_i a_j=\frac{n^2-\sum_i a_i^2}{2}\ge0.
\]
The new assertion concerns the random-source distribution and its divergent-moment phenomenon, not a new derivation of the deterministic formula.

## Proof

**1. Exact root-component laws.** Define the Catalan generating series
\[
C(z)=\sum_{n\ge0} C_n z^n=\frac{1-\sqrt{1-4z}}{2z},
\qquad A(z)=zC(z)=\frac{1-\sqrt{1-4z}}2.
\]
Here \(A(z)=\sum_{a\ge1}C_{a-1}z^a\) is the generating function of nonempty irreducible Dyck components. Unique ordered ground-arch decomposition gives \(C(z)=1/(1-A(z))\).

For each nonempty \(W_n\), let \(M_n=\max_i a_i\) be the largest ground-arch semilength and let \(R_n=n-M_n\) be the total size outside the largest arch. Fix \(r\ge0\) and \(n>2r\). A component of size \(n-r\) is then unique. Its interior has \(C_{n-r-1}\) choices, while the ordered sequence of arches before and after that component has total semilength \(r\), with coefficient \([z^r]C(z)^2\). The Catalan convolution gives \([z^r]C(z)^2=C_{r+1}\), and therefore
\[
\Pr(R_n=r)=\frac{C_{n-r-1}C_{r+1}}{C_n},\quad n>2r.
\]
For fixed \(r\), \(C_{n-r-1}/C_n\to4^{-(r+1)}\), hence the right-hand side tends to \(p_r=C_{r+1}/4^{r+1}\). These limits exhaust unit mass: \(\sum_{r\ge0}p_r=C(1/4)-C_0=1\). Consequently \(R_n\Rightarrow R\), where \(\Pr(R=r)=p_r\), and the sequence \(R_n\) is tight. This argument also proves the explicit distribution of the random remainder, without requiring an external condensation theorem.

**2. Transfer to insertion-degree deficit.** Isolate one component of size \(n-R_n\), whose cross-terms with all others contribute \((n-R_n)R_n\) to \(Q_n\). The cross-terms among the smaller components contribute between zero and \(R_n^2/2\). Thus
\[
0\le R_n-\frac{Q_n}{n}\le\frac{R_n^2}{n}
\]
(the lower inequality also follows from \(\sum_i a_i^2\ge(n-R_n)^2\)). Tightness of \(R_n\) implies the right side converges to zero in probability. Slutsky's theorem gives \(Q_n/n\Rightarrow R\). Catalan asymptotics \(C_j\sim4^j/(\sqrt\pi\,j^{3/2})\) yield \(p_r\sim1/(\sqrt\pi\,r^{3/2})\), whose first moment \(\sum_r r p_r\) diverges.

**3. Exact finite-size expectation.** Let \(B(z)=zA'(z)=z/\sqrt{1-4z}\) mark a ground arch by its semilength. For an ordered Dyck-arch sequence, \(Q_n=\sum_{i<j}a_i a_j\) marks an unordered pair of distinct arches, weighted by the product of their lengths. There are three arbitrary ordered sequences of intervening/unmarked arches (before, between and after the chosen pair). Hence the total \(Q\)-weight of all Dyck words of semilength \(n\) is
\[
S_n=[z^n]B(z)^2 C(z)^3=[z^n]\frac{z^2C(z)^3}{1-4z}.
\]
The exact algebraic identity
\[
\frac{z^2 C(z)^3}{1-4z}=\frac1{2(1-4z)}-\frac3{2\sqrt{1-4z}}+C(z)
\]
gives \(S_n=4^n/2-3\binom{2n}{n}/2+C_n\) for all \(n\ge1\). Dividing by \(C_n\) proves the stated expectation, and \(\binom{2n}{n}\sim4^n/\sqrt{\pi n}\) proves the asymptotic \(\mathbb E Q_n\sim\sqrt\pi\,n^{3/2}/2\). It follows that \(\mathbb E[Q_n/n]\sim\sqrt{\pi n}/2\to\infty\) even while \(Q_n/n\) converges to the proper discrete distribution above.

## Verification

The accompanying standalone `check.py` implements three independent finite checks with only the Python standard library. First, it generates all \(C_n\) Dyck words for each \(1\le n\le8\), explicitly inserts an up-step and a down-step at every positional choice, discards non-Dyck outputs, and deduplicates the survivors; the obtained counts match both the source-wise formula and the claimed deficit. This is \(2055\) source words in total. Second, it compares the aggregated deficit against the exact Catalan-binomial identity for these lengths and verifies all fixed-remainder classes with \(n>2r\). Third, an integer generating-function recurrence checks the aggregate identity independently through \(n=150\). The verifier outputs `VERIFY_OK`. Finite tests are corroboration, not the proof for unbounded \(n\), which is given above.

## Relationship to prior work

Bernini, Ferrari, Pinzani and West (2013), Proposition 2.2, already prove the **exact deterministic one-rank-up degree** in terms of the root arch sizes. This is the indispensable input and is not independently claimed here. Bernini, Cervetti, Ferrari and Steingrímsson (2019) treat interval enumerations and covering relations in the same poset; their inspected statements do not give this random-source law. General giant-component remainder limits for subcritical combinatorial compositions, such as Stufler (2016), explain why a tight remainder is natural; they do not directly give the Dyck insertion deficit's exact finite-size mean and heavy-tail mismatch. The present contribution is the combined exact source-distribution limit, singular expectation and insertion-channel interpretation, derived explicitly for ordered Catalan arches.

## Limitations

The law concerns one inserted up-step and one inserted down-step in the *ordered* (linear, noncircular) Dyck alphabet, with distinct output words counted once. It does not describe multiple balanced-pair insertions, uniform sampling from insertion positions, or an arbitrary law on source words. The limiting distribution is not a moment-convergence statement: its first moment is infinite and the prelimit means diverge. Earlier equivalent probabilistic formulations outside the inspected source set are possible. No independent external audit has been performed.

## References

1. A. Bernini, L. Ferrari, R. Pinzani and J. West, *The Dyck pattern poset*, arXiv:1303.3785v1, first publicly posted 15 March 2013; especially Proposition 2.2, https://arxiv.org/html/1303.3785v1 .
2. B. Stufler, *Gibbs partitions: the convergent case*, arXiv:1609.08859v1, first publicly posted 28 September 2016; particularly Theorem 3.1, https://arxiv.org/abs/1609.08859 .
3. A. Bernini, M. Cervetti, L. Ferrari and E. Steingrímsson, *Enumerative combinatorics of intervals in the Dyck pattern poset*, arXiv:1910.00299v1, first publicly posted 1 October 2019, https://arxiv.org/abs/1910.00299 .
