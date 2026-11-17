# Exact \(q\)-numerical annuli and two threshold transitions for planar antiisometries

## Finding
Let \(H=\mathbb C^2\) with its standard complex Hilbert structure, and let \(A:H\to H\) be a nonzero conjugate-linear operator satisfying \(\|Ax\|=R\|x\|\) for all \(x\in H\), where \(R>0\). Define its ordinary numerical radius and complementary skew radius by
\[
a:=\max_{\|x\|=1}|\langle Ax,x\rangle|,\qquad b:=\sqrt{R^2-a^2}.
\]
For every \(q\in\mathbb C\) with \(|q|\le1\), set \(r=|q|\), \(k=\sqrt{1-r^2}\), and
\[
W_q(A):=\{\langle Ax,y\rangle:\|x\|=\|y\|=1,\ \langle x,y\rangle=q\}.
\]
Then the **entire** constrained numerical range is the closed circular annulus
\[
\boxed{W_q(A)=\{z\in\mathbb C:\ R_-(r)\le|z|\le R_+(r)\}},
\]
with exact radii
\[
\boxed{R_-(r)=\max\{0,\ b\sqrt{1-r^2}-ar\}},
\]
and
\[
\boxed{R_+(r)=\begin{cases}R,&0\le r\le a/R,\\ a r+b\sqrt{1-r^2},&a/R\le r\le1.\end{cases}}
\]
Thus the hole closes exactly when \(r\ge b/R\), whereas the outer radius stays equal to the operator norm exactly when \(r\le a/R\). Both thresholds are intrinsic: \(a\) is the ordinary numerical radius, and \(b=(R^2-a^2)^{1/2}\). Degenerate annuli (disks, circles or the singleton \(\{0\}\)) are included.

## Assumptions and scope
The inner product is linear in its first variable, so \(\langle u,v\rangle=\sum_{j=1}^2u_j\overline{v_j}\). The underlying Hilbert space is complex and exactly two-dimensional; \(A\) is conjugate-linear and a positive multiple of an antiunitary isometry. The result is uniform for every complex \(q\) in the closed unit disk, including \(q=0\), \(|q|=1\), \(a=0\), and \(b=0\). The zero operator has \(W_q(0)=\{0\}\) separately. No result is asserted for nonisometric antilinear operators or dimension other than two.

## Proof
**1. The ordinary numerical radius spans an interval.** Fix coordinatewise conjugation \(C\), and write \(A=UC\) for a complex matrix \(U\) with \(U^*U=R^2 I\). Decompose \(U=S+K\), where \(S=(U+U^{\mathsf T})/2\) is complex symmetric and \(K=(U-U^{\mathsf T})/2\) is skew-symmetric. Because both \(U\) and \(U^{\mathsf T}\) are scaled unitaries,
\[
S^*S+K^*K=R^2I.
\]
Every skew-symmetric complex \(2\times2\) matrix is \(K=\gamma\begin{pmatrix}0&1\\-1&0\end{pmatrix}\), so \(K^*K=b_0^2I\) with \(b_0=|\gamma|\); hence \(S^*S=(R^2-b_0^2)I\). Write \(a_0=\sqrt{R^2-b_0^2}\). If \(a_0>0\), the Takagi factorization of the symmetric scaled-unitary matrix gives a unitary \(V\) with \(V^*S\overline V=a_0I\). In this orthonormal basis, the skew component contributes nothing to \(\langle Ax,x\rangle\), and
\[
|\langle Ax,x\rangle|=a_0|x_1^2+x_2^2|.
\]
For unit vectors, \(x=(\cos t,i\sin t)\), \(0\le t\le\pi/4\), makes the last modulus run continuously through \([0,a_0]\), while the Cauchy–Schwarz inequality bounds it above by \(a_0\). If \(a_0=0\), it vanishes identically. Consequently \(a=a_0\), \(b=b_0\), and, crucially, every \(s\in[0,a]\) is realized as \(s=|\langle Ax,x\rangle|\) for a unit vector \(x\).

