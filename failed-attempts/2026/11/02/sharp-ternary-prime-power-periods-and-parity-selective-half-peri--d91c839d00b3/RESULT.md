# Sharp ternary prime-power periods and parity-selective half-period defects for A158690

## Finding
Let \(a(n)\) be the integer sequence determined by
\[
\sum_{n\ge0}a(n)\frac{t^n}{n!}=1+\sum_{m\ge1}\prod_{j=1}^{m}(1-e^{-(2j-1)t}).
\]
For every integer \(r\ge1\), its **least eventual period modulo \(3^r\)** is exactly
\[
T(3^r)=2\cdot3^{r-1}.
\]
More sharply, for \(r\ge2\), every integer \(n\ge3r\), and \(h_r=2\cdot3^{r-2}\),
\[
a(n+h_r)-a(n)\equiv
\begin{cases}
2\cdot3^{r-1}\pmod{3^r},&n\text{ even},\\
0\pmod{3^r},&n\text{ odd}.
\end{cases}
\]
The Carmichael-function period known from previous work is therefore optimal for every power of three. The parity-selective formula explains exactly why its largest proper divisor is not a period.

## Assumptions and scope
The sequence is defined in the ring of formal exponential power series with integer coefficients. The notation “eventual period” means an integer \(T>0\) such that there exists \(N\) for which \(a(n+T)\equiv a(n)\pmod{3^r}\) for every integer \(n\ge N\); the least such \(T\) is sought. All assertions hold for every positive integer \(r\), with an explicit sufficient onset \(N=3r\); the onset is not asserted optimal. No statement is made about odd primes other than three.

## Proof
**1. An integral Stirling expansion.** Put
\[
G(y)=1+\sum_{m\ge1}\prod_{j=1}^{m}\bigl(1-(1+y)^{-(2j-1)}\bigr)=\sum_{k\ge0}g_ky^k.
\]
Every factor has integer power-series coefficients and zero constant term, so \(g_k\in\mathbb Z\) and each coefficient receives finitely many contributions. Substituting \(y=e^t-1\) and using the defining identity for Stirling numbers of the second kind gives
\[
a(n)=\sum_{k=0}^{n}g_k k!\,S(n,k)
=\sum_{k=0}^{n}g_k\sum_{j=0}^{k}(-1)^{k-j}\binom{k}{j}j^n.
\]
For any \(r\ge1\) put \(K=3r\). Since \(3^r\mid k!\) for every \(k\ge K\), the terms with \(k\ge K\) vanish modulo \(3^r\). Consequently for every \(n\ge K\) there exist fixed **integers**
\[
c_j=\sum_{k=j}^{K-1}g_k(-1)^{k-j}\binom{k}{j}\qquad(0\le j<K)
\]
for which \(a(n)\equiv\sum_{j=0}^{K-1}c_jj^n\pmod{3^r}\). The same coefficients work for \(n+T\) for every positive integer \(T\).

**2. Exact base computation modulo nine.** Expanding the finite products contributing through degree five gives the exact coefficient identity
\[
G(y)\equiv1+y+2y^2+7y^3+33y^4+197y^5\pmod{y^6}.
\]
Thus for \(r=2\) the preceding formula (\(K=6\)) yields
\[
(c_0,c_1,c_2,c_3,c_4,c_5)\equiv(2,7,0,0,2,8)\pmod9,
\]
and, for every integer \(n\ge6\),
\[
a(n)\equiv7+2\cdot4^n+8\cdot5^n\pmod9.
\]
For \(n=2m\) this is \(7+7^m\pmod9\), whereas for \(n=2m+1\) it is \(1\pmod9\). Since \(7^{m+1}-7^m=6\cdot7^m\equiv6\pmod9\),
\[
a(n+2)-a(n)\equiv\begin{cases}6\pmod9,&n\text{ even},\\0\pmod9,&n\text{ odd},\end{cases}\quad(n\ge6).
\]
In particular \(a(n)\equiv2\pmod3\) at all sufficiently large even indices and \(a(n)\equiv1\pmod3\) at all sufficiently large odd indices.

