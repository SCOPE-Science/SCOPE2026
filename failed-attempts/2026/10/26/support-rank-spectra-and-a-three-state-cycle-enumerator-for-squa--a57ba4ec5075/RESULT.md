# Support-rank spectra and a three-state cycle enumerator for square-zero graph algebras

## Finding

For every finite simple graph \(G=(V,E)\) with \(|V|=n\) and every field \(k\), define the finite-dimensional commutative graded algebra
\[
A_G(k)=k[x_v:v\in V]/\bigl(x_v^2,\ x_ux_v\ (\{u,v\}\notin E),\ \text{all monomials of degree }3\bigr).
\]
Thus \((A_G)_1\) has basis \(x_v\), while \((A_G)_2\) has basis \(x_ux_v\) indexed by edges. For a linear form \(L=\sum_{v\in V} a_vx_v\), write \(S=\{v:a_v\ne0\}\), \(N[S]=S\cup\{v:\text{some }u\in S\text{ is adjacent to }v\}\), and \(\beta_k(S)\) for the number of connected components of the induced graph \(G[S]\) which are bipartite if \(\operatorname{char}k\ne2\), or the number of all components if \(\operatorname{char}k=2\). The empty induced graph has zero components. Then the degree-one multiplication map \(\mu_L:(A_G)_1\to(A_G)_2\) satisfies
\[
\boxed{\operatorname{rank}\mu_L=|N[S]|-\beta_k(S).}\tag{1}
\]
In particular, its rank depends on the coefficient support, not on the nonzero coefficient values.

Over any finite field \(\mathbb F_q\) of characteristic \(p\), the *full rank-frequency polynomial* is consequently
\[
\mathcal R_G(q,z):=\sum_{L\in(A_G)_1}z^{\operatorname{rank}\mu_L}
=\sum_{S\subseteq V}(q-1)^{|S|}z^{|N[S]|-\beta_p(S)}.\tag{2}
\]

For the simple cycle \(C_n\), \(n\ge4\), let \(w=q-1\), \(\varepsilon_{n,p}=1\) if \(n\) is even or \(p=2\), and \(\varepsilon_{n,p}=0\) otherwise. Set
\[
T(w,z)=\begin{pmatrix}wz&1&0\\ wz&0&1\\ wz^2&0&1\end{pmatrix}.
\]
Then, *without summation over the exponentially many supports*, all rank frequencies are given by
\[
\boxed{\mathcal R_{C_n}(q,z)=\operatorname{tr}\bigl(T(q-1,z)^n\bigr)
+\varepsilon_{n,p}(q-1)^n(z^{n-1}-z^n).}\tag{3}
\]
In particular, the matrix-trace part has an order-three recurrence: for \(s_j=\operatorname{tr}(T^j)\),
\[
s_{j+3}=(1+wz)s_{j+2}-wz(1-z)s_j\qquad(j\ge0).\tag{4}
\]
Equations (1)--(4), as one support-rank-and-cycle-enumerator theorem, are the finding. They determine every rank stratum of degree-one multiplication in the cycle family in every finite characteristic. The familiar maximal-rank (weak-Lefschetz) subcase is not asserted as new.

## Assumptions and scope

All graphs are finite, undirected, simple, with vertices regarded as labelled; field characteristic may be zero in (1) but (2)--(4) require a finite field. In (1) isolated vertices of \(G[S]\) count as bipartite components. The ideal of degree-three monomials truncates the algebra in degree two; for a triangle-free graph such as \(C_n\), \(n\ge4\), it follows already from the square and nonedge relations. Thus the cycle algebra is the standard square-zero-variable Artinian face algebra of the one-dimensional cycle complex, rather than the quotient by the *edge ideal* of the cycle.

The coefficients of \(z^r\) in (2) and (3) are literal numbers of linear forms of rank \(r\), including the zero form. Rank cannot exceed \(\min(n,|E|)\). Formulas are independent of whether \(q\) is prime or a proper prime power.

