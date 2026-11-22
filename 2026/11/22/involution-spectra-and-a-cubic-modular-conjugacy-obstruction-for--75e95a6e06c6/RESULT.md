# Involution spectra and a cubic modular conjugacy obstruction for free cube-zero associative algebras

## Finding

Let \(k=\mathbb F_q\) be any finite field, let \(V=k^n\) with \(n\geq1\), and let \(A=V\oplus(V\otimes_k V)\) be the free **nonunital associative algebra with all words of length at least three set to zero**: \(vw=v\otimes w\) for \(v,w\in V\), and any product involving \(V\otimes V\) is zero. We determine all automorphisms \(\varphi\) satisfying \(\varphi^2=\mathrm{id}\) (including the identity), with exact finite-field counts and identity-linear conjugacy orbits.

Write \(G_d(q)=|\mathrm{GL}_d(k)|=\prod_{j=0}^{d-1}(q^d-q^j)\) and \(G_0(q)=1\). In **odd characteristic**, for each \(0\leq a\leq n\) the automorphisms whose induced linear involution on \(A/A^2\) has \(+1\)-eigenspace of dimension \(a\) number exactly
\[
\boxed{\frac{G_n(q)}{G_a(q)G_{n-a}(q)}q^{3a^2(n-a)+(n-a)^3}.}
\]
Summing over \(a\) gives the total. For each fixed induced involution, all such automorphisms are conjugate by automorphisms acting trivially on \(A/A^2\).

In **characteristic two**, write the induced involution's Jordan form as \(J_2^{\oplus r}\oplus J_1^{\oplus s}\), with \(s=n-2r\), \(0\leq r\leq\lfloor n/2\rfloor\). Its stratum contains exactly
\[
\boxed{\frac{G_n(q)}{q^{r^2+2rs}G_r(q)G_s(q)}\;q^{e_{r,s}},\qquad e_{r,s}=s^3+2rs(n-r)+rn^2.}
\]
For **each fixed induced involution**, the automorphisms above it split into precisely
\[
\boxed{q^{s^3}}
\]
conjugacy orbits under the normal subgroup acting identically on \(A/A^2\), all of cardinality \(q^{n^3-e_{r,s}}\). Thus every lift of a fixed induced involution can be linearized by such a conjugation **if and only if** it has no singleton Jordan block (\(s=0\)); otherwise genuinely nonlinearizable lifts occur. The cubic exponent distinguishes ordinary automorphism involutions from anti-automorphism involutions on this same algebra.

For example, the total numbers are \(304\) at \((n,q)=(2,2)\), \(7534\) at \((2,3)\), and \(409376\) at \((2,5)\). If *exact* order two rather than order dividing two is required, subtract one for the identity automorphism.

## Assumptions and scope

All automorphisms are \(k\)-linear, multiplicative and bijective. They are **not** anti-automorphisms: the order of the factors is preserved, so the tensor-square action is \(g\otimes g\), not a flip-twisted tensor action. The algebra is nilpotent of index three, free in the variety of such nonunital associative algebras. The conjugacy assertion uses the subgroup of automorphisms inducing the identity on \(A/A^2\), not the entire automorphism group. Counts include the identity and every finite extension field in the stated characteristics.

## Proof

**Normal form.** The characteristic ideal \(A^2=V\otimes V\) is the annihilator of all products involving one element of \(A^2\). Each automorphism is uniquely specified by \(g\in\mathrm{GL}(V)\) and an arbitrary \(h\in H=\mathrm{Hom}_k(V,V\otimes V)\):
\[
\varphi(v)=gv+h(v),\qquad \varphi(v\otimes w)=gv\otimes gw.
\]
Conversely the formulas define an algebra automorphism because the block matrix relative to \(V\oplus(V\otimes V)\) is triangular with invertible diagonal blocks \(g\) and \(g\otimes g\). Put \(F=g\otimes g\). Direct composition gives
\[
\varphi^2=\mathrm{id}\quad\Longleftrightarrow\quad g^2=I,\quad Fh+hg=0.
\]
For fixed \(g^2=I\), define \(T:H\to H\) by \(T(h)=Fhg\). Then \(T^2=I\) and the equation is \((I+T)h=0\). Hence it remains to determine this linear kernel and the count of \(g\).

**Odd characteristic.** Decompose \(V=V_+\oplus V_-\) into eigenspaces of dimensions \(a,b=n-a\). The tensor square splits into \(+1\)-eigenspace of dimension \(a^2+b^2\) and \(-1\)-eigenspace of dimension \(2ab\). The constraint \(Fh=-hg\) therefore sends \(V_+\) freely into the latter and \(V_-\) freely into the former. Its solution-space dimension is \(a(2ab)+b(a^2+b^2)=3a^2b+b^3\). The conjugacy class of \(g\) in \(\mathrm{GL}_n(k)\) has size \(G_n/(G_aG_b)\), proving the odd-characteristic formula.

