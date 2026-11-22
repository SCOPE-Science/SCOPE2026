# Prime-order Frobenius actions on extraspecial groups: exact counts and conjugacy types

## Finding
Let \(p\) and \(\ell\) be primes with \(\ell\ge3\), let \(n\ge1\), and let \(G\) be an extraspecial group of order \(p^{2n+1}\). Let \(N_{\ell}(G)\) count automorphisms of **exact order** \(\ell\) having no fixed element other than the identity. Such automorphisms are precisely actions by a specified generator of a cyclic prime-order Frobenius complement on \(G\).

If \(G\) has exponent \(p^2\), or if \(p=2\), or if \(\ell\nmid(p-1)\), then \(N_{\ell}(G)=0\). In the remaining case, \(p\) is odd, \(G\) has exponent \(p\), and \(\ell\mid(p-1)\). Put \(m=(\ell-3)/2\) and
\[
S_d(p)=p^{d^2}\prod_{i=1}^d(p^{2i}-1),\quad
L_d(p)=\prod_{j=0}^{d-1}(p^d-p^j),\quad S_0(p)=L_0(p)=1.
\]
Then the **exact count** is
\[
\boxed{N_{\ell}(G)=(\ell-1)p^{2n}S_n(p)
\sum_{\substack{b+a_1+\cdots+a_m=n\\b,a_1,\ldots,a_m\ge0}}
\frac{1}{S_b(p)\prod_{j=1}^m L_{a_j}(p)}.}
\]
There are exactly
\[
\boxed{(\ell-1)\binom{n+m}{m}}
\]
conjugacy classes of these automorphisms in \(\operatorname{Aut}(G)\). More precisely, their conjugacy classes are in bijection with a primitive \(\ell\)-th root \(\mu\in\mathbb F_p^\times\) and an ordered nonnegative tuple \((b,a_1,\ldots,a_m)\) summing to \(n\). Each class has \(p^{2n}S_n(p)/(S_b(p)\prod_jL_{a_j}(p))\) elements.

At \(\ell=3\), this reduces for every \(n\ge1\) to exactly \(2p^{2n}\) fixed-point-free automorphisms of order three, in two conjugacy classes, when \(p\equiv1\pmod3\), and none otherwise. At \(\ell=5,n=1\), the nonzero count is \(4p^2(1+p(p+1))\). In fact, the exponent-\(p^2\) extraspecial groups admit **no fixed-point-free automorphism of any order**, not merely none of prime order.

