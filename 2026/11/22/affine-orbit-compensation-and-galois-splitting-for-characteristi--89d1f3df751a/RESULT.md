# Affine-orbit compensation and Galois splitting for characteristic-three anti-pre-Lie Nijenhuis operators

## Finding

Let \(k=\mathbb F_q\) have characteristic three, let \(K=\mathbb F_{q^2}\), and choose \(\alpha\in K\setminus k\) of nonzero field trace \(\operatorname{Tr}_{K/k}(\alpha)\). On the three-dimensional \(k\)-space \(A=kt\oplus K\), define a bilinear multiplication by
\[
 t\circ x=\alpha x,\qquad x\circ t=2\alpha x=-\alpha x,\qquad K\circ K=0,\qquad t\circ t=0.
\]
This is an anti-pre-Lie algebra in the polynomial sense of Liu–Bai, and indeed in characteristic three its product is a Lie bracket. Write \(V=K=[A,A]\), the derived ideal.

**Theorem (one complete classification).** Every \(k\)-linear Nijenhuis operator \(N:A\to A\), defined by
\[
 N(x)\circ N(y)=N\bigl(N(x)\circ y+x\circ N(y)-N(x\circ y)\bigr)
 \quad (x,y\in A),
\]
has a unique form
\[
 \boxed{N(t)=at+u,\qquad N(x)=bx\quad(x\in K),\qquad a\in k,\ u,b\in K.}
\]
There are exactly \(q^5\) such operators. Their linear-rank polynomial, and the polynomial counting conjugacy classes by rank under the *full* anti-pre-Lie automorphism group, respectively, are
\[
 \boxed{1+(q^3-1)X+q^2(q^2-1)X^2+q^2(q-1)(q^2-1)X^3,}
\]
\[
 \boxed{1+qX+(q^2-1)X^2+q^2(q-1)X^3.}
\]
In particular, there are exactly \(q^3+q\) automorphism-conjugacy classes. The group is \(K\rtimes K^\times\); despite the \(q^5\) labeled solutions, translation symmetry collapses each off-diagonal scalar fiber to one orbit.

There is also a **geometric statement explicitly restricted to the derived-ideal-preserving Nijenhuis subscheme** \(\mathcal N_V\) (defined by \(N(V)\subseteq V\)). It is reduced and has three geometric irreducible components, all affine spaces of dimension five: Frobenius fixes one component and exchanges the other two. For every \(s\ge1\), writing \(Q=q^s\), its extension-field point count is
\[
 \boxed{\#\mathcal N_V(\mathbb F_{q^s})=\begin{cases}Q^5,&s\text{ odd},\\3Q^5-2Q^4,&s\text{ even}.
 \end{cases}}
\]
Its Hasse–Weil zeta function is
\[
 \boxed{Z(\mathcal N_V,z)=\frac{1-q^8z^2}{(1-q^5z)(1-q^{10}z^2)}.}
\]
Every \(k\)-rational Nijenhuis operator preserves \(V\), so the \(s=1\) count is also the count of *all* rational operators. The extension-field counts and the geometric component assertion are **not** asserted for the unrestricted full operator scheme: non-\(V\)-preserving solutions can appear after the quadratic splitting extension.

## Assumptions and scope

The field has characteristic exactly three; \(q\) is any power of three. The element \(\alpha\) has irreducible quadratic minimal polynomial over \(k\), and its field trace is nonzero. Irreducibility is used to exclude rational eigenvectors and eigen-covectors. Nonzero trace is used to identify the full automorphism group; without this extra condition, multiplication normal forms and rational rank counts remain valid, but extra scalar symmetries may alter orbit counts. The theorem uses labeled operators on the fixed algebra \(A\) and then conjugacy by its entire algebra-automorphism group, not by all invertible linear basis changes.

The identity above is the defining polynomial Nijenhuis identity; no characteristic-zero deformation theorem is assumed in characteristic three. A Nijenhuis operator here means a \(k\)-linear endomorphism satisfying this identity, not necessarily invertible, diagonalizable or idempotent.

## Proof

**1. Anti-pre-Lie structure.** The multiplication is alternating in characteristic three and is the usual almost-abelian Lie bracket \([t,x]=\alpha x\) on \(kt\ltimes K\). Its Jacobi identity follows from the abelian ideal \(K\). If \(x\circ y=[x,y]\) is any Lie bracket in characteristic three, the two anti-pre-Lie identities
\[
 x\circ(y\circ z)-y\circ(x\circ z)=[y,x]_\circ\circ z,
 \qquad [x,y]_\circ\circ z+[y,z]_\circ\circ x+[z,x]_\circ\circ y=0,
\]
where \([x,y]_\circ=x\circ y-y\circ x=2[x,y]\), follow from Jacobi and \(-2=1\). Consequently this \(A\) is anti-pre-Lie.

