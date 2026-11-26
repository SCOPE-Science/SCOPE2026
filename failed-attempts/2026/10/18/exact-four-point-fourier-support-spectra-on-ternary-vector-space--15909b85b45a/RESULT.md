# Exact four-point Fourier-support spectra on ternary vector spaces

## Finding
Let \(d\ge 2\), \(G=\mathbb F_3^d\), and let \(A\subset G\) have exactly four points. For a function \(f:G\to\mathbb C\) with **exact** spatial support \(\operatorname{supp} f=A\), let
\[\mathcal S(A)=\bigl\{|\operatorname{supp}\widehat f|:\operatorname{supp}f=A\bigr\}.\]
Then the complete attainable Fourier-support spectrum depends only on the affine geometry of \(A\):
\[
\boxed{\mathcal S(A)=
\begin{cases}
3^{d-2}\{6,7,8,9\},&\dim\operatorname{aff}A=2\text{ and }A\text{ contains three collinear points},\\
3^{d-2}\{4,6,7,8,9\},&\dim\operatorname{aff}A=2\text{ and }A\text{ contains no three collinear points},\\
3^{d-3}\{22,24,25,26,27\},&\dim\operatorname{aff}A=3.
\end{cases}}
\]
The last case exists only for \(d\ge3\). Every listed value occurs for **every fixed** support \(A\) of that type. In particular, an affine-independent four-point support in \(\mathbb F_3^3\) allows \(22\) but not \(23\) nonzero Fourier coefficients, a genuine exact-support spectral gap.

## Assumptions and scope
Write \(\zeta=e^{2\pi i/3}\). The (unnormalized) Fourier transform is
\[\widehat f(\xi)=\sum_{x\in G}f(x)\zeta^{\langle\xi,x\rangle},\qquad\xi\in G.\]
The choice of sign or any nonzero scalar normalization does not change support cardinalities. Exact support means that each of the four values on \(A\) is nonzero; a vector with a vanishing spatial coefficient is not permitted. An affine line has three points in characteristic three. Consequently four distinct points have affine span dimension two or three, and the planar four-sets split into those containing a full affine line and four-caps (no collinear triple).

## Proof
**1. Affine reduction and scaling.** Translating \(A\) only modulates its Fourier transform, and an invertible linear change permutes frequencies; both preserve the support sizes. Let \(H=\operatorname{span}(A-A)\), of dimension \(r\in\{2,3\}\). After a translation the function is supported on \(H\). Its Fourier transform is constant on each coset of \(H^\perp\), whose order is \(3^{d-r}\). Hence the nonzero Fourier cardinalities on \(G\) are precisely \(3^{d-r}\) times the corresponding local cardinalities on \(\mathbb F_3^r\).

**2. The two planar geometries.** The ternary affine plane has \(12\) lines and \(\binom94=126\) four-sets. Exactly \(12\cdot6=72\) four-sets contain a whole line (a four-set cannot contain two different full lines); the other \(54\) are caps. Each cap is an affine parallelogram, as follows by counting the \(54\) parallelograms given by a midpoint and two distinct direction lines. Thus, up to affine changes, the planar representatives are
\[
A_L=\{(0,0),(1,0),(2,0),(0,1)\},\qquad
A_P=\{(0,0),(1,0),(0,1),(1,1)\}.
\]
Put \(u,v\in\{1,\zeta,\zeta^2\}\). For \(A_L\), the local transform is
\[P_L(u,v)=a+bu+cu^2+dv,\qquad abcd\ne0.\]
For every fixed \(u\), at most one of the three \(v\)-values can give a zero, since \(d\ne0\). Thus at most three zeros occur. All four counts \(0,1,2,3\) occur with the exact coefficient witnesses listed below. The spectrum is \(\{9,8,7,6\}\).

For \(A_P\), the local transform is
\[P_P(u,v)=a+bu+cv+duv,\qquad abcd\ne0.\]
Unless there is a value \(u_0\) at which both \(a+bu_0=0\) and \(c+du_0=0\), each of the three rows \(u\) contains at most one zero, so there are at most three. If such \(u_0\) exists, then
\[P_P(u,v)=(u-u_0)(b+dv).\]
The entire row \(u=u_0\) consists of three zeros, and there are either zero or two additional zeros (depending on whether \(-b/d\) is a cube root of unity). Thus the only possible counts are \(0,1,2,3,5\); every one is attained by the witnesses below. The spectrum is \(\{9,8,7,6,4\}\).

**3. The genuinely three-dimensional geometry.** Four affinely independent points are all affinely equivalent to
\[A_I=\{(0,0,0),(1,0,0),(0,1,0),(0,0,1)\}.\]
The local Fourier values are
\[P_I(u,v,w)=a+bu+cv+dw,\qquad u,v,w\in\{1,\zeta,\zeta^2\},\quad abcd\ne0.\]
We prove, by a complete exact finite-field certificate, that the possible zero counts are **exactly** \(\{0,1,2,3,5\}\). The mathematical completeness of the certificate follows from the following rank-closure lemma, which applies to any evaluation matrix with four columns over the infinite field \(K=\mathbb Q(\zeta)\).

