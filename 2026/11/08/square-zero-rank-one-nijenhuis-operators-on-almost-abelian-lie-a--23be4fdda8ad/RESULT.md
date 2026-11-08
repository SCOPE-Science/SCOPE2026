# Square-zero rank-one Nijenhuis operators on almost-Abelian Lie algebras: a spectral rigidity and exact census

## Finding

Let \(k\) be any field, \(m\ge2\), \(V=k^m\), and \(A\in\operatorname{End}_k(V)\). On \(L=kt\oplus V\) put \([t,v]=Av\) and \([V,V]=0\). We classify **every nonzero rank-one, square-zero** linear map \(N:L\to L\) satisfying the algebraic Lie-Nijenhuis equation
\[
[Nx,Ny]=N\bigl([Nx,y]+[x,Ny]-N[x,y]\bigr)\quad(x,y\in L).
\]
No assumption on characteristic, invertibility, semisimplicity, or separability of \(A\) is needed.

Write a nonzero rank-one map in the form
\[
N(x)=\phi(x)w,\qquad w=at+u\ne0,\quad \phi=bt^*+\psi\ne0,
\]
where \(a,b\in k\), \(u\in V\), \(\psi\in V^*\), and \(t^*(t)=1\), \(t^*(V)=0\). Here two such factorizations define the same map exactly when \((w,\phi)\mapsto(cw,c^{-1}\phi)\) for some \(c\in k^\times\). The complete classification of nonzero maps with \(N^2=0\) and vanishing Nijenhuis torsion consists of the following three disjoint cases:

1. **Augmentation-covector case:** \(\psi=0\), \(b\ne0\), \(a=0\), \(u\ne0\).
2. **Left-eigenvector case:** \(\psi\ne0\) and \(\psi\circ A=\mu\psi\) for some \(\mu\in k\), with \(ab+\psi(u)=0\) and \(at+u\ne0\).
3. **Non-eigen incidence case:** \(\psi\ne0\) with \(\psi\circ A\notin k\psi\), \(a=0\), \(0\ne u\in\ker\psi\cap\ker(\psi\circ A)\), and \(b\in k\) arbitrary.

For every prime power \(q\), put \(k=\mathbb F_q\) and
\[
E_A(q)=\sum_{\lambda\in\mathbb F_q}\left(q^{\dim\ker(A^{\mathsf T}-\lambda I)}-1\right).
\]
Equivalently, \(E_A(q)\) is the number of nonzero left eigenvectors of \(A\), with each vector counted once. The exact number \(Z_A(q)\) of distinct **nonzero rank-one square-zero Lie-Nijenhuis maps** on \(L\) is
\[
\boxed{Z_A(q)=q^m-1+\frac{q}{q-1}\left[E_A(q)(q^m-1)+(q^m-1-E_A(q))(q^{m-2}-1)\right].}
\]
It also admits the useful form
\[
\boxed{Z_A(q)=q^m-1+\frac{q(q^m-1)(q^{m-2}-1)}{q-1}+q^{m-1}(q+1)E_A(q).}
\]

The number of **all** nonzero rank-one square-zero endomorphisms of the underlying \((m+1)\)-space, without imposing the Nijenhuis equation, equals
\[
Z_{\mathrm{all}}(q)=\frac{(q^{m+1}-1)(q^m-1)}{q-1}.
\]
Their exact exclusion defect is
\[
\boxed{Z_{\mathrm{all}}(q)-Z_A(q)=q^{m-1}(q+1)(q^m-1-E_A(q)).}
\]
Thus over **every field**, not merely finite fields, all rank-one square-zero linear maps on \(L\) satisfy the Nijenhuis equation **if and only if** \(A\) is a scalar endomorphism. For finite fields, the defect measures this obstruction exactly. Adding the zero operator changes each nilpotent-operator count by one.

## Assumptions and scope

Rank always means vector-space rank. Square-zero means \(N^2=0\), and the Nijenhuis equation is the bilinear Lie-algebra identity displayed above, not a Nijenhuis tensor for a varying endomorphism field. The natural family is the codimension-one abelian-ideal construction; the zero action \(A=0\) is allowed as an abelian boundary. The classification holds over an arbitrary field; only the cardinality formulas require finite fields. No algebraic closure is assumed, and only eigenvalues in the ground finite field appear in \(E_A(q)\).

