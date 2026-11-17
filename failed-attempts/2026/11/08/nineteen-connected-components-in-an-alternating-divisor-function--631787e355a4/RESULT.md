# Nineteen connected components in an alternating divisor-function range

## Finding

Let \(s_{-3}:\mathbb N\to(0,1]\) be the multiplicative arithmetic function uniquely specified, for every prime \(p\) and integer \(a\ge0\), by
\[
s_{-3}(p^a)=u_p(a):=\sum_{j=0}^{a}(-p^{-3})^j
=\frac{1-(-p^{-3})^{a+1}}{1+p^{-3}}.
\]
Define \(P=(2,3,5,7)\), \(T=\prod_{p\ge11}(1-p^{-3})\), and for every four-tuple \(\mathbf a=(a_2,a_3,a_5,a_7)\) of nonnegative integers let
\[
c(\mathbf a):=u_2(a_2)u_3(a_3)u_5(a_5)u_7(a_7).
\]
**The topological closure \(\overline{s_{-3}(\mathbb N)}\) has exactly nineteen connected components.** Its components, ordered from smallest to largest, are exactly the intervals \([Tc(\boldsymbol\ell_i),c(\mathbf r_i)]\) given by the following table. Each tuple lists exponents at the ordered primes \((2,3,5,7)\).

| \(i\) | \(\boldsymbol\ell_i\) | \(\mathbf r_i\) |
|---:|:---:|:---:|
| 1 | \((1,1,1,1)\) | \((1,2,2,0)\) |
| 2 | \((1,1,0,1)\) | \((1,2,0,0)\) |
| 3 | \((3,1,1,1)\) | \((2,2,0,0)\) |
| 4 | \((1,0,1,1)\) | \((1,0,2,2)\) |
| 5 | \((1,0,1,0)\) | \((1,0,2,0)\) |
| 6 | \((1,0,0,1)\) | \((1,0,0,2)\) |
| 7 | \((1,0,0,0)\) | \((1,0,0,0)\) |
| 8 | \((3,0,1,1)\) | \((4,0,2,2)\) |
| 9 | \((2,0,1,1)\) | \((4,0,2,0)\) |
| 10 | \((2,0,1,0)\) | \((2,0,2,0)\) |
| 11 | \((3,0,0,1)\) | \((4,0,0,2)\) |
| 12 | \((2,0,0,1)\) | \((4,0,0,0)\) |
| 13 | \((2,0,0,0)\) | \((2,0,0,0)\) |
| 14 | \((0,1,1,1)\) | \((0,2,2,0)\) |
| 15 | \((0,1,0,1)\) | \((0,2,0,0)\) |
| 16 | \((0,0,1,1)\) | \((0,0,2,2)\) |
| 17 | \((0,0,1,0)\) | \((0,0,2,0)\) |
| 18 | \((0,0,0,1)\) | \((0,0,0,2)\) |
| 19 | \((0,0,0,0)\) | \((0,0,0,0)\) |

In particular, the leftmost endpoint is \(1/\zeta(3)\), the rightmost endpoint is \(1\), and there are exactly eighteen genuine open gaps. The tail product has the exact expression
\[
T=\frac{1}{\zeta(3)\prod_{p\in P}(1-p^{-3})}.
\]

## Assumptions and scope

The domain is all positive integers; \(\overline{\cdot}\) means closure in \(\mathbb R\). The parameter is precisely \(r=3\), not a neighborhood of that value. All nineteen interval endpoints are exact expressions in rational numbers and \(1/\zeta(3)\); the displayed table is not a floating-point approximation.

## Proof

**1. The prime tail is an interval.** For each prime \(p\ge11\), put \(w_p=-\log(1-p^{-3})>0\). We first prove the tail-domination inequality
\[
w_p\le\sum_{q>p}w_q\qquad(p\ge11,\ q\text{ prime}). \tag{1}
\]
Equivalently, \(\prod_{q>p}(1-q^{-3})\le1-p^{-3}\). For every prime \(11\le p<137\), the stronger *finite* product inequality
\[
\prod_{p<q\le3p}(1-q^{-3})<1-p^{-3} \tag{2}
\]
is checked with exact rational arithmetic in `verify.py` (all 28 primes in this range, with an ordinary integer sieve). For \(p\ge137\), the classical Rosser--Schoenfeld bounds \(x/\log x<\pi(x)<1.25506x/\log x\) for \(x\ge17\), where \(\pi(x)\) counts primes at most \(x\) and \(\log\) is natural logarithm, imply
\[
\pi(2p)-\pi(p)>
\left(\frac{12}{7}-1.25506\right)\frac{p}{\log p}
>\left(\frac{12}{7}-1.25506\right)\frac{137}{5}>12.
\]
Here \(\log(2p)\le(7/6)\log p\) because \(p\ge64\), \(\log p<5\) at \(p=137\) and \(p/\log p\) is increasing for \(p>e\). Consequently at least thirteen primes lie in \((p,2p]\); using any nine of them yields
\[
\prod_{p<q\le2p}(1-q^{-3})
\le(1-(8p^3)^{-1})^9
\le1-\frac9{8p^3}+\frac{36}{64p^6}
<1-p^{-3},
\]
where the quadratic Taylor upper bound applies for \(0\le (8p^3)^{-1}\le1\). This proves (1) for all primes.

