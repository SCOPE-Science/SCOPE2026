# A sharp stochastic-order obstruction for fixed-point strata of random involutions

## Finding

Let \(\mathcal I_{n,f}\) be the involutions of \([n]=\{1,\dots,n\}\) with exactly \(f\) fixed points, with the uniform law on this finite set. Write \(D_{n,f}\) for the number of descents of a sampled involution. Suppose \(n-f\ge4\) is even. Then whenever
\[
n-f>(f+2)(f+3),
\]
the laws \(D_{n,f}\) and \(D_{n,f+2}\) are incomparable under usual first-order stochastic order. The law with fewer fixed points has strictly larger mean, but also strictly larger probability of having at most one descent.

For the fundamental comparison of zero versus two fixed points on an even number of vertices, \(D_{n,0}\) stochastically dominates \(D_{n,2}\) exactly for \(n=2,4,6\). For every even \(n\ge8\), the two laws are incomparable. In particular, \(n=8\) is the sharp first failure of stochastic monotonicity across these two fixed-point strata.

## Assumptions and scope

All probabilities are under uniform distributions on distinct permutations, not uniform distributions over descent numbers. An involution \(\pi\) satisfies \(\pi^2=\mathrm{id}\); its descent count is \(\operatorname{des}(\pi)=\#\{i:1\le i<n,\ \pi(i)>\pi(i+1)\}\). An admissible fixed-point count is \(0\le f\le n\) with \(n-f\) even. Write
\[
N_{n,f}=\frac{n!}{f!\,2^{(n-f)/2}((n-f)/2)!}.
\]
First-order stochastic domination \(X\succeq_{\mathrm{st}}Y\) means \(\Pr(X\le k)\le\Pr(Y\le k)\) for every real \(k\). The first theorem is a sufficient condition for incomparability; it does not claim to classify all pairs outside the displayed region. The sharp all-even-size classification concerns only \(f=0\) and \(f=2\).

## Proof

**1. Exact one-descent mass.** An involution with one descent also has exactly one inverse descent, at the same position. A permutation with a unique descent at \(k\) is increasing on the two intervals separated at \(k\). Applying the same property to its inverse, and using \(\pi=\pi^{-1}\), shows that every such involution interchanges two adjacent blocks of a common positive length \(r\), fixes all other positions, and has the form
\[
\pi=(1,\dots,a,\ a+r+1,\dots,a+2r,\ a+1,\dots,a+r,\ a+2r+1,\dots,n).
\]
Here \(0\le a\le n-2r\); the number of fixed points is \(f=n-2r\). To see the block characterization directly, take the unique descent at \(k\). The positions in \([1,k]\) mapping across \(k\) must be the last \(r\) left positions, by increasing order of that half; the positions in \([k+1,n]\) mapping back across \(k\) must be the first \(r\) right positions. Increasing order in both value halves forces the crossing images to occupy the adjacent last \(r\) left and first \(r\) right values. Every noncrossing row must therefore be fixed. The sole descent is at the block boundary. Thus, for \(n-f=2r\ge2\), exactly \(f+1\) elements have one descent, one for each \(a=0,\dots,f\). Nonidentity involutions cannot have zero descents. Consequently
\[
\Pr(D_{n,f}\le1)=\Pr(D_{n,f}=1)=\frac{f+1}{N_{n,f}}.
\]

**2. Conditional mean.** Put \(m=n-f\). For any fixed adjacent indices \(i,i+1\), both fixed produces no descent; if they are paired to one another, probability \(m/[n(n-1)]\), they always give a descent. If exactly one is fixed, the two cases each have probability \(fm/[n(n-1)]\), with conditional descent probabilities \((i-1)/(n-2)\) and \((n-i-1)/(n-2)\). If both move but are not paired, probability \(m(m-2)/[n(n-1)]\), exchange symmetry of their distinct partners gives conditional descent probability \(1/2\). Adding these contributions gives the location-independent probability
\[
\Pr(\pi(i)>\pi(i+1))=\frac{m(n+f)}{2n(n-1)}.
\]
This computation applies for \(n\ge3\); the \(n=2\) case is checked immediately. Summing over \(n-1\) adjacent pairs yields the exact, previously accessible expectation
\[
\mathbb ED_{n,f}=\frac{n^2-f^2}{2n}.
\]
In particular \(\mathbb ED_{n,f}>\mathbb ED_{n,f+2}\) whenever \(0\le f\le n-4\) and \(n-f\) is even.

**3. Opposition of lower tail and mean.** The class cardinality ratio is
\[
\frac{N_{n,f+2}}{N_{n,f}}=\frac{n-f}{(f+1)(f+2)}.
\]
Therefore
\[
\frac{\Pr(D_{n,f}\le1)}{\Pr(D_{n,f+2}\le1)}
=\frac{n-f}{(f+2)(f+3)}.
\]
When the last quotient exceeds one, \(D_{n,f}\not\succeq_{\mathrm{st}}D_{n,f+2}\), because the lower-tail inequality is reversed at one descent. Conversely, \(D_{n,f+2}\not\succeq_{\mathrm{st}}D_{n,f}\), because stochastic domination of integrable laws would imply the corresponding mean inequality, contrary to Step 2. This proves incomparability throughout the indicated quadratic region.

**4. Sharp onset for the two lowest strata.** Put \(f=0\), so the strict lower-tail inequality is equivalent to \(n>6\). This proves incomparability for every even \(n\ge8\). For the remaining positive even sizes, the exact descent-count histograms (unnormalized, in ascending descent order, with zero coefficients suppressed) are
\[
\begin{array}{c|cc}
n & f=0 & f=2\\ \hline
2&(1)\text{ at }1 &(1)\text{ at }0\\
4&(1,1,1)\text{ at }1,2,3 &(3,3)\text{ at }1,2\\
6&(1,3,7,3,1)\text{ at }1,2,3,4,5 &(3,15,21,6)\text{ at }1,2,3,4
\end{array}
\]
Dividing rows by respective totals \((1,1)\), \((3,6)\), and \((15,45)\), direct comparison of the finite cumulative sums shows \(D_{n,0}\succeq_{\mathrm{st}}D_{n,2}\) in all three remaining cases. These tables can be obtained by enumerating matchings; an direct generator is included in the verification program.

## Verification

The accompanying standard-library program `check_involutions.py` enumerates all involutions through order \(12\), separately tallies their descent distributions and fixed points, checks the one-descent block characterization and exact conditional means, and tests the sharp small and first larger cases by rational arithmetic. It also verifies the quadratic tail-ratio sign algebra for admissible \(n<100\). It returned `PASS: 4893 exact assertions`. These finite diagnostics do not replace the all-size argument in Steps 1–4.

## Relationship to prior work

The joint descent/fixed-point enumerator is classical; in particular Dukes (2004) records the Désarménien–Foata generating function and separate results for all involutions and fixed-point-free involutions. Guo–Zeng (2005) establish unimodality of the separate descent enumerators. Chow (2008) gives general involution descent-set enumeration. Kim–Lee (2018) treat descents on conjugacy classes asymptotically, and Gessel–Zhuang (2020, Section 5.1) give a stronger complete joint enumerator involving peaks, descents, and fixed points. Those generating functions can in principle recover every finite distribution, so the formulas for the one-descent count and conditional mean are not claimed as novel in isolation. The claim assessed here is the explicit all-size, across-class stochastic **incomparability** region together with the sharp first failure at \(n=8\), which is not stated in the materials inspected. Priority remains qualified.

## Limitations

The sufficient quadratic incomparability region need not be maximal for arbitrary \(f\). The theorem gives a complete stochastic-order classification only for the pair \(f=0,2\). It does not assert an ordering of the full involution distribution as \(f\) varies or independence of descent indicators. Historic implicit coverage, especially via complete fixed-point-refined generating functions, remains possible. No independent audit has been performed.

## References

- W. M. B. Dukes, *Permutation statistics on involutions*, arXiv:math/0412222v1, first posted 2004-12-11. https://arxiv.org/html/math/0412222v1
- V. J. W. Guo and J. Zeng, *The Eulerian Distribution on Involutions is Indeed Unimodal*, arXiv:math/0504195, first posted 2005-04-10. https://arxiv.org/html/math/0504195v3
- C.-O. Chow, *On the Eulerian Enumeration of Involutions*, Electron. J. Combin. 15 (2008), R71. https://doi.org/10.37236/795
- S. Kim and S. Lee, *Central limit theorem for descents in conjugacy classes of the symmetric group*, arXiv:1803.10457 (2018). https://arxiv.org/abs/1803.10457
- I. M. Gessel and Y. Zhuang, *Plethystic formulas for permutation enumeration*, arXiv:2001.00654 (2020), Section 5.1. https://arxiv.org/html/2001.00654v2
