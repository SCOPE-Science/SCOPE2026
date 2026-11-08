# Digitwise classification and least equality period in the lcm-binomial triangle

## Finding
For \(0\le k\le n\), define Farhi's least-common-multiple analogue
\[
B(n,k)=\frac{\operatorname{lcm}(n-k+1,\ldots,n)}{\operatorname{lcm}(1,\ldots,k)},\qquad B(n,0)=1.
\]
The following gives a complete answer, in terms of explicit finite digit tests, to the equality-characterization question in Farhi's 2010 paper.

**Theorem.** For \(k\ge1\), write \(h_p=\lfloor\log_p k\rfloor\) for every prime \(p\le k\), and write \(n_{p,i},k_{p,i}\in\{0,\ldots,p-1\}\) for the base-\(p\) digits of \(n,k\). Then
\[
B(n,k)=\binom nk\quad\Longleftrightarrow\quad
n_{p,i}\ge k_{p,i}\quad\text{for every }p\le k,\ 0\le i<h_p.
\]
The equality is automatic when \(k=0\) or \(k=1\). For general \(k\ge1\), put
\[
e_p=\begin{cases}0,&k_{p,i}=0\text{ for all }0\le i<h_p,\\
1+\max\{i<h_p:k_{p,i}\ne0\},&\text{otherwise.}\end{cases}
\]
For fixed \(k\), the equality indicator on \(n\ge k\) has **least positive period**
\[
T_k=\prod_{p\le k}p^{e_p},
\]
and the set of accepted integers has natural density
\[
\delta_k=\prod_{p\le k}\prod_{i=0}^{h_p-1}\frac{p-k_{p,i}}{p}>0.
\]
A quantitative consequence is
\[
\delta_k\le 2^{-\#\{p\text{ prime}:k/2<p\le 2k/3\}}
=\exp\!\left(-\left(\frac{\log2}{6}+o(1)\right)\frac{k}{\log k}\right)
\quad(k\longrightarrow\infty).
\]
For example, at \(k=10\), the exact density is \(4/21\) and the least period is \(84\).

## Assumptions and scope
All integers \(n,k\) satisfy \(0\le k\le n\). A prime's digit conditions use positions strictly below its maximal power not exceeding \(k\); no high-digit conditions are imposed. For \(k=0\), all empty lcms are interpreted by \(B(n,0)=1\); the density and period are \(1\). The period is for the indicator \(\mathbf1_{B(n,k)=\binom nk}\), **not** for Farhi's entire integer-valued quotient.

## Proof
**Prime-adic identity.** Fix \(k\ge1\) and a prime \(p\). Put \(h=\lfloor\log_p k\rfloor\) when \(p\le k\). Let \(I=\{n-k+1,\ldots,n\}\), \(A=\max_{j\in I}\nu_p(j)\), and \(N_r=\#\{j\in I:p^r\mid j\}\). The factorial formula yields
\[
\nu_p\binom nk=\sum_{r\ge1}\left(N_r-\lfloor k/p^r\rfloor\right).
\]
The lcm ratio has valuation \(A-h\), since the largest \(p\)-valuation among \(1,\ldots,k\) is \(h\). Every interval of \(k\) successive integers contains a multiple of \(p^h\), so \(A\ge h\). For \(r>h\), the interval has at most one multiple of \(p^r\), and it has one precisely when \(h<r\le A\). Those contributions cancel \(A-h\). Therefore
\[
\nu_p\left(\frac{\binom nk}{B(n,k)}\right)
=\sum_{r=1}^{h}\left(N_r-\lfloor k/p^r\rfloor\right)
=\sum_{r=1}^{h}\mathbf1_{\{n\bmod p^r<k\bmod p^r\}}.
\]
Indeed, \(N_r=\lfloor n/p^r\rfloor-\lfloor(n-k)/p^r\rfloor\), which differs from \(\lfloor k/p^r\rfloor\) by exactly the displayed indicator. For \(p>k\) no contribution is possible, so the formula holds with an empty sum.

**Digit criterion.** Each summand is nonnegative; the quotient equals one exactly when each is zero. All comparisons \(n\bmod p^r\ge k\bmod p^r\) for \(1\le r\le h\) hold precisely when each corresponding lower digit satisfies \(n_{p,i}\ge k_{p,i}\). In one direction, nonnegative digit differences make every truncated sum nonnegative. In the other direction, if a digit at position \(i<h\) is deficient, the difference of the two residues modulo \(p^{i+1}\) is negative because the total effect of lower positions has absolute value less than \(p^i\). This proves the equivalence.

**Density.** For each prime \(p\le k\), the valid residue classes modulo \(p^{h_p}\) number \(\prod_{i<h_p}(p-k_{p,i})\). The Chinese remainder theorem gives exact independence of these finite constraints, so the valid integers are periodic and have density equal to the displayed product.

**Sharp least period.** The local support modulo \(p^{h_p}\) depends only on digits below \(e_p\), hence has period \(p^{e_p}\). If \(e_p\ge1\), set \(j=e_p-1\), choose all constrained digits equal to the corresponding digits of \(k\) except set digit \(j\) equal to \(k_{p,j}-1\). The resulting residue is rejected, but adding \(p^j\) makes it accepted without affecting other constrained digits. Thus the local support is not invariant under translation by \(p^j\), and no positive power \(p^a\), \(a\le j\), can be a local period: invariance by \(p^a\) implies invariance by its integer multiple \(p^j\). The global support is the Cartesian product of nonempty local supports under the Chinese remainder isomorphism. Any global translation period must therefore stabilize each local support under its projected translation. Hence its \(p\)-valuation is at least \(e_p\) for every constrained prime, proving the least period \(T_k\). The cases \(e_p=0\) impose no condition.

**Scarcity for growing \(k\).** For sufficiently large \(k\), any prime \(k/2<p\le2k/3\) satisfies \(p^2>k\), so \(h_p=1\) and \(k_{p,0}=k-p\). Its factor in the density is \((2p-k)/p\le1/2\); all other local factors are at most one. The prime number theorem gives \(\pi(2k/3)-\pi(k/2)=(1/6+o(1))k/\log k\), establishing the bound.

## Verification
The independent exact-integer checker `artifacts/verify.py` compares the formula to direct lcm and binomial evaluation for every \(0\le k\le\min(n,70)\), \(0\le n\le200\), totaling 11,786 comparisons. For all fixed \(k<34\) whose proposed period is at most 50,000, it exhausts one period, counts accepted residues, and rejects every proper-divisor period; 15 cases are checked. Exact arithmetic only. Finite computations corroborate but do not prove unrestricted claims.

Run: `python3 artifacts/verify.py`.

## Relationship to prior work
Farhi's 2010 paper introduced the lcm-binomial triangle, proved divisibility by the ordinary binomial coefficient, and explicitly asked for all equality pairs. Its valuation identities are an essential input to the proof above, but the digitwise necessary-and-sufficient characterization and the least period of the equality indicator are not stated there. Farhi and Kane (2008) study the entire product-over-lcm quotient and its periods. An earlier full joint valuation-distribution theorem for a generalized product-over-lcm quotient gives value frequencies; it does not, as a distribution theorem, identify precisely which integer arguments meet this equality test or determine the indicator's least period. That distribution can recover the density here and the density is not asserted to be independent of it. Hong and Qian (2014) describe sufficient families of equality pairs in their abstract; their complete text was not available for direct comparison. This is a specific historical-priority limitation, not a claim that their paper excludes a stronger result.

## Limitations
Only the equality locus, its least indicator period, its exact density and an upper bound for large \(k\) are determined. The full quotient distribution and its least period are different invariants. No optimal asymptotic constant for the density decay is claimed. A short derivation from earlier local valuation identities remains a substantive originality risk; accessible literature comparisons do not prove exclusive priority. No independent mathematical audit is claimed.

## References
- B. Farhi, *An analog of the arithmetic triangle obtained by replacing the products by the least common multiples*, arXiv:1002.1383 (first public 2010-02-06), especially the divisibility result and Section 3 Question 2.
- B. Farhi and D. Kane, *New results on the least common multiple of consecutive integers*, arXiv:0808.1507 (2008).
- S. Hong and G. Qian, *On the lcm-analog of binomial coefficient*, *Asian-European Journal of Mathematics* 7 (2014), 1450056, DOI 10.1142/S1793557114500569 (abstract available; full text not inspected).
- OEIS A093430, lcm-binomial triangle (integer table).
