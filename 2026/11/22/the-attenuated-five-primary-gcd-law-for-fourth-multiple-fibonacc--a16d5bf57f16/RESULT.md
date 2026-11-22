# The attenuated five-primary gcd law for fourth-multiple Fibonacci power windows

## Finding
Let \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\) for all \(n\ge0\). For every positive exponent \(d\) divisible by \(4\) and every window length \(k\ge1\), define
\[
W_{d,k}(n)=\sum_{j=0}^{k-1}F_{n+j}^{d},\qquad C_d(k)=\gcd_{n\ge0}W_{d,k}(n).
\]
Then, for all such \(d,k\),
\[
\boxed{\nu_5(C_d(k))=\max\{0,\nu_5(k)-1\}.}
\]
More strongly, for all \(d\ge4\) with \(4\mid d\), \(r\ge1\), and \(n\ge0\),
\[
\boxed{\sum_{j=0}^{5^r-1}F_{n+j}^{d}\equiv-5^{r-1}\pmod{5^r}.}
\]
Thus, whenever \(k=5^r u\) with \(r\ge1\) and \(5\nmid u\), **every** length-\(k\) window has valuation exactly \(r-1\), not merely the common gcd. In particular, five first enters the gcd at window length \(25\), and its exponent thereafter is one less than the exponent of five in the length.

## Assumptions and scope
The Fibonacci sequence has its standard integer initial conditions; \(n\) ranges over all nonnegative integers, \(k\) over all positive integers, and \(d\) over all positive multiples of four. Each window contains precisely \(k\) successive powers. The gcd of these nonnegative integer windows is positive because at least one window is positive. We use \(\nu_5(N)\) for the exponent of \(5\) in a positive integer \(N\), with \(\nu_5(k)=0\) when \(5\nmid k\). No formula for the other prime factors of \(C_d(k)\) is asserted. A linear recurrence, described below, shows that the infinite gcd is in fact the gcd of the first \(d+1\) windows.

## Proof
**1. The five-step scalar identity.** Write the Fibonacci state as \(v_n=(F_n,F_{n+1})^T\), so that \(v_{n+1}=A v_n\) for
\[
A=\begin{pmatrix}0&1\\1&1\end{pmatrix},\qquad A^5=\begin{pmatrix}3&5\\5&8\end{pmatrix}\equiv3I\pmod5.
\]
For fixed \(d\), take the integral column \(M_d(v)=(x^d,x^{d-1}y,\ldots,y^d)^T\) of homogeneous monomials of \(v=(x,y)^T\). Substituting \(Av\) gives an integer matrix \(B_d\) of size \(d+1\) such that \(M_d(Av)=B_dM_d(v)\). Functoriality under composition gives
\[
B_d^5\equiv3^d I\equiv I\pmod5,
\]
since the substitution matrix of \(A^5\) is \(B_d^5\) and \(4\mid d\). This identity takes place in the full integer matrix ring and uses no diagonalization or division by five. Thus \(f_d(n)=F_n^d\), the first coordinate of \(B_d^nM_d(v_0)\), is an integral linear-recurrence sequence of order at most \(d+1\). By Cayley–Hamilton, any sequence of its shifted window sums satisfies the same monic recurrence. Hence the first \(d+1\) windows suffice to determine their positive gcd, although the proof below does not need that reduction.

**2. Five-power lifting of the shift operator.** The elementary binomial expansion of \((I+5^tD)^5\) shows that for every integer matrix \(D\) and \(t\ge1\),
\[
(I+5^tD)^5\equiv I\pmod{5^{t+1}}.
\]
Starting with \(B_d^5\equiv I\pmod5\) and iterating yields \(B_d^{5^t}\equiv I\pmod{5^t}\) for every \(t\ge1\). Fix \(r\ge2\), set \(h=5^{r-1}\), and write \(B_d^h=I+5^{r-1}D\), with \(D\) integral. Expanding \((I+5^{r-1}D)^j\) for \(0\le j\le4\), and summing, gives
\[
\sum_{j=0}^4B_d^{jh}\equiv5I+10\cdot5^{r-1}D\equiv5I\pmod{5^r}.
\]
All terms quadratic and higher are divisible by \(5^{2(r-1)}\), hence by \(5^r\), and the linear term is divisible by \(5^r\). Applying the first-coordinate functional to \(B_d^{n+i}\sum_{j=0}^4B_d^{jh}M_d(v_0)\), for each \(0\le i<h\), yields
\[
S_r(n):=\sum_{j=0}^{5^r-1}f_d(n+j)\equiv5S_{r-1}(n)\pmod{5^r}.
\]

