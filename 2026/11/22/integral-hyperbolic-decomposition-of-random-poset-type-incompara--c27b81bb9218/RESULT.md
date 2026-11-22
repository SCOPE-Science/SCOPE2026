# Integral hyperbolic decomposition of random-poset type incomparability over named chains

## Finding
Let \(\mathcal P\) be the countable universal homogeneous strict partial order (the random poset), and let \(a_1<\cdots<a_n\) be \(n\geq1\) individually named parameters forming an induced chain. Let \(\mathcal T_n\) be the complete nonalgebraic one-point types over this chain. Index a symmetric integer matrix \(M_n\) by \(\mathcal T_n\), with entry one if and only if the two indexed types admit **distinct, incomparable** realizations in \(\mathcal P\), and zero otherwise. The two types may coincide; the entry then tests two distinct realizations of that one type.

Put \(N_n=\binom{n+2}{2}\) and \(H=\begin{pmatrix}0&-1\\-1&0\end{pmatrix}\). For every \(n\geq1\), an explicitly specified integer matrix \(U_n\in\operatorname{GL}_{N_n}(\mathbb Z)\) satisfies
\[
\boxed{U_n^{\mathsf T}M_nU_n= [1]\oplus H^{\oplus n}\oplus 0_{\binom n2}.}
\]
In particular,
\[
\boxed{\operatorname{SNF}_{\mathbb Z}(M_n)=\operatorname{diag}(I_{2n+1},0_{\binom n2}),}
\qquad
\boxed{\operatorname{inertia}_{\mathbb R}(M_n)=(n+1,n,\binom n2).}
\]
Thus the rank is \(2n+1\) over every field, the integer cokernel has no finite torsion, and the real signature equals one. Moreover, the **entire integral null lattice** has an explicit primitive basis indexed by pairs \(1\leq i\leq j\leq n-1\). A principal submatrix on just \(2n+1\) boundary types has determinant \((-1)^n\).

## Assumptions and scope
The language is the pure strict-order language, with all old parameters named separately and no additional predicates or functions. The relation in the matrix is existential incomparability of **two** new distinct realizations, not incomparability forced for all realizations and not the count of full two-point types. The type set includes only points distinct from every old parameter. Matrices have integral zero-one entries, including diagonal entries; they are not the loopless adjacency matrices of a simple graph. Congruence is the relation \(A\mapsto U^{\mathsf T}AU\) for integer unimodular \(U\).

## Proof
**1. One-point types are intervals.** Introduce \(a_0,a_{n+1}\) only as formal endpoint markers, not actual elements. A type is uniquely represented by a pair \((i,j)\) with \(0\leq i\leq j\leq n\): its realization \(x\) satisfies \(a_k<x\) exactly when \(1\leq k\leq i\), and \(x<a_k\) exactly when \(j<k\leq n\). The old elements \(a_{i+1},\dots,a_j\) are incomparable with \(x\). The inequalities \(i\leq j\) are forced by transitivity; conversely each such pattern is a finite partial-order extension and is realized by homogeneity and universality. Since finite induced isomorphisms extend to automorphisms, this quantifier-free incidence pattern determines the complete one-point type. Hence \(\mathcal T_n\) corresponds bijectively to the nonempty discrete closed intervals \([i,j]\) of the \((n+1)\)-point chain \(\{0,\dots,n\}\), and \(|\mathcal T_n|=N_n\).

**2. Exact binary feasibility.** For type intervals \([i,j]\) and \([k,\ell]\), two distinct realizations \(x,y\) can be declared incomparable precisely when
\[
\boxed{M_n([i,j],[k,\ell])=\mathbf1\{i\leq\ell\text{ and }k\leq j\}.}
\]
Necessity: if \(j<k\), then the old witness \(a_{j+1}\) (whose index is at most \(k\)) satisfies \(x<a_{j+1}<y\), forcing \(x<y\); the case \(\ell<i\) is dual. Sufficiency: whenever the two intervals intersect, add incomparable \(x,y\) with the specified old incidences. Transitivity holds inside the old chain and separately for each new point; the only possible missing transitivity conclusions linking the two new points are precisely the forbidden witnesses just excluded. There is no cycle, so this is a finite strict poset and embeds over the old chain into \(\mathcal P\). In particular the diagonal entries are one, since each type can be realized twice with no comparison between the new points.

**3. An explicit integral null basis.** Write \(e_{ij}\) for the standard basis vector indexed by \([i,j]\); let \(f=e_{0n}\), \(L_j=e_{0j}\) for \(0\leq j<n\), and \(R_i=e_{in}\) for \(1\leq i\leq n\). For any interval \([k,\ell]\), direct substitution in Step 2 gives the row identity
\[
M_n([i,j],[k,\ell])=M_n([0,j],[k,\ell])+M_n([i,n],[k,\ell])-M_n([0,n],[k,\ell])
\]
for every internal interval \(1\leq i\leq j\leq n-1\). Consequently
\[
w_{ij}=e_{ij}-e_{0j}-e_{in}+e_{0n}
\]
is in the integral kernel. The \(\binom n2\) vectors \(w_{ij}\) are linearly independent over \(\mathbb Z\), because each has coefficient one at its own unique interior interval and zero at every other interior interval.

