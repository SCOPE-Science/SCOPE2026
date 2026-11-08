# Prime-private shattering and the complete coset profile of finite cyclic groups

## Finding

Let \(n\geq1\), let \(G=\mathbb Z/n\mathbb Z\), and let \(\mathcal H_n\) consist of **all nonempty cosets of all subgroups** of \(G\), regarded as subsets of \(G\). Equivalently, the concepts are all congruence fibers
\[
C_{d,a}=\{x\in G:x\equiv a\pmod d\},\qquad d\mid n,\quad a\in\mathbb Z/d\mathbb Z.
\]
Write \(s_r(n)\) for the number of unordered \(r\)-element supports shattered by \(\mathcal H_n\), and \(\Phi_n(z)=\sum_{r\geq0}s_r(n)z^r\).

For every integer \(n\geq3\), \(s_0(n)=1\), \(s_1(n)=n\), and \(s_2(n)=\binom n2\). For \(r\geq3\), factor \(n=\prod_{i=1}^{t}p_i^{a_i}\) into distinct prime powers, and put \(q=p^a\) and
\[
B_r(p^a)=q(q-1)+q\bigl(p^{r-2}-1\bigr)
\sum_{b=1}^{a-1}p^{(b-1)(r-2)}(q-p^b).
\]
The empty sum is zero. Then the **complete shattered-support polynomial** is determined by
\[
\boxed{\displaystyle
s_r(n)=\frac1{r!}\sum_{j=0}^{r}(-1)^j\binom rj
\prod_{i=1}^{t}\bigl(p_i^{a_i r}-jB_r(p_i^{a_i})\bigr)\quad(r\geq3).}
\]
In particular, \(s_r(n)=0\) for \(r>t\). For \(n=1\), \(\Phi_1(z)=1\); for \(n=2\), \(\Phi_2(z)=1+2z\).

Consequently,
\[
\boxed{\operatorname{VCdim}(\mathcal H_n)=
\begin{cases}0,&n=1,\\1,&n=2,\\\max\{2,\omega(n)\},&n\geq3,\end{cases}}
\]
where \(\omega(n)\) is the number of distinct prime divisors. Whenever \(t=\omega(n)\geq3\), the number of *maximum-cardinality* shattered supports is
\[
\boxed{s_t(n)=\prod_{p^a\parallel n}B_t(p^a).}
\]
For squarefree \(n\) with \(t\geq3\), this simplifies to the arithmetic identity
\[
\boxed{s_t(n)=\prod_{p\mid n}p(p-1)=n\varphi(n).}
\]
The coefficient formula is valid for every positive integer \(n\), apart from the explicitly specified one- and two-point boundary conventions.

## Assumptions and scope

Shattering is classical, nonadaptive VC shattering: \(S\subseteq G\) is shattered if every \(T\subseteq S\), including the empty trace, equals \(S\cap C\) for at least one \(C\in\mathcal H_n\). A coset is required to be nonempty as a subset of \(G\); the empty concept is not adjoined. This matters exactly at \(n=1,2\). The modulus of a concept is any positive divisor of \(n\), including \(1\) (the entire group) and \(n\) (singletons). No primality, squarefreeness, or bounded-exponent assumption is imposed on \(n\).

For a support \(S=\{x_1,\ldots,x_r\}\) with \(r\geq3\), call a prime \(p\mid n\) **private for index \(i\)** if some \(1\leq k\leq v_p(n)\) satisfies
\[
x_j\equiv x_\ell\pmod{p^k}\quad\text{for every }j,\ell\ne i,
\qquad x_i\not\equiv x_j\pmod{p^k}\quad(j\ne i).
\]
The supporting criterion proved below is that \(S\) is shattered exactly when every index has a private prime. A prime cannot be private for two different indices when \(r\geq3\).

## Proof

**1. Congruence-fiber closure.** Every subgroup of a cyclic group has the form \(dG\) for some \(d\mid n\); its cosets are precisely the displayed fibers. A nonempty intersection of two such fibers is again a congruence fiber, modulo the least common multiple of their moduli. The lcm still divides \(n\). A finite nonempty intersection therefore remains a concept in \(\mathcal H_n\).

