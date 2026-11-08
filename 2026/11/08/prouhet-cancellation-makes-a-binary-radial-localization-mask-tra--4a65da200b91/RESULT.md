# Prouhet cancellation makes a binary radial localization mask trace-class flat

## Finding

Let \(\mathcal F^2\) be the analytic Bargmann–Fock Hilbert space on \(\mathbb C\), normalized by
\[
\|F\|^2=\frac1\pi\int_{\mathbb C}|F(z)|^2e^{-|z|^2}\,dA(z).
\]
For an integer \(j\geq0\), let \(s_2(j)\) be the number of ones in its binary expansion and put \(\varepsilon_j=(-1)^{s_2(j)}\). Define the binary radial observation mask
\[
E=\bigcup_{\substack{j\geq0\\\varepsilon_j=1}}\{z\in\mathbb C:j\leq|z|^2<j+1\}
\]
and the positive concentration operator \(T=P_{\mathcal F}\mathbf1_E\big|_{\mathcal F^2}\), where \(P_{\mathcal F}\) is the orthogonal Bargmann projection.

**Theorem.** For \(n\geq0\), the normalized monomials \(e_n(z)=z^n/\sqrt{n!}\) are eigenfunctions with
\[
Te_n=\lambda_ne_n,\qquad
\lambda_n=\frac12+\frac{q_n}{2},\qquad
q_n=\frac1{n!}\int_0^\infty \varepsilon_{\lfloor t\rfloor}e^{-t}t^n\,dt.
\]
For integers \(k\geq1\) and \(n\geq k+1\), the following **nonasymptotic certificate** holds:
\[
\boxed{\displaystyle
|q_n|\leq 2^{k(k-1)/2}\left[
2^{-k}\sqrt{\frac{k!(n-k)!}{n!}}+
\sqrt{\frac{(k+1)!(n-k-1)!}{n!}}
\right].}
\tag{1}
\]
Consequently, with natural logarithms,
\[
\boxed{\displaystyle
\limsup_{n\to\infty}\frac{\log|\lambda_n-1/2|}{(\log n)^2}
\leq-\frac1{8\log2},}
\tag{2}
\]
where \(\log0=-\infty\). Thus \(K=T-\frac12I\) belongs to every Schatten class \(\mathcal S_p\), \(p>0\), in particular is trace class, and
\[
\boxed{\operatorname{Tr}(K)=0,\qquad \sigma_{\rm ess}(T)=\{1/2\}.}
\tag{3}
\]
The compact operator \(K\) is nonzero and has eigenvalues of both signs. In fact
\[
q_0=(1-e^{-1})\prod_{r=0}^\infty(1-e^{-2^r})>0.
\tag{4}
\]
The sets \(E\) and \(\mathbb C\setminus E\) each contain infinitely many complete radial shells of normalized area one (Euclidean area \(\pi\) in Fock coordinates); the symbol \(\mathbf1_E-1/2\) does not decay at infinity. The bound (2) is an upper decay estimate, **not** a claim that its constant is sharp.

## Assumptions and scope

The operator is the ordinary Gaussian-window time–frequency localization operator, equivalently the Fock Toeplitz operator, with phase-space radial coordinate normalized as \(t=|z|^2\) on the Fock side (or \(t=\pi(x^2+\xi^2)\) in the standard Gaussian short-time Fourier convention). The mask is the canonical Prouhet–Thue–Morse coloring of consecutive equal-area shells, starting with shell \(j=0\) included. All indices and shell widths in this theorem are **exact**, not asymptotic. Neither the symbol nor its complement is compactly supported. The theorem is for one complex variable; no higher-dimensional multiplicity claim is made.

The special property used from the binary sequence is the exact block rule
\[
\varepsilon_{2^kq+r}=\varepsilon_q\varepsilon_r
\quad(0\leq r<2^k),\qquad
\sum_{r=0}^{2^k-1}\varepsilon_rX^r=
\prod_{a=0}^{k-1}(1-X^{2^a}).
\tag{5}
\]
It follows that \(\sum_{r=0}^{2^k-1}\varepsilon_r r^j=0\) for every integer \(0\leq j<k\). This exact cancellation is much stronger than merely having half of the shell indices of each color.

## Proof

