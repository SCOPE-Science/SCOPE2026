# All positive \(\tau\) are admissible in the fractional half-space Hardy–Maz’ya remainders
## Finding
For \(d\ge2\), write
\[
\mathbb R^d_+=\{x\in\mathbb R^d:x_d>0\},\qquad
R(x)=\left(x_{d-1}^2+x_d^2\right)^{1/2}.
\]
For \(\beta>0\) and \(\tau>0\), define the remainder weight
\[
w_{\beta,\tau}(x)
=\frac{1}{x_d^{\beta-\tau}R(x)^\tau}
=x_d^{-\beta}\left(\frac{x_d}{R(x)}\right)^\tau.
\]
Since \(0<x_d/R(x)\le1\), the family is pointwise decreasing in \(\tau\):
\[
0<\tau_1\le\tau_2
\quad\Longrightarrow\quad
w_{\beta,\tau_2}(x)\le w_{\beta,\tau_1}(x).
\]
This simple order relation removes the upper restrictions on \(\tau\) in both main remainder theorems of Kijaczko--Szczukiewicz.

For the fractional Gagliardo form, let \(0<s<1\), \(p>1\), and \(d\ge2\). For every \(\tau>0\), there exists \(C_{d,s,p,\tau}>0\) such that
\[
\begin{aligned}
&\int_{\mathbb R^d_+}\int_{\mathbb R^d_+}
\frac{|u(x)-u(y)|^p}{|x-y|^{d+sp}}\,dy\,dx\\
&\qquad\ge
\mathcal D_{d,s,p}\int_{\mathbb R^d_+}\frac{|u(x)|^p}{x_d^{sp}}\,dx
+C_{d,s,p,\tau}\int_{\mathbb R^d_+}|u(x)|^p w_{sp,\tau}(x)\,dx.
\end{aligned}
\]
The test-function class is exactly the one in the source: \(u\in C_c(\mathbb R^d_+)\) when \(sp\ge1\), and \(u\in C_c(\overline{\mathbb R^d_+})\) when \(sp<1\).

