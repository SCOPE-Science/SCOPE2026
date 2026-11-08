# Universal midpoint optimality and a sharp three-source Fourier superresolution constant

## Finding
Let \(\mathcal W=\{(\omega_j,w_j):1\le j\le m\}\) be any finite multiset of real frequencies with strictly positive weights, invariant under frequency reflection with equal reflected weights. Normalize \(\sum_jw_j=1\). Put \(\mu_r=\sum_jw_j\omega_j^r\) and suppose \(\Delta=\mu_4-\mu_2^2>0\). For \(-1<t<1\), \(\delta>0\), and \(x=(-1,t,1)\), define the \(m\times3\) Fourier sampling matrix
\[
A_\delta(t)_{j,\ell}=\sqrt{w_j}\,e^{i\omega_j\delta x_\ell},\qquad \ell=1,2,3.
\]
Then for every fixed \(t\in(-1,1)\), as \(\delta\downarrow0\),
\[
\boxed{\lim_{\delta\downarrow0}\frac{\sigma_{\min}(A_\delta(t))}{\delta^2}=\sqrt\Delta\,\frac{1-t^2}{\sqrt{6+2t^2}}.}
\]
The limit is uniform on each compact subinterval of \((-1,1)\). Of all strictly interior third-source placements between two sources a fixed distance \(2\delta\) apart, the **unique maximizer of this leading-order recovery gain** is the midpoint \(t=0\), independently of the symmetric frequency weights. The sharp leading condition-number coefficient is
\[
\lim_{\delta\downarrow0}\delta^2\kappa_2(A_\delta(t))
=\frac{\sqrt{3(6+2t^2)}}{(1-t^2)\sqrt\Delta},
\]
and its unique minimum occurs at \(t=0\), where it equals \(3\sqrt2/\sqrt\Delta\).

For the concrete, normalized contiguous Fourier aperture \(\omega_j=-N,\ldots,N\), \(w_j=(2N+1)^{-1}\), \(N\ge1\), the midpoint's exact leading coefficient becomes
\[
\boxed{\lim_{\delta\downarrow0}\frac{\sigma_{\min}(A_\delta(0))}{\delta^2}
=\sqrt{\frac{N(N+1)(4N^2+4N-3)}{270}}.}
\]
All limits hold for fixed finite aperture, not in a simultaneous bandwidth/separation limit.

## Assumptions and scope
The frequency weights are positive, finite, normalized, and reflection-symmetric. The strict variance condition \(\Delta>0\) is equivalent to having at least two distinct sampled values of \(\omega^2\), and ensures that the three low-order moment vectors are linearly independent. The endpoints of the source cluster are fixed at \(-\delta\) and \(+\delta\). The parameter \(t\) specifies a third distinct interior source. All singular values and condition numbers refer to the linear complex-amplitude sampling matrix, with Euclidean source coefficient norm and weighted measurement norm. They are **not** nonlinear location-estimation minimax errors.