**3. The base congruence.** The matrix identity \(A^5\equiv3I\pmod5\) implies \(F_{n+5}\equiv3F_n\pmod5\). Since the first five Fibonacci residues are \(0,1,1,2,3\), the only zero among any five successive residues occurs at the index divisible by five. Because \(4\mid d\), Fermat's theorem makes every nonzero \(F_n^d\) equal to one modulo five, and \(3^d\equiv1\pmod5\) makes these indicators five-periodic. Every five-term sum therefore satisfies \(S_1(n)\equiv4\equiv-1\pmod5\). Inducting with step 2 proves
\[
S_r(n)\equiv-5^{r-1}\pmod{5^r}\quad\text{for all }r\ge1,n\ge0.
\]

**4. Exact gcd valuations.** Write \(k=5^r u\) with \(r=\nu_5(k)\). If \(r\ge1\), divide each length-\(k\) interval into \(u\) consecutive blocks of length \(5^r\). By step 3, independently of the starting index,
\[
W_{d,k}(n)\equiv-u5^{r-1}\pmod{5^r}.
\]
Since \(5\nmid u\), this implies \(\nu_5(W_{d,k}(n))=r-1\) for **every** \(n\ge0\). If \(r=0\), the difference between the first two windows is
\[
W_{d,k}(1)-W_{d,k}(0)=F_k^d-F_0^d=F_k^d\equiv1\pmod5.
\]
Indeed, \(5\nmid k\) implies \(5\nmid F_k\). Thus the first two windows cannot both be multiples of five, so \(\nu_5(C_d(k))=0\). Both cases establish the theorem. \(\square\)

## Verification
The self-contained standard-library program `artifacts/verify.py` verifies the exact matrix identity \(A^5=\bigl(\begin{smallmatrix}3&5\\5&8\end{smallmatrix}\bigr)\), 600 independently evaluated block congruences for exponents \(4,8,12,20\), lengths \(5,25,125,625,3125\), and 30 starts per pair, and 1,120 integer-gcd checks across exponents \(4,8,12,20\) and lengths up to \(650,230,145,95\) respectively. The gcd tests use the first \(d+1\) windows, which suffice by the recurrence from step 1. Run `python3 artifacts/verify.py` from the package root. These finite checks corroborate, and do not replace, the unbounded proof.

## Relationship to prior work
Mbirika and Spilker (first public 2022-04-26, arXiv:2204.12626) solve the quadratic-power Fibonacci window gcd and explicitly raise higher-power gcd questions in Section 6. Adegoke (arXiv:1706.00407) supplies formulas for fourth-power Fibonacci sums, without classifying prime-five gcd valuations of all translates. A published quartic-window prime-order theorem covers primes at least seven and explicitly leaves \(2,3,5\) outside its scope; a second published odd-quartic-window formula assumes the length is coprime to five. Their statements therefore do not imply the present exceptional five-primary law. This theorem additionally holds for every fourth-multiple exponent, not only the quartic case. Its proof exploits the scalar collision of the Fibonacci matrix modulo the ramified prime five, rather than the Vandermonde diagonalization valid away from that prime.

## Limitations
This is a local prime-five result, not a complete factorization of the window gcd. It does not cover exponents outside multiples of four, other linear recurrences, arbitrary Gibonacci initial values, or all higher-power sums modulo unrelated primes. Closed-form expressions for individual sums do not automatically imply the gcd claim, but an equivalent implicit corollary in unindexed literature cannot be excluded. No independent mathematical audit has been performed.

## References
1. aBa Mbirika and Jürgen Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers*, arXiv:2204.12626 (first posted 2022-04-26), Section 6, Question 6.1; https://arxiv.org/abs/2204.12626 and https://www.mathstat.dal.ca/FQ/Papers1/60-5/mbirika.pdf.
2. Kunle Adegoke, *Sums of fourth powers of Fibonacci and Lucas numbers*, arXiv:1706.00407 (first posted 2017-05-28); https://arxiv.org/abs/1706.00407.
3. *All prime factors at least seven in fourth-power Fibonacci window gcds*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-all-prime-factors-at-least-seven-in-fourth-power-fibonacci-windo--d68afecbf84e.
4. *Prime-order factorization of odd quartic Fibonacci and Lucas window GCDs*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-prime-order-factorization-of-odd-quartic-fibonacci-and-lucas-win--45586db4c178.
