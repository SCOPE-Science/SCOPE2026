# Modular Betti and integral two-primary torsion profiles of square-zero almost-abelian Lie algebras

## Finding
Let \(r\geq1\) and \(s\geq0\) be integers. Over any field \(k\) of characteristic two, let \(L_{r,s}(k)\) be the \((2r+s+1)\)-dimensional Lie algebra with basis \(t,x_1,\ldots,x_r,y_1,\ldots,y_r,z_1,\ldots,z_s\), whose only nonzero brackets between basis elements, up to the required skew-symmetry, are \([t,y_i]=x_i\) for \(1\leq i\leq r\). Write \(b_j=\dim_k H^j_{\mathrm{CE}}(L_{r,s}(k);k)\) for ordinary alternating Chevalley–Eilenberg cohomology with trivial coefficients. Then

\[
\boxed{\sum_{j=0}^{2r+s+1}b_jq^j=
\frac{(1+q)^{s+1}}2\bigl((1+q)^{2r}+(1+q^2)^r\bigr).}
\tag{1}
\]

Here division by two is performed **in the ring of integer coefficient polynomials** after adding the two expressions; it is not an operation in the coefficient field. The total cohomology dimension is \(2^s(4^r+2^r)\).

There is a simultaneous integral statement. Let \(\mathfrak L_{r,s}\) be the free integral Lie ring with the identical basis and structure constants, and give its ordinary alternating integral Chevalley–Eilenberg complex the trivial module \(\mathbb Z\). Let \(\tau_j\) be the number of cyclic factors of even order in the torsion subgroup of \(H^j_{\mathrm{CE}}(\mathfrak L_{r,s};\mathbb Z)\), counted with multiplicity; **their individual orders are not claimed**. Define integer polynomials

\[
K_r^{(2)}(q)=\frac{(1+q)^{2r}+(1+q^2)^r}{2},
\]
\[
K_r^{(0)}(q)=\sum_{a=0}^r\binom ra^2q^{2a}
+\sum_{a=0}^{r-1}\binom ra\binom r{a+1}q^{2a+1}.
\]

Then the complete two-primary *cyclic-summand rank profile* is

\[
\boxed{\sum_{j\geq0}\tau_jq^j=
q(1+q)^s\bigl(K_r^{(2)}(q)-K_r^{(0)}(q)\bigr).}
\tag{2}
\]

All coefficients on the right are nonnegative integers. For \(r=1,2\) they vanish. For \(r=3,s=0\), there is exactly one even-order cyclic summand, in degree four; for \(r=4,s=0\), there are respectively four, two, and four in degrees four, five, and six. The total number of even-order cyclic factors in all degrees is

\[
\boxed{2^{s-1}\left(4^r+2^r-\binom{2r+2}{r+1}\right).}
\tag{3}
\]

For \(s=0,r\geq3\), this is strictly positive. Thus the first discrepancy from the classical characteristic-zero Betti profile occurs at \(r=3\): the characteristic-two Betti vector is \((1,4,12,19,19,12,4,1)\), whereas the rational vector is \((1,4,12,18,18,12,4,1)\).

## Assumptions and scope
The Lie bracket is alternating even in characteristic two, so in particular \([u,u]=0\). The Jacobi identity holds since all nonzero brackets lie in the central span of the \(x_i\). Its abelian ideal \(\langle x_i,y_i,z_j\rangle\) has codimension one; the adjoint of \(t\) on this ideal is square zero, with exactly \(r\) Jordan blocks of length two and \(s\) blocks of length one. Cohomology is **ordinary alternating** cohomology, not the symmetric-cochain/commutative variant sometimes used in characteristic two. The integral statement refers to the cochain complex of the displayed integral Lie ring; no claim is made that it computes integral singular cohomology of any nilmanifold.

## Proof
Write \(V^*=\langle X_1,\ldots,X_r,Y_1,\ldots,Y_r,Z_1,\ldots,Z_s\rangle\), with \(T\) the covector dual to \(t\). The Chevalley–Eilenberg differential is \(dX_i=-T\wedge Y_i\), while \(dT=dY_i=dZ_j=0\). Thus, up to an overall sign, \(d\alpha=T\wedge\delta\alpha\) for \(\alpha\in\Lambda V^*\), where the degree-preserving derivation \(\delta\) sends \(X_i\) to \(Y_i\) and kills \(Y_i,Z_j\). Also \(d(T\wedge\beta)=0\). Consequently, with \(E_k=\Lambda^kV^*\),

\[
H^j_{\mathrm{CE}}(L;k)\cong\ker(\delta|_{E_j})\oplus T\wedge\bigl(E_{j-1}/\operatorname{im}(\delta|_{E_{j-1}})\bigr)
\]

as graded vector spaces. Both summands have dimensions determined by the kernel of the respective square matrix; hence the Betti polynomial is \((1+q)K(q)\), where \(K(q)=\sum_j\dim\ker(\delta|_{E_j})q^j\).

In characteristic two \(\delta^2=0\): it vanishes on generators, and the square of a derivation has no cross terms when two is zero. More precisely, grade the exterior algebra also by the number of \(X\)-symbols. On each four-dimensional pair algebra \(\Lambda(X_i,Y_i)\), the differential maps \(X_i\mapsto Y_i\) and kills \(1,Y_i,X_iY_i\); its homology is spanned by \(1\) and \(X_iY_i\). The tensor differential on the \(r\) pair factors is the sum of the individual differentials (Koszul signs vanish in characteristic two). The elementary Künneth theorem over a field, together with the \(s\) unaffected \(Z\)-generators, gives the graded homology polynomial