## Proof
Set \(u_r=(\sqrt{w_j}(i\omega_j)^r)_j\), and \(v_r=(x_1^r,x_2^r,x_3^r)\), for \(r=0,1,2\). Termwise Taylor expansion yields
\[
A_\delta=u_0v_0^\top+\delta u_1v_1^\top+\frac{\delta^2}{2}u_2v_2^\top+O(\delta^3)
\]
in operator norm for each fixed aperture, uniformly for \(t\) in bounded sets. Reflection symmetry gives \(\mu_1=\mu_3=0\), hence
\[
\|u_0\wedge u_1\|=\sqrt{\mu_2},\qquad
\|u_0\wedge u_1\wedge u_2\|=\sqrt{\mu_2(\mu_4-\mu_2^2)}.
\]
Direct three-dimensional algebra gives
\[
\|v_0\wedge v_1\|=\sqrt{6+2t^2},\qquad
|\det(v_0,v_1,v_2)|=2(1-t^2).
\]
Writing \(s_1\ge s_2\ge s_3\) for the singular values of \(A_\delta\), the leading exterior-power expansions consequently give
\[
\begin{aligned}
s_1&=\sqrt3+O(\delta),\\
s_1s_2&=\delta\sqrt{\mu_2}\sqrt{6+2t^2}+O(\delta^2),\\
s_1s_2s_3&=\delta^3(1-t^2)\sqrt{\mu_2\Delta}+O(\delta^4).
\end{aligned}
\]
Here the second formula follows because the norm of the second exterior-power operator equals \(s_1s_2\) (and the third similarly); the displayed leading wedge coefficient has rank one. In the third formula the factor \(1/2\) from the quadratic Taylor coefficient cancels the factor \(2\) from the node Vandermonde determinant. Since \(\mu_2>0\) and \(6+2t^2>0\), division gives
\[
s_3=\delta^2\sqrt\Delta\frac{1-t^2}{\sqrt{6+2t^2}}+O(\delta^3).
\]
All Taylor remainders are uniform for \(t\) in compact sets; this proves the first claim. Dividing the limiting largest singular value by \(s_3\) proves the condition-number formula. Finally, for \(0<t<1\), the logarithmic derivative of \(f(t)=(1-t^2)/\sqrt{6+2t^2}\) is
\[
\frac{f'(t)}{f(t)}=-\frac{2t}{1-t^2}-\frac{2t}{6+2t^2}<0.
\]
As \(f\) is even, its unique maximizer on \((-1,1)\) is \(0\). Thus midpoint placement optimizes the leading term globally over *fixed* normalized shapes; the argument does not assert exact optimality at every nonzero \(\delta\).

For the integer aperture, \(\mu_2=N(N+1)/3\) and \(\mu_4=N(N+1)(3N^2+3N-1)/15\). Subtraction yields
\[
\Delta=\frac{N(N+1)(4N^2+4N-3)}{45};
\]
substituting \(t=0\) gives the stated coefficient.

## Verification
A standalone Python checker `check.py` uses 75-digit arithmetic to reconstruct independent weighted Gram matrices directly from the source locations (not the asymptotic spectral formula). It checks the predicted leading constant for five contiguous apertures and five offsets, as well as two nonuniform apodizations, against small separations; it separately verifies integer-aperture moment identities. It reports `APODIZED_CLUSTER_CHECKS_PASS 186`. These computations test examples, not the universal quantifier or the limit proof.

To reproduce, install `mpmath`, then execute `python check.py` from the folder containing this result. No external data files are needed.

## Relationship to prior work
Batenkov–Demanet–Goldman–Yomdin (2018, arXiv:1809.00658) establish the optimal *order* of the smallest singular value of Fourier matrices with clustered nodes. Batenkov–Diederichs–Goldman–Yomdin (2019, arXiv:1909.01927) give general two-sided singular-value scale bounds for single clusters and multi-cluster decompositions; their Theorem 2.3 does not identify this exact constant. Kunis–Nagel (2020) analyze *pairs* of nearly colliding nodes. Classical prolate-matrix results already analyze equispaced clusters, so the midpoint example and the quadratic rate alone are not asserted new. The distinction here is the **exact leading coefficient for all reflection-symmetric weighted apertures and all three-source interior placements, with weight-independent uniqueness of the midpoint as the best leading-order design**.

## Limitations
Only a fixed finite symmetric frequency aperture, a fixed normalized three-source shape, and the small-separation limit are established. No uniform remainder for frequency sets whose bandwidth grows as separation shrinks is claimed. The theorem does not optimize the frequency weights, handle four or more sources, or quantify nonlinear support recovery. Existing results may encode the leading coefficient in a different interpolation formulation; historical priority requires external scrutiny.

## References
- D. Batenkov, L. Demanet, G. Goldman, Y. Yomdin, *Conditioning of partial nonuniform Fourier matrices with clustered nodes*, arXiv:1809.00658 (first public 2018-09-03), https://arxiv.org/abs/1809.00658.
- D. Batenkov, B. Diederichs, G. Goldman, Y. Yomdin, *The spectral properties of Vandermonde matrices with clustered nodes*, arXiv:1909.01927 (2019), https://arxiv.org/abs/1909.01927.
- S. Kunis and D. Nagel, *On the condition number of Vandermonde matrices with pairs of nearly-colliding nodes*, *Numerical Algorithms* (first published 2020-07-21), https://doi.org/10.1007/s11075-020-00974-x.
