# Exact Lie-bracket fibers of the minimal nonzero nilpotent orbit over finite fields

## Finding

Let \(k=\mathbb F_q\), where \(q\) is any prime power, and let \(n\ge2\). Consider the minimal nonzero nilpotent conjugacy class
\[
\mathcal N=\{A\in M_n(k): A^2=0,\ \operatorname{rank}A=1\}.
\]
For every prescribed target \(C\in M_n(k)\), the theorem gives the number of **ordered** pairs \((A,B)\in\mathcal N^2\) satisfying \([A,B]=AB-BA=C\).

Put
\[
L_m=\frac{q^m-1}{q-1},\quad N=L_n(q^{n-1}-1),\quad
Z=N\left[(q^{n-1}-1)+(L_{n-1}-1)(q^{n-2}-1)\right].
\]
Then the complete fiber formula is
\[
F_{n,q}(C)=\begin{cases}
Z,&C=0,\\
2q^{n-1}(q^{n-2}-1),& C\ne0,\ \operatorname{rank}C=1,\ C^2=0,\\
2(q-1),&q\text{ odd},\ C\sim\operatorname{diag}(t,-t,0_{n-2}),\ t\in k^\times,\\
q(q^2-1),&q\text{ even},\ C\sim\operatorname{diag}(t,t,0_{n-2}),\ t\in k^\times,\\
0,&\text{otherwise}.
\end{cases}
\]
The zero block \(0_{n-2}\) is absent in dimension two. In that dimension the rank-one coefficient equals zero, so no rank-one output occurs. In odd characteristic the rank-two spectral parameter is defined up to sign; in characteristic two it is unique. Rank-two outputs are always split semisimple, despite both inputs being nonzero nilpotent.

The numbers of distinct rank-two targets are, respectively,
\[
\#\mathcal I_2=\begin{cases}
Nq^{2n-3}/2,&q\text{ odd},\\
N(q-1)q^{2n-4}/(q^2-1),&q\text{ even}.
\end{cases}
\]
The image has size \(1+\#\mathcal I_2\) when \(n=2\), and \(1+N+\#\mathcal I_2\) when \(n\ge3\). These are exact integers.

## Assumptions and scope

The field \(k\) is any finite field, the dimension \(n\) is any integer at least two, and ranks and similarity refer to matrices over \(k\). No characteristic restriction or algebraic closure is assumed. All factor matrices are **nonzero** and square-zero of rank one. The bracket is the additive Lie commutator, not the group commutator. Counts use ordered pairs of actual matrices, not pairs modulo simultaneous conjugation. The rank-two similarity classes in the formula consist of the indicated direct sum of a two-dimensional semisimple block and the zero block.

## Proof

**Step 1: unique rank-one parametrization.** Every element of \(\mathcal N\) is \(A=u\varphi\), with nonzero \(u\in k^n\), nonzero \(\varphi\in(k^n)^*\), and \(\varphi(u)=0\). Fix one normalized nonzero representative of each projective line for \(u\); then \(\varphi\) is unique. There are \(L_n\) possible image lines and \(q^{n-1}-1\) possible nonzero covectors annihilating each line, so \(|\mathcal N|=N\).

**Step 2: all possible output types.** Write \(A=u\varphi\), \(B=v\psi\), put \(\alpha=\varphi(v)\), \(\beta=\psi(u)\), and calculate
\[
[A,B]=\alpha u\psi-\beta v\varphi.
\]
If \(\alpha=\beta=0\), the bracket is zero. If exactly one is zero, the bracket is nonzero rank one and squares to zero because its row covector annihilates its image vector. If both are nonzero, \(u,v\) are linearly independent and so are \(\varphi,\psi\). The bracket has rank two with image \(U=ku+kv\), and
\[
[A,B]u=(\alpha\beta)u,\qquad [A,B]v=-(\alpha\beta)v.
\]
The restriction to \(U\) is invertible, hence \(k^n=U\oplus\ker[A,B]\). Thus the bracket is similar to the asserted rank-two diagonal form. In characteristic two both eigenvalues agree, but the image is still a direct sum of two independent eigendirections.

**Step 3: the zero fiber.** For a fixed \(A=u\varphi\), commutator zero forces \(\varphi(v)=\psi(u)=0\). The line \(kv\) can be \(ku\), giving \(q^{n-1}-1\) choices for the covector \(\psi\), or one of the other \(L_{n-1}-1\) lines of \(\ker\varphi\), giving \(q^{n-2}-1\) choices for \(\psi\) annihilating the two-dimensional span \(ku+kv\). Multiplying by the \(N\) choices of \(A\) proves \(F(0)=Z\), including the dimension-two boundary.

**Step 4: the rank-one fiber.** Fix a nonzero rank-one square-zero target \(C=u_0\chi\), with fixed nonzero \(u_0\) and nonzero \(\chi\) satisfying \(\chi(u_0)=0\). In an ordered pair with \(AB=C\), the rank-one matrix \(A=u_0\varphi\) has image line \(ku_0\), and \(B=v\psi\) must satisfy \(\alpha=\varphi(v)\ne0\), \(\psi=\chi/\alpha\), and \(\chi(v)=0\). Since \(\varphi(u_0)=0\), the line \(kv\) must be distinct from \(ku_0\). Among the \(L_{n-1}\) lines of \(\ker\chi\), there are \(L_{n-1}-1\) eligible lines. For a fixed normalized \(v\), exactly \((q-1)q^{n-2}\) covectors satisfy \(\varphi(u_0)=0\) and \(\varphi(v)\ne0\). Thus the number of pairs with \(AB=C\) is
\[
(L_{n-1}-1)(q-1)q^{n-2}=q^{n-1}(q^{n-2}-1).
\]
For every such pair \(\psi(u_0)=\chi(u_0)/\alpha=0\), hence \(BA=0\). The disjoint case \(AB=0\), \(-BA=C\) has the same count by swapping the two factors. Both cross-products cannot be nonzero when the bracket has rank one, by Step 2. Doubling yields the claimed rank-one coefficient.

**Step 5: the rank-two fiber.** Suppose \(C\) has the stated rank-two semisimple form, with image \(U\) and eigenvalues \(t,-t\), where \(t\ne0\). Any factor pair has \(ku=L\) and \(kv=M\), two distinct eigenlines in \(U\), and the eigenvalue of \(C\) on \(L\) is the scalar \(\alpha\beta\). Conversely choose such ordered lines \((L,M)\) and fixed nonzero vectors \(u\in L\), \(v\in M\). Writing \(C(w)=c_u(w)u+c_v(w)v\), choose any \(\alpha\in k^\times\), set \(\beta=t_L/\alpha\), where \(t_L\) is the eigenvalue on \(L\), and define
\[
\psi=c_u/\alpha,\qquad\varphi=-c_v/\beta.
\]
Since \(C(u)=t_Lu\) and \(C(v)=-t_Lv\), these satisfy \(\varphi(u)=\psi(v)=0\), \(\varphi(v)=\alpha\), \(\psi(u)=\beta\), and \([u\varphi,v\psi]=C\). Each ordered eigenline pair therefore yields exactly \(q-1\) ordered factor pairs, without duplication. In odd characteristic there are exactly two choices \((L,M)\), corresponding to the two distinct eigenvalues. In characteristic two all \(q+1\) lines in \(U\) are eigendirections, and there are \(q\) choices for the distinct second line, giving \(q(q+1)\) ordered line pairs. This proves both rank-two coefficients and establishes that every stated target is attained.

**Step 6: rank-two target counts and mass check.** For a fixed \(A=u\varphi\), the number of lines \(kv\) not in \(\ker\varphi\) is \(q^{n-1}\). Once such a line has been chosen, there are \((q-1)q^{n-2}\) nonzero covectors \(\psi\) satisfying \(\psi(v)=0\), \(\psi(u)\ne0\). The number of ordered factor pairs producing rank-two brackets is therefore \(N(q-1)q^{2n-3}\). Dividing by the rank-two target-fiber size from Step 5 proves both target counts. The remaining pairs are precisely the zero and rank-one cases, so the fiber mass is \(N^2\), as it must be.

## Verification

The standalone file `verify_fibers.py` enumerates every factor by a unique projective-vector/covector representation over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7\) in the tested dimensions. It compares all nonzero output multiplicities, zero multiplicity, spectral restrictions, and total mass against the theorem. It checks every possible matrix target for nine cases; the largest listed case \((n,q)=(3,5)\) checks all attained targets and the mass and support criteria but does not exhaust its unattained matrix targets. The exhaustive all-target cases include \((n,q)=(4,2)\), \((3,4)\), and \((3,3)\).

