# Liouville sign-balance phase diagram for arbitrary-stride LCM windows

## Finding
For integers \(k,c\ge1\) and \(n\ge1\), define
\[
G_{k,c}(n)=\frac{\prod_{i=0}^{k}(n+ic)}{\operatorname{lcm}(n,n+c,\ldots,n+kc)},\qquad
S_{k,c}(n)=\lambda(G_{k,c}(n)),
\]
where \(\lambda(m)=(-1)^{\Omega(m)}\) is the Liouville function and \(\Omega\) counts prime factors with multiplicity. Set \(e=\nu_2(c)\). The natural densities of \(S_{k,c}=+1\) and \(S_{k,c}=-1\) are equal **if and only if** one of the following disjoint conditions holds:
\[
\boxed{\begin{array}{ll}
e=0 &: k+1=3\cdot2^r \quad(r\ge0);\\
e=1 &: k+1=2^{2r+1}\quad(r\ge0);\\
e=2 &: k+1=2^{2r+2}\quad(r\ge0).
\end{array}}
\]
For \(e\ge3\), sign balance never occurs. In every balanced case each sign has density \(1/2\); outside these cases the two natural densities exist and differ. In particular, every odd stride has the same balance criterion as stride one, while strides divisible by exactly two or exactly four create two new, mutually exclusive power-of-two window families.

## Assumptions and scope
All indices \(n\), window parameters \(k\), and strides \(c\) are positive integers. The quotient \(G_{k,c}(n)\) is a positive integer because an LCM divides the product. Density means the limit of the proportion among \(1\le n\le X\) as integer \(X\to\infty\). The theorem concerns **all starting integers** \(n\) for a fixed stride \(c\); it does not restrict \(\gcd(n,c)=1\). Write \(L_k=\operatorname{lcm}(1,\ldots,k)\), with \(L_1=1\), and \(\nu_p\) for the usual nonnegative prime valuation. A claimed period below is not asserted to be least.

## Proof
**1. Finite prime-local periodic model.** For each prime \(p\) set
\[
E_p(n)=\sum_{i=0}^k\nu_p(n+ic)-\max_{0\le i\le k}\nu_p(n+ic),\quad S_p(n)=(-1)^{E_p(n)}.
\]
Then \(S_{k,c}(n)=\prod_pS_p(n)\). If \(p\nmid cL_k\), then \(p>k\) and \(p\nmid c\); two different window terms cannot both be divisible by \(p\), because their difference is \((i-j)c\) with \(0<|i-j|\le k<p\). Hence \(E_p(n)=0\) for every \(n\).

For \(p\mid cL_k\), put \(a=\nu_p(c)\), \(h=\max\{j\ge0:p^j\le k\}\), and \(J=a+h\). The difference between two distinct terms has valuation at most \(J\). Consequently, for any \(j>J\) at most one term is divisible by \(p^j\), and
\[
E_p(n)=\sum_{j=1}^{J}\left(N_{p,j}(n)-\mathbf1_{N_{p,j}(n)>0}\right),\quad
N_{p,j}(n)=\#\{0\le i\le k:p^j\mid n+ic\}.
\]
Each summand depends only on \(n\bmod p^j\). Thus \(S_p\) has period dividing \(p^J\). The product has period dividing \(\prod_{p\mid cL_k}p^{\nu_p(c)+\nu_p(L_k)}=cL_k\), and its natural signed mean is the Chinese-remainder product of the local signed means \(M_p\). For odd \(p\), the local period has odd cardinality \(p^J\); a sum of an odd number of signs in \(\{\pm1\}\) cannot vanish. Therefore **the full signed mean vanishes exactly when its binary local mean vanishes**.

**2. Binary means for consecutive windows.** Let \(m_t\) be the binary local mean when the window contains \(t\ge1\) consecutive integers (stride one). It is a rational number in \([-1,1]\). The initial values are \(m_1=m_2=1\). For \(u\ge1\), separate the even terms of each window. A block of \(2u\) terms has exactly \(u\) even terms, and a block of \(2u+1\) terms has \(u+1\) or \(u\), according to the parity of the first term. Removing the common factor two from those even terms contributes respectively \(u-1\), \(u\), or \(u-1\) to the quotient valuation. Uniform averaging therefore gives
\[
 m_{2u}=(-1)^{u-1}m_u,\qquad
 m_{2u+1}=\frac{(-1)^u}{2}(m_{u+1}-m_u). \tag{1}
\]
For every \(u\ge2\), the pair \((m_u,m_{u+1})\) admits a common power-of-two denominator with numerators of opposite parity. This is true for the bases \((m_2,m_3)=(1,0)\) and \((m_3,m_4)=(0,-1)\). If \((m_u,m_{u+1})=(A,B)/2^d\) has the property, equation (1) gives the child pairs
\[
(m_{2u},m_{2u+1})=\frac{(-1)^{u-1}}{2^{d+1}}(2A,A-B),
\]
\[
(m_{2u+1},m_{2u+2})=\frac{(-1)^{u-1}}{2^{d+1}}(A-B,-2B).
\]
In both pairs one numerator is odd and the other even, establishing the induction. Hence \(m_{u+1}\ne m_u\) for every \(u\ge2\). By (1), the only **odd** index \(t\ge3\) with \(m_t=0\) is \(t=3\), coming from \(m_1=m_2\); the even-index recurrence propagates this precisely to
\[
 m_t=0\quad\Longleftrightarrow\quad t=3\cdot2^r\ (r\ge0). \tag{2}
\]
Moreover, \(|m_t|=1\) exactly when \(t\) is a power of two. Indeed, this holds at \(t=1,2\), and passes unchanged in absolute value from \(u\) to \(2u\). For odd \(t=2u+1\ge3\), equation (1) could have absolute value one only if \(m_u,m_{u+1}\) were opposite unit signs, which their opposite-parity common numerators exclude for \(u\ge2\), while \(m_3=0\). Iterating the even recurrence also gives
\[
 m_{2^r}=(-1)^{r-1}\qquad(r\ge1). \tag{3}
\]

