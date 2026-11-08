# Eleven leaves are sharp for two reversals in expected future phylogenetic diversity

## Finding

**Theorem.** For rooted nonplane full binary trees with the same number \(n\ge2\) of leaves, with every edge of unit length and every terminal species independently extinct with one common probability \(q\in(0,1)\), a pair of tree shapes whose **expected surviving rooted phylogenetic diversity** changes strict ranking at least twice exists **if and only if** \(n\ge11\). No pair with \(n\le10\) has two reversals. At \(n=11\), among the \(194\) different expected-diversity response polynomials arising from \(207\) unlabelled tree shapes, exactly \(15\) unordered pairs of **distinct response polynomials** have two distinct interior crossing roots; those roots are simple and are strict ranking reversals. This is a count of distinct response-polynomial pairs, not of shape pairs.

One explicit eleven-leaf witness has nonplane rooted Newick forms (each `a` denotes a different terminal species):

```
A = ((a,((a,a),(a,a))),((a,a),((a,a),(a,a))))
B = ((a,(a,a)),((a,(a,a)),((a,a),(a,(a,a)))))
```

Its expected-diversity difference is exactly

\[
\Delta(q)=\mathbb E[X_A(q)]-\mathbb E[X_B(q)]
=-q^2+3q^3-2q^4-q^6+q^8
=-q^2(1-q)(q^2+q-1)(q^3+q-1).
\]

Consequently the exact two strict ranking reversals occur at \(q=(\sqrt5-1)/2\) and at the unique positive root of \(q^3+q-1=0\), approximately \(0.6180339887\) and \(0.6823278038\). At \(q=1/2,2/3,3/4\), respectively, \(\Delta(q)=-3/256,+4/6561,-495/65536\). The last two factors are each strictly increasing on \((0,1)\), so they each have one simple root; the roots are distinct.

## Assumptions and scope

A tree is unordered, rooted, full binary (every nonterminal vertex has exactly two children), with \(n\ge2\) distinct leaves and all \(2n-2\) edges of length one; distinct Newick `a` occurrences are separate leaves. The root is retained even if all leaves die. Independently for each leaf, extinction occurs with probability \(q\), and a given edge is retained exactly when at least one descendant leaf survives. The random surviving rooted phylogenetic diversity \(X_T(q)\) is the number of retained edges; this definition assigns diversity zero to total extinction. The comparison is between expected values for any two shapes with the **same** leaf count and common extinction probability, not between individual-species diversity indices, variances, or empirical phylogenies. Crossing means a strict change of the sign of the difference as \(q\) increases in \((0,1)\); an endpoint equality is not a reversal.

Write \(c_T(k)\) for the count of edges whose downward descendant clade contains exactly \(k\) leaves. The \(n\) terminal edges all have \(k=1\), and there are \(n-2\) other nonroot internal edges. The \(c_T(k)\) values for \(k=2,\ldots,n-1\) are nonnegative integers summing to \(n-2\).

## Proof

**1. Expected-diversity identity.** The indicator that an edge with \(k\) descendant leaves survives has expectation \(1-q^k\) by independent extinction. Summing the edge indicators gives the classical formula
\[
\mathbb E[X_T(q)]=\sum_{k=1}^{n-1}c_T(k)(1-q^k)
=(2n-2)-nq-\sum_{k=2}^{n-1}c_T(k)q^k.
\]
For two shapes \(T,U\), their difference is the polynomial \(\Delta_{T,U}(q)=-\sum_{k=2}^{n-1}(c_T(k)-c_U(k))q^k\). It has the forced factors \(q^2\) and \(1-q\), because the nonterminal edge counts of the two shapes each total \(n-2\). Any further zero in \((0,1)\) is an expected-diversity crossing; only an odd-multiplicity zero changes ranking.

**2. Complete finite cutoff.** Enumerate all rooted nonplane full binary shapes by the recurrence \(\mathcal T_1=\{a\}\), and for \(n\ge2\), \(\mathcal T_n\) consists of unordered root joins \((L,R)\) with \(L\in\mathcal T_i\) and \(R\in\mathcal T_{n-i}\), \(1\le i\le\lfloor n/2\rfloor\), where for equal subtree sizes only the canonical order \(L\le R\) is kept. This recurrence is exhaustive by decomposing at the unique root and is nonredundant by the canonical unordered-child convention. For each shape count downward clade sizes and deduplicate **identical** expected-diversity profiles. For each distinct-profile pair, form its integer coefficient difference; cancel forced endpoint factors and apply the exact signed Euclidean Sturm sequence to count the distinct real roots in \((0,1)\). The complete reproducible program `verify.py` implements this recurrence, exact integer/rational polynomial operations, positive-scaling normalization (which does not change signs), and Sturm's zero-count rule, with no floating-point decisions.

The certified counts \((\text{shapes},\text{profiles},\text{pairs with }0,1,2\text{ interior distinct roots})\) are

