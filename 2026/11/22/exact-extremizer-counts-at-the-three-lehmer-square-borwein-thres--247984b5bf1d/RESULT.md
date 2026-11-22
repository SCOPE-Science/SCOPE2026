# Exact extremizer counts at the three Lehmer-square Borwein thresholds

## Finding

Let
\[
L(x)=x^{10}+x^9-x^7-x^6-x^5-x^4-x^3+x+1.
\]
A *Borwein polynomial* is a polynomial \(Q\in\mathbb Z[x]\) with coefficients in \(\{-1,0,1\}\) and nonzero constant and leading coefficients. Define \(Q^*(x)=x^{\deg Q}Q(1/x)\). Restrict attention to \(Q\) divisible by \(L(x)^2\). At the previously determined minimum degrees for the unrestricted, self-reciprocal and antireciprocal classes, the **complete** numbers of polynomials (including both signs) are

| Degree | Class | Number | Additional classification |
|---|---|---:|---|
| \(34\) | unrestricted | \(4\) | one orbit under sign and coefficient reversal |
| \(38\) | \(Q^*=Q\) | \(2\) | one polynomial up to sign |
| \(41\) | \(Q^*=-Q\) | \(4\) | two distinct polynomials up to sign |

More precisely, the complete list is \(Q=\pm L^2H\), where the five normalized quotient-polynomial coefficient vectors below are written in **ascending order**, from the constant term to the leading coefficient:

| Class | \(\deg H\) | Coefficients of \(H\) |
|---|---:|---|
| unrestricted A | 14 | `1,-3,4,-3,0,3,-4,3,-2,1,0,-1,2,-2,1` |
| unrestricted B | 14 | `1,-2,2,-1,0,1,-2,3,-4,3,0,-3,4,-3,1` |
| self-reciprocal | 18 | `1,-2,2,0,-2,3,-2,1,0,0,0,1,-2,3,-2,0,2,-2,1` |
| antireciprocal A | 21 | `1,-3,5,-5,3,0,-2,3,-3,3,-3,3,-3,3,-3,2,0,-3,5,-5,3,-1` |
| antireciprocal B | 21 | `1,-2,3,-3,3,-2,1,1,-3,5,-6,6,-5,3,-1,-1,2,-3,3,-3,2,-1` |

The two degree-\(14\) quotient polynomials are reciprocal reversals of one another. The two antireciprocal degree-\(21\) quotients are distinct even modulo sign and reversal. No inference about counts at larger degrees or powers above \(L^2\) is made.

## Assumptions and scope

All coefficients and operations are over the ordinary integers. The degree is exact, not an upper bound. Sign reversal identifies only the pair \(Q,-Q\); both are included in the table counts. The symmetry classes use \(Q^*=Q\) and \(Q^*=-Q\) exactly, not a convention allowing either sign. The minimum degrees \(34,38,41\), already established by El Otmani, Idris and Sac-Épée, are taken as the motivating known thresholds. The new claim is the exhaustive classification and multiplicity at each threshold.

## Proof

Write \(G=L^2=\sum_{i=0}^{20}g_i x^i\), where the ascending coefficient vector is

`1,2,1,-2,-4,-4,-3,-2,1,6,9,6,1,-2,-3,-4,-4,-2,1,2,1`.

Because \(g_0=g_{20}=1\), a degree-\(D\) polynomial \(Q\) divisible by \(G\) has a **unique** quotient \(H=\sum_{j=0}^{e}h_jx^j\), with \(e=D-20\). Replacing \(Q\) by \(-Q\) if necessary, we may and do assume \(Q(0)=h_0=1\). Let \(a_j=[x^j]Q\). For \(1\le j\le e\), the exact triangular identity is
\[
h_j=a_j-\sum_{i=1}^{\min(20,j)}g_i h_{j-i}.
\]
Every \(a_j\) belongs to \(\{-1,0,1\}\). Thus there are exactly \(3^e\) possible prefixes in the unrestricted class; every admissible normalized \(Q\) appears **once** among them. For each prefix, form the complete product \(Q=GH\), reject it unless every coefficient belongs to \(\{-1,0,1\}\) and the leading coefficient is nonzero.

