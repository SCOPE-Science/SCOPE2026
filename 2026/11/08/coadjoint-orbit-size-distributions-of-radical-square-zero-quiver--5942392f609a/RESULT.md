# Coadjoint orbit-size distributions of radical-square-zero quiver unit groups and the Tutte polynomial

## Finding
Let \(Q\) be any finite quiver with \(n\ge1\) vertices and finite arrow multiset \(E\), allowing loops, parallel arrows, oppositely directed arrows, and disconnected components. Let \(k=\mathbb F_q\) for an arbitrary prime power \(q\). Put \(A=kQ/J^2\), with \(J\) the arrow ideal, and \(G=A^\times\). The Lie algebra \(\mathfrak g=A^-\) is the underlying vector space of \(A\) with the commutator bracket, and \(G\) acts on \(\mathfrak g^*\) by the coadjoint action induced from conjugation in \(A\).

Let \(\Gamma\) be the underlying undirected multigraph of \(Q\), retaining loops and parallel edges. For \(S\subseteq E\), write \(c(S)\) for the number of connected components of the spanning multigraph \((Q_0,S)\), with isolated vertices counted, and \(r(S)=n-c(S)\). Let \(c=c(E)\) and \(R=n-c\). For \(0\le j\le R\), let \(O_j(Q,q)\) be the number of distinct coadjoint orbits of cardinality \([q(q-1)]^j\). Then

\[
\boxed{\displaystyle
O_j(Q,q)=\sum_{\substack{S\subseteq E\\r(S)=j}}q^{n-j}(q-1)^{|S|-j}.}
\]

Consequently, the complete orbit-size enumerator, with its exponent measuring graph rank (not the cardinality directly), is

\[
\boxed{\displaystyle
\mathcal O_{Q,q}(z)=\sum_{j=0}^{R}O_j(Q,q)z^j
=q^c z^R T_{\Gamma}\!\left(1+\frac qz,q\right),}
\]

where \(T_\Gamma\) is the ordinary Tutte polynomial of the graphic matroid, including its loop and parallel-edge conventions. The expression on the right is a polynomial despite the displayed rational substitution. In particular the **total** number of distinct coadjoint orbits is

\[
\boxed{\displaystyle K_Q(q)=q^cT_\Gamma(q+1,q).}
\]

These formulas are valid in every characteristic. They depend on the underlying cycle matroid, together with the number of connected components, and not on arrow orientations. For a forest with \(m\) arrows, \(\mathcal O_{Q,q}(z)=q^c(q+z)^m\). For the loopless three-cycle, \(\mathcal O_{Q,q}(z)=q^3+3q^2z+q(q+2)z^2\).

## Assumptions and scope
All objects are finite. The algebra \(A=kQ/J^2\) has basis \(\{e_v:v\in Q_0\}\cup\{a:a\in E\}\), with \(e_ve_w=\delta_{v,w}e_v\), \(e_{s(a)}a=a=ae_{t(a)}\), and all products of two arrows zero. Thus \(A\) has vector-space dimension \(n+|E|\) and is unital even for disconnected \(Q\). The unit group is \(G=A^\times\), not merely the radical subgroup \(1+J\). The coadjoint action means \((g\cdot f)(x)=f(g^{-1}xg)\). Distinct orbits, rather than points of the dual vector space, are counted. The dimension of a Kirillov form is separate from the finite cardinality of a group orbit; no orbit-method correspondence with irreducible characters is asserted.

The Tutte polynomial convention is
\[
T_\Gamma(x,y)=\sum_{S\subseteq E}(x-1)^{R-r(S)}(y-1)^{|S|-r(S)}.
\]
The rank of a loop is zero, and parallel edges are distinct elements in the subset sum.

## Proof
**Step 1: the unit group and its action.** Write \(D=\bigoplus_{v\in Q_0}ke_v\) and \(A=D\oplus J\). Since \(J^2=0\), the invertible elements of \(A\) are exactly those whose diagonal coefficients are all nonzero, and
\[
G=T\ltimes U,\qquad T=(k^\times)^{Q_0},\quad U=1+J\cong(J,+).
\]
A functional \(f\in\mathfrak g^*\) is uniquely specified by its diagonal coefficients \(\alpha_v=f(e_v)\) and arrow coefficients \(w_a=f(a)\). Write \(S(f)=\{a:w_a\ne0\}\).

