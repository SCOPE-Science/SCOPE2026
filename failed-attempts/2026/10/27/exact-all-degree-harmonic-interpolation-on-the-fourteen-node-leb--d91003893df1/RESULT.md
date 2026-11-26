# Exact all-degree harmonic interpolation on the fourteen-node Lebedev sphere

## Finding

Let \(X\) be the union of the six coordinate-axis points \(\{\pm e_1,\pm e_2,\pm e_3\}\) and the eight unit body-diagonal points \(\{(\pm1,\pm1,\pm1)/\sqrt3\}\) on \(S^2\). These are the nodes of the classical fourteen-point, fifth-order Lebedev integration rule. Let \(E_\ell\) evaluate **real spherical harmonics of exactly degree** \(\ell\ge0\) at all fourteen nodes. Then

\[
\operatorname{rank} E_\ell=\begin{cases}
1,&\ell=0,\\
3,&\ell=1,\\
5,&\ell=2,\\
4,&\ell=3,\\
6,&\ell\in\{4,5,6,8,10,14\},\\
7,&\text{all remaining integers }\ell\ge0.
\end{cases}
\]

The dimension of the parity-compatible data space is seven; thus every such data set can be interpolated by harmonics of any individual degree \(\ell\ge15\), and this is the smallest **persistent** threshold. There are earlier surjective degrees, but degree \(14\) has rank six. At this exceptional degree the unique (up to scale) missing interpolation functional is

\[
\sum_{x\in X_{\rm axis}}f(x)-\frac{729}{1024}\sum_{x\in X_{\rm corner}}f(x)=0
\qquad\text{for every }f\in\mathcal H_{14}(S^2).
\]

## Assumptions and scope

The sphere is the ordinary unit two-sphere in \(\mathbb R^3\). The fourteen nodes are distinct and antipodally paired. The space \(\mathcal H_\ell(S^2)\) consists of restrictions of real homogeneous harmonic polynomials of degree \(\ell\). The evaluation map is unweighted, although multiplying individual rows by nonzero cubature weights would not change its rank. Because \(f(-x)=(-1)^\ell f(x)\), its image is contained in a seven-dimensional parity space. The theorem concerns one exact degree at a time, **not** simultaneous bands of degrees or quadrature accuracy.

## Proof

**Step 1: Legendre Gram reduction.** Normalize the Legendre polynomial by \(P_\ell(1)=1\). The spherical-harmonic addition theorem identifies the rank of \(E_\ell\) with that of the seven-by-seven matrix \(G_\ell=(P_\ell(x_i\cdot x_j))_{i,j=1}^{7}\), where we choose representatives \(e_1,e_2,e_3\) and \((1,u,v)/\sqrt3\) for \(u,v\in\{\pm1\}\). Indeed the full fourteen-point matrix consists of antipodally redundant rows; the seven-representative Gram is positive semidefinite and has exactly the evaluation rank.

Set
\[
 b=P_\ell(0),\quad c=P_\ell(1/3),\quad d=P_\ell(1/\sqrt3).
\]
Every off-diagonal inner product of the representatives is one of \(0,\pm1/3,\pm1/\sqrt3\).

**Step 2: Separate parity.** If \(\ell\) is even, the three axis rows and four corner rows give, after an orthogonal symmetry change of basis, eigenvalues \(1-b\) twice, \(1-c\) three times, and the two eigenvalues of
\[
 B_\ell^{\rm even}=\begin{pmatrix}1+2b&2\sqrt3\,d\\2\sqrt3\,d&1+3c\end{pmatrix}.
\]
The last block's determinant is \(\Delta_\ell=(1+2b)(1+3c)-12d^2\). If \(\ell\) is odd, the four corner rows diagonalize in the characters \(1,u,v,uv\); the first three couple one-to-one to the axis rows. Thus there are three copies of the block
\[
 B_\ell^{\rm odd}=\begin{pmatrix}1&2d\\2d&1+c\end{pmatrix},
\]
with determinant \(\delta_\ell=1+c-4d^2\), and one extra eigenvalue \(1-3c\). All displayed blocks are positive semidefinite by the addition theorem. These block decompositions reduce every rank assertion to exact arithmetic in three Legendre values.

