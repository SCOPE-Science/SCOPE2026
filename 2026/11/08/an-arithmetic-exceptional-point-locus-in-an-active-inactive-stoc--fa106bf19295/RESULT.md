# An arithmetic exceptional-point locus in an active–inactive stochastic ring

## Finding

Consider a continuous-time Markov process on a ring with \(n\ge 3\) positions, each having an active state and an immobile inactive state. An active particle jumps clockwise one position at rate \(p>0\), switches to the inactive state at its present position at rate \(r>0\), and reactivates there at rate \(s>0\). An inactive particle cannot move.

**Theorem.** Its real \(2n\)-state generator is nondiagonalizable over \(\mathbb C\) **if and only if** the rates coincide with one of exactly \(\lfloor(n-1)/2\rfloor\) distinct pairs
\[
(r,s)=\bigl(p\eta_k(1-\eta_k),\ p\eta_k(1+\eta_k)\bigr),
\qquad \eta_k=\sin(\pi k/n),\qquad
1\le k\le\lfloor(n-1)/2\rfloor.
\]
At each pair, the generator has exactly two nontrivial complex-conjugate Jordan blocks, both of size two, at eigenvalues
\[
\lambda_{\pm}=-s\pm i\frac p2\sin(2\pi k/n).
\]
Every other eigenvalue is simple. In particular, no larger Jordan block occurs and the stationary eigenvalue remains simple. Outside the displayed finite set the generator is diagonalizable.

The exceptional pairs all lie on the *same* parabola
\[
(r+s)^2=2p(s-r),\qquad r,s>0.
\]
As the ring size varies, they are dense in the open parabolic arc parametrized by \(r=p\eta(1-\eta)\), \(s=p\eta(1+\eta)\), \(0<\eta<1\). Every exceptional pair satisfies \(r\le p/4\), with equality at a finite ring size exactly when \(6\mid n\).

The Jordan degeneracy is directly observable. Starting active at position zero, define the Fourier amplitude of inactive-site probabilities by
\[
\widehat I_k(u)=\sum_{j=0}^{n-1} e^{2\pi i k j/n}\,\Pr\{\text{inactive at position }j\text{ at time }u\}.
\]
At the rate pair corresponding to \(k\), for all physical times \(u\ge 0\),
\[
\boxed{\widehat I_k(u)=ru\exp\!\left[\left(-s+\frac{ip}{2}\sin\frac{2\pi k}{n}\right)u\right].}
\]
The factor \(u\) is the critical Jordan enhancement of an exponentially damped oscillatory Fourier mode; it is not a change of the stationary distribution or a claim that total probabilities diverge.

## Assumptions and scope

All rates \(p,r,s\) are finite and strictly positive; \(n\) is an integer at least three; the process contains a **single noninteracting particle** on a periodic clockwise ring. Each position has exactly one active and one inactive microstate. The generator is in the column convention \(\dot v=Gv\), with nonnegative off-diagonal entries and columns summing to zero. The result concerns exact algebraic defectiveness of the complete generator, not only proximity of eigenvalues. Boundary rates \(r=0\), \(s=0\), or \(p=0\) are excluded. The classification is not asserted for reverse walking, heterogeneous rates, open boundaries, or interacting particles.

## Proof

Write \(A_j(u),I_j(u)\) for the active and inactive probabilities at position \(j\) modulo \(n\). The master equations are
\[
\dot A_j=pA_{j-1}-(p+r)A_j+sI_j,\qquad
\dot I_j=rA_j-sI_j.
\]
Fourier-transform both sequences using \(\widehat A_k=\sum_j e^{i\theta_kj}A_j\) and \(\widehat I_k=\sum_j e^{i\theta_kj}I_j\), where \(\theta_k=2\pi k/n\). Since the discrete Fourier transform is invertible, \(G\) is similar over \(\mathbb C\) to the direct sum of the two-by-two blocks
\[
B_k=\begin{pmatrix}p e^{i\theta_k}-p-r&s\\r&-s\end{pmatrix}.
\]
The characteristic equation is
\[
(\lambda+s)(\lambda+p+r-pe^{i\theta_k})-rs=0.
\tag{1}
\]
No eigenvalue equals \(-s\), since substituting it into (1) yields \(-rs\ne 0\). Solving (1) for \(e^{i\theta_k}\) shows that any given eigenvalue determines the unique spatial Fourier index:
\[
e^{i\theta_k}=\frac{\lambda+p+r-rs/(\lambda+s)}p.
\tag{2}
\]
Therefore spectra from distinct Fourier blocks cannot overlap. Consequently, \(G\) is defective precisely when one Fourier block has a repeated root.

The quadratic discriminant of \(B_k\) is
\[
\Delta_k=\left(s-r-p(1-\cos\theta_k)+ip\sin\theta_k\right)^2+4rs.
\tag{3}
\]
For \(k=0\), the two eigenvalues are \(0\) and \(-(r+s)\). When \(n\) is even and \(k=n/2\), the discriminant is \((s-r-2p)^2+4rs>0\). Neither block is defective. For other \(k\), \(\sin\theta_k\ne0\). Taking imaginary and real parts of (3), the necessary and sufficient conditions \(\Delta_k=0\) are
\[
s-r=p(1-\cos\theta_k),\qquad 4rs=p^2\sin^2\theta_k.
\tag{4}
\]
Put \(\eta=\sin(\pi k/n)\in(0,1)\). Then \(1-\cos\theta_k=2\eta^2\) and \(\sin^2\theta_k=4\eta^2(1-\eta^2)\). Equation (4) gives \(s-r=2p\eta^2\) and \(rs=p^2\eta^2(1-\eta^2)\); hence \((r+s)^2=(s-r)^2+4rs=4p^2\eta^2\). Positivity selects \(r+s=2p\eta\) and thus exactly \(r=p\eta(1-\eta)\) and \(s=p\eta(1+\eta)\).

