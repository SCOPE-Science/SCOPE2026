# Faster-outside Strang ordering for two rank-one dissipative generators

## Finding

Let \(u,v\in\mathbb R^d\), \(d\ge2\), be unit vectors, \(P=uu^{\mathsf T}\), \(Q=vv^{\mathsf T}\), and \(z=(u^{\mathsf T}v)^2\). For \(a,b,h>0\), compare the target flow and the two canonical symmetric splittings
\[
E_h=e^{-2h(aP+bQ)},\qquad
S_A=e^{-ahP}e^{-2bhQ}e^{-ahP},\qquad
S_B=e^{-bhQ}e^{-2ahP}e^{-bhQ}.
\]
Put \(X=e^{-ah}\), \(Y=e^{-bh}\), \(\Delta=\sqrt{(a-b)^2+4abz}\), and \(L=e^{-h(a+b)}\sinh(h\Delta)/\Delta\), with \(L=he^{-h(a+b)}\) at \(\Delta=0\). The exact signed difference is
\[
\boxed{\|S_A-E_h\|_{\mathrm F}^2-\|S_B-E_h\|_{\mathrm F}^2
=4Lz(1-z)(1-X)^2(1-Y)^2
\bigl[b\coth(bh/2)-a\coth(ah/2)\bigr].}
\]
For \(0<z<1\) and unequal rates, the splitting with the larger rate on its outer half-steps has strictly smaller one-step Frobenius error for every \(h>0\). Equality for positive \(h\) occurs precisely when \(a=b\) or the projectors commute (\(z=0\) or \(z=1\)). At \(h=0\) both products are exact. In particular, for symmetric heat flow on a three-vertex path with the standard Euclidean site inner product, the normalized edge projectors have \(z=1/4\), and the faster-edge-outer composition minimizes the one-step Frobenius error among these two Strang orders.

## Assumptions and scope

The ambient space is real Euclidean, and the rank-one projectors are orthogonal projectors. The matrix Frobenius metric includes all common invariant directions. The two schemes have the same operator time budget and number of exponential factors. This compares the two canonical Strang orders for one step, not all positive splittings, elapsed-time error after many steps, arbitrary initial states, or operator-norm error. The heat-path example uses symmetric rates across each edge (uniform reversible measure); it does not assign \(z=1/4\) to an arbitrarily weighted reversible chain.

## Proof

For \(z=0\) or \(z=1\) the projectors commute, so both splittings are exact and the right side is zero. Otherwise all nontrivial action occurs on \(U=\operatorname{span}\{u,v\}\). In an orthonormal basis of \(U\),
\[
P=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
Q=\begin{pmatrix}z&w\\w&1-z\end{pmatrix},\qquad w^2=z(1-z).
\]
For \(T=2aP+2bQ-(a+b)I_2\), direct multiplication gives \(T^2=\Delta^2 I_2\). Hence
\[
E_h|_U=e^{-h(a+b)}\cosh(h\Delta)I_2-LT.
\]
By cyclicity of trace, both products have trace \(\operatorname{tr}(e^{-2ahP}e^{-2bhQ})\) on \(U\). Both have determinant \(e^{-2h(a+b)}\) there. They are real symmetric and therefore have equal squared Frobenius norms on \(U\), and both fix \(U^\perp\) pointwise. Writing \(D=S_A-S_B\), the signed squared-error difference is \(-2\operatorname{tr}(E_hD)=2L\operatorname{tr}(TD)\), where the last trace is on \(U\).

To compute the contraction, write \(\alpha=1-X\), \(\beta=1-Y\), \(A=1-X^2\), \(B=1-Y^2\). The rank-one exponential identity \(e^{-sP}=I+(e^{-s}-1)P\) and \(PQP=zP\), \(QPQ=zQ\) give
\[
D=(\alpha B-\beta A)(PQ+QP)-\alpha^2 BzP+\beta^2 AzQ.
\]
Using \(2(\alpha B-\beta A)=\alpha^2 B-\beta^2 A\), \(\operatorname{tr}(PQ)=z\), and the two sandwich identities gives
\[
\operatorname{tr}(PD)=-\beta^2 A z(1-z),\qquad
\operatorname{tr}(QD)=\alpha^2 B z(1-z).
\]
Since \(\operatorname{tr}D=0\), it follows that
\[
\operatorname{tr}(TD)=2z(1-z)(1-X)(1-Y)
\{b(1-X)(1+Y)-a(1+X)(1-Y)\}.
\]
Dividing \(1+X\) by \(1-X\) gives \(\coth(ah/2)\), and the corresponding quotient for \(Y\) gives \(\coth(bh/2)\). This proves the stated factorization.

