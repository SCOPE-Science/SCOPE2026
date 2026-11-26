# Uniform local Dold classifications for negative-unit Lucas pairs

## Finding
Fix any integer \(P\ge1\). Define the two integer sequences
\[
U_0=0,\quad U_1=1,\quad V_0=2,\quad V_1=P,\qquad
W_{n+2}=P W_{n+1}+W_n\quad(W=U,V).
\]
For a prime \(p\), let \(A_p(n)=p^{\nu_p(U_n)}\) and \(B_p(n)=p^{\nu_p(V_n)}\), for \(n\ge1\), and let \(D=P^2+4\). All these terms are positive. Write
\[
\mathcal L_n(F)=\sum_{d\mid n}\mu(n/d)F(d),\qquad
k(F)=\min\{k\ge1:n\mid k\mathcal L_n(F)\text{ for every }n\ge1\}.
\]
Thus \(k(F)=1\) means that \(F\) satisfies all Dold congruences. For every odd \(p\), put \(\chi_p=(D/p)\), including \(\chi_p=0\) when \(p\mid D\). If \(p\nmid D\), let \(\rho_p\) be the least positive index with \(p\mid U_{\rho_p}\). Then:

1. **Exact minimal repair for first-kind terms.**
\[
k(A_p)=\begin{cases}
3,&p=2,\ P\text{ odd},\\
2,&p=2,\ P\text{ even},\\
p,&p\text{ odd},\ p\mid D,\\
\rho_p/\gcd(\rho_p,p-1),&p\text{ odd},\ p\nmid D.
\end{cases}
\]
For odd unramified primes, \(\rho_p\mid p-\chi_p\). In particular \(A_p\) is Dold **if and only if** \(p\) is odd and \(\chi_p=+1\). All \(\mathcal L_n(A_p)\) are nonnegative; consequently all \(A_p\) are almost realizable (and realizable exactly at their Dold primes).

2. **Exact minimal repair for companion terms.** For odd \(p\nmid D\) with \(\rho_p\) odd, \(B_p(n)=1\) identically. In all other cases,
\[
k(B_p)=\begin{cases}
3,&p=2,\ P\text{ odd},\\
1,&p=2,\ P\text{ even},\\
1,&p\text{ odd},\ p\mid D,\\
\rho_p/\gcd(\rho_p,p-1),&p\text{ odd},\ p\nmid D,\ \rho_p\text{ even}.
\end{cases}
\]
For odd primes, \(B_p\) is Dold precisely when \(\chi_p\ge0\) or \(p\equiv1\pmod4\). The companion \(2\)-part is Dold exactly when \(P\) is even. The companion \(p\)-part is almost realizable if and only if **no** term \(V_n\) is divisible by \(p\), or \(p=2\) and \(\nu_2(P)=1\); in these cases it is already realizable. All remaining companion prime parts have a negative Möbius transform and cannot be made realizable by any positive integer multiplier.

3. **Prime densities.** For every fixed \(P\ge1\), among rational primes, the Dold-prime set for \(A\) has natural prime density \(1/2\), and the Dold-prime set for \(B\) has natural prime density \(3/4\). The finitely many ramified primes and the prime \(2\) do not affect these densities.

## Assumptions and scope
The parameter is a fixed, arbitrary positive integer \(P\), with \(Q=-1\) in the standard Lucas convention. The discriminant \(D=P^2+4\) is strictly positive and cannot be a perfect square for \(P\ge1\), since \(P^2<D<(P+2)^2\). The local prime part is formed from **every term** indexed by \(n\ge1\), and the minimal repair multiplier must work simultaneously for every index. No assertion is made about arbitrary \(Q\) or about optimal finite verification ranges.

A sequence \(F\) is **realizable** when \(\mathcal L_n(F)/n\) is a nonnegative integer at every index, and is **almost realizable** if a positive integer multiple is realizable. No dynamical system is assumed in the definitions.

