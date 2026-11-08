# A universal positive Lebesgue-norm penalty for fixed Fourier frequency deletions

## Finding

Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), equipped with normalized Haar measure \(dm(t)=dt/(2\pi)\). For every nonempty finite \(F\subset\mathbb Z\), define the ordinary symmetric Fourier projection \(S_n\) and the punctured projection \(Q_{n,F}\) on \(C(\mathbb T)\):

\[
S_nf(x)=\sum_{|k|\le n}\widehat f(k)e^{ikx},\qquad
Q_{n,F}f(x)=\sum_{\substack{|k|\le n\\k\notin F}}\widehat f(k)e^{ikx},
\qquad n\ge\max_{k\in F}|k|.
\]

Write \(D_n(t)=\sum_{|k|\le n}e^{ikt}=\sin((n+1/2)t)/\sin(t/2)\) for \(t\ne0\), and \(h_F(t)=\sum_{k\in F}e^{ikt}\). Then the positive finite limit

\[
\lim_{n\to\infty}\big(\|Q_{n,F}\|_{C\to C}-\|S_n\|_{C\to C}\big)=\mathcal C(F)>0
\]

exists for **every fixed, nonempty frequency deletion**. The exact constant is the absolutely controlled, phase-averaged integral

\[
\mathcal C(F)=\frac1{(2\pi)^2}\int_{-\pi}^{\pi}\int_0^{2\pi}
\left(\left|\frac{\sin u}{\sin(t/2)}-h_F(t)\right|-
\left|\frac{\sin u}{\sin(t/2)}\right|\right)\,du\,dt.
\]

At \(t=0\), any assigned integrand value is immaterial: its magnitude is bounded by \(|h_F(t)|\). In particular, **removing the mean** gives the explicit asymptotic increase

\[
\boxed{\lim_{n\to\infty}\big(\|Q_{n,\{0\}}\|_{C\to C}-\|S_n\|_{C\to C}\big)
=\frac12-\frac{4\log 2}{\pi^2}=0.2190780289\ldots>0.}
\]

The asymptotic formula remains valid, and its limit is strictly positive, if the trigonometric polynomial \(h_F\) is replaced by any fixed nonzero continuous complex-valued perturbation \(h\) of the Dirichlet kernel; the operator interpretation applies specifically to frequency deletions.

## Assumptions and scope

All functions are complex-valued. The frequency deletion \(F\) is independent of \(n\), finite and nonempty; \(n\) is any integer sufficiently large to contain it. No symmetry or conjugate pairing is imposed on \(F\). The norm \(\|\cdot\|_{C\to C}\) is the operator norm induced by the supremum norm on continuous functions. The conclusion asserts eventual positivity, not monotonicity in \(n\) or positivity at every finite \(n\).

## Proof

**Step 1: identify the sharp operator norms.** Convolution with the continuous kernels \(D_n\) and \(D_n-h_F\) represents \(S_n\) and \(Q_{n,F}\), respectively. On \(C(\mathbb T)\), convolution with a continuous complex-valued kernel \(K\) has sharp norm \(\int|K|\,dm\): the upper bound is immediate; the reverse bound follows by approximating the complex sign of \(K(-t)\) in \(L^1(|K|\,dm)\) by continuous functions bounded in modulus by one and evaluating the convolution at the origin. Hence

\[
\|Q_{n,F}\|-\|S_n\|=\int_{-\pi}^{\pi}
\big(|D_n(t)-h_F(t)|-|D_n(t)|\big)\,dm(t).
\]

**Step 2: an oscillatory-averaging lemma without singularity loss.** More generally, fix any continuous \(h:\mathbb T\to\mathbb C\). Put \(a(t)=1/\sin(t/2)\), away from \(t=0\), and

\[
G(t,u)=|a(t)\sin u-h(t)|-|a(t)\sin u|.
\]

The reverse triangle inequality gives \(|G(t,u)|\le |h(t)|\) uniformly in \(u\), even when \(t\to0\). On \(E_\varepsilon=[-\pi,-\varepsilon]\cup[\varepsilon,\pi]\), the function \(G\) is continuous and periodic in \(u\), so its \(u\)-dependence is uniformly approximated by trigonometric polynomials with continuous \(t\)-coefficients. For each nonconstant angular harmonic, the Riemann--Lebesgue lemma makes its integral at \(u=(n+1/2)t\) tend to zero. The constant angular coefficient survives. Both the original and averaged integrals over \(|t|<\varepsilon\) have absolute value at most \(2\varepsilon\|h\|_\infty/(2\pi)\). First let \(n\to\infty\), then \(\varepsilon\downarrow0\). This proves the displayed exact limit, including the case \(h=h_F\).

**Step 3: strict positivity.** For each fixed \(t\ne0\) and \(x=a(t)\sin u\in\mathbb R\), the paired phases \(u\) and \(u+\pi\) give

