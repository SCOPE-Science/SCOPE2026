# Sharp invariant-ellipse area in the elliptic three-cycle window of a nonmonotonic toral shear

## Finding
For the toral map \(H_\eta\) below, every \(\eta\) satisfying
\[
\frac13<\eta<\eta_*:=\frac{9-\sqrt{33}}8
\]
admits **two distinct elliptic primitive three-cycles** and six pairwise interior-disjoint explicit invariant elliptic disks. Their **combined area** is exactly
\[
\boxed{\mathcal A_{\rm six}(\eta)=\frac{\pi\eta(1-\eta)\sqrt{(3\eta-1)(4\eta^2-9\eta+3)}}{\sqrt3(3\eta^2-7\eta+3)}}.
\]
This is a rigorously certified area **contained in** the islands, not a computation of the whole island boundaries. The formula vanishes as a square root at either endpoint of the open parameter window.

## Assumptions and scope
Work on \(\mathbb T^2=\mathbb R^2/\mathbb Z^2\) with normalized Lebesgue area and \(0<\eta<1/2\). Define
\[
H_\eta(x,y)=\bigl(x+f_\eta(y),\,y+x+f_\eta(y)\bigr)\bmod1,
\qquad
f_\eta(y)=\begin{cases}y/(1-\eta),&0\le y\le1-\eta,\\ (1-y)/\eta,&1-\eta\le y\le1.\end{cases}
\]
The function extends periodically to the real line, so this defines a continuous, invertible, area-preserving toral map. Call \(L\) the lower-shear branch \(0<y<1-\eta\), and \(R\) the upper-shear branch \(1-\eta<y<1\). The two primitive cycles, each with branch word \(RLR\), are
\[
\begin{aligned}
C_+ :&(0,1-\eta/3)\to(1/3,(1-\eta)/3)\to(2/3,1-\eta/3)\to(0,1-\eta/3),\\
C_- :&(0,1-2\eta/3)\to(2/3,2(1-\eta)/3)\to(1/3,1-2\eta/3)\to(0,1-2\eta/3).
\end{aligned}
\]
For the upper/lower-branch derivatives use
\[
R=\begin{pmatrix}1&-1/\eta\\1&1-1/\eta\end{pmatrix},\quad
L=\begin{pmatrix}1&1/(1-\eta)\\1&1+1/(1-\eta)\end{pmatrix},\quad M=RLR.
\]
Define the symmetric matrix
\[
Q=\begin{pmatrix}-M_{21}&(M_{11}-M_{22})/2\\(M_{11}-M_{22})/2&M_{12}\end{pmatrix}
\]
and the exact radius
\[
r_\eta^2=\frac{(1-\eta)(3\eta-1)(4\eta^2-9\eta+3)}{12\eta(3\eta^2-7\eta+3)}.
\]
The two centered ellipses are the embedded toral disks
\[
E_\pm=\{z_\pm+w:\ w^TQw\le r_\eta^2\},
\quad z_+=(0,1-\eta/3),\quad z_-=(0,1-2\eta/3).
\]
These ellipses are largest in the precise sense of **centered \(Q\)-ellipses confined to their respective closed three-step affine itinerary cells**. No maximality is claimed over arbitrary invariant sets or arbitrary ellipse shapes.

## Proof
**1. Elliptic return matrix and invariant metric.** Direct multiplication gives
\[
M=\begin{pmatrix}
(\eta-3)/\eta&3(1-\eta)/\eta^2\\
(3\eta^2-7\eta+3)/(\eta(\eta-1))&(\eta^2-6\eta+3)/\eta^2
\end{pmatrix}.
\]
Its determinant equals one, its trace equals \((2\eta^2-9\eta+3)/\eta^2\), and in the stipulated window the trace lies strictly between \(-2\) and \(2\). The displayed \(Q\) satisfies \(M^TQM=Q\), with positive \(Q_{11}\) and
\[
\det Q=\frac{3(3\eta-1)(4\eta^2-9\eta+3)}{4\eta^4}>0.
\]
Hence it is positive definite, and \(H_\eta^3\), on either prescribed itinerary cell, acts as the affine \(Q\)-rotation about its cycle point.

