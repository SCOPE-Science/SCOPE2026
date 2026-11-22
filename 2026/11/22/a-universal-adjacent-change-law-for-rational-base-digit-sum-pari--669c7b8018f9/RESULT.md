# A universal adjacent-change law for rational-base digit-sum parity

## Finding
Fix coprime positive integers \(a<b\) and let \(x_{a,b}(n)\) be the parity of the sum of the digits in the standard rational-base \(b/a\) representation of the integer \(n\ge0\). Define
\[
C_{a,b}(N)=\#\{0\le n<N:x_{a,b}(n)\ne x_{a,b}(n+1)\},\qquad N\ge0.
\]
If \(a,b\) are both odd, \(x_{a,b}(n)\equiv n\pmod2\), hence \(C_{a,b}(N)=N\) exactly. Otherwise exactly one of \(a,b\) is even; call that even integer \(t\). Then **for every integer \(N\ge0\)**,
\[
\boxed{C_{a,b}(bN)+C_{a,b}(aN)=tN.}
\]
In particular,
\[
\boxed{C_{a,b}(N)=\frac{t}{a+b}N+O_{a,b}(\log(N+2)).}
\]
Consequently the limiting proportions of adjacent unequal bits \(01\) and \(10\) each equal \(t/(2(a+b))\), whereas adjacent equal bits, counted together, have limiting proportion \(1-t/(a+b)\). For both odd parameters, the unequal pair proportions are each \(1/2\) and equal pairs never occur. These statements concern joint counts of equal pairs only: they do not assert separate limiting frequencies for \(00\) and \(11\).

## Assumptions and scope
The radix is \(b/a>1\); \(\gcd(a,b)=1\). Its standard digit algorithm starts with \(n_0=n\), repeatedly sets
\[
n_{j+1}=\left\lfloor\frac{a n_j}{b}\right\rfloor,\qquad d_j=a n_j-bn_{j+1}\in\{0,\dots,b-1\},
\]
and stops at zero. The digit sum is \(s_{b/a}(n)=\sum_j d_j\), with \(s_{b/a}(0)=0\), and \(x_{a,b}(n)=s_{b/a}(n)\bmod2\). Termination follows since \(0\le n_{j+1}<n_j\) for each positive \(n_j\). All density limits are over the integer indices \(n\), not over digit positions of one expansion. The constants in the errors may depend on the fixed parameters \(a,b\).

## Proof
The digit algorithm gives the elementary identity
\[
x_{a,b}(n)=x_{a,b}(\lfloor an/b\rfloor)\oplus(an\bmod b\bmod2),
\]
where \(\oplus\) is addition modulo two. In particular, for \(m\ge0\) and \(0\le r\le b\), set
\[
h_r=\lfloor ar/b\rfloor,\quad d_r=ar-bh_r,\quad
x_{a,b}(bm+r)=x_{a,b}(am+h_r)\oplus(d_r\bmod2).
\]
Here \(h_0=0\), \(h_b=a\), \(d_0=d_b=0\), and every increment \(\delta_r=h_{r+1}-h_r\) is either 0 or 1. Exactly \(a\) of the \(b\) increments are 1. Over the consecutive blocks with \(m=0,\ldots,N-1\), the corresponding jump edges \((am+h_r,am+h_r+1)\) enumerate each of the \(aN\) consecutive input edges exactly once. The phase difference on the edge at offset \(r\) is
\[
d_{r+1}-d_r=a-b\delta_r.
\]
If \(a\) is even and \(b\) odd, this phase flips precisely for \(\delta_r=1\). No edge with \(\delta_r=0\) produces a change; a jump edge produces a change exactly when the corresponding input pair is equal. Summing yields \(C_{a,b}(bN)=aN-C_{a,b}(aN)\). If \(a\) is odd and \(b\) even, the phase flips on all \(bN\) edges. A nonjump edge then always changes; a jump edge changes precisely when its input pair is equal. Thus \(C_{a,b}(bN)=bN-C_{a,b}(aN)\). These are the asserted two-scale identities.

For the asymptotic, write \(\beta=t/(a+b)\) and \(E(M)=C_{a,b}(M)-\beta M\). The exact identity gives \(E(bN)=-E(aN)\). Since \(C_{a,b}\) counts binary changes, \(|E(M)-E(M')|\le|M-M'|\) for \(M\ge M'\). Putting \(K=\lfloor M/b\rfloor\), obtain
\[
|E(M)|\le|E(bK)|+b=|E(aK)|+b.
\]
Repeated replacement \(M\mapsto a\lfloor M/b\rfloor\) decreases any \(M\ge b\) by at least the fixed ratio \(a/b<1\), and terminates below \(b\), where \(|E(M)|<b\). There are at most \(O_{a,b}(\log(M+2))\) replacements, proving the error bound. Every change is either \(01\) or \(10\); their counts differ by \(x_{a,b}(N)-x_{a,b}(0)\), whose absolute value is at most one. Halving the change frequency yields the asserted ordered unequal-pair densities and aggregate equal-pair density.

Finally, if \(a\) and \(b\) are both odd, strong induction from the digit recursion gives \(x_{a,b}(n)\equiv n\pmod2\): if \(h=\lfloor an/b\rfloor<n\), then \(x(n)\equiv h+(an-bh)\equiv n\pmod2\), since both parameters are odd. The stated alternating behavior follows.

## Verification
The standalone `verify.py` implements the Euclidean digit algorithm and, independently, a tabulated recurrence. It checks 149 coprime rational bases \(b/a\) with \(2\le b\le22\), compares both constructions, verifies exact two-scale equalities at several scales and all-odd alternation, and tests longer prefixes for six mixed-parity bases. Execution produces `PASS 149 coprime bases; 15377 independent identities and checks`. These are finite checks only; the all-parameter and all-index results follow from the preceding proof.

## Relationship to prior work
Rigo and Stipulanti (2021 preprint; 2022 publication) establish rational-base automatic sequence representations and give the base-\(3/2\) digit-sum-parity example. Dekking (2023) studies that sequence through block substitutions. Later work of Cassaigne and collaborators (2026) reports numerical predictions for its two-letter frequencies; the particular base-\(3/2\) case of the present law, \(\Pr(01)=\Pr(10)=1/5\), is explicitly anticipated there and is not asserted as a new numerical observation. The present statement instead treats **every coprime rational radix**, gives the exact all-prefix two-scale identity, and proves an error of order at most logarithmic without assuming the existence of individual symbol frequencies. The searched works do not state this universal parameter law; undiscovered equivalent arguments remain possible.

## Limitations
The theorem does not establish the separate frequencies of \(00\) and \(11\), individual zero/one frequencies, higher-order pattern laws, or sharp constants for the logarithmic error. This is a mathematical derivation with finite computational cross-checks, not an independent external proof audit. Literature comparisons are limited to the expressly inspected sources and searches.

## References
- M. Rigo and M. Stipulanti, *Automatic sequences: from rational bases to trees*, DMTCS 24:1 (2022), arXiv:2102.10828 (first public version 2021-02-22), https://arxiv.org/pdf/2102.10828.
- M. Dekking, *The Thue-Morse sequence in base 3/2*, Journal of Integer Sequences 26 (2023), arXiv:2301.13563 (first public version 2023-01-31), https://arxiv.org/pdf/2301.13563.
- J. Cassaigne et al., *Symbols frequencies in the Thue--Morse word in base 3/2 and related conjectures*, arXiv:2602.21895 (2026), https://arxiv.org/pdf/2602.21895; a later comparison source, not the date defining the initial research context.
