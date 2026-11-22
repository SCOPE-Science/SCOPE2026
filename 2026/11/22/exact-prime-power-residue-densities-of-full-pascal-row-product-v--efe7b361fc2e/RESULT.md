# Exact prime-power residue densities of full Pascal-row product valuations

## Finding

Write
\[
B_n=\prod_{j=0}^{n}\binom{n}{j},\qquad W_p(n)=\nu_p(B_n)
\quad(n\ge0).
\]
For **every** prime \(p\), integer \(k\ge1\), and residue \(0\le b<p^k\), the natural density of indices with \(W_p(n)\equiv b\pmod{p^k}\) exists and equals
\[
\mu_{p,k}(b)=
\begin{cases}
\dfrac{k(p-1)+p}{p^{k+1}},&b=0,\\[4pt]
\dfrac{(p-1)(\nu_p(b)+1)}{p^{k+1}},&1\le b<p^k.
\end{cases} \tag{1}
\]
For some \(\delta_{p,k}>0\), the count through \(N\) is \(\mu_{p,k}(b)N+O_{p,k}(N^{1-\delta_{p,k}})\), uniformly in the finitely many residues \(b\).

In particular, conditional on \(\nu_p(n+1)=j<k\), the residues of \(W_p(n)\) become **uniform on the multiples of \(p^j\)** modulo \(p^k\); if \(p^k\mid n+1\), then \(W_p(n)\equiv0\pmod{p^k}\).

A sharp exact compression underlies (1). For \(s_p(t)\) the base-\(p\) digit sum, \(L\ge k\), \(0\le a<p^L\), and \(t\ge0\),
\[
W_p(a+p^L t)\equiv W_p(a)+(a+1)(p-1)^{-1}s_p(t)\pmod{p^k}. \tag{2}
\]
The inverse \((p-1)^{-1}\) in (2) is taken modulo \(p^k\). The threshold \(L=k\) is best possible **uniformly**: for every \(L<k\) there are permissible \(a,t\) violating (2) with that smaller \(L\).

For \(r\ge k\), let \(c_{p,m}(h)=[X^h](1+X+\cdots+X^{p-1})^m\). There is also the following **exact**, non-asymptotic histogram, for every \(b\bmod p^k\):
\[
\begin{aligned}
H_{p,k,r}(b)
&=\#\{0\le n<p^r: W_p(n)\equiv b\pmod{p^k}\}\\
&=\sum_{a=0}^{p^k-1}
\sum_{h=0}^{(p-1)(r-k)}
c_{p,r-k}(h)\,
\mathbf 1\!\left[
W_p(a)+(a+1)(p-1)^{-1}h\equiv b\pmod{p^k}
\right]. \tag{3}
\end{aligned}
\]
For the first layer, (3) simplifies for every \(r\ge2\): \(H_{p,1,r}(0)=(2p-1)p^{r-2}\) and \(H_{p,1,r}(b)=(p-1)p^{r-2}\) for \(1\le b<p\). For instance the four densities modulo four at \(p=2\) are \((1/2,1/8,1/4,1/8)\), in residue order \((0,1,2,3)\).

## Assumptions and scope

The prime \(p\) is arbitrary, including \(2\); \(k,r,L\) are integers, with the inequalities stated above, and indices \(n,a,t\) are nonnegative integers. The convention is \(B_0=1\) and \(s_p(0)=0\). Densities mean natural, rather than merely prime-power-block, densities. The formula (1) evaluates \(\nu_p(b)\) only for \(b\ge1\), avoiding an undefined finite exponent at zero.

## Proof

**1. Pointwise base formula.** Put \(S_p(n)=\sum_{0\le j<n}s_p(j)\). The factorial valuation formula gives \(\nu_p\binom nj=(s_p(j)+s_p(n-j)-s_p(n))/(p-1)\), hence
\[
W_p(n)=\frac{2S_p(n)-(n-1)s_p(n)}{p-1}.\tag{4}
\]
This classical identity is Theorem 5.1 of Lagarias–Mehta [1], and is *not* claimed as new.

