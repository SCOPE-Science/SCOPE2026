# Exact arithmetic block spectra for adjoint commutators of Hardy weighted-composition isometries

## Finding
For integers \(m,n\ge 2\), set \(V_k f(z)=k^{-1/2}(1+z+\cdots+z^{k-1})f(z^k)\) on the classical Hardy Hilbert space \(H^2(\mathbb D)\) and define \(K_{m,n}=V_m^*V_n-V_nV_m^*\). Each \(V_k\) is an isometry and \(V_mV_n=V_nV_m=V_{mn}\). Nevertheless, the mixed adjoint commutator never vanishes or becomes compact.

More precisely, after independent orthogonal identifications of its domain with \(\bigoplus_{\ell\ge0}\mathbb C^m\) and codomain with \(\bigoplus_{\ell\ge0}\mathbb C^n\), the operator becomes countably many identical copies of a finite \(n\)-by-\(m\) matrix \(B_{m,n}\) defined below. It has finite-block rank \(\min(m,n)-1\). The singular value \(1\) occurs in one block with multiplicity exactly \(\gcd(m,n)-1\), so
\[
\|K_{m,n}\|=\|K_{m,n}\|_{\mathrm{ess}}=1\quad\Longleftrightarrow\quad\gcd(m,n)>1.
\]
For coprime bases the common norm is strictly smaller than one.

For the adjacent-base pair \(n=m+1\), the finite block has precisely \(m-1\) distinct positive singular values,
\[
\boxed{\ \sigma_j(m)=\sqrt{1-\frac{j(j+1)}{m(m+1)}},\qquad j=1,\ldots,m-1.\ }
\]
Each positive value occurs with infinite multiplicity in \(|K_{m,m+1}|\), and its remaining spectrum includes zero. In particular,
\[
\|K_{m,m+1}\|=\|K_{m,m+1}\|_{\mathrm{ess}}
=\sqrt{1-\frac{2}{m(m+1)}}.
\]
The empirical measure of the \(m-1\) *distinct block levels* converges weakly to the probability density \(s/\sqrt{1-s^2}\) on \(0<s<1\). For every fixed real \(p>0\),
\[
\lim_{m\to\infty}\frac1{m-1}\sum_{j=1}^{m-1}\sigma_j(m)^p
=\frac{\sqrt\pi\,\Gamma(1+p/2)}{2\Gamma(3/2+p/2)}.
\]

## Assumptions and scope
Use the standard monomial orthonormal basis \(e_k(z)=z^k\), \(k\ge0\), of complex \(H^2(\mathbb D)\). All bases \(m,n\) are integers at least two; no irrational power or weighted Hardy-space extension is asserted. The finite-block matrix has row indices \(s=0,\ldots,n-1\) and column indices \(r=0,\ldots,m-1\). Define
\[
H_{s,r}=\max\{0,\min(n(r+1),m(s+1))-\max(nr,ms)\},\qquad
B_{m,n}=\frac{H-\boldsymbol1_{n\times m}}{\sqrt{mn}},
\]
where \(\boldsymbol1\) is the all-ones matrix. \(H_{s,r}\) counts integer positions common to the half-open intervals \([nr,n(r+1))\) and \([ms,m(s+1))\). A singular value of a finite block is not identified with a compact-operator singular-value sequence of the infinite direct sum. The direct sum is never compact and belongs to no finite Schatten ideal.

## Proof
**1. Coefficient-level decomposition.** For every \(k\ge0\), \(V_n e_k=n^{-1/2}\sum_{q=0}^{n-1}e_{nk+q}\). Disjoint coefficient supports prove isometry. For each input block \(e_{m\ell+r}\), with \(0\le r<m\), applying \(V_m^*V_n\) gives the output \(e_{n\ell+s}\) coefficient \(H_{s,r}/\sqrt{mn}\); applying \(V_nV_m^*\) gives \(1/\sqrt{mn}\) for every \(s\) in this output block. Thus the operator has a **two-sided unitary block decomposition** with the direct sum of \(B_{m,n}\), for all \(\ell\ge0\); the same unitary change of basis on domain and codomain is not asserted. The semigroup identity follows directly by multiplying the two geometric polynomials.

**2. Rank and unit singular levels.** View \(H/\sqrt{mn}\) as the cross-Gram matrix of normalized indicators of two partitions of \([0,mn)\): \(m\) consecutive intervals of length \(n\), and \(n\) consecutive intervals of length \(m\). The two step-function subspaces intersect exactly in the functions constant on the \(d=\gcd(m,n)\) consecutive intervals of length \(mn/d\). Consequently the cross-Gram singular value \(1\) has multiplicity exactly \(d\). The common globally constant vector is one of these directions; the all-ones subtraction removes exactly this singular direction, leaving exactly \(d-1\) unit singular levels. All others are strictly below one.