**2. All rational operators preserve the derived ideal.** Write an arbitrary operator in blocks as
\[
 N(t)=at+u,\qquad N(x)=f(x)t+Bx
\]
with \(a\in k\), \(u\in K\), \(f\in\operatorname{Hom}_k(K,k)\), and \(B\in\operatorname{End}_k(K)\). Put \(T(x)=\alpha x\). Applying the Nijenhuis identity to \(x,y\in K\) and comparing the \(t\)-coordinates gives
\[
 f(x)f(Ty)-f(y)f(Tx)=0\quad(x,y\in K).
\]
If \(f\ne0\), this forces \(f\circ T=c f\) for some \(c\in k\); that would be a rational left eigen-covector of the irreducible quadratic operator \(T\), a contradiction. Hence \(f=0\) and \(N(K)\subseteq K\).

**3. The full matrix equation.** Once \(f=0\), the identities for \((K,K)\) and \((t,t)\) hold automatically: the first by commutativity of the zero product on \(K\), the second by alternation. The \((t,x)\) identity is
\[
 aTB=B(aT+TB-BT),\qquad\text{equivalently}\qquad(aI-B)[T,B]=0.
\]
Put \(C=B-aI\); this is exactly
\[
 C[T,C]=0.
\]
If \(C\) is invertible, it commutes with \(T\). If \(C\) has rank one, write \(C=v\otimes\varphi\) with nonzero \(v\in K\) and nonzero \(\varphi\in K^*\). Then
\[
 C[T,C]=v\otimes\bigl(\varphi(Tv)\varphi-\varphi(v)(\varphi\circ T)\bigr).
\]
When \(\varphi(v)\ne0\), the vanishing would make \(\varphi\) a rational left eigen-covector of \(T\); when \(\varphi(v)=0\), it would give \(\varphi(Tv)=0\), but \(v,Tv\) span \(K\) by irreducibility, so \(\varphi=0\), again impossible. Thus no nonzero rank-one \(C\) solves the equation. All solutions are \(C=0\) or invertible operators commuting with \(T\), and so in either case \(C\in k[T]\cong K\). Conversely all such \(C\), together with every \(a,u\), satisfy the Nijenhuis identity. Writing \(b=a+c\) for \(c\in K\) proves the unique normal form.

**4. Linear ranks.** In the decomposition \(kt\oplus K\), the normal-form matrix is
\[
 N=\begin{pmatrix}a&0\\u&m_b\end{pmatrix},
\]
where \(m_b\) denotes multiplication by \(b\) on the quadratic field \(K\). If \(a,b\ne0\), its rank is three; if \(a=0,b\ne0\), its rank is two; if \(a\ne0,b=0\), its rank is one; and if both vanish, its rank is zero or one according as \(u=0\) or \(u\ne0\). Counting the respective choices gives exactly the displayed rank polynomial. Summing its coefficients yields \(q^5\).

**5. The full automorphism group and orbits.** The ideal \(K=[A,A]\) is characteristic. Every algebra automorphism is therefore \(\Phi(t)=st+w\), \(\Phi|_K=H\), with \(s\in k^\times\), \(w\in K\), \(H\in\mathrm{GL}_k(K)\). Preservation of \(t\circ x=Tx\) gives \(HT=sTH\). Taking traces of the similar operators \(T\) and \(sT\), and using \(\operatorname{tr}(T)\ne0\), yields \(s=1\). Now \(H\) commutes with the irreducible \(T\), hence is multiplication by an element \(h\in K^\times\). Conversely arbitrary \(w\) and \(h\) yield automorphisms. For the classified Nijenhuis operators, conjugation is
\[
 (a,b,u)\longmapsto(a,b,hu+(a-b)w).
\]
If \(b\ne a\), each fixed \((a,b)\) has one orbit of size \(q^2\). If \(b=a\), each fixed scalar \(a\) has exactly two orbits, represented by \(u=0\) and any nonzero \(u\), of sizes \(1\) and \(q^2-1\). Thus the total orbit count is \(q(q^2-1)+2q=q^3+q\). Sorting the same orbits by the ranks in Step 4 gives the stated orbit-rank polynomial.

