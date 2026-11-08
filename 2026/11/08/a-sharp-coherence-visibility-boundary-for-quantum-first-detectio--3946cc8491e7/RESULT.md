# A sharp coherence-visibility boundary for quantum first-detection stochastic order

## Finding

**Theorem (rate-uniform ordering and its sharp breakdown).** Consider a two-level quantum system prepared in the basis state \(\lvert 0\rangle\), evolving unitarily between independent Poissonian projective interrogations of rate \(r>0\). Compare the *transition* first-detection time \(T_{\mathrm{tr}}\), which detects \(\lvert 1\rangle\), with the *return* first-detection time \(T_{\mathrm{ret}}\), which detects \(\lvert 0\rangle\). Let the nonzero energy gap be \(\omega>0\), set \(\hbar=1\), and write the transition probability after free evolution of duration \(t\) as
\[
p(t)=a\sin^2(\omega t/2),\qquad 0<a\le 1.
\]
Let \(z_*\in(\pi,3\pi/2)\) be the unique solution of \(\tan z_*=z_*\), and put
\[
a_* = \frac{1}{1-\sin z_*/z_*}=0.8215349763788107\ldots.
\]
Then the following are equivalent:

1. \(0<a\le a_*\).
2. For **every** Poisson interrogation rate \(r>0\) and **every** \(t\ge0\),
\[
\Pr(T_{\mathrm{ret}}>t)\le\Pr(T_{\mathrm{tr}}>t).
\]

For every \(a>a_*\), there is an \(r_0(a,\omega)>0\) such that, for **every** \(0<r<r_0(a,\omega)\), these two survival functions cross: the return-detection survival is initially smaller, but exceeds the transition-detection survival at \(t=z_*/\omega\). Nevertheless, for **every** \(0<a\le1\), \(r>0\), and \(s>0\),
\[
\mathbb E[e^{-sT_{\mathrm{ret}}}]>\mathbb E[e^{-sT_{\mathrm{tr}}}],
\]
so the return first-detection time is strictly smaller in Laplace-transform order even in the survival-crossing regime. The known means satisfy
\[
\mathbb ET_{\mathrm{ret}}=\frac2r
<\mathbb ET_{\mathrm{tr}}=\frac{2(r^2+\omega^2)}{a r\omega^2}.
\]

The distinctive contribution is the exact sharp visibility boundary separating rate-uniform first-order stochastic dominance from a regime with finite-time reversal despite persistent Laplace-transform ordering; the underlying renewal transforms and mean formulas are previously known.

## Assumptions and scope

Let \(H\) be a time-independent Hermitian \(2\times2\) matrix with nonzero off-diagonal entry in the orthonormal preparation/detection basis \(\{\lvert0\rangle,\lvert1\rangle\}\). With its two distinct energies \(E_+>E_-\), define \(\omega=E_+-E_-\) and \(a=4|\langle0|H|1\rangle|^2/\omega^2\). The spectral identity for a two-level unitary gives \(a\in(0,1]\) and the displayed \(p(t)\). Independent waiting times between measurement attempts have density \(r e^{-rt}\), and each unsuccessful ideal rank-one projective measurement collapses the state onto the one-dimensional complementary subspace. The process stops on the first successful measurement. There are no intervening reservoirs, additional resets, dark states, or detector inefficiencies.

The two protocols start from the same state \(\lvert0\rangle\) and use the same rate \(r\) and Hamiltonian, but different projective targets. Their detection times are nonnegative and almost surely finite because \(a,r>0\).

## Proof

