# A joint-rank census of commuting singular endomorphisms of full transformation semigroups

## Finding
For every integer \(n\geq5\), let \(\mathcal T_n\) be the full transformation semigroup on \([n]\), and let \(\mathcal S_n\) denote the *singular* (nonautomorphism) elements of the semigroup-endomorphism monoid \(\operatorname{End}(\mathcal T_n)\). We count **ordered commuting pairs** \((\alpha,\beta)\in\mathcal S_n^2\) simultaneously by the cardinalities of their images as transformations of \(\mathcal T_n\). Identity preservation is not imposed on endomorphisms.

For \(m\geq0\), define the involution numbers and signed involution sums
\[
 U_m^\pm=\sum_{j=0}^{\lfloor m/2\rfloor}\frac{m!}{2^j j!(m-2j)!}(\pm1)^j.
\]
For every integer \(s\geq1\), define
\[
 a_s=\sum_{h=1}^{s}\binom{s-1}{h-1}U_{h-1}^{+}h^{s-h},\qquad
 d_s=\sum_{h=1}^{s}\binom{s-1}{h-1}h^{s-h},\qquad
 b_s=U_{s-1}^{+},\quad c_s=U_{s-1}^{-}.
\]
If \(e\in\mathcal T_n\) is idempotent with rooted kernel-fiber sizes \(s_1,\ldots,s_k\), set
\[
 A_e=\prod_i a_{s_i},\quad B_e=\prod_i b_{s_i},\quad
 C_e=\prod_i c_{s_i},\quad D_e=\prod_i d_{s_i},\quad
 E_e=\frac{B_e+C_e}{2},\quad O_e=\frac{B_e-C_e}{2},\quad N_e=A_e-B_e.
\]
For every nonidentity \(e\), let
\[
 p_e(v)=v^2+(E_e-1)v^3,\qquad
 q_e(v)=v+(D_e-2)v^2+(A_e-B_e-D_e+1)v^3.
\]
Then the complete ordered-commuting **joint rank** polynomial is
\[
\boxed{\begin{aligned}
 R_n(x,y)&=\sum_{\substack{\alpha,\beta\in\mathcal S_n\\\alpha\beta=\beta\alpha}}
 x^{|\operatorname{im}\alpha|}y^{|\operatorname{im}\beta|}\\
 &=xy+\sum_{\substack{e^2=e\text{ in }\mathcal T_n\\e\ne\mathrm{id}}}
 \bigl[p_e(x)p_e(y)+q_e(x)q_e(y)+O_ex^3y^3\\
 &\hspace{23mm}+O_e(x^3y^2+x^2y^3)+2O_e(x^3y+xy^3)
 +2\bigl(xp_e(y)+yp_e(x)\bigr)\bigr].
\end{aligned}}
\]
This is an explicit finite formula: summation over idempotents can be replaced by summation over integer partitions \(\lambda\vdash n\), each weighted by
\[
 w_\lambda=\frac{n!}{\prod_{s\geq1}((s-1)!)^{m_s(\lambda)}m_s(\lambda)!},
\]
where the all-singleton partition, corresponding to \(e=\mathrm{id}\), is excluded.

In particular, if \(H_n=R_n(1,1)\), then
\[
 H_n=1+\sum_{e^2=e,\ e\ne\mathrm{id}}(E_e^2+N_e^2+7O_e+4E_e).
\]
There is also one exact *formal exponential generating function*. For a weight sequence \(w=(w_s)_{s\geq1}\), let
\[
 \mathscr B(w;z)=\exp\!\left(\sum_{s\geq1}w_s\frac{z^s}{(s-1)!}\right),
\]
and write multiplication and powers of such weight sequences componentwise. The coefficients of degree \(n\geq5\) in
\[
\boxed{\mathscr B(a^2;z)-2\mathscr B(ab;z)
 +\tfrac54\mathscr B(b^2;z)+\tfrac12\mathscr B(bc;z)
 +\tfrac14\mathscr B(c^2;z)+\tfrac{11}{2}\mathscr B(b;z)
 -\tfrac32\mathscr B(c;z)-4e^z}
\]
equal \(H_n/n!\). No assertion is made that its lower-degree coefficients count all singular endomorphisms for the exceptional case \(n=4\).

For \(n=5\), the joint coefficient table, with row and column indices \(1,2,3\), is
\[
 \begin{pmatrix}
 196&2160&1140\\2160&67755&56595\\1140&56595&53925
 \end{pmatrix},
\]
so that \(H_5=241666\). Further totals are \(H_6=15801247\), \(H_7=1248611442\), and \(H_8=118745065537\).

