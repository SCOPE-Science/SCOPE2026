# Exact one-site eigenvalue threshold for the non-self-adjoint discrete Dirac operator
## Finding
Consider the one-dimensional free discrete Dirac operator of Cassano, Ibrogimov, Krejčiřík and Štampach with mass \(m\ge 0\), and let \(\lambda\in\rho(D_0)\). Let \(k\) be the unique parameter with \(0<|k|<1\) satisfying
\[
\lambda^2=m^2+2-k-k^{-1},
\]
and let \(T_0(k)\) be the diagonal \(2\times2\) block of the free resolvent \((D_0-\lambda)^{-1}\). Among all block potentials supported at a single lattice site, the exact least \(\ell^1\)-norm needed to make \(\lambda\) an eigenvalue is
\[
Q_{\min}(\lambda)=\frac{1}{\|T_0(k)\|}.
\]
Equivalently, for every \(Q>0\), there exists a single-site potential \(V\) with \(\|V\|_1=Q\) and \(\lambda\in\sigma_{\mathrm p}(D_0+V)\) if and only if
\[
Q\,\|T_0(k)\|\ge 1.
\]
At the threshold \(Q=Q_{\min}(\lambda)\), a rank-one block potential attains equality.

Consequently, on the improved \(\ell^1\) spectral-enclosure boundary
\[
\Gamma_Q=\{\lambda\in\rho(D_0):Q\max(\|T_0(k)\|,\|T_1(k)\|)=1\},
\]
a boundary point is attainable by a single-site potential of norm \(Q\) if and only if
\[
\|T_0(k)\|\ge \|T_1(k)\|.
\]
Thus the diagonal-dominance region used in the source paper is exactly, not merely sufficiently, the part of the improved boundary that can be saturated by one-site witnesses.

## Assumptions and scope
The operator is the block-Jacobi realization of the free discrete Dirac operator in arXiv:1910.10710v1. A single-site potential means \(V=\bigoplus_n v_n\) with \(v_n=0\) except at one lattice site; by translation invariance that site can be taken to be \(0\). The block norm is the operator norm on \(\mathbb C^2\), hence \(\|V\|_1=\|v_0\|\). The spectral parameter is restricted to \(\lambda\in\rho(D_0)\); embedded spectral points are not claimed.

The resolvent block used below is
\[
T_0(k)=\frac{1}{k^{-1}-k}
\begin{pmatrix}
\lambda-m&1-k\\
1-k&\lambda+m
\end{pmatrix}.
\]
The neighboring block \(T_1(k)\) is the one defined in Eq. (1.14) of the source paper.

## Proof
Let \(R_0(\lambda)=(D_0-\lambda)^{-1}\). Because the free resolvent is translation invariant, the \((0,0)\) block of \(R_0(\lambda)\) is exactly \(T_0(k)\).

Suppose first that a single-site potential \(V\), supported at \(0\), has \(\|V\|_1=\|v_0\|=Q\) and that \(\lambda\) is an eigenvalue. Let \(\psi\ne0\) satisfy \((D_0+V)\psi=\lambda\psi\), and put \(\phi=V\psi\). Since \(\lambda\in\rho(D_0)\), one cannot have \(\phi=0\); otherwise \(D_0\psi=\lambda\psi\). Hence \(\phi\) is a nonzero vector supported at site \(0\), and
\[
\psi=-R_0(\lambda)\phi.
\]
Writing \(x=\phi_0\ne0\), the site-zero component of \(\phi=V\psi\) gives
\[
(I+v_0T_0(k))x=0.
\]
Therefore
\[
\|x\|=\|v_0T_0(k)x\|\le Q\,\|T_0(k)\|\,\|x\|,
\]
so every one-site eigenvalue witness necessarily satisfies \(Q\|T_0(k)\|\ge1\).

