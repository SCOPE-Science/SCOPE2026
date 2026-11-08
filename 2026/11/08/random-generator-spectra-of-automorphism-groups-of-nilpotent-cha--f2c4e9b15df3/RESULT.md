# Random generator spectra of automorphism groups of nilpotent chain evolution algebras

## Finding
Let \(n\ge2\), \(q=p^f\) be any prime power, and let \(E_n(q)\) be the evolution algebra with natural basis \(e_1,\ldots,e_n\), products \(e_i e_j=0\) for \(i\ne j\), \(e_i^2=e_{i+1}\) for \(1\le i<n\), and \(e_n^2=0\). Let \(G_n(q)=\operatorname{Aut}_{\mathbb F_q}(E_n(q))\). For an integer \(s\ge1\), let \(\mathcal P_s(n,q)\) denote the probability that \(s\) independently uniform elements of \(G_n(q)\) generate the whole group.

Put \(m=q-1\), \(L=2^{n-1}-1\), \(d=\gcd(L,m)\), \(h=m/d\), and \(\Phi_s(m)=\prod_{\ell\mid m,\,\ell\text{ prime}}(1-\ell^{-s})\), where the empty product is \(1\). If \(h>1\), define \(e=\operatorname{ord}_h(p)\) and \(r=f/e\). Then
\[
\boxed{\mathcal P_s(n,q)=\Phi_s(m)\prod_{i=0}^{r-1}\bigl(1-p^{e(i-s+1)}\bigr)\quad (h>1).}
\]
If \(h=1\), then
\[
\boxed{\mathcal P_s(n,q)=\Phi_s(m)\prod_{i=0}^{f-1}\bigl(1-p^{i-s}\bigr)\quad (h=1).}
\]
The factors vanish when their exponents are zero. Thus the minimum number \(\mathrm d(G_n(q))\) of group generators equals \(r+1\) if \(h>1\), and \(f\) if \(h=1\). In addition, the number of conjugacy classes of \(G_n(q)\) is exactly \(m+d^2\), and the probability that two uniformly random automorphisms commute is \((m+d^2)/(qm)\).

There is a sharp extension-degree resonance in characteristic two. When \(q=2^f\) and \(f\ge2\),
\[
\mathrm d(G_n(2^f))=\begin{cases}f,&f\mid(n-1),\\2,&f\nmid(n-1).\end{cases}
\]
For \(f\nmid(n-1)\), the two-generator probability is \((1-2^{-f})\Phi_2(2^f-1)\). For \(f\ge3\) and \(f\mid(n-1)\), this probability is zero. For example, when \(q=8\), the two-generator probability is \(6/7\) if \(3\nmid(n-1)\), and zero otherwise. The even-characteristic phenomenon is complemented by odd-characteristic higher-rank cases: \(\mathrm d(G_{13}(27))=4\).

## Assumptions and scope
Automorphisms are \(\mathbb F_q\)-linear algebra automorphisms, not semilinear transformations. Products are nonassociative but bilinear and commutative. Exponentiation by \(2\) in the defining multiplication is the algebra square, not a claim of associative powers. The formulas concern fixed finite \(q\) and arbitrary \(n\ge2\), \(s\ge1\). The integer \(e\) is defined only when \(h>1\) (thus \(p\) is coprime to \(h\)); \(e\mid f\). For \(q=2\), the automorphism group is cyclic of order two, and the \(h=1\) formula applies.

## Proof
**1. Intrinsic automorphism normal form.** The square subspace of the algebra is \(E_n(q)^2=\langle e_2,\ldots,e_n\rangle\). An automorphism \(T\) therefore sends \(e_1\) to \(a e_1+\sum_{j=2}^n b_j e_j\), with \(a\ne0\). Because \(e_{i+1}=e_i^2\), the images of \(e_i\) are obtained by iterated squaring of \(T(e_1)\). Inductively, if \(b_2=\cdots=b_{i-1}=0\), the coefficient of \(e_i\) in \(T(e_i)\) is \(a^{2^{i-1}}\), and \(T(e_i)\) has no components below \(e_i\). The coefficient of \(e_{i+1}\) in \(T(e_1)T(e_i)=0\) is consequently \(a^{2^{i-1}}b_i\), forcing \(b_i=0\) for \(2\le i<n\). Thus all automorphisms, and only automorphisms, have form
\[
T_{a,b}(e_1)=ae_1+be_n,\qquad T_{a,b}(e_i)=a^{2^{i-1}}e_i\quad(2\le i\le n),
\]
with \(a\in\mathbb F_q^\times\) and \(b\in\mathbb F_q\). Their matrices are invertible and preserve all basis products, including zero cross-products. This argument uses no restriction on the characteristic.

**2. Scalar semidirect product.** Set \(x=b/a\). Composition of the above automorphisms corresponds to
\[
(x,a)(y,c)=(x+a^L y,ac),\qquad L=2^{n-1}-1.
\]
Thus \(G_n(q)\cong(\mathbb F_q,+)\rtimes\mathbb F_q^\times\), where \(a\) acts as multiplication by \(a^L\). The action has kernel of order \(d=\gcd(L,q-1)\) and cyclic image \(H\) of order \(h=(q-1)/d\). When \(h>1\), the subfield \(\mathbb F_p[H]\) is exactly \(\mathbb F_{p^e}\), with \(e=\operatorname{ord}_h(p)\), so \(\mathbb F_q\) is the direct sum of \(r=f/e\) copies of the simple \(\mathbb F_p[H]\)-module.