**2. Exact digit splitting.** Let \(M=p^L\) with \(L\ge1\) and \(0\le a<M\). Partition the integers smaller than \(a+Mt\) into \(t\) complete blocks of length \(M\) and one incomplete block. Digit independence yields
\[
S_p(a+Mt)=tS_p(M)+MS_p(t)+S_p(a)+a\,s_p(t),
\quad s_p(a+Mt)=s_p(a)+s_p(t),
\]
and \(S_p(M)=LM(p-1)/2\). Substitution into (4) yields the **exact integer equality**
\[
\begin{aligned}
W_p(a+p^L t)-W_p(a)
={}&\frac{a+1}{p-1}s_p(t)\\
&+\frac{p^L}{p-1}\Big(2S_p(t)+L(p-1)t-t s_p(a)-t s_p(t)\Big).
\end{aligned}\tag{5}
\]
Fractions here are rational notation for a combined integer; for modular reduction, \(p-1\) is invertible modulo \(p^k\). If \(L\ge k\) the last term vanishes modulo \(p^k\), giving (2).

**3. A forced divisibility stratum.** Kummer's theorem, summed over all \(0\le j\le n\), gives the alternative exact carry count
\[
W_p(n)=\sum_{h\ge1}\left\lfloor\frac{n}{p^h}\right\rfloor
\left(p^h-1-(n\bmod p^h)\right).\tag{6}
\]
Only finitely many terms are nonzero. Indeed, at digit length \(p^h\), each of the \(\lfloor n/p^h\rfloor\) completed blocks contributes exactly \(p^h-1-(n\bmod p^h)\) indices whose subtraction from \(n\) requires a borrow at that digit. If \(p^j\mid n+1\), then for \(h\le j\) each parenthesis is zero, while for \(h>j\) it is divisible by \(p^j\). Consequently
\[
p^j\mid n+1\quad\Longrightarrow\quad p^j\mid W_p(n).\tag{7}
\]
In particular, \(W_p(p^k-1)=0\) (also immediate by Lucas's theorem).

**4. Uniformity of digit sums on all long intervals.** For any integer \(d=p^e\ge p\) and nontrivial \(d\)-th root of unity \(\zeta\), put \(\Phi_p(\zeta)=1+\zeta+\cdots+\zeta^{p-1}\). Each \(|\Phi_p(\zeta)|<p\). Over a complete interval \(0\le t<p^m\), the character sum is \(\Phi_p(\zeta)^m\). More generally, a prefix \(0\le t<T\) decomposes into at most \(p-1\) aligned blocks of each length \(p^i\); digit additivity on an aligned block shows its character sum has absolute value \(|\Phi_p(\zeta)|^i\). Therefore, for some \(\delta_{p,e}>0\), the nontrivial character sums are \(O_{p,e}(T^{1-\delta_{p,e}})\). Fourier inversion proves that \(s_p(t)\bmod p^e\) is equidistributed with a power-saving error. This argument handles every real cutoff \(T\), not only powers of \(p\).

**5. Conditional distributions and (1).** Fix \(k\) and choose the unique decomposition \(n=a+p^k t\) with \(0\le a<p^k\). Write \(j=\nu_p(a+1)\), where \(0\le j\le k\). If \(j=k\), then \(a=p^k-1\), and (2),(7) make the output identically zero modulo \(p^k\). If \(j<k\), (7) shows \(W_p(a)\) is a multiple of \(p^j\), and \((a+1)(p-1)^{-1}\) has valuation exactly \(j\) modulo \(p^k\). By step 4, (2) therefore distributes \(W_p(a+p^k t)\) uniformly over the \(p^{k-j}\) multiples of \(p^j\) modulo \(p^k\).

There are exactly \((p-1)p^{k-j-1}\) low-digit values \(a\) with \(j<k\). For each residue divisible by \(p^j\), their **combined** density is
\[
\frac{(p-1)p^{k-j-1}}{p^k\,p^{k-j}}=\frac{p-1}{p^{k+1}}.
\]
The lone class \(j=k\) contributes an additional mass \(1/p^k\) to zero. Thus a nonzero residue of valuation \(v<k\) gets the contributions \(j=0,\ldots,v\); zero gets \(j=0,\ldots,k\). This proves (1), including its power-saving error.

**6. Exact finite counts.** In (2) take \(L=k\) and restrict \(t<p^{r-k}\). The number of such \(t\) with digit sum \(h\) is the coefficient \(c_{p,r-k}(h)\), proving (3). For \(k=1\) and \(r\ge2\), the digit sums modulo \(p\) are already exactly uniform in a complete block, which gives the stated simple counts.

**7. Sharpness of \(L=k\).** Suppose \(L=k-1\ge1\). In (5), put \(a=0\) and let \(D_L(t)=2S_p(t)+L(p-1)t-t s_p(t)\). If \(t=1\), then \(D_L(1)=L(p-1)-1\equiv-(L+1)\pmod p\). If this vanishes, take \(t=p+1\): because \(s_p(p+1)=2\) and \(S_p(p+1)=p(p-1)/2+1\), we have \(D_L(p+1)\equiv-L\pmod p\), which is nonzero when \(L+1\equiv0\pmod p\). For one of these two choices the omitted term in (5) has exact \(p\)-valuation \(L\), violating the putative congruence modulo \(p^{L+1}\). For \(k=1\), the smaller choice \(L=0\), \(a=0,t=1\), also fails: \(W_p(1)=0\) whereas \((p-1)^{-1}s_p(1)\not\equiv0\pmod p\). Any \(L<k-1\) is excluded by the same argument at modulus \(p^{L+1}\), which is a quotient of \(p^k\). This establishes optimality.

## Verification

The accompanying `check.py` is a standalone Python 3 exact-arithmetic checker. Run `python check.py`; it verifies the pointwise digit formula against independently accumulated factorial valuations, Kummer carry counts, and small literal row products; checks digit splitting at multiple moduli, sharpness witnesses and every residue in exact finite histograms for several primes and depths; and verifies the finite probability masses. It does **not** prove natural density or equidistribution: those are established in steps 4–5 above. The preceding proof treats all primes, depths and unbounded indices, whereas finite tests cover only the explicitly coded ranges.

## Relationship to prior work

Lagarias and Mehta [1] establish the object, its original source date, and the exact digit-sum identity (4) for its prime valuations. Their Theorem 5.1 already determines each individual valuation. **Neither that pointwise formula nor the tabulated values in [3,4] are claimed as new here.** The additional result is the uniform all-prime, all-precision *natural-density theorem* (1), the residue-by-residue conditional law, the exact finite-block histogram (3), and the optimal low-digit compression theorem (2), proved by a new digit-block decomposition and a Fourier power-saving argument. The more general reduced Farey products in [2] are related by Möbius inversion but are different objects; their residue statistics do not supply (1). The identified nearby work on fixed Pascal columns and binomial valuation vectors concerns different functions of \(n\).

The new result is a nontrivial consequence of the previously known exact evaluation; it is **not independent of** that evaluation. It remains possible that an earlier digit-automaton, modular-distribution, or OEIS discussion implicitly established an equivalent density law. The source checks below cannot establish exhaustive historical priority.

## Limitations

The theorem concerns the valuations of **complete** row products, not the products themselves modulo prime powers, nor reduced Farey products, nor simultaneous correlations between different primes. Its error constants depend on the fixed prime and precision; no uniform estimate as these parameters grow is asserted. No computational test is an infinite proof. The reviewed argument has not undergone independent mathematical validation, and an earlier equivalent formulation outside the inspected material remains possible.

## References

1. J. C. Lagarias and H. Mehta, *Products of Binomial Coefficients and Unreduced Farey Fractions*, arXiv:1409.4145, first publicly posted September 15, 2014, Theorem 5.1 and Section 6, https://arxiv.org/abs/1409.4145.
2. J. C. Lagarias and H. Mehta, *Products of Farey Fractions*, arXiv:1503.00199, first publicly posted March 1, 2015, Sections 1–2, https://arxiv.org/abs/1503.00199.
3. OEIS A001142, complete Pascal-row binomial products, https://oeis.org/A001142.
4. OEIS A187059, binary valuation sequence of those products, https://oeis.org/A187059.
