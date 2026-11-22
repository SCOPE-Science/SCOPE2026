# Noncongruent octahedral rotation classes with identical Wigner sampling spectra

## Finding
Let \(O\) be the 24-element rotational symmetry group of a cube inside \(SO(3)\). Its six quarter-turns about coordinate axes form a conjugacy class \(Q\), and its six half-turns about axes through opposite edges form a different conjugacy class \(H\). The two six-point configurations have **identical labeled pairwise intrinsic angular distances**, after a specified pairing of their three two-point blocks, but are **not congruent under any isometry of the standard bi-invariant metric on \(SO(3)\)**. Indeed, their unit-quaternion lifts span real vector spaces of dimensions four and three, respectively.

More strongly, for every function \(k:[0,\pi]\to\mathbb C\), the two six-by-six matrices with entries \(k(\theta(g_i^{-1}g_j))\), where \(\theta\) is the principal relative rotation angle, are exactly equal after a fixed relabeling. Thus the distinct conjugacy classes are indistinguishable by any two-point conjugacy-invariant kernel, not merely isospectral for a particular kernel.

For every integer \(\ell\ge1\), put \(d=2\ell+1\), and let \(\mathcal W_\ell\) be the \(d^2\)-dimensional exact-degree Wigner matrix-coefficient space on \(SO(3)\), with Haar-probability \(L^2\) norm. Define the normalized six-point evaluation \(E_\ell f=(f(g_1),\ldots,f(g_6))/d\), for either configuration. Put \(a=(-1)^\ell\) and \(b=1,0,-1\) when \(\ell\equiv0,1,2\pmod3\), respectively. The entire six-value sampling Gram spectrum is
\[
\boxed{\frac{d-a}{d}\ (3),\qquad\frac{d+a-2b}{d}\ (2),\qquad\frac{d+a+4b}{d}\ (1).}
\]
Parentheses indicate multiplicity, with coincident levels merged. Every level is positive for \(\ell\ge1\). Hence arbitrary six scalar data are interpolable by a single exact-degree Wigner function at **every positive degree** (but six values do not uniquely recover an arbitrary function from the much larger coefficient space). The sharp degree-uniform normalized squared singular-value bounds are
\[
\boxed{\frac25\le \lambda\le\frac85,}
\]
with **both** endpoint levels attained only at degree \(\ell=2\). Consequently the sharp worst-case squared condition number over all positive degrees is \(4\), attained only at \(\ell=2\), and the singular-value condition number is at most \(2\). For each fixed degree, uniform positive sampling weights minimize the squared condition number among all positive weights of the same total mass.

## Assumptions and scope
Represent \(SO(3)\) as \(S^3/\{\pm1\}\) using unit quaternions \(q=(q_0,q_1,q_2,q_3)\). Use the standard Euclidean basis \(e_1,e_2,e_3\) for the imaginary quaternion components. Enumerate the six rotations in \(Q\) by the lifts
\[
q^Q_{i,\pm}=\frac{1}{\sqrt2}(1,\pm e_i),\qquad i=1,2,3.
\]
For \(H\), let \((i,j,k)\) run over \((1,2,3),(2,1,3),(3,1,2)\) and enumerate the lifts
\[
q^H_{i,\pm}=\frac{1}{\sqrt2}(0,e_j\pm e_k).
\]
The chosen ordering is by \(i\), with \(+\) followed by \(-\). Distinct quaternion lifts represent distinct rotations modulo sign. The intrinsic principal relative rotation angle is \(\theta(g^{-1}h)=2\arccos|\langle q_g,q_h\rangle|\in[0,\pi]\). The standard bi-invariant metric is the one for which this principal angle is the geodesic distance; overall metric scaling does not change the congruence statement.

The integer-spin irreducible unitary representation \(D^\ell\) has dimension \(d=2\ell+1\). Relative to normalized Haar probability, the functions \(\sqrt d\,D^\ell_{mn}\) for \(-\ell\le m,n\le\ell\) are orthonormal. The sampling operator here uses \(1/d\) per sample, making each row of its sampling matrix have squared norm one. The finite point data carry the usual Euclidean \(\ell^2\) norm. No assertion concerns mixed-degree function spaces, arbitrary rotations outside these two classes, uniqueness from six observations, or arbitrary noncentral kernels.