**Characteristic two.** Every \(g\) satisfying \(g^2=I\) has unipotent Jordan type \(J_2^r\oplus J_1^s\) with \(2r+s=n\). Regard \(V\) as a \(k[C_2]\)-module. A two-dimensional Jordan block is the regular module, while a singleton is trivial. In characteristic two the diagonal tensor action satisfies \(J_2\otimes J_2\cong J_2^{\oplus 2}\) (the tensor product of one regular module with any module is free of the latter's vector-space rank); likewise \(J_2\otimes J_1\cong J_2\). Thus \(V\otimes V\) has exactly \(2r(n-r)\) regular blocks and \(s^2\) trivial blocks. The solutions of \(Fh=hg\) are precisely module homomorphisms. A map from each singleton has \(s^2+2r(n-r)\) free scalar parameters (the dimension of the target's fixed space), and a map from each regular block has \(n^2\) parameters. Their dimension is therefore
\[
e_{r,s}=s\big(s^2+2r(n-r)\big)+rn^2.
\]
The centralizer of this \(g\) has semisimple quotient \(\mathrm{GL}_r(k)\times\mathrm{GL}_s(k)\), and its group order is \(q^{r^2+2rs}G_rG_s\); this also follows by writing the endomorphism ring of \((k[t]/t^2)^r\oplus k^s\) in four blocks and checking invertibility on its two semisimple summands. Hence the number of distinct \(g\) of this type is the stated quotient, completing the exact count.

**Identity-linear conjugacy.** The normal shear subgroup \(U\) is the vector group \(H\), with elements \(u_f(v)=v+f(v)\) fixing \(V\otimes V\). Conjugating \(\varphi_{g,h}\) by \(u_f\) changes \(h\) by \(fg-Ff\). The substitution \(z=fg\) identifies these translations with \(\operatorname{im}(I-T)\). In odd characteristic \(H=\ker(I+T)\oplus\ker(I-T)\), so \(\operatorname{im}(I-T)=\ker(I+T)\), giving one orbit. In characteristic two, \(I-T=I+T\); since \(\dim H=n^3\) and \(\dim\ker(I+T)=e_{r,s}\), the translation image has dimension \(n^3-e_{r,s}\). Every orbit has \(q^{n^3-e_{r,s}}\) elements, and the quotient space of solutions has dimension
\[
2e_{r,s}-n^3=s^3,
\]
where the final equality follows upon substituting \(n=2r+s\). Its cardinality is \(q^{s^3}\). The purely linear model corresponds to the zero solution, so all lifts are conjugate to it exactly when this quotient is zero-dimensional, equivalently \(s=0\).

## Verification

The self-contained `verify.py` works with the Python standard library. Extract it next to this document and execute `python3 verify.py`. It enumerates each reduced linear involution for \((n,q)=(1,2),(2,2),(3,2),(1,3),(2,3),(2,5)\), independently computes the rank of the actual \(n^3\)-variable linear equation \(Fh+hg=0\), and matches every dimension and the total counts. For \((n,q)=(1,2),(2,2),(1,3)\), it also enumerates **every** \(h\) and directly squares the full \((n+n^2)\)-dimensional automorphism matrices, with agreement in each case. It explicitly enumerates the characteristic-two identity-linear conjugation orbits at \((n,q)=(2,2)\), recovering \(q^{s^3}\) independently. The supplied `verification_output.txt` is the recorded output. Finite checks do not prove the all-field theorem; the proof above does.

## Relationship to prior work

Bardakov, Neshchadim and Sosnovsky (arXiv:1007.2711v1, first public 2010-07-16) study automorphism groups of free associative algebras, including triangular subgroups, in a different untruncated setting and generally characteristic zero. Their finite-order discussion motivates considering nilpotent truncations and positive-characteristic torsion but does not count these involutions or their shear orbits. Lopatin and Shestakov (arXiv:1303.0898v1, 2013-03-05) study different finite-field nil-algebra questions and provide background for truncated free associative constructions, not the count here. A published 2026 result, *A modular conjugacy obstruction and exact census of anti-involutions on free cube-zero algebras* (published-finding corpus record `e842947e3cb4`), treats the **reversal**-twisted tensor action and obtains an exponent linear in the singleton count times generator number; it does **not** imply this distinct automorphism formula and cubic obstruction. Published work on involutions of free class-two **Lie** automorphism groups uses exterior squares, not the tensor square here. The elementary representation-theoretic ingredients are standard; the assessed mathematical contribution is their exact automorphism-specific census and nonlinearizability classification for this natural algebra family.

## Limitations

The assertion is confined to two-step nonunital free associative algebras and the subgroup \(U\) for orbit classification. It does not classify orbits under all of \(\operatorname{Aut}(A)\), higher truncations, infinitesimal scheme structures, or all invariant rings. The formula counts \(\varphi^2=I\) rather than only automorphisms of exact order two. Historical priority can be affected by an unlocated general formula for involutions in semidirect products or a classification of characteristic-two modules; an independent scholarly literature review and independent mathematical validation have not been performed.

## References

- V. G. Bardakov, M. V. Neshchadim and Y. V. Sosnovsky, *Groups of triangular automorphisms of a free associative algebra and a polynomial algebra*, arXiv:1007.2711v1, posted 2010-07-16, https://arxiv.org/abs/1007.2711. Full online preprint consulted.
- A. A. Lopatin and I. P. Shestakov, *Associative nil-algebras over finite fields*, arXiv:1303.0898v1, posted 2013-03-05, https://arxiv.org/abs/1303.0898. Full online preprint consulted.
- *A modular conjugacy obstruction and exact census of anti-involutions on free cube-zero algebras*, public research record `e842947e3cb4`, published 2026-11-02. Its complete scientific result and proof were compared with the distinct automorphism condition.
- *Conjugacy classes and centralizers of involutions in free class-two Lie automorphism groups*, public research record `0f3c26f9728b`, published 2026-10-25. Summary compared; different algebraic variety.
