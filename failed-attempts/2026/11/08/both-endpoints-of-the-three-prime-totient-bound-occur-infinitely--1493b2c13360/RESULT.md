# Both endpoints of the three-prime totient bound occur infinitely often

## Finding

For odd \(n>1\), define \(T(n)\) to be the number of odd integers \(1\le m\le n\) such that
\[
\gcd(m,n)=\gcd((m-1)/2,n)=1.
\]
Write \(S(n)=n\prod_{\ell\mid n}(1-2/\ell)\), with \(\ell\) running through the distinct prime factors of \(n\). Renshaw's Theorem 3 establishes, for \(n\) with three distinct prime factors,
\[
\frac{S(n)-13}{2}\le T(n)\le\frac{S(n)+11}{2}.
\]
Both constants are exactly optimal, each on infinitely many squarefree three-prime integers. Specifically:
\[
\begin{aligned}
 r>115,\ r\text{ prime},\ r\equiv119\pmod{230}
 &\implies T(5\cdot23\cdot r)=\frac{S(5\cdot23\cdot r)-13}{2},\\
 r>119,\ r\text{ prime},\ r\equiv31\pmod{238}
 &\implies T(7\cdot17\cdot r)=\frac{S(7\cdot17\cdot r)+11}{2}.
\end{aligned}
\]
There are infinitely many primes in each displayed progression by Dirichlet's theorem.

## Assumptions and scope

All indicated prime factors are odd and pairwise distinct. The variable \(r\) is prime and strictly exceeds the fixed product of the other two primes. This theorem establishes *two-sided sharpness* for the distinct-prime-support size \(\omega(n)=3\); it does not classify all extremizers or assert optimality for other support sizes.

## Proof

**Residue-parity transfer lemma.** Fix distinct odd primes \(p,q\) and set \(P=pq\). Define
\[
G_P=\{m:1\le m\le P,\ m\not\equiv0,1\pmod p,\ m\not\equiv0,1\pmod q\},
\qquad O_P=\#\{m\in G_P:m\text{ odd}\}.
\]
Thus \(|G_P|=(p-2)(q-2)\). For any prime \(r>P\), define \(k_c(m)\) to be the least nonnegative solution of
\[
P k_c(m)\equiv c-m\pmod r,\qquad c\in\{0,1\},\ m\in G_P,
\]
and let \(B_r\) count those \(2|G_P|\) pairs \((m,c)\) for which \(m+P k_c(m)\) is odd.

Each candidate contributing to \(T(Pr)\) has a unique form \(m+Pk\) with \(m\in G_P\) and \(0\le k<r\). Since \(P\) and \(r\) are odd, for fixed \(m\), exactly \((r-1)/2+\mathbf1_{m\text{ odd}}\) of the \(r\) candidates are odd. Exactly two values of \(k\) are prohibited by the additional prime \(r\), namely the unique values with \(m+Pk\equiv0,1\pmod r\); these two prohibited candidates are distinct. Therefore
\[
T(Pr)=\frac{(p-2)(q-2)(r-1)}2+O_P-B_r.
\]
Because \(S(Pr)=(p-2)(q-2)(r-2)\), subtraction yields the exact transfer identity
\[
2T(Pr)-S(Pr)=|G_P|+2O_P-2B_r.\tag{1}
\]

**Periodicity of the correction.** For \(m\in G_P\), \(c\in\{0,1\}\), there is a unique \(u\in\{1,\ldots,P-1\}\) satisfying \(ur\equiv m-c\pmod P\); nonzero status follows because \(m\not\equiv c\pmod p,\pmod q\). The integer
\[
k=\frac{ur+c-m}{P}
\]
is nonnegative and strictly less than \(r\), because \(r>P\), \(1\le u<P\), \(1\le m\le P\), and \(c\in\{0,1\}\). It also satisfies \(m+Pk=c+ur\equiv c\pmod r\), so it equals \(k_c(m)\). If prime \(r'>P\) obeys \(r'\equiv r\pmod{2P}\), then \(u\) is unchanged and
\[
k_c^{(r')}(m)-k_c^{(r)}(m)=u\frac{r'-r}{P}
\]
is even. Hence the parity of every forbidden candidate is unchanged, \(B_{r'}=B_r\), and by (1), \(2T(Pr')-S(Pr')=2T(Pr)-S(Pr)\). This holds for all primes \(r,r'>P\) in the same class modulo \(2P\).

**Two finite residue certificates.** The residue set, odd residue count and forbidden-odd count are obtained from their displayed definitions by exact integer enumeration:
\[
\begin{array}{c|c|c|c|c|c}
(p,q)&P&r&|G_P|&O_P&B_r\\ \hline
(5,23)&115&349&63&30&68\\
(7,17)&119&269&75&38&70
\end{array}
\]
Both witness values of \(r\) are prime and exceed \(P\). Equation (1) gives, respectively,
\[
63+2(30)-2(68)=-13,\qquad75+2(38)-2(70)=11.
\]
Directly, \(S(5\cdot23\cdot349)=21861\), \(T(5\cdot23\cdot349)=10924\), \(S(7\cdot17\cdot269)=20025\), and \(T(7\cdot17\cdot269)=10018\). Every prime \(r\equiv349\equiv119\pmod{230}\) with \(r>115\), and every prime \(r\equiv269\equiv31\pmod{238}\) with \(r>119\), has the same correction in (1) as the corresponding witness. Finally \(\gcd(119,230)=\gcd(31,238)=1\), so Dirichlet's theorem guarantees infinitely many primes in both progressions. This proves both statements.

## Verification

The standalone `verify.py` performs two independent integer calculations: enumeration of permissible odd \(m\) by gcd tests up to \(pqr\), and counting the \(2|G_P|\) forbidden candidates using modular inverses. It also checks the stated residue certificates, the equalities in (1), primality of the two witnesses, and congruence-class parity invariance against further prime witnesses. Execute with `python3 verify.py` from the extracted package directory. These finite computations certify the two finite residue tables and corroborate, but do not replace, the periodicity proof or Dirichlet's theorem.

## Relationship to prior work

Renshaw, *A Totient Function Associated with Variants of Groups* (2026), introduces \(T\), gives the general support-dependent error estimate in Theorem 3 and two-prime branches in Corollary 6. The present statement verifies that *both* extremal constants in the three-prime specialization are actually attained, infinitely often, using an explicit prime-residue transfer. Theorem 3 alone bounds the correction but does not establish either infinite extremal family. Search-based historical priority is qualified; no classification of all possible equality cases is claimed.

## Limitations

The argument uses Dirichlet's theorem and establishes infinitude, not a new quantitative error term for counting such primes. The method is conditional on \(r\) being a prime exceeding \(P\); it is not an assertion about composite \(r\). Finite certificates verify the specified small residue sets, not an unbounded search. No claim of independent mathematical validation or exhaustive literature priority is made.

## References

1. J. Renshaw, *A Totient Function Associated with Variants of Groups*, arXiv:2603.13939v1, first made public 2026-03-14, Sections 1–2, Theorem 3, Lemma 4 and Corollary 6. https://arxiv.org/abs/2603.13939
2. Dirichlet's classical theorem on primes in coprime arithmetic progressions (used for the final infinitude step).
