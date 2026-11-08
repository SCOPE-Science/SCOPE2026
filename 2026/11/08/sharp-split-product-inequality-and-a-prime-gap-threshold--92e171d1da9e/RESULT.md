# Sharp split-product inequality and a prime-gap threshold

## Finding

Let \(x\ge 2\) and \(G>0\) be real numbers. Let \(U,V\) be finite sets of **distinct integers**, with \(V\ne\varnothing\), \(2\le u\le x\) for every \(u\in U\), and \(v\ge x+G\) for every \(v\in V\). Assume
\[
d:=\sum_{u\in U}u-\sum_{v\in V}v>0.
\]
Then the following universal inequality is **sharp**:
\[
\boxed{\frac{\prod_{u\in U}u}{\prod_{v\in V}v}\ge\frac{d+G}{2}.}
\]
The constant \(1/2\) cannot be increased, even when both sets are nonempty: for integers \(t\ge3\), take \(U=\{t,t+1\}\), \(V=\{2t\}\), \(x=t+1\), \(G=t-1\), and \(d=1\). The quotient of the left side by \(d+G\) is \((t+1)/(2t)\to1/2\).

**Prime-partition consequence.** Let \(A\) be a nonempty finite set of distinct primes that uniquely minimizes the product among prime sets with the same sum \(d\), and set \(M=\prod_{p\in A}p\). Let \(x>d\) be prime, and let \(y\) be the next prime. If \(y-x>2M\), then the unique maximum-product set of distinct primes summing to
\[
n=\sum_{p\le x,\ p\text{ prime}}p-d
\]
is precisely \(\{p\le x:p\text{ prime}\}\setminus A\). This improves the sufficient prime-gap hypothesis \(y-x>11M\) in Campbell's 2026 construction; the constant \(2\) here is sufficient, not asserted necessary or optimal for prime-only sets.

## Assumptions and scope

All products are over the listed elements without repetitions. The hypothesis requires integer sets (not multisets); the endpoint \(x\) and the gap \(G\) may be real. Since \(G>0\), every element of \(V\) is strictly larger than every element of \(U\). The sum difference \(d\) is a positive integer. The result is unconditional and applies to sets of composite as well as prime integers. For the consequence, "product-minimal" is a condition imposed on \(A\); no method for finding such an \(A\) is claimed.

## Proof

**1. Ordered reduction.** Write \(b=|V|\ge1\). Because each element of \(V\) exceeds every element of \(U\), the positive sum difference forces \(|U|=a+b\) with \(a\ge1\). Order
\[
U=\{u_1<\cdots<u_{a+b}\},\qquad V=\{v_1<\cdots<v_b\}.
\]
Put \(w_i=u_i\) for \(1\le i\le a\), \(T=\sum_{i=1}^a w_i\), \(Q=\prod_{i=1}^a w_i\), and \(m=w_a\). Define \(\Delta_j=v_j-u_{a+j}\). Each \(\Delta_j\) is a positive integer and \(\Delta_j\ge G\); moreover
\[
D:=\sum_{j=1}^{b}\Delta_j=T-d\le T-1,
\qquad d+G\le T.
\]
The desired product ratio equals
\[
\frac{Q}{\prod_{j=1}^{b}(1+\Delta_j/u_{a+j})}.
\]

**2. One extra factor.** If \(a=1\), write \(w_1=T=Q=t\). The elementary product inequality \(\prod_j(1-z_j)\ge1-\sum_jz_j\) for \(0\le z_j\le1\), with \(z_j=\Delta_j/v_j\), implies
\[
\frac{\prod U}{\prod V}
=t\prod_j(1-\Delta_j/v_j)
\ge t\left(1-\frac{D}{t+G}\right)
=\frac{t(d+G)}{t+G}.
\]
Since \(D\ge G\) and \(d>0\), we have \(G<t\), so this is strictly greater than \((d+G)/2\).

**3. General reduction to finite rational inequalities.** Suppose \(a\ge2\). Since \(u_{a+j}\ge m+1\), Bernoulli's inequality for positive integer \(\Delta_j\) gives
\[
1+\frac{\Delta_j}{u_{a+j}}
\le\left(1+\frac1{u_{a+j}}\right)^{\Delta_j}
\le\left(1+\frac1{m+1}\right)^{\Delta_j}.
\]
Thus, setting \(B_m=1+1/(m+1)\),
\[
\frac{\prod U}{\prod V}\ge Q B_m^{-(T-1)}.
\]
It suffices to prove \(S(w_1,\ldots,w_a):=2Q/(T B_m^{T-1})\ge1\), except that we treat one two-factor pattern directly.

**4. Two extra factors.** Write \(w_1=u<w_2=v\). When \(u\ge8\), \(2uv/(u+v)>u\ge8\) while \(B_v^{u+v-1}<e^2<(11/4)^2<8\). For fixed \(3\le u\le7\), \(2uv/(u+v)\) increases with \(v\), whereas \(B_v^{u+v-1}\) decreases with \(v\) (the calculus verification is below). Thus it suffices to check \(v=u+1\); the five strict comparisons are in the exact rational verifier. For \(u=2\) and \(v\ge5\), \(2uv/(u+v)=4v/(v+2)\ge20/7>e>B_v^{v+1}\). The remaining case \((u,v)=(2,4)\) satisfies \(16/6>(6/5)^5\).

