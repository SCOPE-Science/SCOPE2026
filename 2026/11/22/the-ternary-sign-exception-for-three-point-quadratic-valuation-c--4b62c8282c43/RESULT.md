# The ternary sign exception for three-point quadratic valuation cumulants

## Finding

For every odd prime \(p\), positive integer \(c\) divisible by \(p\), and integer \(s\ge1\), set
\[
Q_c(n)=n(n+1)+c,\qquad
X_i(n)=\nu_p\bigl(Q_c(n+i p^s)\bigr)\quad(i=0,1,2).
\]
All three valuations are finite for every integer \(n\). As \(n\) ranges uniformly over nonnegative integers, the exact limiting **trivariate** distribution of \((X_0,X_1,X_2)\) is as follows. Every triple not listed has probability zero:
\[
\begin{aligned}
\Pr[(X_0,X_1,X_2)=(0,0,0)]&=\frac{p-2}{p},\\
\Pr[(X_0,X_1,X_2)=(j,j,j)]&=\frac{2(p-1)}{p^{j+1}}\quad(1\le j<s),\\
\Pr[(X_0,X_1,X_2)=(s,s,s)]&=\frac{2(p-3)}{p^{s+1}},\\
\Pr[(X_0,X_1,X_2)=(j,s,s)]&=\Pr[(s,j,s)]=\Pr[(s,s,j)]
=\frac{2(p-1)}{p^{j+1}}\quad(j>s).
\end{aligned}
\]
In particular, for \(p=3\) the central triple \((s,s,s)\) is impossible, because the three shifted roots occupy all three children of a shared depth-\(s\) residue ball. Clipping every coordinate at any \(k\ge1\) gives the exact three-coordinate census among \(0\le n<p^k\): simply push forward the displayed probabilities under \((i,j,\ell)\mapsto(\min(i,k),\min(j,k),\min(\ell,k))\) and multiply by \(p^k\). Explicit integer formulas appear in `verify_triple.py`.

The **connected three-point cumulant** is
\[
\begin{aligned}
\kappa_{p,s}&=\mathbb E\bigl[(X_0-\mu)(X_1-\mu)(X_2-\mu)\bigr],\qquad \mu=\frac2{p-1},\\
&=\boxed{\frac{2}{(p-1)^3}\left[p^2-2p+3-\frac{3s(p^2-1)+p^2-2p-5}{p^s}\right]}.
\end{aligned}
\]
Its sign has exactly **one negative exception**:
\[
\boxed{\kappa_{p,s}<0\iff (p,s)=(3,1),\qquad\kappa_{p,s}>0\ \text{otherwise}.}
\]
There are no zero cases. In contrast, **every pairwise covariance is strictly positive**:
\[
\operatorname{Cov}(X_i,X_j)
=\frac{2(p+1)(1-p^{-s})-4}{(p-1)^2}>0
\qquad(0\le i<j\le2).
\]
Thus the least ternary scale exhibits *negative connected three-way dependence despite positive dependence in every pair*. The cumulant increases strictly with \(s\) and tends to \(2(p^2-2p+3)/(p-1)^3>0\) as \(s\to\infty\). These expectations equal the limits of empirical integer averages; they are not merely formal local moments.

## Assumptions and scope

The prime \(p\) is any odd prime, \(c>0\) is an integer multiple of \(p\), \(s\ge1\) is an integer, and the equally spaced lags are exactly \(0,p^s,2p^s\). The symbol \(\nu_p(m)\) denotes the usual prime-adic valuation of a nonzero integer. Because \(Q_c(n)>0\) for all \(n\in\mathbb Z\), these valuations are finite. The probabilities are natural densities of index sets and also Haar probabilities over \(\mathbb Z_p\). The exact finite-block assertion applies to every depth \(k\ge1\), including \(k\le s\). No claim is made about arbitrary triples of shifts, the binary prime, or constants not divisible by \(p\).

## Proof

