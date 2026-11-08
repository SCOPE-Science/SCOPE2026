# Infinite dimension plateaus for the cubic Walsh Fourier projection

## Finding

Let \(G_n=\{-1,1\}^n\), with normalized counting measure, and let \(\Pi_{3,n}\) be the Fourier–Walsh multiplier which keeps precisely the characters \(\chi_S(x)=\prod_{j\in S}x_j\) with \(|S|=3\). For every integer \(n\ge3\), write
\[
L_n=\|\Pi_{3,n}\|_{L^\infty(G_n)\to L^\infty(G_n)}
=\|\Pi_{3,n}\|_{L^1(G_n)\to L^1(G_n)}.
\]
Then \(L_{n+1}\ge L_n\), and equality holds **if and only if**
\[
n=\frac{r(r+2)}3\qquad\text{for an odd integer }r\ge3.
\]
Equivalently, all plateau indices (and no others) are
\[
n=12k^2+16k+5\quad(k\ge0),\qquad
n=12k^2+8k+1\quad(k\ge1).
\]
The first indices are \(5,21,33,65,85,133,161\). If \(P(X)=\#\{n:3\le n\le X,\ L_{n+1}=L_n\}\), then
\[
P(X)=\sqrt{X/3}+O(1)\qquad (X\to\infty).
\]
Thus the norm is nondecreasing but exactly constant upon a sparse, infinite set of successive dimension increases.

For every \(n\ge3\), there is also an exact nonnegative increment formula. Put \(s_j=n-2j\),
\[
E_2(n,s)=\frac{s^2-n}{2},\qquad E_3(n,s)=\frac{s^3-(3n-2)s}{6}.
\]
Then
\[
L_{n+1}-L_n=2^{-n}\sum_{j=0}^n\binom nj
\Big(|E_2(n,s_j)|-|E_3(n,s_j)|\Big)_+,
\]
where \((a)_+=\max(a,0)\).

## Assumptions and scope

The group, Haar measure, characters and Fourier projections have precisely the definitions above. The norm is the operator norm on all real-valued or all complex-valued functions; the two norms agree. A plateau index is an integer \(n\ge3\) for which the canonical cubic Fourier projection has equal endpoint norms in dimensions \(n\) and \(n+1\). No normalization by the dimension of the cubic subspace is used. The theorem covers every integer dimension \(n\ge3\), not just the dimensions tested computationally.

## Proof

**Kernel reduction.** The normalized convolution kernel of \(\Pi_{3,n}\) is the real function
\[
K_{3,n}(x)=\sum_{1\le i<j<k\le n}x_ix_jx_k.
\]
The convolution estimate gives \(\|\Pi_{3,n}\|_{\infty\to\infty}\le\mathbb E|K_{3,n}(X)|\), where the coordinates of \(X\) are independent symmetric signs. At the identity, equality is attained by the function \(f(y)=\operatorname{sgn}(K_{3,n}(y))\); the choice at zeros is immaterial. The \(L^1\) norm is equal by finite-dimensional duality. Therefore
\[
L_n=\mathbb E\left|\sum_{i<j<k}X_iX_jX_k\right|.
\]

**Adding one coordinate.** Write \(E_d(X)=\sum_{|S|=d}\prod_{i\in S}X_i\). If \(Y\) is a new independent symmetric sign, then
\[
E_3(X,Y)=E_3(X)+Y E_2(X).
\]
For real numbers \(a,b\),
\[
\frac{|a+b|+|a-b|}{2}=\max(|a|,|b|).
\]
Conditioning on \(X\) thus gives
\[
L_{n+1}=\mathbb E\max(|E_3(X)|,|E_2(X)|),
\]
which proves monotonicity and the displayed exact nonnegative increment formula. The increment vanishes exactly when \(|E_3(X)|\ge|E_2(X)|\) for every sign vector (all such vectors have positive probability).

**Reducing to an arithmetic interval.** Write \(s=\sum_{i=1}^n X_i\), whose values are \(n,n-2,\dots,-n\). Elementary symmetric polynomial identities, using \(X_i^2=1\), yield
\[
E_2(X)=E_2(n,s)=\frac{s^2-n}{2},\qquad
E_3(X)=E_3(n,s)=\frac{s^3-(3n-2)s}{6}.
\]
If \(n\) is even, the possible value \(s=0\) has \(E_3(n,0)=0\), \(|E_2(n,0)|=n/2>0\); hence the increment is strictly positive.

Suppose \(n\) is odd. Since \(E_2(n,s)\) is even in \(s\) and \(E_3(n,s)\) is odd, it suffices to consider positive odd \(s\). At \(s=1\), \(E_2(n,1)=E_3(n,1)=(1-n)/2\). For every odd \(s\ge3\), direct factorization gives
\[
E_3(n,s)+E_2(n,s)=\frac{(s+1)(s(s+2)-3n)}{6},
\]
\[
E_3(n,s)-E_2(n,s)=\frac{(s-1)(s(s-2)-3n)}{6},
\]
and consequently
\[
E_3(n,s)^2-E_2(n,s)^2
=\frac{(s^2-1)(s(s-2)-3n)(s(s+2)-3n)}{36}.
\]
Thus a strict increase occurs precisely when at least one available odd \(s\in\{3,5,\ldots,n\}\) satisfies
\[
s(s-2)<3n<s(s+2).
\]
As \(s\) runs through these consecutive odd integers, the intervals have adjoining endpoints: \(s(s+2)=(s+2)s\). Their union as closed intervals is \([3,n(n+2)]\). Because \(n\ge3\), the number \(3n\) lies strictly inside this union. Therefore it lies inside an open interval (strict increase), unless it coincides with an internal shared endpoint \(r(r+2)\) for an odd integer \(r\ge3\). In that latter case every squared difference is nonnegative, so equality holds. This proves the claimed necessary-and-sufficient arithmetic condition.

**Arithmetic progression and counting.** For odd \(r\ge3\), the integrality of \(r(r+2)/3\) forces \(r\equiv1\) or \(3\pmod6\). Substituting \(r=6k+3\), \(k\ge0\), or \(r=6k+1\), \(k\ge1\), gives the two stated quadratic families. Among integers \(r\) up to \(\sqrt{3X+1}-1\), precisely one third up to a bounded counting error are positive odd integers of these two residue classes. Hence \(P(X)=\sqrt{X/3}+O(1)\).

## Verification

The standalone `verify_cubic_walsh.py` uses exact integer and rational arithmetic. It independently enumerates all sign vectors for dimensions \(3\) through \(10\); checks the binomial kernel formula, consecutive-dimension norm differences and their positive-part representations for dimensions \(3\) through \(181\); and compares every zero increment through dimension \(180\) to the quadratic classification. Its output is

```text
CUBIC_WALSH_PLATEAU_PASS brute_dimensions=3..10 exact_n=3..181 plateaus=5,21,33,65,85,133,161
```

All infinite-dimensional assertions follow from the preceding algebraic proof. Finite checks alone cannot prove the complete classification.

## Relationship to prior work

The exact convolution-kernel expectation for the projection norm is a special case of Defant, Galicer, Mansilla, Mastyło and Muro, *Projection constants for spaces of multivariate polynomials*, Theorem 8.1.1, and their later *Asymptotic insights for projection, Gordon–Lewis and Sidon constants in Boolean cube function spaces*, Theorem 3.1. The latter also establishes fixed-degree Gaussian/Hermite scaling, including the cubic case. The present statement instead classifies **every consecutive-dimension equality**, not just the norm's value in a fixed dimension or its leading asymptotic behavior.

Integral zeros of Krawtchouk polynomials have a separate older literature, including Habsieger and Stanton. The arithmetic boundaries in the present proof are related to cubic Krawtchouk zeros, but the claimed Fourier-projection plateau law additionally requires the absolute-moment comparison, the all-sign criterion and an exhaustive interlacing argument.

## Limitations

The theorem concerns the homogeneous degree-three Walsh multiplier and endpoint \(L^1\) and \(L^\infty\) norms only; it does not classify plateaus for other degrees or intermediate \(L^p\) norms. The arithmetic classification is complete, but a historical-literature priority search cannot rule out an earlier equivalent result expressed in different terminology. The theorem does not assert a new formula for the per-dimension projection norm already represented in the earlier convolution-kernel identity.

## References

1. A. Defant, D. Galicer, M. Mansilla, M. Mastyło and S. Muro, *Projection constants for spaces of multivariate polynomials*, arXiv:2208.06467, version 1 publicly posted 12 August 2022; Chapter 8, especially Theorem 8.1.1 and §8.2.
2. A. Defant, D. Galicer, M. Mansilla, M. Mastyło and S. Muro, *Asymptotic insights for projection, Gordon–Lewis and Sidon constants in Boolean cube function spaces*, arXiv:2302.00233, first posted 1 February 2023; Theorems 3.1 and 4.1.
3. L. Habsieger and D. Stanton, *More zeros of Krawtchouk polynomials*, *Graphs and Combinatorics* **9** (1993), 163–172, especially the introduction and §2; doi:10.1007/BF02988302.