## Assumptions and scope
All maps are transformations of the labeled finite set \([n]\), with ordinary function composition; all counts are of *ordered* pairs. A rank means \(|\operatorname{im}\alpha|\) of the semigroup endomorphism \(\alpha\), not the rank of its parameter \(e\) or \(t\). The theorem covers all \(n\geq5\); at \(n=4\), exceptional rank-seven semigroup endomorphisms prevent the same complete census formula. No finite-field hypothesis is involved.

## Proof
**1. Unique normal form and multiplication.** By the classification of Schein--Teclezghi, in the form restated with multiplication by Gould--Grau--Johnson, all singular semigroup endomorphisms for \(n\geq5\) are uniquely \(\phi_{t,e}\) with
\[
 t^3=t,\qquad e^2=e,\qquad te=et=e.
\]
Explicitly, \(\phi_{t,e}\) sends an odd permutation to \(t\), an even permutation to \(t^2\), and every nonpermutation to \(e\). A unique permissible pair with \(e=\mathrm{id}\) is \((\mathrm{id},\mathrm{id})\), giving the rank-one element \(b_0=\phi_{\mathrm{id},\mathrm{id}\). We do not claim this normal form or multiplication table as new.

**2. A rooted-fiber count of parameters.** Fix an idempotent \(e\) with kernel blocks of sizes \(s_i\) and their unique distinguished fixed-point roots. The equations \(te=et=e\) require \(t\) to preserve every fiber and fix its root. The equation \(t^3=t\) says that the restriction of \(t\) to its image is an involution, and every other vertex maps in one step into that image. On a fiber of size \(s\), choose the image to have \(h\) points containing the root; choose any involution of the other \(h-1\) image points; and map the remaining \(s-h\) points to the chosen image points. This gives \(a_s\) choices. If \(t\) is a permutation, its root-fixed involution contributes \(b_s\) choices, signed according to the parity of its transpositions by \(c_s\); if \(t\) is idempotent, the same selection with trivial image permutation contributes \(d_s\) choices. Independence of the fibers gives \(A_e,B_e,C_e,D_e\). Thus \(E_e\) and \(O_e\) count even and odd involutive permutations, respectively, and \(N_e\) counts nonpermutation tripotents. Notice \(e\ne\mathrm{id}\) implies \(D_e\geq2\).

**3. Rank polynomials within a prescribed fiber idempotent.** For fixed nonidentity \(e\), every odd permutation parameter has image cardinality three. Every even permutation parameter has cardinality three except \(t=\mathrm{id}\), which gives cardinality two: this yields \(p_e\). Every nonpermutation parameter has cardinality one if \(t=e\), cardinality two if \(t\) is idempotent and different from \(e\), and cardinality three otherwise, because \(t^2=e\) implies \(t=t^3=te=e\). Exactly \(D_e-1\) idempotent parameter maps are nonpermutations, and one is \(t=e\); thus the three coefficients of \(q_e\) are \(1,D_e-2,A_e-B_e-D_e+1\).

**4. Characterization of commuting pairs.** For a nonidentity \(e\), call a parameter even if \(t\) is an even permutation, odd if it is an odd permutation, and nonpermutation otherwise. The normal-form multiplication table has three actions on a second parameter pair \((u,f)\): an odd left parameter returns \((u,f)\); an even left parameter returns \((u^2,f)\); a nonpermutation left parameter returns \((f,f)\). The special \(b_0\) sends \((u,f)\) to \((u^2,u^2)\). Equality of the two composite parameter pairs yields the following complete criterion. Two even-type elements commute exactly when their \(e\)'s agree, as do two nonpermutation-type elements. Two odd-type elements commute exactly when they are equal. A mixed odd/even pair commutes exactly when the even parameter is \(\phi_{\mathrm{id},e}\) with the same \(e\). A mixed odd/nonpermutation pair commutes exactly when the nonpermutation parameter is \(\phi_{e,e}\) with the same \(e\). A mixed even/nonpermutation pair commutes exactly when the nonpermutation parameter is \(\phi_{e,e}\) with the same \(e\). The element \(b_0\) commutes with all even and odd types but with no nonpermutation type other than itself (which is already \(b_0\)); its self-pair contributes \(xy\). These are equality statements derived from the four multiplication cases, not assumptions about commutativity.

**5. Assigning both ranks.** At fixed nonidentity \(e\), even--even pairs contribute \(p_e(x)p_e(y)\), nonpermutation--nonpermutation pairs contribute \(q_e(x)q_e(y)\), identical odd pairs contribute \(O_ex^3y^3\), mixed odd--even pairs contribute \(O_e(x^3y^2+x^2y^3)\), mixed odd--nonpermutation and \(b_0\)--odd pairs together contribute \(2O_e(x^3y+xy^3)\), and mixed even--nonpermutation and \(b_0\)--even pairs contribute \(2(xp_e(y)+yp_e(x))\). No other pairs commute. Adding across \(e\) and including the \(b_0\) self-pair proves the displayed bivariate formula.

**6. Partition conversion and exponential formula.** An idempotent \(e\) is a set partition into kernel blocks, each with a distinguished root. For a fixed fiber-size partition \(\lambda\), the number of such labeled rooted partitions is \(w_\lambda\). Hence any product weight \(\prod_i w_{s_i}\) sums over \(e\) to \(n![z^n]\mathscr B(w;z)\) by the exponential formula. Setting \(x=y=1\) in Step 5 and simplifying yields \(1+\sum_{e\ne\mathrm{id}}(E_e^2+N_e^2+7O_e+4E_e)\). Expand
\[
 E_e^2+N_e^2+7O_e+4E_e
 =A_e^2-2A_eB_e+\tfrac54B_e^2+\tfrac12B_eC_e+\tfrac14C_e^2+\tfrac{11}{2}B_e-\tfrac32C_e.
\]
For the excluded \(e=\mathrm{id}\), the right side is \(5\), and its associated single \(b_0\) self-pair replaces this by \(1\). Thus the subtraction is exactly \(4e^z\), proving the formal exponential generating function and the theorem.

## Verification
The accompanying standard-library Python script `verify_commuting.py` independently implements (i) the partition-weighted joint-rank formula, (ii) the exponential Bell recurrence for the unweighted totals, and (iii) direct evaluation of the endomorphisms \(\phi_{t,e}\) on representative permutation and nonpermutation elements. It checks all pairs in the \(\phi\)-family exhaustively for \(n\leq4\), where the exceptional additional endomorphisms are deliberately *not* included, and checks \(12500\) randomly selected actual map-pairs for \(n=5\). The two exact counting algorithms agree through \(n=8\). Finite tests are consistency evidence, not a proof for all \(n\); the argument in Steps 1--6 supplies the all-degree proof.

Reproduce using `python3 verify_commuting.py` with no third-party dependencies. A successful run terminates with `COMMUTING_SINGULAR_ENDOMORPHISM_CENSUS_CHECKS_PASSED`.

## Relationship to prior work
Schein and Teclezghi (1998) classify all endomorphisms and count them; Gould, Grau, and Johnson (2023) give the structural multiplication rules, rank/type decomposition, and semigroup Green theory. The present result *takes those published structural results as inputs* and counts an additional two-object invariant: commuting ordered pairs with **both** image ranks retained, including nonregular singular types. The work is not a rediscovery of the one-object rank totals or a claim of a new normal form.

Related previously released enumerations restricted to idempotent endomorphisms or to commuting pairs in other transformation semigroups do not imply the present nonidempotent joint-rank matrix without further analysis. No claim of independently certified historical priority is made.

## Limitations
The result is confined to the canonical singular subsemigroup and excludes the unit automorphisms of \(\operatorname{End}(\mathcal T_n)\); it therefore does *not* count all commuting pairs in the whole endomorphism monoid. The full formula requires \(n\geq5\); at \(n=4\) there are additional rank-seven endomorphisms. The associated small-degree generating-function coefficients describe only the standard \(\phi\)-family. The work does not claim a sharp asymptotic law for the commuting probability. A direct earlier enumeration covering the same bivariate invariant may exist outside the inspected literature.

## References
1. V. Gould, A. Grau, and M. Johnson, *The structure of End(\(\mathcal T_n\))*, first arXiv version posted 2023-07-21, arXiv:2307.11596, https://arxiv.org/abs/2307.11596 . In particular Section 2 (normal form, rank, multiplication), and Section 3 (idempotents).
2. B. M. Schein and B. Teclezghi, *Endomorphisms of finite full transformation semigroups*, Proceedings of the American Mathematical Society 126 (1998), 2579--2587, https://doi.org/10.1090/S0002-9939-98-04764-9 .
3. A. Grau, *Aspects of endomorphism monoids of certain algebras*, Ph.D. thesis, University of York (2023), chapter on full transformation semigroup endomorphisms, https://etheses.whiterose.ac.uk/id/eprint/33804/ .
