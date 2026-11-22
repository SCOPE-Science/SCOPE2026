# Exact dyadic neighbour-valuation laws and a resultant-controlled covariance reversal for quadratic sequences

## Finding

Let \(a,b,c\) be positive integers with \(a,b\) odd and \(c\) even. Put
\[
f(n)=an^2+bn+c,\quad X_n=\nu_2(f(n)),\quad Y_n=\nu_2(f(n+1)),
\]
and define the **shifted resultant parameter**
\[
R=a^2-b^2+4ac,\qquad
 d=\begin{cases}\nu_2(|R|)-1,&R\ne0,\\+\infty,&R=0.\end{cases}
\]
Because \(8\mid R\), a finite \(d\) is at least \(2\). For **all integers** \(i,j\ge1\), the following three disjoint alternatives precisely characterize the nonzero natural-density cells of the adjacent-valuation distribution:

1. \(\min(i,j)=1\) and \(\max(i,j)\ge2\);
2. \(i=j<d\);
3. \(d<\infty\), \(\min(i,j)=d\), and \(\max(i,j)>d\).

In every listed case, the indices producing \((X_n,Y_n)=(i,j)\) form **exactly one residue class modulo** \(2^{\max(i,j)+1}\). Thus their natural density is exactly
\[
\Pr(X=i,Y=j)=2^{-\max(i,j)-1}.
\]
Every other cell is empty (not merely zero-density). In fact every finite interval \(0\le n<N\) obeys
\[
\left|\#\{0\le n<N:(X_n,Y_n)=(i,j)\}-N\Pr(X=i,Y=j)\right|<1
\]
for nonempty cells; empty cells have count zero.

Both marginal distributions satisfy \(\Pr(X=i)=\Pr(Y=i)=2^{-i}\), hence each has mean \(2\) and variance \(2\). Their limiting index-sampled covariance is
\[
\boxed{\lim_{N\to\infty}\operatorname{Cov}_{0\le n<N}(X_n,Y_n)
=\frac12-\frac3{2^d},\qquad 2^{-\infty}=0.}
\]
In particular, the covariance is negative exactly when \(R\equiv8\pmod{16}\), and positive exactly when \(16\mid R\), including \(R=0\); it never vanishes. Every value \(\frac12-3/2^d\) for \(d=2,3,\ldots,\infty\) actually occurs in this coefficient family.

## Assumptions and scope

The valuation \(\nu_2(m)\) of a nonzero integer is the exponent of \(2\) dividing its absolute value. The assumptions \(a,b,c>0\), \(a,b\) odd, \(c\) even guarantee \(f(n)>0\) for every integer \(n\ge0\), so no infinite-valued observations arise. A natural density is a limit of counts for \(0\le n<N\), divided by \(N\). The symbol \(+\infty\) for \(d\) is a convention only for \(R=0\); the comparisons \(i<d\) have the usual interpretation. The covariance uses the **population** normalization \(N^{-1}\sum\), not the unbiased sample divisor.

## Proof

