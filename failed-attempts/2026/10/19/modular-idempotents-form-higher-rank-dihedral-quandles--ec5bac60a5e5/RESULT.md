# Modular idempotents form higher-rank dihedral quandles

## Finding

Let \(p\) be an odd prime, \(K\) any field of characteristic \(p\), and \(Q=R_p\) the dihedral quandle on \(\mathbb F_p\) with \(a\triangleright b=2b-a\). The quandle algebra \(A=K[Q]\) has basis \(e_a\) with \(e_a e_b=e_{2b-a}\). Set
\[
H=\langle-1,2\rangle\leq\mathbb F_p^\times,
\qquad r=\frac{p-1}{|H|}.
\]
Under the multiplication of \(A\), **all nonzero idempotents form a subquandle isomorphic to the core quandle of the additive group \(K^r\)**, namely the operation
\[
(v,w)\longmapsto -v+2w.
\]
More precisely, identify the underlying vector space of \(A\) with the ordinary group ring \(R=K[T]/(T^p-1)\), taking \(e_a\) to \(T^a\). For each multiplicative coset \(C\) of \(H\) in \(\mathbb F_p^\times\), put
\[
V_C=\sum_{a\in C}a^{-1}T^a,
\qquad L=\bigoplus_{C\in\mathbb F_p^\times/H}K V_C.
\]
Here \(a^{-1}\) is the inverse in the prime field, viewed as a scalar in \(K\). The entire idempotent set, **including zero**, is exactly
\[
\operatorname{Idem}(A)
=\{0\}\cup\left\{\operatorname{Exp}_p(v):v\in L\right\},
\qquad
\operatorname{Exp}_p(v)=\sum_{j=0}^{p-1}\frac{v^j}{j!},
\]
where powers and products in \(\operatorname{Exp}_p\) are those of the **ordinary associative group ring** \(R\), not of \(A\).