## Proof

**Reduction of the original identity.** For \(N=w\otimes\phi\), put \(\lambda=\phi(w)=ab+\psi(u)\). Then \(N^2=\lambda N\). Since \([w,w]=0\), direct substitution of \(Nx=\phi(x)w\) into the ORIGINAL Nijenhuis identity, without dropping any terms, gives the exact scalar condition
\[
\phi(x)\phi([w,y])-\phi(y)\phi([w,x])=\lambda\phi([x,y])\qquad(x,y\in L).
\]
The left-hand side and the right-hand side are alternating bilinear maps. Therefore it is necessary and sufficient to check \((x,y)=(t,v)\) and \((x,y)=(v,z)\), with \(v,z\in V\). The first gives
\[
\boxed{\psi(Au)\,\psi=\psi(u)(\psi\circ A),}
\]
and the second gives
\[
\boxed{a\,\psi\wedge(\psi\circ A)=0.}
\]
These two equations are together equivalent to the Nijenhuis identity for arbitrary \(a,b,u,\psi\). Square-zero imposes the independent equation \(ab+\psi(u)=0\).

**Exhaustion of the three cases.** If \(\psi=0\), nonzero \(\phi\) forces \(b\ne0\), and square-zero implies \(a=0\); \(w\ne0\) then forces \(u\ne0\). If \(\psi\ne0\) is a left eigenvector, the two Nijenhuis equations vanish identically and only \(ab+\psi(u)=0\) remains. If \(\psi\) is not an eigenvector, then \(\psi\) and \(\psi\circ A\) are linearly independent. The wedge equation forces \(a=0\), and the first equation forces both \(\psi(u)=0\) and \(\psi(Au)=0\). These also ensure square-zero, and \(u\ne0\) is necessary for \(w\ne0\). This proves necessity and sufficiency, including the boundary \(m=2\), where the non-eigen incidence case is empty.

**Finite-field enumeration.** The first case contributes \(q^m-1\) distinct maps (normalize \(b=1\)). In the eigenvector case, fix one of the \(E_A(q)\) nonzero eigen-covectors. For \(a\ne0\), there are \((q-1)q^m\) choices of \((a,u,b)\), since \(b\) is uniquely forced. For \(a=0\), there are \(q(q^{m-1}-1)\) choices: choose \(0\ne u\in\ker\psi\) and arbitrary \(b\). Their sum is \(q(q^m-1)\). In the non-eigen case, the two independent covectors cut out a subspace of dimension \(m-2\), yielding \((q^{m-2}-1)q\) pairs \((u,b)\) per non-eigen \(\psi\). The number of non-eigen nonzero \(\psi\) is \(q^m-1-E_A(q)\). In each of the last two cases each nonzero rank-one map is represented by exactly \(q-1\) ordered tensor factorizations, so division by \(q-1\) gives the displayed formula.

**Rigidity and defect.** For an arbitrary \((m+1)\)-space, a square-zero rank-one map \(N=w\otimes\phi\) requires \(\phi(w)=0\); choose nonzero \(w\), nonzero \(\phi\in w^\perp\), then divide by \(q-1\) tensor rescalings. This gives \(Z_{\mathrm{all}}\). Subtracting the proven count gives the defect formula. If \(A=cI\), every covector is a left eigenvector, and both Nijenhuis conditions vanish for every rank-one map. Conversely, if \(A\) is non-scalar over ANY field and \(m\ge2\), there exists a nonzero \(\psi\) with \(\psi\circ A\notin k\psi\): otherwise every one-dimensional subspace of \(V^*\) is invariant and \(A\) is scalar. Take \(w=t\), \(\phi=\psi\) (that is, \(a=1,u=0,b=0\)). Then \(N^2=0\), but \(a\psi\wedge(\psi\circ A)\ne0\); hence \(N\) is not Nijenhuis. This proves the if-and-only-if without a finite-field hypothesis.

## Verification

