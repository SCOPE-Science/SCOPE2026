# No negative point spectrum in the interior phase-twisted square quantum graph
## Finding
For the equilateral square metric graph studied by Exner and Tater, let every edge have length \(\ell>0\), normalize the coupling length scale to one, and impose at every degree-four vertex the phase-twisted preferred-orientation condition \(U=e^{i\mu}R\) with \(0<\mu<\pi/2\). Then the negative point spectrum is empty. Equivalently, no energy \(E=-\kappa^2<0\) is a Bloch flat band.

Writing
\[
Q=\cos\theta_1+\cos\theta_2,
\]
the source's negative-energy Bloch equation is affine in \(Q\). Its coefficient is
\[
2\kappa(1+\kappa^2)\sinh(\kappa\ell),
\]
which is strictly positive for every \(\kappa>0\). Consequently a fixed negative energy can satisfy the fiber equation only on a measure-zero quasimomentum level set, never on a positive-measure family of fibers.

## Assumptions and scope
The graph is the nonmagnetic equilateral square lattice of arXiv:2108.04708v1. The phase is restricted to \(0<\mu<\pi/2\), exactly the interior phase regime emphasized there. A negative energy is parameterized as \(E=-\kappa^2\) with \(\kappa>0\). The statement concerns point spectrum, equivalently dispersionless Bloch bands of the periodic operator. It makes no assertion about the existence, number, or widths of negative absolutely-continuous bands.

There is no omitted negative analogue of the positive Dirichlet singular set: for \(\kappa>0\), \(\sinh(\kappa\ell)\neq0\), so the hyperbolic Floquet reduction has no exceptional momentum at which the edge ansatz degenerates.

## Proof
Exner--Tater write the negative-energy spectral condition, after setting the positive-energy momentum to \(i\kappa\), as
\[
F_-(\kappa,Q)=\sum_{j=0}^4 c_j\kappa^j=0,
\]
with
\[
\begin{aligned}
c_0=c_4&=\sin(2\mu)\sinh^2(\kappa\ell),\\
c_2&=-\sin(2\mu)\bigl(1+3\cosh(2\kappa\ell)\bigr),\\
c_1&=-2\bigl(2\cos(2\mu)\cosh(\kappa\ell)-Q\bigr)\sinh(\kappa\ell),\\
c_3&=2\bigl(2\cos(2\mu)\cosh(\kappa\ell)+Q\bigr)\sinh(\kappa\ell).
\end{aligned}
\]
Only \(c_1\) and \(c_3\) depend on \(Q\). Therefore
\[
\frac{\partial F_-}{\partial Q}
=2\kappa\sinh(\kappa\ell)+2\kappa^3\sinh(\kappa\ell)
=2\kappa(1+\kappa^2)\sinh(\kappa\ell)>0.
\]
Thus for every fixed \(\kappa>0\), the equation \(F_-(\kappa,Q)=0\) determines at most one value \(Q=q_\kappa\).

On the Bloch torus \(\mathbb T^2\), the function \(Q(\theta_1,\theta_2)=\cos\theta_1+\cos\theta_2\) is a nonconstant real-analytic function. Every level set \(Q=q\) has two-dimensional Lebesgue measure zero. Hence the set of fibers carrying the fixed energy \(-\kappa^2\) has measure zero. A point eigenvalue of the periodic direct integral would require the same fiber eigenvalue on a positive-measure set of quasimomenta, so no \(-\kappa^2<0\) belongs to the point spectrum. This proves the claim.

## Verification
The bundled `artifacts/verify.py` reconstructs the source polynomial symbolically and differentiates it with respect to \(Q\). It verifies the exact identity
\[
\frac{\partial F_-}{\partial Q}=2\kappa(1+\kappa^2)\sinh(\kappa\ell)
\]
and checks directly that subtracting this affine term removes all \(Q\)-dependence. The checker is an exact symbolic replay; the proof of the measure-zero implication is analytic and is not replaced by finite sampling.

## Relationship to prior work
The primary 2021 source derives the negative-energy coefficients above and analyzes how the phase twist changes the spectrum. Its flat-band discussion then concerns the positive-energy equation: it notes that the old infinite flat-band series disappears for interior phase and exhibits an exceptional positive flat band at \(k=1\). It does not state that the negative point spectrum is empty.

The earlier general square-lattice analysis of Exner and Turek proves that periodic square quantum graphs with general self-adjoint vertex conditions can have both absolutely-continuous bands and infinitely degenerate eigenvalues, and that the negative spectrum has only finitely many bands. That general structural theorem does not decide whether the present phase-twisted family has a negative flat band. The strict affine coefficient above resolves that question for this family.

A separate asymptotic analysis of the same phase-twisted model can resolve negative Bloch-band widths for large \(\ell\); such asymptotics do not exclude a flat negative eigenvalue at arbitrary finite \(\ell\). The present statement is uniform over the full stated \((\ell,\mu)\) domain.

## Limitations
The result is restricted to negative energies for the equilateral nonmagnetic square lattice and interior phase \(0<\mu<\pi/2\). It does not classify the positive point spectrum, endpoint phases, magnetic variants, unequal edge lengths, or the number and location of negative absolutely-continuous bands. It also does not assert any quantitative lower bound on their widths.

## References
1. P. Exner and M. Tater, *Quantum graphs: self-adjoint, and yet exhibiting a nontrivial \(\mathcal{PT}\)-symmetry*, arXiv:2108.04708v1 (2021); Physics Letters A 416, 127669; DOI:10.1016/j.physleta.2021.127669.
2. P. Exner and O. Turek, *High-energy asymptotics of the spectrum of a periodic square-lattice quantum graph*, arXiv:1006.1446 (2010); Journal of Physics A 43, 474024; DOI:10.1088/1751-8113/43/47/474024.
