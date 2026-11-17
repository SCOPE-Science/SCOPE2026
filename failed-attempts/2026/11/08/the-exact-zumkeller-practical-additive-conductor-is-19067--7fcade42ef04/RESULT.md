# The exact Zumkeller–practical additive conductor is \(19067\)

## Finding

Let a **Zumkeller number** be a positive integer whose positive divisors can be partitioned into two sets with equal sums. Let a **practical number** be a positive integer such that every positive integer no greater than it is a sum of distinct positive divisors of it; in particular, \(1\) is practical. Write \(\mathcal Z\) and \(\mathcal P\) for these two sets.

**Theorem.** The largest positive integer outside the sumset \(\mathcal Z+\mathcal P\) is exactly \(19067\):

\[
19067\notin\mathcal Z+\mathcal P,
\qquad
\{n\in\mathbb Z:n\ge19068\}\subseteq\mathcal Z+\mathcal P.
\]

This determines the exact conductor of the additive set studied qualitatively by Somu, Kukla and Tran (2023). Their Proposition 4.10 establishes eventual representability without an explicit threshold.

## Assumptions and scope

All summands are strictly positive integers. A sum uses **one** Zumkeller and **one** practical summand; it need not have two different summands. For \(n\ge19068\), every such integer has at least one representation. No assertion is made about the number of representations or about the complete smaller exceptional set.

For a positive integer \(n\), write \(\sigma(n)=\sum_{d\mid n}d\). A necessary condition for Zumkeller status is that \(\sigma(n)\) is even and \(\sigma(n)\ge2n\). The following exact criterion, valid also for perfect numbers, is used in the finite certificate:

\[
n\in\mathcal Z\iff \sigma(n)\text{ is even and }
\sigma(n)/2-n\text{ is a sum of distinct proper divisors of }n.
\]

For the practical test, if \(1=d_1<d_2<\cdots<d_t=n\) are the positive divisors in increasing order, practicality is equivalent to the gap inequalities \(d_i\le1+\sum_{j<i}d_j\) for each \(i\). Indeed, these inequalities make consecutive intervals of available subset sums overlap; when one fails, the omitted integer \(1+\sum_{j<i}d_j\), which is smaller than \(d_i\le n\), cannot be expressed. The executable checker compares this direct criterion to the classical ordered-prime-power criterion for every even candidate in its entire range.

## Proof

**1. Every even integer at least eight is represented.** Numbers congruent to \(6\) or \(12\) modulo \(18\) are Zumkeller (Somu–Kukla–Tran, Remark 2.3). The practical numbers \(2,4,6,8,12,16\) give, for the nine even residues modulo \(18\), the following choices of (Zumkeller, practical) summands:

| \(n\) | \(z\) | \(p\) | Applicable range |
| --- | --- | --- | --- |
| \(18k\) | \(18(k-1)+6\) | \(12\) | \(k\ge1\) |
| \(18k+2\) | \(18(k-1)+12\) | \(8\) | \(k\ge1\) |
| \(18k+4\) | \(18(k-1)+6\) | \(16\) | \(k\ge1\) |
| \(18k+6\) | \(18(k-1)+12\) | \(12\) | \(k\ge1\) |
| \(18k+8\) | \(18k+6\) | \(2\) | \(k\ge0\) |
| \(18k+10\) | \(18k+6\) | \(4\) | \(k\ge0\) |
| \(18k+12\) | \(18k+6\) | \(6\) | \(k\ge0\) |
| \(18k+14\) | \(18k+12\) | \(2\) | \(k\ge0\) |
| \(18k+16\) | \(18k+12\) | \(4\) | \(k\ge0\) |

**2. Every sufficiently large odd integer is represented by a finite periodic cover.** First, \(945=3^3\cdot5\cdot7\) is Zumkeller: \(\sigma(945)=1920\) and the divisors \(945\) and \(15\) add to \(960\), exactly half the divisor sum. A coprime multiple of a Zumkeller number is Zumkeller: partition divisors of the base number into equal-sum halves and multiply both halves by every divisor of the coprime multiplier. Consequently, \(945m\) is Zumkeller whenever \(\gcd(m,945)=1\).

