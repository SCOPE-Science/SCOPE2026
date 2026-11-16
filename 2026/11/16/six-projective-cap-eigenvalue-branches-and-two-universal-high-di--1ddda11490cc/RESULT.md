# Six projective cap eigenvalue branches and two universal high-dimensional transitions

## Finding

Let \(d\ge3\) be an integer, let \(X=\mathbb{CP}^{d-1}\) carry normalized invariant measure, and let \(\mathcal H_2\) be the second nonconstant Laplace eigenspace, equivalently the restrictions of bihomogeneous harmonic polynomials of bidegree \((2,2)\) on \(\mathbb C^d\). For \(0<t<1\), define the geodesic cap
\[
C_t=\{[u]\in X:|u_1|^2\ge t\},\qquad \|u\|=1,
\]
and the self-adjoint concentration operator \(T_{d,t}=\Pi_{\mathcal H_2}\mathbf1_{C_t}|_{\mathcal H_2}\). Its entire spectrum, with multiplicities, consists of the six rows below. Write \(q=1-t\) and \(n=d-1\).

| Type \((p,r)\) and its conjugate | Eigenvalue \(\lambda_{pr}\) | Total multiplicity |
|---|---|---|
| \((0,0)\) | \(q^{d-1}Q_{00}\) | \(1\) |
| \((1,0),(0,1)\) | \(q^d Q_{10}\) | \(2n\) |
| \((1,1)\) | \(q^{d+1}Q_{11}\) | \(n^2-1\) |
| \((2,0),(0,2)\) | \(q^{d+1}Q_{20}\) | \(n(n+1)\) |
| \((2,1),(1,2)\) | \(q^{d+2}Q_{21}\) | \(n(n-1)(n+2)\) |
| \((2,2)\) | \(q^{d+3}\) | \(n^2(n-1)(n+3)/4\) |

Here, with all polynomials evaluated at \(t\),
\[
\begin{aligned}
Q_{00}(t)&=1-4t+(2d^2+6d+6)t^2-(d+1)^2(d+4)t^3+\tfrac14(d+1)^2(d+2)^2t^4,\\
Q_{10}(t)&=1+dt-\tfrac12(d+1)(d+6)t^2+\tfrac12(d+1)(d+2)^2t^3,\\
Q_{11}(t)&=1-2t+(d+2)^2t^2,\\
Q_{20}(t)&=1+(d+1)t+\tfrac12(d+1)(d+2)t^2,\\
Q_{21}(t)&=1+(d+2)t.
\end{aligned}
\]
All six displayed branches are counted with their stated multiplicities, even if two eigenvalues coincide at a particular cap height. The smallest eigenvalue is always \(\lambda_{22}=q^{d+3}\), strictly below every other branch for \(0<t<1\). In particular, every positive-volume geodesic cap yields injective restriction on \(\mathcal H_2\).

There is a universal fixed-cap-volume limit. Fix \(v\in(0,1)\), put \(s=\log(1/v)\), and choose \(t=t_d=1-v^{1/(d-1)}\), so that \(\operatorname{vol}(C_{t_d})=v\). The sharp squared condition number \(\kappa_d(v)=\lambda_{\max}(T_{d,t_d})/\lambda_{\min}(T_{d,t_d})\) satisfies
\[
\boxed{\lim_{d\to\infty}\kappa_d(v)=\mathcal M(s)},\qquad
\mathcal M(s)=\begin{cases}
1+s+\tfrac12s^2,&0<s\le2,\\
1+s-\tfrac12s^2+\tfrac12s^3,&2\le s\le2+\sqrt2,\\
1+2s^2-s^3+\tfrac14s^4,&s\ge2+\sqrt2.
\end{cases}
\]
The first limiting crossover at \(s=2\) is a four-sector collision of the \((0,0),(1,0),(1,1),(2,0)\) eigenvalue branches; the second, at \(s=2+\sqrt2\), is between the \((1,0)\) and \((0,0)\) branches. These are limiting collisions, not assertions that finite-dimensional eigenvalues coincide exactly at those parameter values.

## Assumptions and scope

