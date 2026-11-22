# Sharp reversal counts and prescribed crossing times in reversible Ehrenfest relaxation

## Finding

For any reversible continuous-time Markov chain on \(n\ge2\) states, the stationary-weighted squared relaxation-distance ordering of two initial distributions can reverse at **at most \(n-2\) distinct positive times** unless their squared distances agree identically. This maximum is attained for every state count on the same canonical family of Ehrenfest urns, with **arbitrary specified crossing times** obtained solely by choosing two strictly positive initial preparations.

Precisely, define \(\chi^2(\mu\Vert\pi)=\sum_{x}(\mu(x)-\pi(x))^2/\pi(x)\). Let \(P_t=e^{tQ}\) be an irreducible Markov semigroup reversible with respect to \(\pi\), and \(p_t=pP_t\), \(q_t=qP_t\). Either
\[\chi^2(p_t\Vert\pi)=\chi^2(q_t\Vert\pi)\quad\text{for all }t\ge0,\]
or the equality can hold at no more than \(n-2\) distinct positive times. If exactly \(m\) distinct nonzero decay eigenvalues have a nonzero difference of their **total squared eigenspace projections**, the stronger maximum is \(m-1\) (with zero possible isolated crossings when \(m\le1\)). These are equal-distance times; each simple zero is a genuine strict ordering reversal.

For every \(n\ge2\), on the \(n\)-state Ehrenfest urn, each ordered set \(0<\tau_1<\cdots<\tau_{n-2}\) is exactly the set of strict positive reversal times for two suitably chosen strictly positive initial probability laws.

As a fully explicit minimum-state double reversal, consider two independent fair spins \(a,b\in\{-1,+1\}\) flipping at respective rates one and two, with uniform equilibrium. Choose
\[p(a,b)=\frac14\left[1+\frac14\left(\frac{12}{25}a+ab\right)\right],\qquad q(a,b)=\frac14\left[1+\frac14b\right].\]
Then the squared-distance gap is exactly
\[\Delta(t)=\chi^2(p_t\Vert\pi)-\chi^2(q_t\Vert\pi)=\frac1{16}e^{-4t}\left(e^{-4t}-\frac9{25}\right)\left(e^{-4t}-\frac{16}{25}\right).\]
The gap is positive before \(t=\frac14\log(25/16)\), negative until \(t=\frac14\log(25/9)\), and positive thereafter. The two crossing times are approximately \(0.111571775657\) and \(0.255412811883\). Both individual distances strictly decrease throughout.

## Assumptions and scope

The state space is finite and contains \(n\ge2\) points. The conservative generator \(Q\) is irreducible and satisfies detailed balance \(\pi(x)Q(x,y)=\pi(y)Q(y,x)\), with \(\pi(x)>0\). Initial laws are probability distributions; no assumption of initial thermal Gibbs form or componentwise temperature ordering is made. The zero bound is only for the Pearson \(\chi^2\) (stationary-weighted squared Hilbert) distance gap, **not** Kullback–Leibler relative entropy, total variation, temperature, energy or a nonreversible chain. In the constructive part initial laws have full support, and the urn dynamics are fixed independently of the selected times.

## Proof

**1. Upper bound, including repeated eigenvalues.** On functions of the state, the detailed-balance generator is self-adjoint in \(L^2(\pi)\) and has spectral values \(0,-\lambda_1,\ldots\) with positive nonstationary decay rates. Write the density departures \(f_p=p/\pi-1\), \(f_q=q/\pi-1\). In an orthonormal eigenbasis their time evolutions are sums of decaying eigenmodes. Orthogonality yields
\[\Delta(t)=\sum_{\lambda>0}c_\lambda e^{-2\lambda t},\qquad c_\lambda=\|E_\lambda f_p\|_{L^2(\pi)}^2-\|E_\lambda f_q\|_{L^2(\pi)}^2,\]
where \(E_\lambda\) is the **whole eigenspace projector**, so no spurious multiplicity is counted. If every \(c_\lambda=0\), the gap vanishes identically. Otherwise keep the \(m\) distinct rates with nonzero coefficients. A nonzero real linear combination of \(m\) exponentials with distinct real exponents has at most \(m-1\) distinct real zeros. For completeness, divide by the slowest exponential; the resulting function has a nonzero constant plus \(m-1\) decaying exponentials. Its derivative is a combination of at most \(m-1\) exponentials; induction and Rolle's theorem bound its zeros, and hence those of the original function. As \(m\le n-1\), the upper bound follows. Strictly positive times are a subset of all real times.

**2. Exact spectrum of one fixed urn.** Put \(N=n-1\) and take the birth–death generator on \(k\in\{0,\ldots,N\}\),
\[(Qf)(k)=(N-k)[f(k+1)-f(k)]+k[f(k-1)-f(k)],\]
with boundary terms omitted. Its strictly positive equilibrium is \(\pi(k)=2^{-N}\binom Nk\) and satisfies detailed balance. Define the Krawtchouk coefficients \(K_j(k)\) by
\[G_k(z)=(1-z)^k(1+z)^{N-k}=\sum_{j=0}^NK_j(k)z^j.\]
Direct substitution gives \(QG_k(z)=-2z\partial_zG_k(z)\), so \(QK_j=-2jK_j\). Moreover,
\[\sum_{k=0}^N\pi(k)G_k(z)G_k(w)=(1+zw)^N,\]
so \(\sum_k\pi(k)K_j(k)K_\ell(k)=\binom Nj\mathbf1_{\{j=\ell\}}\). Therefore \(\phi_j(k)=K_j(k)/\sqrt{\binom Nj}\), for \(1\le j\le N\), form a mean-zero orthonormal set with distinct decay rates \(2j\).