**3. Uniform ternary lifting of two-step differences.** For every integer \(r\ge2\) and every \(j\) coprime to three, write \(j^2=1+3b\). The binomial theorem, or induction by cubing, gives
\[
j^{2\cdot3^{r-2}}-1\equiv3^{r-2}(j^2-1)\pmod{3^r}.
\]
When \(3\mid j\), multiplying both sides by \(j^n\) gives the same congruence for every \(n\ge r\), since both products vanish modulo \(3^r\). Multiply the congruence by \(c_jj^n\), sum over the finite Stirling expansion from step 1, and obtain, for every \(n\ge3r\),
\[
a(n+2\cdot3^{r-2})-a(n)
\equiv3^{r-2}\bigl(a(n+2)-a(n)\bigr)\pmod{3^r}.
\]
Apply the exact modulo-nine result from step 2. Because the right-hand side requires only the two-step difference modulo nine, it is \(2\cdot3^{r-1}\) at even indices and zero at odd indices, as asserted.

**4. Least period.** For every \(r\), Euler's theorem gives \(j^{2\cdot3^{r-1}}\equiv1\pmod{3^r}\) when \(3\nmid j\). Terms with \(3\mid j\) vanish at indices \(n\ge3r\) in step 1. Therefore \(2\cdot3^{r-1}\) is an eventual period. For \(r=1\), the alternating residues modulo three prove that \(1\) is not an eventual period. For \(r\ge2\), every proper positive divisor of \(2\cdot3^{r-1}\) divides at least one of \(3^{r-1}\) and \(2\cdot3^{r-2}\). The first candidate fails modulo three because it is odd; the second fails modulo \(3^r\) at every even \(n\ge3r\) by step 3. Any two eventual periods also have their greatest common divisor as an eventual period, after increasing the onset if necessary. Thus no proper divisor, and hence no smaller positive period, can be an eventual period. This proves both claims.

## Verification
The standalone file `verify.py` uses exact integer arithmetic. It independently expands the original exponential generating products through degree fifteen and reconstructs the same values from the Stirling transform; it computes the first six coefficients of \(G\), and checks the asserted period and half-period defects for \(1\le r\le7\) at thirty-six consecutive indices per level. The observed result is `VERIFY_OK exact_g_prefix=6 independent_egf_coefficients=16 prime_power_levels=7 shifts=252`. These finite checks are not substituted for the all-level proof.

## Relationship to prior work
Kallat, *A Proof of Bala's Congruence Conjectures for A158690* (first public version 7 September 2026), establishes eventual periodicity with Carmichael-function upper period for all moduli. The present result determines its **least** period at every power of three and an explicit parity-dependent obstruction to shortening it. The OEIS entry A158690 describes the original conjectures and illustrates a shorter period modulo sixteen, but does not give this all-level ternary minimum. The independently considered sharp power-of-two phenomenon concerns different prime powers and does not imply the ternary statement. Danesh's August 2026 preprint gives related Stirling-transform eventual-period bounds rather than an exact ternary minimum. A complete page-level comparison of Kallat's preprint was not possible; see the limitation below.

## Limitations
The theorem is specifically about moduli \(3^r\). It does not classify the least preperiod and makes no claim for arbitrary composite moduli. The source preprint's abstract, publication metadata, and public sequence record were inspected, but the complete preprint PDF was inaccessible during this comparison; earlier implicit coverage is a residual priority risk. Independent review of correctness and originality has not been performed.

## References
- A. Kallat, *A Proof of Bala's Congruence Conjectures for A158690*, arXiv:2609.07238v1 (7 September 2026), https://arxiv.org/abs/2609.07238.
- *The On-Line Encyclopedia of Integer Sequences*, A158690, https://oeis.org/A158690 (accessed 29 October 2026).
- P. Danesh, *Eventual periodicity of weighted Stirling transforms and two conjectures of Bala*, Cambridge Open Engage (26 August 2026), DOI: 10.33774/coe-2026-4d6jr.
