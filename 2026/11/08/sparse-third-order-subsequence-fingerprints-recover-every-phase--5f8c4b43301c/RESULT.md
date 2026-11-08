# Sparse third-order subsequence fingerprints recover every phase of a two-run binary cycle

## Finding

Let \(a,b,m\) be arbitrary positive integers, put \(p=a+b\), and let \(X=(0^a1^b)^\omega\) be the one-sided periodic binary word. For \(0\le i<p\), write \(F_i=X[i:i+mp]\) for the length-\(mp\) factor beginning at phase \(i\). For finite words \(w,u\), write \(\binom{w}{u}\) for the number of increasing index selections whose letters spell \(u\). Define the sparse signature

\[
\mathcal S(w)=\left(\binom{w}{01},\binom{w}{001}\right).
\]

**Theorem.** The \(p\) signatures \(\mathcal S(F_i)\), \(0\le i<p\), are pairwise distinct, for every \(a,b,m\ge1\). The first coordinate alone has exactly \(p-g+1\) distinct values, where \(g=\gcd(a,b)\); its only collisions consist of exactly \(g-1\) pairs of phases. Consequently the least \(k\ge1\) for which all length-\(mp\) factors are distinguished by their complete \(k\)-binomial decks is

\[
\kappa(a,b;m)=\begin{cases}2,&\gcd(a,b)=1,\\3,&\gcd(a,b)>1.\end{cases}
\]

In every collision of the first coordinate, the second-coordinate gap is explicitly positive. Parameterizing the collision pairs by \(1\le j<g\), their gaps are

\[
\Delta_j=\frac{bm}{2}\frac{a(g-j)}g\frac{aj}g
=\frac{bma^2}{2g^2}j(g-j).
\]

Thus the smallest positive gap among these pairs (when \(g>1\)) equals \(bma^2(g-1)/(2g^2)\). The two-run hypothesis is sharp as a family restriction: the primitive four-run cycle \(01100011\) has two different rotations \(01100011\) and \(10001101\) with identical *complete* \(3\)-binomial decks, and this ambiguity persists after any positive common repetition of these rotations.

## Assumptions and scope

All run lengths and the repetition count are positive integers, the alphabet is labeled \(\{0,1\}\), and scattered occurrences count distinct index sets, not merely distinct subsequence strings. All factors are linear length-\(mp\) windows at the \(p\) phases of the infinite periodic word. No assertion is made about nonmultiples of \(p\), arbitrary four-run periods, or arbitrary binary necklaces. Because \(0^a1^b\) has exactly one zero-run and one one-run on a circle, its least period is \(p\), and its \(p\) phases are genuinely different words.

Two words are \(k\)-binomially equivalent when the counts of every scattered word of length at most \(k\) agree. The degree-one deck is the constant Parikh vector \((ma,mb)\) for all phases.

## Proof

**1. Enumerating phases.** Every length-\(mp\) phase word is exactly one of the following, without duplication:

\[
Z_s=0^s1^b(0^a1^b)^{m-1}0^{a-s},\qquad1\le s\le a,
\]

\[
O_t=1^t(0^a1^b)^{m-1}0^a1^{b-t},\qquad1\le t\le b.
\]

Here \(Z_s\) begins inside a zero run with \(s\) zeros remaining, whereas \(O_t\) begins inside a one run with \(t\) ones remaining. These give exactly \(a+b\) phases.

**2. The first counter.** Count a `01` subsequence by selecting a one and a preceding zero. For \(Z_s\), each one-run contains \(b\) ones, and its preceding-zero count is respectively \(s,s+a,\ldots,s+(m-1)a\). For \(O_t\), the initial \(t\) ones have no preceding zeros, the intermediate one-runs have \(a,2a,\ldots,(m-1)a\) preceding zeros, and the final \(b-t\) ones have \(ma\) preceding zeros. Therefore, with \(T=abm(m-1)/2\),

\[
\binom{Z_s}{01}=T+bms,\qquad
\binom{O_t}{01}=T+ma(b-t).
\]

Both families are injective in their own parameter. Across families equality holds exactly when

\[
bs=a(b-t).
\]

Writing \(a=gA\), \(b=gB\), with \(\gcd(A,B)=1\), all positive solutions in the stated ranges are precisely

\[
s=A(g-j),\qquad t=Bj,\qquad1\le j<g.
\]

Thus the only second-order ambiguities are \(g-1\) disjoint pairs, leaving \(p-g+1\) classes. Since each word has the same numbers of zeros and ones, all length-two scattered counts other than `01` are determined by these counts and the Parikh vector: `00` and `11` use ordinary binomial coefficients, while `10` equals \(m^2ab-\binom{w}{01}\). Thus the complete second-order deck has exactly the same collisions.

**3. A third-order counter resolves every collision.** A `001` subsequence is determined by its terminal one and an unordered pair of earlier zeros. The exact counts are