**1. Renewal kernels from two-level unitarity.** Since the two-level transition probabilities satisfy \(p_{01}(t)=p_{10}(t)=p(t)\), define the nonnegative time densities
\[
K(t)=r e^{-rt}p(t),\qquad L(t)=r e^{-rt}(1-p(t)).
\]
In the transition experiment, a failed measurement leaves the system in \(\lvert0\rangle\), so its first-detection density \(f_{\mathrm{tr}}\) satisfies \(f_{\mathrm{tr}}=K+L*f_{\mathrm{tr}}\). In the return experiment, the first interrogation succeeds with density \(L\); if it fails, the post-measurement state is \(\lvert1\rangle\), and subsequent detection of \(\lvert0\rangle\) has the same renewal law as transition detection. Hence \(f_{\mathrm{ret}}=L+K*f_{\mathrm{tr}}\). Here convolution is on \([0,\infty)\).

**2. Exact survival-difference convolution.** Write hats for Laplace transforms in time, and let \(h(s)=r/(r+s)=\widehat K(s)+\widehat L(s)\). The two renewal equations give
\[
\widehat f_{\mathrm{tr}}=\frac{\widehat K}{1-\widehat L},\quad
\widehat f_{\mathrm{ret}}=\widehat L+\widehat K\widehat f_{\mathrm{tr}},\quad
\widehat f_{\mathrm{ret}}-\widehat f_{\mathrm{tr}}=\frac{(1-h)(\widehat L-\widehat K)}{1-\widehat L}.
\]
Since \(S_i(t)=\Pr(T_i>t)\), the Laplace transform of \(S_{\mathrm{tr}}-S_{\mathrm{ret}}\) is \((\widehat f_{\mathrm{ret}}-\widehat f_{\mathrm{tr}})/s\). Using \((1-h)/s=1/(r+s)\), inverting gives
\[
S_{\mathrm{tr}}-S_{\mathrm{ret}}
=G_r*\left(\delta_0+\sum_{n\ge1} L^{*n}\right),\qquad
G_r(t)=r e^{-rt}\left((1-a)t+\frac a\omega\sin(\omega t)\right).
\]
The geometric convolution series converges on every finite time interval, since \(L\ge0\) and \(\int_0^\infty L(t)dt<1\). This equality is between continuous functions for \(t>0\), with value zero at \(t=0\).

**3. Sign of the convolution seed and the sharp threshold.** Put \(x=\omega t\). The factor in parentheses in \(G_r(t)\) has the sign of \((1-a)x+a\sin x\). It is nonnegative for all \(x\ge0\) precisely when
\[
\frac{1-a}{a}\ge\sup_{x>0}\left(-\frac{\sin x}{x}\right).
\]
This global supremum is \(-\sin z_*/z_*\): it is zero or negative on \((0,\pi)\), and on \((\pi,2\pi)\) it has one maximum where \(\tan x=x\). For \(x\ge2\pi\) its value is at most \(1/(2\pi)\), smaller than its value \(2/(3\pi)\) at \(x=3\pi/2\). Thus the supremum occurs uniquely at \(z_*\), proving that the seed \(G_r\) is nonnegative for all times exactly when \(a\le a_*\). Convolution with the nonnegative renewal measure then proves \(S_{\mathrm{tr}}\ge S_{\mathrm{ret}}\) for every rate and time whenever \(a\le a_*\).

**4. Necessity of the visibility bound.** For fixed \(t\) and \(r\downarrow0\), the renewal kernel \(L\) has bounded-on-compacts size \(O(r)\) and its repeated convolution contributes \(O(r)\) beyond the identity term. Therefore, uniformly for \(t\) in any fixed compact interval,
\[
S_{\mathrm{tr}}(t)-S_{\mathrm{ret}}(t)
=r\left((1-a)t+\frac a\omega\sin(\omega t)\right)+O(r^2).
\]
If \(a>a_*\), the bracket is negative at \(t=z_*/\omega\), hence the survival difference is negative there for every sufficiently small positive \(r\). By contrast, as \(t\downarrow0\) at any fixed rate, \(f_{\mathrm{ret}}(0+)=r\) and \(f_{\mathrm{tr}}(0+)=0\), so \(S_{\mathrm{tr}}(t)-S_{\mathrm{ret}}(t)=rt+o(t)>0\) for small positive \(t\). Continuity forces at least one crossing. This proves the converse and the stated reversal.

