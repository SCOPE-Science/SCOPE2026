# A single-frequency orthogonal Fourier progression for four paired masses

## Finding

Let \(x_1,x_2,x_3,x_4\in\mathbb R^3\) be affinely independent and let \(\mu=a(\delta_{x_1}+\delta_{x_2})+b(\delta_{x_3}+\delta_{x_4})\), where \(a,b>0\) and \(2a+2b=1\). Write \(e_\xi(x)=\exp(2\pi i\langle\xi,x\rangle)\) for \(\xi\in\mathbb R^3\). There is a single frequency \(\xi\ne0\) for which \(1,e_\xi,e_{2\xi}\) are mutually orthogonal in \(L^2(\mu)\) **if and only if** \(1/2\le a/b\le2\). The frequency may be constructed by solving three real linear equations, with explicit right-hand sides depending on the ratio. At \(a=b\) the same frequency also gives an orthogonal fourth term \(e_{3\xi}\).

The restriction is on the witness, not just the cardinality: an arbitrary orthogonal triple may require two distinct frequency differences, whereas here all its members are consecutive powers of a single character. Equivalently, the pushforward under \(x\mapsto e_\xi(x)\) matches Haar probability on the circle on all trigonometric polynomials of degree at most two.

## Proof

Let \(w=(a,a,b,b)\). For any phases \(z_1,\ldots,z_4\) on the unit circle, choose real \(s_j\) with \(e^{2\pi i s_j}=z_j/z_1\), for \(j=2,3,4\). Solve \(\langle \xi,x_j-x_1\rangle=s_j\). Affine independence makes the real coefficient matrix invertible, giving \(e_\xi(x_j)=\alpha z_j\) for a common unit scalar \(\alpha\). Hence orthogonality of \(1,e_\xi,e_{2\xi}\) is equivalent to the vanishing of the first two weighted power sums for the assigned phases. All characters have norm one.

If the triple is orthogonal, the four-by-three matrix with columns given by its evaluations weighted by \(\sqrt{w_j}\) has orthonormal columns. Its row squared norms are \(3w_j\), and they are the diagonal entries of an orthogonal projection, so each is at most one. With \(a+b=1/2\) this is exactly the stated ratio condition.

Conversely, in the closed ratio interval choose \(\theta\in[0,\pi/2]\) and \(\phi\in[\pi/2,\pi]\) with
\[
\cos\theta=\sqrt{b/(2a)},\qquad \cos\phi=-\sqrt{a/(2b)}.
\]
Both choices exist at every admissible ratio. Assign \(z=(e^{i\theta},e^{-i\theta},e^{i\phi},e^{-i\phi})\). Then
\[
\sum_jw_j z_j=2a\cos\theta+2b\cos\phi=0,\qquad
\sum_jw_j z_j^2=2a(2\cos^2\theta-1)+2b(2\cos^2\phi-1)=0.
\]
Use these phases in the linear system above. The vanished first moment guarantees \(\xi\ne0\); the two vanishing moments give the triple, including when one paired phase coincides at a threshold. In the uniform case the assigned phases are the four fourth roots of \(-1\), so the third moment vanishes as well and the four consecutive powers are an orthonormal basis.

## Relation to the unrestricted capacity problem

*Fourier orthogonality on a positively weighted square: a complete classification* [1], case \(T_1\), gives the same sharp threshold for an unrestricted orthogonal triple on a square with opposite paired weights. With the site labels matched by weight, each character's relative square phases can be lifted separately to a real frequency on any affine tetrahedron by the linear system above. Thus the square construction already gives unrestricted triple existence throughout the ratio interval. Outside the interval the projection obstruction applies on the tetrahedron, and the phases \((1,-1,1,-1)\) give an orthogonal pair for all positive \(a,b\). Four orthogonal characters would give projection diagonal \(4w_j\le1\) and hence force equal masses; the uniform case is attained. The unrestricted capacity is therefore 4 at uniform mass, 3 at the other in-range weights, and 2 outside the range. This capacity calculation is not claimed as a separate contribution.

The square record's displayed \(T_1\) witness \(\{0,\xi,\eta\}\) verifies three differences by using independent phase directions; it does not in general impose \(\eta=2\xi\) or exhibit vanishing of the first two moments of a single character. The construction here enforces those two moment equations simultaneously. Li and Wang [2] consider infinite uniform-digit self-affine measures rather than this prescribed-mass circle-moment problem. Equivalent four-node quadrature results may exist outside the sources inspected.

## Verification and scope

The algebra applies to every admissible real mass ratio and affine tetrahedron. The supplementary `checker.py` samples the phase formula including both endpoints, tests the equal-mass fourth term, and solves the relative-phase system on one non-axis-aligned tetrahedron. These numerical diagnostics are not the universal proof. No claim is made about four arbitrary weights, affinely dependent supports, lattice-restricted frequencies, or infinite self-affine measures.

## References

1. [*Fourier orthogonality on a positively weighted square: a complete classification*](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-fourier-orthogonality-on-a-positively-weighted-square-a-complete--6f6d58e5ae26/RESULT.md), Finding and proof of case \(T_1\). The shared date alone does not establish priority.
2. Y.-Q. Li and Z.-M. Wang, *The Number of Orthogonal Exponential Functions of a Class of Self-Affine Measures in \(\mathbb R^3\)*, **Axioms** 15 (2026), 563, [doi:10.3390/axioms15080563](https://doi.org/10.3390/axioms15080563).