For \(t=\sum_vt_ve_v\in T\), conjugation by \(t^{-1}\) fixes all vertex idempotents and multiplies arrow \(a\) by \(t_{t(a)}/t_{s(a)}\). Thus \(T\) fixes \(\alpha\) and acts on \(w_a\) by these ratios. For \(u=1+\sum_ay_aa\in U\), the equality \(u^{-1}=1-\sum_ay_aa\) and the relation \(J^2=0\) give
\[
(u\cdot f)(e_v)=\alpha_v+\sum_a(\mathbf1_{v=s(a)}-\mathbf1_{v=t(a)})w_ay_a,
\qquad (u\cdot f)(a)=w_a.
\]
This formula also holds for loops, whose two endpoint contributions cancel, in any characteristic.

**Step 2: the weighted incidence image.** Let \(B_S\) be the \(n\)-by-\(|S|\) oriented incidence matrix of the spanning multigraph \((Q_0,S)\), with column \(e_{s(a)}-e_{t(a)}\) for each active arrow. The possible changes of \(\alpha\) under \(U\) comprise precisely the column space \(L_S\) of \(B_S\): each active coefficient \(w_a\) is nonzero, so scaling each column by \(w_a\) does not affect its span. The incidence matrix has rank \(n-c(S)=r(S)\) over **every** field. Indeed, the columns of a spanning forest are linearly independent by successively removing leaves, all other nonloop columns telescope along forest paths, and loop columns are zero. Therefore \(|L_S|=q^{r(S)}\), and the quotient \(k^n/L_S\) has exactly \(q^{n-r(S)}\) elements.

**Step 3: torus orbits of arrow coefficients.** Fix the support \(S\). The number of arrow-weight vectors with this exact support is \((q-1)^{|S|}\). The stabilizer in \(T\) of any such vector consists precisely of vertex scalars equal across every edge of \(S\). It has size \((q-1)^{c(S)}\). Hence all these \(T\)-orbits have size \((q-1)^{r(S)}\), and there are exactly \((q-1)^{|S|-r(S)}\) of them. This applies without change to disconnected graphs, loops and parallel edges.

**Step 4: the combined coadjoint orbits.** The subspace \(L_S\) depends only on the support \(S\), not on its particular nonzero weights. Torus action fixes the diagonal coordinates, so it induces the identity on the quotient \(k^n/L_S\). Every torus orbit of active weight vectors therefore lifts to exactly \(q^{n-r(S)}\) distinct \(G\)-coadjoint orbits, indexed by these diagonal cosets. Each lifted orbit has size
\[
q^{r(S)}(q-1)^{r(S)}=[q(q-1)]^{r(S)}.
\]
Multiplication gives \(q^{n-r(S)}(q-1)^{|S|-r(S)}\) orbits of this size for each exact support \(S\). Summing proves the stated coefficients. As a normalization check, multiplying the number of such orbits by their common size and summing over supports gives
\[
\sum_{S\subseteq E}q^n(q-1)^{|S|}=q^{n+|E|}=|\mathfrak g^*|.
\]
Thus no dual functionals are omitted or double-counted.

**Step 5: the Tutte transform.** Substituting \(x=1+q/z\), \(y=q\) into the defining Tutte expansion yields
\[
q^cz^RT_\Gamma(1+q/z,q)
=\sum_{S\subseteq E}q^{n-r(S)}(q-1)^{|S|-r(S)}z^{r(S)},
\]
which is exactly the orbit-size enumerator. Setting \(z=1\) proves the total-count formula. For a forest, every edge subset has \(r(S)=|S|\), giving \(q^c(q+z)^{|E|}\); for a triangle the subsets of cardinalities zero, one, two, three have ranks zero, one, two, two respectively, giving the stated example. This completes the proof.

## Verification
Three standalone scripts are included. Run them with a standard Python interpreter:

