# Gaussian-regulator Hankel pairs: a spectral notch and reversal of Schatten rankings

## Finding

On the normalized analytic Gaussian Fock space \(\mathcal F^2\subset L^2(\mathbb C,\pi^{-1}e^{-|z|^2}dA)\), let \(P\) be the orthogonal analytic projection and \(H_f=(I-P)M_f|_{\mathcal F^2}\) be the big Hankel operator. For every integer \(m\ge1\) and \(\beta>0\), put
\[
f_{m,\beta}(z)=z^m e^{-\beta|z|^2},\qquad H_+=H_{f_{m,\beta}},\qquad H_-=H_{\overline{f_{m,\beta}}}.
\]
Both symbols are bounded and both Hankel operators belong to every Schatten class \(\mathcal S_p\), \(p>0\). Their exact squared singular-value multisets are \(\{a_{n,\pm}(\beta):n\ge0\}\), where
\[
A_n=\frac{(n+m)!}{n!\,(1+2\beta)^{n+m+1}},\quad
B_{n,+}=\frac{(n+m)!}{n!\,(1+\beta)^{2(n+m+1)}},
\]
\[
B_{n,-}=\begin{cases}
0,&n<m,\\
\displaystyle\frac{n!}{(n-m)!\,(1+\beta)^{2(n+1)}},&n\ge m,
\end{cases}\qquad a_{n,\pm}=A_n-B_{n,\pm}.
\]
These indexed channels need not be arranged in decreasing order. For every \(p>0\) and fixed \(m\), the exact small-regulator asymptotics are
\[
\lim_{\beta\downarrow0}\beta^{1+(m-1)p/2}\|H_+\|_{\mathcal S_p}^{p}
=\int_0^\infty u^{(m+1)p/2}e^{-pu}\,du
=\frac{\Gamma(1+(m+1)p/2)}{p^{1+(m+1)p/2}},
\]
\[
\lim_{\beta\downarrow0}\beta^{1+(m-1)p/2}\|H_-\|_{\mathcal S_p}^{p}
=\int_0^\infty u^{(m-1)p/2}|u-m|^p e^{-pu}\,du.
\]
At the individual channel scale \(n\beta\to u\in[0,\infty)\),
\[
\beta^{m-1}a_{n,+}(\beta)\longrightarrow u^{m+1}e^{-2u},\qquad
\beta^{m-1}a_{n,-}(\beta)\longrightarrow u^{m-1}(u-m)^2e^{-2u},
\]
with \(u^0=1\) at \(u=0\). The anti-analytic profile has a **spectral notch** at the critical scaled index \(u=m\), whereas the analytic profile does not. Operator norms satisfy
\[
\lim_{\beta\downarrow0}\beta^{(m-1)/2}\|H_+\|=\sup_{u\ge0}u^{(m+1)/2}e^{-u},\qquad
\lim_{\beta\downarrow0}\beta^{(m-1)/2}\|H_-\|=\sup_{u\ge0}u^{(m-1)/2}|u-m|e^{-u}.
\]

For the natural first angular mode \(m=1\),
\[
\lim_{\beta\downarrow0}\beta\|H_+\|_{\mathcal S_1}=1,\quad
\lim_{\beta\downarrow0}\beta\|H_-\|_{\mathcal S_1}=\frac2e,
\]
\[
\lim_{\beta\downarrow0}\|H_+\|=\frac1e,\qquad
\lim_{\beta\downarrow0}\|H_-\|=1.
\]
Consequently, for all sufficiently small positive \(\beta\), the analytic Hankel operator has the **larger trace norm but smaller operator norm**. Despite this reversal, the Hilbert–Schmidt norms are exactly equal at every \(\beta>0\):
\[
\|H_+\|_{\mathcal S_2}^2=\|H_-\|_{\mathcal S_2}^2
=m!\left[(2\beta)^{-m-1}-\{\beta(2+\beta)\}^{-m-1}\right].
\]
The equality of Hilbert–Schmidt norms for integrable symbols is an established phenomenon; novelty is **not** claimed for that equality alone.