**2. The exact one-parameter reduction.** Put \(r=|q|\) and \(k=\sqrt{1-r^2}\). Every admissible \(y\) can be written as \(y=\overline qx+kv\), where \(v\) is a unit vector perpendicular to \(x\) (when \(k=0\), choose any such \(v\)). For each fixed \(x\), the phase of \(v\) varies freely and
\[
\langle Ax,y\rangle=q\langle Ax,x\rangle+k\langle Ax,v\rangle.
\]
Since \((x,v)\) is an orthonormal basis and \(\|Ax\|=R\), the second summand has modulus \(k\sqrt{R^2-s^2}\) with \(s=|\langle Ax,x\rangle|\). Thus the possible moduli for this \(s\) form precisely
\[
\big[\,|rs-k\sqrt{R^2-s^2}|,\quad rs+k\sqrt{R^2-s^2}\,\big].
\]
The full modulus set is a closed interval because it is a continuous image of the connected parameter space \([0,a]\times\mathbb T\). Simultaneously multiplying \(x\) and \(y\) by a common unit scalar rotates \(\langle Ax,y\rangle\) by its inverse square without changing the overlap; hence the set is circularly symmetric. The radial extrema therefore determine the entire closed annulus.

**3. The inner radius.** The function \(g(s)=rs-k\sqrt{R^2-s^2}\) is nondecreasing on \([0,a]\), with \(g(0)=-kR\) and \(g(a)=r a-k b\). Therefore the minimum of \(|g(s)|\) is \(0\) if \(r a\ge k b\), and \(k b-r a\) otherwise. Since \(r^2+k^2=1\) and \(a^2+b^2=R^2\), the inequality \(r a\ge k b\) is equivalent to \(r\ge b/R\), including the limiting cases. This yields \(R_-(r)=\max\{0,k b-r a\}\).

**4. The outer radius.** By Cauchy–Schwarz,
\[
f(s):=rs+k\sqrt{R^2-s^2}\le R.
\]
Equality is attained at \(s=rR\) exactly when \(rR\le a\). Otherwise \(f\) increases on \([0,a]\) and its maximum is \(f(a)=r a+k b\). This proves the outer-radius formula. All endpoints occur by compactness. The conclusions about the two thresholds follow immediately.

## Verification
A standalone standard-library Python diagnostic `checker.py` numerically checks the canonical family \(A(z_1,z_2)=(a\overline z_1+b\overline z_2,-b\overline z_1+a\overline z_2)\) at seven parameter pairs and nine overlap moduli. It checks the orthonormal decomposition, the antiisometry norm identity, the two radial bounds, and a dense angular approximation to the extrema. Run `python3 checker.py`; the expected line is `TWO_DIMENSIONAL_ANTILINEAR_Q_RANGE_FINITE_OK 475146`. Numerical samples corroborate but do not establish the infinite family of claims; the analytic proof above is decisive.

## Relationship to prior work
Majumdar and Müller (2026, Section 6) establish the general centered-disk result for complex dimension at least three, demonstrate a skew antiunitary in dimension two whose \(q\)-range omits zero for \(|q|<1\), and identify the annular shape in dimension two. The present calculation instead determines both radii of that annulus for **every** planar antiisometry and describes two sharp, potentially differently ordered thresholds. Kołaczek and Müller (2024) prove the disk structure of the **ordinary** numerical range of antilinear operators and the symmetric/skew decomposition; those results explain the endpoint \(|q|=1\) but do not state the constrained-radius formulas. The classical \(q\)-numerical-range theory for complex-linear operators concerns a different operator class.

## Limitations
The formula does not cover arbitrary antilinear matrices, which need not have constant \(\|Ax\|\). It does not claim a new definition of \(q\)-numerical range, a new Takagi factorization, or any independently certified publication priority. A general older theorem in a different representation could imply the specialized radius formulas; this remains a literature risk. The finite diagnostic is not a proof.

## References
1. A. Majumdar and V. Müller, *Some Generalized Numerical Ranges of Real-linear Operators on Hilbert Spaces*, arXiv:2610.16823 (first publicly submitted 2026-10-12), Section 6. https://arxiv.org/abs/2610.16823
2. D. Kołaczek and V. Müller, *Numerical Ranges of Antilinear Operators*, Integral Equations and Operator Theory 96 (2024), article 17, DOI 10.1007/s00020-024-02768-5. https://link.springer.com/article/10.1007/s00020-024-02768-5
3. D. Kołaczek and V. Müller, *Real linear operators and numerical ranges*, arXiv:2508.04347 (2025). https://arxiv.org/abs/2508.04347
4. B. Jia and T. Liu, *A characterization of numerical ranges for antilinear operators*, Canadian Mathematical Bulletin 69 (2026), 372–387, DOI 10.4153/S000843952500044X (abstract consulted). https://doi.org/10.4153/S000843952500044X
