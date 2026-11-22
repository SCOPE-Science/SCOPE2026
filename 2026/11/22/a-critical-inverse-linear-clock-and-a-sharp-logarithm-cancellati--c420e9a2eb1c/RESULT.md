# A critical inverse-linear clock and a sharp logarithm-cancellation resonance in a five-lag rational map

## Finding
Let \(b>0\), put \(a=b+1\), and prescribe any five strictly positive real numbers \(x_{-4},x_{-3},x_{-2},x_{-1},x_0\). Define for every integer \(n\geq0\)
\[
x_{n+1}=\frac{b x_n+x_{n-4}}{b+1+x_{n-1}}.
\]
Then \(x_n\to0\), and there is a finite, initial-history-dependent real constant \(C\) such that
\[
\boxed{\frac1{x_n}=\frac{n}{b+5}+\frac{b-15}{(b+5)^2}\log n+C+o(1)}
\qquad(n\to\infty).
\]
In particular \(n x_n\to b+5\). The uncorrected finite-part limit \(\lim_{n\to\infty}(1/x_n-n/(b+5))\) is finite **if and only if** \(b=15\). It tends to \(-\infty\) for \(0<b<15\) and to \(+\infty\) for \(b>15\). This identifies a unique exact logarithm-cancellation resonance at the nonhyperbolic extinction boundary.

## Assumptions and scope
All iterates are formed over the real numbers with the **same fixed** \(b>0\) and \(a=b+1\); the history is strictly positive, not assumed small. The relevant phase-space map on \((0,\infty)^5\) is
\[
T(s_0,s_1,s_2,s_3,s_4)=\left(\frac{b s_0+s_4}{b+1+s_1},s_0,s_1,s_2,s_3\right),
\]
where \(s_j=x_{n-j}\). The equality \(a=b+1\) is the extinction/fixed-point threshold: at \(a<b+1\) a strictly positive equilibrium \(b+1-a\) exists, whereas at equality the positive equilibrium collides with zero. No claim is made for nonpositive histories, noncritical \(a\), or a distinct delay arrangement.

## Proof
**1. A global strict Lyapunov quantity.** Set \(d=b+5\), \(c=b+1\), and
\[
W_n=c x_n+x_{n-1}+x_{n-2}+x_{n-3}+x_{n-4}.
\]
Multiplying the recurrence by its denominator gives the exact identity
\[
W_n-W_{n+1}=x_{n-1}x_{n+1}>0.
\]
Hence \(W_n\) decreases and remains nonnegative; the five-dimensional orbit remains in a compact subset of the nonnegative orthant and is forward-defined. If its limit were \(L>0\), every point in the nonempty omega-limit set would have \(W=L\), and every forward iterate of that point would also have \(W=L\). But every nonzero nonnegative phase vector reaches a strictly positive phase vector after finitely many steps: the directed dependency graph has edges from lag zero and lag four to the new leading coordinate, has all four shift edges, and has a self-loop of positive weight \(b\). It is strongly connected and aperiodic, hence its nonnegative adjacency matrix is primitive. The rational map has precisely the same positivity propagation as that adjacency matrix because every denominator is positive. Thus an omega-limit orbit through a nonzero state must eventually make \(x_{n-1}x_{n+1}>0\), strictly decreasing \(W\), contradiction. Hence \(W_n\to0\) and \(x_n\to0\) for every positive history.

**2. Primitive linear center and a positive slow coordinate.** The derivative \(M=DT(0)\) has top row \((b/c,0,0,0,1/c)\) and four shift rows. It is a primitive stochastic matrix: \(M\boldsymbol1=\boldsymbol1\), one eigenvalue is the simple unit root, and all other eigenvalues have modulus less than one. Indeed, a unit-circle root of \(c\lambda^5-b\lambda^4-1=0\) must satisfy equality in the triangle inequality and therefore \(\lambda^4=\lambda^5=1\), implying \(\lambda=1\); roots outside the unit disk are excluded by the same inequality. The stationary left vector, normalized to pair to one with \(\boldsymbol1\), is
\[
\pi=\frac1d(c,1,1,1,1),\qquad U_n=\pi s_n=\frac{W_n}{d}>0.
\]
The exact drift is
\[
U_{n+1}-U_n=-\frac{x_{n-1}x_{n+1}}{d}.
\]
Since each phase coordinate is at most \(dU_n\), both factors are \(O(U_n)\), so \(0\le U_n-U_{n+1}\le K U_n^2\), for a constant depending on \(b\). Thus \(U_n\to0\), \(U_{n+1}/U_n\to1\), and \(U_n\ge K_1/(n+K_2)\) for sufficiently large \(n\). In particular no strictly positive history can hide in a purely exponentially decaying strong-stable mode.

**3. Second-order stable slaving, with quantitative error.** Write \(P=\boldsymbol1\pi\), \(Q=I-P\). As \(M\) contracts the subspace \(\pi v=0\), the recurrence
\[
Qs_{n+1}=M Qs_n+Q\big(T(s_n)-Ms_n\big)
\]
and \(T(s)-Ms=O(\|s\|^2)=O(U_n^2)\) show \(Qs_n=O(U_n^2)\). To see this rigorously without presuming a convergence rate, choose a fixed \(k\) for which \(\|M^kQ\|<1/2\). Over \(k\) steps, nonlinear forcing is \(O(U_n^2)\); meanwhile \(U_{n+k}/U_n\to1\), so the normalized stable-component inequality is eventually strictly contractive. Applying it on each residue class modulo \(k\) gives the estimate.

