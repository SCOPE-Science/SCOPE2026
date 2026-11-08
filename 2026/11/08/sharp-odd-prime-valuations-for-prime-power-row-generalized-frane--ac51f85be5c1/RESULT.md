# Sharp odd-prime valuations for prime-power-row generalized Franel sums

## Finding

For every odd prime \(p\), every integer \(q\ge1\), and every integer \(t\ge2\), put \(m=\nu_p(t-1)\) and
\[
G_{p,q}(t)=\sum_{k=0}^{p^q-1}(-1)^{kt}\binom{p^q-1}{k}^{t}.
\]
Then the **sharp congruence** is
\[
\boxed{G_{p,q}(t)\equiv -(t-1)p^q\pmod{p^{q+m+1}},\qquad \nu_p(G_{p,q}(t))=q+m.}
\]
In particular, if \(t\) is even, the signs disappear. For every odd prime \(p\) and integers \(q,a\ge1\),
\[
\boxed{\nu_p\!\left(\sum_{k=0}^{p^q-1}\binom{p^q-1}{k}^{p^a+1}\right)=q+a.}
\]
This proves the odd-prime case of the specific generalized-Franel valuation conjecture posed by Fabius Wiesner in 2025, and establishes a stronger theorem for all even exponents and the corresponding signed odd-exponent sums.

## Assumptions and scope

Here \(p\ge3\) is prime, \(q\ge1\) and \(t\ge2\) are integers, \(\nu_p\) is the usual \(p\)-adic valuation of a nonzero integer, and congruences hold in \(\mathbb Z_p\). For \(0\le k<p^q\), define
\[
U_{q,k}=(-1)^k\binom{p^q-1}{k}=\prod_{j=1}^k\left(1-\frac{p^q}{j}\right).
\]
Every denominator in this expression is invertible after canceling its power of \(p\), so \(U_{q,k}\in1+p\mathbb Z_p\). The sum of the \(U_{q,k}\) is zero because \(p^q-1>0\). The claim is for all stated primes and exponents, not merely the verified finite samples.

## Proof

**1. A binomial lifting fact.** If \(u=1+pv\in1+p\mathbb Z_p\), \(h\ge1\), \(m=\nu_p(h)\), and \(w=h/p^m\), then
\[
\frac{u^h-1}{p^{m+1}}\equiv wv\pmod p.
\]
Indeed \((1+pv)^{p^m}\equiv1+p^{m+1}v\pmod{p^{m+2}}\) for odd \(p\), by the binomial theorem and induction on \(m\); raising this to \(w\) proves the assertion. In particular \(u^h-1\in p^{m+1}\mathbb Z_p\).

**2. Initial block.** Let \(q=1\) and \(h=t-1\). For \(0\le b<p\), write \(H_b=\sum_{j=1}^b1/j\), with \(H_0=0\). Then
\[
U_{1,b}\equiv1-pH_b\pmod{p^2}.
\]
Since \(\sum_{b=0}^{p-1}U_{1,b}=0\),
\[
G_{p,1}(t)=\sum_{b=0}^{p-1}U_{1,b}(U_{1,b}^{h}-1).
\]
By step 1,
\[
\frac{G_{p,1}(t)}{p^{m+1}}\equiv-\frac{h}{p^m}\sum_{b=0}^{p-1}H_b\equiv-\frac{h}{p^m}\pmod p,
\]
because \(\sum_{b=0}^{p-1}H_b=pH_{p-1}-(p-1)\equiv1\pmod p\). This proves the asserted congruence for \(q=1\).

**3. Exact block decomposition.** Let \(q\ge2\), and write \(k=pb+a\), where \(0\le b<p^{q-1}\) and \(0\le a<p\). Splitting factors with indices divisible by \(p\) gives the exact identity
\[
U_{q,pb+a}=U_{q-1,b}V_{b,a},\quad
V_{b,a}=\prod_{\substack{1\le j\le pb+a\\p\nmid j}}\left(1-\frac{p^q}{j}\right)=1+p^qz_{b,a},
\]
where \(z_{b,a}\in\mathbb Z_p\). Put \(Z_b=\sum_{a=0}^{p-1}z_{b,a}\). Evaluating the binomial cancellation \(\sum_k U_{q,k}=\sum_b U_{q-1,b}=0\) yields the **exact** equality
\[
\sum_b U_{q-1,b}Z_b=0.
\]

