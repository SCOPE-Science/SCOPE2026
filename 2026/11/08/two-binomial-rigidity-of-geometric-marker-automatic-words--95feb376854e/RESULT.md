# Two-binomial rigidity of geometric-marker automatic words

## Finding
For each integer \(B\ge 2\), let \(w_B\) be the infinite binary word indexed by \(i\ge0\) with \(w_B(i)=1\) exactly at the positions \(1,B,B^2,\ldots\), and \(w_B(i)=0\) otherwise. For a finite word \(u\), let \(\binom{u}{v}\) count (possibly scattered) subsequences equal to \(v\). **Every length-\(n\) factor of \(w_B\) is uniquely determined by**
\[
\left(n,\binom{u}{1},\binom{u}{01}\right).
\]
Equivalently, distinct same-length factors are never 2-binomially equivalent. If \(b_{w_B}^{(2)}(n)\) denotes the number of 2-binomial classes and \(p_{w_B}(n)\) the number of distinct factors, then
\[
 b_{w_B}^{(2)}(n)=p_{w_B}(n)\qquad(B\ge2,\ n\ge1).
\]
The order 2 is sharp: \(b_{w_B}^{(1)}(2)<p_{w_B}(2)\), because both \(01\) and \(10\) occur. In particular, this is an infinite family of aperiodic, base-\(B\) automatic words on which the entire factor language is reconstructible using scattered subwords of length at most two.

There is also an exact finite formula for the common complexity. For \(r\ge2\), \(a\ge0\), and \(n\ge1\), put
\[
L_{a,r}(n)=\begin{cases}
\max\{0,B^{r-1}-n+1\},&a=0,\\
\max\{B^{a-1}+1,B^{a+r-1}-n+1\},&a\ge1,
\end{cases}
\]
\[
U_{a,r}(n)=\min\{B^a,B^{a+r}-n\},\qquad
H_{a,r}(n)=\max\{0,U_{a,r}(n)-L_{a,r}(n)+1\}.
\]
Then
\[
\boxed{b_{w_B}^{(2)}(n)=p_{w_B}(n)
=n+1+\sum_{r=2}^{\infty}\sum_{a=0}^{\infty}H_{a,r}(n).}
\]
Only finitely many summands are nonzero: a factor containing the consecutive markers \(B^a,\ldots,B^{a+r-1}\) requires \(B^a(B^{r-1}-1)<n\). This formula is a count of explicit integer intervals rather than a claim of closed-form simplification.

## Assumptions and scope
The alphabet is \(\{0,1\}\); indices and marker positions start at zero. All factors are contiguous, nonempty, and finite, whereas binomial counts refer to scattered subsequences. The integer base \(B\) is arbitrary and fixed, \(B\ge2\). For binary words of a fixed length, 2-binomial equivalence is equivalent to equality of \(\binom{u}{1}\) and \(\binom{u}{01}\): all remaining length-at-most-two counts follow from these and the length. No claim is made for arbitrary sparse-support words or for larger alphabets.

## Proof
**1. Reduction to a position sum.** Let a factor \(u=w_B[s:s+n]\) contain \(r\) occurrences of the letter \(1\) at relative positions \(0\le x_0<\cdots<x_{r-1}<n\), and put \(T(u)=\sum_j x_j\). Each marker at position \(x_j\) has exactly \(x_j-j\) zeros before it. Thus
\[
 \binom{u}{01}=T(u)-\binom{r}{2}.
\]
So the proposed data determine \(r\) and \(T(u)\). For \(r=0\), the word is \(0^n\). For \(r=1\), the lone marker is at position \(T(u)\). We therefore consider \(r\ge2\).

**2. Geometric marker windows.** The markers of such a factor must be consecutive powers \(B^a,B^{a+1},\ldots,B^{a+r-1}\), for some \(a\ge0\). Write \(A_r=1+B+\cdots+B^{r-1}=(B^r-1)/(B-1)\). Its starting index \(s\) satisfies \(0\le s\le B^a\); if \(a\ge1\), the preceding marker is excluded, and hence \(B^{a-1}<s\le B^a\). The relative position sum is
\[
T(u)=A_r B^a-rs.\tag{1}
\]
For fixed \(r,a\), \(T(u)\) therefore determines \(s\) uniquely and hence determines the entire factor. It remains to show that it determines \(a\).

**3. Separation across positive levels.** For \(a\ge1\), (1) gives the *half-open* bounds
\[
 (A_r-r)B^a\le T(u)<(A_r-r/B)B^a.\tag{2}
\]
The intervals in (2) at successive \(a\) are disjoint provided
\[
 B(A_r-r)\ge A_r-r/B,
\]
or equivalently
\[
 B^r-1\ge r(B-1/B).\tag{3}
\]
At \(r=2\), the difference of the two sides of (3) is \((B-2)(B^2-1)/B\ge0\). Increasing \(r\) increases that difference by \((B-1)B^r-(B-1/B)>0\). Thus (3) holds for all \(B\ge2,r\ge2\), with equality only when \(B=r=2\). The strict upper bound in (2) makes the intervals disjoint even at equality. Therefore two factors with \(a\ge1\), the same \(r\), and the same \(T\) have the same \(a\) and \(s\).

