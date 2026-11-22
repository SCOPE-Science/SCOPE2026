# Faster-outside Strang ordering for two rank-one dissipative generators

## Finding
For unit real vectors \(u,v\in\mathbb R^d\), \(d\ge 2\), let \(P=uu^{\mathsf T}\), \(Q=vv^{\mathsf T}\), and \(z=(u^{\mathsf T}v)^2\). Fix positive rates \(a,b\) and step \(h>0\). The target flow and two symmetric splittings are
\[
 E_h=e^{-2h(aP+bQ)},\quad
 S_A=e^{-ahP}e^{-2bhQ}e^{-ahP},\quad
 S_B=e^{-bhQ}e^{-2ahP}e^{-bhQ}.
\]
With \(X=e^{-ah}\), \(Y=e^{-bh}\), \(\Delta=\sqrt{(a-b)^2+4abz}\) and \(L=e^{-h(a+b)}\sinh(h\Delta)/\Delta\), the exact signed difference of squared Frobenius errors is
\[
 \boxed{\|S_A-E_h\|_{\mathrm F}^2-\|S_B-E_h\|_{\mathrm F}^2
 =4Lz(1-z)(1-X)^2(1-Y)^2
 \left[b\coth(bh/2)-a\coth(ah/2)\right].}
\]
For \(0<z<1\), the splitting with the **larger rate on its outer half-steps** has strictly smaller Frobenius error for every positive timestep. Equality occurs precisely when \(a=b\) or the two projectors commute (\(z=0\) or \(z=1\)); at \(h=0\) both are exact. In particular, on a three-site reversible heat path, where the two normalized edge projectors have \(z=1/4\), the faster-edge-outer Strang composition minimizes one-step Frobenius error among the two reversible Strang orders, irrespective of timestep.

## Assumptions and scope
The ambient space is a finite-dimensional real Euclidean space; the rank-one projectors are orthogonal projectors. Rates and timesteps are strictly positive; no coupling-angle lower bound is required. The Frobenius metric is computed on the entire matrix including common invariant directions. Both schemes use the same operator time budget and the same number of exponential factors. The strict claim covers only these two canonical Strang compositions, not all positive splitting methods, multiple steps, arbitrary initial conditions, or operator-norm error.

## Proof
If \(z=0\) or \(z=1\), the projectors commute, so both splittings equal the exact exponential. Otherwise all nontrivial action occurs on \(U=\operatorname{span}\{u,v\}\). In an orthonormal basis of \(U\), put
\[
 P=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
 Q=\begin{pmatrix}z&w\\w&1-z\end{pmatrix},\qquad w^2=z(1-z).
\]
Write \(T=2aP+2bQ-(a+b)I_2\). Direct multiplication gives \(T^2=\Delta^2 I_2\), hence
\[
 E_h\big|_U=e^{-h(a+b)}\left[\cosh(h\Delta)I_2-\frac{\sinh(h\Delta)}{\Delta}T\right].
\]
The rank-one exponential identity \(e^{-sP}=I+(e^{-s}-1)P\) gives the two products as polynomials in \(P,Q\). Their traces agree:
\[\operatorname{tr}S_A=\operatorname{tr}S_B
=\operatorname{tr}(e^{-2ahP}e^{-2bhQ}).\]
Both have determinant \(e^{-2h(a+b)}\) on \(U\), so the two real symmetric \(2\times2\) products have equal eigenvalues and equal squared Frobenius norms. The same statements hold on the full space, where both are the identity on \(U^\perp\). Consequently their squared-error difference is \(-2\operatorname{tr}[E_h(S_A-S_B)]\).

