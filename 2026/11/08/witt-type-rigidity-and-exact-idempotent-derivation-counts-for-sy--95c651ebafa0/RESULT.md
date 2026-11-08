# Witt-type rigidity and exact idempotent-derivation counts for symmetric two-step Leibniz algebras

## Finding
Let \(k=\mathbb F_q\) have **odd** cardinality \(q\), let \(V\) be a nonzero \(n\)-dimensional \(k\)-space, and let \(B:V\times V\to k\) be a nondegenerate **symmetric** bilinear form. Form the (non-Lie) two-step nilpotent Leibniz algebra \(L_B=V\oplus kz\), with \([u,v]=B(u,v)z\) and central \(z\).

The number of \(k\)-linear derivations \(D:L_B\to L_B\) with \(D^2=D\) is **exactly one** unless \(n=2m\) for some \(m\geq1\) and \(B\) is **split hyperbolic** (Witt index \(m\)). In that exceptional case it is
\[
1+2q^{m(m+1)/2}\prod_{i=1}^{m-1}(q^i+1).
\]
Every nonzero idempotent derivation has ordinary operator rank \(m+1\), and all nonzero idempotent derivations form a single conjugacy orbit under \(\operatorname{Aut}_k(L_B)\). Thus the two possible conjugacy classes, when present, are zero and nonzero. The same existence, rank, and conjugacy classification holds over any field of characteristic different from two; only the finite-field cardinality requires finiteness.

In particular, the rank-generating polynomial for idempotent derivations is \(1\) in the nonsplit or odd-dimensional cases, and is
\[
1+2q^{m(m+1)/2}\left(\prod_{i=1}^{m-1}(q^i+1)\right)T^{m+1}
\]
in split even dimension. The total number of all derivations is \(q^{1+n(n+1)/2}\).

## Assumptions and scope
The bracket is bilinear and has image in \(kz\); all brackets involving \(z\) vanish. Consequently all triple brackets vanish, so the left and right Leibniz identities both hold. Because \(B\) is nonzero symmetric and \(\operatorname{char}k\neq2\), some \(v\) has \([v,v]\neq0\); the algebra is not Lie. Split hyperbolic means an orthogonal sum of \(m\) hyperbolic planes, equivalently two complementary totally isotropic \(m\)-dimensional subspaces. No claim is made for degenerate \(B\) or characteristic two.

A derivation is a \(k\)-linear operator satisfying \(D([x,y])=[D(x),y]+[x,D(y)]\) for all \(x,y\in L_B\). Idempotent refers to composition \(D^2=D\), not to the product on \(L_B\). Operator rank is over \(k\). Automorphisms and conjugacy are \(k\)-linear and preserve the bracket.

## Proof
**1. Normal form.** Since \([L_B,L_B]=kz\), every derivation has the unique form
\[
D(v)=Av+\phi(v)z,\qquad D(z)=cz,
\]
where \(A\in\operatorname{End}_k(V)\), \(\phi\in V^*\), \(c\in k\). Writing \(A^*\) for the adjoint relative to \(B\), the derivation identity is precisely
\[
A+A^*=cI.
\]
This follows by evaluating the identity on \([u,v]=B(u,v)z\); it is also sufficient because all brackets with \(z\) vanish. Idempotence adds
\[
A^2=A,\qquad c^2=c,\qquad \phi A+c\phi=\phi.
\]
The scalar \(c\) is either zero or one.

**2. The zero-scalar branch.** If \(c=0\), then \(A^*=-A\). Taking adjoints in \(A^2=A\) gives \((A^*)^2=A^*\), so \(A^2=-A\). Since also \(A^2=A\) and the characteristic is odd, \(A=0\). The equation \(\phi A=\phi\) then forces \(\phi=0\). The only such derivation is zero.

**3. The unit-scalar branch.** If \(c=1\), then \(A^*=I-A\), \(A^2=A\) and \(\phi A=0\). Put \(U=\operatorname{im}A\), \(W=\ker A\). They are complementary. For \(u=Ax\) and \(v=Ay\),
\[
B(u,v)=B(x,A^*Ay)=B(x,(I-A)Ay)=0,
\]
so \(U\) is totally isotropic. For \(u,v\in W\), the relation \(B(Au,v)+B(u,Av)=B(u,v)\) gives \(B(u,v)=0\); hence \(W\) is totally isotropic as well. Nondegeneracy implies \(\dim U,\dim W\le n/2\). Because their dimensions add to \(n\), necessarily \(n=2m\), each has dimension \(m\), and \(B\) is split. Conversely, any ordered pair \((U,W)\) of complementary maximal totally isotropic subspaces defines a unique projection \(A\) onto \(U\) along \(W\). The vanishing of \(B\) on both subspaces implies \(A+A^*=I\), so it defines derivations for every \(\phi\) with \(\phi A=0\). This space of functionals has dimension \(m\), hence exactly \(q^m\) choices. Each such \(D\) has rank \(m+1\), since \(D(z)=z\) and \(\operatorname{im}D=U\oplus kz\).

