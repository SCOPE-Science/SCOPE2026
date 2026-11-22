# Exact Hamming quantization spectrum of binary words avoiding `010`

## Finding

Let \(\mathcal C_n\subseteq\{0,1\}^n\) consist of binary words with **no ordinary contiguous occurrence** of `010`. For every \(y\in\{0,1\}^n\), put
\[
d_n(y)=\min_{x\in\mathcal C_n}d_{\rm H}(x,y),\qquad
P_n(u)=\sum_{y\in\{0,1\}^n}u^{d_n(y)}.
\]
For all integers \(n\ge0\), with the empty word included at \(n=0\), the complete quantization-distance distribution is given by
\[
\boxed{\sum_{n\ge0}P_n(u)z^n=\frac{1+z^2}{1-2z+z^2-(1+u)z^3}.}
\]
More strongly, \(d_n(y)\) equals the largest number of **pairwise disjoint occurrences** of `010` in \(y\); the leftmost-first greedy scan computes it, and an optimum Hamming quantizer can be constructed in linear time.

The exact covering radius is \(R_n=\lfloor n/3\rfloor\). For \(k\ge0\), the numbers of words at that maximum distance (deep holes) are
\[
\boxed{H_{3k}=1,\qquad H_{3k+1}=2k+2,\qquad H_{3k+2}=2k^2+5k+4.}
\]
For uniform independent unbiased source bits, the quantization-distance random variable \(D_n\) satisfies
\[
\boxed{\mathbb E D_n=n/10+O(1),\qquad
\operatorname{Var}(D_n)=29n/500+O(1).}
\]
In particular, the typical normalized quantization cost tends to \(1/10\) in probability, while the worst normalized cost tends to \(1/3\). The deep-hole probability is exactly \(H_n/2^n\), and hence at most polynomially many source words meet the worst-case radius.

## Assumptions and scope

Symbols are the fixed binary alphabet \(\{0,1\}\). Hamming distance counts substituted **positions** with no insertions or deletions. Forbidden factors and occurrence intervals are linear, not wraparound; \(\mathcal C_n\) contains **all** finite length-\(n\) `010`-avoiding words. A pairwise disjoint occurrence family has disjoint three-position intervals. No code-linearity, periodicity, or random-source assumption is used for the finite exact identities. The expectation and variance statements assume uniform independent Bernoulli-\(1/2\) input bits. For \(n<3\), all words are admissible, as the formulas imply.

## Proof

**1. Disjoint occurrence packing is exactly Hamming correction cost.** Let \(s_1<\cdots<s_m\) be the starting indices of every occurrence of `010` in a fixed input word, indexed from zero. Consecutive starts cannot differ by one: that would demand the same symbol be both zero and one. Break the starts into maximal runs of successive differences exactly two. Distinct runs are separated by a difference at least three, so their occurrence intervals are disjoint from one another.

For a run of \(q\) occurrences starting at \(s,s+2,\ldots,s+2(q-1)\), the maximum number of disjoint occurrence intervals is \(\lceil q/2\rceil\), obtained by selecting every second interval. Summing over runs gives the overall maximum disjoint-occurrence packing number \(\nu(y)\). Any correction to an avoiding word must change at least one position in each interval of a disjoint occurrence packing; thus \(d_n(y)\ge\nu(y)\).

For the reverse inequality, group a run's first two occurrences, next two, and so on. Each paired overlap occupies `01010`; flip its shared **zero** to one, turning it into `01110`. If \(q\) is odd, flip the **central one** of its last, unpaired `010` to zero. All selected flip positions have separation at least two, including between different runs. Each flipped zero has two unchanged original neighboring ones, and so cannot be the center of a newly created `010`. Each flipped one has two unchanged original neighboring zeros, and so cannot be an endpoint of a newly created `010`. Since the flipped symbols could occur in `010` only at those respective positions, no new occurrence is created. Every original occurrence is destroyed. The number of flips is \(\sum\lceil q/2\rceil=\nu(y)\). Therefore \(d_n(y)=\nu(y)\), and the described flips give a constructive optimum.

**2. Greedy packing and exact enumerator.** Among equal-length occurrence intervals, greedily taking the earliest-ending available interval maximizes their number: replacing the first interval of any optimal packing by the earliest-ending one cannot invalidate later intervals, and induction finishes the proof. Hence a left-to-right scan that records `010` then resumes **after** its last symbol computes \(d_n(y)\).

A three-state deterministic weighted automaton implements that scan. State \(0\) has no pending prefix, state \(1\) has pending prefix `0`, and state \(2\) has pending prefix `01`. Reading `010` from state \(2\) contributes a factor \(u\) and returns to state \(0\), because overlapping occurrences are not counted. Its weighted transition matrix, with source states in rows, is
\[
M(u)=\begin{pmatrix}1&1&0\\0&1&1\\1+u&0&0\end{pmatrix}.
\]
The polynomial for length \(n\) is \(P_n(u)=e_0^{\mathsf T}M(u)^n\mathbf1\), so formal power-series inversion yields
\[
\sum_{n\ge0}P_n(u)z^n=e_0^{\mathsf T}(I-zM(u))^{-1}\mathbf1
=\frac{1+z^2}{1-2z+z^2-(1+u)z^3}.
\]
Equivalently, \(P_0=1\), \(P_1=2\), \(P_2=4\), and for \(n\ge3\),
\[
P_n(u)=2P_{n-1}(u)-P_{n-2}(u)+(1+u)P_{n-3}(u).
\]
This gives the full integer spectrum rather than only the largest distance.

