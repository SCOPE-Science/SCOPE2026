# Exact one-way sign transitions in three-step Lanczos graph heat propagation

## Finding
Let \(G=(V,E,w)\) be any finite connected simple undirected graph with positive edge weights, with weighted combinatorial Laplacian \(L\). Fix a source vertex \(r\). Suppose the ordinary **symmetric three-step Lanczos process** with starting vector \(e_r\) reaches three orthonormal basis vectors, and write \(T_3\) for its symmetric tridiagonal projected matrix. The exact-arithmetic Lanczos approximation to the heat response is
\[
y_3(t)=Q_3e^{-tT_3}e_1,\qquad t\ge0.
\]
Let \(a_0,a_1,a_2\) be the diagonal entries of \(T_3\), let \(b_0,b_1>0\) be the off-diagonal entries, and let \(\vartheta\) be its smallest eigenvalue. For a neighbor \(i\sim r\), put
\[
 d_i=\sum_j w_{ij},\qquad
 c_{ri}=\sum_{k\ne r,i}w_{rk}w_{ik},\qquad
 \widehat d_{ri}=d_i-\frac{c_{ri}}{w_{ri}},
\]
with nonexistent-edge weights interpreted as zero. Define the **local sign margin**
\[
 H_{ri}=a_1+a_2-\vartheta-\widehat d_{ri}.
\]
Then, for every finite \(t>0\), the root coordinate is positive, every coordinate at graph distance two is positive, and every coordinate at graph distance at least three is exactly zero. A neighboring coordinate obeys the complete dichotomy:

- If \(H_{ri}\ge0\), then \(y_{3,i}(t)>0\) for **all** \(t>0\).
- If \(H_{ri}<0\), then there is **exactly one** \(t_{ri}>0\) at which \(y_{3,i}(t_{ri})=0\); it is positive before this time and negative afterwards.

In particular, the three-step approximation is componentwise nonnegative for every nonnegative time **if and only if** \(\widehat d_{ri}\le a_1+a_2-\vartheta\) for all neighbors \(i\sim r\). It never develops a negative coordinate farther than one edge from the source, and it never recovers positivity at a neighbor once that neighbor has become negative.

On a tree, \(c_{ri}=0\), so the test depends only on the incident neighbor degree, three Lanczos diagonals, and the smallest projected Ritz value. A five-vertex weighted tree gives a strict, exactly certified failure: take edges \((0,1),(0,3),(0,4),(1,2)\) with respective conductances \(1,4,40,60\), and source \(r=0\). Here
\[
 a_0=45,\quad b_0^2=1617,\quad
 a_1=\frac{21375}{539},\quad
 b_1^2=\frac{4417376}{290521},\quad
 a_2=\frac{1471877080}{74405177},
\]
so
\[
 \widehat d_{01}=61,
 \qquad \widehat d_{01}-a_1-a_2=\frac{215528}{138043}>0.
\]
Because \(\vartheta\ge0\), the neighbor \(1\) necessarily turns negative at exactly one positive time, whereas the exact heat response \(e^{-tL}e_0\) is strictly positive everywhere for every \(t>0\). A supplementary evaluation gives \(t_{01}\approx0.118162675755\) and \(y_{3,1}(0.2)\approx-0.001188200823\). No minimal-order assertion is made.

## Assumptions and scope
The graph has finitely many vertices, one positive weight per undirected edge, no loops, and no negative edges. All Lanczos operations are performed in exact arithmetic, with orthonormal basis signs chosen so that \(b_0,b_1>0\). The starting vector is a unit coordinate vector \(e_r\). The displayed theorem requires \(b_1>0\); if Lanczos terminates at or before step two, its approximation is already the **exact** strictly positive heat response at all positive times on a connected graph. If Lanczos terminates at step three, the three-step response is likewise exact. The result concerns a single, unrestarted polynomial Krylov approximation, not a rational Krylov method, entrywise positivity of the entire matrix function approximation, or finite-precision orthogonality loss. The truncated approximation need not conserve total mass.

