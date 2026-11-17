# Two-center rigidity and a sharp three-center escape for the Veronese projector surface

## Finding
Let \(\operatorname{Sym}_0(3)\) be the five-dimensional Euclidean space of real symmetric trace-zero \(3\times3\) matrices with Frobenius inner product. For every unit vector \(u\in\mathbb R^3\), set
\[
p(u)=\frac{uu^{\mathsf T}-I/3}{\sqrt2},\qquad V=\{p(u):\|u\|_2=1\}.
\]
For integers \(k\ge1\), write \(r_k(V)\) for the infimum of radii of \(k\) congruent closed Euclidean balls, with unrestricted centers in \(\operatorname{Sym}_0(3)\), whose union contains \(V\). Then
\[
\boxed{r_1(V)=r_2(V)=\frac1{\sqrt3},\qquad r_3(V)\le\frac{\sqrt{21}}8<\frac1{\sqrt3}.}
\]
In particular, **three is the smallest number of Euclidean balls that can improve the single-ball covering radius of \(V\)**. Every two-ball covering attaining radius \(1/\sqrt3\) necessarily has at least one ball centered at the zero matrix. More quantitatively, for arbitrary two centers \(C_1,C_2\in\operatorname{Sym}_0(3)\),
\[
\sup_{u\in S^2}\min_{j=1,2}\|p(u)-C_j\|_F^2
\ \ge\ \frac13+\min\{\|C_1\|_F^2,\|C_2\|_F^2\}.
\]
A three-ball covering with radius \(\sqrt{21}/8\) is obtained from the three coplanar axes \(v_j=(\cos(j\pi/3),\sin(j\pi/3),0)\), \(j=0,1,2\), by taking centers \(C_j=-p(v_j)/8\). All three centers lie in the interior of \(\operatorname{conv}V\). The theorem **does not assert** that \(\sqrt{21}/8\) is the optimal three-ball radius.

## Assumptions and scope
All balls, norms, inner products and radii use the Frobenius Euclidean metric on \(\operatorname{Sym}_0(3)\), **not** a projective angular metric or the Euclidean metric on the original sphere. The underlying set is the two-dimensional embedded projective plane \(V\), **not** its five-dimensional convex hull. Ball centers are unrestricted, including centers outside \(\operatorname{conv}V\). Covering is literal containment in the union of the closed balls. A center at zero is allowed, and a ball may be redundant.

## Proof
**1. The common-zero lemma.** For any two real symmetric trace-zero \(3\times3\) matrices \(A,B\), there is a unit \(u\in\mathbb R^3\) such that \(u^{\mathsf T}Au=u^{\mathsf T}Bu=0\). If \(A=0\), a unit zero of the indefinite (or zero) form \(B\) suffices. Otherwise, the trace-zero form \(A\) is indefinite. By the intermediate value theorem it has a unit zero \(u_1\). Its symmetric compression to \(u_1^\perp\) has trace zero, so a \(45^\circ\) rotation of a planar orthonormal eigenbasis gives an orthonormal pair \(u_2,u_3\) satisfying \(u_i^{\mathsf T}Au_i=0\) for all three indices. Because \(\sum_i u_i^{\mathsf T}Bu_i=\operatorname{tr}B=0\), either some \(u_i\) is also a zero of \(B\), or \(B\) assumes both positive and negative values on the projective zero locus \(Z_A=\{[u]\in\mathbb{RP}^2:u^{\mathsf T}Au=0\}\). This locus is connected: by orthogonal diagonalization, a nondegenerate indefinite ternary form has a single projective conic, while a rank-two indefinite form has two intersecting projective lines. Continuity along \(Z_A\) produces a common zero. This establishes the lemma without assuming that \(A\) and \(B\) commute.

**2. The two-center obstruction and rigidity.** Direct multiplication gives \(\|p(u)\|_F^2=1/3\) and, for every trace-zero \(C\),
\[
\langle p(u),C\rangle_F=\frac{u^{\mathsf T}Cu}{\sqrt2}.
\]
Given centers \(C_1,C_2\), choose \(u\) from the lemma. Both squared distances are then exactly \(1/3+\|C_j\|_F^2\). Their minimum proves the displayed quantitative lower bound. The single ball centered at zero covers all of \(V\) with radius \(1/\sqrt3\), establishing both equal optimal radii. If a two-ball covering has this radius and neither center is zero, the lower bound is strictly larger than \(1/3\), a contradiction. Conversely, any center pair containing zero gives such a covering. Thus the entire two-center optimizer locus is characterized.

