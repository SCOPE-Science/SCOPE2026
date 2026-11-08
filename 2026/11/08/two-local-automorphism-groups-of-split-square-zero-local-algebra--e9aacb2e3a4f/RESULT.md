# Two-local automorphism groups of split square-zero local algebras

## Finding
Let \(K=\mathbb F_q\) be any finite field, \(n\ge1\), and \(A=K1\oplus V\) with \(\dim_KV=n\) and product \((a1+v)(b1+w)=ab1+aw+bv\). For an integer \(m\ge2\), an **\(m\)-local automorphism** is an arbitrary set map \(\Phi:A\to A\) such that for each ordered \(m\)-tuple of elements there is a single \(K\)-algebra automorphism agreeing with \(\Phi\) on the whole tuple. Linearity, injectivity, and surjectivity are not imposed in advance.

Set \(N=(q^n-1)/(q-1)\). The complete group of two-local automorphisms (under composition) is
\[
\operatorname{Loc}_2(A)\cong (K^\times)^N\rtimes S_N\cong C_{q-1}\wr S_N,
\qquad |\operatorname{Loc}_2(A)|=N!(q-1)^N.
\]
The subgroup of ordinary algebra automorphisms is \(\operatorname{Aut}_K(A)\cong\operatorname{GL}_n(q)\) and has order \(\prod_{j=0}^{n-1}(q^n-q^j)\). Every three-local automorphism is an ordinary automorphism. Equality \(\operatorname{Loc}_2(A)=\operatorname{Aut}_K(A)\) holds **if and only if** \(n=1\) or \((n,q)=(2,2)\). Thus, outside these cases, nonlinear two-local automorphisms exist, and three evaluation points are necessary and sufficient to force global linearity.

## Assumptions and scope
The field is finite of *arbitrary* prime-power cardinality, including characteristic two and extension fields. All automorphisms are unital \(K\)-algebra automorphisms (they fix \(K\) pointwise), not merely ring automorphisms allowing field automorphisms. Let \(\mathbb P(V)\) denote the set of one-dimensional \(K\)-linear subspaces (projective points). Choose once and for all a nonzero representative \(r_L\in L\) for every \(L\in\mathbb P(V)\). The conclusion counts actual set maps on the underlying algebra, not maps modulo conjugacy. The symbol \(C_{q-1}\) denotes a cyclic group of order \(q-1\); if \(q=2\), this group is trivial.

## Proof
**Step 1: Automorphisms.** The unique maximal ideal of \(A\) is \(V\); every algebra automorphism fixes the unit and hence each scalar. Its restriction to \(V\) is a linear invertible transformation. Conversely every \(T\in\operatorname{GL}(V)\) extends uniquely to the algebra automorphism \(a1+v\mapsto a1+T(v)\) because \(V^2=0\). Thus \(\operatorname{Aut}_K(A)=\operatorname{GL}(V)\).

**Step 2: Reduction of two-local maps.** Let \(\Phi\) be two-local. Each individual value of \(\Phi(a1+v)\) has scalar part \(a\), since every interpolating automorphism fixes scalar parts. Write \(f(v)=\Phi(v)\in V\). Applying the two-local condition to the pair \((v,a1+v)\) shows
\[
\Phi(a1+v)=a1+f(v) \quad\text{for all }a\in K,\;v\in V.
\]
Conversely any map of that form is two-local precisely when, for every \(v,w\in V\), some \(T\in\operatorname{GL}(V)\) simultaneously satisfies \(T(v)=f(v)\) and \(T(w)=f(w)\).

**Step 3: Projective classification.** Pairing \(v\) with \(cv\) gives \(f(cv)=cf(v)\) for every \(c\in K\), including zero, so \(f\) is homogeneous and \(f(0)=0\). An automorphism cannot map a nonzero vector to zero. Pairing independent \(v,w\) shows that \(f(v),f(w)\) are independent. Consequently the induced map on \(\mathbb P(V)\) is injective; finiteness makes it a permutation \(\pi\in S_N\). There are unique scalars \(b_L\in K^\times\) such that
\[
f(c r_L)=c b_L r_{\pi(L)}\qquad(c\in K,\ L\in\mathbb P(V)).
\]
Conversely any permutation \(\pi\) and any choice of the \(N\) nonzero \(b_L\) define a homogeneous map taking independent pairs to independent pairs. An invertible linear transformation can send any given independent pair to any other independent pair, by extending both pairs to bases; dependent pairs are matched by homogeneity. Hence each displayed map is two-local. This also works when \(n=1\), since every nonzero pair is dependent. Composition produces the full permutational wreath product \((K^\times)^N\rtimes S_N\). Counting choices gives \(N!(q-1)^N\).

