# Exact additive energy of modular hyperbolas at every odd modulus

## Finding
For each odd integer \(q\ge3\), put \(R_q=\mathbb Z/q\mathbb Z\), \(U_q=R_q^\times\), and
\[
H_q=\{(u,u^{-1}):u\in U_q\}\subset R_q^2.
\]
Define its ordered additive energy by
\[
\mathcal E(q)=\#\{(u,v,w,z)\in U_q^4:
 u+v\equiv w+z\pmod q,\quad
 u^{-1}+v^{-1}\equiv w^{-1}+z^{-1}\pmod q\}.
\]
For every odd prime \(p\) and integer \(k\ge1\), the exact answer is
\[
\boxed{\mathcal E(p^k)=3p^{2k-2}(p-1)\big(k(p-1)-1\big)
 =3\varphi(p^k)^2\left(k-\frac1{p-1}\right).}
\tag{1}
\]
For every odd \(q\ge3\), the Chinese remainder theorem gives the complete multiplicative classification
\[
\boxed{\mathcal E(q)=\prod_{p^k\parallel q}
 3p^{2k-2}(p-1)\big(k(p-1)-1\big).}
\tag{2}
\]
In particular, \(\mathcal E(q)/\varphi(q)^2
=3^{\omega(q)}\prod_{p^k\parallel q}(k-1/(p-1))\), where \(\omega(q)\) counts distinct prime divisors. An equivalent *complete fourth moment* of Kloosterman sums is
\[
\sum_{a,b\bmod q}\left|
  \sum_{u\in U_q}\exp\!\left(\frac{2\pi i(au+bu^{-1})}{q}\right)
\right|^4=q^2\mathcal E(q).
\tag{3}
\]
The prime-field instance \(k=1\) recovers the previously established energy \(3(p-1)(p-2)\); the exact prime-power formula for \(k\ge2\) and its odd-modulus product are the contribution assessed here.

## Assumptions and scope
All rings are the ordinary commutative residue rings \(R_q\), and all four variables are **units**. Quadruples are ordered, with repetitions allowed. The modulus is odd and at least three. For prime powers, \(p\) is an odd prime and \(k\) is any positive integer. In a valuation \(\nu_p(t)\) of a residue modulo \(p^k\), the value is truncated at \(k\): \(\nu_p(0)=k\). No asymptotic limits or assumptions on primality outside the displayed factorization are used.

## Proof
**1. Reduction to one normalized collision count.** Fix \(p\) odd, \(k\ge1\), \(Q=p^k\), and \(N=|U_Q|=(p-1)p^{k-1}\). Every collision is unchanged under the invertible transformation \((u,v,w,z)\mapsto (xu,xv,xw,xz)\), since both the ordinary and inverse-sum equalities are preserved. Thus we may fix the first entry to be \(1\) and multiply its collision count by \(N\).

Write the second entry as \(t\), the third as \(r\), and the fourth as \(1+t-r\), with all entries units. The first-coordinate equality is automatic, and the inverse-coordinate equality is equivalent to
\[
(1+t)(r-1)(r-t)\equiv0\pmod Q.
\tag{4}
\]
Indeed the inverse sums have invertible denominators, so one first obtains equality of \((1+t)/(t)\) and \((1+t)/(r(1+t-r))\), which is exactly (4). Conversely, (4) together with the unit conditions is sufficient.

**2. Three disjoint residue regimes for \(t\).** Since \(p\) is odd, the classes \(1\) and \(-1\) modulo \(p\) are distinct.

*If \(t\not\equiv\pm1\pmod p\)*, all of \(1+t\) and \(1-t\) are units. The factors \(r-1\) and \(r-t\) cannot both be divisible by \(p\), so (4) has precisely \(r=1\) and \(r=t\) modulo \(Q\). They give legal fourth entries. There are \((p-3)p^{k-1}\) choices of \(t\), contributing \(2(p-3)p^{k-1}\).

*If \(t\equiv-1\pmod p\)*, then \(1-t\) is a unit. For each \(1\le j<k\), there are \((p-1)p^{k-j-1}\) choices with \(\nu_p(1+t)=j\). By (4), \(r\equiv1\) or \(r\equiv t\pmod{p^{k-j}}\), giving exactly \(2p^j\) legal \(r\) modulo \(Q\). When \(t=-1\) exactly, (4) is automatic and all \(N\) units \(r\) work. The total from this regime is
\[
2\sum_{j=1}^{k-1}(p-1)p^{k-j-1}p^j+N=(2k-1)N.
\tag{5}
\]

*If \(t\equiv1\pmod p\)*, then \(1+t\) is a unit. Put \(h=\nu_p(t-1)\), with \(1\le h\le k\). Equation (4) becomes \((r-1)(r-t)\equiv0\pmod Q\). If \(2h<k\), its roots are the two disjoint classes \(r\equiv1\) and \(r\equiv t\pmod {p^{k-h}}\), so there are \(2p^h\) roots. If \(2h\ge k\), the roots are precisely \(r\equiv1\pmod{p^{\lceil k/2\rceil}}\), so there are \(p^{\lfloor k/2\rfloor}\). To verify the latter characterization, write \(s=r-1\), \(d=t-1\). If \(\nu_p(s)<\lceil k/2\rceil\), then \(\nu_p(s)<h=\nu_p(d)\), so both factors have valuation \(\nu_p(s)\) and their product has valuation \(2\nu_p(s)<k\); such a value is not a root. Conversely, if \(\nu_p(s)\ge\lceil k/2\rceil\), both factors are divisible by \(p^{\lceil k/2\rceil}\), so their product vanishes modulo \(p^k\). All these roots give legal unit fourth entries, because both are \(1\) modulo \(p\).