For a subset \(T\) of evaluation rows, let \(V_T\) be the common kernel over \(K^4\). Define its row-span closure to consist of *all* evaluation rows vanishing identically on \(V_T\). If \(V_T\ne0\) and none of the four coordinate functionals vanishes identically on \(V_T\), then some vector of \(V_T\) has all four coordinates nonzero and has zeros at **exactly** the closure rows: every coordinate-zero hyperplane and every other row-zero hyperplane is a proper subspace of \(V_T\), and finitely many proper subspaces cannot exhaust a vector space over the infinite field \(K\). Conversely, a vector with all four coordinates nonzero and any prescribed Fourier zeros has zero-row rank at most three, since it lies in their nonzero common kernel. A basis of those zero rows therefore consists of at most three actual evaluation rows, and its closure is the complete zero set of the original vector. This proves that examining **every subset of at most three rows** and testing its kernel and closure is logically exhaustive, not a heuristic bound.

The supplied standalone `artifacts/verify.py` carries out precisely that exact computation on the \(27\) rows of \(P_I\): it reduces all
\[\sum_{j=0}^3\binom{27}{j}=3304\]
possible generating subsets over \(K\), represented as rational pairs using \(\zeta^2+\zeta+1=0\). It tests the full-coordinate kernel criterion and computes the exact row-span closure without floating-point arithmetic. The only eligible closure sizes are
\[\boxed{0,1,2,3,5}.\]
Explicit integer-coefficient witnesses below independently realize each one, so the certificate establishes both necessity and sufficiency. The independent-support spectrum is consequently \(\{27,26,25,24,22\}\). Combining with step 1 proves all dimensions.

**4. Explicit witness table.** In each parenthesized quadruple the entries are the coefficients \((a,b,c,d)\) in the displayed local polynomial; the indicated number is its **number of zeros**, not its Fourier-support size.

For \(P_L\), counts \(0,1,2,3\) are respectively realized by
\[(1,1,1,1),\quad(-1,1,1,-1),\quad(-1+\zeta,-1-\zeta,1,1),\quad(-(2+\zeta),-(1+2\zeta^2),-(2+\zeta),3).\]
For \(P_P\), counts \(0,1,2,3,5\) are respectively realized by
\[(1,1,1,1),\quad(-3,1,1,1),\quad(\zeta,\zeta^2/2,\zeta^2/2,1),\quad(-1,1,-1,1),\quad(1,-1,-1,1).\]
For \(P_I\), counts \(0,1,2,3,5\) are respectively realized by
\[(-1,-1,-1,-1),\quad(-3,-1,2,2),\quad(-2,-2,-1,-1),\quad(-2,-1,1,2),\quad(-1,-1,1,1).\]
All entries are nonzero and all zero counts are checked exactly in the verification artifact.

## Verification
Run `python3 artifacts/verify.py` from the extracted package. The program uses only the Python standard library and exact arithmetic in \(\mathbb Q(\zeta)\), performs the planar orbit/line count, checks both planar representative spectra, enumerates all \(3304\) independent-support generating subsets, and replays every explicit coefficient witness. It prints the three zero-count and Fourier-support spectra and ends with `All rank, geometry, and exact witness checks passed.` The infinite family in \(d\) is justified by the proved annihilator-coset reduction; the exact finite certificate addresses only the \(27\)-character local three-dimensional core.

## Relationship to prior work
Recent work on parity-sensitive finite Fourier zero patterns motivates the support-geometry problem, but its **finite-parabola** hypothesis and prime restriction \(p\ge5\) do not cover four arbitrary points over \(\mathbb F_3\). Classical finite-Abelian uncertainty theory determines minimal-support bounds and selected equality cases, not the complete fixed-support spectrum by all three affine types. A public exact five-point spectrum on \(\mathbb F_3^2\) covers the different exact support cardinality five. Exact unrestricted four-point parallelogram computations have already appeared, and the planar parallelogram line in our table is **not claimed in isolation as new**; likewise a phase-only rectangle result is restricted to equal coefficient magnitudes. What is additional here is the complete three-dimensional affine-independent case, particularly the forbidden zero count four, together with its integration into an all-dimensional three-orbit classification.

## Limitations
The classification concerns exactly four nonzero coefficients and elementary Abelian groups of exponent three. No characterization of *all individual extremizing coefficient vectors*, larger coefficient supports, other primes, or non-elementary groups is asserted. The independent-support upper bound and the exclusion of exactly four Fourier zeros depend on an explicit exhaustive **exact** rank certificate for the finite local matrix, not on a separate case-free analytic formula. An older equivalent result in nonindexed Fourier-matroid literature remains a bibliography risk. These limitations do not affect the finite logical completeness of the provided certificate.

## References
1. D. Li, *Parity-Sensitive Fourier Uncertainty and Zero-Set Rigidity on the Finite Parabola*, arXiv:2609.16030v1, first posted 11 September 2026. Its primary MSC is 43A25; it treats a different prime and support geometry.
2. A. Bonami and S. Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, arXiv:1003.5060v1, first posted 26 March 2010; *Acta Scientiarum Mathematicarum* 79 (2013), 507–528. See Section 4, Proposition 21 and Theorem 23.
3. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, KU Leuven Report TW477 (2006); *Linear Algebra and its Applications* 426 (2007), 349–367, DOI 10.1016/j.laa.2007.05.009.
4. *Complete exact-support five-point Fourier spectrum on \(\mathbb F_3^2\)*, published mathematical record dated 4 October 2026 (published-finding corpus archive), which treats five rather than four spatial coefficients.
5. *Phase-only Fourier-zero spectrum of a four-point rectangle on cyclic product groups*, published mathematical record dated 4 October 2026 (published-finding corpus archive), which assumes four equal coefficient magnitudes.
6. *Exact three-sparse Fourier support spectra on elementary Abelian odd-prime groups*, published mathematical record dated 4 October 2026 (published-finding corpus archive), which concerns three, not four, spatial coefficients.
