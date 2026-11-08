# Exact reflection complexity and oscillation of geometric-support automatic words

## Finding

For an integer \(B\ge 2\), let \(w_B=w_B(0)w_B(1)\cdots\) be the binary word
\[
w_B(i)=\begin{cases}1,&i=B^j\text{ for some integer }j\ge0,\\0,&\text{otherwise},\end{cases}\quad i\ge0.
\]
Let \(R_B(n)\) be the number of length-\(n\) factors of \(w_B\), with two factors identified exactly when one equals the other or its reversal. This is the reflection complexity introduced in [1]. Then \(R_B(0)=1\). For \(n\ge1\), the following is a complete, exact all-base formula.

**Initial range.** If \(1\le n<B\), then \(R_B(n)=1+\lceil n/2\rceil\). If \(B\le n\le B(B-1)\), then
\[
R_B(n)=1+\lceil n/2\rceil +\begin{cases}1,&n=B\text{ or }n=B+1,\\2,&n\ge B+2.\end{cases}
\]
The second range is empty if its lower bound exceeds its upper bound; for \(B=2\) it consists only of \(n=2\).

**General range.** If \(n>B(B-1)\), there is a unique integer \(k\ge1\) satisfying
\[
(B-1)B^k<n\le (B-1)B^{k+1}.
\]
Set
\[
s=B^k,\qquad h=B^{k-1},\qquad M=n-1-(B-1)s,\qquad A=s-h-1,
\]
and define
\[
U=\min\{h+M+2,s+1\},\qquad
P=\max\left\{0,\min\left(\left\lfloor\frac{M+1}{2}\right\rfloor,A-\left\lfloor\frac M2\right\rfloor\right)\right\}.
\]
Then
\[
\boxed{R_B(n)=1+\left\lceil\frac n2\right\rceil+U-P-\mathbf1_{\{B=2,\ n=3\}}.}
\]
In particular, for the characteristic word of the powers of two,
\[
\boxed{R_2(0),R_2(1),R_2(2),R_2(3)=1,2,3,5,\qquad R_2(n)=2\lceil n/2\rceil+2\quad(n\ge4).}
\]

**Sharp asymptotic dichotomy.** For every integer \(B\ge2\),
\[
\boxed{\liminf_{n\to\infty}\frac{R_B(n)}n=\frac12+\frac1{B(B-1)},\qquad
\limsup_{n\to\infty}\frac{R_B(n)}n=\frac12+\frac B{(B-1)(B+2)}.}
\]
Thus the normalized reflection complexity converges to \(1\) for \(B=2\), but has two different sharp accumulation endpoints for every \(B\ge3\). In fact, every intermediate value between these endpoints is also a subsequential limit.

## Assumptions and scope

All factors are contiguous, are taken in the one-sided infinite word with zero-based positions, and may start anywhere \(i\ge0\). The symbol at position zero is \(0\), not \(1\). A reversal class includes only factors actually present; the reversal of a factor need not occur. Base \(B\) is a fixed integer at least two, and factor length \(n\) is any nonnegative integer. Every \(w_B\) is \(B\)-automatic because the base-\(B\) representations of its \(1\)-positions have the regular form \(10^*\).

## Proof

**1. Factors with at most one \(1\).** Gaps between successive \(1\)-positions \(B^j\) grow without bound in both directions relative to a sufficiently large marked position. Hence every length \(n\ge1\) zero word occurs, as does the factor with a single \(1\) at each of the \(n\) offsets \(0,\ldots,n-1\). The single-\(1\) words form exactly \(\lceil n/2\rceil\) reversal classes, and the all-zero word contributes one. Therefore their contribution is \(1+\lceil n/2\rceil\).

