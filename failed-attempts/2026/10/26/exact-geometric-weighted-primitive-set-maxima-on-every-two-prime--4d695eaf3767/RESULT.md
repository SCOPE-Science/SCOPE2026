# Exact geometric-weighted primitive-set maxima on every two-prime semigroup

## Finding
Let \(p<q\) be distinct primes and \(t>0\). A set \(S\) of integers greater than \(1\), each of the form \(p^a q^b\) for nonnegative integers \(a,b\), is *primitive* if no two distinct elements divide one another. For every integer \(d\ge1\), define the complete multiplicative-degree layer
\[
L_d=\{p^i q^{d-i}:0\le i\le d\},\qquad W_d(t)=\sum_{i=0}^d p^{-it}q^{-(d-i)t}.
\]
Then every primitive set is finite and
\[
\max_{S\text{ primitive}}\sum_{n\in S}n^{-t}=\max_{d\ge1}W_d(t).
\]
Equality occurs *only* for a complete layer \(S=L_d\) at a maximizing index \(d\). There are either one or two such indices; in the latter case they are consecutive. Put \(x=p^{-t}\), \(y=q^{-t}\) and \(z=y/x\). The exact rank-selection rule is that the smallest integer \(d\ge1\) with
\[
R_d(t):=\frac{W_{d+1}(t)}{W_d(t)}=x\frac{1-z^{d+2}}{1-z^{d+1}}\le1
\]
is maximizing; if equality holds, precisely \(d\) and \(d+1\) maximize.

For every prime pair there is exactly one critical exponent \(t_{p,q}>0\), the solution of
\[
p^{-2t}+(pq)^{-t}+q^{-2t}=p^{-t}+q^{-t}.
\]
The prime pair \(\{p,q\}\) itself is an optimal primitive set if and only if \(t\ge t_{p,q}\). It is the unique optimizer when \(t>t_{p,q}\), and ties precisely with \(\{p^2,pq,q^2\}\) when \(t=t_{p,q}\). Uniformly over *all* two-prime supports the sharp threshold is
\[
 t_* =t_{2,3}=0.4606716038733825692830131734435\ldots.
\]
Thus every prime pair is the unique optimizer for \(t>t_*\); at \(t=t_*\) only \(\{2,3\}\) has the stated additional layer optimizer; for every \(0<t<t_*\), the support \(\{2,3\}\) supplies a strict counterexample to universal prime-layer optimality.

## Assumptions and scope
The primes are distinct and ordered \(2\le p<q\). The weight exponent \(t\) is any positive real, including values below one. The integer \(1\), which would give the trivial primitive singleton \(\{1\}\), is explicitly excluded, consistent with the motivating restricted-prime literature. The prime support has exactly two elements. No assertion is made for three or more distinct prime factors or for the logarithmic weight \(1/(n\log n)\).

## Proof
**Finite antichains and the sharp size bound.** Represent each element uniquely by its exponent pair \((a,b)\in\mathbb Z_{\ge0}^2\), except for \((0,0)\). Divisibility is coordinatewise order. If distinct elements of a primitive set are arranged by increasing first exponent, their second exponents strictly decrease. An infinite such arrangement is impossible, since the second exponents are nonnegative integers; hence every primitive set has finite cardinality \(r\).

For \(r\ge2\), enumerate pairs as \((a_i,b_i)\), with \(0\le i<r\), \(a_0<\cdots<a_{r-1}\) and \(b_0>\cdots>b_{r-1}\). Integrality gives \(a_i\ge i\) and \(b_i\ge r-1-i\). Since \(x,y\in(0,1)\), termwise
\[
 x^{a_i}y^{b_i}\le x^i y^{r-1-i},\quad
 \sum_{n\in S}n^{-t}\le W_{r-1}(t).
\]
The inequality is strict unless \((a_i,b_i)=(i,r-1-i)\) for every \(i\), which is exactly \(S=L_{r-1}\). If \(r=1\), the unique element is at least \(p\), so the weighted sum is at most \(x<W_1=x+y\); a singleton is never globally optimal. Conversely every \(L_d\) is primitive and attains \(W_d\). This proves the maximum and characterizes all equality cases once the layer sequence is controlled.