For fixed \(h>0\), \(r\coth(rh/2)\) is strictly increasing on \((0,\infty)\): with \(s=rh/2\), the derivative has the sign of \(\sinh(s)\cosh(s)-s>0\). The positivity of the other factors for \(0<z<1\) gives the ordering and equality statements. In the symmetric three-vertex path the two normalized incidence vectors are \((1,-1,0)/\sqrt 2\) and \((0,1,-1)/\sqrt 2\), with squared inner product \(1/4\).

For comparison, the expansion at fixed positive \(a,b\) and \(0<z<1\) is
\[
\|S_A-E_h\|_{\mathrm F}^2-\|S_B-E_h\|_{\mathrm F}^2
=\tfrac23 z(1-z)a^2b^2(b^2-a^2)h^6+O(h^7).
\]
The exact factorization, rather than this local expansion, establishes the sign for every positive timestep.

## Verification

The accompanying `verify.py` checks five symbolic matrix identities by polynomial reduction modulo \(w^2-z(1-z)\), 45 exact-rational substitutions, and 120 numerical tests with separately evaluated matrix exponentials in dimensions two to eight. The recorded output is in `verification_output.txt`. The greatest absolute discrepancy in those numerical tests was below \(1.5\times10^{-15}\). The tests supplement the analytic proof and do not establish the all-timestep conclusion on their own.

## Relationship to prior work

Strang's symmetric factorization and the treatment of positivity and structure preservation by Blanes, Iserles and Macnamara [1, 2] supply the method, not the exact difference between the errors of the two orders. Mitra, Diddens and Heuer [3, §3.1.1 and Appendix 1] compare the two Strang orders on a bidirectional three-state diffusion–reaction path using state-probability error and an expansion in the low-diffusion regime. That result addresses a related order choice on a similar path, but not the whole-matrix Frobenius comparison for all positive steps. An exact faster-outer rule is also known for an irreversible serial three-state chain with worst-initial-state total variation [4]; this is the same qualitative ordering under different hypotheses and a different metric, and it does not imply the signed factorization above. A directed-cycle Lie-versus-Strang comparison [5] uses stationary total-variation error. The exact two-state three-factor result [6] permits noncommuting conservative generators and chooses a timestep-dependent allocation; it does not compare the two fixed symmetric orders for Euclidean orthogonal projectors. The distinct result here is the exact signed factorization and its rate ordering in the rank-one orthogonal setting.

## Limitations

No comparison is asserted for arbitrary-rank, nonnormal, time-dependent or nonlinear generators, nor is a stronger norm or long-time ordering inferred. The literature comparison is bounded and does not establish comprehensive historical priority.

## References

1. G. Strang, “On the Construction and Comparison of Difference Schemes,” *SIAM Journal on Numerical Analysis* 5 (1968), https://doi.org/10.1137/0705041.
2. S. Blanes, A. Iserles and S. Macnamara, “Positivity-preserving methods for ordinary differential equations,” arXiv:2102.08242, https://doi.org/10.1051/m2an/2022042.
3. S. Mitra, D. Diddens and A. Heuer, “Improving operator splitting and effective reaction probability for a reactive-step based molecular dynamics workflow,” https://doi.org/10.1007/s10910-026-01780-x.
4. “All-step Strang ordering and exact rate-two resonance for a serial chain,” https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-all-step-strang-ordering-and-exact-rate-two-resonance-for-a-seri--5774d7fcf5b8.
5. “Sharp stationary-error crossover for Lie and Strang splitting on a directed Markov cycle,” https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-sharp-stationary-error-crossover-for-lie-and-strang-splitting-on--7f19d5bc5d02.
6. “An exact positive three-factor split for two-state Markov generators,” https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-an-exact-positive-three-factor-split-for-two-state-markov-genera--9b0eeef7eade.