## Proof
**Pairwise geometry.** For either list of lifts and each pair of different indices, direct dot products give
\[
|\langle q_{i,\sigma},q_{j,\tau}\rangle|=
\begin{cases}
0,&i=j,\ \sigma\ne\tau,\\
\frac12,&i\ne j.
\end{cases}
\]
The diagonal is one. For \(Q\) every cross-block dot product is \(+1/2\). For \(H\), vectors from two different coordinate planes share one imaginary coordinate and therefore have absolute dot product \(1/2\). Thus in both sets the relative rotation is \(\pi\) within each of three pairs and \(2\pi/3\) between different pairs. These explicit values prove the exact equality of all two-point central-kernel matrices, for every \(k\).

**Noncongruence.** All six lifts of \(H\) have scalar quaternion component zero and their imaginary parts span \(\mathbb R^3\). The six lifts of \(Q\) span \(\mathbb R^4\): their differences span the three imaginary coordinate directions and their sums span the real quaternion direction. Replacing any lift by its negative does not change its real linear span. An isometry of round real projective three-space lifts to a round three-sphere isometry, hence to an orthogonal linear transformation of \(\mathbb R^4\). Such a transformation preserves the dimension of the span of representative lines. The projective ranks three and four therefore rule out an ambient isometry. In particular, the classes are not related by left/right translation or inversion of rotations.

**Sampling kernel.** Schur orthogonality and unitarity give the reproducing kernel \(K_\ell(g,h)=d\,\chi_\ell(g^{-1}h)\), where
\[
\chi_\ell(\theta)=\sum_{m=-\ell}^\ell e^{im\theta}=\frac{\sin((\ell+1/2)\theta)}{\sin(\theta/2)}.
\]
Consequently \((E_\ell E_\ell^*)_{ij}=\chi_\ell(g_i^{-1}g_j)/d\). At angles zero, \(\pi\), and \(2\pi/3\), the character is \(d\), \(a=(-1)^\ell\), and \(b\in\{1,0,-1\}\), respectively, with the stated residue rule. The unscaled six-by-six Gram matrix has diagonal \(d\), value \(a\) at the three within-pair off-diagonal positions, and \(b\) at all twelve cross-pair positions per directed half.

**Complete spectrum.** In \(\mathbb C^6\), the within-pair antisymmetric subspace has dimension three and the unscaled Gram acts there by \(d-a\). The within-pair symmetric subspace is identified with \(\mathbb C^3\), where the unscaled Gram is \((d+a-2b)I_3+2bJ_3\). Its perpendicular-to-constants sector has dimension two and eigenvalue \(d+a-2b\); its constant sector has dimension one and eigenvalue \(d+a+4b\). Division by \(d\) proves all eigenvalues and their multiplicities exactly.

**Positivity and sharp bounds.** The six residue classes \(\ell\pmod6\) yield these unscaled levels, listed with multiplicity:
\[
\begin{array}{c|c}
\ell\pmod6&\text{six levels, with multiplicities}\\\hline
0&(d-1)\ (5),\ (d+5)\ (1)\\
1&(d+1)\ (3),\ (d-1)\ (3)\\
2&(d-1)\ (3),\ (d+3)\ (2),\ (d-3)\ (1)\\
3&(d+1)\ (3),\ (d-3)\ (2),\ (d+3)\ (1)\\
4&(d-1)\ (3),\ (d+1)\ (3)\\
5&(d+1)\ (5),\ (d-5)\ (1)
\end{array}
\]
In the residue-zero row take \(\ell\ge6\), and in the residue-five row take \(\ell\ge5\); all other rows start at the least positive degree in that residue. The lower levels in the six rows are bounded below, respectively, by \(12/13,2/3,2/5,4/7,8/9,6/11\), while the upper levels are bounded above, respectively, by \(18/13,4/3,8/5,10/7,10/9,12/11\). Each fractional extremum is achieved at the smallest admissible degree in its row; monotonicity is immediate from the displayed linear numerators. This proves strict positivity, the global sharp bounds \(2/5\) and \(8/5\), and their unique degree-two occurrence. For \(\ell\ge1\), the minimum-norm interpolant to data \(y\in\mathbb C^6\) is \(E_\ell^*(E_\ell E_\ell^*)^{-1}y\), with universal sharp energy bounds \((5/8)\|y\|^2\le\|f_{\min}\|^2\le(5/2)\|y\|^2\).