Put \(M=198450=945\cdot210\), and let
\[
U=\{u:1\le u<210,\ u\text{ odd},\ \gcd(u,105)=1\}.
\]
There are \(48\) elements of \(U\). The finite certificate constructs, for **each of the \(99225\) odd residues** \(r\) modulo \(M\), an even practical integer \(p_r\le539968\) and \(u_r\in U\) such that
\[
p_r+945u_r\equiv r\pmod M,\qquad
p_r+945u_r\le716683.
\]
The checker enumerates all practical candidates exactly, visits every residue, and verifies the asserted maximum; its output is included with the certificate. If \(n\ge716683\) is odd, choose the pair for its residue and write
\[
n=p_r+945(u_r+210t),\qquad
 t=\frac{n-p_r-945u_r}{198450}\in\mathbb Z_{\ge0}.
\]
Since \(\gcd(u_r+210t,945)=1\), the second summand is Zumkeller, proving the whole infinite tail.

**3. The finite bridge.** A direct exact divisor-subset test certifies the \(208\) odd Zumkeller numbers at most \(100000\). For every even practical \(p\le716683\) and each of these odd Zumkeller numbers \(z\), the checker marks \(p+z\) using integer bitsets. Every odd integer in \([19069,716683)\), except \(20177\), is marked. The remaining integer has the explicit representation
\[
20177=20176+1,
\]
where \(1\) is practical and \(20176\) is Zumkeller: \(\sigma(20176)=42532\), and the proper divisors
\[
8,13,26,52,97,104,194,208,388
\]
are distinct, each divides \(20176\), and their sum is \(1090=42532/2-20176\).

**4. Sharpness.** If \(19067=p+z\) with \(p\) practical, either \(p=1\) or \(p\) is even. In the former case \(z=19066\), whose divisor sum is \(28602<2\cdot19066\); hence \(z\) is not Zumkeller. In the latter case \(z\) is odd. The exact certificate checks **every** positive even practical \(p<19067\); for no such \(p\) does \(z=19067-p\) simultaneously have an even divisor sum and satisfy \(\sigma(z)\ge2z\). Therefore no \(z\) can be Zumkeller. This proves that \(19067\) is not represented, completing the classification of the maximal exception.

## Verification

Run `python3 checker.py` using Python 3 with no third-party dependencies. It builds smallest-prime-factor tables, independently compares two complete criteria for practical numbers over all \(358341\) positive even candidates at most \(716683\), proves every needed odd Zumkeller assertion by subset-sum dynamic programming, verifies \(99225\) periodic residue classes, and checks the finite bridge and the sharp obstruction.

Its recorded output is in `verification_output.txt`. A separate direct-divisor implementation was also run through \(25000\), reproducing the maximal missing value \(19067\) without using the prime-factor practical test; that additional calculation is corroboration, not a replacement for the full proof certificate. The infinite step is the modular argument in Step 2, not extrapolation from an interval.

## Relationship to prior work

Somu, Kukla and Tran, *Some Results on Zumkeller Numbers* (first publicly posted 22 October 2023), prove in Proposition 4.10 that all sufficiently large integers are a Zumkeller number plus a practical number; their proof chooses practical representatives modulo \(945^2\) without computing a finite conductor. They separately compute the largest exception \(32761\) for sums of **two Zumkeller numbers**, which is a different additive set. Their Proposition 4.8 provides the even-integer case used above.

The related characterization of practical numbers and OEIS sequences A005153 (practical) and A083207 (Zumkeller) supply individual-summand context, not this mixed-sum conductor. The present result determines both an actual missing integer and a rigorous representation for every larger integer. No claim is made that the earlier qualitative eventual-representability theorem itself is new.

## Limitations

This is a finite-certificate-assisted exact theorem. Its finite bridge and all-residue checks require replaying the standalone integer-arithmetic code. It does not determine every smaller exception or the number of decompositions. A logically equivalent result in unindexed literature or unpublished computations cannot be excluded by the searches performed; independent mathematical audit remains outstanding.

## References

1. S. T. Somu, A. Kukla, D. V. K. Tran, *Some Results on Zumkeller Numbers*, arXiv:2310.14149v2 (2023), https://arxiv.org/html/2310.14149v2, especially Lemma 2.1 and Propositions 4.7–4.10.
2. K. P. S. Bhaskara Rao and Y. Peng, *On Zumkeller numbers*, Journal of Number Theory **133** (2013), 1135–1155.
3. OEIS A083207, *Zumkeller or integer-perfect numbers*, https://oeis.org/A083207.
4. OEIS A005153, *Practical numbers*, https://oeis.org/A005153.