## Proof

**Support kernel.** Write \(b=\sum_{v\in V}b_vx_v\). By the defining quadratic monomial basis, \(\mu_L(b)=0\) if and only if
\[
a_ub_v+a_vb_u=0\quad\text{for every edge }\{u,v\}\in E.\tag{5}
\]
If \(v\in N[S]\setminus S\), some adjacent \(u\in S\) has \(a_u\ne0\) and \(a_v=0\); equation (5) forces \(b_v=0\). If \(v\notin N[S]\), every incident edge has both coefficients \(a\) zero, so \(b_v\) is completely unconstrained. On a vertex \(v\in S\), set \(y_v=b_v/a_v\). For every edge inside \(G[S]\), (5) becomes \(y_u+y_v=0\). On a connected component the assignments are determined by the value at one root, propagated with alternating sign along paths. In characteristic different from two, this value is free exactly when all cycles have even length, equivalently the component is bipartite; an odd cycle forces \(y=0\). In characteristic two the sign constraint disappears, and every connected component admits one free constant. The kernel therefore has dimension \(n-|N[S]|+\beta_k(S)\). Subtracting from the \(n\)-dimensional domain gives (1).

**Finite-field support count.** A prescribed support \(S\) has exactly \((q-1)^{|S|}\) coefficient assignments, all having the same rank by (1). Sum over disjoint supports to obtain (2), with the usual empty-product convention \((q-1)^0=1\) for \(S=\varnothing\).

**Cycle support statistic.** Let \(G=C_n\), \(n\ge4\), and suppose \(S\) is nonempty and proper. Every component of \(C_n[S]\) is a path, hence bipartite in every characteristic. The complementary zero vertices form cyclic blocks. Let \(r_{\ge2}(S)\) be the number of maximal cyclic zero blocks of length at least two. If a zero block has length \(\ell\), its internal \(\max(\ell-2,0)\) vertices are outside \(N[S]\); there is one component of \(C_n[S]\) per zero block. Using (1) and summing over blocks gives
\[
\operatorname{rank}\mu_L=|S|+r_{\ge2}(S).\tag{6}
\]
If \(S=\varnothing\), rank is zero. If \(S=V\), the signed-edge equations on the cycle have one-dimensional kernel precisely when the length is even or characteristic is two. Thus the full-support rank is \(n-\varepsilon_{n,p}\).