For the converse, set \(\sigma=\|T_0(k)\|\), and assume \(Q\ge1/\sigma\). Choose a unit right singular vector \(x\) of \(T_0(k)\) for its largest singular value, so that \(y=T_0(k)x\) has \(\|y\|=\sigma\). Put \(e_1=y/\sigma\) and choose a unit vector \(e_2\perp e_1\). Put \(f_1=-x\) and choose a unit vector \(f_2\perp f_1\). Define the site block by
\[
v_0 e_1=\sigma^{-1}f_1,
\qquad
v_0 e_2=Qf_2.
\]
Because \((e_1,e_2)\) and \((f_1,f_2)\) are orthonormal bases, \(\|v_0\|=\max(\sigma^{-1},Q)=Q\). Moreover,
\[
v_0T_0(k)x=v_0y=-x,
\]
so \((I+v_0T_0(k))x=0\). Let \(\phi\) be supported at site \(0\) with \(\phi_0=x\), and define \(\psi=-R_0(\lambda)\phi\). Then \(\psi\in\ell^2(\mathbb Z;\mathbb C^2)\), \(\psi\ne0\), and the last displayed identity gives \(V\psi=\phi\). Consequently
\[
(D_0+V-\lambda)\psi=(D_0-\lambda)\psi+V\psi=-\phi+\phi=0.
\]
Thus \(\lambda\) is an eigenvalue. At equality \(Q=1/\sigma\), one may instead take the rank-one map
\[
v_0z=-\frac{1}{\sigma}\,x\langle e_1,z\rangle,
\]
which has norm \(1/\sigma\) and still sends \(y\) to \(-x\).

Finally, on \(\Gamma_Q\) one has
\[
Q\max(\|T_0(k)\|,\|T_1(k)\|)=1.
\]
The exact one-site criterion becomes \(Q\|T_0(k)\|\ge1\). Since \(Q\|T_0(k)\|\le1\) on \(\Gamma_Q\), this is possible exactly when \(\|T_0(k)\|=\max(\|T_0(k)\|,\|T_1(k)\|)\), equivalently \(\|T_0(k)\|\ge\|T_1(k)\|\). This is precisely the diagonal-dominance set \(\mathcal D\) in the source paper.

## Verification
The proof uses only the published free-resolvent block formula and finite-dimensional singular-value geometry. The bundled script `verify.py` reconstructs \(T_0(k)\) for several complex off-spectrum parameters, computes a maximizing singular vector, builds a potential of prescribed norm above threshold, checks \(v_0T_0(k)x=-x\), verifies singularity of \(I+v_0T_0(k)\), and finds a sample point where \(\|T_1(k)\|>\|T_0(k)\|\) so that the improved-boundary normalization forces \(Q\|T_0(k)\|<1\). These finite checks are corroborative only; the theorem is proved analytically above.

## Relationship to prior work
Cassano, Ibrogimov, Krejčiřík and Štampach derive the explicit block resolvent and the improved \(\ell^1\) enclosure with boundary controlled by \(\max(\|T_0(k)\|,\|T_1(k)\|)\). Their Theorem 5 proves that every boundary point in the diagonal-dominance region \(\mathcal D\) is attainable by a specially chosen one-site potential. The paper explicitly says that full optimality of the improved enclosure is not proved and explains that the point-potential construction works in \(\mathcal D\). The result here identifies the exact capability of the entire class of one-site block potentials: outside \(\mathcal D\), no one-site potential of the boundary norm can work.

The scalar discrete Schrödinger analogue of Ibrogimov and Štampach has a diagonally dominant scalar free resolvent and uses a delta potential to saturate its full \(\ell^1\) boundary. That argument motivates point-supported witnesses but does not imply the matrix-valued discrete Dirac threshold, where the competition between \(T_0(k)\) and \(T_1(k)\) is the central obstruction.

## Limitations
The theorem does not settle whether boundary points outside \(\mathcal D\) are attainable by multi-site potentials; it only proves that one-site potentials cannot attain them at the same norm. It does not address spectral parameters embedded in the essential spectrum, threshold points, potentials constrained to be Hermitian, or minimization over a fixed scalar or diagonal subclass of \(2\times2\) blocks.

## References
1. B. Cassano, O. O. Ibrogimov, D. Krejčiřík, F. Štampach, *Location of eigenvalues of non-self-adjoint discrete Dirac operators*, arXiv:1910.10710v1; Annales Henri Poincaré 21 (2020), 2193–2217, DOI 10.1007/s00023-020-00916-2.
2. O. O. Ibrogimov, F. Štampach, *Spectral enclosures for non-self-adjoint discrete Schrödinger operators*, arXiv:1903.08620v1; Integral Equations and Operator Theory 91 (2019), 53.