**1. Two simple dyadic roots.** Modulo \(2\) the polynomial is \(f(x)\equiv x(x+1)\), and its formal derivative satisfies \(f'(x)=2ax+b\equiv1\pmod2\). Hensel lifting therefore yields unique roots \(\alpha,\beta\in\mathbb Z_2\) of even and odd parity respectively. As \(a\) is a dyadic unit,
\[
f(x)=a(x-\alpha)(x-\beta)\quad\text{over }\mathbb Z_2.
\]
For integers \(n\) of even parity, precisely one factor of \(f(n)\) and one of \(f(n+1)\) is even, giving
\[
(X_n,Y_n)=(\nu_2(n-\alpha),\nu_2(n-(\beta-1))).
\]
For odd \(n\), similarly
\[
(X_n,Y_n)=(\nu_2(n-\beta),\nu_2(n-(\alpha-1))).
\]
Thus we have two comparisons between **centres of the same parity**, whose separations are \(A+1\) and \(1-A\), where \(A=\alpha-\beta\) is odd.

**2. Collision depths determined by coefficients.** The discriminant identity gives \(a^2A^2=b^2-4ac\), whence
\[
(1+A)(1-A)=1-A^2=\frac{a^2-b^2+4ac}{a^2}=\frac R{a^2}.
\]
For any odd dyadic integer \(A\), exactly one of \(1+A\), \(1-A\) has dyadic valuation \(1\), and the other has valuation at least \(2\), possibly infinite. Their collision depths are therefore \(1\) and \(d=\nu_2(|R|)-1\) when \(R\ne0\), or \(1\) and \(+\infty\) when \(R=0\). This also directly proves \(8\mid R\) and \(d\ge2\).

**3. The two-centre lemma.** Fix a parity class and dyadic centres \(u,v\) of that parity; let \(e=\nu_2(u-v)\ge1\), allowing \(+\infty\). For a uniformly chosen \(n\) of the fixed parity, if \(k<e\), then \(\nu_2(n-u)=k\) if and only if \(\nu_2(n-v)=k\), and this joint event has conditional probability \(2^{-k}\). If \(e<\infty\) and \(k>e\), the two events \((e,k)\) and \((k,e)\) each have conditional probability \(2^{-k}\), and there are no others. Indeed, the nonarchimedean triangle rule identifies equal valuations below the separation depth and exactly one valuation equal to the separation depth above it. Each event is one residue class modulo \(2^{k+1}\) within the full integers. For \(e=+\infty\), the centres coincide and only \((k,k)\) remains, again of conditional probability \(2^{-k}\).

**4. Assemble the two parities.** Each parity has natural density \(1/2\). Apply the lemma with \(e=1\) to one parity: it produces precisely the off-diagonal cells \((1,k),(k,1)\), \(k\ge2\). Apply it with \(e=d\) to the other parity: it produces \((k,k)\) for \(1\le k<d\), together with \((d,k),(k,d)\) for \(k>d\), unless \(d=\infty\), when all diagonal cells occur. The two supports are disjoint because \(d\ge2\). Multiplication by \(1/2\) gives every stated probability. Every event is a *single* full-integer residue class modulo \(2^{\max(i,j)+1}\), proving both precise support and the discrepancy bound; there is no unresolved union or error from mixing two parities.

**5. Moments and the sign transition.** Under the conditional two-centre law of collision depth \(e\), each marginal has mass \(2^{-k}\) at each \(k\ge1\), with mean \(2\) and second moment \(6\). Direct summation yields
\[
\mathbb E[XY\mid e]
=\sum_{k<e}\frac{k^2}{2^k}+2e\sum_{k>e}\frac{k}{2^k}
=6-\frac6{2^e},
\]
where the second sum is absent when \(e=\infty\). Averaging the depths \(1\) and \(d\) gives \(\mathbb E[XY]=\tfrac12(3+6-6/2^d)=\tfrac92-3/2^d\). Subtract the product of the two means, \(4\), to obtain the covariance formula.

The conversion from dyadic-Haar expectations to natural-index sampled moments is legitimate even though the valuations are unbounded: for any \(k\), the event \(X_n\ge k\) consists of two residue classes modulo \(2^k\), so its count on \(0\le n<N\) is at most \(2N/2^k+2\), and likewise for \(Y\). Since \(f(n+1)=O_{a,b,c}(N^2)\) for \(n<N\), both valuations are at most \(O_{a,b,c}(\log N)\). Applying \(m^2=\sum_{k=1}^{m}(2k-1)\) controls each quadratic tail by \(\sum_{k>K}O(k2^{-k})+O((\log N)^2/N)\), plus the similarly geometric level-\(K\) truncation. Hence the first and second empirical moments converge, and \(XY\le (X^2+Y^2)/2\) controls the mixed moment. The limiting covariance is therefore as claimed, rather than merely a formal Haar covariance.

Finally, \(R\equiv8\pmod{16}\) corresponds exactly to \(d=2\), giving covariance \(-1/4\); \(16\mid R\) corresponds to \(d\ge3\) or infinity, giving strictly positive covariance. The examples \((a,b,c)=(1,1,2^{d-1})\) realize each finite \(d\ge2\), and \((1,3,2)\) realizes \(d=\infty\). This proves the sharpness and exhaustiveness of the covariance spectrum.

## Verification

Run the standalone Python 3 program `verify.py` with `python3 verify.py` from the directory containing this document. It independently computes valuations of integer polynomial values and compares all \(81\) cells with \(1\le i,j\le9\) on blocks of \(2^{13}\) consecutive indices, for \(128\) positive coefficient triples, as well as exact one-residue tests for \(49\) cells on their own modulus. It includes both \(R=0\) and nonzero \(R\), negative and positive covariance examples. This is a finite consistency test; the proof above establishes the universal claim.

## Relationship to prior work

Boultinghouse, Long, Kozhushkina and Trulen classify the one-coordinate dyadic valuation trees for integer quadratics and show the odd-odd-even coefficient family is unbounded (their Theorem 1, case 4). Their full paper does not give the joint adjacent-index cell probabilities, the resultant-controlled collision depth or the sharp covariance sign reversal. Earlier work of Medina, Moll and Rowland treats general \(p\)-adic periodicity and boundedness. A related recorded joint-root collision result over **odd** primes supplies a general technique for two different polynomials; it does not cover characteristic two, where the same quadratic has the full pair of simple roots in the only two residue classes and the parity collision depths are necessarily \(1\) and \(d\). The current finding explicitly credits the root-lifting and nested-ball method, and claims as the new content only the complete dyadic adjacent-quadratic coefficient classification and its sign transition.

## Limitations

No claim is made for even \(a\), even \(b\), odd \(c\), or general polynomial pairs. The asymptotic moment statements concern natural initial segments \(0\le n<N\), not arbitrary very short sliding windows. An equivalent result may occur in uncatalogued literature, especially work on local valuation correlations. Independent validation of the present argument has not been carried out.

## References

- W. Boultinghouse, J. Long, O. Kozhushkina and J. Trulen, *2-Adic Valuations of Quadratic Sequences*, arXiv:2012.10332 (first public 2020-12-18), *Journal of Integer Sequences* **24** (2021), Article 21.6.1. https://arxiv.org/abs/2012.10332 ; https://cs.uwaterloo.ca/journals/JIS/VOL24/Trulen/trulen5.pdf
- L. A. Medina, V. H. Moll and E. S. Rowland, *Periodicity in the p-adic valuation of a polynomial*, arXiv:1505.02302. https://arxiv.org/abs/1505.02302
- *A root-collision law for joint polynomial valuations and a quadratic covariance trichotomy* (2026; odd-prime polynomial valuation correlations). The statement covers odd primes, not the dyadic boundary considered here; see related published research records.
