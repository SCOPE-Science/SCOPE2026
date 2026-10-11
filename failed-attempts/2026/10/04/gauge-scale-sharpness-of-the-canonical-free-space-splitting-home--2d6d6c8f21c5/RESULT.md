# Gauge-scale sharpness of the canonical free-space splitting homeomorphism
## Finding
Let \(X\) be a nonzero real Banach space and let \(0<\alpha\le 2\). Define the strongly normalized gauge
\[
\omega(t)=\begin{cases}
0,&t=0,\\
t(|\log t|^{\alpha}+1),&0<t<e^{-1},\\
\dfrac{e-2}{e-1}t+\dfrac{1}{e-1},&e^{-1}\le t<1,\\
t,&t\ge1.
\end{cases}
\]
Let \(\mathcal F_\omega(X)\) be the Lipschitz-free space over \(X\) with metric \(d_\omega(x,y)=\omega(\|x-y\|)\), let \(\delta_\omega:X\to\mathcal F_\omega(X)\) be the canonical map, and let \(\beta_\omega:\mathcal F_\omega(X)\to X\) be the barycentric quotient. For the canonical homeomorphism
\[
\varphi:\ker\beta_\omega\oplus_1 X\longrightarrow\mathcal F_\omega(X),
\qquad \varphi(\gamma,x)=\gamma+\delta_\omega(x),
\]
write \(\omega_f(t)=\sup\{\|f(a)-f(b)\|:\|a-b\|\le t\}\). Then, for every \(t>0\),
\[
\omega(t)\le \omega_\varphi(t)\le2\omega(t),
\qquad
\omega(t)\le \omega_{\varphi^{-1}}(t)\le3\omega(t).
\]
Therefore the logarithmic exponent \(\alpha\) used in the recent almost-Lipschitz construction is sharp for this canonical map in both directions: for every \(0<\gamma<\alpha\), neither \(\varphi\) nor \(\varphi^{-1}\) is \(\gamma\)-almost Lipschitz.

## Assumptions and scope
The claim uses the specific gauge above and a nonzero real Banach space \(X\). The direct sum is the \(\ell_1\)-sum, so \(\|(\gamma,x)\|=\|\gamma\|+\|x\|\). The canonical free-space embedding is based at \(0\), hence \(\delta_\omega(0)=0\), and it satisfies
\[
\|\delta_\omega(x)-\delta_\omega(y)\|=\omega(\|x-y\|).
\]
The barycentric map satisfies \(\beta_\omega\delta_\omega=\operatorname{Id}_X\). The statement proves sharpness only for the displayed canonical homeomorphism; it does not claim that no different homeomorphism between these spaces has smaller logarithmic losses.

## Proof
The upper estimates are the estimates of Kalton's Proposition 5.1, restated in the recent construction:
\[
\omega_\varphi(t)\le2\omega(t),
\qquad
\omega_{\varphi^{-1}}(t)\le3\omega(t).
\]
It remains to prove matching lower bounds at the scale \(\omega\).

Choose \(u\in X\) with \(\|u\|=1\). For the forward map, compare \((0,tu)\) with \((0,0)\). Their distance in \(\ker\beta_\omega\oplus_1X\) is \(t\), while
\[
\|\varphi(0,tu)-\varphi(0,0)\|
=\|\delta_\omega(tu)-\delta_\omega(0)\|
=\omega(t).
\]
Thus \(\omega_\varphi(t)\ge\omega(t)\).

For the inverse map, put \(\eta_t=t\delta_\omega(u)\). Since \(\omega(1)=1\),
\[
\|\eta_t\|=t\|\delta_\omega(u)\|=t.
\]
Linearity of \(\beta_\omega\) and \(\beta_\omega\delta_\omega(u)=u\) give \(\beta_\omega(\eta_t)=tu\). Hence
\[
\varphi^{-1}(\eta_t)=
\bigl(t\delta_\omega(u)-\delta_\omega(tu),tu\bigr).
\]
Using the \(\ell_1\)-sum norm and the reverse triangle inequality,
\[
\begin{aligned}
\|\varphi^{-1}(\eta_t)-\varphi^{-1}(0)\|
&=\|t\delta_\omega(u)-\delta_\omega(tu)\|+t\\
&\ge \|\delta_\omega(tu)\|-t\|\delta_\omega(u)\|+t\\
&=\omega(t)-t+t=\omega(t),
\end{aligned}
\]
Since the input distance is \(t\), this yields \(\omega_{\varphi^{-1}}(t)\ge\omega(t)\).

Finally, for \(0<t<e^{-1}\),
\[
\frac{\omega(t)}{t|\log t|^{\gamma}}
=|\log t|^{\alpha-\gamma}+|\log t|^{-\gamma}.
\]
If \(0<\gamma<\alpha\), this tends to \(+\infty\) as \(t\downarrow0\). The two lower bounds therefore rule out a \(\gamma\)-almost-Lipschitz estimate in either direction, while the published upper bounds show that exponent \(\alpha\) is admissible. Thus the least admissible exponent for each direction is exactly \(\alpha\).

## Verification
The proof uses only the exact free-space distance formula, the barycentric identity, linearity, the \(\ell_1\)-sum norm, and the two published upper estimates. The two lower-bound witnesses are explicit and work for every \(t>0\). No finite experiment or asymptotic numerical evidence is used.

The endpoint \(\alpha=2\) is included because the recent paper verifies that the displayed piecewise function is a strongly normalized gauge throughout \(0<\alpha\le2\). The argument requires \(X\ne\{0\}\) only to choose a unit vector.

## Relationship to prior work
Kalton proved that for any strongly normalized gauge the canonical splitting homeomorphism obeys the upper bounds \(2\omega\) and \(3\omega\) for the map and its inverse, respectively. The recent paper of Cheng, He and Xiang specializes this construction to the displayed logarithmic gauge and concludes that the spaces are \((\alpha,\alpha)\)-almost Lipschitz homeomorphic. The inspected statements give upper control; they do not state the matching lower bounds above or the resulting optimality of \(\alpha\) for the canonical map.

The lower bound for the inverse is not a formal consequence of the forward lower bound: it uses the scaled free vector \(t\delta_\omega(u)\), whose barycenter is \(tu\), and the resulting cancellation defect \(t\delta_\omega(u)-\delta_\omega(tu)\). This identifies the same gauge scale in both directions.

## Limitations
The result does not optimize the numerical constants \(2\) and \(3\). It proves only that the gauge order is unavoidable for the canonical Kalton homeomorphism. A different homeomorphism between \(\mathcal F_\omega(X)\) and \(\ker\beta_\omega\oplus_1X\) could conceivably have smaller logarithmic losses. The novelty search may miss equivalent observations stated without the recent almost-Lipschitz terminology.

## References
1. Qingjin Cheng, Wuyi He, Bo Xiang, *Sphere version of Banach--Kadec--Paley theorem*, arXiv:2609.14641v1, first submitted 2026-09-13. Section 5.4, Proposition 5.2 and Example 5.1 give the gauge and the canonical almost-Lipschitz homeomorphism.
2. N. J. Kalton, *Spaces of Lipschitz and Hölder functions and their applications*, Collectanea Mathematica 55 (2004), 171--217. Proposition 5.1 gives the canonical homeomorphism and the upper bounds \(2\omega\) and \(3\omega\).
