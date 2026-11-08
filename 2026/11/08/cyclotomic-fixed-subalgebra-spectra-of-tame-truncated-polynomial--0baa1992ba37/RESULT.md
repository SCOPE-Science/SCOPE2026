# Cyclotomic fixed-subalgebra spectra of tame truncated-polynomial automorphisms

## Finding
Let \(n\ge 2\), let \(q=p^e\) be any prime power of characteristic \(p>n\), and put \(A=\mathbb F_q[t]/(t^n)\). An automorphism \(\phi\) is determined by \(\phi(t)=a_1t+\cdots+a_{n-1}t^{n-1}\), where \(a_1\ne0\). Write \(R(\phi)=\dim_{\mathbb F_q}\{f\in A:\phi(f)=f\}\). For an element \(a\in\mathbb F_q^\times\) of multiplicative order \(d\), set
\[
 h_d=\left\lfloor\frac{n-2}{d}\right\rfloor,\qquad L_d=\left\lfloor\frac{n-1}{d}\right\rfloor.
\]
Exactly \((q-1)q^{n-2-j}\) automorphisms having \(a_1=a\) have \(R=1+j\) for each \(1\le j\le h_d\), and a further \(q^{n-2-h_d}\) have \(R=1+L_d\). These multiplicities are **added** when two indicated dimensions coincide. In particular, conditional on \(a_1=a\), the probabilities are \((q-1)q^{-j}\) at \(1+j\), for \(1\le j\le h_d\), and \(q^{-h_d}\) at \(1+L_d\). This holds for every finite extension field of characteristic \(p>n\).

There is also a fixed-ring normal form. After an automorphism of \(A\) changes coordinates, \(\phi=\sigma_a u=u\sigma_a\), where \(\sigma_a(t)=at\) and \(u(t)=t+\sum_{j=1}^{h_d}b_jt^{1+jd}\). If \(u=1\), its fixed algebra is the span of \(1,t^d,\ldots,t^{L_dd}\), isomorphic to \(\mathbb F_q[y]/(y^{L_d+1})\). Otherwise, if \(j\) is the smallest index with \(b_j\ne0\), the fixed algebra is the span of \(1,t^{(L_d-j+1)d},\ldots,t^{L_dd}\), isomorphic to \(\mathbb F_q\oplus y^{L_d-j+1}\mathbb F_q[y]/(y^{L_d+1})\) with multiplication induced from the truncated polynomial ring.

As a consequence, the exact number of orbits of \(\operatorname{Aut}_{\mathbb F_q}(A)\) acting on the underlying set \(A\) is
\[
 \frac{1}{q-1}\sum_{d\mid(q-1)}\varphi(d)\bigl(h_dq(q-1)+q^{L_d+1-h_d}\bigr),
\]
where \(\varphi\) is Euler's totient function. This is an orbit count for elements of \(A\), not a classification of algebras.

## Assumptions and scope
All fields are finite of characteristic \(p>n\), and \(n\ge2\). The group is the complete group of unital \(\mathbb F_q\)-algebra automorphisms, not only linear scalings. The fixed algebra is taken under **one** automorphism, including its constant elements. The coefficient \(a=a_1\) is fixed when stating the conditional law; averaging uniformly over \(a\in\mathbb F_q^\times\) produces the full law. The denominator group order is \((q-1)q^{n-2}\).

## Proof
**1. The tame substitution decomposition.** Let \(U\) be the subgroup with \(a_1=1\); it has order \(q^{n-2}\). Each \(v\in U\) is upper unitriangular on the basis \(1,t,\ldots,t^{n-1}\), so \((v-I)^n=0\). In characteristic \(p>n\), \(v^p=(I+(v-I))^p=I\). Fix an automorphism \(\phi\) with multiplier \(a\) of order \(d\). Since \(d\mid(q-1)\), \(p\nmid d\), and \(\phi^d\in U\), hence \(\phi^{dp}=1\). Choose an integer \(r\) with \(pr\equiv1\pmod d\). Then \(s=\phi^{pr}\) has order dividing \(d\), its multiplier is \(a\), and \(u=s^{-1}\phi\in U\); moreover \(s\) and \(u\) commute and \(u^p=1\). This pair is canonical, so no multiplicity is lost.

**2. Linearization and uniform centralizers.** Every \(s\) of order \(d\) with multiplier \(a\) is conjugate, by an element of \(U\), to the scalar substitution \(\sigma_a(t)=at\): set
\[
 y=\frac1d\sum_{i=0}^{d-1}a^{-i}s^i(t).
\]
The leading coefficient of \(y\) is one, and \(s(y)=ay\), proving that \(y\) is a valid new coordinate. The centralizer \(C_U(\sigma_a)\) consists exactly of \(u(t)=t+\sum_{j=1}^{h_d}b_jt^{1+jd}\), hence has order \(q^{h_d}\). Conjugation acts transitively on possible \(s\), and the canonical decomposition of step 1 gives a bijection between automorphisms with multiplier \(a\) and pairs \((s,u)\) where \(u\in C_U(s)\). Every \(s\) has equally many commuting \(u\). Consequently the normalized coefficients \(b_j\) are jointly uniform over \(\mathbb F_q^{h_d}\).

