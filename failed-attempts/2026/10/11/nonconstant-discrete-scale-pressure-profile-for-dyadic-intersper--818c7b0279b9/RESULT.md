# Nonconstant discrete-scale pressure profile for dyadic interspersion shifts

## Finding
Let \(q\ge2\) be an integer. Form the two-sided shift \(X_q\) by closing all bi-infinite concatenations of words \(0u\), where \(u\) ranges over all \(q\)-letter words of lengths \(2^j\), \(j\ge0\). For the shift \(\sigma\), the clopen marker cylinder \([0]=\{x:x_0=0\}\), and the locally constant potential \(\varphi_t=t\mathbf1_{[0]}\), let
\[
P_q(t)=\sup_{\mu\in\mathcal M_\sigma(X_q)}
\big(h_\mu(\sigma)+t\mu([0])\big).
\]
For every \(t\in\mathbb R\), the pressure is the unique \(P>\log q\) solving
\[
e^{t-P}\sum_{j=0}^{\infty}e^{-2^j(P-\log q)}=1.\tag{1}
\]
There is a unique equilibrium measure; its successive marker-to-marker blocks are independent and have probabilities \(e^{t-P(2^j+1)}\) for each specific block \(0u\) with \(|u|=2^j\).

More sharply, there exists a universal nonconstant, strictly positive, continuous, one-periodic function \(\Theta\) such that the complete rare-marker pressure asymptotic is
\[
P_q(t)-\log q
=e^{-(\log2)q e^{-t}}\big(\Theta(\{q e^{-t}\})+o(1)\big),
\qquad t\longrightarrow-\infty.\tag{2}
\]
The little-oh is uniform over the changing phase \(\{q e^{-t}\}\in[0,1)\). An explicit representation is obtained by defining
\[
F(u)=\sum_{j=0}^{\infty}e^{-2^j u}
+\sum_{j=1}^{\infty}(e^{-2^{-j}u}-1),\qquad u>0.\tag{3}
\]
For each real \(c\), there is a unique \(u_c>0\) with \(F(u_c)=c\), and
\[
\Theta(c)=2^c u_c,\qquad u_{c+1}=u_c/2.\tag{4}
\]
Consequently the logarithmic leading exponent is exact:
\[
\lim_{t\to-\infty}e^t\log\frac1{P_q(t)-\log q}=q\log2.\tag{5}
\]
The periodic correction in (2) is genuinely nonconstant, although its variation is numerically small.

## Assumptions and scope
The alphabet is \(\{0,1,\ldots,q\}\). The symbol \(0\) is the distinguished marker; the \(q\) other symbols are unrestricted between markers. The return schedule is exactly \(S=\{2^j:j\in\mathbb N_0\}\); thus the time between successive markers is \(2^j+1\). We use the two-sided shift so that inducing on the marker cylinder is invertible. The free-marker subsystem consists of the full \(q\)-shift and has entropy \(\log q\). Limits concern fixed integer \(q\) and real \(t\to-\infty\); no simultaneous growth in \(q\) is asserted. The phase \(\{s\}=s-\lfloor s\rfloor\) is the usual fractional part.

## Proof
**1. Return-word variational bound.** For \(P>\log q\), let
\[
R(P,t)=\sum_{j\ge0}q^{2^j}e^{t-P(2^j+1)}.
\]
The series is finite and continuous, strictly decreasing in \(P\), tends to infinity as \(P\downarrow\log q\), and tends to zero as \(P\to\infty\). Thus exactly one \(P>\log q\) solves \(R(P,t)=1\), equivalent to (1). At this value assign to each individual return block \(0u\), \(|u|=2^j\), probability \(p_{j,u}=e^{t-P(2^j+1)}\). Their sum is one. Their mean length is finite, because \(P-\log q>0\) and the length-weighted tail decays superexponentially in \(j\).