```
python verify_orbits.py
python verify_gf4.py
python verify_tutte.py
```

`verify_orbits.py` constructs finite-field coadjoint orbits by breadth-first search under explicit elementary unipotent and diagonal generators for several quivers over \(\mathbb F_2\) and \(\mathbb F_3\). It checks the complete orbit-cardinality histograms against the support formula, including loops, parallel arrows, directed cycles, paths and isolated vertices. `verify_gf4.py` independently uses the polynomial representation \(\mathbb F_4=\mathbb F_2[u]/(u^2+u+1)\) with its additive and multiplicative generators and checks four quivers. `verify_tutte.py` evaluates Tutte polynomials independently by deletion-contraction and compares against the support sum for seven multigraphs and field orders \(2,3,4,5,7,8,9\), including disconnected graphs and loops. See `verification_output.txt` for complete outputs. The three success markers are `ALL_COADJOINT_ORBIT_CHECKS_PASS`, `ALL_GF4_COADJOINT_ORBIT_CHECKS_PASS`, and `ALL_TUTTE_RECURSION_CHECKS_PASS`.

All infinite assertions are proved above; finite checks are supplemental, not substitutes for proof. In particular, the GF4 checker tests an actual extension field, while the Tutte checker evaluates integer polynomials at extension-field orders without enumerating those matrices.

## Relationship to prior work
Coll and Gerstenhaber's 2014 preprint studies the torus--nilpotent decomposition and Lie cohomology of poset algebras; its main statements concern cohomology and deformations, not finite-field coadjoint orbit-size distributions. Coll and Mayers (2019) derive Lie-poset index formulas, including a height-one graph formula; that counts only the minimum possible Kirillov-kernel dimension, not all finite coadjoint orbits and their multiplicities. The present theorem applies to all finite radical-square-zero quiver algebras, including arbitrary oriented cycles, loops and parallel arrows, and yields a full Tutte specialization instead of an index alone.

The general little-group theory of coadjoint orbits of semidirect products (discussed by Arathoon, 2018, with earlier references) supplies a broader framework for orbit parametrization. It does not present the finite-field multigraph support calculation, the exact cardinality of each orbit-size stratum, or the Tutte identity. Nasr-Isfahani (2016) studies singular equivalences of radical-square-zero quiver algebras, rather than conjugation-coadjoint orbit enumeration. The Tutte polynomial itself and its graphic rank expansion are classical and not claimed as new. The specific combination of incidence rank, torus weight orbits and additive coadjoint fibers is the contribution assessed here.

## Limitations
The theorem concerns the coadjoint action of the **full unit group** on the dual of the commutator Lie algebra associated with \(kQ/J^2\). It is not a formula for the number of conjugacy classes of the unit group, for its complex irreducible characters, or for the adjoint orbits of arbitrary higher-radical algebras. The result recovers a known index formula when specialized to loopless height-one posets, but does not claim that classical index result as original. Coadjoint orbit sizes over finite fields should not be conflated with powers of \(q\) determined by Kirillov-form ranks. Priority remains provisional because a general finite-field semidirect-orbit enumeration may encompass this graph-specialized Tutte formula; no independent historical audit has been performed.

## References
- V. E. Coll, Jr., and M. Gerstenhaber, *Cohomology of Lie semidirect products and poset algebras*, arXiv:1407.0428, first version 2014-07-02. https://arxiv.org/abs/1407.0428
- A. R. Nasr-Isfahani, *Singular equivalence of finite dimensional algebras with radical square zero*, arXiv:1603.04191, first version 2016-03-14. https://arxiv.org/abs/1603.04191
- V. E. Coll, Jr., and N. W. Mayers, *The index of Lie poset algebras*, arXiv:1908.06573, first version 2019-08-19, Theorem 3. https://arxiv.org/abs/1908.06573
- P. Arathoon, *A bijection between the adjoint and coadjoint orbits of a semidirect product*, arXiv:1806.08406, first version 2018-06-21, Section 1. https://arxiv.org/abs/1806.08406
- W. T. Tutte, classical Tutte polynomial and graphic rank expansion. The standard defining formula is reproduced under Assumptions and scope.
