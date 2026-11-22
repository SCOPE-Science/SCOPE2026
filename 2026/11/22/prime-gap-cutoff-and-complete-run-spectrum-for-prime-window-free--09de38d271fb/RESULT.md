# Prime-gap cutoff and complete run spectrum for prime-window-free blocks

## Finding

For every integer \(k\ge2\), write \(\mathcal P_k=\{p\text{ prime}:k<p<2k\}\), \(M_k=\prod_{p\in\mathcal P_k}p\), and let \(I_k(n)\) be the indicator that none of the integers \(n-k,\ldots,n-1\) is divisible by a prime in \(\mathcal P_k\). The least positive period of \(I_k\) is exactly \(M_k\).

Put \(g_k=\min_{p\in\mathcal P_k}(p-k)\), the gap from \(k\) to its next prime, and define
\[
A_{k,r}=\prod_{p\in\mathcal P_k}\max\{p-k-r+1,0\}\quad(r\ge1).
\]
Then the number \(R_{k,r}\) of *maximal cyclic runs of exactly \(r\) consecutive admissible endpoints* in one period is
\[
R_{k,r}=A_{k,r}-2A_{k,r+1}+A_{k,r+2}\quad(r\ge1).
\]
In particular, \(R_{k,r}=0\) for \(r>g_k\), and \(R_{k,g_k}>0\). If \(\mathcal P_k\) contains exactly one prime, the only nonzero count is \(R_{k,g_k}=1\). If \(\mathcal P_k\) contains at least two primes, then
\[
R_{k,r}>0\quad\text{for every }1\le r\le g_k,
\]
so *every* run length up to the sharp prime-gap cutoff occurs. In fact, the only values of \(k\ge2\) for which any intermediate length is absent are \(k=3\) and \(k=5\): each has a single run of length two per period. For all other \(k\), every length \(1\le r\le g_k\) occurs.

The number of admissible endpoints is \(A_{k,1}\); the number of nonempty runs is \(A_{k,1}-A_{k,2}\), and the run counts satisfy \(\sum_{r\ge1}rR_{k,r}=A_{k,1}\). For example, at \(k=7\) the relevant primes are \(11\) and \(13\), the cutoff is \(g_7=4\), and the exact run counts for lengths \(1,2,3,4\) are respectively \(2,2,2,3\) in the period \(143\). These are counts in a complete residue period, not a claim about the least admissible endpoint after \(2k\).

## Assumptions and scope

The integer \(k\) is at least two. By Bertrand's postulate, \(\mathcal P_k\) is nonempty, and every prime in it exceeds \(k\). All periods and runs refer to the bi-infinite periodic sequence \((I_k(n))_{n\in\mathbb Z}\) or, equivalently, the cyclic word of length \(M_k\). A maximal cyclic run is a maximal connected cluster of ones on that cycle; since there are zeros, the run decomposition is well-defined even when a run crosses the displayed period boundary. Empty products are not needed because \(\mathcal P_k\ne\varnothing\).

## Proof

**1. Residue box.** For each \(p\in\mathcal P_k\), the block \(n-k,\ldots,n-1\) is free of multiples of \(p\) exactly when
\[
n\bmod p\in B_p=\{0,k+1,\ldots,p-1\},
\]
which has \(p-k\) residues. The Chinese remainder theorem identifies the admissible residue set modulo \(M_k\) with the nonempty Cartesian product \(\prod_{p\in\mathcal P_k}B_p\). Hence \(M_k\) is a period.

To see it is the **least** period, suppose a positive integer \(h\) is a period. Translation by \(h\) preserves this Cartesian-product set. Projection onto the residue coordinate modulo each prime \(p\) shows \(B_p+h=B_p\) in \(\mathbb Z/p\mathbb Z\). But \(B_p\) is nonempty and proper, and a nonzero translation modulo a prime acts transitively. Thus \(p\mid h\) for every \(p\in\mathcal P_k\), whence \(M_k\mid h\).

**2. Consecutive admissible endpoints.** All of \(n,n+1,\ldots,n+r-1\) are admissible precisely when the union of their tested blocks, the contiguous block
\[
n-k,n-k+1,\ldots,n+r-2,
\]
of length \(k+r-1\), has no multiple of any \(p\in\mathcal P_k\). For a given prime \(p\), if \(k+r-1\ge p\) no residue works; otherwise exactly \(p-(k+r-1)\) choices work. Independent choices modulo the distinct primes, combined by CRT, give \(A_{k,r}\) exactly. In particular, \(A_{k,g_k}>0\), while \(A_{k,g_k+1}=0\).