**3. Arbitrary strides.** Write \(c=2^e v\), where \(v\) is odd. If \(0\le j<e\) and \(\nu_2(n)=j\), all \(k+1\) window terms have valuation \(j\), so the binary sign is \((-1)^{kj}\). This event has density \(2^{-j-1}\). If \(2^e\mid n\), factoring \(2^e\) from all terms contributes \(ke\) to the quotient valuation. As \(n/2^e\) runs through residues, the remaining odd stride \(v\) gives the same binary local mean as consecutive integers, since multiplication by an odd unit permutes the relevant residue classes. Thus the binary mean at \(e=\nu_2(c)\) is exactly
\[
 M_2(k,e)=\sum_{j=0}^{e-1}2^{-j-1}(-1)^{kj}+2^{-e}(-1)^{ke}m_{k+1}. \tag{4}
\]
For \(e=0\), this is \(m_{k+1}\); equation (2) yields the first family. If \(k\) is even and \(e\ge1\), equation (4) becomes \(1-2^{-e}+2^{-e}m_{k+1}\). Since \(k+1\) is odd and at least three, step 2 implies \(|m_{k+1}|<1\), so the expression is strictly positive.

If \(k\) is odd and \(e\ge1\), summing the geometric series in (4) gives
\[
 M_2(k,e)=\frac{1-(-1/2)^e}{3}+(-1/2)^e m_{k+1}. \tag{5}
\]
This is zero precisely when \(m_{k+1}=(1-(-2)^e)/3\). For \(e\ge3\), the right side has absolute value greater than one, impossible. For \(e=1\) it is \(1\), which by (3) occurs precisely at \(k+1=2^{2r+1}\). For \(e=2\) it is \(-1\), which occurs precisely at \(k+1=2^{2r+2}\). This exhausts all cases. Finally, since the global signed mean is \(\Pr(S_{k,c}=+1)-\Pr(S_{k,c}=-1)\), it vanishes exactly when both densities are \(1/2\). ∎

## Verification
The standalone Python 3 checker `verify_liouville_stride.py` uses only the standard library. It separately computes the recurrence (1), the mixture (4), and the three-case zero criterion across \(1\le k<2000\), \(0\le e\le7\). It independently enumerates binary local signs for \(1\le k<75\), \(0\le e\le4\), and odd stride multipliers \(1,3,5\). Finally, for \(1\le k\le8\), \(1\le c\le12\), it constructs the actual integer product/LCM quotient over a complete explicit period, computes its Liouville sign by integer factorization, compares independently obtained prime-local products, and verifies global CRT mean factorization and the theorem's zero criterion. The result is `LIOUVILLE_STRIDE_BALANCE_EXACT_CHECK_OK 128834`. These finite checks are supporting diagnostics; the proof establishes all positive integer parameters.

## Relationship to prior work
Huang and Yang, *On least periods of a class of arithmetic functions* (arXiv:2611.15379v1, submitted 2026-11-11), establish least-period formulas for quotients of products of multiplicative-function values over arithmetic progressions. In particular, their Theorem 1.1 concerns periods, **not the natural-density sign-balance zero set**; its prime-local framework motivates this question. Hong and Qian's arXiv:0903.0530v3 studies the periodicity and exact least period of the ordinary positive-integer product/LCM quotient on fixed arithmetic progressions, not its Liouville sign distribution.

A published exact value-frequency theorem for a **fixed arithmetic progression**, identified by the published-finding corpus record `2026/10/26/SCOPE-exact-value-frequency-law-for-consecutive-arithmetic-progression--8e35eb7b4fbc`, provides the full valuation histogram when the starting terms remain in one prescribed progression class. Such a formula can be used as an ingredient for conditional densities but does not state this all-starting-integers classification as the stride varies: varying \(n\) freely also mixes classes with \(\gcd(n,c)>1\), adding the exceptional binary factors in (4). A previously reported consecutive-stride Liouville classification gives the \(e=0\) branch; the \(e=1\) and \(e=2\) families and the universal exclusion at \(e\ge3\) are the present parameter classification. No claim is made to a new period or to rediscovery of known valuation identities.

## Limitations
The result classifies equality of sign densities, not their full rational values in unbalanced cases or their exact least periods. It assumes positive integral strides, positive starting indices, and fixed window lengths as the starting index tends to infinity. Finite tests do not prove infinite cases. Although the relevant period, fixed-progression frequency, and consecutive-stride results were compared, an unindexed equivalent uniform stride-zero-set theorem remains possible; independent validation and exhaustive publication-priority verification are not claimed.

## References
- W.-J. Huang and Q.-H. Yang, *On least periods of a class of arithmetic functions*, arXiv:2611.15379v1, first submitted 2026-11-11, https://arxiv.org/abs/2611.15379.
- S. Hong and G. Qian, *The least common multiple of consecutive arithmetic progression terms*, arXiv:0903.0530v1 (2009-03-03), full text v3 (2010-02-18), https://arxiv.org/html/0903.0530v3.
- B. Farhi and D. Kane, *New results on the least common multiple of consecutive integers*, arXiv:0808.1507v1 (2008-08-11), https://arxiv.org/html/0808.1507v1.
- *Exact value-frequency law for consecutive arithmetic-progression LCM quotients*, publicly accessible RESULT.md at https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-exact-value-frequency-law-for-consecutive-arithmetic-progression--8e35eb7b4fbc/RESULT.md (2026-10-26).