**2. Uniqueness and possible reflected collisions for multiple \(1\)'s.** In a factor containing at least two \(1\)'s, the first two \(1\)'s occur at successive marked positions \(B^j,B^{j+1}\), with distance \(d_j=(B-1)B^j\). The distances \(d_j\) are all distinct, so the first two offsets identify \(j\) and the factor starting position uniquely. Thus factors containing at least two \(1\)'s occur at exactly one starting position each, and distinct starting positions yield distinct such factors. A factor with at least three \(1\)'s has strictly increasing inter-\(1\) gaps \(d_j,d_{j+1},\ldots\), whereas its reversal has strictly decreasing gaps. Hence the reversal of such a factor never occurs in the word. Every nontrivial pairing of two distinct existing factors under reversal therefore comes from exactly two \(1\)'s.

**3. Short lengths.** The smallest gap between adjacent \(1\)'s is \(d_0=B-1\). If \(n\le d_0\), no factor has two \(1\)'s. In the range \(B\le n\le d_1=B(B-1)\), the only pair of marked positions that fits in a window is \(1,B\). It fits starting at \(i=1\) for all \(n\ge B\), and also at \(i=0\) exactly when \(n\ge B+1\). For \(n=B+1\) the two factors are reversals; for \(n\ge B+2\) they are not. These facts give the initial-range formula (and handle \(B=2,n=2\)).

**4. All positions with at least two \(1\)'s in the general range.** Fix \(n>d_1\) and the unique \(k\ge1\) from the statement. A window of length \(n\) contains both \(B^j,B^{j+1}\) exactly when its start belongs to
\[
I_j=[\max\{0,B^{j+1}-n+1\},B^j]\cap\mathbb Z.
\]
There are no such windows for \(j>k\). Because \(B^k<n\), for every \(j<k\), \(I_j=[0,B^j]\cap\mathbb Z\), and their union is \([0,h]\cap\mathbb Z\). For \(j=k\), the interval is \([\max\{0,s-M\},s]\cap\mathbb Z\). Their union therefore has exactly
\[
\boxed{U=\min\{h+M+2,s+1\}}
\]
positions. By Step 2, \(U\) is also the number of distinct factors with at least two \(1\)'s, *before* reversal identification.

**5. Count the nonpalindromic reflected pairs.** Suppose the only two \(1\)'s lie at \(B^j,B^{j+1}\), and let \(\ell\) and \(r\) be the numbers of zeros before the first and after the second. Thus \(\ell+r=n-1-d_j\). The reversal can occur only at the same uniquely determined marked pair and only if both \(\ell\) and \(r\) are valid leading-zero counts for it.

For \(j\ge1\), any leading-zero count is at most \(d_{j-1}-1=d_j/B-1\). For \(j<k\), since \(n>d_k\ge B d_j\), we have
\[
\ell+r=n-1-d_j\ge (B-1)d_j>2(d_j/B-1),
\]
so two reflected factors with this pair are impossible. For \(j=0\), a valid leading-zero count is at most \(1\). Since \(n>d_1\), the sum \(\ell+r\ge(B-1)^2\), which rules out a pair of distinct reversed factors if \(B\ge3\). For \(B=2\), the only exception is \(n=3\), where the factors `011` and `110` constitute one extra reflected pair; \(n=4\) has only the symmetric padding \((1,1)\), giving a palindrome, not a paired pair. For \(n\ge5\), there is no extra pair at \(j=0\).

For \(j=k\), write \(\ell+r=M\). Absence of the preceding marked position \(h\) requires \(\ell\le A=s-h-1\). Absence of the following position \(B^{k+2}\) imposes no additional restriction since \(M\le (B-1)^2s-1<d_{k+1}\). Thus the possible leading-zero counts are precisely \(\ell\in[0,T]\cap\mathbb Z\), where \(T=\min(A,M)\). Two distinct factors are reversals exactly when their leading-zero counts are \(\ell\) and \(M-\ell\), both in this interval. If \(M\le A\), the number of unordered, distinct such pairs is \(\lfloor(M+1)/2\rfloor\); if \(M>A\), it is \(\max(0,A-\lfloor M/2\rfloor)\). Together these are exactly \(P\) as defined in the statement. Consequently the multiple-\(1\) factors contribute \(U-P-\mathbf1_{\{B=2,n=3\}}\) classes. Adding Step 1 proves the exact formula.

