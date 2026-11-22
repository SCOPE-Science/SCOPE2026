# Two-scale singular spectra of coalescing Fock composition sums

## Finding

Distinct radial Gaussian-Fock composition operators obey a complete two-scale singular-spectrum law when their symbols coalesce. A finite-difference cancellation of order \(m\) determines the sharp small-separation decay when the baseline contraction is stronger than the separation, whereas an exponential-polynomial profile determines all positive Schatten exponents, operator norms, and positive-level spectral counting when contraction and separation have comparable scales.

Precisely, with the definitions below and \(\delta,\varepsilon\downarrow0\), if \(\delta/\varepsilon\to\tau\in[0,\infty)\), then

\[
\varepsilon\|T_{\delta,\varepsilon}\|_{\mathcal S_p}^{p}\longrightarrow\int_0^\infty e^{-p\tau x}|F(x)|^p\,dx,\qquad
\|T_{\delta,\varepsilon}\|\longrightarrow\sup_{x\ge0}e^{-\tau x}|F(x)|.
\]

Also, for every \(s>0\), the positive-level singular-value counting law is

\[
\varepsilon\#\{k:s_k(T_{\delta,\varepsilon})>s\}\longrightarrow
\big|\{x\ge0:e^{-\tau x}|F(x)|>s\}\big|,
\]

where \(|\cdot|\) on a set denotes its Lebesgue measure, and singular values are counted with multiplicity. In the separated regime \(\varepsilon/\delta\to0\),

\[
\frac{\delta^{mp+1}}{\varepsilon^{mp}}\|T_{\delta,\varepsilon}\|_{\mathcal S_p}^{p}
\longrightarrow A_m^p\frac{\Gamma(mp+1)}{p^{mp+1}},
\]

and \((\delta/\varepsilon)^m\|T_{\delta,\varepsilon}\|\to A_m(m/e)^m\) if \(m\ge1\); when \(m=0\), the last limit is \(A_0\) without rescaling.

## Assumptions and scope

The standard Gaussian Fock Hilbert space is
\(\mathcal F^2(\mathbb C)=\{f\text{ entire}:\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)<\infty\}\), with orthonormal basis \(e_n(z)=z^n/\sqrt{n!}\), \(n\ge0\). Fix an integer \(N\ge2\), pairwise distinct real rates \(t_j>0\), and complex coefficients \(c_j\), not all zero. For every \(\delta,\varepsilon>0\), put

\[
T_{\delta,\varepsilon}=\sum_{j=1}^N c_j C_{\varphi_j},\qquad
\varphi_j(z)=e^{-\delta-\varepsilon t_j}z,
\qquad F(x)=\sum_{j=1}^N c_j e^{-t_jx}.
\]

Let \(M_k=\sum_j c_jt_j^k\). The least \(m\ge0\) with \(M_m\ne0\) exists and is at most \(N-1\) by the nonsingularity of the Vandermonde matrix. Set \(A_m=|M_m|/m!>0\). Statements apply to every fixed \(p>0\), including quasi-Schatten exponents below one. All limits are joint limits through positive \(\delta,\varepsilon\).

## Proof

**Exact spectrum.** Because \(C_{az}e_n=a^n e_n\), each \(T_{\delta,\varepsilon}\) is diagonal on \((e_n)_{n\ge0}\) with eigenvalue \(e^{-\delta n}F(\varepsilon n)\). Thus its singular-value multiset is precisely
\(\{|e^{-\delta n}F(\varepsilon n)|:n\ge0\}\). Every summand is compact and belongs to every \(\mathcal S_p\), since \(0<e^{-\delta-\varepsilon t_j}<1\). Consequently the trace and norm can be studied using this exact multiset without assuming a particular ordering.

**Critical scale.** Write \(x=\varepsilon n\). Then \(e^{-\delta n}F(\varepsilon n)=e^{-(\delta/\varepsilon)x}F(x)\). As \(\delta/\varepsilon\to\tau<\infty\), these functions converge uniformly on compact \(x\)-intervals to \(G_\tau(x)=e^{-\tau x}F(x)\). The bound \(|F(x)|\le(\sum_j|c_j|)e^{-t_*x}\), \(t_*=\min_j t_j>0\), gives a uniform integrable exponential envelope for the \(p\)-th powers. Therefore the mesh-\(\varepsilon\) Riemann sums converge to the stated integral for every \(p>0\), and density of the same grid together with uniform tail decay gives the operator-norm limit. For fixed \(s>0\), the real-analytic function \(e^{-2\tau x}|F(x)|^2\) is nonconstant and tends to zero. Its level set at \(s^2\) is finite on any bounded interval and its upper-level set lies in a bounded interval. Applying Riemann-sum convergence to that indicator proves the counting law.

