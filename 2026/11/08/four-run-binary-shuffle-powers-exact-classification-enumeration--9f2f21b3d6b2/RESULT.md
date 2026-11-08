# Four-run binary shuffle powers: exact classification, enumeration, and limiting density

## Finding

For an integer \(q\ge3\), a nonempty word is a *\(q\)-shuffle power* if its positions can be partitioned into \(q\) disjoint subsequences all reading the same word. For positive integers \(a,b,c,d\), let
\[
W=0^a1^b0^c1^d.
\]
The following characterization is exact. If either \(q\nmid(a+c)\) or \(q\nmid(b+d)\), then \(W\) is not a \(q\)-shuffle power. Otherwise set
\[
A=(a+c)/q,\qquad B=(b+d)/q.
\]
Then \(W\) is a \(q\)-shuffle power **if and only if**
\[
\boxed{\big(q\mid a,\ q\mid b,\ q\mid c,\ q\mid d\big)
\quad\text{or}\quad
\left\lceil\frac{b}{B}\right\rceil\le
\left\lfloor\frac{a}{A}\right\rfloor.}
\]
The result also applies mathematically to \(q=2\), where the decision criterion recovers a published classification; the claimed novelty begins at \(q=3\).

For fixed \(q\ge3\), \(A,B\ge1\), let \(S_q(A,B)\) be the number of positive quadruples \((a,b,c,d)\) with \(a+c=qA\), \(b+d=qB\) for which the above word is a \(q\)-shuffle power. This is a count of **distinct words**, not labeled partitions. Then
\[
\boxed{S_q(A,B)=\frac{q(q-1)}2AB+(A-1)(B-1)-
\sum_{\alpha=1}^{A-1}\left\lfloor
\frac{B}{q}\left\lfloor\frac{q\alpha}{A}\right\rfloor
\right\rfloor.}
\]
For each fixed \(q\ge3\), as \(A,B\) independently tend to infinity, the limiting proportion among the \((qA-1)(qB-1)\) four-run words of this composition is
\[
\boxed{\delta_q=\frac{q^3-q^2+q+1}{2q^3}.}
\]
In particular \(\delta_3=11/27\). Including the known \(q=2\) boundary value \(\delta_2=7/16\), the proportion is uniquely minimized at \(q=3\) among integer \(q\ge2\), and increases strictly for \(q>3\), tending to \(1/2\).

## Assumptions and scope

The alphabet is \(\{0,1\}\); all four runs have strictly positive length. A subsequence preserves order but need not be contiguous. Each source position is used in exactly one of the \(q\) copies. The copies must be identical and nonempty. Both \(A\) and \(B\) are positive integers whenever the two divisibility tests hold. Asymptotics hold for **fixed** \(q\), with both \(A\to\infty\) and \(B\to\infty\); no uniform-in-\(q\) assertion is made.

## Proof

**1. Possible common roots.** If a \(q\)-fold partition exists, every copy begins with \(0\) and ends with \(1\). Indeed, the earliest source symbol is \(0\) and is first in its copy, whereas the latest symbol is \(1\) and is last in its copy; all copies are identical. Their common one-count and zero-count are respectively \(B\) and \(A\), giving the necessary divisibility conditions. Any subsequence of the four-run source that starts with \(0\) and ends with \(1\) has either two or four maximal runs. Thus its common root is either \(0^A1^B\) or \(0^u1^v0^{A-u}1^{B-v}\), where \(1\le u<A\) and \(1\le v<B\).

**2. Four-run roots.** For any copy with four runs, its first \(1\) must come from the source's second run and its later \(0\) from the third run. Consequently the initial and final zero blocks, and both one blocks, are wholly confined to their corresponding source runs. All \(q\) identical copies contribute the same number of positions to each source run; hence \(q\) divides each of \(a,b,c,d\). Conversely, when all four exponents are multiples of \(q\), partition each source run evenly among \(q\) copies, obtaining the common four-run root \(0^{a/q}1^{b/q}0^{c/q}1^{d/q}\).

**3. Two-run roots.** Suppose every copy is \(0^A1^B\). Let \(k\) be the number of copies receiving at least one \(1\) from the source's second run of length \(b\). Those \(k\) copies must already have received all their \(A\) zeros from the first run, so \(kA\le a\). They can receive at most \(kB\) ones, so \(b\le kB\). Thus
\[
\left\lceil b/B\right\rceil\le k\le\left\lfloor a/A\right\rfloor.
\]
Conversely suppose the displayed inequality holds and set \(k=\lceil b/B\rceil\). Since \(b>0\), \(1\le k\le q-1\). Allocate \(kA\) initial zeros to the first \(k\) copies; distribute the remaining \(a-kA\) initial zeros among the other \(q-k\) copies, never exceeding \(A\) zeros per copy (this is possible because \(a\le qA\)). Then place all \(b\) ones in the first \(k\) copies, between one and \(B\) per copy; existence follows from \(k=\lceil b/B\rceil\), \(b\ge k\), and \(b\le kB\). Complete the remaining \(qA-a=c\) zeros in the third source run, exclusively among the other \(q-k\) copies. Finally distribute the last \(qB-b=d\) ones to complete each copy to \(B\). This yields a partition into identical roots \(0^A1^B\). Steps 2 and 3 prove the criterion.