**Strictly declining successive ratios.** For \(d\ge1\), the finite geometric sum gives
\[
W_d=x^d\frac{1-z^{d+1}}{1-z},\qquad
R_d=x\left(1+\frac{(1-z)z^{d+1}}{1-z^{d+1}}\right).
\]
The function \(u\mapsto u/(1-u)\) is strictly increasing on \((0,1)\), whereas \(z^{d+1}\) strictly decreases with \(d\). Hence \(R_d\) is strictly decreasing, with \(\lim_{d\to\infty}R_d=x<1\). The weights therefore rise and then fall, allowing a unique maximum or one two-layer tie. Selecting the smallest \(d\ge1\) with \(R_d\le1\) yields exactly the rule stated; if \(R_d=1\), the next ratio is strictly smaller.

**Prime-layer thresholds.** The prime layer is maximizing precisely when \(R_1\le1\), or
\[
\frac{x^2+xy+y^2}{x+y}\le1.
\]
For positive \(x,y\), the function \(H(x,y)=(x^2+xy+y^2)/(x+y)\) is strictly increasing in each argument, because
\[
\frac{\partial H}{\partial x}=\frac{x^2+2xy}{(x+y)^2}>0,\qquad
\frac{\partial H}{\partial y}=\frac{y^2+2xy}{(x+y)^2}>0.
\]
Both \(p^{-t}\) and \(q^{-t}\) strictly decrease in \(t\), so \(H(p^{-t},q^{-t})\) decreases continuously from \(3/2\) as \(t\downarrow0\) to \(0\) as \(t\to\infty\). It equals one at a unique positive \(t_{p,q}\). At equality, strict decrease of the ratios makes exactly ranks one and two optimal.

Finally \(p\ge2\) and \(q\ge3\), with at least one strict inequality unless \((p,q)=(2,3)\). Thus \(H(p^{-t},q^{-t})\le H(2^{-t},3^{-t})\), strictly for every other pair. The largest of all critical exponents is \(t_{2,3}\). Solving the defining one-variable continuous monotone equation by arbitrary-precision bisection gives its stated decimal approximation; the theorem defines this constant by the exact equation, so the decimal is not a proof prerequisite.

## Verification
A standalone reproducibility checker (`verify.py`) exhaustively enumerates the \(922\) nonempty permissible antichains in the \(6\)-by-\(6\) exponent grid after excluding \(\{(0,0)\}\). It compares their reciprocal sums to the sharp cardinality bounds using exact rational arithmetic, checks that equality forces the entire layer, and performs independent numerical tests of the rank-selection formula for five prime pairs at twelve weight exponents. The checker prints `VERIFIED rational_antichains 922 grid_side 6 prime_pairs 5 exponent_tests 12 critical_2_3 0.460671603873383`. The finite check corroborates but does not replace the infinite proof above.

## Relationship to prior work
Banks and Martin, *Optimal primitive sets with restricted primes*, arXiv:1301.0948v1 (5 January 2013), study precisely the restricted-prime primitive-set setting and prove a weighted sufficient optimality theorem under their stated \(t>1\) hypothesis. For a two-prime support, their Theorem 6 condition \(x+y\le1+\sqrt{1-x^2-y^2}\) is algebraically equivalent to \(x^2+xy+y^2\le x+y\); thus the **threshold inequality itself is not claimed as an unrelated new criterion**. The contribution here is the exact global value and complete optimizer classification at every \(t>0\), especially the subcritical region where higher-degree layers win, its unique-or-adjacent-ranks rigidity, and the sharp uniform two-prime critical exponent below one. Their paper does not state this exact all-exponent and all-optimizer theorem. Later work on critical exponents for general \(k\)-primitive sets concerns a different, unrestricted prime-support domain. Generic antichain results concern a related exponent poset, but no inspected source supplies the claimed geometric-weighted exact ranking for every prime pair.

## Limitations
This theorem does not assert originality over inaccessible or unindexed mathematics, and relevant weighted-poset work may contain equivalent formulations. The analytic numerical critical value is approximate; the defining equation is exact. Nothing here resolves weighted optimization with three or more primes, Erdős's logarithmic primitive-set conjecture (subsequently settled in separate literature), or any nonpositive exponent. No independent mathematical audit has been performed.

## References
1. W. D. Banks and G. Martin, *Optimal primitive sets with restricted primes*, arXiv:1301.0948v1 (5 January 2013); *Integers* **13** (2013), A69, published 10 October 2013.
2. T. H. Chan, J. D. Lichtman and C. Pomerance, *On the critical exponent for k-primitive sets*, arXiv:2012.01677v1 (3 December 2020).
3. D. Bouyssou, T. Marchant and M. Pirlot, *About maximal antichains in a product of two chains: A catch-all note*, arXiv:2410.16243v1 (21 October 2024); related finite-poset literature, with only its abstract inspected here.