**2. Exact private-prime shattering criterion.** If \(S\) is shattered, for every \(i\) there is a fiber containing \(S\setminus\{x_i\}\) but excluding \(x_i\). Its modulus has a prime-power factor \(p^k\) at which \(x_i\) differs from the common residue of all other points. Thus \(i\) has a private prime.

Conversely, suppose each \(i\) has some private prime. If \(r\geq3\), private primes for different indices must be different: if one prime \(p\) were private for \(i\) at exponent \(k\) and for \(j\ne i\) at exponent \(\ell\), choose a third index \(h\). Assuming \(k\leq\ell\), the witness for \(j\) gives \(x_i\equiv x_h\pmod{p^k}\), while the witness for \(i\) requires \(x_i\not\equiv x_h\pmod{p^k}\), a contradiction. Hence \(r\leq t=\omega(n)\). In particular \(r<n\) for \(n\geq3\).

Fix any nonempty trace target \(T\subseteq S\). For each \(x_i\notin T\), use the private congruence \(p_i^{k_i}\) and choose the residue shared by the other support points. These moduli have distinct prime bases, so the Chinese remainder theorem makes them compatible; their common fiber contains every point of \(T\) and omits each point outside \(T\). Alternatively, intersect the corresponding fibers using step 1. For \(T=S\), use modulus \(1\). For \(T=\varnothing\), use a singleton concept outside \(S\), which exists because \(r<n\). Therefore every trace occurs. This proves the criterion and the bound \(\operatorname{VCdim}(\mathcal H_n)\leq t\) for support sizes at least three.

**3. Attaining every size up to the number of primes.** Suppose \(t\geq3\), and choose distinct prime divisors \(p_1,\ldots,p_t\). By the Chinese remainder theorem construct \(t\) group elements \(x_1,\ldots,x_t\) with residue \(1\) modulo \(p_i\) for \(x_i\) and residue \(0\) modulo \(p_i\) for every other \(x_j\); at any remaining prime-power coordinates assign zero. The elements are distinct, and each prime \(p_i\) is private for \(x_i\). Step 2 shatters this set, yielding dimension at least \(t\). Every subset of a shattered set is shattered. For \(n\geq3\), arbitrary distinct pairs are shattered: the whole group realizes the double-positive trace, the two singleton fibers realize the single positives, and a third singleton realizes the empty trace. This proves the dimension formula, including \(n=1,2\) by direct inspection.

**4. The local private-label census.** Fix a prime power \(q=p^a\), an integer \(r\geq3\), and a designated index \(i\). Consider *ordered* \(r\)-tuples of residues modulo \(q\). Let \(v\in\{0,\ldots,a\}\) be the largest integer for which the other \(r-1\) coordinates are all congruent modulo \(p^v\). If \(v=0\), index \(i\) cannot be private. If \(v\geq1\), it is private exactly when its residue differs from theirs modulo \(p^v\).

For \(v\geq1\), the number of ordered \((r-1)\)-tuples that are all congruent modulo \(p^v\) is
\[
A_v=q\,p^{(a-v)(r-2)}.
\]
For \(1\leq v<a\), exactly \(A_v-A_{v+1}\) of these have largest common exponent \(v\). Each permits \(q-p^{a-v}\) choices for the distinguished coordinate. If \(v=a\), all other coordinates coincide, giving \(q\) choices for them and \(q-1\) choices for the distinguished coordinate. Therefore the exact local count is
\[
q(q-1)+\sum_{v=1}^{a-1}(A_v-A_{v+1})(q-p^{a-v})
=B_r(p^a).
\]
By step 2, a local prime-power tuple cannot have two distinct private indices. For any prescribed \(j\) of the \(r\) labels, the number of local tuples with none of those labels private is consequently \(q^r-jB_r(p^a)\).

