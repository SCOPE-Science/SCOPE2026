# The nine-dimensional Boolean cube is the first Radau IIA fifth-order graph-heat positivity failure

## Finding

Let \(Q_d\) be the unweighted Boolean hypercube on \(\{0,1\}^d\), with the **combinatorial**, not normalized, Laplacian \(L_d=dI-A_d\). Let \(d\ge1\). Apply the standard three-stage, fifth-order Radau IIA method to the heat equation \(u'=-L_du\) and examine its **completed endpoint** matrix

\[
T_d(h)=F(hL_d),\qquad
F(x)=\frac{60-24x+3x^2}{60+36x+9x^2+x^3},\quad h\ge0.
\]

**Theorem.** For every integer \(1\le d\le8\), \(T_d(h)\) is entrywise nonnegative for every real \(h\ge0\), and is entrywise strictly positive for every \(h>0\). The first dimension admitting a negative endpoint entry is \(d=9\), where two vertices joined by an edge satisfy

\[
\bigl(T_9(1)\bigr)_{uv}=
-\frac{223660628942821971}{826114405977278306944}<0.
\]

Here “first” refers to the smallest dimension of an unweighted hypercube with **some** negative endpoint entry at **some** positive step. No claim is made for all dimensions greater than nine. Because \(F(0)=1\), every \(T_d(h)\) has row sums one, so the theorem determines when the endpoint map is a positive (stochastic) transition kernel in the stated range.

## Assumptions and scope

Every cube edge has weight one. \(Q_d\) has exactly \(2^d\) vertices and Laplacian eigenvalues \(2j\), \(j=0,\dots,d\), with multiplicity \(\binom dj\). The integer \(d\) is a graph dimension, not an ODE system dimension. The statement concerns the finished Radau IIA step, not its intermediate stages, and does not extend automatically to other graphs, directional weights, or time integrators. The value \(h\) is a nonnegative real number with no stepsize restriction.

## Proof

**1. Exact Fourier reduction.** For any subset \(S\subseteq\{1,\ldots,d\}\), the Walsh function \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\) is an orthogonal Laplacian eigenvector with eigenvalue \(2|S|\). Consequently the entry of \(T_d(h)\) between two vertices at Hamming distance \(k\) depends only on \(d,k\), and equals

\[
t_{d,k}(h)=\frac1{2^d}\sum_{j=0}^{d}K_{d,k}(j)
\frac{60-48jh+12j^2h^2}{60+72jh+36j^2h^2+8j^3h^3},
\]
\[
K_{d,k}(j)=\sum_{r=0}^{k}(-1)^r\binom{k}{r}\binom{d-k}{j-r},
\]

where a binomial coefficient outside its usual range is zero. This is an identity of rational functions, not a numerical approximation.

**2. Positive denominators and integer numerators.** Set

\[
D_j(h)=60+72jh+36j^2h^2+8j^3h^3,\qquad
N_j(h)=60-48jh+12j^2h^2
\]

for \(j=1,\ldots,d\), and put \(D_0=N_0=1\), which represents \(F(0)=1\). Define the integer polynomial

\[
P_{d,k}(h)=\sum_{j=0}^{d}K_{d,k}(j)N_j(h)
\prod_{\substack{1\le r\le d\\r\ne j}}D_r(h).
\]

Then for all real \(h\ge0\),

\[
t_{d,k}(h)=\frac{P_{d,k}(h)}{2^d\prod_{j=1}^{d}D_j(h)}.
\]

Every denominator factor is strictly positive. Thus exact coefficient sign certificates for the \(P_{d,k}\) establish positivity on the **entire** half-line.

**3. Finite exact positivity certificates.** The included `verify.py` and `CERTIFICATE.json` derive the coefficients solely from the two displayed formulas using integer addition and multiplication. For every pair \((d,k)\) with \(1\le d\le8\), \(0\le k\le d\), **except** \((8,1)\), every coefficient of \(P_{d,k}\) is nonnegative. Moreover, its coefficient of \(h^k\) is strictly positive and all coefficients of lower degree vanish when \(k>0\); the diagonal case has a strictly positive constant coefficient. This checks 43 full numerator polynomials, not a sample of timesteps.

The sole exception is \(P_{8,1}\), whose ordinary monomial expansion has negative coefficients but is still positive for every \(h>0\). Write \(P=P_{8,1}\), which has degree at most 24, and form the two *exact* integer polynomials

\[
A(t)=(1+t)^{24}P\!\left(\frac{t}{1+t}\right),\qquad
B(t)=P(1+t).
\]