## Assumptions and scope

The Fock norm is \(\|g\|^2=\pi^{-1}\int_{\mathbb C}|g(z)|^2e^{-|z|^2}\,dA(z)\), so \(e_n(z)=z^n/\sqrt{n!}\) is an orthonormal basis. The target of each Hankel operator is \(L^2\ominus\mathcal F^2\), not the analytic Fock space. Every assertion holds for integer \(m\ge1\), real \(\beta>0\), and real \(p>0\), with \(m,p\) fixed before taking \(\beta\downarrow0\). The Schatten \(p\) expression is a quasi-norm when \(p<1\). No uniformity in growing \(m\) or varying \(p\) is asserted.

## Proof

**Exact diagonalization.** The vectors \(f_{m,\beta}e_n\) have angular frequencies \(n+m\); the vectors \(\overline{f_{m,\beta}}e_n\) have frequencies \(n-m\). Analytic projection preserves angular frequency, so different \(n\) yield orthogonal Hankel outputs separately for either symbol. Thus \(H_\pm^*H_\pm\) are diagonal in \(e_n\). Gaussian moment integration gives \(\|f_{m,\beta}e_n\|^2=\|\overline{f_{m,\beta}}e_n\|^2=A_n\). The only possibly nonzero analytic projection coefficients have degrees \(n+m\) for the plus operator and \(n-m\) for the minus operator (the latter exists only if \(n\ge m\)). Their squared magnitudes are \(B_{n,+}\) and \(B_{n,-}\) respectively. Pythagoras establishes the displayed exact formula. Exponential factors make both operators all-Schatten at every \(\beta>0\).

**Hilbert–Schmidt identity.** The binomial generating function \(\sum_{n\ge0}(n+m)!\,x^n/n!=m!(1-x)^{-m-1}\) gives
\[
\sum_{n\ge0}A_n=\frac{m!}{(2\beta)^{m+1}},\qquad
\sum_{n\ge0}B_{n,+}=\sum_{n\ge0}B_{n,-}=\frac{m!}{\{\beta(2+\beta)\}^{m+1}}.
\]
In the second equality for minus, reindex \(n=m+k\). Subtraction proves the exact equality.

**The scaled profiles.** Write \(u=\beta n\). For \(u>0\) fixed, factorial products imply \((n+m)!/n!=n^m(1+O_m(n^{-1}))\). The logarithms \(\log(1+t)=t-t^2/2+O(t^3)\) show
\[
\beta^{m-1}A_n\left(1-\frac{B_{n,+}}{A_n}\right)\longrightarrow u^{m+1}e^{-2u},
\]
\[
\beta^{m-1}A_n\left(1-\frac{B_{n,-}}{A_n}\right)\longrightarrow u^{m-1}(u-m)^2e^{-2u}.
\]
For the second expression the crucial first-order cancellation is
\[
\frac{1-B_{n,-}/A_n}{\beta}\longrightarrow\frac{(u-m)^2}{u}.
\]
This follows by expanding the factorial ratio and the two exponential denominators. At \(u=0\), direct use of the product formulas (or the bounds below) extends the limits, including \(m=1\), where the minus limit is \(1\). The convergence is uniform when \(u\) is restricted to any compact interval of \([0,\infty)\).

**Uniform summability and the norm.** For \(0<\beta\le1\), set \(v=\beta(n+1)\). The elementary estimate \(1-e^{-x}\le x\) and \(d_\beta=2\log(1+\beta)-\log(1+2\beta)=O(\beta^2)\) imply
\[
\beta^{m-1}a_{n,+}\le C_m v^{m+1}e^{-c v}.
\]
For \(n\ge m\), the negative logarithm of \(B_{n,-}/A_n\) is
\[
\sum_{j=1}^m\log\frac{n+j}{n-j+1}+(n+1)d_\beta-m\log(1+2\beta),
\]
which is nonnegative and at most \(C_m[(n+1)\beta^2+(n-m+1)^{-1}]\). This yields
\[
\beta^{m-1}a_{n,-}\le C_m(v^{m-1}+v^{m+1})e^{-c v};
\]
for the finitely many \(n<m\), the same bound follows directly from \(a_{n,-}=A_n\). Constants depend only on \(m\), and \(c>0\) is absolute. The bounds are summable after multiplication by \(\beta\) and taking any positive \(p/2\)-power. Consequently dominated Riemann sums prove both \(\mathcal S_p\) limits. Uniform convergence on compact \(u\)-intervals plus exponentially small tails gives the two operator-norm limits.

