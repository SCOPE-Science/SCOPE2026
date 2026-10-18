# Exact \(p\)-adic order of the prime-power Nekrasov--Okounkov/\(t\)-core congruence
## Finding
Let \(A(x)=\prod_{m\ge1}(1-x^m)\in\mathbb Z[[x]]\). For every prime \(p\), integer \(a\ge1\), and \(t=p^a\), write
\[
F_{t^2}(x)=A(x)^{t^2-1}=\sum_{n\ge0}a_t(n)x^n,
\qquad
C_t(x)=\frac{A(x^t)^t}{A(x)}=\sum_{n\ge0}b_t(n)x^n.
\]
Then, for every \(n\ge0\),
\[
a_t(n)\equiv b_t(n)\pmod{p^{a+1}}.
\]
The exponent is sharp uniformly in \(n\):
\[
v_p\!\left(a_t(p^{a-1})-b_t(p^{a-1})\right)=a+1.
\]
Consequently the exact largest uniform \(p\)-power modulus for the row \(t=p^a\) is \(p^{a+1}\).

## Assumptions and scope
All products are interpreted as formal power series over \(\mathbb Z\); this avoids analytic convergence issues. The statement covers every prime \(p\), every integer \(a\ge1\), and every coefficient index \(n\ge0\). The normalization agrees with the Nekrasov--Okounkov product \(F_{t^2}\) and the standard \(t\)-core product \(C_t\).

## Proof
We first prove a formal Frobenius-lift lemma. If \(f(x)\in\mathbb Z[[x]]\), \(k\ge0\), and \(m\ge1\), then
\[
f(x^{p^k})^{p^m}\equiv f(x^{p^{k+1}})^{p^{m-1}}\pmod{p^m}.
\]
Indeed, the freshman's-dream congruence gives
\[
f(x^{p^k})^p=f(x^{p^{k+1}})+pR(x)
\]
for some \(R(x)\in\mathbb Z[[x]]\). Raising this identity to \(p^{m-1}\), every nonconstant binomial term is divisible by \(p^m\). For \(1\le j\le p^{m-1}\),
\[
v_p\!\binom{p^{m-1}}{j}\ge m-1-v_p(j),
\]
because \(\binom{p^r}{j}=(p^r/j)\binom{p^r-1}{j-1}\), and therefore the term containing \((pR)^j\) has valuation at least
\[
m-1-v_p(j)+j\ge m.
\]
This proves the lemma, including \(p=2\).

Apply the lemma to \(f=A\), successively for \(k=0,1,\ldots,a-1\), starting with exponent \(p^{2a}\). The successive moduli are at least \(p^{a+1}\), so
\[
A(x)^{p^{2a}}\equiv A(x^{p^a})^{p^a}\pmod{p^{a+1}}.
\]
Since \(A(0)=1\), division by \(A(x)\) is valid in \(\mathbb Z[[x]]\), giving
\[
A(x)^{p^{2a}-1}\equiv \frac{A(x^{p^a})^{p^a}}{A(x)}\pmod{p^{a+1}},
\]
which is the asserted coefficient congruence.

It remains to prove sharpness. Put \(M=p^{a-1}\). If \(a=1\), then \([x]F_{p^2}=-(p^2-1)\) and \([x]C_p=1\), so their difference is exactly \(-p^2\).

Now assume \(a\ge2\). Iterating the same lemma only \(a-1\) times yields
\[
A(x)^{p^{2a}}\equiv A(x^M)^{p^{a+1}}\pmod{p^{a+2}}.
\]
Because \(A(x^M)=1-x^M+O(x^{2M})\), the right side has coefficient \(-p^{a+1}\) at degree \(M\) and no nonconstant terms below degree \(M\). Hence, for
\[
E(x)=A(x)^{p^{2a}}-A(x^{p^a})^{p^a},
\]
all coefficients in degrees \(1,\ldots,M-1\) are divisible by \(p^{a+2}\), while
\[
[x^M]E(x)\equiv-p^{a+1}\pmod{p^{a+2}}.
\]
Finally,
\[
F_{t^2}(x)-C_t(x)=\frac{E(x)}{A(x)}.
\]
The reciprocal \(1/A(x)\) has integral coefficients and constant term \(1\). Convolution therefore preserves the displayed residue at degree \(M\), because all lower coefficients of \(E\) vanish modulo \(p^{a+2}\). Thus
\[
[x^M]\bigl(F_{t^2}-C_t\bigr)\equiv-p^{a+1}\pmod{p^{a+2}},
\]
so the valuation is exactly \(a+1\).

## Verification
The proof is symbolic and covers infinitely many prime-power rows and all coefficient indices. The included exact-arithmetic verifier independently expands both Euler products for twelve representative pairs \((p,a)\), checks the congruence on every coefficient in its tested range, and verifies the sharp index \(p^{a-1}\). The computation is a normalization check only; it is not used to infer the infinite theorem.

## Relationship to prior work
Sharma proves that \(a_t(n)\equiv b_t(n)\pmod t\) for all \(n\) exactly when \(t\) is a prime power, and proves the stronger modulus \(p^2\) in the prime case \(t=p\). For \(t=p^a\) with \(a>1\), the published proposition supplies modulus \(p^a\), whereas the theorem above gives the strictly stronger modulus \(p^{a+1}\) and proves that no higher uniform \(p\)-power can hold. The same paper explicitly points to possible higher \(p\)-adic lifting as a natural direction.

Earlier work of Han--Ono and Clemm concerns coincidence of supports and vanishing patterns for related hook-length and core-partition series. Those statements neither imply a coefficient-by-coefficient congruence modulo \(p^{a+1}\) nor its exact sharpness witness.

## Limitations
The theorem determines only the largest modulus that works uniformly over all \(n\) within a fixed prime-power row. Individual coefficients can have larger \(p\)-adic valuation. It does not classify those exceptional higher-valuation indices, and it makes no stronger claim for non-prime-power \(t\).

## References
1. M. Sharma, *A Prime-Power Dichotomy for Nekrasov--Okounkov Hook Lengths and \(t\)-Core Partitions*, arXiv:2610.01422v1, 2026.
2. G.-N. Han and K. Ono, *Hook Lengths and 3-Cores*, arXiv:0805.2461v1, 2008.
3. A. Clemm, *A Conjecture of Han on 3-Cores and Modular Forms*, arXiv:1410.7219v1, 2014.
