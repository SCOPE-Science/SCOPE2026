# Primitive disjointness matrices of nonalgebraic Boolean one-types

## Finding
Let \(\mathbb B\) be the countable atomless Boolean algebra in the pure Boolean-algebra signature, and let \(A\subseteq\mathbb B\) be an individually named finite Boolean subalgebra with \(m\ge1\) atoms. Let \(\mathcal T_A\) be the complete nonalgebraic one-types over \(A\). Define the symmetric integer matrix \(D_A\), indexed by \(\mathcal T_A\), by \(D_A(p,q)=1\) if some distinct realizations \(x\models p\), \(y\models q\) satisfy \(x\wedge y=0\), and zero otherwise. Then \(|\mathcal T_A|=3^m-2^m\), and **every such matrix is unimodular**:
\[
\boxed{\operatorname{SNF}_{\mathbb Z}(D_A)=I_{3^m-2^m},\qquad
\det D_A=(-1)^{m(1+2^{m-1})}.}
\]
Its complete real inertia is
\[
\boxed{(n_+,n_-,n_0)=\left(\frac{3^m+1}{2}-2^{m-1},\frac{3^m-1}{2}-2^{m-1},0\right).}
\]
In particular its signature is exactly \(1\), independently of the number of named atoms, and it has full rank in every field, including all positive characteristics. The theorem is about an existential relation **between complete types**, not a relation on the old finite Boolean algebra itself.

## Assumptions and scope
All old elements of \(A\) are fixed individually. Each of the \(m\) atoms of \(A\) is nonzero but is not an atom of \(\mathbb B\): every such piece splits nontrivially in the ambient atomless algebra. In one extension, an ambient element \(x\) has, independently in each old atom \(a_i\), precisely three possibilities: \(x\wedge a_i=0\), \(0<x\wedge a_i<a_i\), or \(x\wedge a_i=a_i\). Label these possibilities \(0,s,1\), respectively. By homogeneous finite-subalgebra extension, the words in \(\{0,s,1\}^m\) are exactly the complete one-types; the algebraic words are exactly those containing no \(s\). The matrix domain consists of all the remaining words. The existential definition permits distinct realizations, including two realizations of the same nonalgebraic type.

## Proof
**(1) Local disjointness and complete types.** In any nonzero old atom, the feasibility of choosing disjoint pieces with prescribed states \(0,s,1\) is described, in that order, by
\[
B=\begin{pmatrix}1&1&1\\1&1&0\\1&0&0\end{pmatrix}.
\]
Indeed zero is disjoint from everything; a full piece is disjoint only from zero; two proper nonzero pieces may be chosen disjoint by splitting the old atom into at least three nonzero pieces. Atomlessness supplies these finite refinements. The choices across old atoms are independent. Consequently the unrestricted full \(3^m\)-square feasibility matrix is \(H=B^{\otimes m}\), and \(D_A\) is its principal submatrix on words containing \(s\). Nonalgebraic words admit infinitely many realizations, so the wordwise diagonal feasibility also admits *distinct* realizations. Because any finite isomorphism between finite Boolean subalgebras extends by back-and-forth, these words encode complete, not only quantifier-free, types.

