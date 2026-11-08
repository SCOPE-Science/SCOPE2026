# First failure of adjacent-order monotonicity for cyclotomic binomial congruences

## Finding

For positive integers \(d,t\), let \(C_t(d)\) mean that, for every integer \(n\),
\[
\frac1t\sum_{s=0}^{t-1}\binom{n+d\zeta_t^s}{d-1}
\equiv\binom{n}{d-1}\pmod d,
\qquad \zeta_t=e^{2\pi i/t}.
\]
As in Miska's definition, rational congruence modulo \(d\) means that the difference has \(p\)-adic valuation at least \(\nu_p(d)\) for every prime \(p\mid d\). The displayed average is rational.

**Theorem.** For every \(1\le d\le35\), the validity pattern in filter order is upward closed: if \(C_t(d)\) holds, then \(C_u(d)\) holds for every integer \(u>t\). The first failure occurs at modulus \(d=36\), where
\[
\{t\ge1:C_t(36)\}=\{15\}\cup\{t\ge17\}.
\]
In particular, \(C_{15}(36)\) holds for all integer arguments, whereas \(C_{16}(36)\) fails. This is the smallest modulus exhibiting a valid order followed by an invalid adjacent order.

## Assumptions and scope

All congruences are rational congruences in the above prime-adic sense. For a polynomial binomial coefficient, \(\binom{x}{c}=x(x-1)\cdots(x-c+1)/c!\) for \(c\ge0\). The theorem is an exact classification for each \(d\le36\), and establishes no monotonicity or classification for larger moduli. The filter order ranges over **all positive integers**, not merely those used by the finite computation.

## Proof

Write \(E_{c,r}=e_r(1,2,\ldots,c)\) for elementary symmetric sums, with \(E_{0,0}=1\), \(E_{c,r}=0\) outside \(0\le r\le c\), and exact recurrence
\[
E_{c,r}=E_{c-1,r}+cE_{c-1,r-1}.
\]
Root-of-unity orthogonality, applied to \(\binom{-1+d z}{c}\), gives the exact rational identity
\[
Q_{d,t,c}:=\frac1t\sum_{s=0}^{t-1}\binom{-1+d\zeta_t^s}{c}-\binom{-1}{c}
=\frac{(-1)^c}{c!}\sum_{j=1}^{\lfloor c/t\rfloor}(-d)^{jt}E_{c,c-jt}.
\tag{1}
\]
In particular, \(Q_{d,t,c}=0\) when \(t>c\). Define the integer
\[
H_{d,t,c}=\sum_{j=1}^{\lfloor c/t\rfloor}(-d)^{jt}E_{c,c-jt}.
\]
The binomial identity \(\binom{x+1}{c}-\binom{x}{c}=\binom{x}{c-1}\) implies the following finite-test equivalence: \(C_t(d)\) holds if and only if \(Q_{d,t,c}\equiv0\pmod d\) for every \(0\le c<d\). Necessity follows by successive differences of the \(c=d-1\) expression. For sufficiency, induction in \(c\) propagates each congruence from \(n=-1\) to all integers, in both forward and backward directions. Hence the equivalent entirely integral criterion is
\[
\nu_p(H_{d,t,c})-\nu_p(c!)\ge\nu_p(d)
\quad\text{for every }p\mid d\text{ and }0\le c<d,
\tag{2}
\]
where \(\nu_p(0)=+\infty\). Identity (1) and equivalence (2) reduce every assertion to finitely many integer calculations; these do not approximate the infinitely quantified congruence.

Here is a compact exact certificate for minimality. For each modulus \(d=2,3,\ldots,35\), evaluating (2) for \(t=1,\ldots,d\) gives a single threshold \(h(d)\): validity occurs exactly for \(t\ge h(d)\). In increasing order of \(d\), the full threshold sequence is
\[
\begin{aligned}
(h(2),\ldots,h(18))&=(1,1,2,1,4,1,2,2,7,1,5,1,11,6,3,1,14),\\
(h(19),\ldots,h(35))&=(1,9,9,19,1,10,2,22,3,12,1,26,1,3,15,30,8).
\end{aligned}
\]
The attached exact-integer checker evaluates all candidate orders and all lower binomial indices using the displayed recurrence, and additionally reproduces each finite coefficient as an independent rational elementary-symmetric sum. Since \(C_t(d)\) holds as an identity for \(t\ge d\), these finite rows prove the asserted upward closure for every order at all moduli below \(36\). The case \(d=1\) is immediate.

For \(d=36\), the same exhaustive criterion yields precisely the passing orders \(t=15,17,18,\ldots,36\), with all orders \(t\ge36\) trivial. As an explicit positive certificate at \(t=15\), the \(2\)-adic valuations of \(Q_{36,15,c}\), as \(c\) runs from \(15\) through \(35\), are
\[
(19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,4,3,4,2,2),
\]
and the corresponding \(3\)-adic valuations are
\[
(24,24,25,25,23,24,21,21,21,21,20,25,18,18,18,18,18,18,15,15,16).
\]
For \(c<15\) the differences vanish. Both displayed valuation lists are termwise at least \(2=\nu_2(36)=\nu_3(36)\), proving \(C_{15}(36)\).

For the adjacent order \(t=16\), the lower-binomial test with \(c=32\) gives the reduced rational number
\[
Q_{36,16,32}=
\frac{196839814746004676662011581276685234}{1506938033147421875}.
\]
Its numerator has \(2\)-adic valuation \(1\) and its denominator is odd, so (2) fails modulo \(4\). Thus \(C_{16}(36)\) fails. Exact calculation of (2) for the remaining orders \(1\le t\le36\) produces the claimed full pattern. This finishes the proof.

## Verification

Run \(\texttt{python3 verify.py}\) with Python 3 and the standard library. It enumerates all \(35\) moduli \(2\le d\le36\), the \(665\) pairs \((d,t)\) with \(1\le t\le d\), and every \(0\le c<d\), using integer arithmetic and exact rational cross-checks. All bounds are complete finite bounds justified by the reductions above, not heuristic truncations. The checker reproduces the threshold list, the exact failure fraction, and the order spectrum for \(d=36\).

## Relationship to prior work

Piotr Miska introduced \(C_t(d)\), proved the finite-test equivalence (Lemma 3.2), gave a classification outside finite exceptional classes for fixed \(t\) (Theorem 2.3), and evaluated the cases \(t\le5\) in Section 4. The finite-test equivalence and coefficient identity are cited background; the result here is the first-modulus adjacent-order comparison and complete \(d=36\) spectrum. In particular, \(36\) is a mixed-prime exceptional modulus for the fixed-order theorem at both \(t=15\) and \(t=16\); an outside-exception theorem alone does not resolve this comparison.

## Limitations

The minimality result does not assert that \(36\) is the only modulus with nonmonotone order behavior, and it does not characterize all moduli above \(36\). The finite certificate requires the provided exact-integer recurrence/checker to reproduce the entire threshold table. This is a mathematical proof supplemented by an exhaustive finite certificate, not independent external validation. An equivalent earlier classification in less readily indexed literature remains possible.

## References

P. Miska, *Binomial coefficients, roots of unity and powers of prime numbers*, arXiv:2203.03281v1, posted 7 March 2022, especially Definition 2.2, Lemmas 3.1–3.2, Theorem 2.3, Proposition 3.10, and Section 4. https://arxiv.org/abs/2203.03281

P. Miska, same title, *Bulletin of the Malaysian Mathematical Sciences Society*, DOI:10.1007/s40840-022-01266-4. The accessible preprint, rather than inaccessible publisher full text, was used for detailed comparison.
