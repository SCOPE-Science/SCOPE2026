# One prime-base solution class in every nonzero residue class at each prime-power modulus

## Finding
For every prime \(p\) and integer \(a\ge1\), put \(m=p^a\). Define
\[
F_m(q)=\binom{qm}{m}-q^m\qquad(q\in\mathbb Z_{\ge0}).
\]
There are exactly \(p\) solutions \(q\bmod p^a\) of \(F_m(q)\equiv0\pmod{p^a}\), one in each residue class modulo \(p\). The unique solution divisible by \(p\) is \(q\equiv0\pmod{p^a}\), and \(q\equiv1\pmod{p^a}\) is always another solution. In particular the admissible **prime bases** \(q\ne p\) lie in exactly \(p-1\) reduced classes modulo \(p^a\), and the prime number theorem for arithmetic progressions gives
\[
\#\{q\le X:q\text{ prime},\ q\ne p,\ F_m(q)\equiv0\pmod m\}
\sim\frac{X}{p^{a-1}\log X}.
\]
This count is for fixed \(p,a\) as \(X\to\infty\); it does not assert a uniform error term in varying \(p,a\).

## Assumptions and scope
Integers \(q\ge0\) are used for residue classification. Prime-base counts restrict to positive primes distinct from \(p\). Ordinary binomial coefficients are evaluated at nonnegative integers. The parameters \(p\) and \(a\) are fixed in the density assertion. The theorem includes \(p=2\) and \(p=3\).

## Proof
**Integral product and derivative congruence.** Fix a prime \(p\), an integer \(a\ge1\), and \(m=p^a\). The exact identity
\[
H_m(q):=\binom{qm}{m}=q\prod_{j=1}^{m-1}\left(1+\frac{(q-1)m}{j}\right)
\]
holds for all integers \(q\ge1\), and also at \(q=0\) by the zero factor. Each \(m/j\) has \(p\)-adic valuation at least one, because \(1\le j<m\) implies \(v_p(j)\le a-1\). Consequently the product \(P(q)=H_m(q)/q\), defined by the displayed formula, lies in \(1+p\mathbb Z_p\).

Let \(k\ge1\), \(t\in\mathbb Z\), and \(\Delta=p^kt\). Each individual factor in \(P(q+\Delta)\) differs from its counterpart in \(P(q)\) by \(\Delta m/j\in p^{k+1}\mathbb Z_p\). Hence
\[
P(q+\Delta)\equiv P(q)\pmod{p^{k+1}},
\qquad
H_m(q+\Delta)-H_m(q)\equiv\Delta\pmod{p^{k+1}}.
\]
To compare the power terms, the binomial expansion gives
\[
(q+\Delta)^m-q^m=\sum_{i=1}^{m}\binom mi q^{m-i}\Delta^i.
\]
The \(i=1\) term is divisible by \(p^{a+k}\), hence by \(p^{k+1}\). For \(i\ge2\), each term is divisible by \(p^{ik}\), hence by \(p^{k+1}\). This shows
\[
\boxed{F_m(q+p^kt)\equiv F_m(q)+p^kt\pmod{p^{k+1}}\quad(k\ge1).}
\]
Also \(P(q)\equiv1\pmod p\) and Fermat's congruence imply \(F_m(q)\equiv q-q^{p^a}\equiv0\pmod p\) for all \(q\ge0\).

**Unique lifting.** Fix a residue \(r\bmod p\). It solves \(F_m(q)\equiv0\pmod p\). If \(q_k\) solves it modulo \(p^k\), then its \(p\) possible lifts \(q_k+p^kt\), \(0\le t<p\), have values differing from \(F_m(q_k)\) modulo \(p^{k+1}\) by exactly \(p^kt\). Exactly one is a solution modulo \(p^{k+1}\). Induction to \(k=a\) establishes exactly one class over every \(r\), hence exactly \(p\) classes. Taking \(k=a\) in the boxed congruence also proves that \(F_m(q)\bmod p^a\) depends only on \(q\bmod p^a\). Because \(F_m(0)=F_m(1)=0\) exactly, the classes \(0\) and \(1\) are as asserted.

**Prime-base density.** Every reduced residue class modulo \(p^a\) has asymptotically \(\operatorname{Li}(X)/\varphi(p^a)\) primes up to \(X\). Exactly \(p-1\) reduced classes satisfy the congruence, so the total has asymptotic main term
\[
\frac{p-1}{\varphi(p^a)}\operatorname{Li}(X)
=\frac1{p^{a-1}}\operatorname{Li}(X)
\sim\frac{X}{p^{a-1}\log X}.
\]
The excluded prime \(p\) changes the count by at most one. This proves the theorem.

## Verification
The accompanying standalone `verify.py` evaluates the exact product modulo \(p^a\) and enumerates all residue classes for \(p=2,3,5,7\) through the stated finite exponents. It checks the unique-lift property and compares the product formula with ordinary integer binomial coefficients for moderate \(m\). These finite checks corroborate, but do not replace, the unrestricted lifting proof or the classical prime number theorem in arithmetic progressions.

## Relationship to prior work
Guedes and Machado, *Structured Solutions of Prime-Base Binomial Congruences* (2026), study \(\binom{qn}{n}\equiv q^n\pmod n\) and prove a square-modulus Wieferich criterion. A closer earlier result, *Prime-power towers for the prime-base binomial congruence* (2026), fixes distinct primes \(p\ge5,q\) and classifies **the exponents** \(a\) for which \(p^a\) works, through a \(p\)-adic binomial limit. Its full result was inspected. Neither cited statement gives the converse-axis classification here: for **each fixed** \(p^a\), precisely which residue classes of variable bases \(q\) solve it, and how frequently prime bases occur. The local congruence for changes in \(q\) supplies that additional input. The prime number theorem for arithmetic progressions and single-digit lifting are classical and not claimed as new.

## Limitations
No bound uniform in varying \(p,a,X\) is claimed; nor are the individual nontrivial root classes given closed formulas. The prior literature scan cannot exclude an unindexed equivalent result, and the motivating arXiv full text was not accessible for direct whole-document comparison; its abstract and metadata were available. The close published result's full statement and proof were inspected. This is a self-reviewed result only; no independent mathematical audit has been performed.

## References
1. G. A. Guedes and R. N. Machado Jr., *Structured Solutions of Prime-Base Binomial Congruences*, arXiv:2606.30232v1, first publicly posted 29 June 2026, primary MSC2020 11B65. https://arxiv.org/abs/2606.30232
2. *Prime-power towers for the prime-base binomial congruence*, public research result dated 4 October 2026. https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-prime-power-towers-for-the-prime-base-binomial-congruence--a71ec1d0fa28/RESULT.md
3. Prime number theorem for arithmetic progressions (classical theorem).