**(2) Jacobi complementary-minor calculation.** Direct calculation gives \(\det B=-1\) and
\[
B^{-1}=\begin{pmatrix}0&0&1\\0&1&-1\\1&-1&0\end{pmatrix}.
\]
The complement of the row/column index set of \(D_A\) is the set \(E=\{0,1\}^m\) of algebraic words, where the digits here denote the \(0\) and \(1\) states and exclude \(s\). The \(E\)-principal submatrix of \(H^{-1}=(B^{-1})^{\otimes m}\) equals
\[
R=\begin{pmatrix}0&1\\1&0\end{pmatrix}^{\otimes m}.
\]
This is a symmetric permutation matrix of determinant \((-1)^{m2^{m-1}}\), with exactly \(2^{m-1}\) positive and \(2^{m-1}\) negative eigenvalues. The ordinary complementary principal-minor identity for an invertible matrix (Jacobi's identity) yields \(\det D_A=\det H\,\det R\). Since \(\det H=(-1)^{m3^{m-1}}=(-1)^m\), the displayed determinant is \((-1)^{m(1+2^{m-1})}\), hence a unit. An integral square matrix with unit determinant is integer-unimodular; its entire Smith normal form is the identity.

**(3) Inertia.** The symmetric real matrix \(B\) has two positive and one negative eigenvalue. For example, the trace is \(2>0\) and determinant is \(-1<0\). The symmetric real matrix is invertible, so it has an odd number of negative eigenvalues, and the positive trace excludes three negative eigenvalues. Tensor-product signs show that \(H\) has \((3^m+1)/2\) positive and \((3^m-1)/2\) negative eigenvalues. Since \(D_A\) is invertible, partition \(H\) along the \(D_A\) and \(E\) indices and apply the Schur-complement inertia identity: \(H\) is real-congruent to \(D_A\oplus R^{-1}\), because \(R\) is the \(E\)-block of \(H^{-1}\). The inertia of \(R^{-1}=R\) is \((2^{m-1},2^{m-1})\). Subtracting these counts gives the stated inertia and signature.

## Verification
The companion `verify.py` is a standard-library-only, independent exact checker. Run `python3 verify.py`. It verifies both orders of the local inverse, independently enumerates every admissible pair of subsets of a four-atom refinement of one old atom to check all nine local feasibility entries, and constructs the actual nonalgebraic principal matrices for \(m=1,2,3,4\), with orders \(1,5,19,65\). A fraction-free Bareiss elimination checks their exact determinants \(1,1,-1,1\) and the word-index counts. Expected output ends with `ALL_EXACT_CHECKS_PASS`. This finite verification is not the proof for arbitrary \(m\); Steps (1)–(3) establish the unrestricted statement.

## Relationship to prior work
The uniqueness and finite-subalgebra extension property of the countable atomless Boolean algebra is standard; Vermeeren (2010), Sections 3–4, gives an accessible presentation. Earlier work on nonzero finite powerset intersection frames studies their bounded morphisms and finite-rank first-order theories; those structures index **old Boolean subsets**, not complete nonalgebraic one-types over a finite subalgebra, and the published conclusions do not imply this unimodularity or signature. Graph-exclusion Fourier interpolation studies independent-support character matrices with a different kernel and index set. Standard Kronecker-product and Jacobi identities are used without claiming these general linear-algebra tools as novel. The proposed contribution is the concrete identification of a logical type-compatibility matrix whose removal of all algebraic-type rows and columns preserves unimodularity and gives a constant signature.

## Limitations
The result is for the pure atomless Boolean algebra, finite nonempty named subalgebras and existential disjointness feasibility for *pairs*. It does not classify matrices for arbitrary Boolean-algebra reducts, further binary relations, simultaneous realization of three types, or the ordinary eigenvalues. The all-size proof is mathematical; finite checker output alone is insufficient. Search and full-text comparisons do not guarantee global historical priority. Independent mathematical validation has not been performed.

## References
1. Stijn Vermeeren, *Embeddings into the countable atomless Boolean algebra*, arXiv:1006.4479v1, first public June 23, 2010, Sections 3–4, https://arxiv.org/abs/1006.4479.
2. *Four rank-three theories of finite Boolean co-consistency frames*, published research report, November 8, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-four-rank-three-theories-of-finite-boolean-co-consistency-frames--e1d3ed9bf29b.
3. *Binary p-morphism rigidity for atomic Boolean compatibility frames*, published research report, October 13, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-binary-p-morphism-rigidity-for-atomic-boolean-compatibility-fram--cf33fd475bad.
4. *Graph-exclusion Fourier interpolation: universal invertibility and a mod-four inverse resonance*, published research report, November 8, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-graph-exclusion-fourier-interpolation-universal-invertibility-an--0cb9494a16e7.