**Step 3: Exact finite classification.** For all integer degrees \(0\le\ell\le28\), compute those Legendre values with the recurrence
\[
 (\ell+1)P_{\ell+1}(t)=(2\ell+1)tP_\ell(t)-\ell P_{\ell-1}(t),
 \quad P_0(t)=1,\quad P_1(t)=t.
\]
At \(t=0\) and \(1/3\) values are rational; at \(t=1/\sqrt3\), values lie in \(\mathbb Q(\sqrt3)\), with rational squares. The exact-rational standalone checker included with this result records all degrees and independently computes every seven-by-seven Gram rank by fraction-only Gaussian elimination. It proves the finite lists
\[
 \{\ell\text{ even}:\Delta_\ell=0\}=\{0,2,4,6,8,10,14\},
\]
\[
 \{\ell\text{ odd}:\delta_\ell=0\}=\{1,3\},\qquad
 \{\ell\text{ odd}:1-3c=0\}=\{1,5\}.
\]
The remaining scalar and block-diagonal factors are strictly positive except at the explicitly reported initial degrees. Substitution gives exactly the ranks stated in the finding. At degree fourteen, the constant-axis and constant-corner null vector of the even block has a corner-to-axis coordinate ratio \(-729/1024\), which yields the displayed functional identity for all degree-fourteen harmonics.

**Step 4: Exclude every later defect.** We use the classical Bernstein inequality for Legendre polynomials: for any integer \(\ell\ge1\) and \(|t|<1\),
\[
 |P_\ell(t)|\le \sqrt{\frac{2}{\pi\ell\sqrt{1-t^2}}}.
\]
For all off-diagonal inner products in our seven-point representative set, \(\sqrt{1-t^2}\ge\sqrt{2/3}>4/5\). When \(\ell\ge29\), use \(\pi>157/50\) and the exact rational inequality \(72<(157/50)\cdot29\cdot(4/5)\) to obtain \(6|P_\ell(t)|<1\). The sum of absolute off-diagonal entries in every Gram row is therefore less than one, whereas every diagonal entry is one. Strict diagonal dominance of the real symmetric Gram matrix implies positive definiteness, so \(\operatorname{rank} E_\ell=7\) for every \(\ell\ge29\). Together with Step 3 this completes the classification and establishes the sharp persistent threshold.

## Verification

Run `python3 CHECKER.py` with standard Python 3. The checker uses no external packages and no floating-point rank thresholds. It prints and tests the ranks of all twenty-nine degrees from zero through twenty-eight using both block determinants and full rational Gaussian elimination, verifies the degree-fourteen null ratio, and verifies the numerical constants used in the rigorous Bernstein/Gershgorin tail. `CHECKER_OUTPUT.txt` is the actual replayed output. The infinite statement for degree at least twenty-nine follows analytically from Step 4; the finite checker is not claimed to enumerate that infinite tail.

## Relationship to prior work

The fourteen-node Lebedev cubature integrates spherical polynomials exactly through degree five, a property documented in numerical integration references. Rogers's real-space quadrature treatment develops discrete harmonic representations and identities conditional on prescribed cubature exactness, and Beentjes surveys and analyzes spherical quadrature schemes. Those results address integration and finite-band reconstruction; they do not directly provide the rank at **each arbitrarily high exact degree** for this fixed fourteen-point grid. Our all-degree interpolation classification, including its isolated degree-fourteen null functional, is a different assertion. It is not implied by the ordinary fifth-order cubature property.

## Limitations

The theorem is for precisely these fourteen spherical nodes. It does not establish equivalent ranks for arbitrary Lebedev orders, other spherical designs, or full multidimensional interpolation in a band of degrees. A bound from classical Legendre theory closes the infinite tail; the detailed low-degree rank table is established by reproducible exact rational arithmetic. Literature coverage is bounded; an equivalent pre-existing calculation under different terminology remains possible. This work has not undergone independent mathematical validation.

## References

- D. M. Rogers, *Real-space quadrature: a convenient, efficient representation for multipole expansions*, arXiv:1411.0011, initially public 2014-10-31, https://arxiv.org/abs/1411.0011.
- C. H. L. Beentjes, *Quadrature on a spherical surface*, technical report, 2015, https://cbeentjes.github.io/files/Ramblings/QuadratureSphere.pdf.
- GNU Scientific Library, *Numerical Integration: Lebedev quadrature*, https://www.gnu.org/software/gsl/doc/html/integration.html, documenting fourteen points and fifth-order exactness.
- G. Szegő, *Orthogonal Polynomials*, fourth edition, American Mathematical Society, 1975, classical Legendre–Bernstein inequality.
