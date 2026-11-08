# Branch-point Jacobi kernels on radial stars: exact Christoffel growth and a Bessel scaling limit

## Finding
For any integer \(q\ge 2\), put \(\zeta=\exp(2\pi i/q)\) and let the radial star be \(E_q=\bigcup_{\ell=0}^{q-1}\zeta^\ell[0,1]\). For real \(\alpha,\beta>-1\), define the probability measure \(\mu\) by averaging the measure proportional to \(r^\beta(1-r^q)^\alpha\,dr\) over the \(q\) rays. Let \(K_n(z,w)\) be the reproducing kernel of complex polynomials of degree at most \(n\) in \(L^2(\mu)\). Write \(A_m=(\beta+2m+1)/q\), \(B_0=\mathrm B(A_0,\alpha+1)\), and \(N_m=\lfloor(n-m)/q\rfloor\).

The entire finite-degree kernel admits the exact orthogonal decomposition
\[
K_n(z,w)=B_0\sum_{m=0}^{q-1}(z\overline w)^m\sum_{j=0}^{N_m}
\frac{J_{j,m}(z^q)J_{j,m}(\overline w^{\,q})}{h_{j,m}},
\quad J_{j,m}(u)=P_j^{(A_m-1,\alpha)}(1-2u),
\]
where an inner sum with \(N_m<0\) is empty, \(P_j^{(a,b)}\) denotes the classical Jacobi polynomial, and
\[
h_{0,m}=\mathrm B(A_m,\alpha+1),\qquad
h_{j,m}=\frac{\Gamma(j+A_m)\Gamma(j+\alpha+1)}{(2j+A_m+\alpha)\,\Gamma(j+1)\Gamma(j+A_m+\alpha)}\quad(j\ge1).
\]
In particular, for every integer \(n\ge0\), setting \(N=\lfloor n/q\rfloor\) gives the **exact central Christoffel kernel**
\[
\boxed{K_n(0,0)=\frac{\Gamma(\alpha+1)\Gamma(N+A_0+1)\Gamma(N+A_0+\alpha+1)}{\Gamma(A_0+1)\Gamma(A_0+\alpha+1)\Gamma(N+1)\Gamma(N+\alpha+1)}.}
\]
It follows that
\[
\boxed{\lim_{n\to\infty}n^{-2(\beta+1)/q}K_n(0,0)=
\frac{q^{-2(\beta+1)/q}\Gamma(\alpha+1)}{\Gamma(1+(\beta+1)/q)\Gamma(1+\alpha+(\beta+1)/q)}.}
\]
Thus the exact singular-junction exponent is \(2(\beta+1)/q\); in particular, unweighted arclength has exponent \(2/q\).

There is also a **full, locally uniform two-variable scaling limit**. Define the entire function
\[
F_A(v)=\sum_{k=0}^{\infty}\frac{(-v)^k}{k!\,\Gamma(k+A)}
\]
for \(A>0\), and define
\[
\mathcal K_{q,\alpha,\beta}(\xi,\eta)=2B_0\sum_{m=0}^{q-1}(\xi\overline\eta)^m
\int_0^1 t^{2A_m-1}F_{A_m}(t^2\xi^q)F_{A_m}(t^2\overline\eta^{\,q})\,dt.
\]
Then, uniformly for \((\xi,\eta)\) in every compact subset of \(\mathbb C^2\),
\[
\boxed{\lim_{N\to\infty}N^{-2A_0}K_{qN+q-1}\left(\frac{\xi}{N^{2/q}},\frac{\eta}{N^{2/q}}\right)=\mathcal K_{q,\alpha,\beta}(\xi,\eta).}
\]
Each of the \(q\) distinct Jacobi residue classes contributes at leading order. More sharply, **the origin-normalized two-point hard-edge limit does not depend on the outer Jacobi exponent \(\alpha\)**: for every \(\alpha>-1\), locally uniformly on \(\mathbb C^2\),
\[
\boxed{\lim_{N\to\infty}\frac{K_{qN+q-1}(\xi/N^{2/q},\eta/N^{2/q})}{K_{qN+q-1}(0,0)}=2A_0\Gamma(A_0)^2\sum_{m=0}^{q-1}(\xi\overline\eta)^m\int_0^1 t^{2A_m-1}F_{A_m}(t^2\xi^q)F_{A_m}(t^2\overline\eta^{\,q})\,dt.}
\]
The right side depends only on \(q\) and the inner-ray exponent \(\beta\); it equals one at \(\xi=\eta=0\). This **boundary-weight universality** identifies the complete complex two-point transition at the branch vertex, rather than merely a scalar growth estimate.