**1. Two simple roots, three translates.** Since \(p\mid c\), the reduction of \(Q_c(x)\) is \(x(x+1)\) modulo \(p\), with simple roots \(0,-1\) for every odd \(p\). Hensel lifting gives distinct \(\alpha,\beta\in\mathbb Z_p\), one over each residue, such that \(Q_c(x)=(x-\alpha)(x-\beta)\). At a point \(x\) in either root residue class, \(\nu_p(Q_c(x))\) is its distance exponent from the corresponding root, since the other factor is a unit. It is zero outside these two residue classes.

The three translates have root sets \(\{\alpha-i p^s,\beta-i p^s\}\) for \(i=0,1,2\). Each original root contributes one triple of points with mutual distance valuation exactly \(s\): differences are \(p^s\) or \(2p^s\), and \(2\) is a \(p\)-adic unit. The two original residue classes are disjoint, so their contributions add without overlap.

**2. Exact three-way cylinder partition.** In a fixed original root class, write the three shifted roots as \(a_0,a_1,a_2\). For \(1\le j<s\), the event \(\nu_p(x-a_0)=j\) forces all three distance exponents to equal \(j\), and occupies fraction \((p-1)/p^{j+1}\) of \(\mathbb Z_p\). At depth \(s\), the three roots are in the same parent ball but in three different child balls, because their scaled residues differ by \(0,1,2\pmod p\). In the other \(p-3\) child balls all three valuations equal \(s\), with probability \((p-3)/p^{s+1}\). Inside each of the three distinguished child balls, precisely the corresponding coordinate can exceed \(s\); its exact value \(j>s\) occurs with probability \((p-1)/p^{j+1}\), while the other two coordinates equal \(s\). The same partition occurs in each of the two distinct original root classes, explaining the factor two in the stated probabilities. Outside those root classes, all three valuations vanish, with probability \((p-2)/p\). This list exhausts the full space and its masses add to one.

For every finite \(k\), each clipped triple depends only on \(n\bmod p^k\). The Haar measure of each clipped event therefore equals exactly its count modulo \(p^k\) divided by \(p^k\). This proves the full integer census at every depth, not only an asymptotic result.

**3. Mixed moments and cumulant.** By the two simple root classes, for each \(i\) and every \(j\ge1\), \(\Pr[X_i\ge j]=2p^{-j}\), giving \(\mathbb E[X_i]=\mu=2/(p-1)\). A fixed root class contributes to \(\mathbb E[X_iX_j]\) for \(i\ne j\) precisely when the two level balls intersect, yielding
\[
\mathbb E[X_iX_j]=\frac{2(p+1)}{(p-1)^2}(1-p^{-s}).
\]
For three root points with mutual distances at depth \(s\), the three level balls of depths \(a,b,d\ge1\) have nonempty intersection exactly when the **second-largest** of \(a,b,d\) is at most \(s\); the intersection, when nonempty, has measure \(p^{-\max(a,b,d)}\). Indeed, beyond depth \(s\), at most one of the three root-centered balls can contain a point. When the maximum level is \(m\le s\), there are \(m^3-(m-1)^3=3m^2-3m+1\) triples of positive levels; for \(m>s\), there are exactly \(3s^2\) permissible triples. Consequently
\[
\begin{aligned}
\mathbb E[X_0X_1X_2]
&=2\left[\sum_{m=1}^{s}\frac{3m^2-3m+1}{p^m}
+\frac{3s^2}{(p-1)p^s}\right]\\
&=\frac{2}{(p-1)^3}\left[p^2+4p+1-
\frac{3s(p^2-1)+p^2+4p+1}{p^s}\right].
\end{aligned}
\]
Expand the centered product to obtain
\[
\kappa_{p,s}=\mathbb E[X_0X_1X_2]-3\mu\,\mathbb E[X_0X_1]+2\mu^3.
\]
Substitution yields the boxed formula. Notice that this third mixed moment is not determined by any *pairwise* joint law in general; here the three-way common cylinder and its three-way split are needed.