For \(n\ge m\), the selected row \(s_r=\lfloor nr/m\rfloor\), \(r=0,\ldots,m-1\), is strictly increasing. Its overlap with column \(r\) is positive and with any column beyond \(r\) is zero; the resulting \(m\)-by-\(m\) submatrix is triangular with positive diagonal. Hence \(H\) has rank \(m\). Transposition gives rank \(n\) when \(m>n\). The constant direction is one of the nonzero singular directions, so subtracting it gives rank \(\min(m,n)-1\). This proves the general claims and noncompactness.

**3. Adjacent bases and a discrete Hahn Laplacian.** Put \(n=m+1\). The exact overlap matrix has just two nonzero entries in each column:
\[
H_{s,r}=(m-r)\mathbf1_{s=r}+(r+1)\mathbf1_{s=r+1}.
\]
Its column sums equal \(m+1\) and row sums equal \(m\). Therefore the constant input vector is annihilated by \(B\), and on its orthogonal complement \(B^*B=H^*H/[m(m+1)]\).

The real symmetric matrix \(L=m(m+1)I-H^*H\) satisfies
\[
(Lp)(r)=r(m-r)[p(r)-p(r-1)]
 +(r+1)(m-r-1)[p(r)-p(r+1)],
\]
for \(r=0,\ldots,m-1\), interpreting the boundary terms with zero coefficients. Applied to the restrictions of polynomials of degree at most \(j\), this operator preserves that space; on the leading monomial \(r^j\) its leading coefficient is \(j(j+1)r^j\). These polynomial restrictions yield a complete triangular basis for the \(m\)-dimensional function space. Therefore the full exact spectrum of \(L\) consists of the simple eigenvalues \(j(j+1)\), \(0\le j<m\). In the constant direction, \(B^*B\) has eigenvalue zero; on its orthogonal complement the eigenvalues are \(1-j(j+1)/[m(m+1)]\), for \(1\le j<m\). They are all strictly positive and pairwise distinct, establishing the displayed singular spectrum. This second-order difference operator is a special symmetric Hahn-polynomial operator; the elementary triangular argument is given to make the proof self-contained.

**4. Limiting levels.** With \(j/m\to t\in(0,1)\), the positive level tends to \(\sqrt{1-t^2}\). Riemann sums prove weak convergence of the empirical block distribution. Changing variables from \(t\) to \(s=\sqrt{1-t^2}\) gives the stated probability density. The beta-integral evaluates the positive power moments. No trace of the infinite direct sum is taken.

## Verification
The accompanying `check_adjacent.py` reconstructs exact integer overlap matrices, checks the block action on monomials, verifies ranks and unit-level multiplicities for 400 ordered small base pairs, verifies adjacent-base eigenvalues through degree forty, checks symbolic Gram identities, and compares limiting moments. It reports 3,775 successful assertion groups. These finite checks supplement, but do not replace, the proof for all integer bases and all real \(p>0\).

## Relationship to prior work
Noor's 2018 work introduced the weighted-composition semigroup in a Hardy-space reformulation of the Báez-Duarte criterion. Manzur–Noor–Santos subsequently studied the same semigroup's cyclic vectors, invariant subspaces, spectra and individual isometric behavior, including its adjoint's coefficient-sum structure. The result here analyzes the **mixed-adjoint difference** \(V_m^*V_n-V_nV_m^*\), which does not follow from semigroup commutativity. The quadratic eigenvalues of the finite Hahn birth-and-death operator are classical; the new connection claimed here is the exact cross-adjoint overlap, its arithmetic norm dichotomy, and the adjacent-base singular-value hierarchy. Literature on *unweighted* monomial composition operators \(f(z)\mapsto f(z^n)\) concerns a different operator, and the algebraic intertwining by \(I-M_z\) is not a bounded unitary equivalence preserving adjoints or singular values.

## Limitations
No characterization of all non-unit singular levels for general nonadjacent pairs is asserted; these are exactly and reproducibly given by the finite overlap matrix. There is no claim of a Schatten trace or approximation-number decay for this noncompact direct sum. This result does not imply a statement about the Riemann hypothesis or related open problems. Its historical priority, particularly potential overlap with older conditional-expectation and canonical-correlation results for interval partitions, is not independently certified.

## References
1. S. Waleed Noor, *A Hardy space analysis of the Báez-Duarte criterion for the RH* (first public 25 September 2018), https://arxiv.org/abs/1809.09577, Section 3.
2. J. Manzur, W. Noor and C. F. Santos, *A weighted composition semigroup related to three open problems* (first public 9 November 2021), https://arxiv.org/abs/2111.05398, especially adjoint and isometry results.
3. R. Sasaki, *Exactly solvable discrete time Birth and Death processes* (first public 7 June 2021), https://arxiv.org/abs/2106.03284; classical Hahn spectral framework.
