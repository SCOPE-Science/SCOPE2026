# Complete graph spectra of rank-one evolution algebras over algebraically closed fields

## Finding

**Graph-spectrum theorem.** Let \(K\) be an algebraically closed field with \(\operatorname{char}K\ne2\), and let \(A\) be an \(n\)-dimensional evolution \(K\)-algebra with \(\dim_K A^2=1\). Write \(r=\dim_K\operatorname{Ann}(A)\) and \(d=n-r\ge1\). For an *ordered* natural basis \(E=(e_1,\ldots,e_n)\), form the directed graph \(\Gamma_E\) on \([n]\) with an arrow \(i\to j\) if the \(e_j\)-coefficient of \(e_i^2\) is nonzero.

Define \(\Gamma(T,S)\) to be the directed graph with arrow set \(T\times S\), where \(T,S\subseteq[n]\). The complete set of labeled directed graphs obtained as \(\Gamma_E\) by varying ordered natural bases of this *fixed algebra* is as follows, with all stated converses holding:

1. **Annihilator-square case:** If \(A^3=0\), then precisely the \(\Gamma(T,S)\) with \(|T|=d\), \(\varnothing\ne S\subseteq[n]\setminus T\) occur (necessarily \(r\ge1\)).
2. **Isotropic active-square case:** If \(A^3\ne0\) but \((A^2)^2=0\), then precisely the \(\Gamma(T,S)\) with \(|T|=d\) and \(|S\cap T|\ge2\) occur (necessarily \(d\ge2\)).
3. **Anisotropic active-square case:** If \((A^2)^2\ne0\), then precisely the \(\Gamma(T,S)\) with \(|T|=d\) and \(|S\cap T|\ge1\) occur.

No other graph occurs. The corresponding numbers of **distinct labeled graphs** are, respectively,
\[
\binom nd(2^r-1),\qquad
\binom nd 2^r(2^d-d-1),\qquad
\binom nd 2^r(2^d-1).
\]
The numbers of **unlabeled graph isomorphism types** are, respectively,
\[
 r,\qquad (d-1)(r+1),\qquad d(r+1).
\]
A type which cannot exist at the given \((d,r)\) is omitted, rather than counted as a separate algebra.

**Simultaneous realization.** Fix one of the three cases and admissible \((n,d,r)\). Every finite collection of graphs satisfying that case's condition with the same \(n,d\) occurs as the graph collection of natural bases of one and the same algebra of that case. Indeed, stronger: each algebra of the fixed case and invariants realizes all such graphs. Without a prescribed case, a finite family of rank-one graphs is simultaneously realizable if and only if its graphs have a common \(n\), a common number \(d\ge1\) of positive-outdegree vertices, each positive-outdegree vertex in each graph has the same nonempty out-neighborhood, and either (i) all those neighborhoods avoid the positive-outdegree vertices or (ii) all intersect them. In (i) one requires \(n-d\ge1\); in (ii) an anisotropic active-square algebra realizes the family.

## Assumptions and scope

All algebras are finite-dimensional, commutative and not assumed associative. The convention is \(A^2=\operatorname{span}\{xy:x,y\in A\}\), \(A^3=A^2 A\), and \((A^2)^2=\operatorname{span}\{uv:u,v\in A^2\}\). The three cases are intrinsic. Directed graphs include loops. The graph statements concern all *ordered* natural bases, not merely bases related by monomial transformations. The labeled graph counts enumerate distinct adjacency relations, not distinct natural bases or algebra isomorphism classes.

## Proof

**1. Intrinsic quadratic model.** Choose a nonzero \(v\) spanning \(A^2\). As the image of multiplication lies in \(Kv\), there is a unique symmetric bilinear form \(B\) such that \(xy=B(x,y)v\). Its radical is precisely \(R=\operatorname{Ann}(A)\), of dimension \(r\), and its rank is \(d\). Because \(A\) is an evolution algebra, \(B\) admits a diagonal natural basis. In any natural basis, the zero-square basis elements are exactly a basis of \(R\): if \(e_i^2=0\), then \(B(e_i,e_j)=0\) for every \(j\), hence \(e_i\in R\); conversely, every radical basis element squares to zero. Consequently precisely \(d\) sources have nonzero squares. Every such square is a *nonzero scalar multiple* of \(v\), so their out-neighborhoods all equal the support \(S\) of \(v\) in that basis. Thus every graph is \(\Gamma(T,S)\), \(|T|=d\), \(S\ne\varnothing\).

Moreover \(A^3=0\) if and only if \(v\in R\), and \((A^2)^2=0\) if and only if \(B(v,v)=0\). The scalar \(B(v,v)\) may change with the choice of \(v\), but whether it vanishes does not. In a natural basis labeled so that \(T=\{1,\dots,d\}\), write \(v=\sum_{i=1}^d z_i e_i+\sum_{j=d+1}^n t_j e_j\). Then \(v\in R\) exactly when every \(z_i=0\). Otherwise, since the active basis elements are pairwise \(B\)-orthogonal and have nonzero \(B(e_i,e_i)\), the equality \(B(v,v)=\sum_{i=1}^d B(e_i,e_i)z_i^2\) shows that \(B(v,v)=0\) and \(v\notin R\) imply at least two active \(z_i\) are nonzero. This proves all necessary restrictions.

