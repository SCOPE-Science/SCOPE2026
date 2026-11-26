# Composition-flat deficit for binary three-subsequence universality

## Finding

For every integer \(n\geq 0\) and \(0\leq k\leq n\), let \(U(n,k)\) denote the number of binary words of length \(n\) with exactly \(k\) ones that contain every one of the eight binary length-three words as a scattered subsequence (positions need not be adjacent). Then

\[
U(n,k)=\begin{cases}
\binom{n}{k}-3(n-2),&3\leq k\leq n-3,\\
0,&\text{otherwise}.
\end{cases}
\]

In the nontrivial range, the number of words *failing* three-subsequence universality is exactly \(3(n-2)\), independent of the prescribed composition. Among words chosen uniformly with \(k\) ones, the probability of universality is \(1-3(n-2)/\binom{n}{k}\) in this range and zero otherwise.

## Assumptions and scope

The alphabet is the labeled two-symbol set \(\{0,1\}\). A word \(v=v_1\cdots v_r\) is a *scattered subsequence* of \(w\) if there are indices \(1\leq i_1<\cdots<i_r\leq |w|\) with \(w_{i_j}=v_j\). The length is \(n=a+b\), where \(a\) is the number of zeros and \(b=k\) is the number of ones. The formula applies to every finite \(n\), including empty and constant words; the interior case requires \(a,b\geq3\). No asymptotic or genericity assumption is used.

## Proof

**Greedy arches.** Starting at the left, repeatedly remove the shortest nonempty prefix containing both letters; call each removed block an *arch*. Stop when the remaining suffix uses at most one letter. Each binary arch is uniquely of the form \(0^j1\) or \(1^j0\) for some \(j\geq1\). The residual suffix is empty or monochromatic.

A binary word contains all eight scattered subsequences of length three **if and only if** it has at least three greedy arches. The forward implication may be proved contrapositive. If there are \(r<3\) arches, choose the last symbol of every arch, then append a letter absent from the residual suffix, and pad the resulting absent subsequence to length three with arbitrary binary symbols. To see absence, greedy matching of the selected last symbols is forced to end at the end of each corresponding arch: that symbol does not appear earlier *inside* its arch. The next selected letter is absent from the residual suffix. Conversely, three disjoint arches allow arbitrary choices of the first, second, and third target bits, one from each arch. The greedy-matching argument also covers \(r=0\) and the empty word.

**Bivariate enumeration.** Introduce commuting formal variables \(x\) and \(y\) marking respectively zero and one counts. The ordinary generating functions for one arch and for the residual suffix are

\[
A(x,y)=\sum_{j\geq1}(x^jy+y^jx)
=\frac{xy(2-x-y)}{(1-x)(1-y)},\qquad
R(x,y)=\frac{1}{1-x}+\frac{1}{1-y}-1
=\frac{1-xy}{(1-x)(1-y)}.
\]

Because the greedy factorization is unique, the generating function of all words with at most two arches is \(R(x,y)(1+A(x,y)+A(x,y)^2)\). Its coefficient at \(x^ay^b\) is the number of words of this composition *not* three-universal.

Suppose \(a,b\geq3\). The contribution of \(R\) is zero. The contribution of \(RA\) is exactly two: the monotone words \(0^a1^b\) and \(1^b0^a\). Next,

\[
RA^2=x^2y^2(1-xy)
\left[\frac{1}{(1-x)(1-y)^3}
+\frac{2}{(1-x)^2(1-y)^2}
+\frac{1}{(1-x)^3(1-y)}\right].
\]

For nonnegative integers \(u,v\), define
\[
H(u,v)=\binom{v+2}{2}+2(u+1)(v+1)+\binom{u+2}{2}.
\]

The coefficient of \(x^ay^b\) in \(RA^2\) is therefore

\[
H(a-2,b-2)-H(a-3,b-3)=3(a+b)-8.
\]

Adding the two one-arch words, the number of nonuniversal words is \(2+3(a+b)-8=3(n-2)\). Since there are exactly \(\binom nk\) words of the required composition, subtraction proves the first case.

When \(a<3\) or \(b<3\), the target \(000\) or \(111\) is absent, respectively. Thus no word is three-universal, proving the remaining case and completing the proof. \(\square\)

## Verification

The standalone program `check_fixed_weight_3univ.py` independently tests every binary word of lengths zero through sixteen using direct greedy matching of **each of the eight length-three patterns**, not arch counting. It checks all \(153\) length/composition parameter pairs and \(131071\) individual words, including constant words and the smallest admissible cases. Run `python check_fixed_weight_3univ.py`; the expected printed line is `PASS_FIXED_WEIGHT_3_UNIVERSAL n=0..16 words=131071 parameter_pairs=153`. These finite checks corroborate rather than establish the universal quantifier over length; the preceding coefficient proof supplies that step.

## Relationship to prior work

The greedy-arch characterization is classical and is explicitly given as Theorem 1 in Adamson, *Ranking and Unranking k-subsequence universal words* (arXiv:2304.04583). Section 3 of that paper gives counting algorithms for all words of a given length, without the conditional fixed-composition closed form above. Adamson and collaborators, *k-Universality of Regular Languages* (arXiv:2311.10658), give more general automaton counting algorithms: a finite-state condition can encode a prescribed composition, but the inspected results do not establish the composition-independent explicit deficiency. Fleischmann, Germann, and Nowotka, *Scattered Factor Universality — The Power of the Remainder* (arXiv:2104.09063), study the same arch/remnant structure for powers and circular universality, not this conditional enumeration. A previously indexed length-only distribution records the specialization in which the counts of zeros and ones are summed out; it does not supply the separate coefficient for every composition.

The contribution claimed here is **only** the all-length, all-composition three-universality formula and its flat-deficit property. Neither arch factorization nor general algorithms for universality testing and counting are claimed as new.

## Limitations

The argument is specific to binary alphabet size two and target subsequence length three. It does not assert composition independence for four-universality, larger alphabets, or restrictions other than fixed symbol counts. Literature comparisons did not identify this exact formula, but exhaustive bibliographic completeness and independent review are not claimed.

## References

- D. Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583 (first posted 2023-04-10), https://arxiv.org/abs/2304.04583.
- D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, and D. Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658 (first posted 2023-11-17), https://arxiv.org/abs/2311.10658.
- P. Fleischmann, S. Germann, and D. Nowotka, *Scattered Factor Universality — The Power of the Remainder*, arXiv:2104.09063 (first posted 2021-04-19), https://arxiv.org/abs/2104.09063.
- S. Z. Fazekas, X. Huang, and R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, arXiv:2610.06717 (first posted 2026-10-05), https://arxiv.org/abs/2610.06717. Its accessible abstract was considered as a related but nondecisive bibliographic comparison; the full text was unavailable during this review.