The Fubini–Study metric is normalized so that \(\operatorname{dist}([u],[e_1])=\arccos|u_1|\). The Haar probability measure on projective space is induced from the unit sphere in \(\mathbb C^d\). The space \(\mathcal H_2\) has complex dimension \(\binom{d+1}{2}^2-d^2\). No other Laplacian degrees are included. All measures and inner products are complex \(L^2\) ones, and \(\kappa\) denotes an eigenvalue ratio (squared frame condition number).

## Proof

**1. Branching and diagonalization.** Decompose \(u=(z,w)\in\mathbb C\oplus\mathbb C^n\), with \(x=|z|^2\). For each \(0\le p,r\le2\), let \(H_{p,r}(\mathbb C^n)\) be the complex-harmonic bihomogeneous polynomials in \(w,\bar w\) of bidegree \((p,r)\). Under \(U(1)\times U(n)\), the restriction of \(\mathcal H_2\) decomposes without multiplicity into these nine angular types. The corresponding separated functions on the unit sphere are proportional to
\[
 z^{(r-p)_+}\bar z^{(p-r)_+}H(w)P_{2-\max(p,r)}^{(p+r+d-2,\,|p-r|)}(2x-1),
\quad H\in H_{p,r}(\mathbb C^n),
\]
where \(P_j^{(\alpha,\beta)}\) is the standard Jacobi polynomial. This follows directly from separation of the complex harmonic equation (or the harmonic projection of \(z^{2-p}\bar z^{2-r}H(w)\)). Distinct types are inequivalent irreducible \(U(1)\times U(n)\)-modules, so the cap operator acts as a scalar on each type.

The squared modulus of each separated function, after integrating all angular variables, has radial density proportional to
\[
 x^{b}(1-x)^a\bigl[P_j^{(a,b)}(2x-1)\bigr]^2dx,
\quad a=p+r+d-2,\quad b=|p-r|,\quad j=2-\max(p,r).
\]
Consequently, its concentration eigenvalue is exactly
\[
\lambda_{pr}(t)=
\frac{\int_t^1 x^b(1-x)^a[P_j^{(a,b)}(2x-1)]^2\,dx}
{\int_0^1 x^b(1-x)^a[P_j^{(a,b)}(2x-1)]^2\,dx}.
\tag{1}
\]
The Jacobi norm denominator equals
\[
\frac{\Gamma(j+a+1)\Gamma(j+b+1)}{(2j+a+b+1)j!\Gamma(j+a+b+1)}.
\]
As \(j\le2\), evaluation of (1) gives precisely the six polynomial expressions in the finding. The accompanying checker establishes the exact derivative identities for symbolic \(d\), and separately integrates the densities at exact rational cap heights for \(3\le d\le8\). The proof itself is the Jacobi identity and integral (1), not the finite replay.

The angular dimensions are
\[
\dim H_{p,r}(\mathbb C^n)=
\binom{n+p-1}{p}\binom{n+r-1}{r}
-\binom{n+p-2}{p-1}\binom{n+r-2}{r-1},
\]
where the second product is zero when \(pr=0\). Their nine-type sum is \(\binom{d+1}{2}^2-d^2\), proving completeness and the stated multiplicities. As an additional independent consistency identity, the multiplicity-weighted sum of the six eigenvalues equals \(\operatorname{vol}(C_t)\dim\mathcal H_2\), since the invariant reproducing kernel has constant diagonal; the exact polynomial table satisfies this identity.

**2. Sharp smallest branch.** Divide every eigenvalue by \(q^{d-1}\). The \((2,2)\) branch becomes \(q^4\). For the other types, the differences from \(q^4\) are, respectively,
\[
\begin{aligned}
\Delta_{00}&=\tfrac14d(d+3)t^2[(d^2+3d+4)t^2-4(d+3)t+8],\\
\Delta_{10}&=\tfrac12(d+3)tq[(d^2+2d+2)t^2-(d+4)t+2],\\
\Delta_{11}&=(d+1)(d+3)t^2q^2,\\
\Delta_{20}&=\tfrac12(d+3)tq^2(dt+2),\\
\Delta_{21}&=(d+3)tq^3.
\end{aligned}
\]
Both quadratic brackets have positive leading coefficients and negative discriminants, respectively \(16(1-d^2)\) and \(-7d^2-8d\). Thus every difference is positive for \(d\ge3\), \(0<t<1\), proving the strict spectral minimum and injectivity.

