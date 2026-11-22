# Exact zero-field magnetization and Curie response of the prism-line Ising antiferromagnet

## Finding
For every integer \(n\ge3\), the zero-field, uniform antiferromagnetic Ising model on the line graph of the circular prism \(C_n\square K_2\) has a completely determined ground-state magnetization polynomial. With \(M\) denoting the sum of its \(3n\) Ising spins, define
\[
G_n(z)=\sum_{\sigma:\,H(\sigma)=E_0}z^{M(\sigma)},\qquad z>0.
\]
Write \(a=z+z^{-1}\) and
\[
T(z)=\begin{pmatrix}
z^{-1}&z&z&z^3+z\\
z^{-1}&0&z+z^{-1}&z\\
z^{-1}&z+z^{-1}&0&z\\
z^{-1}+z^{-3}&z^{-1}&z^{-1}&z
\end{pmatrix}.
\]
Then \(E_0=-2nJ\), \(G_n(z)=\operatorname{tr}T(z)^n\), and
\[
\det(\lambda I-T(z))=(\lambda+a)\bigl(\lambda^3-2a\lambda^2-3\lambda+z^3+z^{-3}\bigr).
\]
In particular, with \(L_{\pm}=(5\pm\sqrt{17})/2\),
\[
G_n(1)=L_+^n+L_-^n+(-1)^n+(-2)^n.
\]
For the physical zero-field susceptibility per spin, defined by \(\chi_n(T)=\frac{1}{3n}\frac{\partial}{\partial h}\langle M\rangle_{T,h}|_{h=0}\) and \(k_B=1\), the iterated, explicitly ordered limit is
\[
\boxed{\lim_{n\to\infty}\lim_{T\downarrow0}T\chi_n(T)=\frac{29}{24}-\frac{33\sqrt{17}}{136}\approx0.2078738800584598.}
\]
Thus the finite-cylinder zero-field Curie coefficient has a positive, nontrivial algebraic thermodynamic limit. The result is a longitudinal uniform-field response, not the transverse susceptibility of a quantum Ising model.

## Assumptions and scope
The base graph is the simple cubic prism with vertices \((u,i)\), where \(u\in\{0,1\}\) and \(i\in\mathbb Z/n\mathbb Z\), rail edges \((u,i)(u,i+1)\), and rungs \((0,i)(1,i)\). Its line graph has one spin \(\sigma_e\in\{-1,1\}\) per base edge, with each pair of base edges incident at a vertex coupled exactly once. The physical energy is \(H(\sigma)=J\sum_{\{e,f\}\in E(L(C_n\square K_2))}\sigma_e\sigma_f\), where \(J>0\); the field extension is \(H_h=H-hM\). No disorder, long-range bonds, field or quantum spin flips are assumed. The limit holds in the order \(T\downarrow0\) first at each finite \(n\), then \(n\to\infty\).

## Proof
Every base vertex gives a triangle of three interacting line-graph spins, and every line-graph interaction belongs to exactly one of the \(2n\) such triangles. The minimum sum of pair products on a triangle is \(-1\), achieved exactly when not all three spins coincide. Assigning all rungs \(-1\) and both rail families \(+1\) simultaneously attains the local minimum everywhere. Consequently \(E_0=-2nJ\), and the ground states are precisely the assignments satisfying the not-all-equal condition at both rail vertices of each column.

Index the four transfer states by the pair of incoming upper/lower rail spins \((-1,-1),(-1,1),(1,-1),(1,1)\). Given incoming pair \(u\), outgoing pair \(v\), and rung spin \(r\), the corresponding two triangle constraints are \(\neg(u_1=v_1=r)\) and \(\neg(u_2=v_2=r)\). Assign the weight \(z^{v_1+v_2+r}\) and sum over \(r\in\{-1,1\}\). This gives exactly the displayed \(T(z)\). Cyclic closure forces the trace, each base edge spin appears once in the exponent, and therefore \(G_n(z)=\operatorname{tr}T(z)^n\) for every \(n\ge3\).