\[
|x-h(t)|+|-x-h(t)|-2|x|\ge0,
\]

because the first two moduli sum to at least the distance \(2|x|\) between their arguments. If \(h(t)\ne0\), then for every \(u\) with \(|a(t)\sin u|<|h(t)|/2\), the sum exceeds \(2|x|\) strictly: it is at least \(2|h(t)|>2|x|\). Such phases have positive measure. Consequently the angular average is strictly positive wherever \(h(t)\ne0\). A nonzero continuous \(h\) is nonzero on an open set, proving positivity of the integrated limit. Since \(h_F\) is a nonzero trigonometric polynomial for nonempty \(F\), the claimed positive constant follows.

**Step 4: central deletion.** Let \(h\equiv1\), and on \(t\in(0,\pi]\) set \(a=1/\sin(t/2)\ge1\). Splitting the angular integral at \(\sin u=1/a\) gives the elementary identity

\[
\frac1{2\pi}\int_0^{2\pi}\big(|a\sin u-1|-|a\sin u|\big)du
=\frac2\pi\big(\sqrt{a^2-1}-a+\arcsin(1/a)\big)
=\frac2\pi\big(t/2-\tan(t/4)\big).
\]

The integrand is even in \(t\), so

\[
\mathcal C(\{0\})=\frac2{\pi^2}\int_0^\pi(t/2-\tan(t/4))\,dt
=\frac2{\pi^2}\left(\frac{\pi^2}4-2\log2\right)
=\frac12-\frac{4\log2}{\pi^2}.
\]

All manipulations are justified by the uniform bound \(|G|\le1\) and elementary one-dimensional integration. This proves the theorem.

## Verification

The enclosed standard-library Python checker numerically integrates the kernel differences for several increasing indices and independently integrates the explicit angular-average formula for central deletion. It also samples genuinely complex one-frequency deletions and compares the direct kernel form with the Fourier sum. Its finite numerical checks are corroboration only: existence, strict positivity, all complex perturbations, and the exact constant are proved above without finite sampling.

Run: `python3 checks/notch_lebesgue.py`. No external packages or datasets are necessary.

## Relationship to prior work

Kolomoitsev and Liflyand (first public arXiv version 2020-04-25; primary MSC 42B05, 42B08, 42A05) prove asymptotics for Lebesgue constants of anisotropically dilated **multidimensional simplex** Fourier bands (dimension at least two). Their main theorem gives large-cutoff expansions for full simplex supports, not the fixed finite deletion of a one-dimensional symmetric Fourier interval. The classical Lebesgue constant is precisely the \(L^1\) norm of the complete Dirichlet kernel, and its leading logarithmic growth and exact full-block formulas are standard. Ortigueira and Bengochea (preprint publicly posted 2024-05-27, later Axioms 2024) give exact formulas and asymptotics for **unmodified** Dirichlet norms. In particular, their section 4 uses an integral of \(D_n-1\) to represent a partial sine series; this is **not** the \(L^1\) norm of \(D_n-1\) and does not establish the present positive notch penalty. Álvarez and Guzmán-Partida discuss bounds and behavior of the ordinary Dirichlet kernel. The new object is the **difference of two sharp endpoint projection norms after fixed spectral deletion**, including its full angular-average functional and explicit constant for the missing zero frequency. Existing formulas for unmodified Lebesgue constants do not by themselves determine this difference.

## Limitations

The deletion set is fixed as \(n\to\infty\); growing deletion sets and endpoint norms on finite cyclic groups are not covered. The theorem does not give a universal finite cutoff for the sign of the norm difference, an error term, or a closed elementary expression for every multisite deletion. Novelty comparison cannot exclude a differently named earlier specialized calculation of \(\|D_n-1\|_1-\|D_n\|_1\); independent bibliographic review remains appropriate.

## References

1. Yu. Kolomoitsev and E. Liflyand, *Asymptotics of the Lebesgue Constants for a d-Dimensional Simplex*, arXiv:2004.12236v1, first posted 2020-04-25; *Proc. Amer. Math. Soc.* 149 (2021), 2911–2926, doi:10.1090/proc/15438.
2. M. D. Ortigueira and G. Bengochea, *On the Lebesgue Constants*, preprint posted 2024-05-27, https://www.preprints.org/manuscript/202405.1746; peer-reviewed publication *Axioms* 13 (2024), 505, doi:10.3390/axioms13080505.
3. J. Álvarez and M. Guzmán-Partida, *Properties of the Dirichlet Kernel*, *Electronic Journal of Mathematical Analysis and Applications* 11 (2023), 96--110.
4. E. M. Stein and R. Shakarchi, *Fourier Analysis: An Introduction*, Princeton University Press (2003), standard Fourier convolution and Dirichlet-kernel facts.