**3. Fixed-volume limit.** For fixed \(s>0\), \(dt_d\to s\) and \(q_d^{d-1}=e^{-s}\). After dividing by \(v\), the six branches converge in the row order above to
\[
 A(s)=1+2s^2-s^3+\tfrac14s^4,\quad
 B(s)=1+s-\tfrac12s^2+\tfrac12s^3,\quad
 C(s)=1+s^2,\quad
 D(s)=1+s+\tfrac12s^2,\quad
 E(s)=1+s,\quad F(s)=1.
\]
The smallest limit is \(F=1\). Exact polynomial differences are
\[
\begin{aligned}
A-C&=\tfrac14s^2(s-2)^2,\\
D-A&=-\tfrac14s(s-2)(s^2-2s+2),\\
D-B&=-\tfrac12s^2(s-2),\\
D-C&=-\tfrac12s(s-2),\\
D-E&=\tfrac12s^2,\\
B-A&=-\tfrac14s(s-2)(s^2-4s+2).
\end{aligned}
\]
For \(0<s<2\), \(D\) strictly dominates all remaining branches. For \(s>2\), either \(A\) or \(B\) dominates, because \(A\ge C\), and both dominate \(D\), while \(D\ge E,F\). The sign of \(B-A\) selects \(B\) for \(2<s<2+\sqrt2\) and \(A\) for \(s>2+\sqrt2\). The equalities at the two stated cutoffs give the limiting sector collisions. This proves the piecewise sharp condition-number law.

## Verification

Run `python cp2_cap_verify.py` with SymPy installed. It checks the six symbolic Jacobi derivative identities (valid for symbolic \(d\)), the identity for the complete dimension count, all factorizations used in the strict-minimum and high-dimensional envelope proofs, and independent rational-polynomial integration for dimensions \(3\) through \(8\) at three cap heights. The recorded output is:

```
CP2_SIX_JACOBI_BRANCHES_EXACT_PASS
CP2_MULTIPLICITIES_AND_STRICT_MINIMUM_PASS
CP2_FIXED_VOLUME_TWO_TRANSITIONS_PASS
CP2_DIRECT_EXACT_BETA_INTEGRALS_PASS dimensions=3..8
```

## Relationship to prior work

Jaming and Speckbacher, *Concentration estimates for finite expansions of spherical harmonics on two-point homogeneous spaces via the large sieve principle* (2020), establish general large-sieve estimates and Jacobi-zonal harmonic machinery on spaces including complex projective spaces. Their Theorem 4.4 is an upper-bound inequality and does not provide a complete spectrum of the second projective eigenspace on a cap. Simons, Dahlen and Wieczorek (2006) treat Slepian localization on real spheres, not the stated complex-projective six-branch and fixed-volume two-transition problem. Standard Jacobi branching, Beta integrals, and the trace-free polynomial description are background, not claimed as new in isolation. The assessed claim is their complete specialization together with a global exact spectral minimum and the explicit high-dimensional two-transition condition-number law.

## Limitations

The theorem is restricted to the second **single** nonconstant Laplace eigenspace on \(\mathbb{CP}^{d-1}\), complex dimensions at least two, and a single geodesic cap. It does not give finite-dimensional exact crossover parameters for the largest eigenvalue, nor spectra for sums of distinct Laplace eigenspaces. The two transition points are high-dimensional fixed-volume limits. Historical priority is not certified: an equivalent formula might be obtainable from earlier, differently named branching or integral-operator work.

## References

1. P. Jaming and M. Speckbacher, *Concentration estimates for finite expansions of spherical harmonics on two-point homogeneous spaces via the large sieve principle*, arXiv:2004.02474v1 (first public 2020-04-06), https://arxiv.org/abs/2004.02474 .
2. F. J. Simons, F. A. Dahlen and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, SIAM Review **48** (2006), 504–536, doi:10.1137/S0036144504445765.
