# A second-order coprimality bias in consecutive-LCM least periods

## Finding

For every integer \(k\ge1\), define
\[
g_k(n)=\frac{\prod_{j=0}^{k}(n+j)}{\operatorname{lcm}(n,n+1,\ldots,n+k)},\qquad n\ge1,
\]
and write \(P_k\) for its least positive period and \(L_k=\operatorname{lcm}(1,\ldots,k)\). For real \(X\ge3\) and fixed integer \(q\ge2\), set
\[
E(X)=\#\{1\le k\le X:P_k<L_k\},\qquad
E_q(X)=\#\{1\le k\le X:P_k<L_k,\ \gcd(k+1,q)=1\}.
\]
Then, as \(X\to\infty\),
\[
\boxed{E_q(X)-\frac{\varphi(q)}q E(X)
=C_q\frac{X}{\log X}+O_q\!\left(\frac{X}{(\log X)^2}\right),}
\]
where the *explicit* constant is
\[
\boxed{C_q=\frac{\varphi(q)}q\sum_{p\mid q}\frac{\log p}{p-1}
-\left(1-\frac{\varphi(q)}q\right).}
\]
The sum is over distinct primes dividing \(q\). In particular, \(C_2=(\log2-1)/2<0\), whereas \(C_3=(\log3-1)/3>0\): a genuine **sign reversal** occurs even though both classes have their expected leading share. The unconditioned count satisfies \(E(X)=(\log 2)X+O(X/\log X)\).

## Assumptions and scope

All integers, primes, periods, least common multiples, and gcds are positive. The modulus \(q\ge2\) is fixed before \(X\to\infty\); the implied constant may depend on \(q\). Natural logarithms are used. The theorem is an asymptotic *in the window parameter* \(k\), not an asymptotic in the argument \(n\) of \(g_k\). No claim of uniformity for growing \(q\), of a full asymptotic series, or of a sharp error term is made.

## Proof

**1. Prime-power defect criterion.** The Farhi--Kane exact-period theorem [1, Theorem 3.2] states that if \(e_p(k)=\lfloor\log_p k\rfloor\) for primes \(p\le k\), then
\[
\frac{L_k}{P_k}=\prod_{\substack{p\le k\\ \nu_p(k+1)\ge e_p(k)}}p^{e_p(k)},
\]
and at most one prime contributes [1, Proposition 3.3]. This is an earlier theorem, used here as an input, not asserted as a new contribution. Put \(N=k+1\). If the contributing exponent \(e_p(k)\) is one, necessarily \(N=mp\) for an integer \(2\le m\le p\). Conversely any such pair gives \(e_p(k)=1\) and a missing factor \(p\), since \(p\le mp-1<p^2\). Thus the exponent-one exceptional family has the exact count
\[
A(Y)=\sum_{2\le m\le\sqrt Y}\bigl(\pi(Y/m)-\pi(m-1)\bigr)
\]
for \(N\le Y\). The representation is unique (a composite integer has at most one prime divisor at least its square root, with equality only for a prime square).

**2. Higher-prime-power exceptional family is negligible at the required scale.** If a missing factor has \(e_p(k)=a\ge2\), then \(N=mp^a\) with \(2\le m\le p\). Its count for \(N\le Y\) is at most
\[
\sum_{a=2}^{\lfloor\log_2Y\rfloor}\ \sum_{p^a\le Y}
\min\{p,Y/p^a\}.
\]
Splitting at \(p=Y^{1/(a+1)}\), bounding primes by all integers, and summing the two tails gives \(O(Y^{2/(a+1)})\) for each \(a\ge2\). Hence the entire higher-power contribution is
\[
O(Y^{2/3}\log Y)=O\!\left(Y/(\log Y)^2\right).
\]
The equality in the last big-O is an eventual upper bound. No uniqueness of additional prime powers is needed for this estimate.

**3. The weighted count.** Define the periodic weight
\[
w_q(m)={\mathbf{1}}_{\gcd(m,q)=1}-\frac{\varphi(q)}q.
\]
Its mean on any complete period of length \(q\) is zero, so all partial sums \(\sum_{m\le t}w_q(m)\) are \(O(q)\). Except for finitely many exponent-one pairs with \(p\mid q\), a prime \(p\ge m\) is coprime to \(q\). Therefore \(\gcd(mp,q)=1\) is equivalent to \(\gcd(m,q)=1\). By steps 1--2 and the harmless reindexing \(N=k+1\),
\[
E_q(X)-\frac{\varphi(q)}q E(X)
=\sum_{2\le m\le\sqrt X}w_q(m)
\{\pi(X/m)-\pi(m-1)\}
+O_q(X^{2/3}\log X+1).
\]
Because \(w_q\) has bounded partial sums and \(\pi(m-1)\) increases with \(m\), the sum of the \(\pi(m-1)\) terms is \(O_q(\sqrt X)\).