## Assumptions and scope
The domain is the finite radial star \(E_q\) with \(q\ge2\) equally spaced unit-length rays. The measure is explicitly
\[
\int_{E_q}g\,d\mu=\frac{q}{B_0}\frac1q\sum_{\ell=0}^{q-1}\int_0^1g(\zeta^\ell r)r^\beta(1-r^q)^\alpha\,dr.
\]
Here \(\alpha,\beta>-1\), guaranteeing finite positive mass and \(A_m>0\). The kernel is taken for all complex polynomials of total degree at most \(n\), not for separate multi-orthogonality systems, and is holomorphic in its first argument and antiholomorphic in its second. The Christoffel function at the origin is \(K_n(0,0)^{-1}\). There is no assertion for unequal ray weights, nonuniform angles, or general intersecting arcs.

## Proof
**1. Orthogonal decomposition.** Every polynomial of degree at most \(n\) has the unique cyclic decomposition \(p(z)=\sum_{m=0}^{q-1}z^mQ_m(z^q)\) with \(\deg Q_m\le N_m\). Averaging over roots of unity annihilates cross terms with different residues. Under \(u=r^q\), one obtains exactly
\[
\|p\|_{L^2(\mu)}^2=\frac1{B_0}\sum_{m=0}^{q-1}\int_0^1|Q_m(u)|^2u^{A_m-1}(1-u)^\alpha\,du.
\]
The classical Jacobi orthogonality formula on \([0,1]\) gives the displayed squared norms \(h_{j,m}\). For \(j=0\) the Beta-integral expression must be used directly, avoiding a removable singularity when \(A_m+\alpha=0\). Summing orthonormal rank-one terms proves the exact formula for \(K_n\), without assuming a limiting Hilbert space.

**2. Central Christoffel function.** At \(z=w=0\), all blocks except \(m=0\) vanish. The endpoint values \(J_{j,0}(0)=\Gamma(j+A_0)/[\Gamma(A_0)\Gamma(j+1)]\) and the Jacobi norms give the displayed kernel sum. For \(N=0\), it equals one since \(\mu\) is a probability measure. The proposed Gamma quotient has the ratio \((N+A_0)(N+A_0+\alpha)/[N(N+\alpha)]\) between successive values. Subtracting adjacent quotients reproduces exactly \(B_0J_{N,0}(0)^2/h_{N,0}\). Induction proves the closed formula for every \(N\ge0\). Standard Gamma-ratio asymptotics give the stated sharp power and constant. Because \(N=\lfloor n/q\rfloor\), the factor \(q^{-2A_0}\) appears when the asymptotic is expressed in \(n\), rather than \(N\).

**3. Uniform Bessel-limit reduction.** Fix \(A>0\), \(\alpha>-1\), and a compact subset of \(\mathbb C\). The hypergeometric expansion
\[
P_j^{(A-1,\alpha)}(1-2v/N^2)=\frac{\Gamma(j+A)}{\Gamma(A)\Gamma(j+1)}
\sum_{k=0}^{j}\frac{(-j)_k(j+A+\alpha)_k}{(A)_k\,k!}\left(\frac v{N^2}\right)^k
\]
shows that if \(j/N\to t>0\), then
\[
 j^{1-A}P_j^{(A-1,\alpha)}(1-2v/N^2)\longrightarrow F_A(t^2v)
\]
uniformly for \(v\) in compact sets and \(t\) in compact subintervals of \((0,1]\). Indeed the term of order \(k\) converges to \((-t^2v)^k/[k!\Gamma(A+k)]\) after extracting \(j^{A-1}\); a summable majorant comes from the Pochhammer coefficients. The same representation gives the uniform bound \(\big|P_j^{(A-1,\alpha)}(1-2v/N^2)\big|\le C(j+1)^{A-1}\) for \(0\le j\le N\) and bounded \(v\). Independently, \(h_j(A,\alpha)^{-1}=2j(1+O(j^{-1}))\) as \(j\to\infty\).