**The trace/operator reversal.** For \(m=1,p=1\), the limiting trace integrals are \(\int_0^\infty ue^{-u}du=1\) and \(\int_0^\infty|u-1|e^{-u}du=2/e\). The plus operator-norm profile \(ue^{-u}\) has maximum \(1/e\), while \(|u-1|e^{-u}\) has global maximum \(1\) at \(u=0\). Strict inequalities in the limits imply the stated reversal for all sufficiently small \(\beta\).

## Verification

The accompanying standalone `checker.py` computes the exact diagonal channels by cancellation-stable logarithmic formulas. It tests the exact Hilbert–Schmidt sums, three values of \(m\), a range of regulator strengths and scaled indices, the \(\mathcal S_p\) integral limits, and both endpoint contrasts. The checker passed 122 assertion groups. These finite tests supplement the analytic argument and are not used as its proof.

## Relationship to prior work

Hu and Virtanen (2022; preprint 2020), Hu and Virtanen (2023; preprint 2021), and Asghari–Hu–Virtanen (2023) give broad Fock Hankel Schatten/compactness criteria and Berger–Coburn relations. Bauer (2004) proves earlier Hilbert–Schmidt comparison and includes equality for Lebesgue-square-integrable symbols, which covers the equal-Hilbert–Schmidt subclaim here. Fan–Wang–Zeng (2024) establish singular-sequence/IDA rearrangement comparability for large operator classes, but the inspected results use unspecified comparison constants, not the explicit coupled regulator spectrum or the first-mode trace/operator ranking reversal. The present finding identifies sharp constants and the cancellation notch for the concrete Gaussian-regulated monomial pair. Published findings on exterior Laurent symbols on Fock space concern an opposite spatial regime (inverse powers outside a disk) and fixed-symbol singular tails, not the \(\beta\downarrow0\) coupled regulator.

## Limitations

The analysis covers only standard Gaussian Fock space and Gaussian cutoff monomials; it does not classify all bounded symbols or settle any general Berger–Coburn conjecture. The anti-analytic notch refers to the **scaled profile**, not a zero singular value at finite regulator. The coincidence of Hilbert–Schmidt norms is known; the precise trace/operator norm inversion and sharp \(p\)-mass profiles are the assessed contribution. Older specialized calculations for the same elementary family remain a possible historical-priority risk. No independent mathematical audit has been performed.

## References

- G. Asghari, Z. Hu, J. A. Virtanen, *Schatten class Hankel operators on doubling Fock spaces and the Berger–Coburn phenomenon*, arXiv:2312.06656, first public 2023-12-11, https://arxiv.org/abs/2312.06656.
- Z. Hu, J. A. Virtanen, *Schatten class Hankel operators on the Segal–Bargmann space and the Berger–Coburn phenomenon*, Trans. Amer. Math. Soc. 375 (2022), 3733–3753, with corrigendum (2023), https://doi.org/10.1090/tran/8638.
- Z. Hu, J. A. Virtanen, *IDA and Hankel operators on Fock spaces*, Anal. PDE 16 (2023), 2041–2077, arXiv:2111.04821, https://arxiv.org/abs/2111.04821.
- W. Bauer, *Hilbert–Schmidt Hankel operators on the Segal–Bargmann space*, Proc. Amer. Math. Soc. 132 (2004), 2989–2996, https://doi.org/10.1090/S0002-9939-04-07264-8.
- Z. Fan, X. Wang, Z. Zeng, *IDA function and asymptotic behavior of singular values of Hankel operators on weighted Bergman spaces*, arXiv:2410.20082 (2024), https://arxiv.org/abs/2410.20082.