## Proof
**1. Exact Lanczos coordinates.** Put \(q_0=e_r\), \(a_0=q_0^TLq_0=d_r\), and
\[
 b_0=\|(L-a_0I)q_0\|_2,\qquad q_1=(L-a_0I)q_0/b_0.
\]
The first residual has \(q_{1,r}=0\) and \(q_{1,i}=-w_{ri}/b_0\) at neighbors of \(r\), and is zero elsewhere. Set \(a_1=q_1^TLq_1\),
\[
 b_1=\|Lq_1-b_0q_0-a_1q_1\|_2,\quad
 q_2=(Lq_1-b_0q_0-a_1q_1)/b_1,\quad a_2=q_2^TLq_2.
\]
At the root \(q_{2,r}=0\); at a neighbor \(i\), direct multiplication gives
\[
 q_{2,i}=-\frac{w_{ri}}{b_0b_1}(\widehat d_{ri}-a_1).
\]
At graph distance two,
\[
 q_{2,j}=\frac{1}{b_0b_1}\sum_{k\sim r,\ k\sim j}w_{rk}w_{kj}>0,
\]
and it vanishes at all more distant vertices. These identities hold with triangles and multiple two-step paths because each counted weight is positive.

**2. Reduced semigroup signs.** The tridiagonal matrix is
\[
 T_3=\begin{pmatrix}a_0&b_0&0\\b_0&a_1&b_1\\0&b_1&a_2\end{pmatrix}.
\]
Let \(S=\operatorname{diag}(1,-1,1)\). The matrix \(K=-ST_3S\) has strictly positive nearest-neighbor off-diagonals and is irreducible Metzler. Thus
\[
 p(t)=e^{tK}e_1=(p_0(t),p_1(t),p_2(t))^T
\]
has strictly positive coordinates for every \(t>0\). Because \(e^{-tT_3}e_1=Sp(t)\), one obtains
\[
 y_{3,r}(t)=p_0(t),\qquad
 y_{3,i}(t)=\frac{w_{ri}}{b_0}\left[p_1(t)-\frac{\widehat d_{ri}-a_1}{b_1}p_2(t)\right]
\]
for neighbors, and \(y_{3,j}(t)=q_{2,j}p_2(t)\) at distance two. This proves all non-neighbor signs and supports.

**3. The asymptotic sign.** Since \(K\) is irreducible Metzler and symmetric, its largest eigenvalue \(-\vartheta\) is simple with a strictly positive eigenvector \(h=(h_0,h_1,h_2)^T\). Its last row implies \(b_1h_1=(a_2-\vartheta)h_2\). Consequently, the coefficient of the slowest exponential \(e^{-\vartheta t}\) in the neighboring response is a positive scalar multiple of
\[
 (a_2-\vartheta)-(\widehat d_{ri}-a_1)=H_{ri}.
\]
Here \(a_2-\vartheta>0\), as is also immediate from the eigenvector relation.

**4. No second crossing.** The three eigenvalues of the irreducible real symmetric tridiagonal \(T_3\) are distinct. Thus every neighboring response is a nonzero real linear combination of three exponentials with three distinct real exponents. Such a combination has at most two real zeros, **counting multiplicity**: divide by any one exponential, differentiate, and apply Rolle's theorem to the remaining sum of two exponentials, whose derivative has at most one zero. Each neighbor has \(y_{3,i}(0)=0\) and \(y'_{3,i}(0)=w_{ri}>0\), because the Lanczos projection reproduces the degree-one polynomial \(Lq_0\) exactly. One of the at most two zeros is therefore already at \(t=0\). If \(H_{ri}>0\), the response is positive both just after zero and asymptotically, so a negative interval would force two additional positive zeros, impossible. If \(H_{ri}<0\), the sign is ultimately negative and must cross exactly once. If \(H_{ri}=0\), the slowest exponential coefficient vanishes: the remaining two exponentials have a zero at zero and positive derivative there, hence form a strictly positive difference for every positive time. This proves all cases, including the equality boundary.