**Optimal positive weights.** Let \(G=E_\ell E_\ell^*\), and let \(W\) be any positive diagonal matrix with \(\operatorname{tr}W=6\). The weighted sample Gram \(W^{1/2}GW^{1/2}\) has the same eigenvalues as \(B=G^{1/2}WG^{1/2}\). Conjugation by the rotational octahedral group acts transitively on either six-point class, induces permutation matrices \(P\), and leaves \(G\) invariant; it therefore commutes with \(G^{1/2}\). Averaging \(PBP^*\) over this group gives precisely \(G\), because the orbit-average of \(W\) is \(I\). Convexity of the maximal eigenvalue and concavity of the minimal eigenvalue imply \(\lambda_{\max}(B)\ge\lambda_{\max}(G)\) and \(\lambda_{\min}(B)\le\lambda_{\min}(G)\). Thus no positive reweighting improves the spectral condition number at the fixed degree.

## Verification
Run `python3 check_spectra.py` with Python 3 and NumPy. The program constructs both explicit six-quaternion configurations, verifies their ranks (four and three) and their exact relative-trace patterns, and, independently of the character-branch derivation, constructs symmetric-power \(SU(2)\) representation matrices for degrees one through six. It checks unitarity, compares the direct representation trace Gram matrices against the predicted six-by-six character matrices, and reproduces all eigenvalue multiplicities. Further corroborating scans test the sharp intervals through degree 10,000 and 1,000 positive random-weight instances. These finite calculations are not proofs for all degrees or all weights; the case analysis and group averaging above establish those statements.

## Relationship to prior work
Bangun, Behboodi and Mathar (initial public arXiv version 2020-10-05, arXiv:2010.02344) study mutual coherence of Wigner sampling on regular Euler-angle grids using Wigner \(3j\) identities and Legendre polynomial comparisons. Their all-degree regular-grid coherence inequalities neither specify the two six-point octahedral conjugacy classes nor evaluate their exact-degree sample Gram matrices. McEwen, Büttner, Leistedt, Peiris and Wiaux (2015, arXiv:1508.03101) develop a bandlimited equiangular sampling theorem rather than a classification on finite rotation conjugacy classes. The publicly indexed analysis *Exact Wigner sampling spectra on the twelve fivefold icosahedral rotations* (identifier `1e4c42991dc6`, 2026) uses a similar character-kernel framework on a twelve-element icosahedral class but does not imply the present six-point octahedral twin construction or the projective noncongruence. The publicly indexed *Sharp negative-type exponent and endpoint embedding rank for octahedral rotations* (identifier `99fe4bac94d9`, 2026) concerns the metric of the full 24-element group; it lists the separate 90-degree and edge 180-degree conjugacy classes but does not compare their internal six-point distance matrices, projective spans or Wigner interpolation spectra. The finite all-degree kernel and symmetrization principles are standard; the particular paired configurations and their sharp evaluated consequences are the claim evaluated here.

## Limitations
The statement classifies these two canonical six-rotation classes, not all six-point subsets of \(SO(3)\), all finite subgroup designs or higher-dimensional rotation groups. Kernel indistinguishability is only for conjugacy-invariant two-point functions: higher-order or noncentral measurements can distinguish the configurations. The all-degree stability bound assumes exactly one positive Wigner degree at a time and equal weights; positive reweighting has only the stated comparative optimality, not the same universal bound. No unique recovery of an arbitrary Wigner function from six samples is claimed. The accessible literature and indexed comparisons did not establish a previously published identical theorem; possible unindexed or implicitly equivalent earlier work is a residual priority risk. Independent validation has not been performed.

## References
1. A. Bangun, A. Behboodi, and R. Mathar, *Tight bounds on the mutual coherence of sensing matrices for Wigner D-functions on regular grids*, first posted 2020-10-05, arXiv:2010.02344, https://arxiv.org/abs/2010.02344.
2. J. D. McEwen, M. Büttner, B. Leistedt, H. V. Peiris, and Y. Wiaux, *A novel sampling theorem on the rotation group*, first posted 2015-08-13, arXiv:1508.03101, https://arxiv.org/abs/1508.03101.
3. *Exact Wigner sampling spectra on the twelve fivefold icosahedral rotations*, publicly indexed mathematical record (2026), identifier `1e4c42991dc6`.
4. *Sharp negative-type exponent and endpoint embedding rank for octahedral rotations*, publicly indexed mathematical record (2026), identifier `99fe4bac94d9`.
5. The normalized Peter–Weyl orthogonality and integer-spin character formula for \(SO(3)\) are used with their normalizations explicitly established above.
