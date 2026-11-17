# Exact open and closed \(q\)-numerical disks of infinite-dimensional antiunitaries

## Finding
Let \(H\) be a complex Hilbert space of dimension at least three and let \(A:H\to H\) be antiunitary: it is conjugate-linear, surjective, and norm-preserving. Take the inner product to be linear in its first variable. For every \(q\in\mathbb C\), \(|q|\le1\), put
\[
 W_q(A)=\{\langle Ax,y\rangle:\|x\|=\|y\|=1,\ \langle x,y\rangle=q\},\quad r=|q|.
\]
Set \(B=A^2\), a complex-linear unitary, and
\[
 \rho=\tfrac12\|I+B\|=\max_{z\in\sigma(B)}\tfrac12|1+z|\ \in[0,1],
 \qquad \Gamma_\rho=\{z\in\sigma(B):|1+z|=2\rho\}.
\]
Then \(W_q(A)\) is exactly the disk centered at zero with radius
\[
 R_\rho(r)=\begin{cases}
 1,&0\le r\le\rho,\\
 r\rho+\sqrt{1-r^2}\sqrt{1-\rho^2},&\rho<r\le1.
 \end{cases}
\]
**The boundary circle is absent if and only if** \(r\ge\rho\) and the spectral projection \(E_B(\Gamma_\rho)\) vanishes. Otherwise the boundary circle is present. The zero-radius disk \(\{0\}\), when it occurs, is understood to be closed.

The criterion is effective even when \(\Gamma_\rho\) consists of points in the continuous spectrum: a point of that set counts for boundary attainment exactly when it has a nonzero spectral eigenspace. For any \(\rho_0\in(0,1)\), there exist antiunitaries with the *same* radius function \(R_{\rho_0}\) but opposite open-versus-closed behavior for every \(r\ge\rho_0\). Thus the scalar radius does not determine boundary attainment.

## Assumptions and scope
The antiunitary is defined on an arbitrary complex Hilbert space of dimension at least three; the explicit nonattainment example is separable and infinite-dimensional. The restriction to antiunitaries, rather than all bounded antilinear maps, is essential to the unitary spectral criterion. The result includes \(q=0\), \(|q|=1\), \(\rho=0\), and \(\rho=1\), without assuming that \(A\) or \(A^2\) has eigenvectors.