The polynomial \(G\) is self-reciprocal. Consequently, \(Q^*=\varepsilon Q\) is equivalent to \(H^*=\varepsilon H\), where \(\varepsilon\in\{-1,1\}\). In the self-reciprocal case at \(D=38\), \(e=18\), and only \(a_1,\ldots,a_9\) need be selected: after computing \(h_0,\ldots,h_9\), set \(h_j=h_{18-j}\) for \(10\le j\le18\). In the antireciprocal case at \(D=41\), \(e=21\), and only \(a_1,\ldots,a_{10}\) need be selected: then set \(h_j=-h_{21-j}\) for \(11\le j\le21\). Every member of each class appears exactly once because the first half of its quotient is fixed by the corresponding low-degree coefficients.

The exhaustive integer loops therefore inspect precisely \(3^{14}=4{,}782{,}969\), \(3^{9}=19{,}683\) and \(3^{10}=59{,}049\) possible normalized prefixes in the three classes. Direct convolution and the exact bound \(|[x^k]GH|\le1\) at **every** degree \(0\le k\le D\) yield, respectively, \(2,1,2\) survivors, listed above. The standalone `check.cpp` implements this finite exhaustive argument twice: once by recursion and independently by a base-three counter. Both implementations return the exact listed quotient vectors. The coefficient-reversal statement follows by reversing the first degree-\(14\) vector and obtaining the second. Since no polynomial can have zero constant or leading coefficient under the accepted tests, restoring the two signs gives \(4,2,4\). This proves the classification.

No unverified extrapolation from experiments is needed: the search domain is **mathematically exhaustive** by the triangular recurrence, and the provided program tests every element of that finite domain.

## Verification

Compile `check.cpp` using a C++17 compiler and run it:

```sh
c++ -std=c++17 -O2 check.cpp -o verify
./verify
```

The program prints `normalized=2,1,2`, `signed=4,2,4`, and a final `VERIFIED` line. It checks the entire quotient product, exact degree, allowed alphabet, symmetry and all five quotient vectors in two enumerations. Independent symbolic multiplication with integer arithmetic verifies each of the five displayed products; the self-reciprocal quotient at degree \(18\) also equals \(L(-x)\Phi_4(x)\Phi_6(x)\Phi_{12}(x)\).

## Relationship to prior work

El Otmani, Idris and Sac-Épée, arXiv:2611.18323v1 (first posted 2026-11-13), establish the minimum degrees \(34,38,41\), set up a feasibility system and list **one** polynomial at each admitted degree; their full text and appendix do not state a complete census of minimizers. The present finding counts all such minimizers and distinguishes the two antireciprocal sign classes. It does not re-claim the minimum-degree theorem. Mossinghoff (2003, Section 4 and Algorithm 3) provides examples of height-one polynomials with Lehmer factors of high multiplicity, not the complete counts at these three thresholds. Drungilas–Jankauskas–Šiurys (2018) study Littlewood/Newman multiples of small-degree Borwein polynomials and do not establish this specific Lehmer-square extremizer classification.

## Limitations

This is a finite, exact extremizer classification, not a theorem about the full degree spectrum, the unbounded number of higher-degree Borwein multiples, or multiples of \(L^3\) or \(L^4\). The minimum-degree claims are quoted from the 2026 paper; the new result needs them only to interpret the three exact-degree classes as extremal. An unindexed enumeration or unpublished computational record could overlap the classification. Independent external audit has not been performed.

## References

1. S. El Otmani, M. Idris and J.-M. Sac-Épée, *On Borwein polynomials with multiple roots outside the unit disk*, arXiv:2611.18323v1 (2026-11-13), https://arxiv.org/html/2611.18323v1 .
2. M. J. Mossinghoff, *Polynomials with restricted coefficients and prescribed noncyclotomic factors*, LMS Journal of Computation and Mathematics 6 (2003), 314–325, https://doi.org/10.1112/S1461157000000474 .
3. P. Drungilas, J. Jankauskas and J. Šiurys, *On Littlewood and Newman polynomial multiples of Borwein polynomials*, Mathematics of Computation 87 (2018), 1523–1541, https://doi.org/10.1090/mcom/3258 .