**5. Exact witness arithmetic.** On the stated five-vertex tree, the three Lanczos diagonal quantities and squared off-diagonals follow from the rational matrix identities
\[
 k=(L-a_0I)e_0,\quad b_0^2=k^Tk,\quad a_1=\frac{k^TLk}{k^Tk},\quad
 v=(L-a_1I)k-b_0^2e_0,\quad b_1^2=\frac{v^Tv}{b_0^2},\quad a_2=\frac{v^TLv}{v^Tv}.
\]
They give exactly \(a_1+a_2=8205095/138043\). Since the Laplacian and its compression are positive semidefinite, \(\vartheta\ge0\), and the strictly negative margin at neighbor \(1\) follows without any floating-point root calculation. The projected characteristic polynomial is
\[
 \det(\lambda I-T_3)=\frac{138043\lambda^3-14417030\lambda^2+252207736\lambda-363098400}{138043}.
\]
This also locates \(\vartheta\) strictly between \(1\) and \(2\). The other two source neighbors have adjusted degrees \(4\) and \(40\), and therefore satisfy the positivity criterion. Vertex \(2\) is at graph distance two and remains positive. The exact graph heat kernel is strictly positive at every positive time because \(-L\) is an irreducible Metzler matrix.

## Verification
The accompanying `verify.py` reconstructs Lanczos coefficients from exact rational weighted Laplacians, checks the local triangle-adjusted formulas and distance-two supports on nine nontrivial test graphs with multiple roots, and verifies the exact rational witness and its projected characteristic polynomial. It also independently diagonalizes the projected matrices to check signs at five positive times per eligible source (200 source/time checks), together with a supplementary crossing estimate. Run `python3 verify.py` with Python 3, SymPy, NumPy and SciPy. Finite tests verify the arithmetic and selected cases, **not** the unrestricted graph theorem or the zero-count lemma; those are proved above.

## Relationship to prior work
Hochbruck and Lubich (1997) establish classical Krylov matrix-function approximation and norm-error estimates; Orecchia, Sachdeva, and Vishnoi (first publicly posted November 6, 2011) employ the Lanczos exponential approximation for graph spectral computation and establish a spectral-norm approximation guarantee. The approximation definition and polynomial-exactness mechanism are prior work. Druskin (2008, available online June 17) proves strict approximation-norm/error monotonicity and positivity of *reduced Jacobi-coordinate* semigroups. Reduced-coordinate positivity is not physical-coordinate positivity after multiplication by a signed Lanczos basis. A 2026 result on incomplete Lanczos exponentials proves a parity sign law for an extreme eigenvalue coordinate when the original matrix is diagonal and the starting vector is strictly positive; it does not classify graph-Laplacian neighbor coordinates from a point source. A two-step diagonal-system positivity-horizon result likewise does not provide the degree-three graph-local criterion. The new contribution here is the complete **original-coordinate, three-step graph-local sign test** and its non-reentrant crossing classification, not any of these classical numerical identities.

## Limitations
The numerical time at which a negative neighbor crosses is generally specified implicitly, not in elementary closed form; the theorem gives an exact yes/no condition and uniqueness. The weighted example is not claimed to be minimal in order or conductance range. The theorem applies at depth three only, and full-depth, restarted, rational, or finite-precision methods are separate questions. Literature searches and full-text comparisons support best-knowledge originality, not proof of publication priority. In particular, a differently phrased statement in older exponential-interpolation literature may remain undiscovered.

## References
1. V. Druskin, *On monotonicity of the Lanczos approximation to the matrix exponential*, Linear Algebra and its Applications 429 (2008), 1679–1683, DOI: https://doi.org/10.1016/j.laa.2008.04.046 (online June 17, 2008).
2. M. Hochbruck and C. Lubich, *On Krylov Subspace Approximations to the Matrix Exponential Operator*, SIAM J. Numer. Anal. 34 (1997), 1911–1925, DOI: https://doi.org/10.1137/S0036142995280572; open preprint: https://na.math.kit.edu/download/papers/exp.pdf.
3. L. Orecchia, S. Sachdeva, N. K. Vishnoi, *Approximating the Exponential, the Lanczos Method and an \(\widetilde O(m)\)-Time Spectral Algorithm for Balanced Separator*, Optimization Online, first public posting 2011-11-06, https://optimization-online.org/2011/11/3231/.
4. *Parity and the unique extreme-mode sign transition in incomplete Lanczos exponentials* (2026-10-26), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-parity-and-the-unique-extreme-mode-sign-transition-in-incomplete--66922def8ca6.
5. *The exact positivity horizon of the two-step Lanczos exponential* (2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-exact-positivity-horizon-of-the-two-step-lanczos-exponential--fb3579f163d8.
