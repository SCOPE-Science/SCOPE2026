# Parity-resolved exact metric-tiling counts on a two-row honeycomb torus

## Finding
Consider the standard combinatorial honeycomb with its hexagonal faces indexed by \(\mathbb Z/2\mathbb Z\times\mathbb Z/n\mathbb Z\), \(n\ge2\), with both periods identified. Assign each *labelled edge* one of two distinct positive lengths \(a,b\), while keeping the six edge directions of every hexagon separated by \(60^\circ\). Require the signed edge vectors to close on every face. Let \(\Omega_{2,n}\) be the number of such assignments (not divided by any translations, rotations or reflections). Then
\[
\boxed{\Omega_{2,n}=\begin{cases}
2^{n+3},&n\text{ odd},\\
12\cdot2^n+2\bigl(6^{n/2}+2^{n/2}\bigr),&n\text{ even}.
\end{cases}}
\]
The count is independent of the particular two positive length values. Moreover, configurations with any face having unequal opposite edge lengths exist **exactly when** \(n\ge4\) is even. Their number for \(n=2k\) is
\[
\boxed{2\left(6^k+2^k-2^{2k+1}\right).}
\]
The per-face logarithmic partition function, \((2n)^{-1}\log\Omega_{2,n}\), has two different limits along odd and even periods:
\[
\lim_{k\to\infty}\frac{\log\Omega_{2,2k+1}}{2(2k+1)}=\frac{\log2}{2},\qquad
\lim_{k\to\infty}\frac{\log\Omega_{2,2k}}{4k}=\frac{\log6}{4}.
\]
Thus the fixed-width thermodynamic limit without a parity restriction does not exist.

## Assumptions and scope
The quotient is the periodic \(2\times n\) honeycomb with \(2n\) distinct labelled faces and \(6n\) labelled edge occurrences modulo sharing. It is the quotient of the infinite honeycomb by two face-lattice periods; for \(n=2\), multiple distinct edges may separate the same pair of quotient faces. Such edges remain individually labelled. No geometric non-overlap condition beyond the source's linear per-face closure equations is imposed. Strict positivity of the two length values ensures individually convex equiangular hexagons but is not needed for the discrete counting argument. The result concerns solutions of *face closure* on this fixed periodic network, not a classification of arbitrary tilings of the Euclidean plane.

Since the vector sum of six unit directions at \(60^\circ\) intervals is zero, an affine change of all lengths \(\ell\mapsto(\ell-a)/(b-a)\) preserves each face-closure equation and bijects the allowed alphabet with \(\{0,1\}\). Work with the binary values below.

Write face indices as \(x=(i,j)\), with \(i\) modulo \(2\) and \(j\) modulo \(n\). Its three positively indexed edge families are \(A_x,B_x,C_x\in\{0,1\}\), with dual neighbour increments \(u=(1,0)\), \(v=(0,1)\), \(w=v-u=(-1,1)\). Each actual edge appears once in exactly one of these three arrays; the opposite edge to \(A_x\) of the face is \(A_{x-u}\), and similarly for the other two families. Choosing edge-direction vectors \(p,q,r\) with \(p-q+r=0\) reduces face closure precisely to the existence of a scalar \(t_x\) such that
\[
A_x-A_{x-u}=t_x,\qquad B_x-B_{x-v}=-t_x,\qquad C_x-C_{x-w}=t_x.
\tag{1}
\]
This also fixes the orientation convention and makes all boundary identifications explicit.

## Proof
**1. The two-row reduction.** By the first equation in (1), \(t_{0,j}=-t_{1,j}\). Put \(s_j=t_{0,j}\in\{-1,0,1\}\). If \(s_j=0\), the first equation permits exactly two choices for \((A_{0,j},A_{1,j})\), namely \((0,0)\) or \((1,1)\). If \(s_j=1\) or \(-1\), it permits exactly one choice, \((1,0)\) or \((0,1)\).

The second equation shows that \(B_{0,j}+B_{1,j}\) is independent of \(j\), and the third shows the same for \(C_{0,j}+C_{1,j}\). If some \(s_j\ne0\), binary integrality forces both constants to be \(1\). Hence \(B_{1,j}=1-B_{0,j}\) and \(C_{1,j}=1-C_{0,j}\). Writing \(b_j=B_{0,j}\) and \(c_j=C_{0,j}\), equation (1) is then exactly
\[
b_j-b_{j-1}=-s_j,\qquad c_j+c_{j-1}-1=s_j.
\tag{2}
\]

