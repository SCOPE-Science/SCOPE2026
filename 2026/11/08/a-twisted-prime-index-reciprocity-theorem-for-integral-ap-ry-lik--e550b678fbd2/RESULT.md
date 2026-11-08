# A twisted prime-index reciprocity theorem for integral Apéry-like recurrences

## Finding

Let \(r\in\{2,3\}\), and let \(a,b,c\in\mathbb Z\) with \(c\ne0\). Suppose the sequence \((u_n)_{n\ge-1}\) of **integers** has \(u_{-1}=0\), \(u_0=1\), and satisfies, for every integer \(n\ge0\),
\[
(n+1)^r u_{n+1}=Q_r(n)u_n-cn^r u_{n-1},\quad
Q_2(n)=an(n+1)+b,\quad
Q_3(n)=(2n+1)(an(n+1)+b).
\]
The integrality hypothesis is substantive: arbitrary parameter triples need not give integral sequences.

For **every odd prime** \(p\nmid c\), put \(e_p=u_{p-1}\bmod p\). Then
\[
\boxed{c^n u_{p-1-n}\equiv e_pu_n\pmod p}\qquad(0\le n\le p-1),
\qquad\boxed{e_p^2\equiv1\pmod p}.
\]
Thus \(e_p\) is either \(1\) or \(-1\) modulo \(p\), and the set of indices \(0\le n<p\) for which \(u_n\equiv0\pmod p\) is invariant under \(n\mapsto p-1-n\).

For the truncated sequence polynomial \(F_p(X)=\sum_{n=0}^{p-1}(u_n\bmod p)X^n\in\mathbb F_p[X]\), the **equivalent** identity is
\[
\boxed{X^{p-1}F_p((cX)^{-1})=e_pF_p(X)}.
\]
Here the left side means its polynomial expansion after clearing the denominators; \(c\) is a nonzero scalar in \(\mathbb F_p\). In particular \(\deg F_p=p-1\), and its nonzero roots over an algebraic closure are paired under \(z\mapsto(cz)^{-1}\), with multiplicities. If the quadratic character \(\chi_p(c)\ne e_p\), then \(cX^2-1\) divides \(F_p(X)\) in \(\mathbb F_p[X]\).

## Assumptions and scope

The hypotheses include integrality of every term, \(r=2\) or \(r=3\), an odd prime \(p\), and \(p\nmid c\). The result makes no unconditional statement for other recurrence orders, for prime divisors of \(c\), or for a cubic recurrence with a nonzero additional \(dn\,u_{n-1}\) term. For any given prime, only indices \(0\le n<p\) are directly classified.

The quadratic family includes the six sporadic Zagier parameter triples
\[
(7,2,-8),\ (11,3,-1),\ (10,3,9),\ (12,4,32),\ (9,3,27),\ (17,6,72).
\]
The cubic family includes the Almkvist–Zudilin triples \((7,3,81)\), \((10,4,64)\), \((12,4,16)\), \((9,3,-27)\) and the Apéry triple \((17,5,1)\). These eleven sequences are integral by their known binomial-sum representations. The theorem gives an exact twisted reciprocal coefficient identity, not merely a zero-index implication, for all eleven. The zero-index implication for four of the cubic families was explicitly identified as an unproved numerical observation by Malik and Straub (2015, section 6).

## Proof

**Step 1: recurrence reversal.** Direct substitution gives the polynomial identity
\[
Q_r(-n-1)=(-1)^r Q_r(n)\qquad(r\in\{2,3\}).
\]
For fixed \(p\nmid c\), work in \(\mathbb F_p\). Define \(v_n=c^nu_{p-1-n}\) for \(0\le n\le p-1\). For \(1\le n\le p-2\), substitute \(m=p-1-n\) into the defining recurrence at index \(m\). Since \(m\equiv-n-1\) and \(m+1\equiv-n\pmod p\), the reflected polynomial identity yields
\[
(n+1)^r v_{n+1}=Q_r(n)v_n-cn^rv_{n-1}.
\]
The transformations involve no division by \(p\) and hold for either parity of \(r\).

**Step 2: the reversed initial values.** The initial recurrence at index zero gives \(u_1=b\). The original recurrence at index \(p-1\), reduced modulo \(p\), gives
\[
0\equiv(-1)^r b\,u_{p-1}-(-1)^r c\,u_{p-2},
\]
so \(c u_{p-2}\equiv b u_{p-1}\pmod p\). Consequently
\[
v_0=u_{p-1}=e_pu_0,\qquad v_1=cu_{p-2}=e_pu_1\pmod p.
\]
For \(1\le n\le p-2\), the coefficient \((n+1)^r\) is a unit modulo \(p\). Induction by the common recurrence and these two initial values proves \(v_n=e_pu_n\) for all \(0\le n\le p-1\).