**4. Boundary hyperbolic core.** First take the \(2n+1\) boundary columns \(f\), \(u_j=L_j-f\) for \(0\leq j<n\), and \(v_i=R_i-f\) for \(1\leq i\leq n\). Their pairings under \(M_n\) are
\[
\langle f,f\rangle=1,\quad\langle f,u_j\rangle=\langle f,v_i\rangle=0,\quad
\langle u_j,u_k\rangle=\langle v_i,v_h\rangle=0,
\quad\langle u_j,v_i\rangle=-\mathbf1\{j<i\}.
\]
Now set \(u'_j=u_j-u_{j+1}\) for \(0\leq j<n-1\), and \(u'_{n-1}=u_{n-1}\). Then \(\langle u'_j,v_i\rangle=-\mathbf1\{i=j+1\}\), while every other pairing among the \(u'\)'s, \(v\)'s, and \(f\) is zero except \(\langle f,f\rangle=1\). Thus in the ordered basis \((f,u'_0,v_1,u'_1,v_2,\dots,u'_{n-1},v_n)\), the boundary matrix is precisely \([1]\oplus H^{\oplus n}\).

**5. Unimodularity of the entire transformation.** Append all \(w_{ij}\) from Step 3 to the ordered boundary basis. The appended columns each have coefficient one at a unique interior coordinate and have support elsewhere only on boundary coordinates. On boundary coordinates, replacing \(e_{0j},e_{in}\) by \(u_j=L_j-f\), \(v_i=R_i-f\), and taking adjacent differences of the \(u_j\)'s are unitriangular integer operations. Therefore the whole change-of-basis matrix is integer unimodular. Every \(w_{ij}\) is orthogonal to all columns, hence the asserted direct-sum congruence follows. This proves exact rank over any field, the integral Smith factors, the inertia, and the primitive kernel basis, without extrapolating from finite cases.

The boundary principal minor in the *original* basis has determinant \((-1)^n\): its change of basis to the displayed hyperbolic core is unimodular and each \(H\) has determinant \(-1\).

## Verification
The accompanying standalone `verify.py` uses only the Python 3 standard library. Running `python3 verify.py` constructs the complete integer matrix and explicit unimodular transformation independently for \(0\leq n\leq9\); it checks the exact congruence, exact integer determinant of the basis transformation, and every interior row relation. It also independently constructs the two-new-point relation and checks all transitivity triples for every pair of types for \(0\leq n\leq5\). The recorded output in `verification_output.txt` ends with `ALL_CHECKS_PASS`.

These finite computations corroborate the construction; Steps 1–5 prove the theorem for arbitrary \(n\), and the finite checks alone would not establish the universal statement.

## Relationship to prior work
Pach, Pinsker, Pluhár, Pongrácz and Szabó define the random partial order and its incomparability reduct and prove the relevant one-point extension property; their main theorem classifies reducts, not the integral arithmetic of a finite-base type-feasibility matrix. Ganian, Hliněný, Kráľ, Obdržálek, Schwartz and Teska study first-order model checking of interval graphs, not this full discrete family’s zero-one intersection-matrix congruence. Billionnet studies interval-graph adjacency patterns, matrix envelopes and ordering problems; his matrix-profile notion is not the Smith form, inertia, or integer congruence in this result.

Two relevant already-published findings are *Order-polynomial spectra of tuple types over chains in the generic partial order* (2026) and *Six rank-three theories of complete discrete-interval intersection graphs* (2026). The former proves scalar tuple counts through endpoint-poset order polynomials; those counts do not determine the integral kernel or Smith factors of the existential incomparability matrix. The latter classifies first-order quantifier-rank-three theories of the **loopless** interval graph family; its proof and claim give neither an integral congruence nor inertia for the looped intersection matrices. The interval encoding itself, and the basic one-type count, are established background rather than claimed discoveries. The contribution asserted here is the explicit primitive all-size hyperbolic decomposition of the pair-feasibility form.

## Limitations
The result is for finite **chain** parameter sets, not arbitrary finite posets. It describes pairwise *existential* incomparability, not an entire complete two-point type count, a higher-arity feasibility tensor, or ordinary eigenvalues. An earlier equivalent congruence may exist under a different interval-graph or integral-form terminology; search and accessible-source inspection cannot guarantee historical uniqueness. No independent mathematical audit has been conducted.

## References
1. P. P. Pach, M. Pinsker, G. Pluhár, A. Pongrácz and C. Szabó, *Reducts of the random partial order*, arXiv:1111.7109v1 (first public 2011-11-30), Sections 1–3; subsequent journal publication in *Advances in Mathematics* 267 (2014), 94–120. https://arxiv.org/abs/1111.7109
2. R. Ganian, P. Hliněný, D. Kráľ, J. Obdržálek, J. Schwartz and J. Teska, *FO Model Checking of Interval Graphs*, arXiv:1302.6043v1 (first public 2013-02-25), Sections 2–3; *Logical Methods in Computer Science* 11(4:11) (2015). https://arxiv.org/abs/1302.6043
3. A. Billionnet, *On interval graphs and matrice profiles*, *RAIRO Recherche opérationnelle* 20 (1986), 245–256, Sections 1–3. https://www.numdam.org/item/RO_1986__20_3_245_0/
4. *Order-polynomial spectra of tuple types over chains in the generic partial order*, scientific record (2026-10-26). https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-order-polynomial-spectra-of-tuple-types-over-chains-in-the-gener--67a71af3c8ab
5. *Six rank-three theories of complete discrete-interval intersection graphs*, scientific record (2026-11-02). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-six-rank-three-theories-of-complete-discrete-interval-intersecti--7082ff1cf8a2
