# Composition-centralizer spectra of prime-kernel cyclic Frobenius-group endomorphisms

## Finding

Let \(p\) be a prime, \(r\ge 3\) a divisor of \(p-1\), and \(u\in\mathbb F_p^\times\) an element of multiplicative order exactly \(r\). Let
\[
G_{p,r}=\langle a,b\mid a^p=b^r=1,\quad bab^{-1}=a^u\rangle\cong C_p\rtimes_u C_r,
\qquad M_{p,r}=\operatorname{End}(G_{p,r}).
\]
Every centralizer below is a **composition centralizer in the entire monoid** \(M_{p,r}\), not a centralizer in \(G_{p,r}\) or in its automorphism group. Put \(N=p(p+r-2)+1\), and let \(\varphi\) be Euler's totient function. Then the complete centralizer-size distribution is
\[
\boxed{\mathscr C_{p,r}(z)=\sum_{f\in M_{p,r}}z^{|C_{M_{p,r}}(f)|}=2z^N+(p-1)z^{p+1}+p(p-2)z^{p+r-1}+p\sum_{\substack{d\mid r\\d<r}}\varphi(r/d)z^{r+(p-1)d}.}
\]
For \(r\ge3\) the displayed centralizer values are pairwise distinct after the \(d=1\) contribution has been grouped with \(p(p-2)z^{p+r-1}\). Consequently **the number of different centralizer cardinalities is exactly \(\tau(r)+1\)**, where \(\tau\) is the divisor-counting function. In particular, the center of \(M_{p,r}\) consists precisely of the identity endomorphism and the trivial group homomorphism.

The nonautomorphisms of nontrivial image admit a canonical arithmetic coloring: write \(B_{k,t}\) for the endomorphism with \(a\mapsto 1\), \(b\mapsto a^t b^k\), where \(1\le k<r\) and \(t\in\mathbb F_p\). Set
\[
\chi(B_{k,t})=\frac{t}{1-u^k}\in\mathbb F_p.
\]
Then the **full pairwise commutation criterion**, for all \(k,\ell\in\{1,\dots,r-1\}\), is
\[
\boxed{B_{k,t}B_{\ell,v}=B_{\ell,v}B_{k,t}
\quad\Longleftrightarrow\quad
k\ell\equiv0\pmod r\ \text{or}\ \chi(B_{k,t})=\chi(B_{\ell,v}).}
\]
Thus the graph on these nonunits is governed by equality of field colors together with zero multiplication in \(\mathbb Z/r\mathbb Z\). For prime \(r\) it is the disjoint union of \(p\) complete graphs of order \(r-1\); for composite \(r\), zero-divisor edges connect different color classes.

As accompanying exact invariants, the image-order polynomial, retraction number, and full-unit-conjugacy class count are
\[
\boxed{\sum_{f\in M_{p,r}}x^{|f(G_{p,r})|}
=x+p\sum_{\substack{e\mid r\\e>1}}\varphi(e)x^e+p(p-1)x^{pr},}
\]
\[
\boxed{\#\{f\in M_{p,r}:f^2=f\}=p\bigl(2^{\omega(r)}-1\bigr)+2,\qquad
\#\bigl(M_{p,r}/\operatorname{Aut}(G_{p,r})\bigr)=p+r.}
\]
Here \(\omega(r)\) counts distinct prime divisors, the quotient means orbits for conjugation by group automorphisms, and every power \(f^2\) denotes composition. The count of **ordered commuting pairs** is exactly \(\mathscr C_{p,r}'(1)\); in particular their probability is \(\mathscr C_{p,r}'(1)/N^2\), which is asymptotic to \(1/p\) as \(p\to\infty\) along primes with fixed \(r\mid p-1\).

## Assumptions and scope

The theorem holds for all primes \(p\), all divisors \(r\mid p-1\) with \(r\ge3\), and all choices of \(u\) of order \(r\). No coprimality among the prime-power factors of \(r\) beyond its usual factorization is assumed. In particular the statement covers prime and composite complements, including prime powers and products of distinct primes. The choice of \(u\) changes no count. The case \(r=2\) is omitted because two centralizer strata merge, so the stated \(\tau(r)+1\) count would need modification.

The group is represented uniquely by \(a^i b^j\), with \(0\le i<p\), \(0\le j<r\), and multiplication
\[
(a^i b^j)(a^k b^\ell)=a^{i+u^j k}b^{j+\ell},
\]
where the first exponent is reduced modulo \(p\), the second modulo \(r\). Define \(S_m(w)=\sum_{h=0}^{m-1}w^h\) for nonnegative integers \(m\), with \(S_0(w)=0\).

## Proof

**1. Classification of all endomorphisms.** Since \(u\not=1\), the commutator subgroup of \(G_{p,r}\) is exactly \(\langle a\rangle\). It is fully invariant, hence any endomorphism maps \(a\) to \(a^s\) for a unique \(s\in\mathbb F_p\). Write the image of \(b\) as \(a^t b^k\), with \(t\in\mathbb F_p\), \(k\in\mathbb Z/r\mathbb Z\). The conjugation relation gives
\[
s(u^k-u)=0\quad\text{in }\mathbb F_p.
\]
If \(s\not=0\), exact order \(r\) forces \(k=1\). If \(s=0\), \(k\) is arbitrary. The relation \(b^r=1\) forces \(t=0\) when \(k=0\) (as \(p\nmid r\)); for nonzero \(k\), the geometric sum \(S_r(u^k)\) vanishes, so \(t\) is free. Conversely every such generator assignment respects the presentation. Thus, precisely,
\[
M_{p,r}=\{\mathbf0\}\ \sqcup\ \{U_{s,t}:s\in\mathbb F_p^\times,\ t\in\mathbb F_p\}
\ \sqcup\ \{B_{k,t}:1\le k<r,\ t\in\mathbb F_p\},
\]
where \(U_{s,t}(a)=a^s\), \(U_{s,t}(b)=a^t b\), and \(\mathbf0\) is the trivial map. Every \(U_{s,t}\) is invertible and every \(B_{k,t}\) is not, so \(\operatorname{Aut}(G_{p,r})=\{U_{s,t}\}\). This proves \(|M_{p,r}|=N\).

**2. The composition law.** For any map \(F=(s,t,k)\) in the preceding normal form and \(F'=(s',t',k')\), using \(k'\in\{0,\dots,r-1\}\), direct evaluation on the two generators yields
\[
F\circ F'=(ss',\ st'+tS_{k'}(u^k),\ kk'\bmod r).
\]
The displayed triple is reduced to the unique normal form from Step 1. This formula also shows that \(\mathbf0\) is absorbing and \(U_{1,0}\) is the identity of \(M_{p,r}\).