**3. Run multiplicities.** The indicator that a run of exact length \(r\) starts at \(n\) is
\[
(1-I_k(n-1))\prod_{j=0}^{r-1}I_k(n+j)(1-I_k(n+r)).
\]
Summing it over a full period and expanding the two boundary factors gives \(A_{k,r}-2A_{k,r+1}+A_{k,r+2}\), by periodic translation. Since the cyclic word contains zeros, each maximal run has exactly one start. This establishes the formula. Summing run lengths gives \(\sum rR_{k,r}=A_{k,1}\); counting starts alone gives \(\sum R_{k,r}=A_{k,1}-A_{k,2}\).

**4. Exactly which lengths occur.** If \(\mathcal P_k=\{p\}\), the allowed residues \(B_p=\{k+1,\ldots,p-1,0\}\) form one contiguous cyclic arc of length \(p-k=g_k\), proving the singleton case.

Now suppose \(\mathcal P_k\) contains distinct primes \(p\) and \(q\). Fix \(1\le r<g_k\) and prescribe the congruences
\[
n\equiv k+1\pmod p,\qquad n\equiv1-r\pmod q.
\]
The first makes \(n-k-1\) a multiple of \(p\), so the preceding endpoint \(n-1\) fails. The second makes \(n+r-1\) a multiple of \(q\), so the following endpoint \(n+r\) fails. Neither prescribed multiple lies in the central block \([n-k,n+r-2]\): the next multiple of \(p\) after \(n-k-1\) is at least \(n-k-1+k+g_k\), hence at least \(n+r-1\), while the preceding multiple of \(q\) before \(n+r-1\) is at most \(n+r-1-(k+g_k)\), hence at most \(n-k-2\). For each remaining prime \(s\), select any residue of \(n\) avoiding multiples of \(s\) in that central block; such choices exist since \(k+r-1<s\). CRT supplies an integer \(n\) with all these prescribed residues. It begins a maximal run of length exactly \(r\), establishing \(R_{k,r}>0\). Finally \(R_{k,g_k}=A_{k,g_k}>0\), since \(A_{k,g_k+1}=0\). The classical second Ramanujan prime \(R_2=11\) gives at least two primes in \((k,2k)\) for every integer \(k\ge6\). Direct inspection of \(k=2,3,4,5\) leaves only \(k=3,5\) with \(g_k>1\) and exactly one window prime; \(k=2\) has \(g_k=1\). Thus the asserted all-parameter exception list follows. This completes the classification.

## Verification

`verify.py` performs an independent direct check of admissibility against all original consecutive factors, rather than using the product formula to generate the indicator sequence. It exhaustively enumerates each complete period for \(k\in\{2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20\}\), recovers exact maximal cyclic run counts, and checks least-period sharpness for each prime divisor of \(M_k\). It separately checks product formulas, weighted counts, and the full support dichotomy for \(2\le k<2000\). Run `python3 verify.py` with Python 3 standard library only. These finite tests corroborate, but do not replace, the proof for all \(k\).

## Relationship to prior work

The original problem asks for the first admissible endpoint \(n>2k\) and is attributed to Erdős. Van Doorn and Tang (2026, arXiv:2606.19863, first submitted 18 June 2026) prove a superpolynomial lower bound for that first endpoint. A 2025 note by Tang already gives the *one-point density* \(A_{k,1}/M_k\), so neither that density nor the basic CRT local residue criterion is claimed as new here. The finding concerns a separate, complete short-range statistic: the distribution of maximal clusters and the exact support of their lengths. It establishes neither a first-hit upper bound nor the Erdős conjecture about that bound.

The method is elementary and uses the same CRT structure underlying the one-point count. Earlier work about runs of regular residues or other sieve sets has a different local admissibility condition and does not directly supply this specific prime-window run spectrum. Possible earlier implicit specialization of the CRT method remains a priority risk.

## Limitations

The run law concerns one full (potentially exponentially long) period, not the distribution in an initial interval, and gives no uniform bound on the first eligible endpoint. The argument requires the window \((k,2k)\) and a block of \(k\) preceding integers. The result uses no hypothesis about prime-gap distribution beyond Bertrand's postulate. The mathematical result has not been independently audited; a direct inspection of the full body of Tang's 2025 PDF was not available, so priority against any implicit statement there is not certified.

## References

1. Wouter van Doorn and Quanyu Tang, *Consecutive integers free of certain prime factors*, arXiv:2606.19863, initially submitted 18 June 2026, https://arxiv.org/abs/2606.19863 .
2. Quanyu Tang, *Notes on Erdős Problem #451: density estimates and heuristic evidence*, 2 October 2025, https://github.com/QuanyuTang/Notes-on-Erdos-Problem-451 .
3. Erdős Problem #451, https://www.erdosproblems.com/451 .
4. *Erdős Problem #451: working report*, 28 July 2026, https://www.erdosproblemaday.com/report/451 .

5. Srinivasa Ramanujan, *A proof of Bertrand's postulate*, J. Indian Math. Soc. **11** (1919), 181–182; the second Ramanujan prime is \(R_2=11\), https://mathworld.wolfram.com/RamanujanPrime.html .