Consequently, for \(K=\mathbb F_q\), with \(q\) any power of \(p\),
\[
\boxed{\bigl|\operatorname{Idem}(\mathbb F_q[R_p])\bigr|=1+q^{(p-1)/|\langle-1,2\rangle|}.}
\]
Over the prime coefficient field, the only nonzero idempotents are the \(p\) basis elements exactly when \(\langle-1,2\rangle=\mathbb F_p^\times\). At \(p=17\), there are \(290\) idempotents over \(\mathbb F_{17}\), including \(272\) nonbasis idempotents; at \(p=31\), the count is \(1+31^3\). Every prime \(p\equiv1\pmod 8\) has \(r\geq2\), so infinitely many prime-order dihedral quandles exhibit nonbasis idempotents over their prime coefficient fields (by Dirichlet's theorem).

## Assumptions and scope

The prime \(p\) is odd and \(K\) is an arbitrary commutative field of characteristic exactly \(p\). The quandle law is the right-distributive convention \(a\triangleright b=2b-a\). The coefficient characteristic **divides** the quandle order; no conclusion is claimed for coefficient characteristics unequal to \(p\), nor for composite-order quandles. Zero is counted as an idempotent in the stated cardinalities, but is excluded from the subquandle statement.

## Proof

**1. Transport to a local group ring.** The ordinary group ring \(R=K[\mathbb Z/p]\) has basis \(T^a\) for \(a\in\mathbb F_p\). Define two commuting group-ring automorphisms \(\alpha(T^a)=T^{-a}\) and \(\beta(T^a)=T^{2a}\). The transported nonassociative quandle-algebra multiplication is
\[
u\star w=\alpha(u)\beta(w),
\]
with the right-hand side multiplied in \(R\). The ordinary augmentation ideal \(I=\ker\varepsilon=(T-1)R\) satisfies \(I^p=0\), since \(T^p-1=(T-1)^p\) in characteristic \(p\).

**2. Exclusion of nonzero augmentation-zero idempotents.** Since \(\varepsilon\) is multiplicative for \(\star\), the augmentation of an idempotent is \(0\) or \(1\). If \(u\star u=u\) and \(\varepsilon(u)=0\), then \(u\in I\) and \(u=\alpha(u)\beta(u)\in I^2\). Repeating with \(I^2,I^4,\ldots\) forces \(u\in I^{2^k}=0\) for sufficiently large \(k\). Thus a nonzero idempotent has augmentation one.

**3. Linearization of augmentation-one idempotents.** Since \(I^p=0\) and \(j!\) is invertible in \(K\) for \(0\leq j<p\), the truncated polynomial \(\operatorname{Exp}_p(v)\) is a bijective group homomorphism
\[
(I,+)\stackrel{\cong}{\longrightarrow}(1+I,\cdot),
\]
whose inverse is the truncated logarithm \(\sum_{j=1}^{p-1}(-1)^{j+1}(u-1)^j/j\). Formal exponential/logarithm identities are legitimate modulo \(I^p\): terms of total degree at least \(p\) vanish and all smaller factorial denominators are units. Moreover, \(\alpha\) and \(\beta\) commute with \(\operatorname{Exp}_p\). Hence for \(u=\operatorname{Exp}_p(v)\),
\[
u\star u=u\quad\Longleftrightarrow\quad
\operatorname{Exp}_p(\alpha v+\beta v)=\operatorname{Exp}_p(v)
\quad\Longleftrightarrow\quad v\in\ker(\alpha+\beta-1).
\]

**4. Exact kernel and its operators.** Put \(H=\langle-1,2\rangle\). As a \(K\)-vector space, \(R\) decomposes into the line \(KT^0\) and the subspaces \(W_C=\operatorname{span}_K\{T^a:a\in C\}\), one for each coset \(C\) of \(H\) in \(\mathbb F_p^\times\). The commuting permutations \(\alpha,\beta\) preserve every summand. On \(KT^0\), \(\alpha+\beta-1\) is identity. Each \(W_C\) is the regular permutation representation of \(H\); because \(|H|\mid p-1\), it splits over \(K\) into its one-dimensional characters \(\chi:H\to K^\times\). A character contributes to the kernel exactly when
\[
\chi(-1)+\chi(2)=1.
\]
Since \(p\) is odd, \(\chi(-1)\in\{-1,1\}\). The value \(+1\) is impossible, since it would require \(\chi(2)=0\). The other case forces \(\chi(-1)=-1\), \(\chi(2)=2\), and these values specify the unique inclusion character \(H\hookrightarrow\mathbb F_p^\times\subset K^\times\). Thus each \(W_C\) contributes **exactly one** kernel dimension. The concrete eigenvector is \(V_C=\sum_{a\in C}a^{-1}T^a\), for which direct reindexing gives
\[
\alpha(V_C)=-V_C,\qquad\beta(V_C)=2V_C.
\]
Because \(-1\in H\) and \(p\ne2\), its coefficient sum is zero, so \(V_C\in I\). Therefore
\[
\ker(\alpha+\beta-1)=L,
\qquad\dim_K L=r,
\qquad\alpha|_L=-1,\quad\beta|_L=2.
\]

**5. Subquandle and count.** For \(v,w\in L\),
\[
\operatorname{Exp}_p(v)\star\operatorname{Exp}_p(w)
=\operatorname{Exp}_p(\alpha v+\beta w)
=\operatorname{Exp}_p(-v+2w).
\]
Thus the nonzero idempotents are closed under the native product, and the bijection \(\operatorname{Exp}_p|_L\) is a quandle isomorphism from \(\operatorname{Core}(L,+)\). For finite \(K=\mathbb F_q\), their number is \(q^r\); adding zero gives the formula.

The natural basis elements \(e_a\) are all idempotent and distinct. Over \(\mathbb F_p\), there are only these when \(r=1\); if \(r>1\), the count \(p^r\) strictly exceeds \(p\). If \(p\equiv1\pmod8\), then both \(-1\) and \(2\) are quadratic residues (Euler's criterion and the supplementary law for \(2\)); hence \(H\) is contained in the index-two quadratic-residue subgroup, giving \(r\ge2\). Dirichlet's theorem supplies infinitely many such primes. For \(p=17\), \(|H|=8\), so \(r=2\), and \(1+17^2=290\), of which \(290-1-17=272\) are not basis elements. ∎

## Verification

Run \(\texttt{python3 verify\_modular\_dihedral.py}\) in the directory containing the standalone verification script. The script uses only Python's standard library. It checks the predicted kernel dimension for eleven distinct odd primes, constructs and directly tests nonzero idempotents (including nonbasis witnesses), and verifies the induced quandle operation on pairs of witnesses. Independently, it exhaustively tests **all** coefficient vectors over \(\mathbb F_3[R_3]\), \(\mathbb F_5[R_5]\), and \(\mathbb F_9[R_3]\). The latter uses the explicit field \(\mathbb F_3[u]/(u^2+1)\). The replay ended in \(\texttt{VERIFY\_OK}\). These tests are finite consistency checks; the theorem for all fields and primes follows from the proof above.

## Relationship to prior work

Zhang (2026, arXiv:2610.08204v1, Proposition 2.1) transports Alexander quandle multiplication to an ordinary group ring. This proof uses the transport as background but treats the modular case, in which ordinary complex Fourier diagonalization does not apply. Zhang's integral-idempotent and complex-Peirce results do not give this modular idempotent census. Elhamdadi, Ta and Virgin (2026, arXiv:2609.03799v1) establish integral idempotent rigidity of latin dihedral quandles, a distinct coefficient-ring statement. Sangare and Ta (2026, arXiv:2608.01550) obtain characteristic-two idempotent results for commutative quandles and other structure theorems, not the odd-prime modular dihedral count. A published characteristic-three computation of the quandle algebra of \(R_3\) already gives \(q+1\) idempotents; the present theorem **includes that known case without claiming it as new** and identifies an arithmetic rank jump beginning at \(p=17\). The comparison with existing nonmodular finite-field formulas is also disjoint because those assume the coefficient characteristic does not divide the quandle order.

## Limitations

This result does not enumerate idempotents for composite-order dihedral quandles or for coefficient characteristic not dividing the quandle order. Its finite checks cover selected small cases, not all primes. The novelty comparison is against the identified literature and searchable published records, not a proof that no equivalent earlier result exists.

## References

1. Z.-L. Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204v1 (public 2026-10-06), especially §§2 and 5. https://arxiv.org/abs/2610.08204
2. M. Elhamdadi, L. Ta and B. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799v1 (public 2026-09-03), especially §§3–4. https://arxiv.org/html/2609.03799v1
3. B. Sangare and L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550 (public 2026-08-03), especially §§3–4. https://arxiv.org/abs/2608.01550
4. *A characteristic-three idempotent line in the quandle algebra of \(R_3\)*, publicly indexed mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-characteristic-three-idempotent-line-in-the-quandle-algebra-of--06aa9c19e539 (statement-level comparison only).
5. G. Churchill, I. R. Churchill, N. Fernando and B. Kousik, *A further study of quandles and quandle rings*, arXiv:2608.09149v1 (2026); its complete relevant calculation was not accessible for inspection and remains a bibliographic risk.
