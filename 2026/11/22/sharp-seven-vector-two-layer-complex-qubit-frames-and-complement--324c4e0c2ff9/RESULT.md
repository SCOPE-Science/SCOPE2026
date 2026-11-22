# Sharp seven-vector two-layer complex qubit frames and complementary spherical designs

## Finding

Let a two-layer complex qubit stratified unit-norm tight frame mean two indexed sequences of unit vectors \((\phi_{1,i})_{i=1}^N\), \((\phi_{2,i})_{i=1}^N\) in \(\mathbb C^2\), each a unit-norm tight frame, for which \(\sum_{r=1}^2|\langle\phi_{r,i},\phi_{r,j}\rangle|^2\) is constant for distinct indices. For integers \(N\ge2\), such a frame exists **if and only if** \(2\le N\le7\). In particular, the complex two-layer seven-vector case attains the sharp stratified Gerzon bound, whereas the corresponding real two-layer, two-dimensional bound is five.

At the extremal size \(N=7\), any such pair is equivalent, under the Bloch-sphere identification of complex projective one-space with \(S^2\), to two indexed point sets \(u_1,\ldots,u_7\) and \(v_1,\ldots,v_7\) in \(S^2\) satisfying
\[
\sum_{i=1}^{7}u_i=\sum_{i=1}^{7}v_i=0,\qquad
U^{\mathsf T}U=V^{\mathsf T}V=\frac73 I_3,\qquad U^{\mathsf T}V=0,
\]
where \(U,V\) are the \(7\times3\) matrices whose rows are the respective points. Conversely, every such pair produces a seven-vector two-layer qubit frame. Thus both layers individually form equally weighted real spherical two-designs, and their centered coordinate spaces are orthogonal complements inside the six-dimensional subspace of \(\mathbb R^7\) orthogonal to the constant vector.

## Assumptions and scope

