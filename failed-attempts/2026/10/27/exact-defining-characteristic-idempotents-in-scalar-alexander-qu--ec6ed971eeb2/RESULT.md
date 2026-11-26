# Exact defining-characteristic idempotents in scalar Alexander quandle algebras

## Finding
For every prime power \(q=p^e\ge 3\) and every \(a\in\mathbb F_q\setminus\{0,1\}\), let \(Q_a\) be the scalar Alexander quandle with \(x\triangleright y=ax+(1-a)y\). In the quandle algebra \(\mathbb F_q[Q_a]\), put
\[
 d_q(a)=\#\{j\in\{0,\ldots,q-2\}:a^j+(1-a)^j=1\}.
\]
Then the number of idempotents, including zero, is exactly
\[
 \boxed{\#\operatorname{Idem}(\mathbb F_q[Q_a])=1+q^{d_q(a)}.}
\]
Zero is the sole idempotent of augmentation zero; every nonzero idempotent has augmentation one. Under **ordinary additive-group-ring convolution**, the nonzero quandle-algebra idempotents constitute an elementary abelian \(p\)-group of order \(q^{d_q(a)}\). In particular \(d_q(a)\ge e\). For \(q=7\), \(a=2\) gives eight idempotents while \(a=4\) gives fifty.

## Assumptions and scope
The coefficient field and the underlying additive group are both those of the same finite field \(K=\mathbb F_q\). The operation on quandle basis vectors is \([x]\star[y]=[ax+(1-a)y]\) and extends \(K\)-bilinearly; the resulting quandle algebra is generally nonassociative. Its augmentation is \(\varepsilon(\sum_xc_x[x])=\sum_xc_x\). The group structure asserted above is for the **different, associative** convolution product associated with the additive group of \(K\), not for the quandle product \(\star\). The assumption \(a,1-a\ne0\) ensures the quandle is latin and ensures both scalar maps belong to \(K^\times\).

## Proof
1. Let \(A=(K,+)\) and \(R=K[A]\) be its ordinary commutative group algebra with convolution, denoted by juxtaposition. For \(c\in K^\times\), define the algebra automorphism \(T_c([x])=[cx]\). Directly on basis vectors, and hence on all elements,
\[
 u\star v=T_a(u)T_{1-a}(v).
\]
The common augmentation \(\varepsilon\) is multiplicative for either product. Any \(\star\)-idempotent has augmentation zero or one.

2. Let \(I=\ker\varepsilon\), the augmentation ideal of \(R\). Choose an \(\mathbb F_p\)-basis \(b_1,\ldots,b_e\) of \(A\). Then
\[
 R\cong K[z_1,\ldots,z_e]/(z_1^p,\ldots,z_e^p),\qquad z_i=[b_i]-[0],
\]
and \(I=(z_1,\ldots,z_e)\), so \(I^{e(p-1)+1}=0\). If \(u\in I\) satisfies \(u=u\star u\), then \(u=T_a(u)T_{1-a}(u)\in I^2\). Repeating with the same identity gives \(u\in I^{2^r}\) for every nonnegative integer \(r\). Thus \(u=0\).

3. Every augmentation-one vector belongs to \(U=1+I\), which is a group under convolution. For \(w\in I\), the characteristic-\(p\) Frobenius map gives \(w^p=0\): writing \(w=\sum_xc_x[x]\), we have \(w^p=(\sum_xc_x^p)[0]=\varepsilon(w)^p[0]=0\), since \(p x=0\) for every \(x\in A\). Hence \((1+w)^p=1\). The commutative group \(U\) is an elementary abelian \(p\)-group and therefore an \(\mathbb F_p\)-vector space, with vector addition represented by convolution multiplication. The maps \(T_c\) are \(\mathbb F_p\)-linear automorphisms on this vector space. The \(\star\)-idempotent equation on \(U\) becomes
\[
 (\mathrm{Id}-T_a-T_{1-a})(u)=0,
\]
where subtraction and addition are those of the \(\mathbb F_p\)-vector-space structure on \(U\). This proves that the nonzero idempotents form a subgroup of \(U\).

4. Put \(U_r=1+I^r\) for \(r\ge1\), and \(U_r=\{1\}\) after the nilpotence index. Each quotient \(U_r/U_{r+1}\) is canonically isomorphic, as an \(\mathbb F_p[K^\times]\)-module, to the additive group of \(I^r/I^{r+1}\) by \(1+w\mapsto w\bmod I^{r+1}\): the error term in multiplying \(1+w\) and \(1+v\) is in \(I^{2r}\subseteq I^{r+1}\). The group \(H=K^\times\), of order \(q-1\) coprime to \(p\), preserves this filtration. Maschke's theorem splits every short exact sequence of \(\mathbb F_p[H]\)-modules. It follows that the \(H\)-module \(U\) is (noncanonically) isomorphic over \(\mathbb F_p\) to the additive \(H\)-module \(I=\bigoplus_{r\ge1}I^r/I^{r+1}\) in the Grothendieck sense, i.e. the direct sum of all these graded pieces, which is \(H\)-isomorphic to \(I\) itself by splitting its own filtration. Thus the two endomorphisms \(\mathrm{Id}-T_a-T_{1-a}\) have equally large kernels on \(U\) and \(I\).

5. As a \(K[H]\)-module, \(I\) is the regular module: the vectors \([x]-[0]\) indexed by \(x\in K^\times\) form a \(K\)-basis, and \(T_c\) acts by multiplying indices by \(c\). Since \(H\) is cyclic of order \(q-1\), and \(K\) contains all its \((q-1)\)-st roots of unity, the regular representation splits into one-dimensional characters \(c\mapsto c^j\), once each for \(0\le j\le q-2\). On the \(j\)-th line, \(\mathrm{Id}-T_a-T_{1-a}\) is scalar multiplication by \(1-a^j-(1-a)^j\). Hence its kernel on \(I\) has \(K\)-dimension \(d_q(a)\), and exactly \(q^{d_q(a)}\) elements. This also counts the kernel on \(U\). Together with the unique zero-augmentation idempotent, this proves the formula.

6. For \(j=p^r\) with \(0\le r<e\), Frobenius gives \(a^j+(1-a)^j=(a+1-a)^j=1\), and the indices are distinct in \(\{1,\ldots,q-2\}\) when \(a\) is admissible. Therefore \(d_q(a)\ge e\). The special counts \(d_7(2)=1\), \(d_7(4)=2\) follow by evaluating the five indices \(j=1,\ldots,5\) (\(j=0\) never contributes).

## Verification
Run `python3 verify.py` with Python 3 (standard library only). The program directly enumerates the coefficient vectors in the **original quandle product** for eight finite-field parameter pairs: \((q,a)=(3,2),(4,2),(4,3),(5,2),(5,3),(5,4),(7,2),(7,4)\); the \(q=4\) cases use an explicit irreducible binary quadratic field implementation. It confirms the idempotent counts \(4,17,17,6,6,6,8,50\), and that none has a nonzero augmentation-zero idempotent. Additional arithmetic resonance tests cover prime fields of sizes \(11,13,17,19\). Successful output terminates in `VERIFY_OK`. Exhaustive finite examples are corroboration; the unrestricted proof is the argument above.

## Relationship to prior work
Ta, *The zero divisor and augmentation conjectures for medial quandle rings* (2026), proves characteristic-zero augmentation criteria for medial and Alexander quandle rings, not the present defining-characteristic count. Zhang, *Group-ring methods for Alexander quandle rings* (2026), establishes the convolution-transport formula used here and studies integral idempotents; it does not provide this positive-characteristic scalar-field enumeration. Sangare--Ta (2026) studies idempotents in other quandle-algebra settings. The three-element dihedral-quandle case \(q=3\) has previously been computed; this theorem includes it as a special case but its scope is every field size and every admissible scalar, with the entire idempotent subgroup identified. The novelty claim is limited to the all-parameter count and convolution-group structure, not to the group-ring transport or the known small case.

## Limitations
This concerns scalar latin Alexander quandles whose underlying additive group and coefficient field are both \(\mathbb F_q\). It does not classify idempotents over arbitrary coefficient fields, all Alexander modules, or nonlatin affine quandles. The character-count formula is explicit but may require testing up to \(q-1\) field exponents to evaluate. Earlier equivalent formulations in unindexed quandle-algebra literature cannot be completely excluded without independent review. No independent mathematical audit has been performed.

## References
- Lực Ta, *The zero divisor and augmentation conjectures for medial quandle rings*, arXiv:2610.20306v1 (2026), §§2,5,6.
- Zhi-Lin Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204 (2026), §§2,4,5.
- Birama Sangare and Lực Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550v2 (2026), §3.
