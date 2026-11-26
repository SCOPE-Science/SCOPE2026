# Parity law and factorial decay for distinct cycle-count covariances in uniform derangements

## Finding

Let \(\pi\) be uniform among derangements of \([n]\). For distinct cycle lengths \(2\le j<k\) satisfying \(j+k\le n\), let \(C_j\) and \(C_k\) denote their cycle counts, put \(r=n-j-k\), and define \(s_m=\sum_{\ell=0}^{m}(-1)^\ell/\ell!\) for nonnegative integers \(m\). Then
\[
\operatorname{Cov}(C_j,C_k)=\frac{s_n s_r-s_{n-j}s_{n-k}}{jk\,s_n^2},\qquad
(-1)^r\operatorname{Cov}(C_j,C_k)>0.
\]
The covariance is **never zero** on this domain; its sign alternates with the parity of the number of labels left after marking both cycles. For each fixed pair \(j<k\), as \(r\to\infty\) through either parity,
\[
\operatorname{Cov}(C_j,C_k)=\frac{(-1)^r e}{jk\,(r+1)!}(1+o(1)).
\]
For the natural pair \(j=2,k=3\), the exact covariances at \(n=5,6,7\) are \(30/121\), \(-432/2809\), and \(1820/31827\), respectively.

## Assumptions and scope

Uniform derangements are permutations of \([n]=\{1,\ldots,n\}\) without fixed points, each with equal probability. Only two distinct cycle lengths \(j,k\ge2\) with \(j+k\le n\) are considered. All statements concern ordinary covariance of integer-valued cycle counts. The formula for the mixed factorial moment is classical; the claimed contribution is the *strict global sign classification*, its all-offset determinant inequality, and the signed sharp asymptotic.

## Proof

**1. The exact mixed moment.** There are \(n!s_n\) derangements of \([n]\). Mark a cycle of length \(j\), with \(j\ge2\), and derange the remaining labels. This gives \(\mathbb E C_j=s_{n-j}/(j s_n)\). Mark two distinct cycles of lengths \(j\) and \(k\) to obtain \(\mathbb E(C_jC_k)=s_{n-j-k}/(jk s_n)\), since the marked cycles are distinct when their lengths differ. Subtracting products of expectations gives the displayed exact covariance.

**2. A signed determinant lemma.** We prove for every \(r\ge0\) and every positive integer \(a,b\),
\[
(-1)^r\big(s_r s_{r+a+b}-s_{r+a}s_{r+b}\big)>0.
\]
The alternating-series remainder gives \(s_{2t}>e^{-1}>s_{2t+1}\); the even subsequence \(u_t=s_{2t}\) is strictly decreasing and the odd subsequence \(v_t=s_{2t+1}\) is strictly increasing. These monotonicities prove the determinant sign whenever the offsets \(a,b\) have different parity: by symmetry take \(a\) even and \(b\) odd. For even \(r\), we have \(s_r>s_{r+a}\) (even subsequence) and \(s_{r+a+b}>s_{r+b}\) (odd subsequence), so the determinant is positive; for odd \(r\), both comparisons reverse and the determinant is negative. If both offsets are odd, for even \(r\) both \(s_r,s_{r+a+b}\) exceed \(e^{-1}\) while both \(s_{r+a},s_{r+b}\) are below it; for odd \(r\) the two sides swap. Both cases are strict.

It remains to consider both offsets even. We show \(u_t\) is strictly log-convex and \(v_t\) strictly log-concave. Write
\[
d_t=u_t-u_{t+1}=\frac{2t+1}{(2t+2)!},\qquad
\frac{d_t}{d_{t+1}}=(2t+1)(2t+4)\ge4.
\]
Also \(u_{t+1}\le1/2\) and \(u_{t+2}>e^{-1}\), hence \(u_{t+1}/u_{t+2}<e/2<4\). Consequently \(d_tu_{t+2}>d_{t+1}u_{t+1}\), equivalent to \(u_tu_{t+2}>u_{t+1}^2\). For the odd subsequence let
\[
c_t=v_{t+1}-v_t=\frac{2t+2}{(2t+3)!}.
\]
Here \(c_t>c_{t+1}>0\), so
\[
v_{t+1}^2-v_tv_{t+2}=v_{t+1}(c_t-c_{t+1})+c_tc_{t+1}>0.
\]
Strict log-convexity (respectively log-concavity) means adjacent log-ratios strictly increase (respectively decrease). Therefore, for arbitrary positive offsets \(h,l\),
\[
u_tu_{t+h+l}>u_{t+h}u_{t+l},\qquad v_tv_{t+h+l}<v_{t+h}v_{t+l}.
\]
These are the even-even offset cases for even and odd \(r\). The lemma follows.

**3. Apply the lemma.** With \(a=j\), \(b=k\), the covariance numerator is precisely the lemma's determinant with \(n=r+j+k\), while \(jk s_n^2>0\). The strict sign statement follows for all allowed parameters, including \(r=0\).

**4. Sharp decay.** The exact alternating-series error may be written
\[
s_m=e^{-1}+(-1)^m a_m,\quad
a_m=\frac{1}{m!}\int_0^1 e^{u-1}u^m\,du
=\frac{1+o(1)}{(m+1)!}.
\]
For fixed positive \(j,k\), all errors \(a_{r+j},a_{r+k},a_{r+j+k}\) are \(o(a_r)\), as are products of two errors. Thus \(s_rs_{r+j+k}-s_{r+j}s_{r+k}=(-1)^r e^{-1}a_r(1+o(1))\), while \(s_n^2=e^{-2}(1+o(1))\); substitution yields the asserted coefficient \(e/(jk)\).

## Verification

The self-contained Python 3 script `verify.py` computes all relevant rational expressions using `fractions.Fraction`, checking **38,779 exact signed covariances** for \(5\le n\le80\). It independently enumerates all derangements for \(5\le n\le8\), comparing 13 mixed covariances to the formula without relying on marked-cycle counting. Both checks passed. These finite checks corroborate but do not replace the all-parameter proof above.

## Relationship to prior work

Arratia and Tavaré (arXiv:1308.3279, initially posted 2013-08-15, MSC 60C05) develop conditioned independent-process representations and derangement approximations (notably §7.2.1 and §9). Da Silva, Jamshidpey and Tavaré (arXiv:2006.04840, initially posted 2020-06-08, §2.1, equation (6)) **already give the general joint factorial moments** from which the first displayed covariance formula follows by subtraction. Their §2.4 gives asymptotic independence. The result here does not claim new factorial moments, but supplies a strict parity sign law for every finite size and a signed factorial-scale first asymptotic term. No equivalent strict all-parameter sign theorem was located in the inspected texts; historical-priority uncertainty remains.

## Limitations

No independence is claimed; covariance is strictly nonzero for the stated pairs. The sign assertion is not extended to equal cycle lengths, nonuniform Ewens weights, or pairs with \(j+k>n\). The signed asymptotic assumes the two lengths are held fixed. Existing general factorial moments cover the algebraic covariance identity, and a previously published version of the sign inequality might exist under another description. Mathematical verification is not an independent audit.

## References

1. R. Arratia and S. Tavaré, *Independent Process Approximations for Random Combinatorial Structures*, Adv. Math. (1994); publicly accessible preprint arXiv:1308.3279, version 1 posted 2013-08-15. https://arxiv.org/abs/1308.3279.
2. P. H. da Silva, A. Jamshidpey and S. Tavaré, *Random derangements and the Ewens Sampling Formula*, arXiv:2006.04840, version 1 posted 2020-06-08. https://arxiv.org/abs/2006.04840.