## Assumptions and scope
An extraspecial group here is a finite nonabelian \(p\)-group with \(Z(G)=G'=\Phi(G)\cong C_p\). Its quotient \(V=G/Z(G)\) has dimension \(2n\) over \(\mathbb F_p\). The commutator induces a nondegenerate alternating form \(\omega:V\times V\to\mathbb F_p\), after choosing a generator of the center. For \(p\) odd there are two extraspecial isomorphism types, of exponent \(p\) and \(p^2\). The prime \(\ell\) is an order of an automorphism, not the defining prime \(p\). Every automorphism is counted as a distinct map on the fixed group; no quotient by conjugacy is taken in \(N_{\ell}(G)\). The separate class count is conjugacy **inside** \(\operatorname{Aut}(G)\), not isomorphism of unoriented semidirect products.

The group-order notation \(S_d(p)\) means \(|\operatorname{Sp}_{2d}(\mathbb F_p)|\), while \(L_d(p)=|\operatorname{GL}_{d}(\mathbb F_p)|\). Empty products are one, including \(m=0\).

## Proof
**1. The multiplier obstruction.** Every automorphism \(\alpha\) acts on \(Z(G)\) by a multiplier \(\mu\in\mathbb F_p^\times\), and induces \(M\in\operatorname{GSp}(V,\omega)\) satisfying
\[
\omega(Mv,Mw)=\mu\,\omega(v,w).
\]
If \(\alpha\) has no nonidentity fixed points, then \(\mu\ne1\), since otherwise it fixes all of \(Z(G)\). If \(\alpha^\ell=1\), then \(\mu^\ell=1\); as \(\ell\) is prime and \(\mu\ne1\), \(\mu\) is primitive of order \(\ell\). Hence \(\ell\mid(p-1)\). When \(p=2\), every automorphism fixes the unique nontrivial central element, so none is fixed-point-free.

**2. Exponent-\(p^2\) obstruction, in every order.** Suppose \(p\) is odd and \(G\) has exponent \(p^2\). The \(p\)-th power of a lift of \(v\in V\) defines a nonzero \(\mathbb F_p\)-linear functional \(\lambda:V\to\mathbb F_p\): this is well-defined because the center has exponent \(p\), and linear because \(G\) has nilpotency class two and \(p\) is odd. Automorphism equivariance yields
\[
\lambda(Mv)=\mu\lambda(v).
\]
Write \(\lambda(v)=\omega(u,v)\) for a unique \(u\in V\setminus\{0\}\). By the similitude identity,
\[
\omega(u,Mv)=\mu\,\omega(M^{-1}u,v),
\]
so nondegeneracy and the displayed equivariance imply \(M^{-1}u=u\). If \(\mu=1\), the nontrivial center is fixed pointwise. If \(\mu\ne1\), any group element over the nonzero fixed quotient vector \(u\) can be multiplied by a uniquely determined central element to become fixed by \(\alpha\) (because the central correction changes by \(\mu-1\)). Thus no automorphism of the exponent-\(p^2\) type can be fixed-point-free, regardless of its order.

**3. Exponent-\(p\) coordinates and fixed-point criterion.** For odd \(p\), the exponent-\(p\) type has a model
\[
G=V\times\mathbb F_p,\qquad
(v,z)(w,t)=(v+w,z+t+\tfrac12\omega(v,w)).
\]
Every automorphism is uniquely
\[
\alpha_{M,\tau}(v,z)=(Mv,\mu z+\tau(v)),
\quad M\in\operatorname{GSp}(V,\omega),\quad \tau\in V^*,
\]
where \(\mu\) is the similitude multiplier. Indeed the commutator forces the similitude property, the multiplication law forces \(\tau\) to be linear, and conversely every such pair gives an automorphism. Thus every \(M\) has precisely \(p^{2n}\) lifts. For \(\mu\ne1\), the automorphism has a nonidentity fixed element exactly when \(M\) has eigenvalue one: a nonzero fixed quotient vector determines one fixed central coordinate; if no such quotient vector exists the only fixed group element is the identity.

**4. Cyclotomic eigenvalue pairing.** Suppose \(\alpha\) is fixed-point-free of order \(\ell\). Then \(M^\ell=I\), \(\mu\) has exact order \(\ell\), and \(M\) has no eigenvalue one. Since \(\ell\mid(p-1)\), the polynomial \(X^\ell-1\) splits into distinct linear factors over \(\mathbb F_p\), so \(M\) is diagonalizable. Write \(V_i\) for the \(\mu^i\)-eigenspace, with \(i\in\mathbb Z/\ell\mathbb Z\). The similitude identity gives
\[
\omega(V_i,V_j)=0\quad\text{unless}\quad i+j\equiv1\pmod\ell.
\]
Nondegeneracy forces \(\dim V_i=\dim V_{1-i}\), with the induced pairing perfect. Since \(V_0=0\), also \(V_1=0\). Among the remaining \(\ell-2\) exponents there is one fixed point of the involution \(i\mapsto1-i\), namely \(i=(\ell+1)/2\), whose eigenspace is symplectic of even dimension \(2b\). The other exponents form \(m=(\ell-3)/2\) pairs; write the paired dimensions as \((a_1,a_1),\ldots,(a_m,a_m)\). Hence \(b+\sum a_j=n\).

Conversely, for any primitive \(\mu\) and any such tuple, take an orthogonal direct sum of a symplectic space of dimension \(2b\) on which \(M\) is scalar \(\mu^{(\ell+1)/2}\), and \(m\) paired symplectic hyperbolic blocks on which \(M\) has scalars \(\mu^i\), \(\mu^{1-i}\). This gives \(M\in\operatorname{GSp}\) with multiplier \(\mu\), \(M^\ell=I\), and eigenvalue one absent. The forbidden eigenvalue \(\mu\) is also absent. For any linear functional \(\tau\), the central part of \(\alpha_{M,\tau}^\ell\) vanishes because
\[
\sum_{j=0}^{\ell-1}\mu^{\ell-1-j}\tau M^j
=\tau\,(M^\ell-\mu^\ell I)(M-\mu I)^{-1}=0.
\]
Thus every one of the \(p^{2n}\) lifts has exact order \(\ell\) (its central multiplier has this order) and is fixed-point-free.

**5. Orbit-stabilizer count and conjugacy.** With fixed \(\mu\) and dimensions \((b,a_1,\ldots,a_m)\), the symplectic group \(\operatorname{Sp}_{2n}(\mathbb F_p)\) acts transitively on the corresponding orthogonal eigen-decompositions, since all nondegenerate alternating forms of the required dimensions are equivalent. The stabilizer is
\[
\operatorname{Sp}_{2b}(\mathbb F_p)\times
\prod_{j=1}^m\operatorname{GL}_{a_j}(\mathbb F_p).
\]
Therefore there are exactly \(S_n(p)/(S_b(p)\prod_jL_{a_j}(p))\) quotient matrices in this stratum. The linear central shifts account for an additional \(p^{2n}\) automorphisms. All shifts above one \(M\) are conjugate by central automorphisms \((v,z)\mapsto(v,z+s(v))\): conjugation changes \(\tau\) by \(s(M-\mu I)\), and \(M-\mu I\) is invertible. Every fixed-\(\mu\), fixed-dimension stratum is therefore one \(\operatorname{Aut}(G)\)-conjugacy class. Different multipliers or eigenspace dimensions are invariant under conjugation and cannot merge. There are \(\ell-1\) primitive multipliers and \(\binom{n+m}{m}\) nonnegative solutions \((b,a_1,\ldots,a_m)\). Counting orbit sizes and classes proves both formulas.

**6. Ordered product law.** Each such automorphism obeys
\[
g\,\alpha(g)\,\alpha^2(g)\cdots\alpha^{\ell-1}(g)=1
\quad\text{for all }g\in G.
\]
Indeed, the map \(h\mapsto h^{-1}\alpha(h)\) is injective because its equal values imply an \(\alpha\)-fixed quotient of the two inputs, and is therefore surjective on the finite group. Writing every \(g=h^{-1}\alpha(h)\), the ordered product telescopes to \(h^{-1}\alpha^\ell(h)=1\). This is a consequence, not an additional hypothesis.

## Verification
The accompanying standalone `check_prime_cyclotomic.py` requires only Python's standard library. It enumerates all invertible \(2\times2\) quotient matrices with the required multiplier, prime order and fixed-space conditions at \((p,\ell)=(5,3),(7,3),(11,5),(13,3),(29,7)\). The exact matrix counts are respectively \(0,2,532,2,10446\), giving lifted counts \(0,98,64372,338,8785086\). These agree with the rank-one formula. For \((7,3)\), it checks all \(98\) lifted automorphisms on every group element; for \((11,5)\), it tests \(16\) explicitly selected lifts on all \(11^3\) elements. Each tested map has exact order \(\ell\), no nonidentity fixed point, and the required noncommutative ordered product identity. The checker outputs `PRIME_CYCLOTOMIC_EXTRASPECIAL_CHECKS_OK`. This finite testing does not establish the all-rank theorem; steps 1–6 do.

## Relationship to prior work
Al-Raisi and Shahryari (2026) investigate split Frobenius groups and properties of their fixed-point-free complement actions. Their results motivate classifying the possible prime-order complements for a particular natural nonabelian kernel; their paper does not enumerate fixed-point-free automorphisms of extraspecial groups. Kumar and Pradhan (2019), building on Winter's classical work, determine automorphism normal forms for both extraspecial types; in particular, their symplectic-similitude parametrization is used in step 3. They do not count the exact prime-order fixed-point-free strata or give the above conjugacy-class census and exponent-type dichotomy. Wall's semisimple symplectic conjugacy theory (2015 arXiv posting of an older note) provides a broad matrix-conjugacy method, but treats multiplier-one symplectic elements rather than the nontrivial-multiplier action and its extraspecial lifts here. The present result combines the group multiplier, exponent obstruction, spectral pairing, full orbit enumeration and central-lift conjugation.

A nearby published record, *Exact Reidemeister-number distribution for automorphisms of the odd Heisenberg group* (2026, public record `0edb94bdc251`), gives a complete twisted-conjugacy histogram for all automorphisms only in order \(p^3\); its fixed-point-free component aggregates all automorphism orders rather than restricting to exact prime order \(\ell\). Another published record, *Every subgroup of an odd-exponent extraspecial group is an automorphism fixed subgroup* (2026), concerns which subgroups can be a fixed set, not the number and conjugacy classes of fixed-point-free prime-order automorphisms. Neither provides this count.

## Limitations
The exact formulas concern **odd prime** complement orders, not composite orders or complement groups with several generators. The conjugacy classes distinguish an oriented generator of the cyclic complement; they are not asserted to equal isomorphism classes of the resulting semidirect-product groups. The formulas concern group automorphisms, not arbitrary endomorphisms, and the group-order argument uses finite fields of prime order (the extraspecial defining field). The exponent-\(p^2\) obstruction applies to automorphisms of every order, but no classification of their fixed-point subgroup sizes is claimed. Classic finite classical-group conjugacy literature may yield an equivalent specialization after a nontrivial reduction; no earlier explicit all-rank extraspecial prime-order spectrum was identified in the checked materials, and historical priority remains subject to specialist comparison.

## References
1. O. Al-Raisi and M. Shahryari, *Split Frobenius Groups, Equational Domains, \(\mathfrak XT\)- and \(CS\mathfrak X\)-groups*, arXiv:2610.32643v1, first public 2026-10-23, https://arxiv.org/abs/2610.32643.
2. C. P. Anil Kumar and S. S. Pradhan, *On the Endomorphism Semigroups of Extra-special \(p\)-groups and Automorphism Orbits*, arXiv:1908.00331v2 (2019), especially Theorems Ω and Σ, https://arxiv.org/abs/1908.00331.
3. G. E. Wall, *The semisimple conjugacy classes in the symplectic groups*, arXiv:1512.04520v1 (2015), https://arxiv.org/abs/1512.04520.
4. *Exact Reidemeister-number distribution for automorphisms of the odd Heisenberg group*, published mathematical record `0edb94bdc251` (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-reidemeister-number-distribution-for-automorphisms-of-the--0edb94bdc251.