## Proof
**1. Prime-power valuations away from \(2\).** Let \(\alpha=(P+\sqrt D)/2\) and \(\beta=(P-\sqrt D)/2\). Then \(\alpha\beta=-1\), \(U_n=(\alpha^n-\beta^n)/(\alpha-\beta)\), and \(V_n=\alpha^n+\beta^n\). Both roots are units at every prime.

Fix an odd \(p\nmid D\). In the unramified quadratic \(p\)-adic algebra containing the two roots, \(x=\alpha/\beta\) has a well-defined residue of order \(\rho\). The rank condition \(p\mid U_n\iff \rho\mid n\) follows because \(\alpha-\beta\) is a unit. Frobenius is the identity if \(\chi_p=+1\), and swaps the roots if \(\chi_p=-1\), proving \(\rho\mid p-\chi_p\). In particular \(p\nmid\rho\). Write \(e=\nu_p(U_\rho)\ge1\). The odd-prime lifting formula applied to \(x^\rho\) gives, for every \(n\ge1\),
\[
A_p(n)=\begin{cases}
p^{e+\nu_p(n/\rho)},&\rho\mid n,\\
1,&\rho\nmid n.
\end{cases}\tag{1}
\]
If \(\rho\) is odd, no \(V_n\) is divisible by \(p\): divisibility of \(V_n\) would force \(\rho\mid2n\), but \(\rho\nmid n\). If \(\rho=2t\) is even, \(p\mid V_n\) exactly for \(n/t\) a positive odd integer. Moreover \(\nu_p(V_t)=\nu_p(U_{2t})=e\) by \(U_{2t}=U_tV_t\). Odd-prime lifting for sums of odd powers shows
\[
B_p(n)=\begin{cases}
p^{e+\nu_p(n/t)},&n/t\text{ is a positive odd integer},\\
1,&\text{otherwise}.
\end{cases}\tag{2}
\]

If \(p\mid D\), then \(p\ge5\) (the congruence \(P^2\equiv-4\pmod3\) has no solution). The roots coincide modulo \(p\), while \(\nu_p(x-1)=\nu_p(D)/2\ge1/2>1/(p-1)\) in the ramified quadratic extension. Binomial lifting therefore gives \(\nu_p((x^n-1)/(x-1))=\nu_p(n)\), so \(A_p(n)=p^{\nu_p(n)}\). Also \(V_n\equiv2(P/2)^n\not\equiv0\pmod p\), whence \(B_p(n)=1\).

**2. Exact odd-prime repair and signs.** For any sequence equal to \(1\) except at multiples of an integer \(r>1\), with the values of (1), the only nonzero Möbius transforms after index \(1\) are
\[
\mathcal L_r=p^e-1,\qquad
\mathcal L_{r p^j}=p^{e+j-1}(p-1)\quad(j\ge1).
\]
All are nonnegative. Since \(p\nmid r\), the congruence at \(rp\) requires \(r\mid k(p-1)\); this condition also suffices for every listed index. Thus the **minimal** multiplier is \(r/\gcd(r,p-1)\). Taking \(r=\rho\) gives the unramified first-kind assertion. For a ramified prime \(A_p(n)=p^{\nu_p(n)}\): its only nonzero transforms above index \(1\) are \(\mathcal L_{p^j}=p^{j-1}(p-1)\), making \(k(A_p)=p\) exactly.

For a companion sequence (2), put \(r=2t=\rho\). The Möbius transform at \(2t\) is \(1-p^e<0\), and at \(2tp^j\) for \(j\ge1\) is \(-p^{e+j-1}(p-1)\). Corresponding positive coefficients occur at \(t\) and \(tp^j\), with the usual index-\(1\) adjustment when \(t=1\). Every nonzero transform has index dividing either \(t p^j\) or \(2t p^j\). Exactly the condition \(2t\mid k(p-1)\) from \(2tp\) controls the index divisibility, giving the asserted minimal \(k(B_p)=\rho/\gcd(\rho,p-1)\). A negative transform cannot be removed by positive scaling. When no term is divisible by \(p\), the prime part is the realizable constant sequence \(1\).

