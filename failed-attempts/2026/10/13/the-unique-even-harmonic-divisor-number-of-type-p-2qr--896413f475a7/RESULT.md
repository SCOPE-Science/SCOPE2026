# The unique even harmonic divisor number of type \(p^2qr\)
## Finding
Let \(H(n)=n\tau(n)/\sigma(n)\), where \(\tau\) is the divisor-counting function and \(\sigma\) is the sum-of-divisors function. For distinct primes \(p,q,r\), suppose \(n=p^2qr\) is even. Then
\[
H(n)\in\mathbb Z \quad\Longleftrightarrow\quad n=140=2^2\cdot5\cdot7.
\]
In particular, \(140\) is the unique even harmonic divisor number in the first nonsquarefree three-prime multiplicity pattern \(p^2qr\).

## Assumptions and scope
The primes \(p,q,r\) are pairwise distinct, the exponent pattern is exactly \(2,1,1\), and \(n\) is even. No bound is imposed on the primes. The result does not address odd integers of type \(p^2qr\), nor exponent patterns with larger total multiplicity.

## Proof
Since \(\tau(p^2qr)=12\), harmonicity is the integrality of \(12n/\sigma(n)\). There are two placements for the prime \(2\).

First suppose the squared prime is \(2\). Write \(n=4qr\) with odd primes \(q<r\). Then
\[
H(n)=\frac{48qr}{7(q+1)(r+1)}=:h.
\]
Because \(q\ge3\) and \(r\ge5\), one has \(H(n)\ge30/7>4\), while \(H(n)<48/7<7\). Hence \(h\in\{5,6\}\).

If \(h=5\), then
\[
r=\frac{35(q+1)}{13q-35}.
\]
The condition \(r>q\) gives \(13q^2-70q-35<0\), so \(q\in\{3,5\}\). The choice \(q=3\) gives \(r=35\), while \(q=5\) gives \(r=7\). Thus this branch gives exactly \(n=140\).

If \(h=6\), then
\[
r=\frac{7(q+1)}{q-7}.
\]
Positivity gives \(q>7\), and \(r>q\) gives \(q^2-14q-7<0\), hence \(q\in\{11,13\}\). These give \(r=21\) and \(r=49/3\), respectively, so no prime \(r\) occurs.

Now suppose \(2\) is one of the unsquared primes. Rename the remaining odd unsquared prime as \(r\), so \(n=2p^2r\) with distinct odd primes \(p,r\). Put \(A=p^2+p+1\). Then
\[
H(n)=\frac{8p^2r}{A(r+1)}=:h.
\]
For \(p,r\ge3\), this is greater than \(4\) and less than \(8\), so \(h\in\{5,6,7\}\).

For \(h=5\),
\[
r=\frac{5A}{3p^2-5p-5}.
\]
Since \(r\ge3\), one obtains \(p^2-5p-5\le0\), hence \(p\in\{3,5\}\). These choices give \(r=65/7\) and \(r=31/9\), so neither is a solution.

For \(h=6\), positivity forces \(p\ge5\), and
\[
r=3+\frac{12(p+1)}{p^2-3p-3}.
\]
If \(r\) is integral, then \(p^2-3p-3\mid12(p+1)\). But \(p^2-3p-3\equiv1\pmod{p+1}\), so the two factors are coprime and therefore \(p^2-3p-3\mid12\). At \(p=5\) the divisor is \(7\), and for \(p\ge7\) it is at least \(25\); neither possibility works.

For \(h=7\), positivity forces \(p\ge11\), and
\[
r=7+\frac{56(p+1)}{p^2-7p-7}.
\]
Again \(p^2-7p-7\equiv1\pmod{p+1}\), so integrality would force \(p^2-7p-7\mid56\). At \(p=11\) this divisor is \(37\), and for \(p\ge13\) it is at least \(71\), so this is impossible.

Finally,
\[
H(140)=\frac{140\cdot12}{336}=5,
\]
so \(140\) is indeed harmonic.

## Verification
The proof above is symbolic and exhaustive for the two possible placements of the prime \(2\). A standalone regression checker independently enumerates pairwise-distinct primes up to \(300\) in the exponent pattern \(p^2qr\) and confirms that the only even harmonic value encountered is \(140\), with harmonic mean \(5\). This finite computation is corroborative only and is not used to establish the unbounded theorem.

## Relationship to prior work
Mahanta, Saikia, and Yaqubi study Zumkeller and layered numbers and explicitly discuss their relationship with harmonic mean numbers; their paper motivates further arithmetic investigation of those connections. Standard references on harmonic divisor numbers record the definition, the example \(140\), and the classical two-prime-support result that harmonic numbers of the form \(p^a q^b\) are even perfect. The checked sources do not state or imply the present exact classification of the even \(p^2qr\) layer. OEIS A001599 lists \(140\) as a harmonic divisor number, but a sequence table does not establish uniqueness within this structural family.

## Limitations
The theorem assumes evenness and the exact exponent pattern \(2,1,1\). It neither proves nor assumes that every three-prime-support harmonic divisor number is even. Older or unindexed literature on Ore numbers remains a residual originality risk; the checked exact-phrase, structural, database, and semantic searches found no covering statement.

## References
1. P. J. Mahanta, M. P. Saikia, D. Yaqubi, “Some properties of Zumkeller numbers and \(k\)-layered numbers,” arXiv:2008.11096; Journal of Number Theory 217 (2020), DOI 10.1016/j.jnt.2020.05.003.
2. OEIS A001599, “Harmonic or Ore numbers.”
3. E. W. Weisstein, “Harmonic Divisor Number,” MathWorld.
