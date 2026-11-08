# A sharp harmonic limit for first-passage fluctuations of projective Brownian fidelity

## Finding

Let \(n\ge2\) be an integer and \(c>0\). Consider the fidelity diffusion with generator
\[
\mathcal G f(x)=c\bigl[x(1-x)f''(x)+(1-nx)f'(x)\bigr],\qquad 0<x<1,
\]
started at \(F_0=0\). For each \(b\in(0,1)\), put \(T_b=\inf\{t\ge0:F_t\ge b\}\), \(m_n(b)=\mathbb ET_b\), and \(C_n(b)=\operatorname{Var}(T_b)/m_n(b)^2\). Define the mean-weighted departure from exponential first-passage fluctuations by
\[
\mathscr D_n(b)=m_n(b)\,[1-C_n(b)].
\]
The function \(\mathscr D_n\) is **strictly increasing** on \((0,1)\), with the sharp finite bound
\[
0<\mathscr D_n(b)<\frac{2H_{n-1}}{c(n-1)},\qquad
\lim_{b\uparrow1}\mathscr D_n(b)=\frac{2H_{n-1}}{c(n-1)},
\quad H_j=\sum_{r=1}^j\frac1r.
\]
In particular, \(0<C_n(b)<1\) at every finite threshold, while \(C_n(b)\to1\) at high fidelity. More precisely, with \(\varepsilon=1-b\),
\[
C_2(b)=1-\frac{2}{\log(1/\varepsilon)}+o\!\left(\frac1{\log(1/\varepsilon)}\right),
\]
and for each fixed integer \(n\ge3\),
\[
C_n(b)=1-2(n-2)H_{n-1}\varepsilon^{n-2}+o(\varepsilon^{n-2}).
\]
The time scale \(c\) cancels from these dimension-dependent relative-fluctuation asymptotics.

## Assumptions and scope

The diffusion is the unique conservative regular solution with the natural entrance/reflecting endpoint at zero, and it is killed when it first reaches \(b<1\). Its invariant density before killing is \((n-1)(1-x)^{n-2}\) on \((0,1)\); it is the fidelity coordinate of isotropic Fubini--Study Brownian motion on complex projective \((n-1)\)-space, up to the positive global time normalization \(c\). Starting at an orthogonal state means \(F_0=0\). Neither microscopic quantum measurement back-action nor Hamiltonian drift is included. Every assertion is for finite \(n\), finite \(c>0\), and thresholds strictly less than one; the displayed high-fidelity expansions are for fixed \(n\).

The choice of \(\mathscr D_n\) is motivated by rare-target first-passage statistics. If \(T_b\) were exactly exponentially distributed, its coefficient of variation squared would be one. The mean-weighted deficit isolates the first additive-time correction to this exponential approximation, which would be obscured in the unweighted ratio \(C_n(b)\to1\).

## Proof

Write \(q=n-1\ge1\). For real \(s\) near zero, let \(a_s\) be the analytic solution with \(a_0=0\) of \(a_s(q-a_s)=s/c\). The regular solution of \(\mathcal Gh=sh\) normalized by \(h(0)=1\) is
\[
h_s(x)={}_2F_1(a_s,q-a_s;1;x).
\]
The backward hitting-time equation with \(h_s(b)\ne0\) therefore yields
\[
\mathbb E_0e^{-sT_b}=\frac{1}{h_s(b)}.
\]
For every integer \(k\ge1\) define
\[
A_k(q)=\frac{\prod_{j=1}^{k-1}j(j+q)}{(k!)^2}>0,
\qquad
S_k(q)=\sum_{j=1}^{k-1}\frac{1}{j(j+q)}
\quad(S_1=0).
\]
The hypergeometric coefficient factors as
\[
(a_s)_k(q-a_s)_k=\prod_{j=0}^{k-1}\bigl(j(j+q)+s/c\bigr).
\]
Termwise differentiation, justified for each \(b<1\) by local uniform convergence, gives
\[
\partial_sh_s(b)|_{s=0}=\frac1c\sum_{k\ge1}A_k(q)b^k,
\qquad
\partial_s^2h_s(b)|_{s=0}=\frac2{c^2}\sum_{k\ge1}A_k(q)b^kS_k(q).
\]
Differentiating the reciprocal Laplace transform gives
\[
m_n(b)=\frac1c\sum_{k\ge1}A_k(q)b^k,
\qquad
\operatorname{Var}(T_b)=m_n(b)^2-\frac2{c^2}\sum_{k\ge1}A_k(q)b^kS_k(q).
\]
Consequently the exact positive-series expression for the asserted deficit is
\[
\mathscr D_n(b)=\frac2c\frac{\sum_{k\ge1}A_k(q)b^kS_k(q)}{\sum_{k\ge1}A_k(q)b^k}.
\tag{1}
\]
This identity can also be obtained by differentiating the classical Jacobi first-passage hypergeometric transform. It is the **monotonicity and sharp harmonic limit** of (1), not the general Jacobi moment representation, that are asserted here as the contribution.

The sequence \(S_k(q)\) increases strictly for \(k\ge1\) and, by partial fractions, converges to
\[
S_\infty(q)=\sum_{j\ge1}\frac{1}{j(j+q)}=\frac{H_q}{q}.
\]
For each \(b\in(0,1)\), \(w_k(b)=A_k(q)b^k/\sum_jA_j(q)b^j\) is a probability mass function. Differentiation with respect to \(\log b\) yields
\[
\frac{d\mathscr D_n}{d\log b}=\frac2c\operatorname{Cov}_{w(b)}(K,S_K(q))>0.
\]
Strict positivity follows because every \(k\ge1\) has positive weight and \(S_2>S_1\), while the covariance of a strictly increasing and a nondecreasing function of the same nondegenerate random variable is positive. Formula (1) now gives its strict positive upper bound. Furthermore,
\[
A_k(q)=\frac{\Gamma(k+q)}{\Gamma(q+1)\,k\,\Gamma(k+1)}\sim\frac{k^{q-2}}{q!}.
\]
Thus \(\sum_kA_k(q)b^k\to\infty\) as \(b\uparrow1\), logarithmically if \(q=1\) and by a power if \(q\ge2\). The mass of \(w_k(b)\) escapes every finite initial set. Since \(S_k(q)\uparrow H_q/q\) boundedly, (1) converges to \(2H_q/(cq)\), establishing sharpness.

For completeness, solving the mean hitting-time equation \(\mathcal Gm=-1\), with \(m(b)=0\), gives
\[
m_n(b)=\frac{1}{cq}\int_0^b\frac{1-(1-x)^q}{x(1-x)^q}\,dx.
\]
Therefore \(m_2(b)=c^{-1}\log(1/(1-b))\), while for fixed \(q\ge2\),
\[
m_n(b)\sim\frac{(1-b)^{-(q-1)}}{cq(q-1)}.
\]
Using the limit of \(\mathscr D_n(b)\) in \(C_n(b)=1-\mathscr D_n(b)/m_n(b)\) proves both advertised expansions. Positivity of the hitting-time variance follows from nondegenerate sample-path fluctuations, and \(C_n(b)<1\) follows from \(\mathscr D_n(b)>0\).

## Verification

`verify.py` computes the convergent series in (1), evaluates an independent boundary-value quadrature, and checks positivity, strict monotonicity at sampled thresholds and the harmonic endpoint. It passed 196 deterministic assertions using Python 3 and SciPy. An independent variance representation used for these checks is
\[
\operatorname{Var}(T_b)=\frac{2}{c^2q^2}\int_0^b\frac{dx}{x(1-x)^q}\int_0^x\frac{[1-(1-y)^q]^2}{y(1-y)^q}\,dy.
\]
Run `python verify.py` in the directory containing that file. Numerical checks are diagnostics only; the assertions for arbitrary \(n\) and \(b\) are proved by the analytic series and comparison argument above.

## Relationship to prior work

Tóth (arXiv:2606.11438, first publicly posted 9 June 2026) derives the underlying Brownian fidelity process, its high-fidelity mean first-passage behavior, and spectral tail representations. D'Onofrio, Tamborrino and Lánský (2018) establish general Jacobi diffusion first-passage Laplace transforms and moment formulas, including mean, variance and third moment. These broad formulas already cover fixed-threshold moment calculations in the present Jacobi specialization; no novelty is claimed for that reduction, the hypergeometric transform, or the first two moments themselves. The substantive further statement proved here is a global strict ordering of the mean-weighted nonexponentiality deficit across **all** fidelity thresholds, with its precise harmonic-number endpoint and sharp dimensional convergence rates.

The source comparison did not identify that dimension-uniform monotonicity and harmonic-limit inequality, but this does not constitute a proof of publication priority. Earlier general Jacobi formulas are the strongest possible source of an implicit equivalent and must be considered in any independent literature review.

## Limitations

The conclusions hold for isotropic Fubini--Study Brownian diffusion only, not a discrete random walk at finite step size, quantum trajectories with measurement back-action, arbitrary initial fidelity, or a nonsymmetric generator. The upper threshold \(b=1\) is inaccessible in finite time; asymptotics refer to \(b\uparrow1\), never an actual first hit of one. The Gaussian/exponential character of the full rescaled hitting-time distribution is not proved here; only its first two moments and their sharp correction are determined. The 3 November 2026 revised arXiv full text could not be inspected, although the accessible earlier full text and revision abstract were compared. Independent publication-priority and mathematical audits remain outstanding.

## References

1. G. I. Tóth, *Isotropic random walks and Brownian diffusion on complex projective space*, arXiv:2606.11438, version 1 submitted 9 June 2026; https://arxiv.org/abs/2606.11438.
2. G. D'Onofrio, M. Tamborrino and P. Lánský, *The Jacobi diffusion process as a neuronal model*, Chaos **28** (2018), 103119; https://doi.org/10.1063/1.5051494. Open author manuscript available at https://iris.polito.it/handle/11583/2982959.