**Separated scale.** The Taylor expansion at zero is
\[
F(y)=\frac{(-1)^m M_m}{m!}y^m+O(y^{m+1}).
\]
For \(m\ge1\), the ratio \(F(y)/y^m\) extends continuously to \(y=0\); it is globally bounded, since \(F\) is exponentially decaying at infinity. For \(m=0\) use \(F\) itself. Put \(x=\delta n\). After multiplying the eigenvalues by \((\delta/\varepsilon)^m\), the resulting profile is
\[
e^{-x}x^m\frac{F((\varepsilon/\delta)x)}{((\varepsilon/\delta)x)^m},
\]
with its continuous interpretation when \(m=0\). It converges on compact intervals to \(e^{-x}(-1)^m M_m x^m/m!\), and is dominated by \(Cx^m e^{-x}\). Mesh-\(\delta\) Riemann-sum convergence yields the sharp \(p\)-trace coefficient because
\(\int_0^\infty x^{mp}e^{-px}\,dx=\Gamma(mp+1)/p^{mp+1}\). Uniform control of the tail and grid density yield the norm coefficient \(A_m\sup_{x\ge0}x^me^{-x}=A_m(m/e)^m\) for \(m\ge1\), and \(A_0\) for \(m=0\).

**Sharp cancellation and exact example.** Since the Vandermonde matrix \((t_j^k)_{0\le k\le N-1,1\le j\le N}\) is invertible, cancellation through order \(N-1\) is impossible for nonzero coefficients. The solution space of \(M_0=\cdots=M_{N-2}=0\) is one-dimensional and is spanned by \(c_j=1/\prod_{k\ne j}(t_j-t_k)\), from the standard partial-fraction identity. For \((t_1,t_2,t_3)=(1,2,3)\), \(c=(1,-2,1)\), we have \(m=2\), \(A_2=1\), and \(F(x)=e^{-x}(1-e^{-x})^2\). Substituting \(u=e^{-x}\) gives
\[
\int_0^\infty e^{-2\tau x}|F(x)|^2\,dx=B(2\tau+2,5),\qquad
\sup_{x\ge0}e^{-\tau x}F(x)=\frac{4(\tau+1)^{\tau+1}}{(\tau+3)^{\tau+3}}.
\]
In particular, the critical norm limit at \(\tau=0\) is \(4/27\), while the separated limit satisfies \((\delta/\varepsilon)^2\|T_{\delta,\varepsilon}\|\to4/e^2\) and \(\delta^5\varepsilon^{-4}\|T_{\delta,\varepsilon}\|_{\mathcal S_2}^2\to3/4\).

## Verification

The standalone Python checker `check.py` establishes exact rational finite-difference diagonal identities, checks an exact geometric-series Schatten trace against its finite partial sum, and probes both parameter-scale limits and the explicit beta-function constant; diagnostic output was `FOCK_COALESCENCE_DIAGNOSTIC_OK 152`. Its finite tests are supporting checks, not infinite proofs. The analytic arguments above establish the limits for all allowed parameters.

## Relationship to prior work

Lin, Lu, Yang and Zu establish qualitative no-cancellation of Schatten membership and fixed-symbol two-sided norm comparisons for finite sums (Theorem 1.3 of [1]). The present claim instead quantifies *degeneration of the comparison* as distinct radial symbols move together: it gives the entire two-scale singular profile, positive-level counting law, all Schatten asymptotic constants, and maximal moment cancellation order. The constants in [1] depend on fixed symbols and therefore do not imply these moving-symbol limits. Earlier work [2] treats order-bounded differences; [3] investigates evolution/iteration of weighted compositions rather than the two-scale finite-sum singular law. Related published work on polynomially weighted radial dilations features a single polynomial-exponential profile, which coincides with the far-separated universal shape but does not cover the full finite-ratio exponential-polynomial profile.

## Limitations

The classification concerns *radial, origin-fixing* symbols and *fixed* coefficients and rates; it does not address arbitrary affine symbols or weights. It does not assert a new characterization of Schatten membership for fixed symbols, or a uniform comparison constant for all families. No separate independent mathematical audit has been performed. Earlier general spectral/semigroup theory could conceivably imply some of the asymptotic consequences; novelty beyond inspected sources remains subject to broader literature review.

## References

1. Z. Lin, Y. Lu, R. Yang, C. Zu, *Finite Sums of Weighted Composition Operators on the Fock Space*, arXiv:2611.19948v1 (first posted 15 November 2026), https://arxiv.org/abs/2611.19948.
2. X.-F. Peng and Z.-J. Jiang, *Order-Bounded Difference in Weighted Composition Operators Between Fock Spaces*, Mathematics 12 (2024), 3360, https://doi.org/10.3390/math12213360.
3. I. Chalendar and J. R. Partington, *Weighted composition operators on the Fock space: iteration and semigroups*, Acta Sci. Math. 89 (2023), 93–108, https://arxiv.org/abs/2106.00427.
