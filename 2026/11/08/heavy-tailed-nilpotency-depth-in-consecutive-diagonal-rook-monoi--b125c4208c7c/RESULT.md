# Heavy-tailed nilpotency depth in consecutive-diagonal rook monoids

## Finding
For every integer \(n\ge 2\), let \(M_n\) be the finite inverse monoid of partial injections of \([n]=\{1,\ldots,n\}\) represented by the zero matrix or by a nonempty, consecutive block of ones on a single matrix diagonal. Select a **nonzero nilpotent** \(X_n\) uniformly from \(M_n\), and write \(K_n=\min\{j\ge 1:X_n^j=0\}\). The following statements form one nilpotency-depth theorem.

1. There are exactly \(N_n=(n^3-n)/3\) eligible elements. For integers \(1\le t\le n-1\), put
   \[
   T_n(t)=\sum_{h=1}^{\lfloor(n-1)/t\rfloor}
     (n-th)(n-th+1),\qquad T_n(n)=0.
   \]
   Then \(\#\{x\ne0:x\text{ nilpotent},\ K(x)\ge t+1\}=T_n(t)\), and the complete exact index spectrum is
   \[
     \#\{x\ne0:x\text{ nilpotent},\ K(x)=j\}=T_n(j-1)-T_n(j),
     \qquad 2\le j\le n.
   \]
2. For every fixed integer \(j\ge2\),
   \[
     \lim_{n\to\infty}\Pr(K_n=j)=\frac{1}{j(j-1)}.
   \]
   In fact \(\Pr(K_n\ge t+1)=1/t+O(1/n)\), **uniformly** over integers \(1\le t\le n\), where the left side is zero for \(t=n\).
3. Writing \(\tau(a)\) for the number of positive divisors of \(a\), the **exact** mean is
   \[
   \mathbb E K_n=1+\frac{1}{N_n}
     \sum_{a=1}^{n-1}\tau(a)(n-a)(n-a+1).
   \]
   With \(\gamma\) denoting Euler's constant, its sharp asymptotic is
   \[
     \mathbb E K_n=\log n+2\gamma-\frac56+O(n^{-1/2}).
   \]
4. The second moment and variance satisfy
   \[
     \lim_{n\to\infty}\frac{\mathbb E K_n^2}{n}
     =\lim_{n\to\infty}\frac{\operatorname{Var}(K_n)}{n}
     =\frac{\pi^2}{12}.
   \]
   For every fixed \(0<\alpha<1\), the rare macroscopic-depth tail has the exact scale
   \[
   \lim_{n\to\infty}n\Pr\!\left(K_n\ge\lceil\alpha n\rceil\right)
   =3\sum_{h\ge1}(1-\alpha h)_+^2,
   \qquad u_+=\max(u,0).
   \]

The limiting discrete law has an infinite mean, although the mean of every finite monoid is finite. This explains the logarithmic drift of the expectation and the much faster, linear growth of the variance. No statement here treats the empty map as a nonzero nilpotent.

## Assumptions and scope
For a nonzero element choose its nonzero matrix diagonal offset \(d\in\{-(n-1),\ldots,n-1\}\), and let \([a,b]\) be the consecutive domain interval of rows. Every row \(i\in[a,b]\) maps to column \(i+d\). Hence \(1\le a\le b\le n\), and \(1\le a+d\le b+d\le n\). The rank is \(r=b-a+1\). Such a map is idempotent when \(d=0\), and is nilpotent when \(d\ne0\). The least positive vanishing power of a nonzero nilpotent is \(1+\lceil r/|d|\rceil\), as follows from intersecting consecutive translated intervals; this elementwise index formula is known [1]. Its use below is explicit and not claimed as new.

The probability space has cardinality \(N_n=(n^3-n)/3\), excluding the zero matrix (whose index is one) and all idempotents. All limits are as \(n\to\infty\) through integers with the sampling rule unchanged. Natural logarithms are used throughout. The classification is semigroup-theoretic, with primary MSC 20M18.

## Proof
**Exact tail counting.** Fix \(h=|d|\in\{1,\ldots,n-1\}\). For each of the two offset signs, the permitted domain is an interval inside a chain of length \(L=n-h\). For each rank \(1\le r\le L\), there are precisely \(L-r+1\) placements. Thus the total number of nonzero nilpotents equals
\[
 2\sum_{h=1}^{n-1}\sum_{r=1}^{n-h}(n-h-r+1)
 =\sum_{h=1}^{n-1}(n-h)(n-h+1)=\frac{n^3-n}{3}.
\]
The index condition \(1+\lceil r/h\rceil\ge t+1\) is equivalent, for positive integers, to \(r\ge(t-1)h+1\). Summing the permitted placements, and accounting for both signs, gives \((n-th)(n-th+1)\) when \(th\le n-1\), and zero otherwise. This yields \(T_n(t)\) and therefore every exact individual multiplicity by differencing successive tails. In particular the maximum possible index is \(n\).

**The harmonic limit and uniform error.** Let \(1\le t\le n\), and set \(g(x)=(n-tx)_+^2\), a nonincreasing nonnegative function on \([0,\infty)\). Its integral is \(n^3/(3t)\), and the right-endpoint Riemann sum differs from this integral by at most \(g(0)=n^2\). The difference between \(T_n(t)\) and that right-endpoint sum is the nonnegative linear correction \(\sum_{h\ge1}(n-th)_+\), at most \(n^2\). Consequently
\[
 T_n(t)=\frac{n^3}{3t}+O(n^2)
 \quad\text{uniformly for }1\le t\le n.
\]
Since \(N_n=(n^3-n)/3\), division gives \(\Pr(K_n\ge t+1)=1/t+O(1/n)\). For each fixed \(j\ge2\), taking the difference of the tails at \(t=j-1\) and \(t=j\) gives \(1/(j(j-1))\). Their sum over \(j\ge2\) is one.

**The sharp mean.** The tail-sum identity and the exact finite tail formula yield
\[
 \mathbb E K_n=1+\frac1{N_n}\sum_{t=1}^{n-1}T_n(t).
\]
Rearrange the sum by the product \(a=th\). Exactly \(\tau(a)\) positive ordered pairs \((t,h)\) have product \(a\), so this equals the stated divisor-weighted sum.

For completeness, the classical divisor summatory estimate
\[
 D(x):=\sum_{1\le a\le x}\tau(a)
 =x\log x+(2\gamma-1)x+O(\sqrt{x})
\]
follows by splitting the divisors at \(\lfloor\sqrt x\rfloor\): \(D(x)=2\sum_{a\le\sqrt x}\lfloor x/a\rfloor-\lfloor\sqrt x\rfloor^2\), together with \(H_m=\log m+\gamma+1/(2m)+O(m^{-2})\). Partial summation then gives
\[
 \begin{aligned}
 \sum_{a=1}^{n-1}\tau(a)(n-a)^2
 &=2\int_0^n(n-x)D(x)\,dx\\
 &=\frac{n^3}{3}\left(\log n+2\gamma-\frac{11}{6}\right)
    +O(n^{5/2}),\\
 \sum_{a=1}^{n-1}\tau(a)(n-a)&=O(n^2\log n).
 \end{aligned}
\]
Substitution in the exact formula, and \(N_n=n^3/3+O(n)\), proves \(\mathbb E K_n=\log n+2\gamma-5/6+O(n^{-1/2})\).

**Second moment.** The direct rank-and-offset count gives
\[
 \mathbb E K_n^2=\frac2{N_n}
 \sum_{h=1}^{n-1}\sum_{r=1}^{n-h}
 (n-h-r+1)\left(1+\left\lceil\frac rh\right\rceil\right)^2.
\]
For each fixed \(h\), a Riemann-sum limit shows that the inner signed contribution, divided by \(n^4\), tends to \(1/(6h^2)\): explicitly, its limit is \(2h^{-2}\int_0^1(1-u)u^2\,du\). The contribution from a given \(h\), divided by \(n^4\), is bounded by \(C(h^{-2}+n^{-2})\), using \(1+\lceil r/h\rceil\le2+r/h\) and \(\sum_r(n-h-r+1)\le n^2\). Hence the contribution of \(h>H\) is bounded by \(C\sum_{h>H}h^{-2}+O(n^{-1})\), justifying passage to the infinite sum. As \(N_n/n^3\to1/3\),
\[
 \lim_{n\to\infty}\frac{\mathbb E K_n^2}{n}
 =3\sum_{h=1}^{\infty}\frac1{6h^2}
 =\frac{\pi^2}{12}.
\]
Since \((\mathbb E K_n)^2=O((\log n)^2)=o(n)\), the variance has the same limit.

**Macroscopic tail.** For \(j_n=\lceil\alpha n\rceil\), put \(t_n=j_n-1\). In \(T_n(t_n)\) only finitely many offsets \(h\) can contribute for sufficiently large \(n\); each fixed summand divided by \(n^2\) tends to \((1-\alpha h)_+^2\). The denominator satisfies \(N_n/n^3\to1/3\). Therefore \(nT_n(t_n)/N_n\to3\sum_{h\ge1}(1-\alpha h)_+^2\). At integer endpoints \(\alpha h=1\), that term tends to zero, as required.

## Verification
Run `python3 verify.py`. It constructs the actual sparse partial maps for \(2\le n\le12\), computes repeated composition until zero rather than using the closed index formula, and compares the entire index spectrum and every tail count against the exact formulas. It separately verifies the exact divisor-sum mean at the same small sizes, evaluates it for \(n=100,1000,10000\), and checks numerical convergence of the second moment. The final output is `VERIFY_OK` when every comparison passes. These finite checks are not substitutes for the unrestricted proofs above.

## Relationship to prior work
Fikioris and Fikioris [1] defined and classified this consecutive-diagonal inverse monoid, obtained its total order and its nilpotent and idempotent totals, and gave the nilpotency index of each individual element. Those results supply the starting structure and must not be described as new. Their subsequent paper [2] studies a **real-parameter** enlargement and extends the elementwise index formula; its uncountable model has no uniform finite-element sampling measure of the present kind.

The additional results here are the **whole finite index distribution**, its harmonic limiting law, the exact divisor-weighted expectation with its sharp constant, the linear second-moment growth, and the rare macroscopic-tail profile. They concern probabilistic structure rather than elementwise computability or the mere number of nilpotents. The argument also distinguishes ordinary rank from the minimal vanishing power. Searches did not establish equivalent statements in the inspected primary literature, but this does not certify global priority.

## Limitations
The theorem is restricted to integer-parameter consecutive-diagonal block partial injections; it is not a theorem for the full rook monoid, arbitrary distance-preserving partial maps, or the continuous-parameter enlargement. The empty matrix is excluded from the sampling distribution. The limit law is only a pointwise distributional statement (with a uniform tail approximation), not convergence of expectations: indeed the expectations diverge. The second-moment assertion gives its leading coefficient, not a lower-order expansion. Publication-priority verification is incomplete and independent mathematical validation has not been performed.

## References
[1] George Fikioris and Giannis Fikioris, *A subsemigroup of the rook monoid*, arXiv:2111.01863, first publicly available 2021-11-02, https://arxiv.org/abs/2111.01863 . See §4, Theorem 4; §6, Propositions 7 and 9.

[2] George Fikioris and Giannis Fikioris, *An extension to “A subsemigroup of the rook monoid”*, arXiv:2302.09496, first publicly available 2023-02-19, https://arxiv.org/abs/2302.09496 . See §3, Proposition 3 and Remark 5. Published in *Semigroup Forum* 107 (2023), 637–650, DOI 10.1007/s00233-023-10393-8.