For \((u,v)=(2,3)\), the coarse bound \(S\ge1\) is unnecessary: \(T=5\), \(Q=6\), \(1\le D\le4\), \(1\le b\le4\), and \(u_{2+j}\ge j+3\). Directly enumerating the positive integer compositions \(D=\Delta_1+\cdots+\Delta_b\) for \(D\le4\) yields
\[
\max\prod_{j=1}^b\left(1+\frac{\Delta_j}{j+3}\right)
\le\frac{21}{10};
\]
the maxima at \(b=1,2,3,4\) are respectively \(2,21/10,21/10,2\). Consequently \(\prod U/\prod V\ge6/(21/10)=20/7>5/2\ge(d+G)/2\). Each of the 15 compositions is checked exactly in the included program.

**5. Three or more extra factors.** For three distinct integers \(2\le u<v<m\), the inequality \(S(u,v,m)>1\) is equivalent to
\[
\frac{2muv}{m+u+v}>
\left(1+\frac1{m+1}\right)^{m+u+v-1}.
\]
For \(uv\ge32\), the left side exceeds \(2uv/3\ge64/3\), while the right side is below \(e^3<(11/4)^3<64/3\), because \(u+v<2m\). For \(uv\le31\), there are exactly 24 pairs of integers \(2\le u<v\). For fixed \(u,v\), the left side increases with \(m\). The right side decreases with \(m\): writing \(z=m+1\), the derivative of its logarithm is at most
\[
\frac1z-\frac{z+u+v-2}{z(z+1)}=
\frac{3-u-v}{z(z+1)}<0.
\]
Thus it is sufficient to check the 24 rational inequalities at \(m=v+1\), as the included standalone verifier does (the smallest left/right ratio occurs at \((u,v,m)=(2,3,4)\) and exceeds one).

For any \(a\ge3\), append a new largest integer \(w>m\) to \((w_1,\ldots,w_a)\), whose sum is \(T\ge9\). The quotient of the new \(S\) by the old \(S\) is
\[
\frac{wT}{T+w}\cdot
\frac{B_m^{T-1}}{B_w^{T+w-1}}
\ge\frac{wT}{T+w}\,B_w^{-w}
>\frac{wT}{e(T+w)}
\ge\frac{45}{14e}>1,
\]
where \(w\ge5\), \(T\ge9\) and \(e<11/4\). Induction from the three-factor case establishes \(S>1\) for every \(a\ge3\). Combined with Steps 2–4 and \(d+G\le T\), this proves the universal bound. The displayed family proves sharpness.

**6. Prime-gap consequence.** Write \(\mathcal B_x=\{p\le x:p\text{ prime}\}\). Any distinct-prime set \(E\) summing to \(n=\sum_{p\in\mathcal B_x}p-d\) has \(U=\mathcal B_x\setminus E\), \(V=E\setminus\mathcal B_x\), with \(\sum U-\sum V=d\). If \(V=\varnothing\), product-minimality gives \(\prod U\ge M\), with equality only for \(U=A\). Otherwise every prime in \(V\) is at least \(y=x+G\), so the sharp inequality gives \(\prod U/\prod V\ge(d+G)/2>G/2>M\). Since \(\prod E=(\prod_{p\in\mathcal B_x}p)(\prod V/\prod U)\), the unique maximizer is \(\mathcal B_x\setminus A\).

## Verification

Run `python3 verify.py` with Python 3 standard library. It checks all 24 critical three-factor inequalities, the five two-factor comparisons and one extra case, all 15 exceptional positive compositions, and 4,790 independent finite \((U,V)\) examples by exact rational arithmetic. None of these finite checks proves the unrestricted inequality alone: the reductions and monotonicity arguments in Steps 1–6 are essential. The bound \(e<11/4\) follows immediately by bounding the tail of its defining series after the first four terms.

## Relationship to prior work

Campbell's October 2026 article proves \(\prod U/\prod V\ge(2/e^3)(d+G)>(d+G)/11\) in precisely this split-set framework (Lemma 5), and applies it with the hypothesis \(G>11M\) to distinct-prime product optimization (Lemma 6). Its Theorem 1 resolves the unboundedness of the difference between maximal prime-partition length and maximal-product prime-partition length; that resolution is **prior work**, not a claim here. The new statement establishes the sharp universal constant \(1/2\) and the resulting sufficient threshold \(G>2M\). Deléglise and Nicolas study the related but different maximum-product function with prime sum bounded above, rather than the sharp split-set gap constant.

## Limitations

The factor \(1/2\) is optimal for unrestricted integer sets, not necessarily for prime-only sets. The sufficient prime-gap threshold \(2M\) is not claimed necessary. This does not strengthen the already-established qualitative unbounded-gap theorem itself, nor give new prime-gap existence estimates. Although the contemporary motivating article and relevant earlier product-optimization source were inspected, the complete historical literature on split-product inequalities has not been exhaustively indexed or independently audited.

## References

1. J. M. Campbell, *On a problem on partitions into distinct primes*, arXiv:2610.19534v1, posted 2026-10-14; Lemmas 5–6 and Theorem 1. https://arxiv.org/abs/2610.19534
2. M. Deléglise and J.-L. Nicolas, *Maximal product of primes whose sum is bounded*, arXiv:1207.0603 (2012); published in Proc. Steklov Inst. Math. 282 (2013), S73–S102. https://arxiv.org/abs/1207.0603