\[
\binom{Z_s}{001}=b\sum_{h=0}^{m-1}\binom{s+ha}{2},
\]

\[
\binom{O_t}{001}=b\sum_{h=1}^{m-1}\binom{ha}{2}
+(b-t)\binom{ma}{2}.
\]

When \(bs=a(b-t)\), subtract the two formulas and use \(\binom{x}{2}=(x^2-x)/2\), together with \(\sum_{h=0}^{m-1}h=m(m-1)/2\). The linear terms cancel because the first moments are equal. The remaining difference is

\[
\binom{O_t}{001}-\binom{Z_s}{001}=\frac{bm}{2}s(a-s)>0.
\]

In a collision, \(s=A(g-j)\) and \(1\le j<g\), so \(0<s<a\), proving strict positivity and the asserted formula for \(\Delta_j\). The minimum follows because \(j(g-j)\) is minimized at \(j=1\) or \(j=g-1\). Therefore the two counters together distinguish all phases. When \(g=1\), second order already suffices; when \(g>1\), it does not and third order does. Degree one never suffices, since all phases share their Parikh vector and \(p\ge2\). This proves the exact reconstruction-order statement.

**4. The four-run boundary.** Let \(u=01100011\) and its two-position rotation \(v=10001101\). Direct counting of all fourteen nonempty binary scattered patterns of lengths at most three gives, in pattern order `0`, `1`, `00`, `01`, `10`, `11`, `000`, `001`, `010`, `011`, `100`, `101`, `110`, `111`, the same vector for both:

\[
(4,4,6,10,6,6,4,12,6,9,6,12,3,4).
\]

The words are different. For any positive \(m\), equality of these truncated scattered-count vectors is preserved on taking \(m\)-th powers: the formal subsequence enumerator \(\sum_{|x|\le3}\binom{w}{x}x\), with multiplication truncated at degree three, is multiplicative under word concatenation. Hence \(u^m\) and \(v^m\) have equal degree-three decks but are distinct conjugates. This demonstrates that two-run rigidity is not a general circular-word theorem.

## Verification

Run `python3 verify.py` using Python 3 and its standard library. The verifier independently calculates subsequence counts by a descending-length dynamic program, checks the two formulas above for every \(1\le a,b\le12\) and \(1\le m\le5\), checks the predicted \(g-1\) cross-family collision count and exact positive third-order gaps, and compares all phase signatures. It also verifies the four-run example and its first six powers. The recorded execution passed 9,360 direct signature checks, 30,420 cross-family phase comparisons, and six four-run repetition checks. These finite tests are supporting diagnostics, not proofs of the universally quantified theorem; the algebraic argument above supplies the proof.

## Relationship to prior work

- Poovanandran, Simpson and Teh (2021), *Counting Subwords in Circular Words and Their Parikh Matrices*, arXiv:2110.14858, introduce circular scattered-count approaches; their average Parikh matrix forgets rotation phase and does not provide this two-statistic phase reconstruction.
- Rigo, Stipulanti and Whiteland (2022), *Characterizations of Families of Morphisms and Words via Binomial Complexities*, arXiv:2201.04603, develop binomial-complexity theory and related reconstruction questions, but the inspected results do not provide this cyclic two-run third-order recovery formula.
- Vivion (2025), *New Examples of Words for Which the Binomial Complexities and the Subword Complexity Coincide*, arXiv:2509.11172, proves second-order rigidity for balanced and other classes; its stated hypotheses do not cover the nonbalanced two-run family in general and it does not state the precise gcd-sensitive phase threshold here.

The second-order gcd class count alone is not claimed as a new result. The contribution is the *sparse* third-order phase-injectivity theorem, exact gap formula, and its sharp failure for four-run cycles. Unlike averaged circular statistics, the counters here are applied to an individual chosen linear phase word.

## Limitations

The result requires both run lengths to be strictly positive and the observation window to contain an integer number of complete periods. For lengths not divisible by the period, distinct third-order signatures can collide; no all-length claim is made. The fourth-order and higher-order decks are not separately analyzed. Literature searches and inspected primary sources cannot rule out every unindexed equivalent theorem, and this is not an independently audited result.

## References

1. G. Poovanandran, J. Simpson, W. C. Teh, *Counting Subwords in Circular Words and Their Parikh Matrices*, arXiv:2110.14858 (first posted 2021-10-28), https://arxiv.org/abs/2110.14858.
2. M. Rigo, M. Stipulanti, M. A. Whiteland, *Characterizations of Families of Morphisms and Words via Binomial Complexities*, arXiv:2201.04603 (first posted 2022-01-12), https://arxiv.org/abs/2201.04603.
3. L. Vivion, *New Examples of Words for Which the Binomial Complexities and the Subword Complexity Coincide*, arXiv:2509.11172 (first posted 2025-09-14), https://arxiv.org/abs/2509.11172.