Fix an ergodic invariant probability \(\mu\) with \(\mu([0])>0\). Induce on \([0]\); consecutive blocks are uniquely parsed by marker positions. Let \(\nu\) be the induced stationary block process and \(p\) its one-block distribution. The mean return length is \(\mathbb E_\nu L=1/\mu([0])<\infty\) (Kac's formula). Abramov's entropy identity gives
\[
h_\mu(\sigma)+t\mu([0])
=\frac{h_\nu+t}{\mathbb E_\nu L}
\le\frac{H(p)+t}{\mathbb E_p L}.
\]
The entropy \(H(p)\) is finite because the average return length is finite and the block alphabet has at most \((q+1)^L\) words of length \(L\). For the normalized return weights \(\rho_{j,u}=e^{t-P L_{j,u}}\), the Kullback--Leibler identity yields
\[
H(p)+t-P\mathbb E_pL
=-D(p\Vert\rho)\le0.
\]
Hence \(h_\mu+t\mu([0])\le P\). Equality requires both that the induced block process is i.i.d. and that its distribution is \(\rho\). Conversely, the i.i.d. block process with law \(\rho\) has finite mean return time, and its normalized suspension defines an ergodic invariant probability with free energy exactly \(P\). For an ergodic invariant probability with \(\mu([0])=0\), the support is in the marker-free full \(q\)-shift, so its free energy is at most \(\log q<P\). An ergodic-decomposition argument now proves that \(P_q(t)=P\) and the equilibrium measure is unique. Termwise differentiability and the nonvanishing derivative of \(R(P,t)\) also make \(P_q\) real analytic for every finite \(t\).

**2. Dyadic rare-marker equation.** Put \(\varepsilon=P_q(t)-\log q>0\), \(s=q e^{-t}>0\), and \(A(\varepsilon)=\sum_{j\ge0}e^{-2^j\varepsilon}\). Equation (1) is exactly
\[
A(\varepsilon)=s e^{\varepsilon}.\tag{6}
\]
For \(\varepsilon\downarrow0\), separate indices below and above \(\lfloor\log_2(1/\varepsilon)\rfloor\). Below that cutoff the total deficit relative to one is bounded by \(\sum \varepsilon2^j<2\), while above the cutoff the sum is bounded by a fixed convergent dyadic exponential tail. Therefore
\[
A(\varepsilon)=\frac{\log(1/\varepsilon)}{\log2}+O(1).
\]
Equation (6) implies \(\varepsilon\to0\) as \(s\to\infty\), then \(\log(1/\varepsilon)=s\log2+O(1)\), since \(s\varepsilon\to0\). This proves (5) and fixes the doubly exponential scale.

**3. Uniform scale profile.** Define \(F\) by (3). Both sums and their derivatives converge locally uniformly on \((0,\infty)\). The exact identity \(F(2u)=F(u)-1\) follows by shifting the two dyadic index ranges. Moreover
\[
F'(u)=-\sum_{j\in\mathbb Z}2^j e^{-2^j u}<0.
\]
Repeated dyadic scaling implies \(F(u)\to+\infty\) as \(u\downarrow0\) and \(F(u)\to-\infty\) as \(u\uparrow\infty\). Thus each \(c\in\mathbb R\) has a unique root \(F(u_c)=c\), depending continuously on \(c\), and (4) holds.

Write \(s=n+c\), where \(n=\lfloor s\rfloor\) and \(0\le c<1\). For \(u>0\), re-indexing gives
\[
A(2^{-n}u)-n
=\sum_{j=0}^{\infty}e^{-2^j u}
+\sum_{j=1}^n(e^{-2^{-j}u}-1)
\longrightarrow F(u),\tag{7}
\]
with convergence uniform for \(u\) in every compact subinterval of \((0,\infty)\). The right side of (6) becomes \((n+c)e^{2^{-n}u}\), which equals \(n+c+o(1)\) uniformly for bounded \(u\) and \(c\in[0,1]\). Since \(u\mapsto A(2^{-n}u)\) decreases strictly and \(u\mapsto(n+c)e^{2^{-n}u}\) increases, the unique root \(u=2^n\varepsilon\) of (6) converges to \(u_c\) uniformly for \(c\in[0,1]\). To justify the uniform inversion, bracket all \(u_c\) in a fixed compact interval strictly larger than \([u_1,u_0]\), and apply the uniform convergence in (7) and the strict monotonicity of \(F\). It follows that
\[
2^s\varepsilon=2^c u_c+o(1)=\Theta(c)+o(1),
\]
uniformly in the fractional phase. This is (2), and (4) shows \(\Theta(c+1)=\Theta(c)\).

**4. Nonconstancy of the phase modulation.** Put \(L=\log2\) and
\[
D(v)=-L e^v F'(e^v)
=L\sum_{j\in\mathbb Z}(2^j e^v)e^{-2^j e^v}.
\]
The function \(D\) is continuous and \(L\)-periodic. For its first nonzero Fourier frequency, change variables \(y=2^j e^v\) and use the disjoint intervals \([2^j,2^{j+1}]\) to obtain the absolutely convergent integral
\[
\frac1L\int_0^L D(v)e^{-2\pi i v/L}\,dv
=\int_0^\infty e^{-y}y^{-2\pi i/L}\,dy
=\Gamma(1-2\pi i/L)\ne0.\tag{8}
\]
The last inequality follows from the classical zero-free property of the gamma function. Thus \(D\) is nonconstant. If \(\Theta\) were constant, \(u_c=K2^{-c}\), whence \(F(u)=\log_2(K/u)\) on all \(u>0\). This would force \(D(v)\equiv1\), contradicting (8). Therefore the positive periodic profile is genuinely nonconstant.

## Verification
The self-contained script `dyadic_pressure_checker.py` evaluates the dyadic series with controlled truncation, the root relation, and the exact scale shift. Executing `python3 dyadic_pressure_checker.py` with the Python standard library produced `PASS: discrete-scale identity, unique-root convergence diagnostics, and dyadic-sum limits.` It also reproduced the finite approximations \(\Theta(0)\approx0.794024428881\) and \(\Theta(1/2)\approx0.794022803882\). These computations are finite diagnostics, not substitutes for the infinite-series estimates, inducing argument, or gamma-function nonvanishing proof.

## Relationship to prior work
Huang, Jenkinson, Xu and Zhang [1] introduce length-constrained interspersion and identify \(S=\{2^j\}\) as a canonical superlinear choice (Section 11, especially Theorem 11.17 and Remark 11.24). That paper studies typical periodic optimization and Markov boundaries, not the rare-marker pressure response in (2). Ramirez and Somers [2] give the known entropy root for \((S,w)\)-gap shifts, including lacunary gap schedules. In particular, the unweighted renewal-root method and its specialization at \(t=0\) are not claimed as new here. Burr, Das, Wolf and Yang [3] prove broad pressure computability results for coded and generalized gap shifts using inducing. The result here is the explicit nonconstant, universal *full asymptotic phase profile* (2)--(4), obtained by combining a marked-return pressure calculation with a uniform dyadic renormalization and Fourier nonconstancy. See also [4], an independently developed general finite-core approximation result, whose complete text could not be examined.

## Limitations
Only integer \(q\ge2\), dyadic allowed gap lengths, and the marker-counting potential are treated. The profile does not assert an analogous formula for arbitrary shift spaces, arbitrary gap schedules, or arbitrary potentials. Finite reproducibility diagnostics are not infinite mathematical proofs. The asymptotic profile is exact up to an additive \(o(1)\) after multiplying the pressure gap by \(e^{(\log2)q e^{-t}}\); no quantitative rate for this remainder is claimed. The published-prior-work check cannot exclude equivalent statements in unindexed literature or the unexamined full text of [4].

## References
[1] W. Huang, O. Jenkinson, L. Xu, Y. Zhang, *Typical periodic optimization for dynamical systems: symbolic dynamics*, arXiv:2603.07224v1 (7 March 2026), https://arxiv.org/abs/2603.07224 .

[2] C. Ramirez, A. Somers, *(S,w)-Gap Shifts and Their Entropy*, arXiv:2501.08438 (14 January 2025), https://arxiv.org/abs/2501.08438 .

[3] M. Burr, S. Das, C. Wolf, Y. Yang, *Computability of topological pressure on compact shift spaces beyond finite type*, arXiv:2010.14686 (28 October 2020), https://arxiv.org/abs/2010.14686 .

[4] C. E. Hedges, *Finite Cores Exhaustion and the Failure of Strict Sequential-Pressure Approximation in Coded Shifts*, arXiv:2609.09406 (8 September 2026), https://arxiv.org/abs/2609.09406 .