**2. Four-state finite transfer.** Index the states \((b,c)\) as \((0,0),(0,1),(1,0),(1,1)\). A zero shear \(s_j=0\) leaves \(b\) unchanged and replaces \(c\) by \(1-c\), with multiplicity \(2\) from the two \(A\)-choices. A positive shear is possible only from \((1,1)\) to \((0,1)\), and a negative shear only from \((0,0)\) to \((1,0)\), each with multiplicity \(1\). The complete weighted transition matrix, with rows giving starting states, is
\[
T=\begin{pmatrix}0&2&1&0\\2&0&0&0\\0&0&0&2\\0&1&2&0\end{pmatrix}.
\]
The trace \(\operatorname{tr}(T^n)\) counts cyclic binary assignments satisfying (1) **within** the sector whose \(B\)- and \(C\)-row sums are both \(1\). This sector includes all nonzero-shear solutions, but also some zero-shear solutions. A direct determinant expansion gives
\[
\det(zI-T)=(z^2-6)(z^2-2),\qquad
\operatorname{tr}(T^n)=\begin{cases}0,&n\text{ odd},\\2(6^{n/2}+2^{n/2}),&n\text{ even}.\end{cases}
\tag{3}
\]

**3. The zero-shear sector and subtraction.** When \(s_j=0\) for every \(j\), the \(A\)-variables contribute \(2^n\), the two \(B\)-rows contribute \(4\), and the \(C\)-variables are forced to alternate their row positions from one column to the next. They contribute \(2\) choices for odd \(n\) and \(4\) for even \(n\). Therefore the entire zero-shear sector has size \(8\cdot2^n\) for odd \(n\), or \(16\cdot2^n\) for even \(n\). Of these, exactly \(0\) for odd \(n\) or \(4\cdot2^n\) for even \(n\) have both conserved row sums equal to \(1\). Combining this with (3) gives
\[
\Omega_{2,n}=\Omega_{\mathrm{zero}}(2,n)+\operatorname{tr}(T^n)-4\cdot2^n\mathbf1_{2\mid n},
\]
which simplifies to the claimed closed formula.

**4. Parity and existence of actual shears.** The nonzero-shear count for \(n=2k\) is the even trace in (3) minus \(4\cdot2^{2k}\), yielding the second displayed formula. For \(n=2\) this is \(0\). For every \(k\ge2\), strict convexity of \(x\mapsto x^k\) gives \(6^k+2^k>2\cdot4^k\), hence a strictly positive count. For odd \(n\), (3) gives no nonzero shears. The parity obstruction can also be seen directly from (2): nonzero \(s_j\) alternate between \(+1\) and \(-1\), and the number of zero-shear columns between consecutive nonzero columns must be odd. Consequently every cyclic nonzero-shear word has even length and length at least four.

**5. Asymptotics.** The odd-period count is exactly \(2^{n+3}\), while along even \(n=2k\), the term \(2\cdot6^k\) dominates all other terms in the count. Dividing their logarithms by the \(2n\) faces yields the two distinct limits.

## Verification
The accompanying executable `check_honeycomb.py` independently enumerates all possible shear fields and solves binary edge equations around every orientation cycle, rather than relying on the four-state matrix. It matches the formula for each \(2\times n\) quotient with \(2\le n\le9\), and reproduces the source paper's independently reported \(3\times3\) benchmark \(518\). It also checks the matrix/closed-form identity for every \(2\le n<45\). Initial width-two counts at \(n=2,3,4,5,6\) are \(64,64,272,256,1216\). These finite checks do not prove the infinite family; the five proof steps above do.

Reproduce using `python3 check_honeycomb.py` with the Python standard library.

## Relationship to prior work
Wu and Ji [1] introduced the finite-alphabet equiangular metric-tiling ensemble, established affine alphabet invariance, used transfer-matrix counts, and reported the simple \(k^{L_x+L_y+1}\) count on tested coprime periods as well as the \(3\times3\) binary count \(518\). In particular, the **odd** \(2\times n\) count here agrees with that prior coprime-period formula. The contribution here is the *all-even-period explicit closed form*, the exact count and necessary/sufficient existence condition for nonzero-shear sectors, and the two distinct subsequential entropy values for the minimal-width torus. The source's general transfer methodology can compute finite cases but its inspected main text does not state this all-period symbolic classification.

## Limitations
This theorem counts edge-labelled local closure assignments on one natural width-two quotient. It does not give an exact count at arbitrary width, a universal planar entropy, or a global embedded-tiling theorem. The primary article refers to supplemental methods and numerical tables not fully accessible in this review; the possibility that an explicit equivalent width-two expression occurs there remains a priority risk. The exact formula is derived afresh here but independent mathematical or historical validation has not been performed.

## References
[1] Xinyan Wu and Qingqing Ji, *Metric random tilings: exact entropy and the diffraction of counted disorder*, arXiv:2611.16730v1, first posted 2026-11-12, https://arxiv.org/abs/2611.16730; HTML https://arxiv.org/html/2611.16730v1 (accessed 2026-11-17 UTC).