**4. Enumeration.** With \(a+c=qA\), \(b+d=qB\), a word is specified uniquely by \(1\le a\le qA-1\), \(1\le b\le qB-1\). Let \(P\) be the set satisfying the two-run inequality, and \(E\) the set with all four run lengths divisible by \(q\). For each integer \(r=1,\ldots,q-1\), there are precisely \(A\) admissible values of \(a\) with \(\lfloor a/A\rfloor=r\). Each allows precisely \(rB\) values of \(b\), hence
\[
|P|=AB\sum_{r=1}^{q-1}r=\frac{q(q-1)}2AB.
\]
In \(E\), write \(a=q\alpha\), \(b=q\beta\) with \(1\le\alpha\le A-1\) and \(1\le\beta\le B-1\). Thus \(|E|=(A-1)(B-1)\), while \(P\cap E\) contains, for each fixed \(\alpha\), precisely
\[
\left\lfloor \frac{B}{q}\left\lfloor\frac{q\alpha}{A}\right\rfloor\right\rfloor
\]
permitted \(\beta\)'s. Inclusion–exclusion proves the exact sum formula (also when \(A=1\) or \(B=1\), where empty sums are zero).

**5. Density and its minimum.** For fixed \(q\), a partition of the interval \([0,1]\) into \(q\) equal pieces gives
\[
\sum_{\alpha=1}^{A-1}\left\lfloor\frac{q\alpha}{A}\right\rfloor
=\frac{q-1}{2}A+O_q(1).
\]
Rounding the remaining outer floors adds \(O(A)\); hence the intersection term is \(AB(q-1)/(2q)+O_q(A+B)\). Substitution yields
\[
S_q(A,B)=\frac{q^3-q^2+q+1}{2q}AB+O_q(A+B),
\]
which gives \(\delta_q\) after division by \((qA-1)(qB-1)\). Regard the same rational expression as a function of a real variable \(x\ge2\). Its derivative is \((x-3)(x+1)/(2x^4)\). It decreases from \(2\) to \(3\), then increases strictly. Hence the integer minimum is attained exactly at \(q=3\).

## Verification

The standalone Python 3 program `VERIFY.py` uses an independent state-space exploration of all unlabeled partial copies, retaining only states in which all partial tracks are prefixes of a common possible root. It compares exact acceptance with the closed criterion for 286 valid four-run configurations with \(q\in\{2,3,4\}\) and exponents at most five. It also compares the arithmetic enumeration against direct enumeration of all compositions for 1,372 parameter triples with \(2\le q\le8\), \(1\le A,B\le14\). Numerical large-composition checks inspect the limiting constant for \(q=2,\ldots,7\). All checks passed. These finite experiments support but do not prove the universally quantified assertions; the proof above supplies their infinite justification. Run: `python3 VERIFY.py`.

## Relationship to prior work

Grytczuk, Pawlik, and Pleszczyński (2023, first public 2023-08-26) study shuffle squares, generalized similarity, and their enumerative and computational questions. Grytczuk, Pawlik, and Ruciński (2025), Proposition 2, treat exactly **two** shuffled copies in four-run binary words, including the parity exception; the \(q=2\) instance here is therefore not claimed as new. The present result is the quantified \(q\ge3\) equal-subsequence classification and the exact count and sharp asymptotic density across all \(q\). The literature comparisons did not identify a published formula implying these conclusions. Published complexity and avoidance results for shuffle closures of arbitrary multiplicity address broader languages but do not automatically supply this concrete four-run count.

## Limitations

No claim is made for words with more than four runs, larger alphabets, roots with unequal multiplicities, counting the number of distinct partitions per word, or asymptotics with \(q\) growing with \(A,B\). The novelty assessment is limited by discoverability of published sources, especially alternate terminology such as shuffled cubes, shuffle closure, or interleaving powers. Independent validation has not been conducted.

## References

1. J. Grytczuk, B. Pawlik, M. Pleszczyński, *Variations on shuffle squares*, arXiv:2308.13882 (first public 2023-08-26), https://arxiv.org/abs/2308.13882 .
2. J. Grytczuk, B. Pawlik, A. Ruciński, *Shuffle squares and nest-free graphs*, arXiv:2503.22043 (2025), especially Proposition 2 and Section 3.1, https://arxiv.org/abs/2503.22043 .
3. L. Bulteau, V. Jugé, S. Vialette, *On shuffled-square-free words*, Theoretical Computer Science 941 (2023), 91–103, https://doi.org/10.1016/j.tcs.2022.10.028 .
4. *Subsequence covers of words*, Theoretical Computer Science (2025), https://doi.org/10.1016/j.tcs.2025.115216 (background on shuffle closures with arbitrary copy counts).
5. X. He, E. Huang, I. Nam, R. Thaper, *Shuffle squares and reverse shuffle squares*, arXiv:2109.12455 (2021 preprint; 2024 journal), https://arxiv.org/abs/2109.12455 .