Direct multiplication in the displayed basis, eliminating \(w^2\) using \(w^2=z(1-z)\), yields the exact contraction identity
\[
 \operatorname{tr}[T(S_A-S_B)]
 =2z(1-z)(1-X)(1-Y)\{b(1-X)(1+Y)-a(1+X)(1-Y)\}.
\]
Inserting the hyperbolic expression for \(E_h\) gives
\[
 4Lz(1-z)(1-X)(1-Y)\{b(1-X)(1+Y)-a(1+X)(1-Y)\}.
\]
Finally, \((1-X)/(1+X)=\tanh(ah/2)\) and the corresponding identity for \(Y\) turn the braces into
\[(1-X)(1-Y)\{b\coth(bh/2)-a\coth(ah/2)\},\]
proving the boxed formula.

For fixed \(h>0\), the function \(r\mapsto r\coth(rh/2)\) is strictly increasing on \((0,\infty)\): setting \(s=rh/2\), its derivative has the sign of \(\sinh(s)\cosh(s)-s>0\) for \(s>0\). The factor \(L\) and the other nonzero factors are positive when \(0<z<1\). Therefore \(a>b\) makes the displayed error difference negative, and \(a<b\) makes it positive; equality has precisely the asserted cases. In the three-vertex path, normalized edge incidence vectors \((1,-1,0)/\sqrt2\) and \((0,1,-1)/\sqrt2\) have squared inner product \(1/4\), proving the heat-path statement.

For additional local perspective, expansion at fixed positive \(a,b\) and \(0<z<1\) gives
\[
 \|S_A-E_h\|_{\mathrm F}^2-\|S_B-E_h\|_{\mathrm F}^2
 =\frac23z(1-z)a^2b^2(b^2-a^2)h^6+O(h^7).
\]
The all-step sign law is stronger than this local series and follows from the exact identity.

## Verification
The accompanying standalone `verify.py` checks five symbolic matrix identities via exact polynomial reduction modulo \(w^2-z(1-z)\), 45 further exact-rational substitutions, and 120 numerical tests with independently evaluated matrix exponentials in dimensions two to eight. The recorded execution output is in `verification_output.txt`. The greatest absolute discrepancy in the independent numerical comparisons was below \(1.5\times10^{-15}\). These are supplementary checks; the all-dimension, all-step theorem is proved analytically above.

## Relationship to prior work
Strang's classical symmetric factorization supplies the two second-order compositions. Blanes, Iserles and Macnamara (first arXiv version 16 February 2021) discuss splitting for positivity and invariant preservation and provide an appropriate matrix-evolution setting, but their inspected formulations do not give an exact all-step Frobenius comparison between the reversed rank-one Strang products. Related work on Lie/Strang stationary error for directed Markov cycles studies a different stationary distribution and error metric; two-state exact three-factor Markov splitting concerns collinear generators and does not give the strict noncommuting case. The present assertion is the exact signed factorization, the global rate-ordering consequence, and its reversible path application, not the known second-order consistency of Strang splitting.

## Limitations
The comparison is restricted to orthogonal rank-one dissipators and squared Frobenius error of one step. It does not provide an all-initial-state superiority, spectral-norm ordering, or a theorem for arbitrary-rank, nonnormal, time-dependent, or nonlinear generators. Broader historical priority, particularly in exact projector-product comparisons, requires independent comprehensive verification; no claim of external certification is made.

## References
1. G. Strang, “On the Construction and Comparison of Difference Schemes”, *SIAM Journal on Numerical Analysis* 5 (1968), DOI: https://doi.org/10.1137/0705041.
2. S. Blanes, A. Iserles and S. Macnamara, “Positivity-preserving methods for ordinary differential equations”, first public arXiv version 2021-02-16, https://arxiv.org/abs/2102.08242; https://doi.org/10.1051/m2an/2022042.
3. Published comparison on stationary-error crossover for Lie and Strang splitting on a directed Markov cycle, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-stationary-error-crossover-for-lie-and-strang-splitting-on--7f19d5bc5d02.
4. Published comparison on exact positive three-factor splitting for two-state Markov generators, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-an-exact-positive-three-factor-split-for-two-state-markov-genera--9b0eeef7eade.