Set \(m=\lfloor(k-1)/2\rfloor\) and \(\ell=\lfloor k/2\rfloor\). For each \(1\le h\le m\), exactly \((p-1)p^{k-h-1}\) values of \(t\) have that valuation, yielding \(2mN\) roots in total. The remaining \(t\), characterized by \(t\equiv1\pmod {p^{m+1}}\), number \(p^{k-m-1}\); each gives \(p^\ell\) roots. Since \(k-m-1=\ell\), the contribution is
\[
2mN+p^{2\ell}.
\tag{6}
\]

**3. Exact simplification.** The total number of normalized collisions is therefore
\[
B=2(p-3)p^{k-1}+(2k+2m-1)N+p^{2\ell}.
\]
If \(k\) is odd, \(2\ell=k-1\) and \(2m=k-1\); if \(k\) is even, \(2\ell=k\) and \(2m=k-2\). Substituting either parity gives the same identity
\[
B=3p^{k-1}\big(k(p-1)-1\big).
\]
Multiplying by the \(N\) possible first entries proves (1) for every \(p\) and \(k\), including \(k=1\).

**4. General odd modulus and Fourier form.** If \(q_1,q_2\) are coprime, the Chinese remainder theorem identifies \(U_{q_1q_2}\) with \(U_{q_1}\times U_{q_2}\), and each of the two collision congruences splits into its independent components. Thus \(\mathcal E(q_1q_2)=\mathcal E(q_1)\mathcal E(q_2)\), giving (2). Expanding the fourth power in (3), the two sums over \(a,b\) each impose a full congruence by finite-character orthogonality and contribute a factor \(q\); their surviving terms are exactly the \(\mathcal E(q)\) collisions. This proves (3). \(\square\)

## Verification
The standard-library Python program `verify_energy.py` separately builds the ordered pair-sum multiplicity table and sums its squares. It checks the prime-power formula at 16 moduli, the Chinese-remainder product at 18 composite odd moduli, and the normalized fixed-first-index root counts for 1,496 unit parameter choices. Its observed output was `VERIFY_OK local_moduli=16 composite_moduli=18 fixed_first_root_cases=1496`. These are finite consistency checks; the complete claim follows from the above counting proof.

## Relationship to prior work
Iosevich, Murphy, and Pakianathan (2014), arXiv:1405.7657v1, study this exact finite-ring hyperbola, its Kloosterman Fourier coefficients, and spectral graph properties. Their Fourier and graph identities motivate the fourth-moment interpretation, but their inspected results do not give the ordered fourfold additive energy for prime-power rings. Ricotta and Royer (2016), arXiv:1609.03694v1, analyze the **same pair-sum and inverse-pair-sum collision equations** for Kloosterman paths at prime-power moduli. Their Proposition 5.4 gives a big-O upper bound, while their Proposition 5.5 bounds a restricted fourth moment; the source does not present an exact all-exponent value of the full collision count. Their treatment is the closest substantive antecedent.

The finite-field energy \(3(p-1)(p-2)\) is already available via the classical fourth-moment method and an exact sharp extension result for multiplicative hyperbolas; the present formula agrees with and does not reclaim that case. Previous digit-tree results for *orthogonality of characters* restricted to prime-power hyperbolas study zeros of individual Kloosterman coefficients rather than the sum of their fourth powers. The explicit factor \(k(p-1)-1\) and the multiplicative formula for arbitrary odd moduli are not implied by those cited statements. A differently named exact complete Kloosterman fourth-moment identity could nevertheless establish the same formula, so historical priority remains subject to specialist review.

## Limitations
The proof assumes odd moduli. It does not compute the entire ordered pair-sum multiplicity distribution, weighted-energy optimizers, individual Kloosterman fourth moments with one frequency held fixed, or an analogous formula for even moduli. Exhaustiveness of the historical literature cannot be certified by text searches, and no independent mathematical audit has been performed.

## References
1. A. Iosevich, B. Murphy, J. Pakianathan, *The square root law and structure of finite rings*, arXiv:1405.7657v1, first submitted 2014-05-29, https://arxiv.org/html/1405.7657v1.
2. G. Ricotta, E. Royer, *Kloosterman paths of prime powers moduli*, arXiv:1609.03694v1, first submitted 2016-09-13, especially Propositions 5.4–5.5, https://arxiv.org/abs/1609.03694.
3. G. Mockenhaupt, T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234, first submitted 2002-04-18.
4. *Sharp fourth-moment extension on the finite-field multiplicative hyperbola*, published research record, public research identifier 0835fe791166.
5. *Sharp orthogonal exponential capacity and digit-tree rigidity of prime-power modular hyperbolas*, published research record, public research identifier debdea61056e.