**4. The first marker level.** When \(a=0\), the nonnegative integer \(s\) can only be 0 or 1. By (1), the two potential sums are \(A_r\) and \(A_r-r\), distinct since \(r\ge2\). Every sum at \(a\ge1\) is at least \(B(A_r-r)\). This lower bound exceeds \(A_r\) whenever \((B,r)\ne(2,2)\): the equivalent inequality \(B^r-1>Br\) holds at \(r=2,B\ge3\) and at \(r\ge3,B=2\), then persists when either parameter increases. In the sole exceptional case \(B=r=2\), the level-0 sums are \(1,3\), the only level-1 start is \(s=2\) giving \(T=2\), and all levels \(a\ge2\) have \(T\ge4\) by (2). Thus even this exceptional case has no collision. Combining the cases proves the reconstruction assertion.

**5. Exact enumeration.** Every length-\(n\) all-zero factor occurs, and every word with exactly one \(1\) at any prescribed relative position \(0,\ldots,n-1\) occurs: take an arbitrarily large isolated marker with the adjoining gaps longer than \(n\). These are \(n+1\) distinct factors. For a factor with \(r\ge2\) markers from \(B^a\) through \(B^{a+r-1}\), the interval \([s,s+n)\) must contain the first and last, omit the predecessor if present, and omit the next marker. These conditions are precisely
\[
L_{a,r}(n)\le s\le U_{a,r}(n).
\]
Therefore there are exactly \(H_{a,r}(n)\) admissible starts. The already-proved reconstruction shows different admissible triples \((a,r,s)\) give different words. Summing yields the stated exact formula. Finally, \(01\) and \(10\) both occur and are abelian-equivalent but distinct, so 2 is the least binomial order giving equality at every length. The support language is regular in base \(B\) (a leading 1 followed by zeros), so \(w_B\) is base-\(B\) automatic; its unbounded marker gaps and infinitely many markers imply aperiodicity.

## Verification
The standalone Python file `verify.py` independently scans 5,001 starts for every base \(2\le B\le8\) and every factor length \(1\le n\le160\). It computes the pair \((r,T)\) by a rolling update, compares the resulting classes with literal factors, and checks the separate interval-enumeration formula. The extracted-file execution reported:

`VERIFY_OK bases=2..8 lengths=1..160 windows=5601120 exact_count_matches=1120`

These are finite diagnostic checks only. The proof of the infinite statement consists of steps 1–5 and does not rest on these experiments. The verifier uses exact integers, not numerical tolerance or probabilistic testing.

## Relationship to prior work
Rigo, Stipulanti and Whiteland (arXiv:2201.04603, first publicly posted January 12, 2022) study binomial versus factor complexity, including equality for Sturmian words and comparisons with the Tribonacci word; their §7.1 gives a different sparse morphic example for which 2-binomial complexity is **strictly smaller** than factor complexity while 3-binomial complexity equals it. The present geometric-marker family has 2-binomial equality despite being nonrecurrent and automatic. The distinction is in the support geometry and cannot be inferred from their example. Lejeune, Rigo and Rosenfeld determine 2-binomial faithfulness for the primitive Tribonacci substitution via templates; that result does not cover the present nonprimitive sparse language. Previous results concerning palindromes, reflection classes, or attractors for geometric-marker words concern other equivalence relations and do not imply the two-scattered-subsequence reconstruction theorem. These comparisons are not a claim to have searched every possible unpublished or unindexed equivalent.

## Limitations
The theorem is about exactly geometric integer-power supports and the ordinary factor language; it does not classify the full collection of binary sequences satisfying 2-binomial rigidity. The complexity formula is a finite double sum, not an optimized closed form. No independent external scientific audit has taken place. An equivalent result in unindexed literature remains a possible bibliographic risk.

## References
1. M. Rigo, M. Stipulanti, M. A. Whiteland, *Characterizations of families of morphisms and words via binomial complexities*, arXiv:2201.04603 (first public version 2022-01-12), https://arxiv.org/abs/2201.04603 ; especially Introduction and §7.1.
2. M. Lejeune, M. Rigo, M. Rosenfeld, *Templates for the k-binomial complexity of the Tribonacci word*, Advances in Applied Mathematics **112** (2020), 101947, https://doi.org/10.1016/j.aam.2019.101947 .
3. M. Lejeune, J. Leroy, M. Rigo, *Computing the k-binomial complexity of the Thue–Morse word*, J. Combin. Theory Ser. A **176** (2020), 105284, https://arxiv.org/abs/1812.07330 .
