# Kemeny-optimal stochastic walks on Möbius ladders: a two-thirds rung law

## Finding
For each integer \(m\ge 2\), form the Möbius ladder \(M_{2m}\) on \(\mathbb Z/(2m)\mathbb Z\) with cycle edges \(\{i,i+1\}\) and antipodal edges \(\{i,i+m\}\). Minimize the *zero-target* Kemeny constant
\[
\mathcal K(P)=\sum_{j=2}^{2m}\frac{1}{1-\lambda_j(P)}
=\operatorname{tr}\left[(I-P+J)^{-1}\right]-1,
\qquad J=\frac{\mathbf1\mathbf1^{\mathsf T}}{2m},
\]
over every irreducible symmetric entrywise-nonnegative stochastic matrix \(P\) supported off-diagonally on the ladder edges; self-loops are allowed. The minimizer is **unique globally**, without an invariance assumption on the competing transition probabilities.

All rim edges receive the same probability \(a_m=(1-b_m)/2\), all antipodal rungs the same probability \(b_m\), and every holding probability is zero. Put
\[
F_m(b)=\frac{m^2-1}{6(1-b)}+
\frac{m}{2\sqrt b}\frac{1-q(b)^m}{1+q(b)^m},
\qquad q(b)=\frac{1-\sqrt b}{1+\sqrt b}.
\]
The rung probability \(b_m\) is the **unique** root of \(F_m'(b)=0\) in \(0<b<1\), and the exact optimum is \(\mathcal K_m^*=F_m(b_m)\). In particular,
\[
b_2=b_3=\frac13,\qquad 0<b_m<\frac13\quad (m\ge4).
\]
The large-ladder asymptotics are
\[
\boxed{b_m\sim\left(\frac{3}{2m}\right)^{2/3}},
\qquad
\boxed{\mathcal K_m^*=\frac{m^2}{6}
+\frac12\left(\frac32\right)^{2/3}m^{4/3}+o(m^{4/3})}.
\]
The equal-edge-probability walk, with each incident edge assigned probability \(1/3\), incurs the sharp asymptotic multiplicative penalty
\[
\boxed{\lim_{m\to\infty}\frac{\mathcal K(P_{\mathrm{equal}})}{\mathcal K_m^*}=\frac32}.
\]
Thus the globally optimal rung probability is of order \(m^{-2/3}\), not the order \(m^{-2}\) of the fastest-SLEM rung allocation on the same graph family [4,5]. These objectives select qualitatively different stochastic networks.

## Assumptions and scope
The graph is simple and connected; its rim and antipodal edge sets are distinct for \(m\ge2\). Every off-diagonal allowed entry is independently adjustable in the original optimization; the diagonal may be positive. All matrices are symmetric and row-stochastic, hence have the uniform stationary distribution. Irreducibility is required, but aperiodicity is not: the spectral expression for the zero-target hitting-time convention is valid for periodic irreducible chains. If the positive-return-time convention is adopted, the Kemeny constant increases by exactly one for every competitor and the optimizer is unchanged. No claims concern nonuniform stationary laws, directed chains, or total-variation mixing times.

## Proof
**1. Existence, symmetry, and global uniqueness.** For an irreducible symmetric chain put \(L=I-P\), positive definite on \(\mathbf1^\perp\), and \(A=L+J\), positive definite on the entire space. For a nonzero symmetric zero-row-sum perturbation \(H\) along a feasible affine line, direct differentiation gives
\[
\frac{d^2}{dt^2}\operatorname{tr}(A+tH)^{-1}
=2\operatorname{tr}[(A+tH)^{-1}H(A+tH)^{-1}H(A+tH)^{-1}]>0.
\]
Indeed the trace is twice the squared Frobenius norm of \((A+tH)^{-1}H(A+tH)^{-1/2}\); it vanishes only if \(H=0\). Thus the Kemeny objective is strictly convex in the independent edge weights. The cyclic rotations of the ladder preserve the feasible region and the objective. Averaging any admissible \(P\) over rotations retains irreducibility and cannot increase \(\mathcal K\); the averaged matrix has rim probability \(a\), rung probability \(b\), and hold \(1-2a-b\), with \(a>0\), \(b\ge0\), \(2a+b\le1\). If \(s=2a+b<1\), replacing both edge probabilities by \(a/s,b/s\) multiplies the nonzero Laplacian eigenvalues by \(1/s\) and reduces \(\mathcal K\) by the factor \(s<1\). Hence a symmetric optimum must satisfy \(2a+b=1\), and irreducibility then gives \(0\le b<1\). The scalar problem below attains a unique minimum. Strict convexity implies that no nonsymmetric matrix can also be globally optimal, because averaging two distinct global optima would strictly improve them.

**2. Fourier reduction.** With \(a=(1-b)/2\), the nonzero Laplacian eigenvalues are
\[
\nu_k=(1-b)\left(1-\cos\frac{\pi k}{m}\right)
+b\bigl(1-(-1)^k\bigr),\qquad 1\le k<2m.
\]
For even indices, the elementary cosecant sum yields
\[
\sum_{j=1}^{m-1}\frac1{(1-b)(1-\cos(2\pi j/m))}
=\frac{m^2-1}{6(1-b)}.
\]
For odd indices put \(\theta_j=(2j+1)\pi/m\), \(s=\sqrt b\), and \(q=(1-s)/(1+s)\). The Poisson-kernel identity
\[
\frac1{1+b-(1-b)\cos\theta}
=\frac1{2s}\left(1+2\sum_{r=1}^{\infty}q^r\cos(r\theta)\right)
\]
is absolutely convergent for \(0<b<1\). Summing it at the \(m\) odd grid angles annihilates every Fourier mode except the multiples of \(m\), whose cosines equal \((-1)^\ell\). Consequently,
\[
\sum_{j=0}^{m-1}\frac1{1+b-(1-b)\cos\theta_j}
=\frac{m}{2s}\left(1+2\sum_{\ell=1}^{\infty}(-1)^\ell q^{m\ell}\right)
=\frac{m}{2s}\frac{1-q^m}{1+q^m}.
\]
This proves the exact expression \(\mathcal K=F_m(b)\).

**3. Strict scalar convexity and boundary.** The alternative finite-sum representation is
\[
F_m(b)=\frac{m^2-1}{6(1-b)}+
\sum_{j=0}^{m-1}\frac1{1-\cos\theta_j+b(1+\cos\theta_j)}.
\]
Each denominator is strictly positive and affine in \(b\). The first summand has strictly positive second derivative for \(0\le b<1\), while each remaining summand is convex. Thus \(F_m''(b)>0\) throughout the interval. To evaluate its derivative at zero use
\[
\sum_{j=0}^{m-1}\csc^2\frac{(2j+1)\pi}{2m}=m^2,\qquad
\sum_{j=0}^{m-1}\csc^4\frac{(2j+1)\pi}{2m}=rac{m^4+2m^2}{3}.
\]
Both identities follow by differentiating \(\sum_{j=0}^{m-1}\csc^2(z+j\pi/m)=m^2\csc^2(mz)\) at \(z=\pi/(2m)\). Since \((1+\cos\theta)/(1-\cos\theta)^2=\tfrac12(\csc^4(\theta/2)-\csc^2(\theta/2))\),
\[
F_m'(0)=\frac{m^2-1}{6}-\frac{m^4-m^2}{6}
=-\frac{(m^2-1)^2}{6}<0.
\]
Meanwhile \(F_m(b)\to\infty\) as \(b\uparrow1\). Therefore the unique minimizer lies in \(0<b_m<1\) and is exactly the root of \(F_m'(b)=0\). For explicit numerical evaluation, with \(Q=q(b)^m\),
\[
F_m'(b)=\frac{m^2-1}{6(1-b)^2}
-\frac{m}{4b^{3/2}}\frac{1-Q}{1+Q}
+\frac{m^2Q}{b(1-b)(1+Q)^2}.
\]
For \(m=2\), \(M_4\cong K_4\); for \(m=3\), \(M_6\cong K_{3,3}\). Each is edge-transitive, and symmetry plus strict convexity and zero holding give \(b_m=1/3\). For every \(m\ge4\), positivity of the final term and \(0<(1-Q)/(1+Q)<1\) imply
\[
F_m'(1/3)>\frac{3(m^2-1)}8-\frac{3\sqrt3 m}4>0.
\]
The last expression is positive at \(m=4\) and strictly increasing thereafter. Strictly increasing \(F_m'\) implies \(b_m<1/3\).

**4. Sharp asymptotics.** Fix \(c>0\) and substitute \(b=c m^{-2/3}\). Because \(m\sqrt b=\sqrt c\,m^{2/3}\to\infty\), the factor \(Q=q(b)^m\) is exponentially small on the \(m^{2/3}\) scale, uniformly for \(c\) in a compact subinterval of \((0,\infty)\). The derivative formula gives
\[
\frac{F_m'(c m^{-2/3})}{m^2}
\longrightarrow \frac16-\frac1{4c^{3/2}}.
\]
This limiting function changes sign once, at \(c_*=(3/2)^{2/3}\). For arbitrary fixed \(c_-<c_*<c_+\), strict convexity brackets \(b_m\) between \(c_-m^{-2/3}\) and \(c_+m^{-2/3}\) for sufficiently large \(m\). Letting the two bounds approach \(c_*\) proves \(b_m\sim c_*m^{-2/3}\). Expanding the two terms in the exact formula uniformly in this bracket yields
\[
F_m(b_m)=\frac{m^2}{6}+
\left(\frac{c_*}{6}+\frac1{2\sqrt{c_*}}\right)m^{4/3}+o(m^{4/3})
=\frac{m^2}{6}+\frac{c_*}{2}m^{4/3}+o(m^{4/3}).
\]
Finally at fixed \(b=1/3\) the even-index term is \((m^2-1)/4\), while the odd-index term is \(O(m)\). Hence \(F_m(1/3)=m^2/4+O(m)\), proving the ratio \(3/2\).

## Verification
Running `python verify.py` with a standard Python installation performs 417 checks, including independent exact rational inversion of \(I-P+J\) for multiple small ladders and rational square rung probabilities, direct Fourier-spectrum comparisons, derivative checks, optimizer bracket tests, asymptotic checks, and exact comparison against the published unit-conductance Kirchhoff-index table [3]. The matrix-inverse checks do not reuse the Fourier or Poisson-kernel simplification. These finite checks corroborate but do not replace the quantified convexity, Fourier, derivative, and asymptotic arguments above.

## Relationship to prior work
Boyd, Diaconis, Parrilo, and Xiao [1] establish convex graph-symmetry reductions for *fastest mixing* (the second-largest eigenvalue modulus, SLEM). Patel, Agharkar, and Bullo [2] establish convex formulations for reversible Kemeny minimization with a prescribed stationary law, including the trace-inverse method. The current contribution is not either general framework: it is an exact global minimizer and a nontrivial asymptotic transition-probability law for a specific family.

Baigonakova and Mednykh [3, Theorem 1] explicitly evaluate the **unweighted** Kirchhoff index of Möbius ladders. With a \(3\)-regular walk this is the special value \(F_m(1/3)\), not the minimizing \(b_m\), its uniqueness, or the \(m^{-2/3}\) law. The identity at \(b=1/3\) agrees exactly with [3] and is independently checked in `verify.py`.

The separately available Möbius-ladder SLEM classifications [4,5] use the same underlying graph but minimize the spectral maximum rather than the sum of spectral reciprocals. In particular their optimal rung probability scales as \(m^{-2}\) with positive holding, whereas the present unique Kemeny optimizer has no holding and its rung probability scales as \(m^{-2/3}\). A published determinant-optimal rung-allocation result [6] maximizes a spanning-tree determinant under a conductance budget rather than minimizing Kemeny subject to row-stochastic constraints. Durastante, Gnazzo, and Meini [7] develop general sparse reversible Kemeny perturbation algorithms without an explicit Möbius-ladder theorem. Neither a generic optimization formulation nor an unweighted value implies the present global optimizer and asymptotics without further analysis.

## Limitations
Originality has been assessed against identified mathematical records and inspected primary texts, not certified against every unpublished or unindexed equivalent. Specialized weighted Möbius-ladder spectral formulas could yield an alternative derivation. No independent mathematical audit has been performed. Asymptotic statements refer to \(m\to\infty\) with unit row-stochastic normalization; they are not statements about fixed-conductance network budgets. The result concerns discrete-time reversible chains with uniform stationary distribution, not the full class of random walks or finite-time total-variation optimizers.

## References
1. S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1, first public 2007-09-06; https://arxiv.org/abs/0709.0955 .
2. R. Patel, P. Agharkar, F. Bullo, *Robotic surveillance and Markov chains with minimal weighted Kemeny constant*, IEEE Transactions on Automatic Control 60 (2015), author manuscript: https://motion.me.ucsb.edu/pdf/2014b-pab.pdf .
3. G. A. Baigonakova, A. D. Mednykh, *Elementary formulas for Kirchhoff index of Möbius ladder and Prism graphs*, Siberian Electronic Mathematical Reports 16 (2019), 1655–1666: https://www.mathnet.ru/links/60f09bf37b455e6840140f491c0b8e4f/semr1158.pdf .
4. *Exact fastest-mixing probabilities on Möbius ladders*, publicly available scientific record: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-fastest-mixing-probabilities-on-m-bius-ladders--8814c6f5058b .
5. *Parity-sharp fastest mixing on Möbius ladders*, publicly available scientific record: https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-parity-sharp-fastest-mixing-on-m-bius-ladders--ad268224b267 .
6. *Sharp rung-deletion prices and critical-scale D-optimality on Möbius ladders*, publicly available scientific record: https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-rung-deletion-prices-and-critical-scale-d-optimality-on-m--00e372929d94 .
7. F. Durastante, M. Gnazzo, B. Meini, *Kemeny’s constant minimization for reversible Markov chains via structure-preserving perturbations*, BIT Numerical Mathematics 66 (2026), article 59: https://link.springer.com/article/10.1007/s10543-026-01152-6 .