It remains to turn these rank tests into character tests. For odd \(p\nmid D\), if \(\chi_p=+1\) then \(\rho\mid p-1\), so \(A_p\) is Dold. If \(\chi_p=-1\), then \(\rho\mid p+1\). Because \(p\nmid U_1\) and \(\rho=2\) would mean \(p\mid P\), which instead implies \(D\equiv4\pmod p\), we have \(\rho>2\); hence \(\rho\nmid p-1\), since \(\gcd(p-1,p+1)=2\). This proves the first-kind criterion.

For the companion, inertness alone does not force bad Dold congruences. In the inert quadratic residue field, \(\alpha^p=\beta\), \(\beta=-\alpha^{-1}\), and hence
\[
(\alpha/\beta)^{(p+1)/2}=(-1)^{(p+3)/2}.
\]
If \(p\equiv1\pmod4\), the right side is \(1\), so \(\rho\) is odd and \(B_p\equiv1\). If \(p\equiv3\pmod4\), the right side is \(-1\), so \(\rho\) is even and divisible by \(4\); then \(\rho\nmid p-1\) and the companion fails Dold. Split primes and ramified primes were already settled. This establishes the odd-prime companion criterion.

**3. The prime \(2\).** When \(P\) is even, let \(a=\nu_2(P)\ge1\). The recurrence modulo \(2\), the identities \(U_{2n}=U_nV_n\), \(V_{2n}=V_n^2-2(-1)^n\), and odd-index lifting give
\[
A_2(n)=\begin{cases}1,&n\text{ odd},\\2^{a+\nu_2(n)-1},&n\text{ even},\end{cases}\qquad
B_2(n)=\begin{cases}2^a,&n\text{ odd},\\2,&n\text{ even}.
\end{cases}\tag{3}
\]
For \(A_2\), \(\mathcal L_2=2^a-1\) forces the factor \(2\), and this factor makes all other (nonnegative) transforms divisible by their indices. For \(B_2\), only \(\mathcal L_1=2^a\) and \(\mathcal L_2=2-2^a\) can be nonzero; both already satisfy Dold. The latter is negative exactly when \(a>1\). For \(a=1\) the companion local sequence is constantly \(2\) and is realizable.

When \(P\) is odd, modulo \(2\) both sequences have period three. The exact initial valuations \(\nu_2(U_3)=1\) and \(\nu_2(V_3)=2\), odd-index lifting, and repeated doubling give
\[
A_2(n)=\begin{cases}1,&3\nmid n,\\2,&3\mid n\text{ and }n\text{ odd},\\2^{\nu_2(n)+2},&3\mid n\text{ and }n\text{ even},\end{cases}
\]
\[
B_2(n)=\begin{cases}1,&3\nmid n,\\4,&3\mid n\text{ and }n\text{ odd},\\2,&3\mid n\text{ and }n\text{ even}.
\end{cases}\tag{4}
\]
The nontrivial transforms for \(A_2\) are \(\mathcal L_3=1\), \(\mathcal L_6=6\), and \(\mathcal L_{3\cdot2^j}=2^{j+1}\) for \(j\ge2\). They are nonnegative and need exactly the multiplier \(3\). For \(B_2\), \(\mathcal L_3=3\) and \(\mathcal L_6=-2\) (besides \(\mathcal L_1=1\)); exactly the multiplier \(3\) repairs Dold, but negative sign prevents realizability. These calculations finish all prime-\(2\) cases.