**2. Prescribing support on the active quotient.** Choose a complement \(W\) to \(R\) on which \(B\) is nondegenerate, and identify \(A/R\cong W\). Since \(K\) is algebraically closed of characteristic not two, an orthogonal basis of \(W\) can be rescaled to have Gram matrix \(I_d\). Let \(w\) be the image of \(v\) in \(W\). For nonzero \(w\) of norm \(Q=B(w,w)\), we claim that for every prescribed subset \(U\subseteq[d]\), a coordinate vector \(z\in K^d\) of support exactly \(U\) and norm \(Q\) exists if and only if \(|U|\ge1\) when \(Q\ne0\), or \(|U|\ge2\) when \(Q=0\). Necessity is immediate. For sufficiency, if \(Q\ne0\) and \(|U|=1\), take a square root of \(Q\). For \(|U|\ge2\), choose arbitrary nonzero entries except the final one, avoiding the proper algebraic hypersurface on which the final squared entry \(Q-\sum z_i^2\) is zero; then choose a nonzero square root. The same argument works for \(Q=0\) and \(|U|\ge2\), using the fact that the sum of the chosen squares need not vanish on the torus \((K^\times)^{|U|-1}\). All choices are possible over the infinite field \(K\).

By Witt extension (or elementary orthogonal reflections), the orthogonal group of a nondegenerate quadratic space over \(K\) is transitive on nonzero vectors of any fixed norm, including the zero norm. Hence there is an orthonormal basis of \(W\) in which \(w\) has coordinates exactly \(z\). If \(w=0\), the active coordinates of \(v\) are necessarily all zero in every basis.

**3. Radical coordinates are unrestricted once the active vector is nonzero.** If \(w\ne0\), choose active orthonormal lifts \(f_1,\dots,f_d\in W\), so \(v=\sum z_i f_i+u\) with \(u\in R\) and some \(z_i\ne0\). Replacing any active lift \(f_i\) by \(f_i+h_i\), \(h_i\in R\), leaves all \(B\)-inner products and natural-basis products unchanged, but changes the radical coordinates of \(v\) to those of \(u-\sum z_i h_i\). Thus any prescribed radical coordinate vector is obtained by changing just one \(h_i\) with \(z_i\ne0\). If \(w=0\), then \(0\ne v\in R\); a change of basis in \(R\) realizes any desired *nonempty* radical support. This proves all converses for \(T=\{1,\ldots,d\}\). Permuting an ordered natural basis realizes every choice of \(T\) of size \(d\).

**4. Counting and simultaneous realizability.** For fixed \(T\), there are \(2^r-1\) admissible radical-only target sets, \(2^r(2^d-d-1)\) isotropic active target sets, or \(2^r(2^d-1)\) anisotropic active target sets, according to the case. The active source set \(T\) is intrinsic to each labeled graph (it is exactly the set of vertices of positive outdegree), giving the factor \(\binom nd\). Up to graph isomorphism, \(\Gamma(T,S)\) is completely classified by the pair \((|S\cap T|,|S\setminus T|)\), since the source set and common out-neighborhood are intrinsic and permutations of \(T\) and its complement are transitive on subsets of given sizes. This gives \(r\), \((d-1)(r+1)\), or \(d(r+1)\) unlabeled types. The construction above works separately for *every* admissible graph of each fixed algebra; choosing one basis for each graph proves simultaneous realization. Conversely, the intrinsic numbers \(d\) and the status of \(A^3\) prohibit the mixed cases in the final criterion.

## Verification

The executable `checks/replay.py` uses exact SymPy arithmetic (SymPy 1.14.0), constructs explicit invertible changes of basis by orthogonal reflections and radical shears, and checks preservation of the Gram form, support of the fixed square-generator, and all enumerators. It constructs all \(124\) allowed labeled support patterns for \(1\le d\le3\) and \(0\le r\le2\), skipping impossible cases. The archived run in `checks/output.txt` ends with `VERIFY_OK constructed_patterns=124`. These finite constructions are corroboration only; the proof above establishes the universal statement without finite enumeration.

## Relationship to prior work

The quadratic-form representation and classification by annihilator and isotropy are established in Brache–Martín Barquero–Martín González–Sánchez-Ortega (2021), and expanded to commutative algebras by Martín Barquero–Martín González–Sánchez-Ortega (2025). Boudi–Cabrera Casado–Siles Molina (2020) describe natural families and basis changes. These underlying facts are **not** claimed as new. The present graph-spectrum theorem extracts the complete support restrictions, establishes that every allowed support is realized in the *same algebra*, and gives explicit labeled and unlabeled counts and a simultaneous-graph criterion. Question 30 in Kaygorodov–Martín González–Viruel (2026) asks for simultaneous graphical realization in general. This is a solution to that question in the class \(\dim A^2=1\), not a solution for general evolution algebras. Earlier classifications contain ingredients from which some of these conclusions may be derived; their full implications are a residual priority risk.

## Limitations

No conclusion is asserted for non-algebraically-closed fields, characteristic two, rank-two-or-higher square, or for prescribed structure-matrix coefficients rather than support graphs. The formulas count graph patterns, not bases. Over nonclosed fields, quadratic-form representations and their orbits can obstruct particular target supports.

## References

1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248 (first public 2026-10-15), Question 30, https://arxiv.org/html/2610.22248.
2. C. Brache, D. Martín Barquero, C. Martín González, J. Sánchez-Ortega, *Evolution algebras with one-dimensional square*, arXiv:2103.01625 (2021), https://arxiv.org/abs/2103.01625.
3. N. Boudi, Y. Cabrera Casado, M. Siles Molina, *Natural families in evolution algebras*, arXiv:2006.14460 (2020), https://arxiv.org/abs/2006.14460.
4. D. Martín Barquero, C. Martín González, J. Sánchez-Ortega, *Commutative Algebras with One-Dimensional Square*, Mediterranean Journal of Mathematics 22 (2025), Article 48, https://link.springer.com/article/10.1007/s00009-025-02812-7.