| Leaves | Shapes | Profiles | 0 roots | 1 root | 2 roots |
|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 0 | 0 | 0 |
| 3 | 1 | 1 | 0 | 0 | 0 |
| 4 | 2 | 2 | 1 | 0 | 0 |
| 5 | 3 | 3 | 3 | 0 | 0 |
| 6 | 6 | 6 | 15 | 0 | 0 |
| 7 | 11 | 11 | 53 | 2 | 0 |
| 8 | 23 | 23 | 232 | 21 | 0 |
| 9 | 46 | 45 | 877 | 113 | 0 |
| 10 | 98 | 95 | 3787 | 678 | 0 |
| 11 | 207 | 194 | 15400 | 3306 | 15 |

Every two-root polynomial at eleven leaves is square-free after the endpoint factors have been removed (verified by exact polynomial gcd with its derivative); therefore all the two-root pairs have strict ranking reversals. The absence of two roots for \(n\le10\) proves the sharp lower bound (even-multiplicity touching cannot produce two strict reversals).

**3. Explicit attainment and persistence.** For the displayed shapes the nonleaf clade-count profiles are \((c_A(2),c_A(3),c_A(4),c_A(5),c_A(6),c_A(8))=(5,0,2,1,1,0)\) and \((c_B(2),c_B(3),c_B(4),c_B(5),c_B(6),c_B(8))=(4,3,0,1,0,1)\). Substitution yields the exactly factored \(\Delta\) above. Both quadratic and cubic factors have positive derivatives on \((0,1)\), each is negative at zero and positive at one, and their roots differ (the quadratic root is not a root of the cubic). Thus there are exactly two strict reversals.

To extend to any \(n>11\), attach a **common** new root whose children are the original tree and a new single leaf, repeating as necessary. Both extended trees acquire precisely the same extra root-child clade sizes and terminal leaves. Their expected-diversity difference remains exactly \(\Delta(q)\). Hence every larger leaf count also admits two reversals.

## Verification

Execute `python3 verify.py` using only the Python standard library. The script exhaustively generates the rooted binary tree shapes for leaf counts \(2\) through \(11\), deduplicates the expected-diversity profiles, and counts crossings by exact rational Sturm sequences. For the two witness trees, it also enumerates all \(2^{11}=2048\) binary extinction/survival configurations at each of three rational extinction probabilities, obtaining the exact expectation differences \(-3/256\), \(4/6561\), \(-495/65536\) independently of the clade-profile formula. An independent implementation using symbolic polynomial root counts reproduced the same full profile-pair counts; it is auxiliary corroboration rather than part of the standalone package.

## Relationship to prior work

The edge-survival expectation and independent extinction model are standard, and **are not claimed as new**. Steel, Mimoto and Mooers (2007) develop extinction-weighted future phylogenetic diversity and species-contribution metrics; Faller, Pardi and Steel (2007) treat the distribution of phylogenetic diversity under random extinction and state the underlying edge formula explicitly. Nipperess and Matsen (2013) analyze mean/variance under fixed-size rarefaction; Lambert and Steel (2013) analyze loss in stochastic diversification settings; Fischer, Francis and Wicke (2021) study robustness of individual-species fair-proportion rankings. Those distinguishable claims do not imply this exact first double crossing between *whole-tree expected-PD curves* at eleven leaves or the 15 distinct-profile-pair census. The novelty assessment is subject to historical-priority uncertainty, not an assertion that an absence of search hits proves uniqueness in the worldwide literature.

## Limitations

The exhaustive minimality and 15-pair count are established only through eleven leaves; for larger sizes only **existence** is proved. All edges have unit length, hence no ultrametric/clock assumption is imposed; independently extinct terminal species share one common extinction probability. Unequal edge lengths, species-dependent/correlated extinction, phylogenetic variance and empirically estimated risk are outside the theorem. Distinct tree shapes may have identical expected-diversity curves; the first-layer count is for **distinct profiles**, not tree-shape pairs. The result has self-review only; independent audit and a comprehensive independent historical-priority survey have not been performed.

## References

1. M. Steel, A. Mimoto and A. O. Mooers, *Hedging our bets: the expected contribution of species to future phylogenetic diversity* (first public 20 Apr 2007), https://arxiv.org/abs/0704.2649.
2. B. Faller, F. Pardi and M. Steel, *Distribution of phylogenetic diversity under random extinction* (2007), https://arxiv.org/abs/0708.0425.
3. D. A. Nipperess and F. A. Matsen IV, *The mean and variance of phylogenetic diversity under rarefaction* (2013), https://doi.org/10.1111/2041-210X.12042.
4. A. Lambert and M. Steel, *Predicting the loss of phylogenetic diversity under non-stationary diversification models* (2013), https://arxiv.org/abs/1306.2710.
5. M. Fischer, A. Francis and K. Wicke, *Phylogenetic Diversity Rankings in the Face of Extinctions: Robustness of the Fair Proportion Index* (2021), https://arxiv.org/abs/2107.00748.
6. M. Steel, K. Wicke and A. O. Mooers, *Properties of biodiversity indices that model future extinction risk* (2026), https://arxiv.org/abs/2602.16059.