**4. Densities.** The integer \(D=P^2+4\) is nonsquare; thus \(\mathbb Q(\sqrt D)\) is a real quadratic field. By the prime number theorem for quadratic characters (or Chebotarev), the sets \(\chi_p=\pm1\) have prime density \(1/2\). Since \(\mathbb Q(\sqrt D)\) and \(\mathbb Q(i)\) are distinct quadratic fields, their compositum is biquadratic, so the four joint sign classes of \(\chi_p\) and \((-1/p)\) each have density \(1/4\). The first-kind Dold set is the split class (density \(1/2\)). The companion Dold set is the split class together with inert primes \(p\equiv1\pmod4\) (density \(1/2+1/4=3/4\)); the finitely many ramified primes and \(2\) do not matter.

## Verification
The included standalone `verify.py` enumerates parameters \(1\le P\le20\) and primes \(p\le43\) (280 parameter-prime pairs). It computes both Lucas sequences through \(n=200\) in exact integer arithmetic and independently compares each prime part against formulas (1)--(4). It also calculates the Möbius transforms and verifies predicted repair divisibility, sign patterns, and Dold-prime criteria on that range. The actual replay prints `VERIFY_OK parameter_prime_cases=280 max_index=200 U_and_V_exact_valuations=PASS repair=PASS signs=PASS`. Finite computations corroborate the algebra but do not establish the infinite congruences or prime densities; those follow from the proof.

## Relationship to prior work
Chuysurichay--Jaidee--Panraksa--Ward (2026, arXiv:2609.24544v1) determine local Dold primes, exact repair, and densities for the **classical** first-kind Fibonacci and companion Lucas sequences (the single parameter \(P=1\)); their discussion explicitly motivates moving to general Lucas parameters. Earlier prime-local Pell calculations treat the single parameter \(P=2\). Neither isolated parameter result implies a uniform all-\(P\) theorem, particularly the discriminant-dependent ramification and the complete companion prime-\(2\) dichotomy.

The separately published result *All local prime parts are Dold for split companion Lucas sequences* covers only companion sequences with **positive square discriminant** and integral roots. This is logically disjoint from the present \(D=P^2+4\), which is nonsquare for every allowed \(P\). Sanna (2016) and Murru--Sanna (2018) give general valuation results for Lucas sequences, from which some valuation ingredients here can be obtained, but they do not present the simultaneous local-Dold, minimal-repair, realizability, and prime-density classification for this parameter family. Byszewski--Graff--Ward (2021) explain global Dold congruences of trace sequences, which do not in general persist upon taking local prime parts. The claim is a specific combined local theorem, not originality of classical rank and valuation lemmas.

## Limitations
This classification is confined to \(Q=-1\), fixed positive integral \(P\), and integer indices \(n\ge1\); it does not handle all \((P,Q)\). The companion *realizable-prime density* is not determined here: the result determines its exact primewise predicate, but making a density claim for it would require additional order-distribution input. The prime densities here are natural densities within the primes, not ordinary integer densities. Independently checking priority against literature not indexed or accessible remains necessary.

## References
1. S. Chuysurichay, S. Jaidee, C. Panraksa, and T. Ward, *The local Dold congruence for Fibonacci and Lucas sequences*, arXiv:2609.24544v1 (first posted 2026-09-21), https://arxiv.org/abs/2609.24544.
2. C. Sanna, *The p-adic valuation of Lucas sequences*, Fibonacci Quarterly 54 (2016), 118--124, https://doi.org/10.1080/00150517.2016.12427821.
3. N. Murru and C. Sanna, *On the k-regularity of the k-adic valuation of Lucas sequences*, J. Théor. Nombres Bordeaux 30 (2018), 227--237, https://doi.org/10.5802/jtnb.1025.
4. J. Byszewski, G. Graff, and T. Ward, *Dold sequences, periodic points, and dynamics*, Bull. Lond. Math. Soc. 53 (2021), 1263--1298, https://doi.org/10.1112/blms.12531.
5. *All local prime parts are Dold for split companion Lucas sequences*, published finding, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-all-local-prime-parts-are-dold-for-split-companion-lucas-sequenc--82bcde83c42e.
