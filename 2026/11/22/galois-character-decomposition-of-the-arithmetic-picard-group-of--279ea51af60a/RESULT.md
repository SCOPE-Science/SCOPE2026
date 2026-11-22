# Galois-character decomposition of the arithmetic Picard group of a BHK quartic

## Finding

Let \(X/\mathbb Q\) be the smooth quartic K3 surface
\[
X:\qquad x^3y+xy^3+z^3w+zw^3=0\subset\mathbb P^3.
\]
Set \(L=\mathbb Q(\zeta_8)=\mathbb Q(i,\sqrt2)\), with \(\zeta_8^4=-1\). Let \(\chi_i,\chi_2,\chi_{-2}\) be the quadratic characters of \(\operatorname{Gal}(L/\mathbb Q)\) associated respectively with \(\mathbb Q(i)\), \(\mathbb Q(\sqrt2)\), and \(\mathbb Q(\sqrt{-2})\). The geometric Néron–Severi module has the following **complete rational Galois-character decomposition**:
\[
\boxed{\operatorname{NS}(X_{\overline{\mathbb Q}})\otimes\mathbb Q
\simeq \mathbf{1}^{\oplus9}\oplus\chi_i^{\oplus7}
\oplus\chi_2^{\oplus2}\oplus\chi_{-2}^{\oplus2}.}
\]
The action factors through \(\operatorname{Gal}(L/\mathbb Q)\), and \(L\) is the smallest Galois extension over which every geometric divisor class is defined. In particular, the Picard ranks are
\[
\begin{array}{c|ccccc}
K & \mathbb Q & \mathbb Q(i) & \mathbb Q(\sqrt2) & \mathbb Q(\sqrt{-2}) & L\\ \hline
\rho(X_K) &9&16&11&11&20.
\end{array}
\]
The \(48\) geometric lines split into \(24,40,28,28,48\) Galois orbits over these five fields, respectively. Exactly \(8,32,8,8,48\) individual lines are defined over them, respectively. The Galois traces on the rational Picard space for \(\zeta_8\mapsto\zeta_8^r\), \(r=1,3,5,7\), are \((20,2,12,2)\).

## Assumptions and scope

All surfaces and fields have characteristic zero. Picard ranks over number fields are understood as ranks of their algebraic Picard groups; equivalently, they are dimensions of invariant geometric Néron–Severi spaces after tensoring with \(\mathbb Q\). The equivalence of ranks follows from the Hochschild–Serre obstruction to descent lying in the torsion Brauer group. No integral decomposition, Brauer-group classification, or statement about the transcendental Galois representation is asserted.

## Proof

**1. Rational diagonalization.** Put \(A=x+y\), \(B=x-y\), \(C=z+w\), \(D=z-w\). The identity \((x+y)^4-(x-y)^4=8xy(x^2+y^2)\) gives a \(\mathbb Q\)-isomorphism from \(X\) to
\[
Y:\quad A^4-B^4+C^4-D^4=0.
\]
This quartic is smooth by the Jacobian criterion, so it is a K3 surface. Since it has \(h^{1,1}=20\), its geometric Picard number is at most \(20\).

**2. All forty-eight line classes.** Over \(L\), write \(\zeta=\zeta_8\). For \(m,n\in\{0,1,2,3\}\), consider the following three families of lines:
\[
\begin{aligned}
L^{(0)}_{mn}:&\quad A=\zeta^{2m}B,\quad C=\zeta^{2n}D,\\
L^{(1)}_{mn}:&\quad A=\zeta^{2m+1}C,\quad B=\zeta^{2n+1}D,\\
L^{(2)}_{mn}:&\quad A=\zeta^{2m}D,\quad B=\zeta^{2n}C.
\end{aligned}
\]
Each is on \(Y\): the first and third pair two fourth-power terms with equal signs, while the second pairs terms with opposite signs via the fourth power of an odd power of \(\zeta\), equal to \(-1\). The lines are distinct. Their intersection matrix \(G\) has \(G_{ii}=-2\), and for distinct lines \(G_{ij}=1\) precisely when their defining linear equations have a common projective solution; otherwise \(G_{ij}=0\). The value \(-2\) is adjunction on a K3 surface, and two distinct intersecting straight lines meet transversely in the smooth surface.

For an independent, purely modular description of the incidence relation, let \(e(L^{(t)}_{mn})=(2m+\epsilon_t,2n+\epsilon_t)\), where \(\epsilon_1=1\) and \(\epsilon_0=\epsilon_2=0\). Two distinct lines of the same type intersect exactly if their first or second indices agree. For lines of different types, written in order \((0,1)\), \((0,2)\), or \((1,2)\), and exponents \((a,b)\), \((c,d)\), they intersect respectively when
\[
a+d-b-c\equiv0,\qquad a+d+b-c\equiv0,\qquad a+b-c-d\equiv0\pmod{8}.
\]
These identities follow by eliminating \(A,B,C,D\) around the four-cycle of linear equations. Exact Gaussian elimination on the resulting integer \(48\times48\) matrix gives \(\operatorname{rank}G=20\). Consequently these lines span \(\operatorname{NS}(Y_{\overline{\mathbb Q}})\otimes\mathbb Q\), and \(\rho(Y_{\overline{\mathbb Q}})=20\), without assuming that the lines form an integral basis.