For \(1\le k\le\lfloor(n-1)/2\rfloor\), the numbers \(\eta_k\) strictly increase; the only other Fourier index with the same \(\eta\) is \(n-k\). Thus there are precisely the stated distinct positive-rate exceptional pairs. At each, the repeated eigenvalue of \(B_k\) is half its trace,
\[
\lambda_k=-s+\tfrac{ip}{2}\sin\theta_k.
\]
The matrix \(B_k-\lambda_k I\) is nonzero because its lower-left entry is \(r>0\). Its square is zero by the two-by-two Cayley–Hamilton identity. Therefore it has a single Jordan block of size two. The conjugate Fourier block \(B_{n-k}\) has the conjugate eigenvalue and another block of size two. By (2), neither repeated eigenvalue appears in another block, and all the remaining spectral values are simple. This proves the global classification.

For the initial condition \(A_0(0)=1\) with all other probabilities zero, the \(k\)-th Fourier block starts at column vector \((1,0)^T\). At an exceptional pair, its propagator is
\[
e^{uB_k}=e^{u\lambda_k}\bigl(I+u(B_k-\lambda_k I)\bigr).
\]
The inactive component is therefore \(ru e^{\lambda_k u}\), proving the observable formula.

Finally, \(r+s=2p\eta\) and \(s-r=2p\eta^2\) eliminate \(\eta\) to yield the parabola. Rational \(k/n\) with \(0<k/n<1/2\) are dense in \((0,1/2)\); continuity and strict monotonicity of \(\sin(\pi\cdot)\) imply density of their \(\eta\)-values in \((0,1)\). The bound \(\eta(1-\eta)\le1/4\) is sharp only at \(\eta=1/2\). In the allowed index range, \(\sin(\pi k/n)=1/2\) exactly when \(k/n=1/6\), equivalent to \(6\mid n\).

## Verification

Run `python verify.py` with Python 3, NumPy and SciPy. The independently assembled full \(2n\)-state generator is used for exponential-propagator comparisons, rather than invoking the same Fourier block for both sides of the identity. The recorded run produced 420 zero-discriminant/Jordan-block comparisons for \(3\le n\le42\), 900 off-locus discriminant checks, and 100 full-generator propagation comparisons for \(3\le n\le11\). The exact all-size conclusions follow from the preceding algebra, not from these finite checks. `checks.txt` records the replay output.

## Relationship to prior work

The active/immobile switching motif appears in the many-motor exclusion models of Pinkoviezky and Gov (2013), which analyze current–density and jamming behavior. The present system deliberately restricts to a *single* particle and studies spectral defectiveness at finite positive rates rather than traffic jams; the published stationary current formulas and cluster approximations do not themselves imply the precise exceptional-point locus. Weber and Pande (2015) analyze damped probability oscillations and complex eigenmodes of a biased triangular Markov network with a slow connection, not the periodic two-state ring or a rate-complete Jordan classification. Generic non-Hermitian exceptional-point methods are known (Berry and Uzdin, 2011); the definition and use of a two-by-two discriminant are not claimed as new. The contribution is the exact positive-rate classification across *all* ring sizes, its arithmetic distribution, and the directly measurable Jordan pulse.

## Limitations

This is a mathematical result for an idealized noninteracting, entirely clockwise process. Physical motors with backward moves, interactions, spatial rate disorder, or finite time resolution may not exhibit exact degeneracies, although nearby rates still influence relaxation modes. Exceptional points are subleading transient spectral features and do not cause a nonequilibrium steady-state singularity. Literature comparison is evidence-based rather than a mathematical proof of global priority: accessible relevant primary material was examined, but exhaustive indexing and every historical full text cannot be guaranteed.

## References

1. I. Pinkoviezky and N. S. Gov, “Modelling interacting molecular motors with an internal degree of freedom,” *New Journal of Physics* **15**, 025009 (first public 5 February 2013). DOI: https://doi.org/10.1088/1367-2630/15/2/025009.
2. I. Pinkoviezky and N. S. Gov, “Transport dynamics of molecular motors that switch between an active and inactive state,” *Physical Review E* **88**, 022714 (published 20 August 2013). DOI: https://doi.org/10.1103/PhysRevE.88.022714.
3. J. K. Weber and V. S. Pande, “Entropy-production-driven oscillators in simple nonequilibrium networks,” *Physical Review E* **91**, 032136 (published 24 March 2015). DOI: https://doi.org/10.1103/PhysRevE.91.032136.
4. M. V. Berry and R. Uzdin, “Slow non-Hermitian cycling: exact solutions and the Stokes phenomenon,” *Journal of Physics A* **44**, 435303 (published 28 October 2011). DOI: https://doi.org/10.1088/1751-8113/44/43/435303.