**3. An explicit strict three-center improvement.** Fix \(v_j=(\cos(j\pi/3),\sin(j\pi/3),0)\), \(j=0,1,2\). For every \(u\in S^2\),
\[
\min_{0\le j\le2}(u\cdot v_j)^2\le\frac14.
\]
Indeed, project \(u\) onto the plane of the axes and consider its planar angle. Among the three equally spaced unoriented axes, there is always one making an angle of at least \(\pi/3\) with the projected line, so its absolute cosine is at most \(1/2\); shortening the planar projection only decreases the squared product. Equality is attained when \(u\) is any one of the three planar axes.
For \(C_j=-p(v_j)/8\), use
\[
\langle p(u),p(v_j)\rangle_F=\tfrac12\bigl((u\cdot v_j)^2-\tfrac13\bigr)
\]
to calculate
\[
\min_j\|p(u)-C_j\|_F^2
=\frac13+\frac1{192}+\frac18\left(\min_j (u\cdot v_j)^2-\frac13\right)
\le\frac{21}{64}.
\]
Equality holds for the directions specified above, so this is the **exact radius of the exhibited three-center configuration**, not merely an upper estimate for it. Furthermore, \(C_j=(Q_j-I/3)/\sqrt2\) with \(Q_j=(3I-v_jv_j^{\mathsf T})/8\), whose eigenvalues are \(1/4,3/8,3/8\). Hence each \(C_j\) lies in the interior of the positive-semidefinite trace-one convex body \(\operatorname{conv}V\). Finally, \(21/64<1/3\), proving strict improvement and the exact critical ball count.

## Verification
The standalone `check.py` verifies the normalization and projector inner-product identities, explicitly attains the three-center covering radius at three contact directions, and checks the covering inequality for forty thousand sampled directions. It also numerically constructs common isotropic unit vectors for sixty random independent pairs of trace-zero symmetric matrices and verifies their residuals. A separate exact rational check establishes the squared-radius identity and its strict deficit. The script passed 80,183 finite assertions. The proof above, rather than any finite sampling, establishes the universal assertions.

Run `python check.py` with Python 3, NumPy, and SciPy. No external data files are required.

## Relationship to prior work
Arman, Bondarenko, Prymak and Radchenko (2026) introduced this diameter-one Veronese surface for their theorem that **six** Euclidean balls of radius \(1/2\) do **not** cover it. Their analysis treats the radius-\(1/2\) obstruction, a finite witness, and a Borsuk partition. It does not assert the present one-to-two covering plateau, classify all optimal two-center configurations, or provide the displayed three-center improvement.

The common-zero lemma is a dimension-three instance of the classical convexity of the joint numerical range of two real quadratic forms on the unit sphere (Brickman, 1961; see Martínez-Legaz, 2005). Accordingly, the two-center obstruction **is not claimed as a new general quadratic-form theorem**. The claimed new geometric result is the sharp transition in the ball count for strict improvement of this particular recently studied metric embedding, with the rigidity classification and explicit strict three-center witness.

The older work on spectral convexity, Grassmannian line packings and general equal-diameter coverings is acknowledged as context. The precise critical-count assertion has not been located in the inspected sources, but unindexed k-center or projective quantization literature could overlap.

## Limitations
No exact value or classification of optimal configurations for \(r_3(V)\) is established; only the rigorously attained upper bound for a specified three-center configuration is proved. No assertion is made about the radius profile of \(\operatorname{conv}V\), which need not be covered by the three balls even though \(V\) is. This does not improve the known six-ball obstruction at radius \(1/2\). Historical originality is provisional; the two-center lemma is classical in its general joint-numerical-range form, and an older explicit projective-plane k-center calculation could imply the complete threshold.

## References
1. A. Arman, A. Bondarenko, A. Prymak and D. Radchenko, *A diameter-one set in R^5 that cannot be covered by six diameter-one balls*, arXiv:2611.08198v1, first public November 5, 2026. https://arxiv.org/abs/2611.08198
2. L. Brickman, *On the field of values of a matrix*, Proc. Amer. Math. Soc. **12** (1961), 61–66. https://doi.org/10.1090/S0002-9939-1961-0122827-1
3. J. E. Martínez-Legaz, *On Brickman's Theorem*, J. Convex Anal. **12** (2005), 139–143. https://journalofconvexanalysis.com/articles/jca12009/
4. J. H. Conway, R. H. Hardin and N. J. A. Sloane, *Packing lines, planes, etc.: packings in Grassmannian spaces*, Experiment. Math. **5** (1996), 139–159. https://doi.org/10.1080/10586458.1996.10504585
