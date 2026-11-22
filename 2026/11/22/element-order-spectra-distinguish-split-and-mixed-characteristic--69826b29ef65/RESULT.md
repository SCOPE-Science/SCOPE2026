# Element-order spectra distinguish split and mixed-characteristic square-zero affine groups

## Finding

Let \(R\) be a finite commutative local ring whose nonzero maximal ideal \(\mathfrak m\) satisfies \(\mathfrak m^2=0\), with residue field \(\mathbb F_q\) of **odd** characteristic \(p\), \(q=p^f\), and \(d=\dim_{\mathbb F_q}\mathfrak m\ge2\). Write \(G(R)=R^+\rtimes R^\times\) for the invertible affine group acting by \(x\mapsto ax+b\). For every positive integer \(k\), let \(e_k(R)\) be the number of elements of order exactly \(k\), and let \(E_R(z)=\sum_{k\ge1}e_k(R)z^k\). Put \(s=q^{d+1}\).

Every such ring has characteristic either \(p\) or \(p^2\). Its **complete element-order polynomial** is
\[
E_R(z)=z+\begin{cases}
(q^{2d+1}-1)z^p,&\operatorname{char}R=p,\\
(q^{2d}-1)z^p+(q-1)q^{2d}z^{p^2},&\operatorname{char}R=p^2
\end{cases}
+\sum_{\substack{\ell\mid(q-1)\\\ell>1}}
\varphi(\ell)q^{d+1}\bigl(z^\ell+(q^d-1)z^{p\ell}\bigr).
\]
No other element orders occur. In particular, the order spectra depend only on \((q,d,\operatorname{char}R)\), independently of whether the ring is split or of the additive structure beyond its characteristic.

The order distributions can distinguish affine groups having identical **full conjugacy-class-size and ordinary irreducible-character-degree multisets**: for every odd prime \(p\) and \(d\ge2\), the affine groups of \(\mathbb F_p[x_1,\ldots,x_d]/(x_ix_j:1\le i,j\le d)\) and of \((\mathbb Z/p^2\mathbb Z)[x_2,\ldots,x_d]/(px_i,x_ix_j:2\le i,j\le d)\) have matching class-size and character-degree multisets by the orbit descriptions below, yet the mixed-characteristic group has exactly \((p-1)p^{2d}\) elements of order \(p^2\), while the split group's Sylow-\(p\) subgroup has exponent \(p\). Thus they are nonisomorphic.

## Assumptions and scope

The ring is finite, commutative, unital, and local with \(\mathfrak m\ne0\), \(\mathfrak m^2=0\), odd residue characteristic, and \(d\ge2\). For a nonzero radical, \(p\in\mathfrak m\), so \(p^2=0\) in the ring; therefore \(\operatorname{char}R\in\{p,p^2\}\). The polynomial counts group elements, not conjugacy classes or cyclic subgroups. All powers and element orders are taken in the group \(G(R)\). The result is equally true for \(d=1\), but that principal-radical boundary is a previously studied case and is not claimed as new.

## Proof

The group multiplication is \((b,a)(c,u)=(b+ac,au)\). Since \(\mathfrak m^2=0\), \(1+\mathfrak m\) is an elementary abelian group of order \(q^d\), and the exact sequence \(1\to1+\mathfrak m\to R^\times\to\mathbb F_q^\times\to1\) splits uniquely as a direct product of the \(p\)-subgroup and a cyclic subgroup \(T\) of order \(q-1\). This follows from the elementary splitting of finite abelian groups into their Sylow subgroups. Thus every unit has a unique expression \(a=t(1+w)\) with \(t\in T\) and \(w\in\mathfrak m\).

If \(t\ne1\), then \(1-a\) is a unit. Conjugation by a translation sends \((b,a)\) to \((0,a)\), so its order is the order of \(a\). Since \(t\) has order \(\ell>1\) coprime to \(p\), \((1+w)\) has order \(p\) if \(w\ne0\), and order one otherwise. The orders are therefore respectively \(\ell\) and \(p\ell\). For each \(\ell>1\) dividing \(q-1\), exactly \(\varphi(\ell)\) choices of \(t\) have order \(\ell\), each with \(q^{d+1}\) choices of \(b\) and \(q^d\) choices of \(w\). This gives both coefficients in the sum, with no double counting.

If \(t=1\), write \(a=1+w\). The multiplication rule gives by induction
\[
(b,1+w)^n=\bigl(nb+\tbinom n2 wb,\;1+nw\bigr),
\]
because \(w^2=0\). Since \(p\) is odd, \(pw=0\) and \(\binom p2 wb=0\); hence \((b,1+w)^p=(pb,1)\). If \(\operatorname{char}R=p\), all such elements have order dividing \(p\). If \(\operatorname{char}R=p^2\), then \(pb\ne0\) exactly when \(b\) is a unit: its image is \((b\bmod\mathfrak m)(p\cdot1)\) in the one-dimensional nonzero \(\mathbb F_q\)-subspace \(pR\subseteq\mathfrak m\). There are \((q-1)q^d\) such units \(b\), and \(q^d\) possibilities for \(w\), yielding exactly \((q-1)q^{2d}\) order-\(p^2\) group elements. The remaining nonidentity elements with \(t=1\) have order exactly \(p\), giving the asserted respective \(p\)-coefficients. The identity occurs once. The two multiplier cases exhaust \(G(R)\).