**Step 1 (diagonalization).** Radial symmetry makes the monomials orthogonal for both the full Gaussian measure and the restricted measure. Integrating in polar coordinates with \(t=|z|^2\), their diagonal values are \(\int_Ee^{-t}t^n\,dt/n!\), as asserted. Write
\[
f_n(t)=\frac{e^{-t}t^n}{n!},\qquad
g_n(x)=\int_x^{x+1}f_n(t)\,dt.
\]
Since \(\sum_{j\geq0}g_n(j)=1\), we have \(q_n=\sum_{j\geq0}\varepsilon_jg_n(j)\) with absolute convergence.

**Step 2 (block cancellation and a sampling inequality).** Fix \(k\geq1\), let \(h=2^k\) and let \(E_ag(x)=g(x+a)\) denote translation. Define
\[
H_k(x)=\prod_{a=0}^{k-1}(1-E_{2^a})g_n(x).
\]
Equation (5), applied to blocks of length \(h\), gives the exact identity
\[
q_n=\sum_{q\geq0}\varepsilon_qH_k(qh).
\tag{6}
\]
For every absolutely continuous \(H\) with \(H,H'\in L^1(0,\infty)\), the fundamental theorem of calculus applied on each interval \([qh,(q+1)h]\) gives
\[
\sum_{q\geq0}|H(qh)|\leq h^{-1}\|H\|_{L^1}+\|H'\|_{L^1}.
\tag{7}
\]
Indeed, average \(H(x)\) over that interval, then bound the difference from \(H(qh)\) by integrating \(|H'|\).

Each factor \(1-E_a\) is an integral of the derivative over a segment of length \(a\). By Fubini and positivity after absolute values, for \(r=0,1\),
\[
\|H_k^{(r)}\|_{L^1(0,\infty)}
\leq 2^{k(k-1)/2}\|g_n^{(k+r)}\|_{L^1(0,\infty)}
\leq 2^{k(k-1)/2}\|f_n^{(k+r)}\|_{L^1(0,\infty)}.
\tag{8}
\]
Here the product of the step lengths is \(\prod_{a=0}^{k-1}2^a=2^{k(k-1)/2}\), and the final inequality follows from the definition of \(g_n\) and Tonelli.

**Step 3 (an exact Gamma derivative bound).** For integers \(0\leq r\leq n\), the Rodrigues identity for generalized Laguerre polynomials gives
\[
f_n^{(r)}(t)=\frac{r!}{n!}e^{-t}t^{n-r}L_r^{(n-r)}(t).
\]
Their weighted orthogonality states
\[
\int_0^\infty e^{-t}t^{n-r}\bigl(L_r^{(n-r)}(t)\bigr)^2dt=\frac{n!}{r!}.
\]
Cauchy–Schwarz, using \(\int_0^\infty e^{-t}t^{n-r}dt=(n-r)!\), yields
\[
\boxed{\displaystyle
\|f_n^{(r)}\|_{L^1(0,\infty)}\leq
\sqrt{\frac{r!(n-r)!}{n!}}.}
\tag{9}
\]
Applying (7)–(9) to (6), for \(r=k,k+1\), proves (1) without any asymptotic approximation.

**Step 4 (optimization of the bound).** Choose \(k=\lfloor\log n/(2\log2)\rfloor\) for sufficiently large \(n\). Then \(k=O(\log n)\), and uniformly for these choices,
\[
\log\frac{n!}{(n-k)!}=k\log n+O(k^2/n),
\qquad\log(k!)=O(k\log(k+1)).
\]
Taking logarithms of either term on the right side of (1) therefore gives at most
\[
\frac{\log2}{2}k^2-\frac{k\log n}{2}+O(k\log(k+1))
=-\frac{(\log n)^2}{8\log2}+O(\log n\log\log n).
\]
This establishes (2). In particular \(|q_n|=O_M((n+1)^{-M})\) for every \(M>0\). Diagonalization then implies \(K\in\mathcal S_p\) for all \(p>0\), and Weyl's criterion gives the asserted singleton essential spectrum.

**Step 5 (the exact zero trace).** The generating function of \(q_n\) is analytic for \(|z|<1\). Set \(w=1-z\), initially with real \(0<z<1\). Summing the Gamma kernel first and splitting the integral into shells,
\[
\begin{aligned}
\sum_{n=0}^\infty q_nz^n
&=\int_0^\infty \varepsilon_{\lfloor t\rfloor}e^{-wt}\,dt\\
&=\frac{1-e^{-w}}w\sum_{j=0}^\infty\varepsilon_je^{-wj}\\
&=\frac{1-e^{-w}}w\prod_{a=0}^\infty(1-e^{-w2^a}).
\end{aligned}
\tag{10}
\]
For each fixed positive integer \(m\), the first \(m\) product factors have absolute product at most \(w^m2^{m(m-1)/2}\), while all remaining factors lie in \((0,1)\). Thus the right side tends to zero as \(w\downarrow0\). Since \(\sum_n|q_n|<\infty\) by Step 4, Abel's limit gives \(\sum_nq_n=0\); hence \(\operatorname{Tr}(K)=0\). Equation (10) at \(z=0\) gives (4). All factors in (4) are positive, and the product is positive because \(\sum_a e^{-2^a}<\infty\). Therefore \(K\neq0\) and has a positive eigenvalue. Since its trace is zero, it also has a negative eigenvalue. This completes the proof.

## Verification

The standard-library program `checker.py` reproduces the finite Prouhet moment cancellations through block size \(1024\), evaluates low-degree eigenvalue deviations by explicit incomplete-Gamma shell integrals, verifies sample cases of the **nonasymptotic** inequality (1), and checks the generating-function identity (10) at two interior points. Execute it from the folder containing these files with `python3 checker.py`.

A successful run prints `THUE_MORSE_FOCK_CHECKS_PASS 120`. These checks validate finite algebra and numerical consistency only: the all-index bounds, trace identity, and Schatten claims have their independent mathematical proofs in Steps 1–5.

## Relationship to prior work

Knutsen (arXiv:1907.00848, first public July 1, 2019; open-access 2020 version) establishes Gaussian localization eigenvalue formulas and studies radial Cantor masks, including an infinite periodic annular mask. That supplies the established diagonalization and the motivation to examine symbolic radial masks, **not** a spectral trace-class law for the aperiodic Prouhet coloring. Esmeral and Maximenko (arXiv:1505.07906) characterize the C*-algebra of radial Fock Toeplitz eigenvalue sequences and their asymptotic heat-kernel smoothing; these general approximations do not provide the explicit arbitrary-order finite-difference bound (1), the squared-log decay (2), or the trace identity (3) for this binary mask. Esmeral García and Maximenko (arXiv:2503.23276) develop constructive realization of convergent spectral sequences, which does not specify this mask or a quantitative rate.

Rozenblum (arXiv:1012.3528) investigates faster spectral decay from sign-changing Bargmann symbols, with a distinct rapidly oscillating, decaying continuous example. That work establishes that cancellation can be potent, but its Section 5 does not contain the nondecaying binary Thue–Morse mask or this zero-trace all-Schatten statement. The Prouhet product and moment cancellation are classical; originality here is claimed only for their specific quantitative consequence for Gaussian localization and its trace.

## Limitations

No lower bound of matching squared-logarithmic order is asserted; (2) may not give the optimal coefficient. The theorem establishes the existence of positive and negative eigenvalues of \(K\), not their precise sign pattern or multiplicities. It concerns one-dimensional Gaussian-window localization and equal-area radial shells; general automatic sequences, nonradial masks, and other windows are outside its scope. Earlier general smoothing results could implicitly imply part of the rate, and historical priority still requires expert verification.

## References

- H. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets*, arXiv:1907.00848 (2019); *Journal of Fourier Analysis and Applications* 26, 47 (2020), DOI:10.1007/s00041-020-09751-9.
- K. Esmeral and E. A. Maximenko, *Radial Toeplitz operators on the Fock space and square-root-slowly oscillating sequences*, arXiv:1505.07906 (2015), *Complex Analysis and Operator Theory* 10 (2016).
- K. Esmeral García and E. A. Maximenko, *Constructive approximation of convergent sequences by eigenvalue sequences of radial Toeplitz--Fock operators*, arXiv:2503.23276 (2025).
- G. Rozenblum, *On lower eigenvalue estimates for Toeplitz operators with radial symbols in Bergman spaces*, arXiv:1012.3528 (2010), *Journal of Spectral Theory* 1 (2011), 299–325.
- J.-P. Allouche and J. Shallit, *Automatic Sequences: Theory, Applications, Generalizations*, Cambridge University Press (2003), for the classical binary sequence and finite-product identities.