All fields are complex except for the real Bloch coordinates. Multiplicities and repeated projective directions are permitted, as in the standard definition of a finite unit-norm tight frame. The index sets are labelled: the stratification constraint compares identical index pairs across layers. A complex unit vector represents its rank-one projector, so its arbitrary overall phase is immaterial. Define the Pauli matrices
\[
\sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\sigma_y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
\sigma_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
For each \(u\in S^2\), the matrix \(P(u)=\tfrac12(I_2+u_1\sigma_x+u_2\sigma_y+u_3\sigma_z)\) is a rank-one orthogonal projector. Choose any unit vector \(\phi(u)\) in its range. The claims concern exact existence and the maximal-size structural identities; they do not classify all such frames modulo unitary transformations.

## Proof

**Bloch reduction.** Pauli matrix traces give
\[
|\langle\phi(u),\phi(v)\rangle|^2=\operatorname{tr}(P(u)P(v))=\frac{1+u\cdot v}{2}.
\]
Also \(\sum_iP(u_i)=(N/2)I_2\) holds exactly when \(\sum_i u_i=0\). Consequently, the two-layer frame conditions are equivalent to
\[
\sum_i u_i=\sum_i v_i=0,\qquad
u_i\cdot u_j+v_i\cdot v_j=-\frac2{N-1}\quad (i\ne j).
\]
Indeed, both tight layers imply that the constant sum of squared overlaps must be \((N-2)/(N-1)\): summing over \(j\ne i\) in each layer gives \(N/2-1=(N-2)/2\). Alternatively the zero sums of the Bloch vectors force the dot-product constant \(-2/(N-1)\). Form the real \(N\times6\) matrix \(Z=[U\ V]\). Since every row of \(Z\) has squared norm two, its entire row Gram matrix must be
\[
ZZ^{\mathsf T}=\frac{2N}{N-1}\left(I_N-\frac1N\mathbf1\mathbf1^{\mathsf T}\right).
\tag{1}
\]
Its rank is \(N-1\), while \(Z\) has at most six columns. Therefore \(N\le7\). This proves nonexistence above seven without assuming any parametrization or numerical search.

**Constructing all permitted sizes.** In the following, each displayed \(u\)-point and \(v\)-point is mapped independently to a unit qubit vector through its projector \(P\). It is enough to verify zero sums and the constant dot-product identity above.

For \(N=2\), take both layers as the north and south poles \((0,0,1),(0,0,-1)\). For \(N=3\), take both layers as the equatorial regular triangle \((\cos(2\pi j/3),\sin(2\pi j/3),0)\), \(0\le j<3\). For \(N=4\), take both layers as the tetrahedral points \((\pm1,\pm1,\pm1)/\sqrt3\) with an even number of negative signs. Their distinct within-layer dot products are \(-1\), \(-1/2\), and \(-1/3\), respectively. For \(N=5\), take
\[
u_j=(\cos(2\pi j/5),\sin(2\pi j/5),0),\qquad
v_j=(\cos(4\pi j/5),\sin(4\pi j/5),0),\quad 0\le j<5.
\]
The fifth-root identity gives \(u_i\cdot u_j+v_i\cdot v_j=-1/2\) for distinct indices.

For \(N=6\), put \(r=2/\sqrt5\), \(h=1/\sqrt5\), and \(p_j=(r\cos(2\pi j/3),r\sin(2\pi j/3))\) for \(0\le j<3\). Set
\[
\begin{array}{ll}
u_j=(p_j,h),&v_j=(p_j,h),\\
u_{3+j}=(p_j,-h),&v_{3+j}=(-p_j,-h).
\end{array}
\]
Here \((p,z)\) denotes the vector whose first two coordinates are \(p\) and whose last coordinate is \(z\). The two zero sums follow from \(\sum_jp_j=0\). For indices within the same triangle, \(p_j\cdot p_k=-r^2/2\), yielding \(-r^2+2h^2=-2/5\) as their sum across layers. For two corresponding points from opposite triangles, the sum is \(-2h^2=-2/5\); for noncorresponding points in opposite triangles, their planar contributions cancel and the sum is also \(-2h^2\). All six points in each layer have norm one, since \(r^2+h^2=1\).

For \(N=7\), set \(p_j=(\cos(2\pi j/3),\sin(2\pi j/3))\), \(0\le j<3\), and \(q_k=(\cos(\pi k/2),\sin(\pi k/2))\), \(0\le k<4\). Define
\[
\begin{array}{ll}
u_j=(\frac{\sqrt5}{3}p_j,\frac23),&v_j=(p_j,0),\\
u_{3+k}=(\frac{\sqrt3}{2}q_k,-\frac12),&v_{3+k}=(-\sqrt{\frac5{12}}q_k,\sqrt{\frac7{12}}(-1)^k).
\end{array}
\tag{2}
\]
The top and bottom group sums of the first two coordinates vanish. The third coordinates of \(U\) sum to \(3(2/3)+4(-1/2)=0\), while those of \(V\) sum to zero by alternating signs. Each row has norm one. Standard regular-polygon moment identities yield
\[
\sum_{j=0}^{2}p_jp_j^{\mathsf T}=\frac32I_2,\quad
\sum_{k=0}^{3}q_kq_k^{\mathsf T}=2I_2,\quad
\sum_{k=0}^{3}(-1)^kq_k=0.
\]
The horizontal diagonal blocks of \(U^{\mathsf T}U\), \(V^{\mathsf T}V\), and \(U^{\mathsf T}V\) are, respectively,
\[
\left(\frac59\cdot\frac32+\frac34\cdot2\right)I_2=\frac73 I_2,\qquad
\left(\frac32+\frac5{12}\cdot2\right)I_2=\frac73 I_2,\qquad
\left(\frac{\sqrt5}{3}\cdot\frac32-\frac{\sqrt3}{2}\sqrt{\frac5{12}}\cdot2\right)I_2=0.
\]
The vertical diagonal entries are \(3(4/9)+4(1/4)=7/3\) and \(4(7/12)=7/3\); the mixed vertical entry and all horizontal-vertical entries vanish. Thus
\[
U^{\mathsf T}U=V^{\mathsf T}V=\frac73I_3,
\qquad U^{\mathsf T}V=0.
\tag{3}
\]
Since \(\mathbf1^{\mathsf T}U=\mathbf1^{\mathsf T}V=0\), the six columns of \([U\ V]\) are mutually orthogonal with squared norm \(7/3\) and span \(\mathbf1^{\perp}\). Hence \(ZZ^{\mathsf T}=(7/3)(I_7-\mathbf1\mathbf1^{\mathsf T}/7)\), exactly (1), completing the existence argument.

**Rigidity at \(N=7\).** Conversely, suppose any seven-pair SUNTF is given. Equation (1) reads \(UU^{\mathsf T}+VV^{\mathsf T}=(7/3)P\), where \(P=I_7-\mathbf1\mathbf1^{\mathsf T}/7\) is a rank-six orthogonal projector. Let \(A=(3/7)UU^{\mathsf T}\), \(B=(3/7)VV^{\mathsf T}\). Both are positive semidefinite, \(A+B=P\), and both have rank at most three. Since \(\operatorname{rank}P=6\), both have rank exactly three. Moreover \(0\preceq A,B\preceq P\) implies all their eigenvalues lie in \([0,1]\), while \(\operatorname{tr}A=\operatorname{tr}B=(3/7)\cdot7=3\). Each must therefore be a rank-three orthogonal projector. In particular \(AB=0\). Full column rank implies \(U^{\mathsf T}U=V^{\mathsf T}V=(7/3)I_3\) and \(U^{\mathsf T}V=0\). The zero-sum identities were already established. Conversely these conditions, together with each row having unit norm, imply (1) and hence the two-layer SUNTF conditions. This proves the stated characterization.

## Verification

The algebraic certificate is the explicit identities (1)--(3); no finite sampling is used to prove a universal rank or optimality statement. A separate standard-library Python program `verify.py` reconstructs examples for each \(N=2,3,4,5,6,7\) and checks the norms, centroids and every off-diagonal Gram entry, together with the three \(3\times3\) moment blocks at seven. Executing it as `python3 verify.py` produced `PASS: 229 assertions for N=2,...,7; seven-point orthogonal 2-design split.` Its floating-point tolerance is \(10^{-12}\), so the exact proof above, rather than the checker, supplies certification of the infinite quantifiers.

## Relationship to prior work

Brinkley, Fickus, Jasper and Mixon introduce SUNTFs, their connection to equichordal filter banks, and the general stratified Gerzon upper bound in *Incoherent filter banks*, arXiv:2610.05302, initially public on 2026-10-04. Their Example 3.3 constructs the real and complex two-layer five-vector case, Theorem 4.1 establishes the general rank bound, and their Sections 4.1--4.2 give harmonic difference-family and Gauss-sum constructions with more layers for seven elements. The rank bound, Bloch representation and the five-vector instance are not claimed as new here. The specific six- and seven-vector two-layer complex constructions and maximal-size complementary-design rigidity are the additional claims. Their source was inspected through Sections 3 and 4, including Examples 3.3/4.7 and Theorems 4.1/4.8/4.10, rather than inferred from title matching.

The earlier survey *Certifying the novelty of equichordal tight fusion frames*, arXiv:2103.03192 (2021), discusses Naimark/spatial complement relations and warns that parameter matching or absence from tables cannot certify novelty. Its abstract was available but not its whole text in the material inspected. Published mathematical records on dihedral operator-frame conditioning, harmonic fusion-frame block rank, and spherical-design sampling address other Gram and geometry constraints, so their statements do not imply the two-layer SUNTF identities above.

## Limitations

This is a two-layer existence and maximal-size structure theorem specifically for complex dimension two. It does not classify all seven-point solutions up to rotations, does not show that every maximal design has the latitude form (2), and does not establish real two-dimensional seven-point feasibility. It does not claim novelty for arbitrary equichordal tight fusion frames with the same dimensions without the commuting layered construction. An inaccessible full thesis (*Grassmannian Codes from Stratified Frames*, 2025) and older fusion-frame design literature remain bibliographic priority risks; the conclusion is original relative to checked accessible statements, not a claim of exhaustive worldwide priority. Independent mathematical audit has not been performed.

## References

1. W. J. Brinkley, M. Fickus, J. Jasper and D. G. Mixon, *Incoherent filter banks*, arXiv:2610.05302 (first posted 2026-10-04), https://arxiv.org/abs/2610.05302 .
2. M. Fickus, B. R. Mayo and C. E. Watson, *Certifying the novelty of equichordal tight fusion frames*, arXiv:2103.03192 (2021), https://arxiv.org/abs/2103.03192 .
3. W. J. Brinkley, *Grassmannian Codes from Stratified Frames*, thesis (2025), https://scholar.afit.edu/etd/8306/ (abstract only accessible in this check).