Direct expansion of the \(4\times4\) determinant gives the displayed characteristic polynomial. At \(z=1\) its roots are \(-2,-1,L_+,L_-\), proving the exact finite-size count. The matrix \(T(1)\) is primitive (its square has strictly positive entries), and \(L_+\) is its unique eigenvalue of maximal modulus. Thus \(n^{-1}\log G_n(1)\to\log L_+\); the entropy per physical spin is \(\frac13\log L_+\).

At finite size, global spin reversal gives \(\langle M\rangle_0=0\). The fluctuation-dissipation identity implies
\[
\lim_{T\downarrow0}T\chi_n(T)=\frac{1}{3n}\left.\left(z\frac{d}{dz}\right)^2\log G_n(z)\right|_{z=1}.
\]
For \(z\) in a neighborhood of \(1\), Perron--Frobenius perturbation applies to the simple positive maximal eigenvalue \(\lambda(z)\) of \(T(z)\), so the subsequent \(n\to\infty\) limit equals \(\frac13\frac{d^2}{dt^2}\log\lambda(e^t)|_{t=0}\). Its cubic factor is \(f(\lambda,z)=\lambda^3-2(z+z^{-1})\lambda^2-3\lambda+z^3+z^{-3}\). At \((L_+,1)\), \(f_z=0\), \(f_{zz}=18-4L_+^2\), and \(f_\lambda=3L_+^2-8L_+-3\ne0\). Implicit differentiation gives \(\lambda'(1)=0\) and \(\lambda''(1)=(4L_+^2-18)/(3L_+^2-8L_+-3)\). Dividing by \(3L_+\) and simplifying proves the stated radical.

## Verification
Two reproducible programs are included. Run `python verify_transfer.py` (SymPy required) to check the determinant identity, zero-field eigenvalue factorization, derivative and radical coefficient, and exact trace counts through \(n=9\). Run `python verify_enumeration.py` (standard library only) to enumerate the physical Ising energies of *every* spin assignment on the original line graphs for \(n=3,4,5,6\), compare the minimum energies and exact magnetization distributions, and check the ground-state totals \(86,450,1942,9074\). These finite computations independently test the setup; the statement for all sizes follows from the transfer identity and analytic argument, not numerical extrapolation.

## Relationship to prior work
Frustration and residual entropy of kagome-type Ising systems have a substantial literature. Varma's 2013 study provides transfer-matrix methods for different ladders and the two-dimensional kagome saturation-field ensemble; its explicitly tabulated ladders and characteristic polynomials are not the prism-line, zero-field Ising ensemble analyzed here. The model's unweighted leading entropy constant also appears in earlier counting work on a distinct Eulerian-orientation ice-rule ensemble on the same prism line graphs; equality of growth bases does not specify the present field-weighted magnetization distribution or its Curie coefficient. Existing finite-system Ising line-graph studies and kagome susceptibility studies likewise do not, in the inspected material, give the displayed all-circumference polynomial and radical response coefficient.

## Limitations
This is an exact statement for the specified purely classical finite-width cylinder and the stated order of limits. It does not prove robustness to extra interactions, nonuniform couplings, three-dimensional lattices, or quantum fluctuations. Uniform-field longitudinal susceptibility should not be conflated with transverse quantum response. The historical-priority assessment is bounded by examined accessible material, and an unindexed equivalent computation remains possible. No independent scientific audit is claimed.

## References
- Vipin Kerala Varma, *Saturation field entropies of antiferromagnetic Ising models: Ladders and the kagome lattice*, arXiv:1305.4606 (initial public preprint 20 May 2013), https://arxiv.org/pdf/1305.4606 ; Physical Review B 88, 134421 (2013).
- J. H. Barry and M. Khatun, *Exact solutions for perpendicular susceptibilities of kagomé and decorated-kagomé Ising models*, Physical Review B 35, 8601 (1987), https://doi.org/10.1103/PhysRevB.35.8601 .
- K. A. Muttalib, M. Khatun and J. H. Barry, *Perpendicular susceptibility and geometrical frustration in two-dimensional Ising antiferromagnets: Exact solutions*, Physical Review B 96, 184411 (2017), https://doi.org/10.1103/PhysRevB.96.184411 .