**Step 4: Three-local rigidity.** If \(\Phi\) is three-local, it is two-local, and for each \(v,w\in V\) the triple \((v,w,v+w)\) is interpolated by one linear automorphism. Therefore \(f(v+w)=f(v)+f(w)\). Together with homogeneity from Step 3, this makes \(f\) \(K\)-linear. Its projective permutation property forces injectivity and hence invertibility. Thus \(\Phi\) itself is an algebra automorphism. The converse is immediate.

**Step 5: Sharp two-local rigidity cases.** If \(n=1\), homogeneity makes every two-local map multiplication by a nonzero scalar. If \((n,q)=(2,2)\), there are three nonzero vectors and three projective points, so the two-local group has size \(3!=6=|\operatorname{GL}_2(2)|\), forcing equality. If \(n\ge2\) and \(q>2\), choose a projective line \(L\) and \(b\in K^\times\setminus\{1\}\). Multiply vectors on \(L\) by \(b\) and fix every vector on the other lines. This is two-local by Step 3 but not additive: choose \(x\notin L\) and nonzero \(u\in L\); then \(u-x\notin L\) while \(f(u)\ne f(x)+f(u-x)\). If \(q=2\) and \(n\ge3\), choose independent \(x,y,z\in V\). Transpose the two distinct projective points represented by \(x+y\) and \(z\), fixing all others. This is two-local by Step 3 but violates additivity at \(x,y\). No other rigidity cases occur.

## Verification
Run `python3 verify.py` from the extracted package. The verifier builds all invertible matrices independently and compares *every pair* of nonzero or zero inputs with the list of simultaneously attainable images. It exhaustively constructs all projective-permutation/scalar maps for \((q,n)=(2,1),(2,2),(3,2),(2,3)\), then checks that the additive maps are precisely the ordinary \(\operatorname{GL}_n(q)\)-actions. The resulting two-local/three-local counts are \((1,1),(6,6),(384,48),(5040,168)\); the program prints `VERIFY_OK`. These finite checks are independent of the universal argument and do not certify extension-field cases by enumeration.

## Relationship to prior work
Arzikulov, Karimjanov and Umrzaqov (2023, arXiv:2305.13720) study local and two-local automorphisms of null-filiform and filiform *nilpotent* associative algebras and prove two-local rigidity for their specified families. Their theorem does not classify two-local maps of the unital split square-zero family here. Ayupov, Arzikulov, Umrzaqov and Nuriddinov (2020) give conditions enforcing linearity of two-local linear maps and results for Jordan algebras; their constrained-matrix linearity results do not supply this full finite-field wreath-product group or its sharp small-field exception. Ayupov and Kudaybergenov (2016) construct nonlinear two-local automorphisms of nilpotent Lie algebras, a different algebra category. The ordinary identification of the automorphism group of \(K1\oplus V\) with \(\operatorname{GL}(V)\) is elementary background, not independently novel. The new mathematical claim here is the complete two-local group, its exact size and exceptional rigidity, and its sharp three-local collapse.

## Limitations
This is a theorem about \(K\)-algebra automorphisms of split square-zero local algebras over finite fields. It makes no claim about non-split local rings, higher radical powers, or automorphisms allowing nontrivial field automorphisms. The group description is noncanonical because it chooses a representative of each projective point. The proof is complete mathematically, but publication priority is not guaranteed by the inspected literature; unlocated general theorems about two-local bijections of vector spaces might imply the same classification.

## References
- F. N. Arzikulov, I. A. Karimjanov, S. M. Umrzaqov, *Local and 2-local automorphisms of finite-dimensional nilpotent associative algebras*, first arXiv version 23 May 2023, https://arxiv.org/abs/2305.13720.
- Sh. Ayupov, F. Arzikulov, N. Umrzaqov, O. Nuriddinov, *Description of 2-local derivations and automorphisms on finite-dimensional Jordan algebras*, Linear and Multilinear Algebra, first online 12 November 2020, DOI:10.1080/03081087.2020.1845595.
- Sh. Ayupov, K. Kudaybergenov, *2-local automorphisms on finite-dimensional Lie algebras*, first arXiv version 16 February 2016, https://arxiv.org/abs/1602.05187.