**4. Inductive precision.** With \(h=t-1\) and \(m=\nu_p(h)\), subtract \(pG_{p,q-1}(t)\):
\[
G_{p,q}(t)-pG_{p,q-1}(t)
=\sum_b U_{q-1,b}^{t}\sum_{a=0}^{p-1}\left[(1+p^qz_{b,a})^t-1\right].
\]
Its linear terms in \(z_{b,a}\) total
\[
tp^q\sum_bU_{q-1,b}^{t}Z_b
=tp^q\sum_b\left(U_{q-1,b}^{t}-U_{q-1,b}\right)Z_b,
\]
which belongs to \(p^{q+m+1}\mathbb Z_p\) by step 1 and \(U_{q-1,b}\in1+p\mathbb Z_p\).

For each nonlinear term \(j\), with \(2\le j\le t\),
\[
\binom{t}{j}=\frac{t(t-1)}{j(j-1)}\binom{t-2}{j-2},
\quad\nu_p\!\left(\binom{t}{j}\right)\ge m-\nu_p(j(j-1)).
\]
For odd \(p\) and \(j\ge2\), \(\nu_p(j(j-1))\le j-2\). As \(q\ge2\),
\[
qj-\nu_p(j(j-1))\ge q+1.
\]
Thus every nonlinear summand has valuation at least \(q+m+1\). We conclude
\[
G_{p,q}(t)\equiv pG_{p,q-1}(t)\pmod{p^{q+m+1}}.
\]
Inducting from step 2 proves \(G_{p,q}(t)\equiv-hp^q\pmod{p^{q+m+1}}\). Since \(\nu_p(hp^q)=q+m\), the congruence forces the **exact** valuation \(q+m\). When \(t=p^a+1\) is even, \(h=p^a\), giving the stated unsigned formula. \(\square\)

## Verification

The accompanying `verify.py` recomputes the signed sums modulo \(p^{q+\nu_p(t-1)+1}\) using the exact integer recurrence for row binomial coefficients. It checks all tested triples against the sharp congruence, checks the ordinary unsigned formula when \(t\) is even, and includes the odd-prime and prime-power exponent ranges stated in its output. The computations verify finitely many instances only; the proof above covers every admissible triple.

## Relationship to prior work

Calkin (1998), *Factors of sums of powers of binomial coefficients*, proves broad divisibility results; its Lemma 12 concerns powers of two and binary Hamming weight, not the sharp odd-prime formula. Zhi-Wei Sun's *Congruences for Franel numbers* (first public preprint December 5, 2011) studies Franel congruences and aggregated sums rather than this exact row/exponent valuation. Lengyel (2017) studies rates of \(p\)-adic convergence of Franel-like and lacunary sums; a complete comparison with his paywalled article remains outstanding. Wiesner (June 15, 2025) explicitly asks whether \(\nu_p(f_{p^q-1}^{(p^a+1)})=q+a\) for odd \(p\); this theorem proves that identity, and improves it to the sharp congruence for all \(t\). The \(p=2\) question on that page remains open here.

## Limitations

The proof requires odd \(p\). It does not settle the distinct two-adic question, general binomial rows, or exact higher \(p\)-adic digits beyond the displayed modulus. A relevant 2017 Lengyel paper could not be read in full; its abstract and accessible first page were compared, and it remains a historical-priority risk. This is a mathematical proof accompanied by finite verification, not an independent audit.

## References

1. N. J. Calkin, *Factors of sums of powers of binomial coefficients*, Acta Arithmetica 86 (1998), 17–26, DOI 10.4064/aa-86-1-17-26. Author full-text PDF: https://www.math.clemson.edu/~calkin/Papers/factors_sums_powers_binomial_coefficients.pdf
2. Z.-W. Sun, *Congruences for Franel numbers*, arXiv:1112.1034v1 (public December 5, 2011), https://arxiv.org/abs/1112.1034
3. T. Lengyel, *On the rate of p-adic convergence of sums of powers of binomial coefficients*, Int. J. Number Theory 13 (2017), 2075–2091, DOI 10.1142/S1793042117501111.
4. F. Wiesner, *p-adic valuation of some generalized Franel numbers*, MathOverflow question 496222, June 15, 2025, https://mathoverflow.net/questions/496222/p-adic-valuation-of-some-generalized-franel-numbers