\[
H_{\delta}(q)=(1+q^2)^r(1+q)^s.
\]

For each exterior degree, \(\operatorname{im}\delta\subseteq\ker\delta\), so \(\dim\ker\delta=(\dim E_j+\dim H_\delta^j)/2\). Therefore

\[
K(q)=\frac{(1+q)^{2r+s}+(1+q^2)^r(1+q)^s}{2}
\]

and multiplication by \(1+q\) proves (1). Evaluation at \(q=1\) gives the total dimension. The derivation and Künneth reasoning works over **every** field of characteristic two and does not extrapolate from finite-dimensional experiments.

For the integral statement, let \(D_j\) denote the integral matrix of \(\delta|_{\Lambda^j V^*}\). Since \(d\) is \(T\wedge\delta\) on the \(T\)-free summand and zero on the complementary summand, the nonzero Smith factors of the full degree-\(j\) integral cochain differential are precisely those of \(D_j\). Since its image inside the next cochain group is free, the torsion of the next cohomology group equals that of its cokernel. The number of even Smith factors of \(D_j\) is exactly

\[
\operatorname{rank}_{\mathbb Q}D_j-
\operatorname{rank}_{\mathbb F_2}(D_j\bmod2)
=\dim_{\mathbb F_2}\ker(D_j\bmod2)-\dim_{\mathbb Q}\ker D_j.
\]

The rational kernel polynomial for \(s=0\) is \(K_r^{(0)}(q)\). It follows either from the classical real-field calculation of Armstrong–Cairns–Jessup, or from its proved Jordan-block kernel formulas. Passing to \(s\) extra central generators multiplies both kernel polynomials by \((1+q)^s\). The characteristic-two kernel polynomial for \(s=0\) is \(K_r^{(2)}(q)\). Shifting from differential degree \(j\) to cohomology degree \(j+1\) proves (2), including coefficientwise nonnegativity.

For completeness, Vandermonde's identity yields \(K_r^{(0)}(1)=\tfrac12\binom{2r+2}{r+1}\); also \(K_r^{(2)}(1)=\tfrac12(4^r+2^r)\). Evaluation of (2) at one gives (3). The difference at \(r=3\) equals two in total Betti dimension; for larger \(r\) it is positive by induction using \(\binom{2r+4}{r+2}/\binom{2r+2}{r+1}=4(2r+3)/(2r+4)\). The stated low-rank torsion spectra follow by direct polynomial expansion.

## Verification
The included standalone `verify.py` uses only Python's standard library. It constructs **full Chevalley–Eilenberg differential matrices**, computes their ranks over \(\mathbb F_2\) for \(0\leq r\leq5\) at the documented pairs \((r,s)\), and compares the actual Betti vectors against (1). It also checks the classical kernel formula by exact rank calculations over \(\mathbb F_{1009}\) for all listed cases with \(r\leq4\), then checks the proposed two-primary rank polynomials. A separate exact integer Smith-normal-form calculation of the integral cochain matrices checked that \(r=3\) has one factor of order two in degree four and \(r=4\) has four, two, four factors of order two in degrees four through six. These finite checks are corroboration; the proof of (1)–(3) is algebraic and applies in all stated dimensions.

Run `python3 verify.py` from the directory containing that file. Expected final line: `MODULAR_ALMOST_ABELIAN_BETTI_VERIFIED`.

## Relationship to prior work
Armstrong, Cairns and Jessup (1997) give the Betti numbers of precisely the \(s=0\) family **over the reals** and indicate explicitly that extension to nonzero characteristic requires inverses of certain positive integers. Their formulas imply \(K_r^{(0)}\), but cannot cover characteristic two when \(r\geq3\). Armstrong and Sigg (1996) give a characteristic-zero general Jordan-block calculation and explicitly discuss the same two-step family. Arroyo et al. (first arXiv version, 2024) classify complex and symplectic structures of real almost-abelian Lie algebras using Jordan data, not modular Betti numbers. The present statements concern the missing modular boundary and the exact two-primary torsion multiplicity in the **integral cochain complex**. Searches of relevant algebraic-cohomology and indexed mathematical findings did not identify an equivalent all-rank formula; this search limitation is not a priority guarantee.

## Limitations
The result does not determine the exponents of even-order Smith factors of the integral complex for general \(r\), nor any odd-primary torsion. It does not classify the cohomology ring multiplicatively or symmetric-cochain cohomology in characteristic two. It does not identify integral Lie-algebra cohomology with singular cohomology of a real nilmanifold. No claim is made about arbitrary nilpotent Jordan-block lengths. Historical completeness and independent mathematical validation remain open.

## References
1. R. M. Arroyo, M. L. Barberis, V. S. Diaz, Y. Godoy and I. Hernández, *Classification of nilpotent almost abelian Lie groups admitting left-invariant complex or symplectic structures*, arXiv:2406.06819, first version 2024-06-10, https://arxiv.org/abs/2406.06819.
2. G. F. Armstrong, G. Cairns and B. Jessup, *Explicit Betti numbers for a family of nilpotent Lie algebras*, Proc. Amer. Math. Soc. 125 (1997), 381–385, https://doi.org/10.1090/S0002-9939-97-03607-1.
3. G. F. Armstrong and S. Sigg, *On the cohomology of a class of nilpotent Lie algebras*, Bull. Austral. Math. Soc. 54 (1996), 517–527, https://doi.org/10.1017/S0004972700021936.
4. D. B. Fuks, *Cohomology of Infinite-Dimensional Lie Algebras*, Plenum, 1986 (standard Chevalley–Eilenberg constructions; not a claimed priority comparison).