For the Sobolev--Bregman form, let \(0<\alpha<2\), \(p>1\), and \(d\ge2\). For every \(\tau>0\), there exists \(C'_{d,\alpha,p,\tau}>0\) such that
\[
\begin{aligned}
&\int_{\mathbb R^d_+}\int_{\mathbb R^d_+}
\frac{(u(x)-u(y))(u(x)^{\langle p-1\rangle}-u(y)^{\langle p-1\rangle})}{|x-y|^{d+\alpha}}\,dy\,dx\\
&\qquad\ge
\mathcal D'_{d,\alpha,p}\int_{\mathbb R^d_+}\frac{|u(x)|^p}{x_d^\alpha}\,dx
+C'_{d,\alpha,p,\tau}\int_{\mathbb R^d_+}|u(x)|^p w_{\alpha,\tau}(x)\,dx.
\end{aligned}
\]
Here \(u\in C_c(\mathbb R^d_+)\) when \(\alpha\ge1\), and \(u\in C_c(\overline{\mathbb R^d_+})\) when \(\alpha<1\).

More generally, if \(C^G_*(\tau)\) and \(C^B_*(\tau)\) denote the largest admissible remainder constants in these two inequalities, respectively, then both are nondecreasing on \((0,\infty)\).

## Assumptions and scope
The statement uses the same sharp Hardy terms, dimensions, exponents, and test-function classes as Theorems 1 and 2 of arXiv:2609.10832v1. It changes only the allowed range of the remainder exponent \(\tau\).

The source proves the Gagliardo remainder for
\[
0<\tau<T_G:=
\begin{cases}
\dfrac{p(sp+1)}{2(p-1)},&p\ge2,\\
2\min\{sp,1\},&1<p<2,
\end{cases}
\]
and the Sobolev--Bregman remainder for \(0<\tau<T_B:=1+\alpha\). Both thresholds are strictly positive. The present argument shows that these are sufficient seed intervals, not upper admissibility boundaries.

## Proof
Fix \(\beta>0\). Because \(R(x)\ge x_d>0\),
\[
q(x):=\frac{x_d}{R(x)}\in(0,1].
\]
The remainder weight factors as
\[
w_{\beta,\tau}(x)=x_d^{-\beta}q(x)^\tau.
\]
Therefore, whenever \(0<\sigma\le\tau\),
\[
w_{\beta,\tau}(x)
=x_d^{-\beta}q(x)^\tau
\le x_d^{-\beta}q(x)^\sigma
=w_{\beta,\sigma}(x)
\]
for every \(x\in\mathbb R^d_+\). Hence
\[
\int_{\mathbb R^d_+}|u|^p w_{\beta,\tau}
\le
\int_{\mathbb R^d_+}|u|^p w_{\beta,\sigma}
\]
for every admissible \(u\).

For the Gagliardo inequality, let \(\tau>0\) be arbitrary and choose
\[
\sigma=\min\left\{\frac{\tau}{2},\frac{T_G}{2}\right\}.
\]
Then \(0<\sigma<T_G\) and \(\sigma<\tau\). Theorem 1 of arXiv:2609.10832v1 provides a positive constant \(C_{d,s,p,\sigma}\) with
\[
I_{s,p}[u]\ge C_{d,s,p,\sigma}
\int_{\mathbb R^d_+}|u|^p w_{sp,\sigma},
\]
where \(I_{s,p}\) is the sharp fractional Hardy difference. By the pointwise comparison,
\[
I_{s,p}[u]\ge C_{d,s,p,\sigma}
\int_{\mathbb R^d_+}|u|^p w_{sp,\tau}.
\]
Thus one may set \(C_{d,s,p,\tau}=C_{d,s,p,\sigma}>0\).

For the Sobolev--Bregman inequality, choose instead
\[
\sigma=\min\left\{\frac{\tau}{2},\frac{1+\alpha}{2}\right\}.
\]
Theorem 2 of the same source gives a positive constant at \(\sigma\), and the identical weight comparison transfers it to \(\tau\).

Finally, if a constant \(C\) is admissible at \(\sigma\), then the same \(C\) is admissible at every \(\tau\ge\sigma\). Taking suprema over admissible constants proves that \(C^G_*(\tau)\) and \(C^B_*(\tau)\) are nondecreasing.

## Verification
The critical identity is exact:
\[
\frac{w_{\beta,\tau_2}(x)}{w_{\beta,\tau_1}(x)}
=
\left(\frac{x_d}{\sqrt{x_{d-1}^2+x_d^2}}\right)^{\tau_2-\tau_1}
\le1
\]
for \(\tau_2\ge\tau_1>0\). No limiting argument, numerical experiment, or regularity assumption beyond the source hypotheses enters this comparison.

The source was checked at the full statements of Theorems 1 and 2 and at its explicit discussion immediately afterward. It proves positivity only on the displayed seed ranges and states that it did not determine whether those \(\tau\)-range assumptions are optimal. Since the test-function classes and sharp Hardy terms are independent of \(\tau\), transferring a positive constant from a smaller exponent introduces no hidden change of domain or normalization.

## Relationship to prior work
Kijaczko and Szczukiewicz establish the two fractional half-space remainder inequalities and give explicit positive constants on restricted intervals of \(\tau\). Immediately after Theorems 1 and 2 they explicitly state that the optimality of the \(\tau\)-range assumptions is unclear. The monotonicity above shows that no finite upper restriction is possible: every positive exponent is admissible once any smaller positive exponent is.

The classical half-space Hardy--Maz’ya inequality of Tidblom treats the analogous codimension-two remainder in the local gradient setting. The same geometric factor \(x_d/R(x)\) appears there, but that result does not state the fractional all-\(\tau\) conclusions above. Frank--Seiringer determine the sharp fractional Hardy constant on a half-space, supplying the sharp Hardy term that the focal source retains; their theorem has no codimension-two remainder parameter \(\tau\).

Targeted source-ID, exact-formula, alias, and implication searches did not locate a published fractional statement asserting admissibility for every \(\tau>0\) or monotonicity of the best remainder constant. Because the proof is short, an equivalent observation may exist implicitly under different terminology; the novelty claim is limited to the stated all-positive-\(\tau\) extension and monotonicity principle.

## Limitations
The result does not determine the numerical sharp values of \(C^G_*(\tau)\) or \(C^B_*(\tau)\); that harder problem remains open. It also does not provide a uniform positive lower bound as \(\tau\) varies, nor does it strengthen the remainder weight for large \(\tau\). Indeed, increasing \(\tau\) makes the factor \((x_d/R(x))^\tau\) smaller away from the vertical axis, which is exactly why the transfer works.

No claim is made for different remainder geometries whose weights are not ordered in the parameter.

## References
1. Michał Kijaczko and Antoni Szczukiewicz, *Fractional Hardy--Maz’ya inequality on a half-space*, arXiv:2609.10832v1, 2026.
2. Jesper Tidblom, *A Hardy inequality in the half-space*, Journal of Functional Analysis 221 (2005), 482--495, DOI:10.1016/j.jfa.2004.09.014.
3. Rupert L. Frank and Robert Seiringer, *Sharp fractional Hardy inequalities in half-spaces*, arXiv:0906.1561, 2009.
4. Vladimir Maz’ya and Tatyana Shaposhnikova, *A collection of sharp dilation invariant inequalities for differentiable functions*, arXiv:0802.3209, 2008.