For completeness, the standard class/degree equality used in the separation is ring-independent: for affine conjugacy, each multiplier \(a\) contributes unit-group orbits on \(R/(1-a)R\). The cases \(a-1\) invertible, zero, and nonzero in \(\mathfrak m\) give respectively one orbit, \(1+L_d+1\) orbits, and \(2+L_{d-1}\) orbits, with sizes determined only by \((q,d)\). For ordinary degrees, the abelian normal subgroup \(R^+\) and abelian quotient \(R^\times\) give the little-group classification: character orbits have sizes \(1\), \(q-1\), and \(q(q-1)\) with stabilizer multiplicities \(q^d(q-1)\), \(q^d\), and \(q^{d-1}L_d\). This can be checked by restricting additive characters to \(\mathfrak m\): its nonzero dual vectors form \(L_d\) scalar lines, and the principal units act transitively on the \(q\) extensions of a fixed nonzero radical character. Thus both complete classical spectra indeed agree for the two ring families independently of their additive exponents.

The count sums to \(q^{2d+1}(q-1)=|G(R)|\), because \(\sum_{\ell\mid(q-1),\ell>1}\varphi(\ell)=q-2\). The conclusion on nonisomorphism follows because group-element order is preserved by isomorphism, whereas the cited previous complete class-size and degree distributions for the corresponding upper-triangular groups descend to their affine direct factors: \(B_2(R)\cong R^\times\times G(R)\), with the central first factor abelian of the same order in both examples. No claim of novelty is made for those earlier class or character-degree distributions.

## Verification

The standalone dependency-free `verify.py` directly implements multiplication in split truncated polynomial rings and mixed-characteristic quotients \((\mathbb Z/p^2\mathbb Z)[x]/(px,x^2)\). It enumerates affine-group elements, computes their orders by repeated group composition, and compares each coefficient with the formula. It passed six configurations: split \((p,d)=(3,1),(3,2),(5,1),(5,2)\) and mixed characteristic \((3,2),(5,2)\). In the \((p,d)=(3,2)\) case the split order spectrum is \(z+27z^2+242z^3+216z^6\), and the mixed spectrum is \(z+27z^2+80z^3+216z^6+162z^9\). Run `python3 verify.py`; the final line is `VERIFY_OK`. Exhaustive small computations are corroboration only, not the infinite-family proof.

## Relationship to prior work

Caranti, Dalla Volta and Sala [1] establish radical-ring and affine-group correspondences, motivating affine groups built from finite local rings. Earlier square-zero triangular-group calculations [2] already supply exact conjugacy-class and irreducible-degree distributions of \(B_2(R)\); the affine-group analogues follow via the central direct product, so they are NOT claimed here. That record does not supply the **element-order** spectrum, nor does its complete class/degree distribution imply it: the paired families above share those distributions but have different element orders. The published full affine-monoid centralizer formulas of [3] and the chain-ring affine-group character table of [4] concern separate invariants. Standard decomposition of finite abelian unit groups, not invented theory, is used. The new exact count is specifically the all-parameter split-versus-mixed-characteristic order distribution and its separation of otherwise spectrally indistinguishable groups.

## Limitations

Only odd residue characteristic is covered; at residue characteristic two the binomial term changes the group-power formula. The ring must have square-zero radical, and the numerical invariants do not recover its entire isomorphism type. Full ordinary character tables, conjugacy orbit representatives and group isomorphism classifications are not claimed. The elementary order-spectrum calculation may have appeared implicitly in general literature on affine groups or class-two semidirect products, despite the comparisons performed here. No independent mathematical audit has been performed.

## References

[1] A. Caranti, F. Dalla Volta and M. Sala, *Abelian regular subgroups of the affine group and radical rings*, arXiv:math/0510166 (first public submission 8 October 2005), https://arxiv.org/abs/math/0510166 .

[2] *Conjugacy-class and ordinary character-degree spectra of upper triangular groups over square-zero finite local rings*, earlier result; the required equality is also reconstructed above so the present proof does not depend on external access.

[3] *Centralizer spectra of finite affine monoids distinguish local-ring geometry*, published record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-centralizer-spectra-of-finite-affine-monoids-distinguish-local-r--5531b23a5b4d .

[4] *Conjugacy and ordinary character spectra of affine groups over finite chain rings*, published record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-conjugacy-and-ordinary-character-spectra-of-affine-groups-over-f--0a4181d7ad6d .