Define the column vector \(\alpha\) by
\[
\alpha_j=\frac{j(b+5)-10}{(b+5)^2},\qquad j=0,1,2,3,4.
\]
It satisfies \(\pi\alpha=0\), and direct substitution shows
\[
T(U\boldsymbol1+\alpha U^2)
=(U-qU^2)\boldsymbol1+\alpha(U-qU^2)^2+O(U^3),
\qquad q=\frac1{b+5}.
\]
Equivalently, \(\alpha_j=\alpha_0+jq\) and \(\alpha_0=-10/(b+5)^2\). Subtracting this quadratic approximate invariant graph from the actual orbit gives a stable recurrence whose forcing is \(O(U_n^3)\), whose derivative on the stable subspace is \(M+O(U_n)\), and whose normalized \(k\)-step contraction remains strict. Consequently the sharper estimate holds for every positive trajectory:
\[
s_n=U_n\boldsymbol1+\alpha U_n^2+O(U_n^3).
\]
The preceding fixed-block argument proves both error estimates; it uses only finite-dimensional exponential contraction and \(U_{n+k}/U_n\to1\), not an assumed asymptotic formula.

**4. The cubic center drift.** The previous estimate yields
\[
x_{n-1}=U_n+\alpha_1U_n^2+O(U_n^3),\qquad
x_{n+1}=U_n+(\alpha_0-q)U_n^2+O(U_n^3).
\]
Since \(\alpha_1=\alpha_0+q\), their product is \(U_n^2+2\alpha_0U_n^3+O(U_n^4)\). Substitution into the *exact* Lyapunov drift therefore proves
\[
U_{n+1}=U_n-\frac{U_n^2}{d}+\frac{20U_n^3}{d^3}+O(U_n^4).
\]
It follows that
\[
\frac1{U_{n+1}}-\frac1{U_n}
=\frac1d+\frac{b-15}{d^3}U_n+O(U_n^2).
\]
The reciprocal increment tends to \(1/d\), so \(U_n\sim d/n\). In particular \(U_n=O(1/n)\), and summing the last identity first gives \(1/U_n=n/d+O(\log n)\), hence
\[
U_n=\frac d n+O\!\left(\frac{\log n}{n^2}\right).
\]
As a result, both \(\sum_n U_n^2\) and \(\sum_n(U_n-d/n)\) converge absolutely. After subtracting the harmonic logarithm, the reciprocal-increment remainder is summable, giving the **finite** limit
\[
\lim_{n\to\infty}\left(\frac1{U_n}-\frac nd-\frac{b-15}{d^2}\log n\right)=C_U\in\mathbb R.
\]
Finally, \(x_n=U_n+\alpha_0U_n^2+O(U_n^3)\) gives \(1/x_n=1/U_n-\alpha_0+o(1)\), proving the stated formula with \(C=C_U-\alpha_0\). The logarithmic coefficient vanishes exactly at \(b=15\), with all other claims following directly.

## Verification
The standalone `checker.py` verifies symbolically over \(\mathbb Q(b)\): the weighted identity \(W_n-W_{n+1}=x_{n-1}x_{n+1}\), the stationary projection and quadratic slaving identities, the cubic slow drift coefficient \(20/(b+5)^3\), and the resulting logarithmic coefficient \((b-15)/(b+5)^2\). It also runs finite-time diagnostics for \(b=1,5,15,25\) to test numerical scales without treating them as proofs. Run `python checker.py` with Python 3 and SymPy. The proof above supplies the global and infinite-time statements; computation alone does not.

## Relationship to prior work
Khaliq, Mustafa, Ibrahim and collaborators (2023) introduce precisely the recurrence with general positive parameters and study equilibria, positive-fixed-point stability, and Neimark–Sacker bifurcations. The present result concerns the **critical zero-equilibrium boundary** \(a=b+1\), all positive histories, and the two-term reciprocal decay clock; those implications are not supplied by the inspected source results.

Chatterjee and Hassan (2018) investigate \(y_{n+1}=(p y_{n-\ell}+y_{n-k})/(q+y_{n-k})\), whose denominator lag must coincide with a numerator lag. In the present map the numerator uses lags zero and four while the denominator uses lag one. That published family's global extinction theorem therefore does not directly imply this result, and it does not present the claimed logarithmic coefficient. The earlier higher-order rational model of Khaliq and collaborators (2020) is also structurally different. Indexed comparisons include finite-memory fractional logistic extinction and other unrelated parabolic maps, none providing a reduction that implies this exact five-lag resonance. The searches and source inspections are recorded in `AUDIT.json`. Unindexed equivalent or more general work remains a genuine originality risk.

## Limitations
The result is an exact theorem only for \(b>0\), \(a=b+1\), and strictly positive histories. The parameter \(b=0\) is excluded because the linear center is no longer primitive and synchrony can fail. It does not prove basin structure away from the critical hypersurface, arbitrary initial signs, stochastic perturbation stability, or independent validation. The source and comparative literature are not claimed to have been exhaustively indexed.

## References
1. A. Khaliq, I. Mustafa, T. F. Ibrahim, W. M. Osman, B. R. Al-Sinan, A. A. Dawood and M. Y. Juma, *Stability and Bifurcation Analysis of Fifth-Order Nonlinear Fractional Difference Equation*, Fractal and Fractional **7** (2023), 113. First public date 2023-01-23. https://doi.org/10.3390/fractalfract7020113 .
2. E. Chatterjee and Sk. S. Hassan, *On the asymptotic character of a generalized rational difference equation*, Discrete and Continuous Dynamical Systems **38** (2018), 1707–1718. https://doi.org/10.3934/dcds.2018070 .
3. A. Khaliq, H. S. Alayachi, M. S. M. Noorani and A. Q. Khan, *On Stability Analysis of Higher-Order Rational Difference Equation*, Discrete Dynamics in Nature and Society (2020), article 3094185. https://doi.org/10.1155/2020/3094185 .