The positive summable sequence \((w_p)_{p\ge11}\) decreases to zero. The elementary subsum lemma says that if each term of a positive summable sequence is at most the sum of all later terms, then the closure of its finite subset sums is the whole interval from zero to the total sum. For completeness, this follows recursively by choosing whether to subtract the current term according to the remaining target, keeping the remainder inside the available tail total; residual tail totals tend to zero. Apply it to \(w_p\) and exponentiate. Products \(\prod_{p\in F}(1-p^{-3})\), over finite sets \(F\) of primes at least eleven, are dense in \([T,1]\). Since each local factor \(u_p(a)\) is in \([1-p^{-3},1]\), the entire tail range also has closure exactly \([T,1]\).

**2. Finite reduction.** Multiplicativity gives
\[
\overline{s_{-3}(\mathbb N)}
=\bigcup_{\mathbf a\in(\mathbb Z_{\ge0}\cup\{\infty\})^4}
[c(\mathbf a)T,c(\mathbf a)],\tag{3}
\]
where \(u_p(\infty)=1/(1+p^{-3})\). The union is compact because the exponent space, with each integer tending to \(\infty\), is compact and multiplication is continuous.

For each \(p\in P\), the alternating-series bounds imply that all \(u_p(a)\) with \(a\ge5\), including \(a=\infty\), lie between \(u_p(5)\) and \(u_p(6)\). Hence all infinitely many exponent choices are covered by exactly \(6^4=1296\) rational coefficient rectangles: in each coordinate use one of the exact values at exponent \(0,1,2,3,4\), or the closed interval between the values at exponents five and six. For a resulting product-coefficient interval \([L,H]\), its contribution to (3) is contained in \([LT,H]\).

**3. Exact nineteen-component certificate.** Restrict first to \(a_p\in\{0,1,2,3,4\}\), producing \(5^4=625\) distinct rational products \(c\). Order these products increasingly. The intervals \([cT,c]\) meet their immediate predecessors precisely when \(c_{j+1}T\le c_j\); strict reverse inequalities separate components. The verifier determines \(T\) between two exact rationals by downward rounding the first 200,000 terms of \(\zeta(3)=\sum_{n\ge1}n^{-3}\) at scale \(10^{20}\), and bounding the remaining tail by an integral. Every one of the 624 adjacency tests is determined *strictly*, even at the interval-enclosure endpoints. Exactly 606 adjacent pairs overlap and 18 are separated, giving exactly nineteen finite-component intervals, with the endpoints in the table above.

Finally, for every one of the 1296 coordinate rectangles, the verifier checks by *exact rational comparisons* that its entire coefficient interval \([L,H]\) is contained in one of those nineteen finite-component coefficient spans \([c_{\mathrm{first}},c_{\mathrm{last}}]\). It follows that \([LT,H]\) is covered by the corresponding finite-component interval \([c_{\mathrm{first}}T,c_{\mathrm{last}}]\). No omitted exponent, including the accumulation exponent \(\infty\), creates an additional point outside the nineteen intervals. Conversely, every finite-component interval is filled by overlapping intervals from actual finite exponent choices and the continuous prime tail. This proves both the precise endpoints and the assertion of nineteen connected components.

## Verification

Run `python3 verify.py` with the standard Python library. It uses integer sieving and exact `fractions.Fraction` throughout the certificates. It confirms the 28 finite prime-tail inequalities, the rigorous zeta enclosure, 625 distinct rational coefficients, 606 certified overlaps, 18 certified strict gaps, and 671 additional rectangles involving a large exponent state, each lying inside one certified component. The smallest positive containment slack for these additional rectangles is greater than \(2.14\cdot10^{-8}\). The program also evaluates the multiplicative function directly on the first 3000 positive integers as a nonessential corroborative check. The infinite tail is proved analytically in Step 1; no numerical experiment is used as an infinite proof.

## Relationship to prior work

Defant introduced \(s_{-r}\), proved the sharp one-interval threshold \(\eta_A\approx1.9011618\), and asked which parameters yield a prescribed number of connected components. The previously published exact two-interval instance for \(s_{-2}\) does not imply the nineteen intervals at \(r=3\), nor their endpoints. Sanna's method and Zubrilina's component bounds treat the *ordinary* generalized divisor function \(\sigma_{-r}\), whose local prime-power values are \(1+p^{-r}+\cdots+p^{-ar}\), not the alternating function considered here. Their statements therefore do not imply the result, although their methods provide useful context. These are implication comparisons, not claims of exhaustive priority.

## Limitations

The exact component count is proved only for \(r=3\). There is no asserted classification for nonintegral parameters or larger integers, no formula for component densities, and no claim of historical uniqueness beyond the inspected literature and mathematical-claim searches. The finite certificate is essential for the 625 interval adjacency and 1296 containment comparisons, but its arithmetic is finite, deterministic, and auditable.

## References

1. Colin Defant, *On Ranges of Variants of the Divisor Functions that are Dense*, arXiv:1507.01128v1, July 4, 2015, Definition 1.1, Theorems 2.3--2.4 and Section 3, https://arxiv.org/abs/1507.01128.
2. Carlo Sanna, *On the Closure of the Image of the Generalized Divisor Function*, arXiv:1507.08091v1, July 29, 2015, https://arxiv.org/abs/1507.08091.
3. Nina Zubrilina, *On the Number of Connected Components of Ranges of Divisor Functions*, arXiv:1711.02871v1, November 8, 2017, https://arxiv.org/abs/1711.02871.
4. J. B. Rosser and L. Schoenfeld, *Approximate Formulas for Some Functions of Prime Numbers*, Illinois Journal of Mathematics 6 (1962), 64--94, https://doi.org/10.1215/ijm/1255631807.
