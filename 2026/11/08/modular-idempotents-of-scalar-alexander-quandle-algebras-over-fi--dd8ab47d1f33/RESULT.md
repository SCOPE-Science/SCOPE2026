# Modular idempotents of scalar Alexander-quandle algebras over finite fields

## Finding

Let \(p\) be a prime, \(s,m\ge 1\), \(F=\mathbb F_{p^s}\), and \(K=\mathbb F_{p^m}\). Choose \(\alpha\in F\setminus\{0,1\}\), put \(\beta=1-\alpha\), and give the additive group of \(F\) the scalar Alexander-quandle operation
\[
 x*y=\alpha x+\beta y.
\]
The \(K\)-quandle algebra \(A=K[\operatorname{Alex}(F,\alpha)]\) has basis \(e_x\) for \(x\in F\), with \(e_xe_y=e_{x*y}\); write \(\operatorname{Idem}(A)=\{u\in A:u^2=u\}\), including zero. Set
\[
 S(F,\alpha)=\{k\in\{0,\ldots,p^s-2\}:\alpha^k+\beta^k=1\text{ in }F\},
 \quad d(F,\alpha)=|S(F,\alpha)|.
\]
Then the exact idempotent count is
\[
 \boxed{|\operatorname{Idem}(A)|=1+|K|^{d(F,\alpha)}.}
\]
The nonzero idempotents form a subquandle under the original bilinear product, and are isomorphic to an explicitly defined finite Alexander quandle of \(K\)-dimension \(d(F,\alpha)\): let \(H=F^\times\), let \(\rho_t\) denote left translation by \(t\) on the group algebra \(K[H]\), and put
\[
 W=\ker(\rho_\alpha+\rho_\beta-\operatorname{id}:K[H]\to K[H]).
\]
With \(u\circ v=\rho_\alpha(u)+\rho_\beta(v)\), the quandle \(\operatorname{Idem}(A)\setminus\{0\}\) is isomorphic to \((W,\circ)\). This quandle isomorphism is generally noncanonical; the ordinary addition on \(W\) is not the vector addition in the original quandle algebra. Its isomorphism type is explicit from the commuting actions of \(\rho_\alpha\) and \(\rho_\beta\).

Equivalently, if \(h\) generates \(H\), and \(\alpha=h^a\), \(\beta=h^b\), then
\[
 d(F,\alpha)=\deg\gcd\bigl(T^{p^s-1}-1,\ T^a+T^b-1\bigr)
 \quad\text{over }K.
\]
Here \(d\ge s\), because the distinct exponents \(1,p,p^2,\ldots,p^{s-1}\) belong to \(S(F,\alpha)\). For \(K=\mathbb F_p\), the original \(p^s\) basis idempotents exhaust the nonzero idempotents precisely when \(d=s\).

For a concrete characteristic-two contrast, construct \(F=\mathbb F_{16}=\mathbb F_2[t]/(t^4+t+1)\) and use coefficients \(K=\mathbb F_2\). At \(\alpha=t\), \(d=4\) and there are exactly \(17\) idempotents; at \(\alpha=t^2+t\), \(d=10\) and there are exactly \(1025\). The same underlying additive set therefore admits Latin Alexander-quandle operations with sharply different modular idempotent growth. For \(F=\mathbb F_7\), \(K=\mathbb F_7\), the non-midpoint parameter \(\alpha=3\) gives \(d=2\) and exactly \(50\) idempotents, whereas \(\alpha=2\) gives \(d=1\) and exactly \(8\).

## Assumptions and scope

All fields are finite and have common characteristic \(p\). Neither \(\alpha\) nor \(\beta\) is zero, ensuring that the quandle is Latin and both induced group-ring endomorphisms are automorphisms. For \(F=\mathbb F_2\) no such parameter exists; all other finite fields are allowed, including characteristic two. The result counts algebra elements, not idempotent isomorphism classes under algebra automorphisms. The ordinary associative group-ring multiplication below is distinguished from the generally nonassociative quandle-algebra product.

## Proof

**1. Transport to the ordinary group algebra.** Let \(G=(F,+)\), and let \(R=K[G]\) be its ordinary commutative associative group algebra, with basis \(X^x\), product \(X^xX^y=X^{x+y}\), and augmentation \(\varepsilon(\sum c_xX^x)=\sum c_x\). For \(t\in H\), define the algebra automorphism \(\rho_t(X^x)=X^{tx}\). Then the \(K\)-linear identification \(e_x\leftrightarrow X^x\) transports the quandle-algebra product to
\[
 u\star v=\rho_\alpha(u)\rho_\beta(v),
\]
where multiplication on the right is ordinary associative multiplication in \(R\). Indeed the transported product of two basis elements is \(X^{\alpha x+\beta y}\). This also verifies that the new product is bilinear and that the stated idempotent equation matches the original algebra.

