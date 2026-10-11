# Renormalized half-flux band clusters for a preferred-orientation magnetic square quantum graph
## Finding
Consider the unit-edge magnetic square quantum graph with preferred-orientation vertex coupling and half a flux quantum per plaquette, \(\Phi=\pi\), as defined by Baradaran, Exner and Lipovský. Let \(H\) be its self-adjoint magnetic Laplacian, let \(N_n=n\pi\), and define the translated fixed-energy-window spectrum
\[
B_n=\big(\sigma(H)\cap[N_n^2-3,N_n^2+3]\big)-N_n^2.
\]
For all sufficiently large \(n\), \(B_n\) consists of exactly two bands. If their four ordered edges are \(e_{n,1}<e_{n,2}<e_{n,3}<e_{n,4}\), then
\[
\begin{aligned}
e_{n,1}&=-2\sqrt2+\frac{-2+4\sqrt2/3}{N_n^2}+O(N_n^{-4}),\\
e_{n,2}&=-2-\frac{1}{3N_n^2}+O(N_n^{-4}),\\
e_{n,3}&=2-\frac{5}{3N_n^2}+O(N_n^{-4}),\\
e_{n,4}&=2\sqrt2+\frac{-2-4\sqrt2/3}{N_n^2}+O(N_n^{-4}).
\end{aligned}
\]
Consequently,
\[
B_n\longrightarrow[-2\sqrt2,-2]\cup[2,2\sqrt2]
\]
in Hausdorff distance. Thus the narrow high-energy bands have a nontrivial universal local limit on the actual energy scale after recentering at \((n\pi)^2\), rather than merely shrinking on the momentum scale.

## Assumptions and scope
The graph, magnetic gauge class, edge length, coupling length scale, and half-flux normalization are exactly those of arXiv:2302.04601, Section 3.1. Energies are \(E=k^2>0\). The statement concerns only the two narrow bands in a fixed \(O(1)\) energy window around \((n\pi)^2\) as \(n\to\infty\); it does not describe the wide high-energy bands whose momentum distance from \(n\pi\) is order one.

## Proof
For \(\Phi=\pi\), the published band condition is
\[
-2\le R(k)\le2,
\]
where
\[
R(k)=\frac{-4k^2+(k^2-1)^2\cos(2k)-(k^2+1)^2\cos(4k)}{(k^2-1)^2\sin^2k}.
\]
Fix \(n\) and write
\[
k=N_n+\frac{x}{N_n}.
\]
Since \(2N_n\) and \(4N_n\) are integer multiples of \(2\pi\), direct Taylor expansion at fixed nonzero \(x\) gives, uniformly on compact sets avoiding \(x=0\),
\[
R\!\left(N_n+\frac{x}{N_n}\right)
=6-\frac{8}{x^2}
+\frac{1}{N_n^2}\left(-8x^2+\frac{88}{3}+\frac{16}{x}-\frac{16}{x^2}\right)
+O(N_n^{-4}).
\]
The leading band condition is therefore
\[
-2\le6-\frac{8}{x^2}\le2,
\]
which is equivalent to
\[
1\le|x|\le\sqrt2.
\]
Hence the two narrow bands have scaled momentum limits \([-\sqrt2,-1]\) and \([1,\sqrt2]\). The other high-energy band family in the source is characterized at leading order by \(-1\le\cos(2k)\le0\), so its distance in momentum from \(N_n\) is bounded below by a positive constant and it leaves every fixed translated energy window around \(N_n^2\) as \(n\to\infty\). Thus, for sufficiently large \(n\), the window defining \(B_n\) contains only the narrow pair.

To obtain the four edge corrections, set a band edge by \(R(k)=s\) with \(s\in\{-2,2\}\), and write
\[
x=x_0+\frac{a}{N_n^2}+O(N_n^{-4}).
\]
The leading roots are \(x_0=\pm1\) for \(s=-2\) and \(x_0=\pm\sqrt2\) for \(s=2\). Since the derivative of \(6-8/x^2\) is \(16/x^3\), the implicit-function expansion yields
\[
a=\frac{x_0(3x_0^4-11x_0^2-6x_0+6)}{6}.
\]
Finally,
\[
k^2-N_n^2=2x+\frac{x^2}{N_n^2},
\]
so substitution gives the four displayed energy-edge expansions. The nonzero derivative at each \(x_0\) also gives uniqueness of each nearby edge for all sufficiently large \(n\), and the band inequality fixes the ordering and the two-interval structure.

## Verification
The accompanying `artifacts/verify.py` evaluates the exact published function \(R(k)\), locates all four nearby solutions of \(R(k)=\pm2\) by bisection in the scaled variable \(x=N_n(k-N_n)\), and compares the exact translated energies against the four asymptotic formulas for several large \(n\). The residuals decrease with the predicted \(N_n^{-4}\) scale. This computation checks the expansion numerically; the proof above supplies the infinite-\(n\) argument.

## Relationship to prior work
Baradaran, Exner and Lipovský derive the exact half-flux spectral condition and state that the narrow high-energy pair has energy-band width \(2(\sqrt2-1)+O(n^{-2})\) for each band and intervening gap width \(4+O(n^{-2})\). They also show that these narrow bands contribute zero to the global momentum-band density. The present statement resolves the additional absolute location information that those width and gap estimates do not specify: after centering by \((n\pi)^2\), the entire local spectrum converges to two explicit compact intervals, with all four edges determined through the first nonzero correction.

The original preferred-orientation coupling paper explains the underlying time-reversal-breaking vertex condition and its high-energy parity behavior. Later work on preferred-orientation eigenvalue optimization concerns finite-graph eigenvalue bounds and does not provide this half-flux local periodic-band limit.

## Limitations
The result is specific to half flux, unit edge length, and the coupling length normalization used in the source. It does not claim the same limiting intervals for other rational fluxes. The originality search did not locate an equivalent local Hausdorff-limit statement, but terminology may differ in the magnetic-quantum-graph or almost-Mathieu literature. The proof relies on the exact published half-flux dispersion condition; it does not independently rederive the underlying \(8\times8\) Floquet determinant.

## References
1. M. Baradaran, P. Exner, J. Lipovský, *Magnetic square lattice with vertex coupling of a preferred orientation*, arXiv:2302.04601v1; Annals of Physics 454 (2023), 169339, DOI 10.1016/j.aop.2023.169339.
2. P. Exner, M. Tater, *Quantum graphs with vertices of a preferred orientation*, arXiv:1710.02664; Physics Letters A 382 (2018), 283–287.
3. P. Exner, J. Rohleder, *Optimization of quantum graph eigenvalues with preferred orientation vertex conditions*, arXiv:2410.21820.
