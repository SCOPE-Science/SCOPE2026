# A splitting criterion for pseudo-Fredholm triangular extensions and uniformly convex power counterexamples

## Finding

**Triangular splitting theorem.** Let \(E\) and \(F\) be complex Banach spaces, \(S\in\mathcal B(E)\) surjective, and \(J\in\mathcal B(F,E)\). On the Banach direct sum \(E\oplus F\) define
\[
T(e,f)=(Se+Jf,0).
\]
Then
\[
\boxed{T\text{ is pseudo-Fredholm}\quad\Longleftrightarrow\quad
\exists V\in\mathcal B(F,E):SV=-J.}
\]
If additionally \(SJ=0\), every \(T^n\) with \(n\ge2\) is right generalized Drazin invertible, whether or not \(T\) itself is pseudo-Fredholm.

**Uniformly convex consequence.** For each \(1<p<\infty\), \(p\ne2\), there exist a separable, uniformly convex, complex Banach space \(X\) and \(T\in\mathcal B(X)\) such that
\[
\boxed{T\text{ is not pseudo-Fredholm},\qquad
T^n\text{ is right generalized Drazin invertible for every }n\ge2.}
\]
Thus superreflexivity and uniform convexity do not restore the power axiom for pseudo-Fredholm operators.

## Assumptions and scope

A bounded operator \(L\) is **semi-regular** when its range is closed and \(\ker L\subseteq\bigcap_{n\ge1}\operatorname{ran}L^n\). It is **pseudo-Fredholm** if its space admits a topological direct sum \(M\oplus N\) of closed invariant subspaces with \(L|_M\) semi-regular and \(L|_N\) quasinilpotent. We call an operator **right generalized Drazin invertible** if it admits such a reducing direct sum with a surjective restriction in place of the semi-regular restriction. This standard decomposition characterization is the only one needed below. The theorem holds for any equivalent Banach direct-sum norm and permits \(E\) and \(F\) to be infinite-dimensional.

The **analytic core** \(K(L)\) consists of vectors \(x_0\) admitting a backward sequence \((x_n)_{n\ge0}\) with \(Lx_{n+1}=x_n\) and \(\|x_n\|\le C^n\|x_0\|\) for some finite \(C\ge1\). For \(x_0=0\), take the zero sequence. This definition is used only with bounded operators.

## Proof

**1. Analytic core of the triangular extension.** Since \(S\) is onto, the open mapping theorem gives \(C\ge1\) such that each \(e\in E\) has a preimage \(u\) with \(Su=e\) and \(\|u\|\le C\|e\|\). Recursive choices give an exponentially bounded backward chain for every \(e\). Hence \(K(S)=E\). Since \(\operatorname{ran}T\subseteq E\oplus\{0\}\), each \(x\in K(T)\) lies in \(E\oplus\{0\}\); conversely backward chains within that summand use \(S\). Therefore
\[
K(T)=E\oplus\{0\}.
\]

**2. Any semi-regular summand contains the full analytic core.** Suppose \(E\oplus F=M\oplus N\) is a generalized Kato decomposition of \(T\), with both summands closed and invariant, \(T|_M\) semi-regular and \(T|_N\) quasinilpotent. Let \(Q=T|_N\). If \(x\in K(Q)\), backward chains and submultiplicativity give \(\|x\|\le\|Q^n\|C^n\|x\|\) for every \(n\). Since \(\lim_n\|Q^n\|^{1/n}=0\), necessarily \(x=0\). The bounded projections associated with the reducing sum preserve backward-chain relations and exponential bounds, so the \(N\)-projection of \(K(T)\) lies in \(K(Q)=\{0\}\). Thus
\[
E\oplus\{0\}=K(T)\subseteq M.
\]

If \(M\) contained a vector \((e,f)\) with \(f\ne0\), choose \(u\in E\) with \(Su=-Se-Jf\). Because \((u,0)\in M\), the vector \((e+u,f)\) would be a nonzero element of \(\ker(T|_M)\), with second coordinate \(f\ne0\). But semi-regularity implies \(\ker(T|_M)\subseteq\operatorname{ran}(T|_M)\), and every vector in the latter range has zero second coordinate. Contradiction. Consequently \(M=E\oplus\{0\}\).

**3. Complementary invariant graphs are precisely bounded liftings.** Projection of the complementary closed space \(N\) to \(F\) is a bounded bijection with bounded inverse; hence \(N=\{(Vf,f):f\in F\}\) for some bounded \(V:F\to E\). Since \(T(N)\subseteq N\cap(E\oplus\{0\})=\{0\}\), one has \(SV+J=0\). Conversely if \(SV=-J\), then \(M=E\oplus\{0\}\) and \(N=\operatorname{graph}V\) form a closed reducing direct sum. The first restriction is the surjection \(S\) and is semi-regular, while \(T|_N=0\) is quasinilpotent. This proves the equivalence.

If \(SJ=0\), then direct multiplication gives
\[
T^n(e,f)=(S^ne,0)\quad(n\ge2).
\]
Each \(S^n\) is onto, and \(X=(E\oplus\{0\})\oplus(\{0\}\oplus F)\) is a reducing surjective-plus-zero decomposition. Hence every such power is right generalized Drazin invertible.