## Proof
**Step 1: the antiunitary quadratic radius.** Let \(A^\#\) denote the antilinear adjoint. Since \(A\) is antiunitary, \(A^\#=A^{-1}\). Define \(T=(A+A^{-1})/2\). The antilinear map \(T\) is self-adjoint in the antilinear sense, and its symmetric quadratic form satisfies
\[
 \langle Tx,x\rangle=\langle Ax,x\rangle,\qquad
 \langle Tx,y\rangle=\langle Ty,x\rangle.
\]
Set \(\omega=\sup_{\|x\|=1}|\langle Ax,x\rangle|\). For any \(x,y\), polarization of the symmetric bilinear form (conjugate-bilinear with the stated convention) gives
\[
 4\langle Tx,y\rangle
 =\langle T(x+y),x+y\rangle-\langle T(x-y),x-y\rangle.
\]
For unit \(x,y\), its absolute value is at most \(\omega(\|x+y\|^2+\|x-y\|^2)=4\omega\). Hence \(\|T\|\le\omega\), while \(\omega\le\|T\|\) is immediate. Moreover
\[
 T^2=\tfrac14(2I+B+B^*)=\tfrac14(I+B)^*(I+B),
\]
so \(\omega=\|T\|=\rho\). Because a nontrivial complex homogeneous quadratic form in two variables has a nonzero isotropic vector, some unit \(x\) satisfies \(\langle Ax,x\rangle=0\). Continuity on the connected unit sphere now shows that the attainable values of \(a(x)=|\langle Ax,x\rangle|\) include every \(a\in[0,\rho)\), and include \(\rho\) precisely if the quadratic radius is attained.

**Step 2: optimize a constrained pair.** Given \(\|x\|=\|y\|=1\) and \(\langle x,y\rangle=q\), write
\[
 y=\overline q\,x+\sqrt{1-r^2}\,u,
 \qquad u\perp x,\quad\|u\|=1
\]
when \(r<1\), with the evident convention for \(r=1\). Since \(\|Ax\|=1\) and \(a=|\langle Ax,x\rangle|\), Cauchy–Schwarz yields
\[
 |\langle Ax,y\rangle|\le f_r(a):=r a+\sqrt{1-r^2}\sqrt{1-a^2}.
\]
For every chosen \(x\), equality is realized by taking \(u\) along the component of \(Ax\) orthogonal to \(x\), with phase chosen to align the two scalar summands; if that component vanishes, any orthogonal \(u\) does. The function \(f_r\) increases on \([0,r]\) and decreases on \([r,1]\), so the supremum over \(a\in[0,\rho]\) equals \(f_r(\min\{r,\rho\})=R_\rho(r)\). If \(r<\rho\), the maximizing value \(a=r\) is strictly below the supremum and therefore occurs. If \(r\ge\rho\), the maximizing value is \(a=\rho\), so the outer circle occurs exactly when \(\omega\) is attained.

**Step 3: the entire disk.** The constrained pair space is connected: for \(r<1\), it is parametrized by orthonormal pairs \((x,u)\) through the preceding formula, and the complex Stiefel space of orthonormal two-frames is path connected; for \(r=1\), it is parametrized by the unit sphere. The image \(W_q(A)\) is therefore connected. Simultaneously rotating \(x,y\) by a common unimodular scalar rotates \(\langle Ax,y\rangle\) by its inverse square, hence the image is circularly symmetric. Finally, take a unit isotropic \(x\) and, when \(r<1\), a unit vector \(u\perp\{x,Ax\}\), possible in dimension at least three; this gives \(0\in W_q(A)\). Connectedness and circular symmetry now show that the image is the full centered disk, open or closed according to Step 2, including the degenerate singleton case.

**Step 4: spectral test for attainment.** Since \(T^2\) is positive and equals \((I+B)^*(I+B)/4\), the top spectral projection of \(T^2\) is exactly \(E_B(\Gamma_\rho)\). If \(\rho>0\) and \(|\langle Tx,x\rangle|=\rho\) for unit \(x\), equality in Cauchy–Schwarz implies \(\|Tx\|=\rho\), so \(x\) belongs to the top eigenspace of \(T^2\). Conversely, if \(T^2\) has a top eigenvector, its top eigenspace is invariant under \(T\); there \(T/\rho\) is an antilinear isometric involution. Every nonzero complex Hilbert space with such an involution has a fixed unit vector \(v\), hence \(Tv=\rho v\) and \(|\langle Tv,v\rangle|=\rho\). When \(\rho=0\), \(T=0\), all unit vectors attain the zero quadratic radius and \(E_B(\Gamma_0)=I\). Therefore attainment occurs exactly when \(E_B(\Gamma_\rho)\ne0\), proving the claimed open/closed rule.

**Step 5: genuine nonattainment and its contrast.** On \(H=\bigoplus_{j\ge1}\mathbb C^2\), let \(C\) be coordinatewise conjugation, and let \(Q_\theta\) be the real planar rotation by \(\theta\). Fix \(\rho_0\in(0,1)\), set \(c_j=\rho_0j/(j+1)\), and define \(A=\bigoplus_{j\ge1}Q_{\arccos c_j}C\). Then \(A^2=\bigoplus_{j\ge1}Q_{2\arccos c_j}\) and \(T=\bigoplus_{j\ge1}c_j C\). Thus \(\rho=\rho_0\) but the quadratic supremum is not attained by any unit vector: the peripheral spectral points are limits of block eigenvalues, not eigenvalues. Accordingly \(W_q(A)\) is closed for \(r<\rho_0\) and open for \(r\ge\rho_0\). In contrast, replacing every \(c_j\) by the constant \(\rho_0\) gives the same \(\rho\) and the same radius function, with a nonzero top eigenspace and closed disks for all \(q\).

## Verification
The standalone script `verification_example.py` performs 603 deterministic finite checks: the identities \(T=\rho I\) after conjugation on a rotation block, \(\|T\|=\|I+A^2\|/2\), exact constrained-pair norm attainment in two-dimensional blocks, and the convergence of truncated-block maxima. Executed using Python and NumPy, it returned `PASS: 603 deterministic algebraic and finite-block assertions`. These checks are supplementary, not proofs of spectral projection statements in infinite dimension. Steps 1–5 give the infinite-dimensional argument, including the nonattainment example.

## Relationship to prior work
Majumdar and Müller, *Some Generalized Numerical Ranges of Real-linear Operators on Hilbert Spaces* (first public version October 12, 2026), Section 6, prove in Theorem 6.6 that the \(q\)-numerical range of an antilinear operator in dimension at least three is a centered disk, and explicitly allow open or closed disks. That result is used only for context: the preceding proof reconstructs the disk geometry and supplies an **exact antiunitary radius and an if-and-only-if spectral boundary-attainment criterion**, not given there. Kołaczek and Müller, *Numerical Ranges of Antilinear Operators* (2024), describe ordinary antilinear numerical ranges, but do not give this constrained spectral criterion. The finite-dimensional planar problem has a different annular geometry, and compactness precludes the nonattainment phenomenon addressed here; no new two-dimensional classification is claimed. Classical \(q\)-numerical ranges of complex-linear normal operators concern a different class of mappings.

## Limitations
This is a theorem about **antiunitaries**, not arbitrary bounded antilinear operators. The explicit open-disk examples require infinite dimension and a missing peripheral eigenprojection. No claim is made that the general disk-shape theorem or the finite-dimensional outer-radius optimization is new. Some generic results on quadratic forms of antiunitaries and spectral norm attainment might imply the classification under different terminology; the originality assessment is not an independent publication-priority guarantee. Finite diagnostics cannot establish infinite-dimensional claims. No independent audit has been performed.

## References
1. A. Majumdar and V. Müller, *Some Generalized Numerical Ranges of Real-linear Operators on Hilbert Spaces*, arXiv:2610.16823, version 1, 2026-10-12, Section 6, especially Proposition 6.2 and Theorem 6.6. https://arxiv.org/abs/2610.16823
2. D. Kołaczek and V. Müller, *Numerical Ranges of Antilinear Operators*, Integral Equations and Operator Theory **96**, 17 (2024). https://doi.org/10.1007/s00020-024-02768-5
3. C. R. Chien and H. Nakazato, *The \(q\)-numerical ranges of normal operators*, Linear Algebra and its Applications (2005), complex-linear comparison, not an antiunitary boundary classification.