**2. Eliminate augmentation-zero idempotents.** The ordinary augmentation ideal \(I=\ker\varepsilon\) is nilpotent: choosing an \(\mathbb F_p\)-basis \(g_1,\ldots,g_s\) of \(G\), the group ring is \(R\cong K[z_1,\ldots,z_s]/(z_1^p,\ldots,z_s^p)\), with \(z_i=X^{g_i}-1\), and \(I=(z_1,\ldots,z_s)\). In particular, \(I^{s(p-1)+1}=0\). If \(u\star u=u\), the augmentation satisfies \(\varepsilon(u)^2=\varepsilon(u)\), hence \(\varepsilon(u)=0\) or \(1\). If \(\varepsilon(u)=0\), then \(u\in I\), and
\[
 u=\rho_\alpha(u)\rho_\beta(u)\in I^2.
\]
Inductively \(u\in I^{2^j}\) for every \(j\ge0\), because both automorphisms preserve \(I^i\). Nilpotence forces \(u=0\).

**3. Turn augmentation-one idempotency into a linear equation.** The group \(U=1+I\) of principal units consists of precisely the augmentation-one elements of \(R\). Every \(v\in I\) has \(v^p=0\): writing \(v=\sum_{g\ne0}c_g(X^g-1)\) and using the characteristic-\(p\) Frobenius identity yields \(v^p=\sum_{g\ne0}c_g^p(X^{pg}-1)=0\). Thus \((1+v)^p=1\), so \(U\), with ordinary multiplication as its group law, is an elementary abelian \(p\)-group and hence an \(\mathbb F_p\)-vector space. The automorphisms \(\rho_t\) are \(\mathbb F_p\)-linear maps on this vector space. Since \(U\) is abelian, the map
\[
 \Theta(u)=\rho_\alpha(u)\rho_\beta(u)
\]
is a group endomorphism and corresponds to the \(\mathbb F_p\)-linear map \(\rho_\alpha+\rho_\beta\) when the vector-space addition is the multiplication in \(U\). Therefore the nonzero \(\star\)-idempotents are exactly
\[
 E=\ker(\rho_\alpha+\rho_\beta-\operatorname{id}:U\to U).
\]
The kernel is a subgroup of \(U\); the operators \(\rho_\alpha\) and \(\rho_\beta\) commute with its defining endomorphism and preserve \(E\). On \(E\), their sum is the identity, so the restricted product \(u\star v=\rho_\alpha(u)\rho_\beta(v)\) gives an Alexander quandle.

**4. Equivariant filtration identifies the representation.** The finite group \(H=F^\times\) acts on both \(U\) and \(I\) via the \(\rho_t\). Put \(U_j=1+I^j\). There are natural \(H\)-equivariant isomorphisms of \(\mathbb F_p\)-vector spaces
\[
 U_j/U_{j+1}\cong I^j/I^{j+1},\qquad (1+v)U_{j+1}\longmapsto v+I^{j+1},
\]
for \(j\ge1\), since a product \((1+v)(1+w)\) differs from \(1+v+w\) by an element of \(I^{j+1}\). As \(|H|=p^s-1\) is prime to \(p\), Maschke's theorem makes every finite-dimensional \(\mathbb F_p[H]\)-module semisimple. Consequently the filtrations split as \(H\)-modules, giving an \(\mathbb F_p[H]\)-module isomorphism
\[
 U\cong\bigoplus_{j\ge1}U_j/U_{j+1}
 \cong\bigoplus_{j\ge1}I^j/I^{j+1}\cong I.
\]
It intertwines all \(\rho_t\), and hence the kernel operator in Step 3. This proves that \(E\) is isomorphic as a quandle to the kernel of \(\rho_\alpha+\rho_\beta-\operatorname{id}\) on \(I\).

**5. Regular character spectrum and the formula.** The \(K\)-vector space \(I\) has basis \(\{X^x-1:x\in F^\times\}\). The action of \(H\) permutes this basis freely and transitively, so \(I\cong K[H]\) as \(K[H]\)-modules. The permutation representation is regular, with one copy of each multiplicative character after extending scalars to an algebraic closure. These characters are exactly
\[
 \chi_k(t)=t^k,\qquad 0\le k\le p^s-2,
\]
using an embedding of \(F\) into the algebraic closure of \(K\). On the \(k\)-character line, the kernel operator acts by the scalar \(\alpha^k+\beta^k-1\). Thus its nullity is exactly \(d(F,\alpha)\). Field extension preserves matrix rank, so \(\dim_K W=d(F,\alpha)\), \(\dim_{\mathbb F_p}E=m d(F,\alpha)\), and \(|E|=p^{m d}=|K|^d\). Adding the unique zero idempotent proves the count and the quandle isomorphism.