**3. Fixed subalgebra.** The commuting operators \(s\) and \(u\) have orders dividing coprime integers \(d,p\). Their common fixed space equals that of \(su\): choose integer exponents expressing each factor as a power of the product, or use the cyclic group of coprime-order factors. In normalized coordinates, the \(\sigma_a\)-fixed space is
\[
 V=\operatorname{span}_{\mathbb F_q}\{1,t^d,t^{2d},\ldots,t^{L_dd}\}.
\]
For \(u=1\), the full \(V\) is fixed. Otherwise, let \(j\) be the smallest index with \(b_j\ne0\). For each \(k\ge1\) with \((k+j)d<n\), the first nonzero term of \(u(t^{kd})-t^{kd}\) is \((kd)b_jt^{(k+j)d}\). Its coefficient is nonzero because \(p>n>kd\), and different \(k\) give distinct leading degrees. Thus these rows are linearly independent, while all \(k\) with \(k+j>L_d\) are fixed. The fixed space is exactly the asserted span with dimension \(1+j\); it is a subalgebra because it is a fixed ring. This verifies all boundary values, including \(h_d=0\) and \(L_d=h_d\).

**4. Counts and Burnside.** For \(1\le j\le h_d\), exactly \((q-1)q^{h_d-j}\) centralizer choices have first nonzero coefficient at index \(j\); one choice has all coefficients zero. Each choice occurs for \(q^{n-2-h_d}\) conjugates of \(s\). Multiply to obtain the two asserted multiplicities, whose sum over cases is \(q^{n-2}\) for each \(a\). There are \(\varphi(d)\) elements of order \(d\) in \(\mathbb F_q^\times\). Each automorphism fixes \(q^{R(\phi)}\) elements of \(A\), so summing this statistic and dividing by \(|\operatorname{Aut}(A)|\) gives the stated orbit formula.

## Verification
The accompanying `verify.py` works directly with the substitution matrices of automorphisms, computes the rank of \(\phi-I\) over each tested prime field, and compares the complete fixed-dimension histogram to the formula. Exhaustive configurations were \((q,n)=(5,2),(5,3),(5,4),(7,3),(7,4),(7,5),(7,6),(11,3),(11,4)\). Every histogram and group-size check succeeded. For example, \((q,n)=(5,4)\) gives rank-dimension multiplicities \(\{1:50,2:45,3:4,4:1\}\); \((7,4)\) gives \(\{1:98,2:189,3:6,4:1\}\). Reproduce using `python3 verify.py`. These computations directly test finite fields of **prime** order only; the proof establishes the statement for all prime powers of characteristic \(p>n\). Finite checks are not proofs for arbitrary \(n\).

## Relationship to prior work
Díaz, Liendo, Manzano-Flores, and Regeta (arXiv:2408.02197, first posted 2024-08-05) analyze automorphism groups of zero-dimensional monomial algebras over characteristic-zero fields using derivations and root groups. Díaz and Lucchini Arteche (arXiv:2409.15081, first posted 2024-09-23) prove automorphism-group rigidity for local finite monomial algebras, also in characteristic zero. Their group-theoretic foundations and classical tame finite-order linearization are not claimed as new here. The present characteristic-\(p>n\) finite-field result refines the one-variable automorphism group by a **complete conditional fixed-subalgebra dimension law**, its embedded ring forms, and an orbit-count consequence. Classical univariate formal-power-series conjugacy results may imply parts of the orbit statement; their full relationship is an outstanding priority risk. No claim of proven worldwide novelty or independent verification is made.

## Limitations
The tame inequality \(p>n\) is essential to this proof, and analogous formulas are not asserted for small characteristic. The theorem concerns one-variable truncated polynomial algebras and fixed subrings under individual algebra automorphisms; not all local rings or general conjugacy classifications. The result does not establish uniqueness of this formulation in published literature. The computational verifier is exhaustive only in the listed prime-field dimensions.

## References
1. R. Díaz, Á. Liendo, G. Manzano-Flores, A. Regeta, *The Automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197 (first posted 2024-08-05), https://arxiv.org/abs/2408.02197.
2. R. Díaz and G. Lucchini Arteche, *Finite monomial algebras are determined by their automorphism group*, arXiv:2409.15081 (first posted 2024-09-23), https://arxiv.org/abs/2409.15081.
3. H. D. Nguyen, *The right classification of univariate power series in positive characteristic*, arXiv:1210.2868, https://arxiv.org/abs/1210.2868 (related right-equivalence classification; full comparison remains open).
4. D. Franco-Muñoz, *Subalgebras of Finite-Dimensional Algebras*, arXiv:1812.03576, https://arxiv.org/abs/1812.03576 (distinct subalgebra-enumeration context).