Consequently the \(m\)-th Jacobi block, divided by \(N^{2A_m}\), is a Riemann sum converging locally uniformly to
\[
2\int_0^1t^{2A_m-1}F_{A_m}(t^2\xi^q)F_{A_m}(t^2\overline\eta^{\,q})\,dt.
\]
The contribution with \(j/N\le\varepsilon\) is bounded by \(C\varepsilon^{2A_m}\), so the origin of the Riemann interval causes no loss even when \(A_m<1/2\). Finally, multiplying by \((\xi\overline\eta)^mN^{-4m/q}\) and observing \(2A_m-4m/q=2A_0\) proves the full limit after summing the finitely many blocks. This also proves locally uniform convergence in both complex variables. The center asymptotic written in \(N\) is \(K_{qN+q-1}(0,0)\sim B_0N^{2A_0}/(A_0\Gamma(A_0)^2)\). Dividing the two-point limit by this center constant cancels all factors involving \(\alpha\), proving the displayed outer-weight universality. The limit's value at the origin is \(2A_0\Gamma(A_0)^2\int_0^1t^{2A_0-1}dt/\Gamma(A_0)^2=1\).

## Verification
The accompanying `check_star.py` independently computes finite-degree kernels in two ways: first from the full monomial moment Gram matrix, and second from the explicit Jacobi decomposition. It also checks the exact center Gamma quotient and the predicted off-diagonal scaling numerically at degrees increasing to the hard edge. Three additional checks compare the center-normalized kernel with two different outer exponents. The recorded successful run reports `JACOBI_STAR_KERNEL_CHECK_PASS moment_and_center=8 hard_edge=6 normalized_universality=3 total=17`. Numerical convergence does not prove the infinite-degree theorem; the Riemann-sum and Gamma arguments above do.

## Relationship to prior work
Marinescu and Vu (arXiv:2210.11031, first public October 20, 2022) prove general polynomial growth of Bergman/Christoffel kernels for measures on piecewise smooth totally real submanifolds; their stated theorems do not identify an exact junction exponent or a locally uniform two-point limit on a radial star. Leurs and Van Assche (arXiv:1804.07512) study multiple orthogonal polynomial systems on the same geometric \(q\)-star and related Jacobi weights, but their type-I/type-II multiple orthogonality is not the positive scalar \(L^2\)-projection kernel computed here. Danka and Totik (arXiv:1504.03968) give exact Christoffel asymptotics at locally smooth arc interiors and endpoints; the quoted hypotheses require a single locally smooth arc near the point, not \(q\ge3\) distinct rays meeting there. Classical Jacobi endpoint formulas and Mehler–Heine asymptotics (see Van Assche, arXiv:1408.6140, Introduction) are ingredients, not claimed as new. The central exponent and Gamma factor separately also follow by an elementary symmetry reduction to a single Jacobi endpoint problem; they are not presented as an intrinsically new Christoffel mechanism. The proposed new statement is the complete two-variable \(q\)-channel hard-edge scaling at a branching junction, especially the non-obvious fact that **normalization by the center value removes the outer-weight parameter \(\alpha\)**, even though all \(q\) Jacobi sectors contribute. This result is not the smooth-arc scalar asymptotic quoted in Danka–Totik, nor the separate one-channel classical Jacobi limit.

## Limitations
The asserted novelty is relative to inspected literature and searchable records, not an exhaustive historical priority proof. A previously unnoticed polynomial-inverse-image or singular-crossing universality theorem could already imply part or all of the result. The proof handles equal angular spacing and identical weights on every ray, with fixed \(q,\alpha,\beta\). It gives no quantitative uniform error rates, no general statement for varying parameters, and no claim about unequal-ray perturbations or random-polynomial zero fluctuations.

## References
- G. Marinescu and D.-V. Vu, *Bergman kernel functions associated to measures supported on totally real submanifolds*, arXiv:2210.11031 (first posted October 20, 2022), sections 1 and 4.
- M. Leurs and W. Van Assche, *Jacobi–Angelesco multiple orthogonal polynomials on an \(r\)-star*, arXiv:1804.07512 (first posted April 20, 2018), introduction and main polynomial formulas.
- T. Danka and V. Totik, *Christoffel functions with power type weights*, arXiv:1504.03968 (first posted April 15, 2015), Theorems 1.1 and 1.2.
- W. Van Assche, *Mehler–Heine asymptotics for multiple orthogonal polynomials*, arXiv:1408.6140 (first posted August 26, 2014), introduction, classical Jacobi hard-edge formula.