**4. Exact finite-field count.** In a split symmetric space of dimension \(2m\), the number \(N_m\) of maximal totally isotropic \(m\)-subspaces is
\[
N_m=2\prod_{i=1}^{m-1}(q^i+1).
\]
For completeness: \(N_1=2\). For \(m>1\), count pairs of an isotropic line and a maximal isotropic subspace containing it. There are \((q^m-1)(q^{m-1}+1)/(q-1)\) isotropic lines in a split \(2m\)-space, while each maximal subspace contains \((q^m-1)/(q-1)\) lines; quotienting by a fixed isotropic line gives a split \(2m-2\)-space. Thus \(N_m=(q^{m-1}+1)N_{m-1}\). For a fixed maximal isotropic \(U\), choose one complementary maximal isotropic \(W_0\). Every other complementary maximal isotropic subspace is the graph of a linear map \(T:W_0\to U\). The graph is isotropic exactly when \(T\) is skew-adjoint under the perfect pairing \(U\times W_0\to k\). In dual bases this means a skew-symmetric \(m\times m\) matrix, of which there are \(q^{m(m-1)/2}\). Multiplying the number of first subspaces, their complements, and the \(q^m\) allowed functionals yields the displayed count.

**5. Conjugacy.** For every \(\psi\in V^*\), the central shear \(g_\psi(v)=v+\psi(v)z\), \(g_\psi(z)=z\), is an automorphism. Conjugating \(D=(A,\phi,1)\) by \(g_\phi\) replaces its central functional by \(\phi-\phi(I-A)=\phi A=0\). Any two ordered pairs of complementary maximal isotropic subspaces admit dual hyperbolic bases; the linear map carrying one such basis to the other preserves \(B\) and extends (fixing \(z\)) to an automorphism of \(L_B\). Therefore all nonzero idempotent derivations are conjugate. The zero map is a separate orbit. Finally, all derivations are parameterized by \(c\in k\), arbitrary \(\phi\in V^*\), and \(B\)-skew-adjoint \(K=A-(c/2)I\). The latter has \(n(n-1)/2\) independent entries, giving \(q^{1+n(n+1)/2}\) derivations.

## Verification
The accompanying standalone \(\texttt{verify.py}\) uses prime-field arithmetic only and no external packages. It exhaustively lists the full idempotent-derivation equations for dimension-three Leibniz algebras (\(\dim V=2\)) at \(q=3,5,7\) in the split case and at \(q=3,7\) for the anisotropic form \(\operatorname{diag}(1,1)\). It also enumerates all maximal totally isotropic planes of the split four-dimensional form and all ordered complementary plane pairs at \(q=3,5\). Its output includes \(7,11,15\) idempotent derivations in the split dimension-three examples, one in each anisotropic example, and \(217,1501\) in the split dimension-five Leibniz examples. It returns `VERIFY_OK`. Finite checks corroborate but do not establish the universal classification; the proof above does.

## Relationship to prior work
La Rosa and Mancini (arXiv:2301.11058, first posted January 26, 2023) determine derivation Lie-algebra structures of families of two-step nilpotent Leibniz algebras in characteristic different from two, principally over complex or real fields. Their Kronecker family contains the three-dimensional hyperbolic example, but the inspected theorems do not state this finite-field idempotent census, its Witt-type obstruction for general nondegenerate symmetric forms, or its automorphism-orbit classification. Bai, Gao and Li (2015) study splitting induced by idempotent derivations of *Lie* algebras; the nonalternating bracket here lies outside those hypotheses. Standard finite orthogonal-geometry counts are used in Step 4, not claimed as original. A previously known finite-field enumeration for idempotent derivations of Heisenberg *Lie* algebras treats alternating rather than symmetric brackets; its conclusions do not determine the anisotropic obstruction in this theorem. The claimed contribution is the precise non-Lie split-versus-nonsplit dichotomy, rank/orbit rigidity, and exact all-dimension odd-field count.

## Limitations
Characteristic two, degenerate forms, higher-dimensional commutator ideals, and noncommutative two-step products are outside scope. The count of operators is over labeled \(k\)-vector spaces, while conjugacy is under bracket-preserving \(k\)-linear automorphisms. The derivation-normal-form reduction is elementary, and an unidentified broader treatment of idempotent derivations of bilinear-form algebras could imply the result; the originality conclusion is relative to the inspected literature, not certified publication priority. The software tests prime fields of small order, not all prime-power fields. No independent mathematical audit has been performed.

## References
1. G. La Rosa and M. Mancini, *Derivations of two-step nilpotent algebras*, arXiv:2301.11058 (first public version January 26, 2023), https://arxiv.org/abs/2301.11058.
2. R. Bai, Y. Gao and Z. Li, *Lie algebras with idempotent derivations*, Mathematica Aeterna 5 (2015), 159–162, https://www.longdom.org/articles-pdfs/lie-algebras-with-idempotent-derivations.pdf.