**3. Commutation and centralizer of a unit.** Two units \(U_{s,t}\) and \(U_{s',t'}\) commute if and only if
\[
(s-1)t'=(s'-1)t.
\]
A unit \(U_{s,t}\) commutes with \(B_{k,v}\) precisely if
\[
(s-1)v+tS_k(u)=0.
\]
Because \(k\ne0\), \(S_k(u)=(1-u^k)/(1-u)\ne0\). Therefore \(U_{1,0}\) commutes with all \(N\) maps. For \(s=1\), \(t\ne0\), there are exactly \(p\) commuting units and no commuting nonzero-image nonunits. For \(s\ne1\), there are exactly \(p-1\) commuting units and exactly one \(B_{k,v}\) for each \(1\le k<r\). Each centralizer also contains \(\mathbf0\). Thus the respective centralizer sizes are \(N\), \(p+1\), and \(p+r-1\). Their multiplicities are \(1\), \(p-1\), and \(p(p-2)\).

**4. Commutation and centralizer of a nonunit.** For \(k,\ell\in\{1,\dots,r-1\}\), the composition law gives the necessary and sufficient congruence
\[
tS_\ell(u^k)=vS_k(u^\ell)\pmod p.
\]
If \(k\ell\equiv0\pmod r\), both geometric sums vanish. Otherwise \(1-u^{k\ell}\ne0\), and division by the nonzero \(1-u^k\), \(1-u^\ell\) gives exactly \(t/(1-u^k)=v/(1-u^\ell)\). This proves the boxed color/zero-product criterion with no exceptional case. Fix \(B_{k,t}\) and put \(d=\gcd(k,r)\). Exactly \(d-1\) nonzero residue classes \(\ell\) satisfy \(k\ell\equiv0\pmod r\), and each contributes all \(p\) values of \(v\). The remaining \(r-d\) values of \(\ell\) contribute exactly one \(v\) each. Also exactly \(p-1\) units commute with \(B_{k,t}\), one choice of the translation coordinate for every nonzero unit multiplier, and \(\mathbf0\) commutes with it. Consequently
\[
|C_{M_{p,r}}(B_{k,t})|=1+(p-1)+p(d-1)+(r-d)=r+(p-1)d.
\]
There are exactly \(\varphi(r/d)\) nonzero residue classes \(k\) with \(\gcd(k,r)=d\) for each proper divisor \(d\mid r\), each with \(p\) choices of \(t\). Together with Step 3 and the centralizer of \(\mathbf0\), this proves the complete polynomial \(\mathscr C_{p,r}\).

**5. Distinctness, center, and image orders.** The proper divisors \(d\) produce distinct increasing integers \(r+(p-1)d\), whose smallest is \(p+r-1>p+1\). The largest is strictly smaller than \(N\) since \(d<r\) and \(p\ge r+1\). Thus \(2+(\tau(r)-1)=\tau(r)+1\) distinct sizes occur. Only the identity and \(\mathbf0\) have centralizer size \(N\). Each \(U_{s,t}\) has image order \(pr\). For \(B_{k,t}\), the image is cyclic generated by \(a^t b^k\), of order \(r/\gcd(k,r)\); the trivial map has image order one. Totient enumeration gives the image-order polynomial.

**6. Retractions.** An automorphism with square itself is the identity. The map \(\mathbf0\) is idempotent. By the composition law, \(B_{k,t}\) is idempotent exactly when \(k^2\equiv k\pmod r\): once this congruence holds, the geometric factor \(S_k(u^k)=(1-u^{k^2})/(1-u^k)=1\), so every \(t\) is allowed. The Chinese remainder theorem gives exactly \(2^{\omega(r)}\) idempotents in \(\mathbb Z/r\mathbb Z\), one of which is zero, so the claimed retraction number follows.

