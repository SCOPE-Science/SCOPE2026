# Exact Markov prime-factor decoupling in the rational ceiling map

## Finding
Let \(\chi(x)=x\lceil x\rceil\) on positive rationals. Fix an integer \(M\ge2\) and an integer observation horizon \(h\ge1\). Sample \(a\) uniformly from \(\{1,\ldots,M^{h+1}\}\) subject to \(\gcd(a,M)=1\). Write \(D_j(a)\) for the denominator in lowest terms of \(\chi^j(a/M)\), so \(D_0=M\), and set \(\varphi(1)=1\) for Euler's totient function. For every sequence \(M=d_0,d_1,\ldots,d_h\) of positive integers,
\[
\boxed{\Pr(D_0=d_0,\ldots,D_h=d_h)=\prod_{j=1}^{h}\frac{\varphi(d_j)}{d_{j-1}}}
\]
if \(d_j\mid d_{j-1}\) for all \(j\); otherwise its probability is zero. This finite-resolution identity is *exact*, not merely a limit as the numerator range grows. In particular the entire denominator process has the time-homogeneous Markov transition kernel
\[
\boxed{K(m,d)=\begin{cases}\varphi(d)/m,&d\mid m,\\0,&d\nmid m.\end{cases}}
\]
The process is absorbed at \(1\). If \(M=\prod_{i=1}^s p_i^{e_i}\), the prime-exponent processes \(v_{p_i}(D_j)\), including their complete paths, are independent. Consequently its absorption time is distributed as the maximum of independent random variables \(T_i\) with
\[
\Pr(T_i=n)=\binom{n+e_i-2}{e_i-1}\frac{1}{p_i^{e_i}}\left(1-\frac1{p_i}\right)^{n-1},\qquad n\ge1.
\]
The last one-dimensional law is compatible with, and can be obtained from, the previously published order-count formula; the contribution here is the exact *joint, all-denominator-path* factorization and independent prime-coordinate coupling.

## Assumptions and scope
The formula applies to every integer \(M\ge2\) and every fixed finite horizon \(h\ge1\). The numerator is sampled from the complete reduced residue system modulo \(M^{h+1}\), represented by positive integers. Probabilities of arbitrarily long paths refer to the compatible finite-dimensional distributions; no uniform probability distribution on all positive integers is presumed. The positive integer orbit is well defined, and once the denominator is \(1\) it remains \(1\). No conclusion is asserted concerning the unresolved question whether *every individual* positive reduced rational numerator eventually reaches an integer.

## Proof
**One-step algebra.** For any current positive reduced rational \(a/m\), uniquely write \(a=mt+r\), where \(0<r<m\) and \(\gcd(r,m)=1\). Then \(\lceil a/m\rceil=t+1\). Put \(g=\gcd(m,t+1)\), \(d=m/g\), and \(s=(t+1)/g\). Since \(\gcd(d,s)=1\), reducing the next iterate gives exactly
\[
\chi(a/m)=\frac{(mt+r)s}{d},\qquad \gcd((mt+r)s,d)=1.
\]
Thus the next denominator is \(d=m/\gcd(m,t+1)\). If \(t\) is uniform modulo \(m\), the number of values with \(\gcd(m,t+1)=m/d\) is \(\varphi(d)\). Hence the one-step denominator probability is \(\varphi(d)/m\).