The separate file `verify_literal.py` constructs the factor matrices, uses literal matrix multiplication to form \(AB-BA\), and independently checks all attained fibers and total pair mass for \((n,q)=(2,3),(2,5),(3,2),(3,3),(4,2)\). Both programs' outputs appear in `checks.txt`. These finite tests corroborate but do not replace the unlimited algebraic proof.

## Relationship to prior work

Zoque's 2009 study of almost commuting nilpotent matrices analyzes irreducible components of spaces where the commutator has rank at most one. It does not enumerate the prescribed brackets of pairs constrained to the minimal nonzero nilpotent orbit, nor give the rank-two semisimple fibers. Britnell and Wildon's 2010 preprint determines which nilpotent similarity classes admit commuting representatives and develops finite-field centralizer types. This establishes different existence and orbit relations, not a target-by-target additive-bracket multiplicity formula. The rank-one-product calculation is a special component of the proof, but individual product multiplicities alone do not determine the correlated difference \(AB-BA\): Steps 2 and 5 provide the additional simultaneous eigenline classification.

The closest research context is the geometry of low-rank commutators and nilpotent class centralizers. Searches did not reveal a directly equivalent complete prescribed-fiber formula; this absence is **not** a proof of historical priority. A more general unlocated orbital-convolution or finite-Lie-algebra counting identity could imply the formula.

## Limitations

The theorem treats the additive bracket of **two nonzero rank-one square-zero** matrices. It makes no claim for higher-rank nilpotent factors, arbitrary nilpotent pairs, multiplicative group commutators, or simultaneous-conjugacy classes of witness pairs. The result is algebraically proved but has not undergone independent mathematical review. Historical novelty remains provisional because broader orbit-convolution formulas may be relevant.

## References

1. E. Zoque, *On the variety of almost commuting nilpotent matrices*, arXiv:0903.2032v1, first public version March 11, 2009. https://arxiv.org/abs/0903.2032
2. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811v1, first public version January 6, 2010; Journal of the London Mathematical Society 83 (2011), 470–492. https://arxiv.org/abs/1001.0811