**4. The sharp first correction.** For \(\sqrt X\le t\le X\), the classical prime-number theorem with its standard zero-free-region error gives
\[
\pi(t)=\operatorname{Li}(t)+O\left(t e^{-c\sqrt{\log t}}\right)
\]
for some absolute \(c>0\). Summing the errors over \(m\le\sqrt X\) contributes \(O_A(X/(\log X)^A)\) for each fixed \(A>0\). Set \(R(t)=\operatorname{Li}(t)-t/\log t\). The derivative \(R'(t)=1/(\log t)^2\) is positive and \(R(t)=O(t/(\log t)^2)\), so summation by parts against the bounded partial sums of \(w_q\) yields
\[
\sum_{2\le m\le\sqrt X} w_q(m)R(X/m)
=O_q(X/(\log X)^2).
\]
For the remaining terms use
\[
\frac1{\log X-\log m}=\frac1{\log X}
+\frac{\log m}{\log X(\log X-\log m)}.
\]
On \(2\le m\le\sqrt X\), the function
\(m\mapsto \log m/[m(\log X-\log m)]\) has supremum and total variation \(O(1/\log X)\). Another summation by parts gives
\[
\sum_{2\le m\le\sqrt X}w_q(m)\pi(X/m)
=\frac X{\log X}\sum_{2\le m\le\sqrt X}\frac{w_q(m)}m
+O_q(X/(\log X)^2).
\]
The periodic zero-mean weight ensures that its harmonic series converges and its truncated tail is \(O_q(X^{-1/2})\). Its value is explicitly
\[
\sum_{m=2}^{\infty}\frac{w_q(m)}m
=-\sum_{d\mid q}\frac{\mu(d)\log d}{d}-w_q(1)
=\frac{\varphi(q)}q\sum_{p\mid q}\frac{\log p}{p-1}
-\left(1-\frac{\varphi(q)}q\right).
\]
The first equality follows by inclusion-exclusion in \(\sum_{m\le T}({\mathbf{1}}_{(m,q)=1}-\varphi(q)/q)/m\), using \(H_{\lfloor T/d\rfloor}=\log T-\log d+\gamma+o(1)\). Combining these identities with step 3 proves the displayed bias formula.

**5. Leading count for context.** In step 1, the prime number theorem uniformly for \(X/m\ge\sqrt X\) gives
\[
A(X)=X\sum_{2\le m\le\sqrt X}\frac1{m\log(X/m)}
+O(X/\log X).
\]
An integral comparison gives \(\sum_{2\le m\le\sqrt X}1/[m\log(X/m)]=\log2+O(1/\log X)\). The subtracted \(\pi(m-1)\) terms and the higher-power layer are within \(O(X/\log X)\). Thus \(E(X)=(\log2)X+O(X/\log X)\). This leading law is related to the classical large-prime-factor/Dickman calculation; the new statement is the signed second-order coprimality bias.

## Verification

The independent finite diagnostic `verify.py` computes the exact least period of \(g_k\) directly for each \(1\le k\le8\) and compares it with the prime-power period formula. It also evaluates the complete defect test for \(1\le k\le12000\), checks that every qualifying large-prime-factor case has the predicted defect, and reports six fixed-modulus bias estimates. Run `python3 verify.py` from this directory. The observed check result was `FARHI_LOCAL_BIAS_FINITE_CHECK_OK 8 12000 6`. These finite checks cannot prove the prime-number-theorem step or any infinite asymptotic.

## Relationship to prior work

Farhi and Kane [1] determined the exact least periods at each fixed window length; their formula is the indispensable arithmetic input. Hong and Qian [2] extended least-period questions to arithmetic progressions. Huang and Yang [3] recently generalized the period problem to nonvanishing multiplicative functions and recovered the ordinary consecutive-integer case. The primary texts studied concern the exact period at fixed parameters and do not give this modulus-uniform-in-the-fixed-modulus sense, signed \(X/\log X\) frequency bias as the window length varies. Classical smooth-number and prime-factor-distribution theory [4] supplies the leading constant \(\log2\) and closely related analytic tools, but the present statement isolates a finer coprimality-dependent correction, including a change of sign between moduli two and three. Related arithmetic-progression smooth-number literature [5] concerns distribution of friable integers in residue classes under different cutoff regimes; a broad unindexed result may imply a variant of the correction, which remains a literature-priority risk.

## Limitations

The proof relies on the published Farhi--Kane least-period theorem and the effective prime number theorem. It is not a new proof of either input. The coefficient \(C_q\) can have either sign and is not asserted to be nonzero for every modulus. Error estimates are for fixed \(q\) and are not claimed sharp. The baseline \(E(X)\sim X\log2\) is classical in spirit; the claimed contribution is specifically the prime-local second-order bias in least-period defects. Formal or independent expert verification has not been performed.

## References

[1] B. Farhi and D. Kane, *New results on the least common multiple of consecutive integers*, Proceedings of the American Mathematical Society 137 (2009), 1933--1939, Theorem 3.2 and Proposition 3.3. https://arxiv.org/abs/0808.1507 ; full text: https://cseweb.ucsd.edu/~dakane/lcm.pdf

[2] S. Hong and G. Qian, *The least common multiple of consecutive arithmetic progression terms*, Proceedings of the Edinburgh Mathematical Society 54 (2011), 431--441. https://arxiv.org/abs/0903.0530

[3] W.-J. Huang and Q.-H. Yang, *On least periods of a class of arithmetic functions*, arXiv:2611.15379v1, first posted November 11, 2026. https://arxiv.org/abs/2611.15379

[4] A. Granville, *Smooth numbers: computational number theory and beyond*, in Algorithmic Number Theory (2008), discussion of the Dickman function and its first interval. https://math.utoledo.edu/~codenth/Spring_13/3200/NT-books/Smooth_Numbers-Computational_Number_Theory_and_Beyond-Granville.pdf

[5] *Smooth numbers in arithmetic progressions to large moduli*, Compositio Mathematica, https://www.cambridge.org/core/journals/compositio-mathematica/article/smooth-numbers-in-arithmetic-progressions-to-large-moduli/D8E4EE07BDAA6D41CCD8C5455D81CD7A
