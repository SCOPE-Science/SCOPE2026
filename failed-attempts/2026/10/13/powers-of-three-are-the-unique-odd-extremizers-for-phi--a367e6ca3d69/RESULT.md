# Powers of three are the unique odd extremizers for \(\Phi\)
## Finding
For \(\Phi(n)=\max\{m\in\mathbb Z_{>0}:\varphi(m)\mid 2n\}\), the sharp odd-input bound \(\Phi(n)\le 6n\) has equality exactly at powers of three: for every odd positive integer \(n\), \(\Phi(n)=6n\) if and only if \(n=3^a\) for some integer \(a\ge0\).

## Assumptions and scope
For each positive integer \(n\), define
\[
\Phi(n)=\max\{{m\in\mathbb Z_{{>0}}:\varphi(m)\mid 2n\}}.
\]
The claim concerns all odd positive integers \(n\), including \(n=1\). No assertion is made here about equality cases for even \(n\). The proof uses only elementary properties of Euler's totient function and maximality in the definition of \(\Phi\).

## Proof
Fix odd \(n\), and put \(M=\Phi(n)\). First, \(M\) is even. Indeed, if an admissible \(M\) were odd, then \(\varphi(2M)=\varphi(M)\), so \(2M\) would be a larger admissible integer.

The maximizer is not a power of two. The integer \(6\) is always admissible because \(\varphi(6)=2\mid 2n\). Thus \(M=2\) or \(M=4\) cannot be maximal. If \(M=2^r\) with \(r\ge3\), then
\[
\varphi(3\cdot2^{{r-1}})=2^{{r-1}}=\varphi(2^r),
\]
while \(3\cdot2^{{r-1}}>2^r\), again contradicting maximality.

Write
\[
M=2^r\prod_{{i=1}}^s q_i^{{e_i}},
\]
where the \(q_i\) are distinct odd primes. We have \(r\ge1\) and \(s\ge1\). Since
\[
\varphi(M)=2^{{r-1}}\prod_{{i=1}}^s q_i^{{e_i-1}}(q_i-1)
\]
and every \(q_i-1\) is even,
\[
\nu_2(\varphi(M))\ge r-1+s.
\]
But \(\varphi(M)\mid 2n\) and \(n\) is odd, so \(\nu_2(\varphi(M))\le1\). Hence \(r-1+s\le1\), and therefore \(r=s=1\). Thus
\[
M=2q^e
\]
for one odd prime \(q\) and some \(e\ge1\).

Now
\[
\frac{M}{\varphi(M)}=\frac{2q}{q-1}\le3,
\]
with equality only when \(q=3\). Since \(\varphi(M)\mid2n\), we have \(\varphi(M)\le2n\), and consequently \(M\le6n\). If \(M=6n\), both inequalities are equalities, so \(q=3\). Therefore \(M=2\cdot3^e=6n\), which forces \(n=3^{{e-1}}\).

Conversely, if \(n=3^a\) with \(a\ge0\), then
\[
\varphi(6n)=\varphi(2\cdot3^{{a+1}})=2\cdot3^a=2n.
\]
Hence \(6n\) is admissible. The preceding universal odd bound gives \(\Phi(n)=6n\). This proves the equivalence.

## Verification
The standalone verifier first computes \(\varphi(m)\) for every needed \(m\), then exactly maximizes the defining set for every odd \(n\le1000\) over the exhaustive interval \(1\le m\le6n\). It also checks the critical top candidate \(m=6n\) for every odd \(n\le200000\). The replay output is recorded in `VERIFICATION.md`. These finite checks are consistency tests; the proof above is valid for all odd positive integers.

## Relationship to prior work
Ozeki defines \(\Phi\) and proves the general product bound that yields \(\Phi(n)\le6n\) for odd \(n\). Pelizzari and Punch reproduce that bound and prove sharpness by observing that every \(n=3^k\) with \(k\ge1\) attains \(6n\). Their displayed statement establishes an infinite extremal family but does not give the converse classification. The argument above identifies all equality cases, including \(n=1\), by forcing the prime-factor shape of the maximizing integer and then analyzing equality in the totient ratio.

## Limitations
This is an equality-case classification for the sharp odd bound only. It does not improve the numerical constant \(6\), does not classify large values on even inputs, and does not alter the torsion bounds motivating \(\Phi\). The proof is short because the equality constraints are rigid. Targeted searches and full-text comparison of the two most relevant sources did not locate the converse, but older or differently phrased literature remains a residual originality risk.

## References
1. G. Pelizzari and J. Punch, *The dimension of particular \(p\)-primary torsion subgroups*, arXiv:2508.05966v1, 2025; revised as *Bounds on the Minkowski constants and a function involving \(\varphi\)*, arXiv:2508.05966v2.
2. Y. Ozeki, *Explicit bounds on torsion of CM abelian varieties over \(p\)-adic fields with values in Lubin-Tate extensions*, arXiv:2303.13725v3; Pacific Journal of Mathematics 330 (2024), 171–197.