**3. Exact Galois action.** The automorphisms of \(L\) are \(\sigma_r:\zeta\mapsto\zeta^r\) for \(r\in\{1,3,5,7\}\). They preserve the family label \(t\) and send its parameters to
\[
(m,n)\longmapsto\left(
\frac{r(2m+\epsilon_t)-\epsilon_t}{2},
\frac{r(2n+\epsilon_t)-\epsilon_t}{2}
\right)\pmod4.
\]
All line equations have coefficients in \(L\), so the Galois action on the Picard group factors through \(\operatorname{Gal}(L/\mathbb Q)\).

**4. Character multiplicities.** Let \(V=\mathbb Q^{48}\) have basis the lines, let \(V\to\operatorname{NS}(Y_{\overline{\mathbb Q}})\otimes\mathbb Q\) map basis vectors to divisor classes, and let \(P_\chi=\sum_r\chi(\sigma_r)\sigma_r\) act on \(V\). Because \(G\) is the pullback of the nondegenerate intersection pairing on the geometric Néron–Severi space, the multiplicity of \(\chi\) in that space equals \(\operatorname{rank}(GP_\chi)\). Performing **exact rational**, not modular-probabilistic, row reduction gives the four ranks
\[
\begin{array}{c|rrrr}
\chi &\mathbf{1}&\chi_i&\chi_2&\chi_{-2}\\\hline
\operatorname{rank}(GP_\chi)&9&7&2&2.
\end{array}
\]
Their sum is \(20\), exhausting the entire geometric Picard space. With \(\chi_i(3,5,7)=(-1,+1,-1)\), \(\chi_2(3,5,7)=(-1,-1,+1)\), and \(\chi_{-2}(3,5,7)=(+1,-1,-1)\), the nonidentity traces are \(2,12,2\). Their being strictly less than \(20\) shows that the whole Picard group becomes fixed over no proper intermediate field of \(L/\mathbb Q\).

**5. Descent ranks and line orbit counts.** For the quadratic intermediate fields, invariants of a single quadratic character contribute their full dimension and all other nontrivial characters contribute zero. This gives the Picard-rank table above. The same explicit permutations produce the stated line-orbit and individually rational-line counts. The latter are a separate invariant and do not equal the Picard ranks in general.

## Verification

The standalone \(\texttt{verify_picard.py}\) reconstructs all \(48\) lines combinatorially, the integral intersection matrix, the four exact character projectors and the intermediate-field orbit-sum matrices. It performs exact \(\mathbb Q\)-Gaussian elimination with Python's standard-library fractions. Asserted results: Gram rank \(20\), character multiplicities \((9,7,2,2)\), intermediate ranks \((9,16,11,11,20)\), and Galois traces \((20,2,12,2)\). A separate symbolic calculation using \(\zeta^4+1=0\) independently confirmed all \(1128\) pairwise incidence outcomes in the modular criterion, including their nonintersection outcomes. The verification is exhaustive for the forty-eight lines and does not extrapolate from a sample.

## Relationship to prior work

Barrett–Clayton–DeVries–Priddis (2026) give the defining polynomial and identify the geometric Fermat quartic and its forty-eight lines while studying automorphism-invariant lattices for BHK mirror symmetry. Their calculations concern complex geometric symmetries, not the arithmetic character module of this specified \(\mathbb Q\)-model. Jumagulov (2026) computes Galois-invariant Picard ranks of the **all-plus Fermat surface**, including \(\rho_{\mathbb Q}=5\), \(\rho_{\mathbb Q(i)}=8\) in degree four, and develops methods for higher-degree Fermat surfaces; the signed quartic here is not its \(\mathbb Q\)-isomorphic model. Gvirtz-Chen–Skorobogatov (2019/2022) study cohomology and Brauer groups of general diagonal quartics and provide relevant Galois-representation machinery, but the inspected text does not state this four-character decomposition for the signed quartic. The calculation is therefore a new **explicit arithmetic specialization**, not a new general method for diagonal quartics.

## Limitations

The Galois representation is determined only **over \(\mathbb Q\)** as a rational representation; no integral-lattice splitting or discriminant groups are claimed. Geometric isomorphism to the Fermat quartic does not identify the two different rational Galois modules. Earlier work by Bright and Pinch–Swinnerton-Dyer develops arithmetic methods for diagonal quartics; historical priority for this exact special example cannot be excluded without comprehensive inspection of those older sources. This result supplies arithmetic descent data but does not itself resolve a new mirror-symmetry equivalence.

## References

1. A. Barrett, A. Clayton, B. DeVries, and N. Priddis, *K3 surfaces and BHK Mirror symmetry: A counterexample*, arXiv:2611.15986v1 (first public 2026-11-11), especially §§3.1, 3.3, Appendix A. https://arxiv.org/html/2611.15986v1
2. R. Jumagulov, *Galois-invariant Néron–Severi ranks of Fermat surfaces over number fields: a Galois module, closed forms, a threshold, and exact tables*, arXiv:2607.17387 (2026), §§1, 6–7. https://arxiv.org/abs/2607.17387
3. D. Gvirtz-Chen and A. N. Skorobogatov, *Cohomology and the Brauer groups of diagonal surfaces*, arXiv:1905.11869 (original preprint 2019; published 2022), §§Introduction, 3.2–3.3. https://arxiv.org/abs/1905.11869
4. M. Bright, *Computations on diagonal quartic surfaces* (2002), historically relevant but not verified against its complete text in this comparison.
