# Marked-repetition spectrum of geometric-support automatic words

## Finding

For an integer base \(B\ge2\), let the one-sided binary word \(w_B\) be given, at zero-based positions, by
\[
w_B(n)=\begin{cases}1,&n=B^j\text{ for some integer }j\ge0,\\0,&\text{otherwise}.\end{cases}
\]
A *marked repetition* is a finite factor containing at least one \(1\) whose least positive period \(p\) satisfies \(2p\le\ell\), where \(\ell\) is its length. Factors are indexed by a starting position \(s\ge0\), with end-exclusive interval \([s,s+\ell)\).

**Complete classification.** The marked repetitions are exactly the following factors, with no duplication of \((s,p,\ell)\). Choose an integer \(a\ge0\), put \(p=(B-1)B^a\), choose an integer \(x\) from the following ranges,
\[
\begin{array}{c|c}
\text{case}&\text{allowable }x\\\hline
 a=0,\ B=2&\{0\}\\
 a=0,\ B\ge3&\{0,1\}\\
 a\ge1&\{0,1,\ldots,(B-1)B^{a-1}-1\},
\end{array}
\]
and set \(s=B^a-x\). Every integer length in
\[
\boxed{2p\le\ell\le 2p+x}
\]
then gives a marked repetition of least period \(p\), and there are no others. Thus all nonzero squares have half-lengths \((B-1)B^a\), and no factor containing \(1\) is a cube.

For \(a\ge1\), write \(M_a=(B-1)B^{a-1}\). The exact number of **distinct marked squares** of length \(2(B-1)B^a\) is \(M_a\); the exact number of **distinct marked repetitions** of least period \((B-1)B^a\), over all possible lengths, is \(M_a(M_a+1)/2\). At \(a=0\) these counts are respectively \(1,1\) when \(B=2\), and \(2,3\) when \(B\ge3\). All other square lengths have no marked square factors. Consequently, if \(m\ge0\) is the largest integer with \(2(B-1)B^m\le N\), the number of distinct marked squares of length at most \(N\) is \(B^m\) for \(B=2\) and \(B^m+1\) for \(B\ge3\); it is zero if no such \(m\) exists.

The marked critical exponent, meaning the supremum of \(\ell/p\) over **all factors containing \(1\)** with \(p\) their least period, is
\[
\boxed{\operatorname{ce}_1(w_B)=
\begin{cases}
5/2,&B=2,\\
2+1/(B-1),&B\ge3.
\end{cases}}
\]
For \(B=2\), this supremum is not attained. For every \(B\ge3\), it is attained by the prefix of length \(2B-1\), which has least period \(B-1\).

## Assumptions and scope

The base is any integer \(B\ge2\), including composite bases. Position \(0\) is not marked, while position \(1=B^0\) is marked. The period of a word of length \(\ell\) means the smallest integer \(p\ge1\) with equality of letters at distance \(p\) wherever both letters lie in the word. An ordinary square is \(uu\), where \(u\) is nonempty. The ordinary critical exponent of \(w_B\) is infinite because its zero runs are arbitrarily long, so the marked critical exponent expressly excludes all-zero factors. All stated counts are of distinct finite words, not just occurrences.

The language is naturally automatic: the marked integers have base-\(B\) representations in the regular language consisting of a leading \(1\) followed by zero or more \(0\) digits.

## Proof

**1. Distinct marker differences.** Suppose \(a<b\) are nonnegative integers. Then
\[
B^b-B^a=B^a(B^{b-a}-1),\qquad B^{b-a}-1\equiv-1\pmod B.
\]
The largest power of \(B\) dividing this difference is precisely \(B^a\), even for composite \(B\). Therefore equality \(B^b-B^a=B^d-B^c\) with \(a<b\) and \(c<d\) implies \(a=c\), then \(b=d\). In particular, at any specified distance \(p>0\) there is **at most one ordered pair of marked positions**.

**2. Structure of squares.** Let \(w_B[s:s+2p)\) be a square containing \(1\). Each marked position in the first half must be paired with a marked position in the second half at distance exactly \(p\). The uniqueness just proved implies there is exactly one such pair, with no other marks anywhere in the square. The two marks must be consecutive powers \(B^a,B^{a+1}\), since any intervening power lies between them and would be inside the factor. Hence \(p=(B-1)B^a\) and \(s=B^a-x\), with \(0\le x<p\).

For \(a\ge1\), the previous mark \(B^{a-1}\) must be strictly before the factor, so \(s\ge B^{a-1}+1\) and
\[
0\le x\le B^a-B^{a-1}-1=(B-1)B^{a-1}-1.
\]
Conversely, these inequalities leave exactly the two designated marks inside the factor: the next mark \(B^{a+2}\) lies past its right endpoint, since
\[
s+2p\le B^a+2(B-1)B^a=(2B-1)B^a<B^{a+2}.
\]
Their offsets differ by exactly \(p\), so the two halves agree. For \(a=0\), nonnegative \(s\) and \(0\le x<p\), with \(B^0=1\), give precisely \(x=0\) if \(B=2\), and \(x=0,1\) if \(B\ge3\). This proves both necessity and sufficiency of the square cases.

