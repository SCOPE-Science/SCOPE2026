# Exact reflection and factor profiles for the characteristic powers-of-two word

## Finding

Index all infinite words from position zero. Define the binary sequence \(c\) by \(c_i=1\) exactly when \(i=2^j-1\) for an integer \(j\ge0\); thus \(c=1101000100000001\cdots\). Put \(c^{+}=0c\), corresponding to the alternative convention where ones are at the positive powers \(1,2,4,8,\ldots\) and position zero is zero. For a word \(x\), let \(\rho_x(n)\) count the distinct contiguous length-\(n\) factors of \(x\). Two factors are equivalent for \(r_x(n)\) when one is the reverse of the other; their reverse need not itself occur.

**Theorem.** For all integers \(n\ge4\),
\[
r_c(n)=2\lceil n/2\rceil+1,\qquad
r_{c^{+}}(n)=2\lceil n/2\rceil+2.
\]
At lengths \(n=0,1,2,3\), both reflection-complexity functions have values \(1,2,3,5\), respectively.

For every \(n\ge4\), let \(B=2^{\lfloor\log_2 n\rfloor}\) and \(t=n-B\), so that \(0\le t<B\). Then
\[
\rho_c(n)=n+B/2+1+\min(B/2,t),\qquad
\rho_{c^{+}}(n)=\rho_c(n)+1.
\]
The initial factor-complexity values are \((\rho_c(0),\rho_c(1),\rho_c(2),\rho_c(3))=(1,2,4,6)\) and \((\rho_{c^{+}}(0),\rho_{c^{+}}(1),\rho_{c^{+}}(2),\rho_{c^{+}}(3))=(1,2,4,7)\). As a consequence,
\[
\liminf_{n\to\infty}\frac{r_c(n)}{\rho_c(n)}=\frac35,
\qquad
\limsup_{n\to\infty}\frac{r_c(n)}{\rho_c(n)}=\frac23,
\qquad
\lim_{n\to\infty}\frac{r_c(n)}n=1.
\]

## Assumptions and scope

Factors are contiguous, not scattered; factors are sets rather than occurrence multisets. Reversal, not cyclic rotation or complementation, defines equivalence. All indices are nonnegative integers. The empty factor forms a single class. The source word is the one-sided sequence with a first position, not its two-sided shift orbit. Consequently the distinction between \(c\) and \(0c\) is genuine at every length \(n\ge4\). The theorem covers all lengths exactly, with no asymptotic hypothesis except in the stated limiting corollary.

## Proof

The positions of ones in \(c\) are \(0,1,3,7,15,\ldots\), and the successive distances between ones are \(1,2,4,8,\ldots\). These distances strictly increase. Thus every length-\(n\) factor with at least two ones uniquely identifies the pair of its first two ones from their distance \(d\), where \(d\) is a power of two. No two different distances or different start positions produce the same such factor. A factor with three or more ones has strictly increasing consecutive one-gaps, whereas its reversal has strictly decreasing gaps; hence its reversal cannot occur.

For every \(n\ge1\), the zero word of length \(n\) and each of the \(n\) words with exactly one one occur as factors: sufficiently distant powers of two provide any prescribed left/right padding. Under reversal, the one-one words form precisely \(\lceil n/2\rceil\) classes. The baseline is therefore \(1+\lceil n/2\rceil\) reversal classes and \(n+1\) distinct factors.

Fix a successive one-gap \(d=2^j\ge2\), and write \(h=d/2\). The two ones delimiting that gap occur at \(d-1\) and \(2d-1\), with the preceding one at \(h-1\) and the following one at \(4d-1\). A length-\(n\) factor whose *first two* ones are this pair must have precisely \(a\) zeros on the left and \(b\) positions on the right, with
\[
0\le a<h,\qquad b=n-d-1-a\ge0.
\]
Any such choice uniquely defines a factor (possibly containing further ones on the right). Hence the number of these factors is
\[
N_d(n)=\min\{h,\max(0,n-d)\}.
\]
Their reversals can occur only if they contain exactly two ones. If the reflected factor occurs, it must contain the *same unique adjacent pair* at gap \(d\), so its left padding is \(b\). This occurs exactly when \(0\le a,b<h\). Conversely, under these inequalities the original and reversed two-one factors both occur. Let \(u=n-d-1\). The number of such factors within the mutually reversible subset is
\[
S_h(u)=\max\bigl(0,\min(h-1,u)-\max(0,u-h+1)+1\bigr).
\]
This subset consists of reversal pairs, with at most one central palindrome. Therefore the number of reversal classes arising from the gap \(d\) is
\[
Q_d(n)=N_d(n)-\left\lfloor\frac{S_h(u)}2\right\rfloor
=\min\left\{h,\max\left(0,\left\lfloor\frac{n-d+1}2\right\rfloor\right)\right\}.
\]
The last equality follows by considering \(u<0\), \(0\le u<h\), \(h\le u<2h-1\), and \(u\ge2h-1\). Equivalently, \(Q_d(n)\) counts the odd integers \(m\) in \(d<m<2d\) with \(m\le n\). The dyadic intervals \((d,2d)\) for \(d=2,4,8,\ldots\) partition the odd integers \(m\ge3\). Thus, for \(n\ge2\),
\[
\sum_{d\in\{2,4,8,\ldots\}}Q_d(n)=\lceil n/2\rceil-1.
\]