**3. Inverse design of all maximum-size reversal calendars.** Choose any distinct prescribed positive times \(\tau_1,\ldots,\tau_{N-1}\) and set \(r_i=e^{-4\tau_i}\in(0,1)\). Expand
\[H(z)=\prod_{i=1}^{N-1}(z-r_i)=\sum_{j=1}^{N}c_jz^{j-1}.\]
Take \(a_j=\sqrt{\max(c_j,0)}\), \(b_j=\sqrt{\max(-c_j,0)}\), so \(a_j^2-b_j^2=c_j\). Define
\[p(k)=\pi(k)\left[1+\varepsilon\sum_{j=1}^{N}a_j\phi_j(k)\right],\qquad q(k)=\pi(k)\left[1+\varepsilon\sum_{j=1}^{N}b_j\phi_j(k)\right].\]
The nonconstant eigenfunctions have zero \(\pi\)-mean, so both laws are normalized. Since the state space is finite, choosing \(\varepsilon>0\) smaller than the reciprocal of one plus the maximum absolute value of either finite eigenfunction sum makes **every** probability strictly positive. Orthogonality and the eigenvalue formula now give the exact identity
\[\Delta(t)=\varepsilon^2\sum_{j=1}^{N}c_je^{-4jt}=\varepsilon^2e^{-4t}H(e^{-4t}).\]
The map \(t\mapsto e^{-4t}\) is strictly decreasing and bijects positive time with \((0,1)\). Since all factors of \(H\) are distinct, the complete set of positive zeros is precisely the prescribed \(\tau_i\), and every zero changes sign. The empty-product case \(N=1\) gives no reversal, as required.

**4. Four-state independent-spin witness.** With the specified spin flip rates, the three Walsh modes \(a,b,ab\) have decay rates \(2,4,6\). The two preparations excite coefficients \((\frac14\frac{12}{25},0,\frac14)\) and \((0,\frac14,0)\), respectively. Orthogonality gives the displayed polynomial. The four preparation probabilities are positive: the smallest is \(63/400\) for \(p\) and \(3/16\) for \(q\). Thus the example is genuinely reversible, normalized and fully supported. No chain with at most three states can exhibit two isolated \(\chi^2\) reversals by part 1.

## Verification

The self-contained Python 3 file `verify.py` uses exact rational arithmetic to check the Ehrenfest generator eigen-equations and Krawtchouk orthogonality for \(1\le N\le11\), plus arbitrary rational crossing-polynomial factorization identities at those sizes. It independently checks the exact four-state stationary laws, Walsh eigenmodes, two-crossing factorization, and nine independently computed spin-transition-semigroup values, all within \(10^{-13}\) absolute difference. The output was `PASS` for each test. The all-\(n\) claims depend on the symbolic arguments above, not on finite tests.

Reproduce with `python3 verify.py`; only the standard library is needed.

## Relationship to prior work

The reversible spectral decomposition and squared-modal relaxation mechanism are classical and are explicitly used in Ben-Abdallah (2026), Avitan–Factor–Gelbwaser-Klimovsky (2026), and Pardhi–Abbas–Das (2026). Taye (2026) gives robust finite-time **relative-entropy** crossing bounds. Griffiths (2016) and Ascione–Leonenko–Pirozzi (2021) establish the Krawtchouk/Ehrenfest spectral framework, and the classical exponential Chebyshev zero-count property is not presented as new. The contribution isolated here is the **sharp all-finite-state Pearson-distance reversal cap**, **fixed-model inverse design of any maximal crossing-time calendar using fully supported preparations**, and the **minimal four-state two-spin exact double-reversal witness**. These conclusions are not implied by published single-crossing examples or the known modal expansion without the sharpness and preparation-realizability arguments.

## Limitations

This is a statement about ordering in one specified statistical distance, not cooling of physical water or a universal thermodynamic Mpemba effect. The constructed preparations are potentially fine-tuned and need not lie on a one-parameter Gibbs temperature family. The theorem does not apply to Kullback–Leibler divergence, for which modal terms mix nonlinearly, nor to nonreversible chains or infinite-dimensional diffusions. The zero-count upper bound is a standard property of real exponentials; publication priority of the complete inverse-design conclusion has not been independently certified.

## References

1. U. Pardhi, S. Abbas and M. Das, *Mathematical analysis of the Markovian Mpemba effect*, first public 6 November 2026, https://arxiv.org/abs/2611.09391 .
2. P. Ben-Abdallah, *Mpemba Effect in Many-Body Systems Near Equilibrium*, 2026, https://arxiv.org/abs/2603.11707 .
3. I. Avitan, R. Factor and D. Gelbwaser-Klimovsky, *Necessary conditions for the Markovian Mpemba effect*, 2026, https://arxiv.org/html/2603.04567v1 .
4. M. Taye, *Finite-time Mpemba crossings with imperfect preparation in reversible Markov systems*, 2026, https://arxiv.org/abs/2610.41591 .
5. R. Griffiths, *Multivariate Krawtchouk Polynomials and Composition Birth and Death Processes*, Symmetry **8**, 33 (2016), https://doi.org/10.3390/sym8050033 .
6. G. Ascione, N. Leonenko and E. Pirozzi, *Non-local Solvable Birth–Death Processes*, Journal of Theoretical Probability, first published 2021, https://doi.org/10.1007/s10959-021-01087-4 .
7. *Chebyshev system*, Encyclopedia of Mathematics, https://encyclopediaofmath.org/wiki/Chebyshev_system .