**6. Base two simplification.** For \(B=2\) and \(n\ge5\), write \(s=2h\), so \(0\le M\le s-1\) and \(A=h-1\). For \(M\le h-1\), one has \(U=h+M+2\) and \(P=\lfloor(M+1)/2\rfloor\). For \(M\ge h\), one has \(U=2h+1\) and \(P=h-1-\lfloor M/2\rfloor\). Both yield
\[
U-P=h+\lfloor M/2\rfloor+2=\lceil n/2\rceil+1.
\]
Thus \(R_2(n)=2\lceil n/2\rceil+2\) for \(n\ge5\). Direct evaluation at \(n=0,1,2,3,4\) gives \(1,2,3,5,6\), completing this case.

**7. Normalized asymptotics.** Fix \(B\ge2\), and put \(t=M/s\) and \(a=1-1/B\) for the general range. As \(k\to\infty\), the exact formulas for \(U\) and \(P\) show, uniformly in the allowed \(M\), that
\[
\frac{R_B(n)}n=F_B(t)+O_B(s^{-1}),\qquad
F_B(t)=\begin{cases}
\dfrac12+\dfrac{1/B+t/2}{B-1+t},&0\le t\le2a,\\[6pt]
\dfrac12+\dfrac1{B-1+t},&2a\le t\le(B-1)^2.
\end{cases}
\]
For \(B=2\), this function is identically \(1\). For \(B\ge3\), its first branch increases strictly and its second branch decreases strictly. The two endpoint values agree and equal \(1/2+1/[B(B-1)]\), and the peak at \(t=2a\) equals \(1/2+B/[(B-1)(B+2)]\). Every \(t\) in the domain is approached by admissible integer values \(M/s\) along a sequence of scales; continuity proves that these bounds are sharp and that their entire interval is the subsequential limit set.

## Verification

Run `python3 verify.py` with Python 3.8 or newer. This standalone checker independently enumerates actual length-\(n\) factors for finitely many bases and lengths, compares their reversal-class counts against the closed form, and checks the two endpoint and peak expressions at large geometric scales. Its finite checks are diagnostic and are not substituted for Steps 1–7 of the proof.

## Relationship to prior work

Allouche, Campbell, Li, Shallit and Stipulanti [1] introduced reflection complexity and proved that the reflection complexity of an automatic sequence is computably regular; they computed several classical examples, including Thue–Morse, period-doubling, paperfolding, Golay–Shapiro and Baum–Sweet. The definition and general automaticity theorem do not themselves give the explicit geometric-support formula or the base-dependent sharp normalized oscillation. Dvořáková and Pelantová [2] subsequently studied general reflection-complexity growth and minimum-growth sequences, but their stated characterization of the \(+1\) two-step increment does not imply the present geometric-support value and oscillation results. The word supported on powers of two is a standard example of an automatic sequence [3]. The novelty asserted here is the exact all-base reflection-class census and its sharp asymptotics, not the definition of reflection complexity or the automaticity of these words.

## Limitations

The formula concerns reflection equivalence only, not equivalence under complement or general antimorphisms. This proof does not classify all automatic words with a given normalized reflection-complexity limit set. No claim of independent mathematical certification is made; the finite script is not an infinite proof. Relevant published literature and indexed mathematical findings were compared, but an unindexed equivalent theorem may exist.

## References

[1] J.-P. Allouche, J. M. Campbell, S. Li, J. Shallit, M. Stipulanti, *The reflection complexity of sequences over finite alphabets*, arXiv:2406.09302 (first public June 13, 2024), later *Theory of Computing Systems* 69, article 31 (2025). https://arxiv.org/abs/2406.09302

[2] L. Dvořáková, E. Pelantová, *Reflection on the Reflection Complexity*, *Theory of Computing Systems* 70, article 35 (2026). https://doi.org/10.1007/s00224-026-10278-7

[3] J.-P. Allouche, J. Shallit, *Automatic Sequences: Theory, Applications, Generalizations*, Cambridge University Press, 2003, for base-recognizable sets and automatic sequences.