The exceptional gap \(d=1\) is the unique leading occurrence of \(11\) at positions \(0,1\) in \(c\). For every \(n\ge2\), exactly one factor begins with this occurrence, contributing one reflection class; its reversal never coincides with a *different* factor from any other gap. It follows, for \(n\ge2\), that
\[
r_c(n)=1+\lceil n/2\rceil+1+(\lceil n/2\rceil-1)
=2\lceil n/2\rceil+1.
\]
In particular the value at \(n=3\) is \(5\); the other small values are immediate. For \(c^{+}=0c\), the same multi-one factors from gaps \(d\ge2\) occur. The leading gap \(1\) now occurs in two factors for every \(n\ge3\): one starting at position zero and one at position one. At \(n=3\) they are \(011\) and \(110\), a single reversal class. For \(n\ge4\), they are not reversals (each length-\(n\) factor with at least three ones has no reversing mate; at \(n=4\) the prefix \(0110\) is a palindrome and the other factor is \(1101\)). Hence the leading gap contributes two classes at all \(n\ge4\), exactly one more than for \(c\), and the reflection formula follows.

To enumerate *distinct* factors, retain \(N_d(n)\) without identifying reversals. For \(n\ge4\), let \(B\le n<2B\) be the highest power of two not exceeding \(n\). All gaps \(d\in\{2,4,\ldots,B/2\}\) contribute their saturated counts \(d/2\), summing to \(B/2-1\), while the gap \(d=B\) contributes \(\min(B/2,n-B)\) and larger gaps contribute zero. Include the \(n+1\) zero/one-one factors and the single factor from gap one:
\[
\rho_c(n)=(n+1)+1+(B/2-1)+\min(B/2,n-B)
=n+B/2+1+\min(B/2,n-B).
\]
The extra starting position in \(0c\) adds one new factor for \(n\ge3\) (and does not change counts at smaller lengths), giving the other formula and all initial values.

Finally, putting \(t/B\to s\in[0,1]\) along dyadic scales,
\[
\frac{\rho_c(n)}n\longrightarrow
\frac{3/2+s+\min(1/2,s)}{1+s}.
\]
This function has minimum \(3/2\) at \(s=0\) and \(s=1\), and maximum \(5/3\) at \(s=1/2\); all three values are approached along integer sequences of lengths. Since \(r_c(n)/n\to1\), the ratio bounds follow by taking reciprocals.

## Verification

The accompanying `verify.py` builds the powers-of-two characteristic prefix for each tested length and directly constructs *all distinct factors* and their reversal equivalence classes. It checks both boundary conventions, lengths \(1\) through \(180\) and fourteen longer lengths through \(1025\), for \(388\) exact factor/reflection enumerations. Separately it checks the dyadic-gap identity and the crucial counting equivalence for all \(n=4,\ldots,65536\). It reports `VERIFY_OK` on success. The computational tests do not replace any part of the infinite proof above.

## Relationship to prior work

Allouche, Campbell, Li, Shallit, and Stipulanti introduced reflection complexity, proved it is computably regular for automatic sequences, and evaluated other classical automatic examples, including the Thue–Morse and period-doubling sequences [1]. Their general result guarantees a representation can be computed for this automatic word, but does not itself give the closed expression established here. Cassaigne, Gheeraert, Restivo, Romana, Sciortino, and Stipulanti used the same powers-of-two characteristic word as Example 13 in their work on string-attractor complexities [2], establishing its linear-order factor complexity and logarithmic-order attractor profile. Those orders do not imply the exact reversal-class profile, the boundary effect, or the stated oscillation constants. Dvořáková and Pelantová's subsequent general reflection-complexity characterizations concern a different minimum-growth regime [3]. Earlier descriptions or tables for this specific sequence remain a possible priority source; this result does not claim that general automaticity, linear factor growth, or the word itself is new.

## Limitations

This is a theorem for the one specific binary powers-of-two characteristic sequence and its one-leading-zero variant, not an arbitrary lacunary support or an arbitrary automatic word. The source is not recurrent, and one-sided boundary conventions matter. A relevant exact formula may exist in literature not indexed by the targeted searches. Only a review of the proof and the source comparisons described in the accompanying review has been performed; independent mathematical validation is outstanding.

## References

1. J.-P. Allouche, J. M. Campbell, S. Li, J. Shallit, M. Stipulanti, *The reflection complexity of sequences over finite alphabets*, arXiv:2406.09302 (first posted 2024-06-13), https://arxiv.org/abs/2406.09302.
2. J. Cassaigne, F. Gheeraert, A. Restivo, G. Romana, M. Sciortino, M. Stipulanti, *New string attractor-based complexities for infinite words*, J. Combin. Theory Ser. A 208 (2024), 105936, DOI:10.1016/j.jcta.2024.105936. Public repository record dated 2023-12-11: https://orbi.uliege.be/handle/2268/309672.
3. L. Dvořáková, E. Pelantová, *Reflection on the reflection complexity*, arXiv:2511.12358 (2025), https://arxiv.org/abs/2511.12358.