**Step 3: nonzero endpoint.** At \(n=p-1\), the preceding identity says
\[
c^{p-1}u_0=e_pu_{p-1}\pmod p.
\]
Fermat's theorem gives \(c^{p-1}\equiv1\pmod p\), while \(u_0=1\) and \(u_{p-1}=e_p\pmod p\); hence \(e_p^2=1\). In particular \(e_p\ne0\). Multiplication by \(c^n\) is reversible, so the zero-index symmetry is an equivalence.

**Step 4: reciprocal polynomial and root constraint.** The coefficient of \(X^n\) in \(X^{p-1}F_p((cX)^{-1})\) is \(c^{-(p-1-n)}u_{p-1-n}\), equal to \(c^nu_{p-1-n}\) by Fermat's theorem. The congruence in Step 2 proves the polynomial identity coefficientwise. Its leading coefficient is \(u_{p-1}=e_p\ne0\). Applying the identity over an algebraic closure gives reciprocal root pairing. If \(cx^2=1\) at a nonzero root of \(cX^2-1\), then \(x^{p-1}=\chi_p(c)\), by Euler's criterion (or by raising \(x^2=c^{-1}\) to \((p-1)/2\)). Evaluating the reciprocal identity at \(x\) gives \((\chi_p(c)-e_p)F_p(x)=0\). If the two scalars differ then both simple roots of \(cX^2-1\) are zeros of \(F_p\), giving the claimed divisibility. The roots are distinct because \(p\) is odd.

**Boundary:** A nonzero additional cubic coefficient \(d\) is not covered: for Cooper's integer sequence \(s_{10}(n)=\sum_{j=0}^n\binom nj^4\), governed by \((a,b,c,d)=(6,2,-64,4)\), one has \(s_{10}(p-1)\equiv\sum_{j=0}^{p-1}(-1)^{4j}=0\pmod p\) for every odd prime \(p\). Thus the endpoint-unit conclusion cannot be extended indiscriminately to the \(d\ne0\) cubic family. This obstruction itself is known from earlier literature, rather than asserted to be new.

## Verification

Run `python3 verify_reciprocity.py` using Python's standard library. It checks eleven integral families and sixteen odd primes through \(59\), omitting primes dividing each family coefficient \(c\). It verifies the twisted reflection and polynomial coefficient identity at all admissible indices, matches four sequence families to independently evaluated binomial sums through index \(11\), and checks the explicit excluded-family boundary at four primes. The observed message is

```text
VERIFY_OK families=11 primes=16 coefficient_checks=4803 independent_binomial_n=12 excluded_d_case_primes=4
```

The verification is finite; the unrestricted theorem is proved by Steps 1–4. No certificate of exhaustive historical originality or independent audit is claimed.

## Relationship to prior work

Malik and Straub, *Divisibility properties of sporadic Apéry-like numbers*, arXiv:1508.00297v1 (public 2015-08-03), section 6, Lemma 6.2, proves the **untwisted** reflection for the Apéry sequence and reports the corresponding zero-divisibility mirror as an **unproved empirical observation** for four Almkvist–Zudilin sequences (δ), (α), (ε), (ζ). The present theorem gives a uniform **twisted coefficient identity** for all eleven symmetric-recurrence sequences; for the Apéry sequence it recovers their Lemma 6.2. Earlier Jarvis–Verrill work established reciprocity for particular quadratic Apéry-like families, whose special cases are prior results. Gorodetsky's 2021 work gives constant-term representations and strong Lucas congruences, but the inspected main results do not assert this general index-reflection identity. There remains risk of an earlier or later equivalent identity under a different formulation; the literature comparison is not a priority certificate.

## Limitations

The result assumes integrality, excludes \(p\mid c\), and does not assert any prime-density conjecture, prime-power lift, or complete description of zero indices. This result is a self-reviewed mathematical statement; it has not been independently audited. The extension to nonzero cubic perturbation \(d\) is demonstrably false without further conditions.

## References

- A. Malik and A. Straub, *Divisibility properties of sporadic Apéry-like numbers*, arXiv:1508.00297v1 (2015), §2 Tables 1–2, §6 Lemma 6.2 and subsequent observation. https://arxiv.org/abs/1508.00297
- F. Jarvis and H. A. Verrill, *Supercongruences for the Catalan–Larcombe–French numbers*, arXiv:0905.4187v2 (2009), §2, particularly Lemmas 2.6–2.7. https://arxiv.org/abs/0905.4187
- O. Gorodetsky, *New representations for all sporadic Apéry-like sequences, with applications to congruences*, arXiv:2102.11839 (2021). https://arxiv.org/abs/2102.11839
- S. Cooper, *Sporadic sequences, modular forms and new series for \(1/\pi\)*, Ramanujan J. 29 (2012), 163–183.