The bundled standalone Python 3 checker `verify.py` reconstructs \([t,v]=Av\) from each input matrix and evaluates the original Nijenhuis equation directly on every pair of basis vectors for every pair of nonzero tensor factors. It removes the unique \(q-1\) factorization redundancy by canonical matrix keys, classifies \(N^2=0\) by direct evaluation of \(\phi(w)\), and independently enumerates left eigen-covectors of \(A^{\mathsf T}\). The scalar identities are NOT used to determine acceptance in the direct checker. The seven exhaustive configurations include genuine \(\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\) arithmetic.

Representative verified counts \((Z_A(q),E_A(q))\) are \((56,4)\) for \(m=2,q=3,A=\operatorname{diag}(1,2)\), \((8,0)\) for an irreducible quadratic action over \(\mathbb F_3\), \((21,0)\) for a degree-three action without rational eigenvalues over \(\mathbb F_2\), and \((105,0)\) for the degree-four irreducible binary action. The bundled `verification_output.txt` is the exact output of the checker; its final marker is `ALL_DIRECT_NIJENHUIS_AND_COUNT_CHECKS_OK`. Exhaustive finite experiments are corroboration, not a proof for all \(m,q\).

## Relationship to prior work

Liu, Sheng, Zhou and Bai (arXiv:1601.02356v1, first posted 2016-01-11) give the algebraic Lie-Nijenhuis identity in their Definition 3.4 and discuss constructions from \(\mathcal O\)-operators; the full accessible text discusses general identities and higher-ary Lie examples, not a finite-field rank-one nilpotent census on codimension-one abelian-ideal Lie algebras. Avetisyan (arXiv:1610.05365, first posted 2016-10-17; updated text inspected) systematically describes almost-Abelian Lie algebras, their subalgebras, derivations, and Lie-orthogonal endomorphisms; those operator identities differ from the square-zero Lie-Nijenhuis identity counted here. Ma and Zhao (arXiv:2507.12692v1) classify Nijenhuis operators of three-dimensional REAL Leibniz algebras; their three-dimensional real specializations may already cover individual low-dimensional cases, which are not asserted independently new. Freibert (doi:10.1007/s12220-026-02413-0, published 2026-03-31) studies geometric torsion-free H-structures and full-rank almost tangent structures over the reals; such structures and conditions are not the present arbitrary-rank-one finite-field census.

Earlier related work already gives a rank-by-rank enumeration of **idempotent** Nijenhuis projections on almost-Abelian Lie algebras, and separate rank-one Nijenhuis results for free class-two nilpotent Lie algebras and \(\mathfrak{sl}_2\). None of those statements implies the present square-zero rank-one classification or formula: a nonzero rank-one square-zero map cannot be idempotent, and the underlying Lie families and bracket tensors in the other two results are different. The present result deliberately asserts no novelty for the idempotent branch. Published research-index semantic searches returned only mathematically more distant results; see the scientific comparison in `AUDIT.json`. Nonappearance in search results is not a proof of historical originality.

## Limitations

The result counts labeled operators, not automorphism-conjugacy classes, rank two or higher operators, or nonreduced parameter schemes. It does not assert a universal closed formula for the distribution of left eigenspace dimensions across all input matrices. Prior low-dimensional real classifications and any unidentified general criterion may subsume certain special cases; originality remains a best-knowledge assessment, not certified priority.

## References

- J. Liu, Y. Sheng, Y. Zhou, C. Bai, *Nijenhuis operators on \(n\)-Lie algebras*, arXiv:1601.02356v1, posted 2016-01-11, https://arxiv.org/abs/1601.02356 . Full text inspected through https://ar5iv.labs.arxiv.org/html/1601.02356 .
- Z. Avetisyan, *The structure of almost Abelian Lie algebras*, arXiv:1610.05365, first posted 2016-10-17; accessible updated version https://arxiv.org/pdf/1610.05365 inspected.
- T. Ma, C. Zhao, *Classification of three-dimensional Nijenhuis Leibniz algebras*, arXiv:2507.12692v1, 2025-07-16, https://arxiv.org/abs/2507.12692 .
- M. Freibert, *Torsion-Free H-Structures on Almost Abelian Solvmanifolds*, *Journal of Geometric Analysis* 36, 161 (2026), published 2026-03-31, https://doi.org/10.1007/s12220-026-02413-0 .