**5. Global inclusion–exclusion.** By the Chinese remainder theorem an ordered \(r\)-tuple modulo \(n\) is an independent choice of a local ordered tuple at every prime power \(p_i^{a_i}\). For any fixed set of \(j\) labels, the number of tuples for which none of those \(j\) labels has a private prime equals
\[
\prod_{i=1}^{t}\bigl(p_i^{a_ir}-jB_r(p_i^{a_i})\bigr).
\]
Inclusion–exclusion over the \(r\) labels counts exactly the ordered tuples for which every label has a private prime. Such tuples have pairwise distinct entries, since equal entries cannot be separated. Dividing by \(r!\) gives the claimed \(s_r(n)\). The product is a polynomial in \(j\) of degree at most \(t\); its \(r\)th alternating finite difference vanishes for \(r>t\), confirming the upper cutoff. When \(r=t\), the only surviving leading-degree term gives \(s_t(n)=\prod_{p^a\parallel n}B_t(p^a)\). For squarefree \(n\), each \(a=1\) and \(B_t(p)=p(p-1)\), giving \(n\varphi(n)\). This completes the proof.

## Verification

The standalone script `VERIFY.py` constructs every congruence fiber directly for small moduli, enumerates all support traces through size five for \(1\leq n\leq18\), and compares with the formula. It additionally enumerates all triples for \(n\in\{30,42,60,70,105\}\), independently counts local private-label patterns for nine prime-power/rank choices, and constructs and directly checks all \(10{,}080\) maximum supports for the squarefree modulus \(210\) via the Chinese remainder theorem. All tests pass.

For illustration, \(\Phi_{30}(z)=1+30z+435z^2+240z^3\), while \(\Phi_{60}(z)=1+60z+1770z^2+2400z^3\). At \(n=210\), the coefficients of degrees three and four are \(170{,}520\) and \(10{,}080\), respectively. These finite tests are corroboration; the five proof steps above establish the result for every modulus.

## Relationship to prior work

The arithmetic VC literature generally studies translates of **one fixed subset** of a finite group. Conant, Pillay and Terry's work on finite-group VC-regularity (arXiv:1802.04246, first public 12 February 2018) develops structure and regularity theorems for such families. Sisask (arXiv:1802.02836, first public 8 February 2018) considers a relative VC dimension and proves, in Proposition 4.7, that a single subgroup coset has relative dimension zero. Neither formulation varies the subgroup across the full lattice of divisors in the concept family. In contrast, \(\mathcal H_n\) contains every coset of every subgroup; its rank is unbounded as \(\omega(n)\) grows. The cited works supply motivation and definitions but not the coefficientwise congruence-fiber census.

The proof combines standard cyclic-subgroup classification and the Chinese remainder theorem with a private-prime trace criterion and exact local counting. The arithmetic functions \(\omega\) and \(\varphi\) are classical; their appearance as VC dimension and the squarefree top coefficient is the result being asserted, not their definition.

## Limitations

The concept family consists only of single subgroup cosets, not arbitrary unions of cosets, progressions with freely chosen step and length, or cosets of arbitrary noncyclic groups. The dimension is nonadaptive VC dimension, not Littlestone dimension. An externally published equivalent enumeration under different terminology remains possible; the available comparisons do not certify historical priority. No independent mathematical audit has been performed.

## References

1. O. Sisask, *Convolutions of sets with bounded VC-dimension are uniformly continuous*, arXiv:1802.02836 (initial public posting 8 February 2018); *Discrete Analysis* 2021:1, Proposition 4.7 and Section 4. https://arxiv.org/abs/1802.02836
2. G. Conant, A. Pillay, C. Terry, *Structure and regularity for subsets of groups with finite VC-dimension*, arXiv:1802.04246 (initial public posting 12 February 2018); *J. Eur. Math. Soc.* 24 (2022), 583–621. https://arxiv.org/abs/1802.04246
3. Elementary facts used: subgroup classification for finite cyclic groups, Chinese remainder theorem, and inclusion–exclusion.