**6. Geometric components of the preserved-ideal locus.** The subscheme \(\mathcal N_V\) is defined by the two linear equations \(f=0\) and the matrix entries of \(C[T,C]=0\); the three parameters \(a,u\) are free. Over an algebraic closure, \(T\) is diagonal with distinct eigenvalues. With \(C=\bigl(\begin{smallmatrix}x&y\\z&w\end{smallmatrix}\bigr)\), the matrix equation is equivalent to
\[
 yz=xy=wz=0.
\]
The resulting squarefree monomial ideal decomposes exactly as
\[
 (yz,xy,wz)=(y,z)\cap(x,z)\cap(y,w).
\]
It defines three reduced affine planes; the free \(a,u\) variables increase every component dimension by three. Frobenius exchanges the two eigenlines of the irreducible \(T\), fixes the diagonal component and exchanges the two off-diagonal components. For odd \(s\), only the diagonal component contributes new rational points; for even \(s\), the split union of three planes has \(3Q^2-2Q\) points. Multiplying by \(Q^3\) establishes the exact preserved-ideal counts. Finally, by definition
\[
 Z(\mathcal N_V,z)=\exp\biggl(\sum_{s\ge1}\#\mathcal N_V(\mathbb F_{q^s})\frac{z^s}{s}\biggr),
\]
and substituting the parity count and expanding \(-\log(1-cz)\) gives the displayed rational function.

## Verification

The self-contained `verify_anti_pre_lie.py` uses only the Python standard library. Run `python verify_anti_pre_lie.py` from the directory containing this document. It checks both anti-pre-Lie identities, exhaustively evaluates the original Nijenhuis identity on **all** \(2^9\) endomorphisms over \(\mathbb F_2\) and **all** \(3^9\) endomorphisms over \(\mathbb F_3\) for irreducible trace-one quadratic matrices, checks the complete \(\mathbb F_3\) automorphism-orbit distribution, checks the split characteristic-three preserved-ideal locus, and checks six coefficients of the proposed zeta logarithm.

The exhaustive characteristic-three result is \((1,26,72,144)\) by ranks \((0,1,2,3)\), totaling \(243\), with orbit counts \((1,3,8,18)\), totaling \(30\). The split comparison has exactly \(21\) allowed \(C\)-matrices and \(567\) derived-ideal-preserving Nijenhuis operators over \(\mathbb F_3\). The verifier is a finite consistency check; the all-prime-power and geometric statements depend on the algebraic proof above.

## Relationship to prior work

The anti-pre-Lie polynomial identities were introduced by Liu and Bai (first public arXiv version 2022-07-13), and the anti-pre-Lie Nijenhuis identity was formulated by Liu, Chen and Chen (first public version 2022-11-07). Neither source gives this characteristic-three finite-field classification or the rank-orbit and Galois-component census. The pre-Lie Nijenhuis classification of Gao, Kang, Lü and Yu treats two-dimensional complex pre-Lie and three-dimensional complex associative algebras, not this characteristic-three nonassociative family. Zhikhareva's 2024 study classifies regular-semisimple Nijenhuis eigenbases for real and complex three-dimensional Lie algebras, not unrestricted operators over characteristic three.

A closely related earlier result on the *different* multiplication \(t\cdot x=Tx\), \(x\cdot t=0\) establishes a quadratic Galois-descent classification for pre-Lie Nijenhuis operators. It already has the same \(C[T,C]=0\) block equation but also imposes a constraint on \(u\); its rational count is \(2q^3-q\) rather than the present \(q^5\). That pre-Lie family and its geometry are not presented here as new. Published related work on a three-dimensional Hom–Lie Nijenhuis family has a similar block equation but a different twisting structure and scope. The present contribution is the fully unrestricted characteristic-three anti-pre-Lie rational classification, its full automorphism quotient, and the explicitly bounded geometry of the ideal-preserving locus. Similar matrix equations alone are not a claim of novelty; implications were compared at the level of the underlying objects and constraints.

## Limitations

The theorem assumes an irreducible quadratic action, nonzero trace, and characteristic three. Rank distributions are for labeled \(k\)-linear maps, and orbit counts are for the specified anti-pre-Lie automorphisms. The component and zeta calculations are solely for the derived-ideal-preserving **subscheme** \(\mathcal N_V\). Although this contains *all* \(k\)-rational Nijenhuis operators, it need not contain all operators after scalar extension: once \(T\) splits, extra solutions with \(N(K)\not\subseteq K\) can occur. No count, component description or zeta function is asserted for the unrestricted geometric Nijenhuis scheme. No independent audit has been performed; publication-priority claims remain provisional, especially in light of possible stronger general theorems on algebraic Nijenhuis operators of solvable Lie algebras.

## References

- G. Liu and C. Bai, *Anti-pre-Lie algebras, Novikov algebras and commutative 2-cocycles on Lie algebras*, arXiv:2207.06200 (first public version 2022-07-13), https://arxiv.org/abs/2207.06200.
- S. Liu, Z. Chen and L. Chen, *Deformations and abelian extensions on anti-pre-Lie algebras*, arXiv:2301.06917 (first public version 2022-11-07), https://arxiv.org/abs/2301.06917; in particular Definition 3.3 and Theorem 3.4.
- X. Gao, C. Kang, J. Lü and S. Yu, *Nijenhuis operators on low dimensional pre-Lie algebras and solutions of CYBE*, arXiv:2308.12121 (first public version 2023-08-23), https://arxiv.org/abs/2308.12121.
- E. S. Zhikhareva, *Three-dimensional Lie algebras admitting regular semisimple algebraic Nijenhuis operators*, arXiv:2410.10536 (first public version 2024-10-14), https://arxiv.org/abs/2410.10536.
