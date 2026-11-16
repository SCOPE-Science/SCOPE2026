# Rational-radius geodesic-cap averages on the three-sphere have exactly one exceptional radius

## Finding
Let \(S^3\subset\mathbb R^4\) carry surface-area measure. If \(0<\theta<\pi\) and \(\theta/\pi\) is rational, the normalized geodesic-cap averaging map \(A_\theta:L^2(S^3)\to L^2(S^3)\) is injective exactly when \(\theta\ne\pi/2\). At \(\theta=\pi/2\), the kernel is the orthogonal sum of every positive even-degree spherical-harmonic space. No nonzero odd-degree harmonic lies in the kernel. Thus a single exceptional rational cap radius creates an infinite-dimensional spectral blind space.

## Assumptions and scope
For \(x\in S^3\), define \(C_\theta(x)=\{y\in S^3: \arccos(x\cdot y)\le\theta\}\) and \((A_\theta f)(x)=\operatorname{area}(C_\theta(x))^{-1}\int_{C_\theta(x)}f(y)\,d\sigma(y)\). All functions are complex-valued \(L^2\); harmonic degrees \(\ell\) are nonnegative integers. The classification assumes \(0<\theta<\pi\) and \(\theta/\pi\in\mathbb Q\), and makes no assertion for irrational angles. The endpoints are excluded: the zero-radius limit is the identity, while the whole-sphere limit is projection onto constants.

## Proof
**Harmonic multipliers.** By rotation invariance and the zonal harmonic formula on \(S^3\), the normalized degree-\(\ell\) zonal value at angular separation \(t\) is \(\sin((\ell+1)t)/((\ell+1)\sin t)\), and the radial volume density is proportional to \(\sin^2t\). Put \(V(\theta)=\int_0^\theta\sin^2t\,dt=\theta/2-\sin(2\theta)/4>0\). For \(\ell\ge1\),
\[
\lambda_\ell(\theta)=\frac{\int_0^\theta \sin((\ell+1)t)\sin t\,dt}{(\ell+1)V(\theta)}=\frac{\sin(\ell\theta)/\ell-\sin((\ell+2)\theta)/(\ell+2)}{2(\ell+1)V(\theta)}.
\]
The constant multiplier is \(\lambda_0=1\).

**Arithmetic reduction.** Set \(n=\ell+1\ge2\) and \(z=e^{2i\theta}\). The multiplier vanishes precisely when
\[
(n+1)\sin((n-1)\theta)-(n-1)\sin((n+1)\theta)=0,
\]
or equivalently
\[
P_n(z)=(n-1)z^{n+1}-(n+1)z^n+(n+1)z-(n-1)=0.
\]
Rationality of \(\theta/\pi\) makes \(z\) a root of unity. The four displayed terms have nonzero rational coefficients. If the vanishing relation has a nonempty proper zero subsum, it must split into two two-term relations. Equal absolute coefficients must pair; because \(n-1\ne n+1\), these pairs are the two \(n-1\) terms and the two \(n+1\) terms. Thus \(z^{n+1}=z^{n-1}=1\), so \(z^2=1\).

Otherwise the four-term relation is irreducible. Mann's root-of-unity relation theorem says that the ratio of any two roots occurring in an irreducible rational relation of length four has order dividing the product of primes at most four, namely six. Because the roots \(1\) and \(z\) both occur, the order of \(z\) divides six. Consequently in either case a zero multiplier can arise only for a root of unity of order \(1,2,3\), or \(6\).

For order one, \(z=1\) forces \(\theta=0\) or \(\pi\), excluded. For order two, \(z=-1\), substitution gives \(P_n(-1)=0\) exactly when \(n\) is odd. For primitive order three, reduction modulo \(z^2+z+1\) of \(P_n\), for residues \(n\bmod3=0,1,2\), yields respectively \(2n(z-1)\), \(-(n-1)(z+2)\), and \((n+1)(2z+1)\), none zero for \(n\ge2\). For primitive order six, use \(z^2-z+1=0\); the residues \(n\bmod6=0,1,2,3,4,5\) give respectively \(2n(z-1)\), \((n-1)(z-2)\), \(3-n\), \(2(z+1)\), \((n+3)z\), and \((n+1)(2z-1)\). In the third residue \(n\equiv2\pmod6\), \(3-n\ne0\); every other expression is likewise nonzero. Therefore only \(z=-1\) with odd \(n\) survives; equivalently \(\theta=\pi/2\) and positive even \(\ell\).

**Operator conclusion.** Spherical harmonics of all degrees form a complete orthogonal Hilbert decomposition. Every multiplier except those identified is nonzero, proving the full kernel and injectivity claims. Finally, for any fixed \(0<\theta<\pi\), the explicit multiplier expression is \(O_\theta(\ell^{-2})\); since arbitrarily large degrees exist, an injective \(A_\theta\) cannot be bounded below and has no bounded inverse on its range with the inherited \(L^2\) norm.

## Verification
The bundled `verify_cap.py` checks the exact cyclotomic reductions for all four relevant root orders, the elementary pair-decomposition boundary, and independent high-precision integral formulas across many rational angles and harmonic degrees. These tests support but do not replace the universal argument using Mann's theorem. The dimension-three normalization follows from \(\int_0^\theta\sin^2t\,dt\).

## Relationship to prior work
Schär and Stier (first public September 16, 2023) study a geodesic random walk with an angle-randomized transition law on spheres, using Wasserstein contraction; their transition law is not uniform cap averaging, and their theorems do not give the rational-radius kernel classification. Mann's 1965 result and Evertse's 1999 account provide the general arithmetic input about irreducible root-of-unity relations. The specialized result here is the application of that input to *all* spherical-harmonic cap multipliers on \(S^3\), and the exact classification of its exceptional rational radius. No claim is made about irrational-angle kernels, stability of inversion, or historical priority beyond the literature actually examined.

## Limitations
The operator is compact and ill-conditioned even at every injective angle. The novelty assessment is based on accessible sources and mathematical implication checks, not a proof of absence from all earlier literature. Specialized spherical mean-transform literature may contain equivalent statements and requires independent priority review.

## References
1. P. Schär and T. D. Stier, *A Dimension-Independent Bound on the Wasserstein Contraction Rate of a Geodesic Random Walk on the Sphere*, arXiv:2309.09097, first submitted September 16, 2023. https://arxiv.org/abs/2309.09097
2. H. B. Mann, *On linear relations between roots of unity*, Mathematika 12 (1965), 107–117. https://doi.org/10.1112/S0025579300005210
3. J.-H. Evertse, *The number of solutions of linear equations in roots of unity*, Acta Arithmetica 89 (1999), 45–51. https://doi.org/10.4064/aa-89-1-45-51
