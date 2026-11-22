# The first global jump relocation in exponential Laguerre spectral approximation

## Finding

Equip the half-line with the exponential probability measure \(d\mu(x)=e^{-x}\,dx\). Let \(\Pi_n\) be the orthogonal projector in \(L^2(\mu)\) onto algebraic polynomials of degree at most \(n\), and define the sharp bounded-variation error
\[
C_n=\sup_{\operatorname{TV}(f)>0}\frac{\|(I-\Pi_n)f\|_{L^2(\mu)}}{\operatorname{TV}(f)}.
\]
The supremum is over real functions on \((0,\infty)\) with finite ordinary total variation. For each \(0\le n\le5\), there is a **unique** optimal jump location \(t_n>0\); every nonconstant norming function is \(f(x)=a+b\mathbf1_{[t_n,\infty)}(x)\), with \(b\ne0\), up to equality almost everywhere. The exact \(t_n\) and \(C_n\) are specified by the polynomials and isolated roots below.

Define ordinary Laguerre polynomials
\[
L_k(t)=\sum_{j=0}^{k}(-1)^j\binom{k}{j}\frac{t^j}{j!},\qquad
B_n(t)=1+\sum_{k=1}^{n}\bigl(L_k(t)-L_{k-1}(t)\bigr)^2,
\]
and \(Q_n(t)=B_n(t)-\tfrac12B'_n(t)\). Let \(\tau_{n,1}<\cdots<\tau_{n,m_n}\) be the *positive real solutions* of \(e^t=2Q_n(t)\). The exact number of solutions is \(m_n=1\) for \(0\le n\le2\), and \(m_n=3\) for \(3\le n\le5\). The unique global norming jump is
\[
\boxed{\quad t_n=\tau_{n,1}\quad(0\le n\le4),\qquad t_5=\tau_{5,3}.\quad}
\]
In every case,
\[
\boxed{\quad C_n^2=e^{-t_n}-e^{-2t_n}B_n(t_n).\quad}
\]
The complete certified finite-degree classification is:

| Degree \(n\) | Optimal jump \(t_n\) (approx.) | Sharp \(C_n^2\) (approx.) | Number of positive stationary locations |
|---:|---:|---:|---:|
| 0 | 0.693147180560 | 0.250000000000 | 1 |
| 1 | 0.415042743113 | 0.149192406785 | 1 |
| 2 | 0.301680174679 | 0.106928528670 | 1 |
| 3 | 0.238793082687 | 0.083492177871 | 3 |
| 4 | 0.198423667971 | 0.068546955691 | 3 |
| 5 | 0.840751437132 | 0.058221960053 | 3 |

At degree five, the earlier, near-boundary local maximum occurs at \(\tau_{5,1}\approx0.170163142423\) and has squared residual approximately \(0.058169765577\). The interior maximum at \(\tau_{5,3}\approx0.840751437132\) is **strictly larger**, by more than \(0.0000521944\) in squared error. Degrees zero through four have their unique global optimum on the first critical branch. Thus degree five is the **first global branch relocation** in this natural nested orthogonal projection family, despite the sharp norm itself strictly decreasing with degree.

## Assumptions and scope

Ordinary total variation is the variation measure mass on the *open* half-line, with endpoints excluded, so changing isolated point representatives is irrelevant. Finite-variation functions have bounded representatives, hence lie in \(L^2(\mu)\). Only real-valued functions are asserted. The Laguerre normalization used here makes \(\{L_k\}_{k\ge0}\) an orthonormal basis of \(L^2(e^{-x}dx)\); \(L_0=1\). The finite-degree statement is exactly for the six projection orders \(n=0,1,2,3,4,5\), not a claim about the first-branch behavior at every higher degree.

## Proof

**Step reduction.** Write \(h_t(x)=\mathbf1_{[t,\infty)}(x)\). Standard Laguerre integration identities give, for \(k\ge1\),
\[
\langle h_t,L_0\rangle_\mu=e^{-t},\qquad
\langle h_t,L_k\rangle_\mu=e^{-t}\bigl(L_k(t)-L_{k-1}(t)\bigr).
\]
Using orthogonality, \(\|h_t\|_{L^2(\mu)}^2=e^{-t}\), and Pythagoras,
\[
R_n(t):=\|(I-\Pi_n)h_t\|_{L^2(\mu)}^2
=e^{-t}-e^{-2t}B_n(t).
\]
If \(f\) has distributional derivative \(Df=\nu\), the Stieltjes representation is \(f(x)=a+\int_{(0,\infty)}h_t(x)\,d\nu(t)\) almost everywhere and \(\|\nu\|_{\rm TV}=\operatorname{TV}(f)\). The projector kills constants under \(I-\Pi_n\). Bochner integration and the triangle inequality show
\[
\|(I-\Pi_n)f\|_{L^2(\mu)}
\le \operatorname{TV}(f)\,\sup_{t>0}\sqrt{R_n(t)}.
\]
Each step realizes the lower bound. Since \(R_n(0)=\lim_{t\to\infty}R_n(t)=0\) and \(R_n(t)>0\) for \(t>0\), its maximum is attained at an interior stationary point. If the maximizing location is unique, equality forces \(\nu\) to be a multiple of the point mass there, yielding the asserted uniqueness of norming functions modulo constants.

**Polynomial-exponential critical equation.** Direct differentiation yields
\[
R'_n(t)=e^{-t}\bigl(2e^{-t}Q_n(t)-1\bigr),
\qquad
Q_n(t)=1+\sum_{k=1}^n\bigl(L_k(t)-L_{k-1}(t)\bigr)L_k(t).
\]
Thus every stationary point solves \(e^t=2Q_n(t)\). Put \(H_n(t)=e^{-t}Q_n(t)\), so
\[
H'_n(t)=e^{-t}A_n(t),\qquad A_n(t)=Q'_n(t)-Q_n(t).
\]
For \(n\ge1\), \(A_n\) is a polynomial of degree \(2n\). The certificate below isolates exactly \(2n\) distinct positive roots of \(A_n\) with rational sign-change intervals, exhausting all its complex roots by the degree bound. At these consecutive critical points, the rigorously enclosed signs of \(H_n-1/2\) are, in increasing order:

| \(n\) | Signs at the \(2n\) critical points of \(H_n\) |
|---:|:---|
| 0 | (no critical points) |
| 1 | \(-,-\) |
| 2 | \(-,-,-,-\) |
| 3 | \(-,+,-,-,-,-\) |
| 4 | \(-,+,-,-,-,-,-,-\) |
| 5 | \(-,+,-,-,-,-,-,-,-,-\) |

Because \(H_n(0)=1\), \(H_n(t)\to0\), and \(H_n\) is strictly monotone between its critical points, these signs prove that the stationary equation has exactly one or three positive roots as asserted. The certificate separately encloses every root in an explicit rational interval of width at most \(2\cdot10^{-11}\), establishes an opposite sign at the two endpoints, and computes rigorous disjoint intervals for all stationary residual values \(R_n\). The one-sided value intervals establish uniquely that the first root wins through degree four, while the third wins at degree five, including the strict quantitative margin. No numerical approximation or incomplete sampling is used to exhaust the critical points: exhaustion follows from the exact polynomial degree and rational sign changes.

**Why the certificate is exact.** The standalone `CHECK.py` constructs the polynomials over rational numbers, checks each polynomial identity, and uses only rational interval arithmetic. For \(0\le x<20\), it bounds the exponential using the Taylor polynomial \(S_{120}(x)=\sum_{j=0}^{120}x^j/j!\) and the provable remainder
\[
S_{120}(x)\le e^x\le S_{120}(x)+
\frac{x^{121}}{121!}\left(1-\frac{x}{122}\right)^{-1}.
\]
All critical-point and stationary-root intervals lie below 15. Every sign decision, exhaustion step and final strict value comparison uses these rational enclosures. This makes the finite-degree classification a finite, reproducible exact certificate rather than an extrapolation from floating-point experiments.

## Verification

Run `python3 CHECK.py` with a standard Python 3 implementation (no third-party packages required). The successful output ends with `LAGUERRE_EXACT_CERTIFICATE_PASSED 84`. This script performs 84 groups of exact-rational signed or interval calculations, including the 30 positive critical roots of the five derivative polynomials, comparisons against the threshold \(1/2\), all 12 positive stationary locations, and all stationary residual values. Independently, numerical quadrature at the six claimed global jumps reproduced the finite-term formula to floating-point precision. The analytical step reduction supplies the infinite-dimensional part; the exhaustive exact certificate supplies the finite algebraic-transcendental comparison. Finite grids or numerical quadrature are not used as proofs of global optimality.

## Relationship to prior work

Tang and Zhou (arXiv:1403.6579v1, 2014) treat exponential/Gamma Laguerre polynomial-chaos expansion and stability of discrete least-squares sampling. Their original article's introduction, §§2–3 and conclusions were inspected; in particular equation (2.20) uses the exponential Laguerre basis, but their objective is randomized sampling stability and scaling rather than the sharp continuous \(BV\)-to-\(L^2\) orthogonal truncation norm or its maximizing jump geometry. The published finding *A hard-edge transition for sharp generalized Laguerre bounded-variation coefficients* treats the norm of an **individual** coefficient and provides a single-coefficient envelope. Its complete statement and proof were read: an optimal bound on one coefficient does not determine the joint squared residual of *all* coefficients beyond a cutoff, and its extremizer classification does not imply the present displacement at degree five. The classical Laguerre identities and the variation-to-step reduction are ingredients, not claims of novelty. Earlier sharp residual results for Hermite, Legendre, Chebyshev and Walsh systems use different measures or orthogonal systems, and no implication transferring their exact optimizers to the exponential Laguerre setting was identified.

## Limitations

The degree-five winner exceeds the alternative local maximum by a small but strictly certified amount. The result makes no claim about the number of stationary points, global jump location, or asymptotic rate at degrees greater than five; it also does not extend the conclusion to generalized Laguerre weights, alternative normalizations, nonlinear approximation or complex-valued variation. Priority remains subject to possible unindexed equivalent results. Independent mathematical auditing has not been performed.

## References

- T. Tang and T. Zhou, *On discrete least square projection in unbounded domain with random evaluations and its application to parametric uncertainty quantification*, arXiv:1403.6579v1, first posted 2014-03-26, https://arxiv.org/abs/1403.6579 .
- *A hard-edge transition for sharp generalized Laguerre bounded-variation coefficients*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-hard-edge-transition-for-sharp-generalized-laguerre-bounded-va--e0cc28c7853e .
- NIST Digital Library of Mathematical Functions, §18.18 (Laguerre expansions and orthogonality), https://dlmf.nist.gov/18.18 .