**Three-state trace.** Traverse a cyclic binary word marking supported vertices by \(1\) and unsupported vertices by \(0\). Immediately before each step, retain one of three states: \(A\) (the preceding position is \(1\)), \(B\) (exactly one consecutive preceding \(0\)), or \(C\) (at least two consecutive preceding \(0\)'s). When the new symbol is \(1\), assign a factor \(w\) for choosing its nonzero coefficient and \(z\) for its contribution to \(|S|\). If the preceding state was \(C\), assign one further \(z\) to record the end of a zero block of length at least two. A \(0\) has weight one and advances \(A\to B\to C\to C\). These transitions have exactly the matrix \(T(w,z)\) displayed above, with row indexed by the preceding state and column by the new state.

For every nonconstant cyclic word the state sequence is uniquely determined by its positions, so \(\operatorname{tr}(T^n)\) counts it with weight \(w^{|S|}z^{|S|+r_{\ge2}(S)}\). The all-zero word contributes \(1\) (constant state \(C\)). The all-one word contributes \(w^n z^n\), whereas its correct rank weight is \(w^nz^{n-\varepsilon_{n,p}}\). The stated correction yields (3). Finally,
\[
\det(\lambda I-T)=\lambda^3-(1+wz)\lambda^2+wz(1-z).
\]
Cayley--Hamilton and taking traces give (4), proving all formulas.

## Verification

The included standalone \(\texttt{verify.py}\) constructs degree-one multiplication matrices over prime fields by the explicit edge coefficients in (5), computes their ranks by modular row reduction, and separately checks (1), (6), and the polynomial matrix trace (3) by coefficient arithmetic. It exhaustively checks twelve cycle/prime combinations, three cycle cases over the extension field \(\mathbb F_4\), and *every* simple four-vertex graph for each of the primes two and three. The tested cyclic lengths range from four through eight. Running \(\texttt{python verify.py}\) prints \(\texttt{GRAPH\_LEFSCHETZ\_RANK\_ENUMERATOR\_OK 17 families}\). Larger prime-power fields are covered by the abstract proof, not by these finite experiments.

For example, the same formula gives
\[
\mathcal R_{C_5}(2,z)=1+5z^2+15z^3+11z^4,
\qquad
\mathcal R_{C_5}(3,z)=1+10z^2+80z^3+120z^4+32z^5.
\]
The distinct top-rank behavior comes solely from the full-support correction; both polynomials sum to the expected number of linear forms when \(z=1\).

As elementary consistency checks, \(\mathcal R_{C_n}(q,1)=q^n\) and the highest-rank term for odd \(n\), odd characteristic, is exactly \((q-1)^nz^n\). The latter recovers the known full-support weak-Lefschetz case and must not be counted as a separate original result.

## Relationship to prior work

Migliore--Miró-Roig--Nagel (arXiv:0811.1023, Proposition 2.2) established full-coefficient normalization for general linear forms in Artinian monomial algebras over infinite fields. Dao--Nair (arXiv:2112.09434, Proposition 3.1 and Theorem 3.3) identified multiplication by the sum of variables with an unsigned graph incidence matrix in characteristic zero and determined when it has maximal rank. These facts already account for the all-supported WLP conclusion; that conclusion is prior work, not claimed as new. The present statement computes the actual rank for *every* coefficient support and packages the resulting finite-field cycle rank distribution in a uniform size-three transfer matrix, including characteristic two.

Migliore--Nagel--Schenck (arXiv:1706.05058) analyze failure of Lefschetz properties for quotients by quadratic monomials. Nguyen--Tran (arXiv:2310.14368) analyze quotients by *edge ideals* of paths and cycles; these are not the cycle face algebras considered here, as their degree-two basis consists of nonedges. These papers were checked for a possible broader graph-algebra rank enumeration; the inspected material did not yield (3).

## Limitations

The novelty assessment is relative to the inspected literature and available indexed records. A generalized graph-support rank identity can be deduced from classical incidence-matrix reasoning and monomial coordinate rescaling; the distinctive proposed contribution is the explicit all-rank finite-field cycle enumerator and three-state recurrence, not the old criterion for generic maximal rank. An unlocated rank-enumerator or transfer-matrix result could subsume that contribution. No independent mathematical audit or claim of publication priority is made. The result does not address multiplication in degrees beyond one, higher-dimensional face complexes, scheme structure of rank loci, or edge-ideal cycle algebras.

## References

1. J. C. Migliore, R. M. Miró-Roig and U. Nagel, *Monomial ideals, almost complete intersections and the Weak Lefschetz Property*, arXiv:0811.1023, first posted 6 November 2008. https://arxiv.org/abs/0811.1023
2. J. Migliore, U. Nagel and H. Schenck, *The Weak Lefschetz property for quotients by Quadratic Monomials*, arXiv:1706.05058, first posted 15 June 2017. https://arxiv.org/abs/1706.05058
3. H. Dao and R. Nair, *On the Lefschetz Property for quotients by monomial ideals containing squares of variables*, arXiv:2112.09434, first posted 17 December 2021. https://arxiv.org/abs/2112.09434
4. H. D. Nguyen and Q. H. Tran, *The weak Lefschetz property of artinian algebras associated to paths and cycles*, arXiv:2310.14368, first posted 22 October 2023. https://arxiv.org/abs/2310.14368