**2. Sharp confinement radius.** The initial vertical displacement is \(b_0w\), with \(b_0=(0,1)\); the second and third vertical displacements are \(b_1w\), \(b_2w\), with \(b_1=b_0R\), \(b_2=b_0LR\). Their squared dual \(Q\)-norms are
\[
\begin{aligned}
v_R&=b_0Q^{-1}b_0^T=b_2Q^{-1}b_2^T
=\frac{4\eta^3(3\eta^2-7\eta+3)}{3(1-\eta)(3\eta-1)(4\eta^2-9\eta+3)},\\
v_L&=b_1Q^{-1}b_1^T=\frac{4\eta^2(1-\eta)}{3(4\eta^2-9\eta+3)}.
\end{aligned}
\]
Cauchy–Schwarz in the \(Q\)-inner product gives precisely \(\max_{w^TQw\le r^2}|b_jw|=r\sqrt{v_j}\). For either cycle, the smallest permitted vertical distance to its upper-strip boundary in phases 0 and 2 is \(\eta/3\), and the smallest permitted distance in its lower-strip phase is \((1-\eta)/3\). Consequently the **largest permissible squared radius** is
\[
\min\left\{\frac{\eta^2}{9v_R},\frac{(1-\eta)^2}{9v_L}\right\}.
\]
The first term is smaller: their ratio is \(\eta(3\eta-1)/(3\eta^2-7\eta+3)<1\), because \(3\eta^2-7\eta+3-\eta(3\eta-1)=3(1-2\eta)>0\). Substitution yields the claimed \(r_\eta^2\). At larger centered radius, a genuine boundary of the prescribed itinerary strip is crossed, proving sharpness **within this defined class**. The ellipses remain embedded on the torus: the squared maximal horizontal semiaxis equals \(\eta(1-\eta)^2/[3(3\eta^2-7\eta+3)]<1/4\), while all vertical strips lie within \([0,1]\).

**3. Invariance and distinctness.** On the interior of either ellipse all three branch prescriptions hold, so its third return is exactly \(z_\pm+Mw\) modulo integers. Since \(M^TQM=Q\), its third return maps the ellipse onto itself. At boundary tangencies the identity extends by continuity and invertibility. The images \(E_\pm,H_\eta(E_\pm),H_\eta^2(E_\pm)\) are ellipses, mapped cyclically. Their interiors are pairwise disjoint: phase-1 interiors lie in the lower strip while phases 0 and 2 lie in the upper strip; the upper-strip phases are distinguished by their *next* branch symbols, \(RL\) versus \(RR\). At any fixed phase, the two cycles' vertical centers differ by one-third of the corresponding strip width, and their vertical projection radii are at most one-third of that width; hence the two ellipses at the same phase have disjoint interiors (indeed their projections merely meet). Thus there are six distinct disks. Because both shear branches have determinant one, every image has the same area.

**4. Exact area.** Each ellipse has Euclidean area \(\pi r_\eta^2/\sqrt{\det Q}\). Simplifying gives
\[
A(\eta)=\frac{\pi\eta(1-\eta)\sqrt{(3\eta-1)(4\eta^2-9\eta+3)}}{6\sqrt3(3\eta^2-7\eta+3)}.
\]
Disjointness yields the stated total area \(6A(\eta)\). Because the product \((3\eta-1)(4\eta^2-9\eta+3)\) has a simple zero at each endpoint and the remaining factors stay finite and positive, the area vanishes with square-root order at both endpoints.

## Verification
The accompanying standalone Python checker uses symbolic SymPy algebra to verify \(M^TQM=Q\), the determinant, both dual norms, and the radius identity. Numerical boundary sampling at five distinct parameters (1,000 boundary points per ellipse) verifies the full \(RLR\) itinerary and the affine third-return matrix modulo \(\mathbb Z^2\). The boundary sampling does not prove the infinite statement: the sharp bound follows from dual-norm Cauchy–Schwarz and the exact matrix identities.

## Relationship to prior work
J. Myers Hill, R. Sturman and M. C. T. Wilson introduced this triangular-shear family and studied measure-preserving mixing windows and the obstruction caused by elliptic periodic orbits. Their original preprint was publicly posted on 2021-12-14. The present result quantifies a specific six-disk **guaranteed invariant area** and its sharp maximal centered-ellipse construction throughout the elliptic period-three window. This is not a new discovery of the original periodic orbit or a classification of the complete chaotic sea.

## Limitations
Only the stated open parameter window and the two specified period-three itineraries are covered. The computed ellipses need not fill the complete islands. In particular the formula is a lower bound on invariant-island area, not an exact total-island-area formula or an assertion about mixing in the complement. The maximality refers only to centered ellipses in the invariant metric whose three iterates respect the same affine branch cell; other shapes or sets could be larger. Source searches cannot exclude unpublished or unindexed equivalent statements, and there has been no independent audit.

## References
1. J. Myers Hill, R. Sturman, M. C. T. Wilson, *A Continuous Family of Non-Monotonic Toral Mixing Maps*, arXiv:2112.07346, first posted 2021-12-14; journal article *A Family of Non-Monotonic Toral Mixing Maps*, *Journal of Nonlinear Science* 32 (2022), article 31, DOI 10.1007/s00332-022-09790-0.