**3. Radius and deep holes.** There are at most \(\lfloor n/3\rfloor\) disjoint three-symbol intervals, and \((010)^k\) with any remaining suffix realizes \(k=\lfloor n/3\rfloor\). Thus the radius equals \(k\). Set \(Q(z)=1-2z+z^2-z^3\). Expanding the rational enumerator in powers of \(u\) gives
\[
[u^k]\sum_{n\ge0}P_n(u)z^n
=\frac{z^{3k}(1+z^2)}{Q(z)^{k+1}}.
\]
The number of deep holes at length \(3k+r\), for \(r\in\{0,1,2\}\), is the coefficient of \(z^r\) in \((1+z^2)Q(z)^{-k-1}\). Its first three coefficients are respectively \(1\), \(2(k+1)\) and \(2k^2+5k+4\), proving the stated classification by counts.

**4. Uniform-source moments.** Write \(G(t,u)=\sum_{n\ge0}2^{-n}P_n(u)t^n\). Exact differentiation at \(u=1\) gives
\[
\partial_uG(t,1)=\frac{t^3}{8(1-t)^2(1+t^2/4)},\qquad
\partial_{uu}G(t,1)=\frac{t^6}{32(1-t)^3(1+t^2/4)^2}.
\]
Expanding at the only singularity on the unit circle, \(t=1\), the first expression is \(1/[10(1-t)^2]-13/[50(1-t)]+O(1)\), and the second is \(1/[50(1-t)^3]-13/[125(1-t)^2]+O((1-t)^{-1})\). All other poles are at \(t=\pm2i\). Coefficient extraction yields \(\mathbb ED_n=n/10-4/25+o(1)\). Combining the second factorial moment with \(\mathbb ED_n\) and \((\mathbb ED_n)^2\) gives \(\operatorname{Var}(D_n)=29n/500+O(1)\). Chebyshev's inequality implies \(D_n/n\to1/10\) in probability.

## Verification

Run `python3 verify.py` using only Python 3's standard library. The script independently computes minimum Hamming correction cost by dynamic programming over allowable output suffixes, and compares it to greedy packing and the explicit optimum correction construction for **all 65,535 binary inputs of lengths zero through fifteen**. It additionally compares every resulting distance histogram with exact coefficients of the claimed rational series and validates the radius/deep-hole formulas and normalization through length 180. Its terminal success text is `VERIFY_OK`.

These computations are finite corroboration. The all-length statements follow from the occurrence-run proof, automaton identity and rational-function coefficient argument above, not from finite testing.

## Relationship to prior work

Elimelech, Meyerovitch and Schwartz (2023), *Quantized-Constraint Concatenation and the Covering Radius of Constrained Systems*, introduced the constrained-system covering-radius and essential-radius framework. Their Example 1 and Theorem 14 give worst-case and essential quantization radii for **homogeneous run-length constraints** (forbidding long runs of zeros), whereas this theorem studies the mixed factor `010` and determines the **entire finite-length distortion distribution**, deep-hole counts and moments. The target result is not a corollary of those displayed run-length formulas. Their general constrained-system methods motivate the question but do not supply this specific computation.

*Exact cyclic-cover lengths for binary words avoiding `010`* studies the same finite forbidden-factor language but minimizes the **length of a single circular word containing all admissible factors**. Its ordinary avoidance counting series is obtained here at \(u=0\), but that scalar specialization contains no Hamming-distance or deep-hole information. Cyclic covering and Hamming quantization have different objective functions and feasibility witnesses. Search comparisons also considered approximate pattern matching with substitutions, which measures distance *to occurrence of a pattern*, not to the class avoiding that pattern.

## Limitations

The exact formulas are restricted to one forbidden factor `010` (equivalently `101` under bit complement), binary linear words, and Hamming substitutions. No claim is made about cyclic source words, insertion/deletion distance, general forbidden languages, or optimal practical encoder implementations. While relevant literature and the available indexed research records were checked, an unindexed formulation or a general theorem with this case implicit remains a priority risk. Self-review is not an independent mathematical audit.

## References

1. D. Elimelech, T. Meyerovitch and M. Schwartz, *Quantized-Constraint Concatenation and the Covering Radius of Constrained Systems*, arXiv:2302.02363, first public submission 2023-02-05. https://arxiv.org/abs/2302.02363 ; primary full text https://arxiv.org/pdf/2302.02363 .
2. *Exact cyclic-cover lengths for binary words avoiding `010`*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-cyclic-cover-lengths-for-binary-words-avoiding-010--c88f5aa31843 .
3. P. Charalampopoulos, T. Kociumaka and P. Wellnitz, *Faster Approximate Pattern Matching: A Unified Approach*, arXiv:2004.08350, 2020. https://arxiv.org/abs/2004.08350 .