**Uniformity of the new reduced numerator, conditional on the new denominator.** Fix any positive integer \(N\). Suppose the current numerator is uniform in the reduced residue classes modulo \(m^{N+1}\). Then its decomposition \(a=mt+r\) makes \(r\) uniform among the units modulo \(m\) and \(t\) uniform modulo \(m^N\), independently. Fix \(r\) and a permissible \(d\mid m\), and set \(g=m/d\). Conditional on \(\gcd(m,t+1)=g\), write \(t+1=gs\). Since \(m^N/g=g^{N-1}d^N\), the residue of \(s\) modulo \(d^N\) is uniform among the units modulo \(d^N\). The reduced next numerator \(b=(mt+r)s\) satisfies
\[
 b=(gm)s^2+(r-m)s\pmod{d^N}.
\]
For each prime \(\ell\mid d\), the polynomial \(P(s)=(gm)s^2+(r-m)s\) obeys \(P(s)\equiv rs\pmod\ell\) and \(P'(s)\equiv r\not\equiv0\pmod\ell\), because \(\gcd(r,m)=1\). Hensel lifting therefore makes \(P\) a permutation of the unit residue classes modulo \(\ell^k\) for every \(k\ge1\). The Chinese remainder theorem makes it a permutation of the units modulo \(d^N\). Thus, even after conditioning on \(r\) and the new denominator \(d\), the new numerator is uniform among units modulo \(d^N\). The case \(d=1\) is trivial.

**Induction over a complete path.** In the initial experiment the current numerator is uniform modulo \(M^{h+1}\), conditional on being coprime to \(M\). The preceding uniformity result with \(N=h\) shows that after the first step, conditional on the new denominator \(d_1\), the reduced numerator is uniform modulo \(d_1^h\). Apply the same result with \(N=h-1\) for the second step and continue. At each step, conditioning on *the entire previous denominator path* does not change the uniform conditional numerator distribution, by induction. Multiplication of successive transition probabilities proves the formula for the path, including absorbing paths.

**Prime-coordinate factorization.** For \(m=\prod p_i^{e_i}\) and \(d=\prod p_i^{f_i}\) with \(0\le f_i\le e_i\), multiplicativity gives
\[
K(m,d)=\prod_i\frac{\varphi(p_i^{f_i})}{p_i^{e_i}}.
\]
This is a product transition kernel on the exponent coordinates and the initial exponents are deterministic. Thus all prime-exponent *processes*, not only their absorption times, are independent. The absorption time is the maximum of their individual hitting times. The negative-binomial probabilities stated above follow either by solving the prime-power kernel recursion, or from the published exact count for fractions of fixed prime-power denominator: \(A(n,p^e)=\binom{n+e-2}{n-1}\varphi(p^e)^n\), divided by \(\varphi(p^{e(n+1)})\). This also confirms that the finite-dimensional compatible law is absorbed with probability one.

## Verification
Run \(\texttt{python3 verify.py}\) from the directory containing the standalone script. It performs exact integer and rational arithmetic, comparing every admissible complete denominator path against the predicted product probability for moduli \(2,3,4,6,8,9,10,12,15\) and horizons \(1,2,3\). It independently tests the claimed Hensel-permutation property for the prime-power congruence levels \(1\) and \(2\) and moduli up to \(16\). The observed success marker was `VERIFY_OK`. These finite calculations test implementation and boundaries only; the proof for all moduli and horizons is the one-step Hensel argument and induction above.

As a small exact instance, with \(M=6\), the probability of denominator path \((6,3,1)\) over two iterations is \(\varphi(3)/6\cdot\varphi(1)/3=1/9\). Exactly \(8\) of the \(72\) reduced residues modulo \(6^3\) have that path.

## Relationship to prior work
Azevedo, Carvalho and Machiavelo (arXiv:1210.0042v1, first public 2012-09-28) introduced the quasi-quadratic ceiling map and proved that fractions of any given order form congruence classes. Their Theorem 2.3 counts numerators by the *final hitting time*, and Corollary 2.4 provides the prime-power order counts that imply the one-dimensional negative-binomial formula. Their proof contains a related Hensel-based bijection, which is credited. The inspected published statements do not establish the complete finite-dimensional law of *all intermediate denominators*, the conditional Haar-uniform numerator transition, or independence of full prime-exponent trajectories. The present theorem reconstructs those stronger properties directly, rather than claiming priority for the marginal absorption-time counts.

## Limitations
The primary theorem is a natural-density statement under complete reduced residue sampling, not a statement of probabilistic randomness for a particular fixed rational orbit. The initial sampling modulus changes with the desired finite horizon. Independent prime processes exist as a compatible limiting distribution, not as independent sources of randomness used to generate the original deterministic map. Although the closest primary paper has been read, full historical novelty is not guaranteed; especially its proof-level bijections should be checked carefully during independent review. No independent validation has been conducted.

## References
1. A. Azevedo, M. Carvalho and A. Machiavelo, *Dynamics of a quasi-quadratic map*, arXiv:1210.0042v1 (2012-09-28), especially Proposition 2.2, Theorem 2.3, Corollary 2.4, and Section 3.
2. Classical Hensel lifting for polynomial congruences with unit derivative and the Chinese remainder theorem, used as explicit elementary lemmas above.