For the gcd formula, choose a generator \(h\) of \(H\). The regular representation is \(K[T]/(T^{p^s-1}-1)\), where \(\rho_h\) is multiplication by \(T\). The kernel of multiplication by \(T^a+T^b-1\) has dimension equal to the degree of its gcd with \(T^{p^s-1}-1\), because the latter polynomial is separable (its degree is prime to \(p\)). Finally \(\alpha^{p^j}+\beta^{p^j}=(\alpha+\beta)^{p^j}=1\) for \(0\le j<s\). These exponents are distinct and less than \(p^s-1\) whenever the parameter set is nonempty, proving \(d\ge s\).

**6. Explicit examples.** In \(F=\mathbb F_2[t]/(t^4+t+1)\), direct finite-field exponent calculations yield
\[
 S(F,t)=\{1,2,4,8\},\qquad
 S(F,t^2+t)=\{1,2,4,5,7,8,10,11,13,14\}.
\]
The total idempotent counts over \(K=\mathbb F_2\) are therefore \(17\) and \(1025\), respectively. In \(F=K=\mathbb F_7\), \(S(F,2)=\{1\}\) and \(S(F,3)=\{1,5\}\), giving \(8\) and \(50\). Both nontrivial counts were independently checked by exhaustive enumeration of coefficients.

## Verification

Run `python3 verify.py` from the extracted package. It uses only the Python standard library. The file `verification_output.txt` records 24 exhaustive cases: prime fields of orders \(3,5,7\), scalar parameters on the additive field of order \(9\) with \(\mathbb F_3\)-coefficients, and characteristic-two fields of orders \(4,8,16\) with \(\mathbb F_2\)-coefficients. The checker enumerates each coefficient tuple and directly tests all idempotent equations, independently of the representation-theoretic proof. The output ends with `VERIFY_OK checked=24`. The proof above, not finite extrapolation, establishes the theorem for all permitted finite fields and parameters.

## Relationship to prior work

The ordinary group-ring transport \(u\star v=\rho_\alpha(u)\rho_\beta(v)\) is recorded in Zhang, *Group-ring methods for Alexander quandle rings* (arXiv:2610.08204, Proposition 2.1). That article's idempotent classification in Theorem 5.2 concerns **integral** coefficients and **commutative** Alexander quandles; neither its augmentation-power formula nor the integral classification gives the modular cardinalities above. Elhamdadi, Ta, and Virgin (arXiv:2609.03799, Lemma 6.2) derive a superficially similar character condition for complex Fourier data of **integral** quandle idempotents, with additional evenness and root-of-unity constraints; those conditions do not compute the modular principal-unit kernel. Sangare and Ta (arXiv:2608.01550) treat ordered commutative and characteristic-two commutative settings, not the general scalar modular law. Bardakov and Elhamdadi (arXiv:2601.07057) motivate the idempotent problem without deriving these finite-field counts.

A previously obtained midpoint-quandle result concerns the special case \(\alpha=\beta=1/2\) over elementary abelian groups in odd characteristic. The present theorem includes but is not limited to that case: it treats all nonzero scalar pairs, all finite fields as underlying additive groups, and characteristic two, and distinguishes parameters by the full character condition. For instance, the two characteristic-two algebras in Step 6 are both outside the midpoint setting. The reviewed searches did not locate a prior complete scalar modular count or structural classification. This is a qualified originality assessment, not proof of historical uniqueness.

## Limitations

The theorem assumes that the underlying additive group is the additive group of a finite field and the quandle endomorphism is multiplication by a scalar. It does not classify arbitrary nonscalar Alexander automorphisms or coefficient characteristic different from that of \(F\). The isomorphism \(E\cong W\) is not canonical because it uses a splitting of a filtration. The exact formula may require computing discrete logarithms or a polynomial gcd; it does not give a uniformly small closed expression for \(d(F,\alpha)\). Finite verification covers only the listed cases. Historical priority requires independent scrutiny of the surrounding literature.

## References

1. Zhi-Lin Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204v1, first publicly posted 2026-10-06, https://arxiv.org/abs/2610.08204.
2. Mohamed Elhamdadi, Luc Ta, and Bryce Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799v1, first publicly posted 2026-09-03, https://arxiv.org/abs/2609.03799.
3. Birama Sangare and Luc Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550v1, first publicly posted 2026-08-03, https://arxiv.org/abs/2608.01550.
4. Valeriy Bardakov and Mohamed Elhamdadi, *Idempotents and Powers of Ideals in Quandle Rings*, arXiv:2601.07057v1, first publicly posted 2026-01-11, https://arxiv.org/abs/2601.07057.
5. Gregory Churchill, Indu Rasika Churchill, Neranga Fernando, and Bhitali Kousik, *A further study of quandles and quandle rings*, arXiv:2608.09149v2, https://arxiv.org/abs/2608.09149.