**4. Sharp sign.** For \(s=1\), direct simplification gives
\[
\kappa_{p,1}=\frac{2\{p(p-1)(p-5)+8\}}{p(p-1)^3}.
\]
This is \(-1/3\) at \(p=3\), and positive for all odd primes \(p\ge5\). The successive difference is
\[
\kappa_{p,s+1}-\kappa_{p,s}
=\frac{2[3s(p^2-1)+p^2-5p-8]}{p^{s+1}(p-1)^2}>0
\]
for every \(p\ge3,s\ge1\). At \(p=3\), the next value is \(\kappa_{3,2}=2/9>0\). Hence the unique negative case is \((p,s)=(3,1)\), and no zero occurs. The pair covariance above is positive because \(p^{-s}\le p^{-1}\) and the numerator is then at least \(2(p+1)(1-1/p)-4>0\).

**5. Convergence of empirical higher moments.** Every valuation \(X_i(n)\) among \(0\le n<N\) is at most \(O_{p,c,s}(\log(N+2))\), since its polynomial argument is positive of quadratic growth. At most two residue classes modulo \(p^j\) have valuation at least \(j\), giving the bound \(\#\{n<N:X_i(n)\ge j\}\le2(N/p^j+1)\). The tail-sum formula for nonnegative integer powers therefore shows uniform integrability of the third moments: the contribution from levels above \(J\) is at most \(O_p(J^3p^{-J})+O_{p,c,s}((\log(N+2))^3/N)\). The mixed product is bounded by the average of the third powers through AM–GM, and its large-level part by the corresponding individual tails. Thus the empirical third mixed moment and all lower joint moments converge to the calculated Haar moments, proving the natural-density interpretation of the connected cumulant.

## Verification

Run `python3 verify_triple.py`. The checker independently calculates every predicted clipped triple-cell multiplicity and compares it to direct integer evaluations of \(Q_c(n)\), \(Q_c(n+p^s)\), and \(Q_c(n+2p^s)\), for \(0\le n<p^k\). It verified **400 complete histograms comprising 1,396,368 index triples** for \(p\in\{3,5,7,11,13\}\), four positive values of \(c\) divisible by \(p\), \(s\in\{1,2,3,4\}\), and all checked depths \(k=1,\dots,6\) with \(p^k\le65000\). The infinite classification and sign proof are mathematical, not based on finite exhaustive computation.

## Relationship to prior work

Snyder, *Products of \(p\)-Adic Valuation Trees* (arXiv:2308.11718v1, first posted August 22, 2023), develops polynomial valuation trees and factor-product identities, with primary MSC2020 11B83. Boultinghouse et al., *The \(p\)-Adic Valuation Trees for Quadratic Polynomials for Odd Primes* (arXiv:2309.16637v1, posted September 28, 2023), classify one-coordinate quadratic valuation trees. Previous bivariate simple-root valuation theorems yield the pair covariances, but not the trivariate cylinder splitting, exact three-way census or third cumulant. The present conclusion isolates a ternary negative third-order dependence that coexists with positive pairwise covariances. Full-text comparisons of these primary sources and targeted searches did not locate a statement of the same trivariate classification. An earlier equivalent treatment in multivariate local-zeta or higher-order correlation literature remains possible.

## Limitations

Only three equally spaced prime-power shifts \(0,p^s,2p^s\), odd primes, and positive constants divisible by the prime are covered; the analogous general triple-shift problem, singular-root polynomials and the binary prime remain outside scope. The assertion concerns exact trivariate valuation frequencies and one third connected cumulant, not statistical independence or high-dimensional normal limits. Priority was assessed using inspected primary literature and searchable scientific records, not an exhaustive historical database.

## References

1. D. Snyder, *Products of \(p\)-Adic Valuation Trees*, arXiv:2308.11718v1, first posted 2023-08-22, https://arxiv.org/abs/2308.11718; *The PUMP Journal of Undergraduate Research* 7 (2024), 299–322, https://doi.org/10.46787/pump.v7i0.3877.
2. W. Boultinghouse, E. Hammett, S. Hu, O. Kozhushkina, R. Snyder, J. Trulen, *The \(p\)-Adic Valuation Trees for Quadratic Polynomials for Odd Primes*, arXiv:2309.16637v1, first posted 2023-09-28, https://arxiv.org/abs/2309.16637.