The certificate checks that **all** coefficients of both \(A(t)\) and \(B(t)\) are nonnegative; \(A(t)>0\) for \(t>0\) and \(B(0)>0\). For \(0<h<1\), put \(t=h/(1-h)>0\), giving \(P(h)=A(t)/(1+t)^{24}>0\). For \(h\ge1\), put \(t=h-1\ge0\), giving \(P(h)=B(t)>0\). At \(h=0\), the distance-one entry vanishes, as required for the identity update. These two intervals cover every nonnegative real step.

This proves strict entrywise positivity in every dimension \(1\le d\le8\) for every positive step, and nonnegativity at zero. The certificate is finite only because the claimed safe dimensions form the explicitly bounded set \(\{1,\ldots,8\}\); it makes no extrapolation to arbitrary dimensions.

**4. Exact negative witness in dimension nine.** Substituting \(d=9\), \(k=1\), \(h=1\) into the same exact Fourier formula yields

\[
t_{9,1}(1)=-\frac{223660628942821971}{826114405977278306944},
\]

with strictly positive denominator. The included verifier independently evaluates this fraction both from the common-denominator polynomial and from the original finite Walsh spectral sum using exact rationals. Therefore dimension nine admits a negative endpoint entry, while every smaller positive dimension is safe for all steps. This completes the proof.

## Verification

All certificates are mathematical sign statements about explicit integer polynomials and hence certify infinitely many real steps in each of the **eight** safe dimensions. With Python 3 standard library only, run:

```bash
python verify.py CERTIFICATE.json
```

The verifier recomputes 44 numerator polynomials for dimensions one through eight, checks 43 full nonnegative-coefficient certificates, verifies the two transformed certificates for \((d,k)=(8,1)\), checks the exact negative fraction for \(Q_9\), and independently confirms it by the Walsh spectral sum. Its expected final line begins `VERIFY_OK 792` for the particular implementation supplied. The JSON certificate retains the coefficient arrays, so they can be checked separately without trusting floating-point output. Neither a numerical scan nor an unverified computer algebra oracle is used in the argument.

## Relationship to prior work

The classical stability and SSP literature distinguishes order, spectral stability and positive-cone preservation. Ketcheson, Macdonald and Gottlieb (2008/2009) establish general implicit SSP order barriers and state explicitly that classical multi-stage Radau IIA methods need not possess a positive unrestricted SSP radius; this does **not** determine endpoint positivity on a fixed family of self-adjoint graph Laplacians. Zappavigna, Colaneri, Kirkland and Shorten (2010) analyze positivity and Lyapunov properties of **diagonal** Padé discretizations of general Metzler systems; their sufficient thresholds and examples do not establish the off-diagonal \([2/3]\) Radau IIA hypercube classification. Gottlieb, Ketcheson and Shu (2008) survey high-order SSP schemes and the distinction between stability and convex/positivity properties.

Related graph-specific classifications for lower-order Radau IIA on Hamming graphs, for fourth-order Gauss on complete-graph Cartesian products, and for fifth-order Radau IIA on unweighted paths concern different rational functions or Laplacian spectra. In particular, the path order threshold does not imply a Boolean-cube dimension threshold. The new claim is the exact eight-dimensional all-step positivity certificate **and** the adjacent-pair negative witness in dimension nine for the fifth-order Radau IIA scheme.

## Limitations

No classification is claimed for cubes \(Q_d\) with \(d\ge10\), weighted cubes, or intermediate Runge–Kutta stages. The sign certificates are finite exact computations tied to the displayed algebraic identity, not a statement that any finite timestep grid is exhaustive. The novelty review compared relevant indexed material and inspected primary text, but unindexed or inaccessible equivalent results remain a possibility; independent mathematical and publication-priority review has not occurred.

## References

1. S. Gottlieb, D. I. Ketcheson, and C.-W. Shu, “High Order Strong Stability Preserving Time Discretizations,” *Journal of Scientific Computing* **38** (2009), 251–289, first published September 5, 2008. DOI: [10.1007/s10915-008-9239-z](https://doi.org/10.1007/s10915-008-9239-z).
2. D. I. Ketcheson, C. B. Macdonald, and S. Gottlieb, “Optimal Implicit Strong Stability Preserving Runge–Kutta Methods,” *Applied Numerical Mathematics* **59** (2009), 373–392. DOI: [10.1016/j.apnum.2008.03.034](https://doi.org/10.1016/j.apnum.2008.03.034). [Author postprint](https://www.davidketcheson.info/assets/papers/implicit_ssp_postprint.pdf).
3. A. Zappavigna, P. Colaneri, S. Kirkland, and R. N. Shorten, “On the Preservation of Co-positive Lyapunov Functions under Padé Discretization for Positive Systems,” MTNS 2010. [Open-access full text](https://mural.maynoothuniversity.ie/id/eprint/2195/).
