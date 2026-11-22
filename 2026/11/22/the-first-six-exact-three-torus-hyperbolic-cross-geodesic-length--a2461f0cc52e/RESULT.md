# The first six exact three-torus hyperbolic-cross geodesic lengths

## Finding
On the standard flat three-torus \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\), define the hyperbolic cross
\[
H_3(t)=\{m\in\mathbb Z^3:\prod_{j=1}^3\max(1,|m_j|)\le t\}.
\]
A primitive integer vector \(v\in\mathbb Z^3\) determines a closed geodesic \(\gamma_v(s)=x_0+sv\pmod{2\pi}\), for \(0\le s\le2\pi\). Call it a hyperbolic-cross \(t\)-design geodesic if normalized arclength observation annihilates every nonconstant Fourier character with frequency in \(H_3(t)\). For the complete natural range \(1\le t\le6\), the sharp minimum squared winding norm \(Q(t)=\min\|v\|_2^2\), and its **unique** minimizer up to independent coordinate signs and permutation, are:

| \(t\) | \(|H_3(t)|\) | \(Q(t)\) | Canonical optimum \(v\) |
|---|---:|---:|---|
| 1 | 27 | 21 | \((1,2,4)\) |
| 2 | 81 | 65 | \((2,5,6)\) |
| 3 | 135 | 101 | \((4,6,7)\) |
| 4 | 225 | 133 | \((4,6,9)\) |
| 5 | 279 | 133 | \((4,6,9)\) |
| 6 | 405 | 314 | \((7,11,12)\) |

Thus the minimum physical length is \(2\pi\sqrt{Q(t)}\). In particular, **strength four and strength five have exactly the same unique optimal winding and length**, whereas strength six forces a jump from squared winding norm \(133\) to \(314\). The row \(t=1\) is the classical full-cube baseline; the finite classification at \(t=2,\ldots,6\) is the additional result.

## Assumptions and scope
The curve is a single complete, once-traversed, primitive closed geodesic of the quotient Euclidean metric, not an arbitrary closed rectifiable curve or a disconnected trajectory. The normalized arclength measure is \(ds/(2\pi)\). The frequency set is exactly the three-dimensional hyperbolic cross defined above, with integer strength \(1\le t\le6\). The coordinate-period convention is \(2\pi\), whereas references on the unit-period torus express lengths smaller by a factor \(2\pi\). Translations \(x_0\) do not affect exactness.

## Proof
For a Fourier character, directly integrate along the proposed geodesic:
\[
\frac1{2\pi}\int_0^{2\pi}e^{i m\cdot\gamma_v(s)}\,ds=
\begin{cases}e^{im\cdot x_0},&m\cdot v=0,\\0,&m\cdot v\ne0.\end{cases}
\]
Hence the design criterion is **equivalent**, without approximation, to
\[
\forall m\in H_3(t)\setminus\{0\},\quad m\cdot v\ne0.\tag{1}
\]
The hyperbolic cross is invariant under every independent sign reversal and coordinate permutation. The unit coordinate frequencies belong to it, so (1) forces all three coordinates of \(v\) to be nonzero. A winding whose coordinates have common divisor greater than one is a repeated traversal of a shorter geodesic, and dividing by that divisor preserves (1). Thus every shortest design has a unique representative of the form \(1\le a\le b\le c\), \(\gcd(a,b,c)=1\).

