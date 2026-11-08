# Strict convexity and a detuning-monotone noise optimum for a middle-initialized quantum trimer

## Finding

A three-site coherent path with a detuned central site, initially excited at that site and trapped irreversibly at the right endpoint, has a unique best homogeneous dephasing rate. For a sink matched to the hopping strength, this optimum increases strictly with the magnitude of the central detuning. The entire mean-trapping-time curve is strictly convex, and the optimal dephasing is asymptotic to the detuning magnitude at large detuning.

With \(g=\gamma/J\), \(z=(\Delta/J)^2\), and \(\Theta=J\,\mathbb E[T]\), the exact formula is

\[
\Theta(g,z)=\frac72+g+\frac1{2g+1}+z\,\frac{2(2g^2+g+1)}{4g^3+4g^2+9g+2}.
\]

For every \(z\ge0\), there is precisely one global minimizer \(g_*(z)>0\), satisfying

\[
g_*(0)=\frac{\sqrt2-1}{2},\qquad \frac{d g_*}{dz}>0,\qquad \lim_{z\to\infty}\frac{g_*(z)}{\sqrt z}=1.
\]

## Assumptions and scope

The one-excitation space has orthonormal basis \(|1\rangle,|2\rangle,|3\rangle\). The Hamiltonian, site-dephasing and loss-only (no-click) generator are

\[
H=J(|1\rangle\langle2|+|2\rangle\langle1|+|2\rangle\langle3|+|3\rangle\langle2|)+\Delta|2\rangle\langle2|,
\]
\[
\mathcal L(\rho)=-i[H,\rho]+\gamma\sum_{j=1}^3\bigl(P_j\rho P_j-\tfrac12\{P_j,\rho\}\bigr)-\tfrac J2\{P_3,\rho\},
\]

where \(P_j=|j\rangle\langle j|\), and \(\rho(0)=P_2\). Rates satisfy \(J>0\), \(\gamma\ge0\), \(\Delta\in\mathbb R\). The dephasing normalization makes every off-diagonal element decay at the rate \(\gamma\) from dephasing alone. The terminal sink is fixed at the balanced extraction rate \(\kappa=J\). The capture time is the integral of the no-click survival probability, \(\mathbb E[T]=\int_0^\infty\operatorname{tr}(e^{t\mathcal L}P_2)\,dt\). The dimensionless parameters are \(g=\gamma/J\) and \(z=(\Delta/J)^2\).

## Proof

Scale time by \(J^{-1}\) and form the nine-dimensional real generator in the ordered coordinates consisting of the three populations, the real parts of coherences \(12,13,23\), and their imaginary parts. Solving the integrated master equation \(\mathcal L R=-P_2\) gives a unique solution and, on summing the first three components, yields the stated exact rational expression. Explicit independent linear-algebra construction and exact rational witnesses are provided in `verify.py`; a symbolic full-parameter inversion also gives exactly this rational formula. Denominators are positive because \(2g+1>0\) and \(Q(g)=4g^3+4g^2+9g+2>0\).

Set \(F(g)=2(2g^2+g+1)/Q(g)\). Direct differentiation gives

\[
F'(g)=-\frac{2(8g^4+8g^3-2g^2+7)}{Q(g)^2}<0,
\]

since \(8g^4+8g^3-2g^2+7>0\) for \(g\ge0\): on \([0,1/2]\), the constant dominates the negative term, while on \([1/2,\infty)\), \(8g^4\ge2g^2\). A second differentiation gives

\[
F''(g)=\frac{4(2g+3)P(g)}{Q(g)^3},\qquad P(g)=16g^5-36g^3+16g^2+6g+21.
\]

To prove \(P(g)>0\) globally, on \(0\le g\le3/2\) put \(g=3u/2\) with \(0\le u\le1\). The degree-five Bernstein coefficients of \(P(3u/2)\) are precisely \(21,114/5,141/5,501/20,6/5,66\), all positive. On \(g\ge3/2\), expanding \(P(3/2+u)\) in powers of \(u\ge0\) gives coefficients, in descending order, \(16,120,324,394,216,66\), again all positive. Hence \(F''(g)>0\).

Therefore \(\partial_g^2\Theta=8/(2g+1)^3+zF''(g)>0\) for all nonnegative \(g,z\). Furthermore \(\partial_g\Theta(0,z)=-1-7z/2<0\) and \(\partial_g\Theta(g,z)\to1\) as \(g\to\infty\), proving existence and uniqueness of a positive global minimizer. At \(z=0\), solving \(1-2/(2g+1)^2=0\) yields \(g_*(0)=(\sqrt2-1)/2\). Implicit differentiation of \(\partial_g\Theta(g_*(z),z)=0\) yields

\[
\frac{dg_*}{dz}=\frac{-F'(g_*)}{\partial_g^2\Theta(g_*,z)}>0.
\]

Because \(F'<0\) at every finite argument, the critical equation forces \(g_*(z)\to\infty\) as \(z\to\infty\). Finally, \(-F'(g)=g^{-2}(1+o(1))\) and \(1-2/(2g+1)^2=1+o(1)\); evaluating the critical equation at \(g=g_*(z)\) gives \(z/g_*(z)^2\to1\), establishing the asymptotic claim.

## Verification

Run `python verify.py` with Python, SymPy and NumPy. The checker independently constructs the nine-real-variable no-click generator, checks seven exact-rational mean-absorption witnesses, reconstructs a separate complex Liouvillian through Kronecker products at five points, proves the derivative identities and two polynomial positivity certificates symbolically, and numerically checks illustrative minimizers. The full-parameter generator inverse was also symbolically evaluated, giving zero difference from \(\Theta(g,z)\). These finite witnesses supplement, rather than replace, the analytic sign and uniqueness proof.

## Relationship to prior work

Zhang, Celardo, Borgonovi and Kaplan (2017), Section V, Eq. (33), give the mean trapping time from the **middle site of a clean trimer**; setting \(z=0\) in the formula here reproduces it, after matching dephasing, sink and coupling conventions. Their disorder-dependent short-chain analysis principally initializes at the first site, and their explicit middle-initialized expression assumes a clean chain. Contreras-Pulido, Bruderer, Huelga and Plenio (2014) analyze steady source-to-drain current in a dephased triple dot with input at the end; that source/detector renewal geometry is different from a single excitation initially in the central state. The contribution here is the detuned-middle-source formula and global convex/monotone optimization at matched extraction, not a claim to the underlying Lindblad formalism.

## Limitations

The extraction rate is fixed to \(J\); no theorem is claimed for arbitrary sink-to-hopping ratios, more than three sites, correlated noise, non-Markovian dephasing, or higher capture-time moments. The optimized observable is the **mean** capture time, not its variance or tail. The model assumes one excitation and an ideal absorbing sink. General published master equations could imply the rational formula through algebra; priority of the explicit global optimization should be checked independently before publication.

## References

1. Y. Zhang, G. L. Celardo, F. Borgonovi and L. Kaplan, *Optimal Dephasing for Ballistic Energy Transfer in Disordered Linear Chains*, arXiv:1706.09524 (first public 2017-06-29), https://arxiv.org/abs/1706.09524. Section V, Eq. (33).
2. L. D. Contreras-Pulido, M. Bruderer, S. F. Huelga and M. B. Plenio, *Dephasing-assisted transport in linear triple quantum dots*, arXiv:1407.0924 (first public 2014-07-03), https://arxiv.org/abs/1407.0924.