**4. A uniformly convex obstruction from any nonsplit quotient.** Let \(U\) be a complex Banach space, let \(Y\subsetneq U\) be closed and uncomplemented, and write \(F=U/Y\), \(q:U\to F\) for the quotient. There is no bounded right inverse \(R:F\to U\): such an \(R\) would make \(I_U-Rq\) a bounded projection onto \(Y\); conversely if \(Y\) were complemented, \(q\) would split.

Take \(G=\ell^2(\mathbb N_0;U)\) and \(E=U\oplus_2 F\oplus_2 G\). Define
\[
S\bigl(u,f,(u_0,u_1,u_2,\ldots)\bigr)
=\bigl(u_0,qu,(u_1,u_2,\ldots)\bigr),
\qquad Jf=(0,f,0).
\]
The map \(S:E\to E\) is bounded and onto: for prescribed target \((a,b,(w_0,w_1,\ldots))\), choose \(u\) with \(qu=b\), choose input sequence \((a,w_0,w_1,\ldots)\), and set the unused middle input to zero. Also \(SJ=0\). If \(SV=-J\), the \(F\)-coordinate of this identity gives \(q\pi_UV=-I_F\), and \(-\pi_UV\) would split \(q\), impossible. Thus \(T(e,f)=(Se+Jf,0)\) on \(X=E\oplus_2F\) is not pseudo-Fredholm, whereas all powers from the second onward are right generalized Drazin invertible.

For \(U=\ell^p(\mathbb N,\mathbb C)\), \(1<p<\infty\), \(p\ne2\), the Lindenstrauss–Tzafriri complemented-subspaces theorem supplies a closed uncomplemented \(Y\): \(\ell^p\) is not isomorphic to a Hilbert space. Both \(U\) and its quotient \(F\) are uniformly convex; uniform convexity passes to \(\ell^2\)-sums and their finite \(\ell^2\)-sums. Therefore \(X\) is separable and uniformly convex, as asserted.

## Verification

Every step above is analytic. The decisive identities are \(K(T)=E\oplus\{0\}\), \(M=E\oplus\{0\}\) for every generalized Kato decomposition, \(SV+J=0\) for its complementary graph, and the explicit coordinate formula for \(S\). These identities can be checked by direct substitution. The argument invokes the open mapping theorem, spectral-radius formula for quasinilpotent operators, bounded inverse theorem, the classical Lindenstrauss–Tzafriri complemented-subspaces theorem, and standard stability of uniform convexity under quotients and \(\ell^2\)-sums. It is not a finite-dimensional experiment.

## Relationship to prior work

Aznay, Chabbabi and Zariouh (2026, arXiv:2611.04004) establish power stability of pseudo-Fredholmness on Hilbert space and exhibit a separable Banach-space counterexample using a nonsplitting surjection from \(\ell^1\) to \(\ell^2\). The present theorem identifies a necessary-and-sufficient bounded splitting obstruction for the *entire surjective-corner triangular family*, and locates the failure within uniformly convex, hence reflexive, spaces. Their example, the generalized Kato framework, and the Lindenstrauss–Tzafriri theorem are acknowledged antecedents.

The earlier Aznay–Chabbabi preprint (arXiv:2610.23229) discusses pseudo-Fredholm counterexamples on Banach spaces, and Tajmouati–Karmouni (arXiv:1602.00626) discusses generalized Kato decompositions of upper triangular operator matrices. Available summaries do not establish the displayed equivalence or the uniformly convex construction, but neither inaccessible full text was used to assert its absence. These are priority-of-publication risks.

## Limitations

The necessary-and-sufficient statement applies only when the upper-left corner \(S\) is surjective and the lower row is zero. It does not characterize arbitrary upper triangular matrices or all Banach spaces for which pseudo-Fredholm operators satisfy the power axiom. The uniformly convex example is an existence construction depending on a known noncomplemented subspace, not a fully enumerated basis for that subspace. The result is a mathematical proof and comparison, not an independent external audit or an absolute novelty certificate.

## References

1. Z. Aznay, F. Chabbabi, H. Zariouh, *Pseudo-Fredholm operators form a regularity on Hilbert spaces* (2026), arXiv:2611.04004, https://arxiv.org/abs/2611.04004.
2. Z. Aznay, F. Chabbabi, *On Mbekhta's conjecture and pseudo-Fredholm operators on Banach and Hilbert spaces* (2026), arXiv:2610.23229, https://arxiv.org/abs/2610.23229.
3. A. Tajmouati, M. Karmouni, *Generalized Kato Decomposition For Operator Matrices and SVEP* (2016), arXiv:1602.00626, https://arxiv.org/abs/1602.00626.
4. J. Lindenstrauss, L. Tzafriri, *On the complemented subspaces problem*, Israel J. Math. 9 (1971), 263–269, https://doi.org/10.1007/BF02771592.
5. *Banach space*, Encyclopedia of Mathematics, https://encyclopediaofmath.org/wiki/Banach_space (uniform convexity of subspaces, quotients and \(\ell^p\) spaces).