**5. Persistent Laplace-transform ordering.** Direct integration gives, for \(s\ge0\),
\[
\widehat L(s)-\widehat K(s)=\frac r{r+s}
\left(1-\frac{a\omega^2}{(r+s)^2+\omega^2}\right)>0.
\]
Also \(1-h(s)>0\) for \(s>0\) and \(1-\widehat L(s)>0\). The difference of first-detection Laplace transforms above is therefore strictly positive for every \(s>0\), independently of the survival-order threshold. At zero transform argument, \(\widehat K(0)=a\omega^2/[2(r^2+\omega^2)]\). Differentiating the renewal transforms at zero yields the stated known means, including the strict inequality for \(r>0\).

## Verification

Run `python checker.py` with NumPy and SciPy. The deterministic checker reconstructs transition probabilities from direct \(2\times2\) matrix exponentiation; compares independent integral and rational representations of the exact survival-difference Laplace transform; finds the critical root; tests the nonnegative convolution seed over a wide grid; and evaluates the rational inverse transform through partial fractions for subcritical and supercritical parameters. It produced `PASS 3278 deterministic assertions` when run with the packaged source. For illustration, at \(\omega=1\), \(r=0.1\), and \(t=z_*\), numerical inversion gives \(S_{\mathrm{tr}}-S_{\mathrm{ret}}\approx+0.01725852\) at \(a=0.8\), versus \(-0.06475635\) at \(a=1\).

These are independent numerical consistency checks; they do **not** certify signs at all times or rates. The proof of the universal threshold uses the exact nonnegative convolution representation and an elementary global extremum argument, not finite enumeration. The strict Laplace ordering follows from an exact rational transform inequality.

## Relationship to prior work

Kulkarni and Majumdar (2023) derive the two schemes' first-detection Laplace transforms for arbitrary two-level Hamiltonians and their distinct mean-detection behavior. In particular, their sections 4.1–4.2 contain the predecessor renewals underlying the present calculation. Kessler, Barkai and Ziegler (2020) establish random-probing detection statistics and two-level return identities. Del Vecchio Del Vecchio and Majumdar (2025, updated 2026) study exact detection distributions and optimal mean/tail times on fully connected graphs. These known formulas and model reductions are credited, not claimed as original here. The new statement is a rate-uniform, necessary-and-sufficient **first-order stochastic dominance** threshold and the simultaneous failure of that order with preservation of **Laplace-transform order** above the threshold. The retrieved studies do not state or establish this sharp visibility boundary.

## Limitations

The theorem covers time-independent unitary **two-level** Hamiltonians, **Poisson** observation epochs, ideal projective measurements and identical preparation basis state in the two protocols. It neither asserts a fixed-rate stochastic-order phase boundary nor extends the threshold to non-Poisson clocks, three or more energy levels, mixed initial states or inefficient detectors. The classification is mathematical; no experimental validation or independent audit is claimed. Although the ordering theorem needs a new global-sign argument, its raw renewal transforms are accessible from the earlier exact literature, leaving a residual risk of implicit or independently derived coverage.

## References

1. M. Kulkarni and S. N. Majumdar, *First detection probability in quantum resetting via random projective measurements*, arXiv:2305.15123, first posted 2023-05-24. https://arxiv.org/abs/2305.15123
2. D. A. Kessler, E. Barkai and K. Ziegler, *The first detection time of a quantum state under random probing*, arXiv:2012.01763, first posted 2020-12-03. https://arxiv.org/abs/2012.01763
3. G. Del Vecchio Del Vecchio and S. N. Majumdar, *Optimal detection of quantum states via projective measurements*, arXiv:2509.08556, first posted 2025-09-10. https://arxiv.org/abs/2509.08556