**3. Criterion for simultaneous generation.** A uniformly chosen ordered \(s\)-tuple projects to an ordered tuple in the cyclic quotient \(C_m\). Its projections generate that quotient with probability \(\Phi_s(m)\), by the Chinese remainder theorem. If they do not generate it, the original tuple cannot generate the group. Assume the projections do generate it. For \(h>1\), at least two generators are necessary. When \(s\ge2\), Nielsen operations on the tuple (permutations, inversions, and multiplications of one member by another) reduce the projection tuple to one generator of \(C_m\) followed by \(s-1\) identity projections. This change is bijective on each fixed-projection fiber. Since the first projected element has nontrivial action on the additive normal group, conjugating by a suitable translation removes its translation component. The remaining \(s-1\) entries are independent uniform translations. They generate the full normal group under conjugation by the first entry exactly when they span the \(r\)-dimensional vector space over \(\mathbb F_{p^e}\). That probability is \(\prod_{i=0}^{r-1}(1-(p^e)^{i-(s-1)})\), yielding the first formula. If \(s=1\) and \(h>1\), both the formula and the group-theoretic probability are zero. When \(h=1\), the group is the direct product of the additive group \((C_p)^f\) and the cyclic group \(C_m\), whose orders are coprime; the quotient-generation event and spanning of \(s\) independent vectors in \(\mathbb F_p^f\) are independent, giving the second formula. Their first nonzero values give the claimed generator ranks.

**4. Conjugacy classes.** Two pairs \((x,a)\), \((y,c)\) commute precisely when \((a^L-1)y=(c^L-1)x\). There are \(d^2q^2+((q-1)^2-d^2)q\) ordered commuting pairs. Dividing by \(|G_n(q)|=q(q-1)\) gives the number of conjugacy classes \(q-1+d^2\). Indeed, the centralizer strata are: \(d\) elements of the form \((0,a)\) with \(a^L=1\), all central; \(d(q-1)\) further elements with \(a^L=1\) and nonzero translation component, whose centralizer has size \(qd\); and \(q(q-1-d)\) elements with \(a^L\ne1\), whose centralizer has size \(q-1\). When \(h=1\), the second stratum is also central; the formulas still apply. This gives the stated commuting probability.

**5. Characteristic-two jump.** For \(q=2^f\), the elementary gcd identity gives \(d=2^{\gcd(f,n-1)}-1\). If \(f\mid n-1\), then \(h=1\) and the minimum generating rank is \(f\). Otherwise, \(g=\gcd(f,n-1)\) is a proper divisor, so \(g\le f/2\), and
\[
h=\frac{2^f-1}{2^g-1}>2^{f/2}-1.
\]
Every proper subfield of \(\mathbb F_{2^f}\) has at most \(2^{f/2}\) elements. Therefore \(H\) is not contained in any proper subfield, \(e=f\), and the minimum rank is \(2\). The two-generator probabilities follow on putting \(s=2\). For \(q=27\), \(n=13\), one has \(m=26\), \(L=4095\), \(d=13\), \(h=2\), \(e=1\), \(r=3\), so the minimum rank is \(4\).

## Verification
Run `python3 verify.py` with the standard Python 3 library. The script exhaustively enumerates all linear maps of \(E_3(2)\), \(E_3(3)\), and \(E_4(2)\), independently checking homomorphism and invertibility, and confirms the predicted normal-form sets. It then explicitly composes the corresponding finite groups to count commuting pairs for field orders \(2,3,4,8,16,27\), including the \(q=27\), \(n=13\) example. For the smaller groups of orders at most \(56\), it also enumerates every generating pair by subgroup closure and compares with the exact probabilities. All checks conclude `VERIFY_OK`. Exhaustive finite checks are corroboration, not the proof of the all-dimension assertions.

## Relationship to prior work
Mukhamedov, Khakimov, Omirov, and Qaralleh (2018) classified automorphisms of maximal-nilindex nilpotent evolution algebras over characteristic-zero fields (arXiv:1805.10285; Section 5). That automorphism normal form is a structural predecessor, not a newly claimed result. The present proof independently extends the chosen chain case to all finite characteristics. The generator-tuple probability, characteristic-two extension-degree jump, and conjugacy-class count are the new assertions assessed here. General group facts about cyclic quotients, scalar semidirect products, and finite-field vector-space generation enter the proof as established tools; no general theorem for such groups is claimed.

The related 2019 work of Elduque and Labra on automorphism group schemes treats perfect evolution algebras, not this nilpotent family. General work on random generation of finite groups, including Burness–Liebeck–Shalev (2013), provides context but not the present indexed formula. A generic general theorem on generation of scalar semidirect products could imply part of the result; the existence of unlocated stronger coverage remains an originality limitation.

## Limitations
The finding concerns the specific chain evolution algebra, not every evolution algebra of maximal nilindex and not arbitrary coefficient patterns in upper-triangular evolution algebras. The count of generating tuples is for ordered uniformly random \(\mathbb F_q\)-linear automorphisms. The group-semidirect decomposition and elementary generation principles could be independently derivable from other group-theory literature; publication priority is provisional. The original characteristic-zero classification was inspected in full-text form, but this does not constitute a comprehensive literature census. No independent validation or independent audit is asserted.

## References
1. F. Mukhamedov, O. Khakimov, B. Omirov, I. Qaralleh, *Derivations and automorphisms of nilpotent evolution algebras with maximal nilindex*, arXiv:1805.10285 (first posted May 25, 2018), especially Section 5. https://arxiv.org/abs/1805.10285
2. A. Elduque, A. Labra, *Evolution algebras, automorphisms, and graphs*, arXiv:1902.02191 (2019). https://arxiv.org/abs/1902.02191
3. T. C. Burness, M. W. Liebeck, A. Shalev, *Generation and random generation: From simple groups to maximal subgroups*, Advances in Mathematics 248 (2013), 59–95. https://doi.org/10.1016/j.aim.2013.07.009