The six displayed candidate vectors satisfy (1), as established by the exact integer loops in `checker.py`. This yields the finite respective upper bounds \(C_t=21,65,101,133,133,314\) for \(\|v\|_2^2\). To prove that no shorter geodesic or inequivalent equal-length minimizer exists, it suffices to inspect the **entire** finite set
\[
\mathcal W_t=\{(a,b,c)\in\mathbb Z^3:1\le a\le b\le c\le\lfloor\sqrt{C_t}\rfloor,\ a^2+b^2+c^2\le C_t,\ \gcd(a,b,c)=1\}.
\]
Indeed every omitted positive ordered integer triple has norm squared greater than \(C_t\), and the preceding symmetries and primitivity eliminate no possible distinct shortest curve. For each \(w\in\mathcal W_t\), the `checker.py` certificate constructs the complete finite set \(H_3(t)\setminus\{0\}\) by three nested integer loops and searches for an **explicit nonzero integer witness** \(m\) satisfying \(m\cdot w=0\). The code asserts that the only triple without any such witness is precisely the listed canonical optimum. Thus the candidate’s design property and all competitors' failures are both checked against *every* required frequency. The bounded enumeration is exhaustive for the stated finite theorem; it does not purport to establish a formula at untested strengths.

For additional transparency, the numbers of primitive ordered candidates examined in order \(t=1,\ldots,6\) are \(9,41,80,119,119,421\). Respectively \(8,40,79,118,118,420\) have an integer orthogonality witness, leaving exactly one survivor in each case. These values are recomputed and independently asserted by the standalone source. Since the original winding vectors are precisely the signed coordinate permutations of these survivors, this completes all sharp bounds and equality classifications.

## Verification
Run `python checker.py` in a standard Python 3 environment. It uses only the standard library, exact integer arithmetic, independently constructs each hyperbolic cross, enumerates all ordered positive primitive triples under the certified norm bound, searches every hyperbolic-cross frequency for a zero dot product, and asserts the uniquely surviving triple for each strength. The output has six `survivors` entries of size one, the norm-squared sequence \(21,65,101,133,133,314\), and the final message `EXHAUSTIVE FINITE CERTIFICATE PASSED`. The program is small enough for manual review and has no files, network, random seeds, or external dependencies. The explicit range-covering argument above is necessary: merely running some finite tests would not prove global optimality.

## Relationship to prior work
The reconstruction and nonaliasing principles underlying rank-one lattice sampling are classical; see Kämmerer–Potts–Volkmer (2015) and Gross–Iwen–Kämmerer–Volkmer (2020). Much closer, Ehler's *Optimal bounds for design curves on the torus* (arXiv:2611.03362, November 2, 2026), Section 4, defines exactly these hyperbolic crosses, gives a **sharp all-strength answer in dimension two**, and establishes order-optimal asymptotic length bounds, not exact finite optima, in dimension at least three (Theorem 4.3). Its general cube-length theorem (Section 2) gives the \(t=1\) baseline but does not determine these stronger noncubical cross constraints. The novelty here is the explicit finite three-dimensional sharp *arclength staircase*, including a nontrivial plateau and equality rigidity for the six initial strengths, not the definition of the cross or a general rank-one lattice construction.

## Limitations
The result covers strengths one through six, dimension three, and primitive **geodesic** design trajectories only; it does not claim optimality among arbitrary closed curves, or provide asymptotics in strength or dimension. The certificate is an exhaustive finite integer proof under a proved bound, not an infinite proof or a numerical estimate. Specialist historical literature may contain an unlocated equivalent table. The comparison with the 2026 source rests on inspection of its relevant full-text Sections 2 and 4; earlier hidden results are not ruled out. No independent mathematical audit is claimed.

## References
1. C. Gross, M. A. Iwen, L. Kämmerer, and T. Volkmer, *A Deterministic Algorithm for Constructing Multiple Rank-1 Lattices of Near-Optimal Size*, arXiv:2003.09753, first public March 21, 2020, https://arxiv.org/abs/2003.09753.
2. M. Ehler, *Optimal bounds for design curves on the torus*, arXiv:2611.03362, first public November 2, 2026, https://arxiv.org/abs/2611.03362; especially Sections 2 and 4.
3. L. Kämmerer, D. Potts, and T. Volkmer, *Approximation of multivariate periodic functions by trigonometric polynomials based on rank-1 lattice sampling*, Journal of Complexity 31 (2015), 543–576, open manuscript https://www-user.tu-chemnitz.de/~lkae/paper/KaPoVo2013.pdf.