**7. Unit-conjugacy.** The identity and trivial map are fixed. Conjugating a unit by \(U_{v,w}\) sends \(U_{s,t}\) to \(U_{s,vt+(1-s)w}\). For \(s\ne1\) all \(t\) lie in one \(p\)-element orbit for each multiplier \(s\). For \(s=1\), the identity and the \(p-1\) nonzero translations form two orbits. Conjugating \(B_{k,t}\) by \(U_{v,w}\) sends its second parameter to \(vt+wS_k(u)\) and leaves \(k\) unchanged. Since \(S_k(u)\ne0\), each of the \(r-1\) nonzero classes \(k\) gives one orbit of size \(p\). Adding the trivial map yields \((p-2)+2+(r-1)+1=p+r\) orbits, as claimed.

**8. Commuting probability.** The polynomial \(\mathscr C_{p,r}\) counts all endomorphisms by the number of commuting partners, hence the number of ordered pairs is \(\mathscr C_{p,r}'(1)\). For fixed \(r\), the exact formula has leading term \(p^3\), while \(N^2\sim p^4\), proving the stated asymptotic along admissible primes. No assumption about infinitely many primes is needed for the exact finite statements.

## Verification

The accompanying standard-library Python file `reproducibility/check.py` enumerates every homomorphism candidate in the normal form and independently checks composition-centralizer sizes, image-order distributions, idempotents, unit-conjugacy orbits, and the predicted centralizer polynomial for \((p,r)=(7,3),(13,3),(13,4),(13,6),(17,8),(19,9),(31,15)\). For the first four pairs it additionally constructs maps on the actual group elements and verifies the group-homomorphism law on every ordered pair of elements, then verifies commuting relationships by full function composition. See `reproducibility/check-output.txt` for the saved invocation output. All checks passed. The general proof is Steps 1–8, not finite enumeration.

For example, at \((p,r)=(13,6)\), the exact spectrum is
\[
\mathscr C_{13,6}(z)=2z^{222}+12z^{14}+169z^{18}+26z^{30}+13z^{42},
\]
with \(4980\) ordered commuting pairs, \(41\) retractions, and \(19\) automorphism-conjugacy classes.

## Relationship to prior work

García-Blázquez and del Río (2023) give an isomorphism classification of all finite metacyclic groups by group invariants; the present family is a special metacyclic/Frobenius family, but their principal statements classify **groups**, not composition commutants of their endomorphisms. Wang (2016 preprint; 2020 publication) determines automorphism groups for broader elementary-abelian-kernel cyclic-complement Frobenius groups; that provides the surrounding group-automorphism context but neither counts noninvertible group endomorphisms nor computes their monoid centralizers. Bors (2014) studies the endomorphism monoids of different, nilpotent \(p\)-groups with abelian automorphism groups. DeWolf–Edmunds (2018) study semigroups generated by commutator maps on centerless metacyclic groups, which are not the entire group-endomorphism monoid. Ajith–Cameron–Ghosh–Lakshmanan (2025) study graphs **on elements of groups** induced by endomorphisms, not the graph whose vertices are the endomorphisms themselves. These are distinctions of mathematical statements, not just titles.

No equivalent full composition-centralizer spectrum was found in the inspected sources or searched mathematical-record summaries. This negative search is not proof of historical novelty. In particular, an unlocated general theorem for endomorphism monoids of semidirect products could subsume the calculation.

## Limitations

This theorem concerns prime cyclic kernels and faithful cyclic complements only. It makes no claim about a composite-order kernel, arbitrary elementary-abelian kernels, or the exceptional \(r=2\) stratum collision. It is a same-model mathematical proof and computational cross-check, **not an independently certified theorem**. Historical originality is provisional, especially with respect to older semidirect-product endomorphism-monoid literature. Finite verification does not replace the all-parameter proof.

## References

1. À. García-Blázquez and Á. del Río, *A classification of metacyclic groups by group invariants*, arXiv:2301.08683, first posted 2023-01-20. https://arxiv.org/abs/2301.08683
2. L. Wang, *On the automorphism groups of Frobenius groups*, arXiv:1610.05914, first posted 2016-10-19; *Communications in Algebra* 48 (2020), 5330–5342. https://arxiv.org/abs/1610.05914
3. A. Bors, *On the endomorphism monoids of some groups with abelian automorphism group*, arXiv:1411.4190 (2014). https://arxiv.org/abs/1411.4190
4. D. DeWolf and C. C. Edmunds, *Commutation Semigroups of Finite Metacyclic Groups with Trivial Centre*, arXiv:1807.10389 (2018). https://arxiv.org/abs/1807.10389
5. M. V. Ajith, P. J. Cameron, M. Ghosh, A. Lakshmanan S., *Endomorphism and automorphism graphs of finite groups*, arXiv:2511.15602 (2025). https://arxiv.org/abs/2511.15602