The period \(p\) is the *least* period: a shorter positive period \(d<p\) would force a mark at \(B^a+d\) within the factor, whereas the next mark is \(B^{a+1}=B^a+p\). Thus no smaller period works.

**3. Maximal extensions.** Let a marked square be as classified. After its \(2p\) letters, exactly \(x\) further zero letters repeat the first \(x\) letters of the first block. At the next position, periodicity fails: the symbol at offset \(2p+x\) would have to be \(1\), copying the mark at offset \(x\), but the actual location is
\[
s+2p+x=B^a+2p=(2B-1)B^a,
\]
which is strictly between \(B^{a+1}\) and \(B^{a+2}\) and is therefore unmarked. This establishes exactly the length interval \(2p\le\ell\le2p+x\) for each start and period. Conversely, any marked repetition contains its first \(2p\) letters as a marked square: if the mark were only beyond those first \(2p\) letters, periodicity would copy it into the first two blocks, a contradiction. Hence the list is exhaustive.

**4. Counting distinct words.** For \(a\ge1\), the possible offsets are exactly \(x=0,\ldots,M_a-1\), so there are \(M_a\) marked squares and \(\sum_{x=0}^{M_a-1}(x+1)=M_a(M_a+1)/2\) marked repetitions. Different offsets locate the first mark differently; different lengths are distinct; different scales have different gaps between their two marks. Thus none of these words coincide. The base cases follow from \(x=0\) or \(x=0,1\). Summing \(M_a\) gives \(\sum_{a=1}^{m}(B-1)B^{a-1}=B^m-1\), proving the cumulative count.

**5. Sharp exponents.** At \(a\ge1\), the largest attainable exponent is
\[
2+\frac{M_a-1}{(B-1)B^a}=2+\frac1B-\frac1{(B-1)B^a}.
\]
At \(a=0\), the largest exponent is \(2\) for \(B=2\) and \(2+1/(B-1)\) for \(B\ge3\). Taking the supremum yields the stated dichotomy; in base \(2\), the increasing exponents tend to \(5/2\) without attaining it. Any factor of exponent less than \(2\) cannot increase this supremum. Also, every factor of exponent at least \(3\) containing a mark would be a marked repetition longer than the maximum possible \(2p+x<3p\); hence no marked cube exists.

## Verification

The accompanying `verify.py` constructs the word directly from its support and independently enumerates all marked square occurrences for bases \(2\) through \(8\), all half-periods from \(1\) through \(150\), and every admissible start within a prefix of length \(2400\). It compares these against the explicit square-start formula. At every detected square it independently checks all predicted continuation lengths, the first disallowed continuation, and the absence of shorter periods. Its successful output is:

```text
VERIFY_OK bases=2..8 periods=1..150 marked_square_windows= 372192 square_occurrences= 223 maximal_length_checks= 3376
```

These finite diagnostics are independent consistency checks. The proof above, not the finite test, establishes the unbounded quantifiers.

## Relationship to prior work

The work of Shallit and Xu (2023) studies repetition factorization and period predicates for automatic words, including Fibonacci, Thue–Morse, paperfolding and Rudin–Shapiro sequences. It neither states this geometric-support marked-repetition classification nor the two-base critical-exponent dichotomy. Allouche, Rampersad and Shallit (2024, original public version) determine the *minimum critical exponent across classes* of automatic binary sequences, rather than the marked exponent of this fixed sparse word. Schaeffer and Shallit (2020) analyze string attractors of the powers-of-two characteristic sequence; their same-word material concerns attractor positions and sizes, not the square language. The precise one-sided indexing used here matters: an initial shift changes the exceptional \(a=0\) cases.

## Limitations

The critical exponent qualified by a marked symbol is deliberately distinct from the ordinary critical exponent, which is infinite for this word. The classification concerns **ordinary periodicity**, not Abelian or approximate periods. It does not establish a general theorem for arbitrary lacunary supports with non-geometric gaps. Literature comparison is bounded to accessible records and full-text sections; an equivalent result not indexed by these searches remains possible. No independent scientific validation has been performed.

## References

1. J. Shallit and X. Xu, *Repetition factorization of automatic sequences* (first publicly available 2023-11-25), https://arxiv.org/abs/2311.14961.
2. J.-P. Allouche, N. Rampersad and J. Shallit, *Repetition Threshold for Binary Automatic Sequences* (first publicly available 2024-06-10), https://arxiv.org/abs/2406.06513.
3. L. Schaeffer and J. Shallit, *String Attractors for Automatic Sequences* (first publicly available 2020-12-12), https://arxiv.org/abs/2012.06840.
4. A. Baranwal, J. Currie, L. Mol, P. Ochem, N. Rampersad and J. Shallit, *Antisquares and Critical Exponents* (first publicly available 2022-09-19), https://arxiv.org/abs/2209.09223.
