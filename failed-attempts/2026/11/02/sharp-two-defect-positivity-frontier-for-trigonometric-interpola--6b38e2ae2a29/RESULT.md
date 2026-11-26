# Sharp two-defect positivity frontier for trigonometric interpolatory quadrature

## Finding

On an equispaced periodic grid of any odd length \(K\ge5\), moving a single node by less than half a mesh cannot make an exact trigonometric interpolatory quadrature weight negative. By contrast, moving exactly two nodes inward toward their common, unperturbed neighbor gives a single negative weight at a sharp displacement threshold, explicit for every odd \(K\ge5\):

\[
\boxed{\delta_K=1-\frac{K}{\pi}\arcsin\!\sqrt{1-\cos(\pi/K)}}.
\]

These thresholds are strictly increasing with \(K\), satisfy \(\frac14<\delta_K<1-1/\sqrt2\), and converge to \(1-1/\sqrt2\). The resulting two-defect quadrature has **exactly one negative weight** above this threshold, while all remaining weights stay strictly positive. Its absolute-weight condition number is explicit and tends to the ideal value \(2\pi\) as \(K\to\infty\) for each fixed displacement in the admissible range.

## Assumptions and scope

Let \(K=2m+1\ge5\), \(h=2\pi/K\), \(x_j=jh\pmod{2\pi}\) for \(j=0,\ldots,K-1\), and
\[
\mathcal T_m=\operatorname{span}\{e^{ikx}:-m\le k\le m\}.
\]
For distinct periodic nodes \(y_j\), let \(w_j\in\mathbb R\) denote the unique weights satisfying
\[
\sum_{j=0}^{K-1}w_jp(y_j)=\int_0^{2\pi}p(x)\,dx\quad(p\in\mathcal T_m).
\]
The two configurations considered are (i) one moved node, \(y_0=\delta h\), \(y_j=x_j\) for \(j\ne0\), with an arbitrary signed \(\delta\) satisfying \(|\delta|<1/2\); and (ii) two inward-moving nodes, \(y_0=\delta h\), \(y_2=(2-\delta)h\), \(y_j=x_j\) otherwise, with \(0\le\delta<1/2\). All angular locations are interpreted modulo \(2\pi\). The assertion about the *sharp displacement* concerns configuration (ii), not arbitrary two-node movements.

Write \(t=\pi/K\), \(v=(1-\delta)t\), and \(c=\cos t\). In configuration (ii), the central unchanged node \(j=1\) has weight
\[
\boxed{\frac{w_1}{h}=\frac{1+c-\sin^2t/\sin^2v}{c}}.
\]
For \(\delta=0\) every weight equals \(h\). For \(0<\delta<1/2\), the two shifted-node weights are equal and positive, and every unchanged-node weight other than \(w_1\) is strictly positive. Hence \(w_1>0\), \(w_1=0\), or \(w_1<0\) as \(\delta<\delta_K\), \(\delta=\delta_K\), or \(\delta>\delta_K\), respectively.

For all such \(K,\delta\),
\[
\sum_{j=0}^{K-1}|w_j|=2\pi+2\max\{0,-w_1\}.
\]
For a fixed \(\delta\in(1-1/\sqrt2,1/2)\), the negative center weight obeys
\[
\frac{w_1}{h}=2-(1-\delta)^{-2}+O(K^{-2}),\qquad
\frac{1}{2\pi}\sum_j|w_j|=1+\frac{2}{K}\big((1-\delta)^{-2}-2\big)+O(K^{-3}).
\]
The second expansion is stated only when the center is negative, which holds eventually for such fixed \(\delta\).

## Proof

**1. Exactness and cardinal functions.** As all nodes under the stated displacement bounds are distinct, the odd-order trigonometric Vandermonde determinant is nonzero: the map \(p(x)=\sum_{k=-m}^{m}c_ke^{ikx}\) to \(K\) distinct values is a Vandermonde map in \(e^{ix}\) after multiplying by \(e^{imx}\). Hence the weights exist uniquely and are real by conjugation. The cardinal functions for the **unperturbed** grid are
\[
\ell_j(x)=\frac{D_m(x-jh)}{K},\qquad
D_m(z)=\frac{\sin(Kz/2)}{\sin(z/2)},
\]
with the continuous value at removable singularities. Their integrals all equal \(h\). Using quadrature exactness on \(\ell_j\) relates all perturbed weights to only the changed nodes. Every rule integrates the constant, so \(\sum_jw_j=2\pi\).

**2. One-site positivity.** By rotation and reflection it suffices to treat a shift \(0<\delta<1/2\) at node zero. The cardinal equation at index zero gives
\[
 w_0=\frac{h}{\ell_0(\delta h)}=\frac{2\pi\sin(\delta t)}{\sin(\pi\delta)}>0.
\]
For every \(j=1,\ldots,K-1\), the other cardinal equations yield
\[
 \frac{w_j}{h}=1-(-1)^{j+1}
 \frac{\sin(\delta t)}{\sin((j-\delta)t)}.
\]
Even \(j\) give values greater than one. For odd \(j\), \(\delta t<(j-\delta)t<\pi-\delta t\); this follows from \(j\ge1>2\delta\) and \(j\le K-1\). Consequently \(\sin((j-\delta)t)>\sin(\delta t)\), proving all weights are positive. Negative shifts follow by reflection; the zero shift is the original trapezoidal rule. Thus one changed node never destroys nonnegativity within the half-mesh regime.

**3. Two-site weights and signs.** Assume \(0<\delta<1/2\), set \(u=\delta t\), \(v=(1-\delta)t\), \(s=\sin(\pi\delta)>0\), and define \(S_j=\ell_j(\delta h)+\ell_j((2-\delta)h)\). Reflection across \(x_1=h\) interchanges the two moved nodes, so their weights coincide. The cardinal equations at indices zero and two show
\[
 w_0=w_2=\frac{h}{S_0},\qquad
 S_0=\frac{s}{K}\left(\frac1{\sin u}-\frac1{\sin((2-\delta)t)}\right)
 =\frac{2s\sin v\cos t}{K(\sin^2t-\sin^2v)}>0.
\]
For every index \(j\notin\{0,2\}\),
\[
 \frac{w_j}{h}=1-\frac{S_j}{S_0}.
\]
Write the representative \(j=1+k\pmod K\), where \(-m\le k\le m\). Direct substitution into the Dirichlet kernel and the sine-difference identity give
\[
 S_{1+k}=\frac{2(-1)^k s\sin v\cos(kt)}{K(\sin^2v-\sin^2(kt))}.
\]
For \(k=0\), \(S_1=2s/(K\sin v)\). The moved nodes correspond to \(k=\pm1\). If \(k\ne0\) is even, then \(S_{1+k}<0\). If \(k\) is odd and \(|k|\ge3\), then \(S_{1+k}>0\), but
\[
 \frac{S_{1+k}}{S_0}=
 \frac{\cos(|k|t)}{\cos t}
 \frac{\sin^2t-\sin^2v}{\sin^2(|k|t)-\sin^2v}<1.
\]
These inequalities use \(0<v<t\), \(0<|k|t<\pi/2\), and monotonicity of sine and cosine there. Therefore every unchanged node except \(j=1\) has strictly positive weight. Finally
\[
 \frac{S_1}{S_0}=\frac{\sin^2t-\sin^2v}{\cos t\,\sin^2v}
\]
proves the displayed formula for \(w_1\).

**4. Sharp crossing and its limiting law.** For fixed \(K\), the central weight is strictly decreasing in \(\delta\), because \(v=(1-\delta)t\) decreases and \(\csc^2v\) increases. Its initial value is \(h\), while at \(\delta=1/2\) its continuous-limit normalized value is \(-1-\sec t\). It therefore crosses zero exactly once. Its zero condition is
\[
 \sin^2((1-\delta)t)=\frac{\sin^2t}{1+\cos t}=1-\cos t,
\]
which gives \(\delta_K\). Define \(g(t)=\arcsin(\sqrt2\sin(t/2))\) on \(0<t\le\pi/3\). Then \(\delta_K=1-g(t)/t\) and
\[
 g''(t)=\frac{\sin(t/2)}{2\sqrt2(\cos t)^{3/2}}>0.
\]
Thus \(g(t)/t\) is strictly increasing in \(t\). Since \(t=\pi/K\) decreases with odd \(K\), \(\delta_K\) strictly increases. The boundary \(K=3\) gives \(\delta_3=1/4\) (included here solely as an algebraic comparison, not the new-order claim), and \(g'(0)=1/\sqrt2\) gives \(\delta_K\nearrow1-1/\sqrt2\).

**5. Condition number.** The sum of the weights is \(2\pi\) and only \(w_1\) can be negative; hence the absolute-weight identity follows exactly. Taylor expansion at \(t=\pi/K=0\), with fixed \(\delta>1-1/\sqrt2\), yields \(w_1/h=2-(1-\delta)^{-2}+O(t^2)\). The displayed condition-number expansion follows on multiplying the negative part by \(2h/(2\pi)=2/K\). In particular, two node perturbations can destroy positivity without causing a nonvanishing asymptotic relative \(\ell^1\) amplification.

## Verification

Run `python3 verify.py` with Python 3 and no external dependencies. The script evaluates independent complex Fourier moment systems, compares the computed weights with the one-defect and two-defect closed forms, checks positivity patterns, exact-mass identities numerically, crossing values, monotonic frontier behavior for multiple odd grid sizes, and absolute-weight identities. It reports `PASS: 5100 grouped reproducible assertions` in the tested environment. These finite floating-point checks support the formulas but do not replace the all-\(K\) analytic argument above; no interval-arithmetic or machine-checked infinite proof is claimed.

## Relationship to prior work

Austin's 2016 thesis, section 3.5.2, investigates absolute quadrature weights, includes general perturbed-grid experiments and partially unmoved grids, and conjectures global boundedness. Austin and Trefethen (2017, first posted December 2016) prove convergence for perturbed trigonometric interpolation and quadrature. Yu and Townsend (2022), section 4.1 and Appendices A–B, establish that an alternating perturbation of linearly many nodes can produce a negative exact quadrature weight for arbitrarily small nonzero displacement as grid size increases; they also prove a universal small-perturbation grid-size obstruction. Those results do not specify whether one or two changed nodes suffice, classify all weights of a two-changed-node pattern, or derive the finite-\(K\) threshold and limit above.

The present theorem is specific to the rank-two local defect: it does **not** assert that \(\delta_K\) is optimal over all ways to move two nodes, nor does it contradict the arbitrarily-small-displacement negative-weight phenomenon that uses many changed nodes.

## Limitations

No general worst-case theorem over arbitrary two-site displacement patterns is proved. The analysis concerns exact real trigonometric interpolation with an odd number of nodes, not polynomial Newton–Cotes weights, even grids, oversampled least-squares rules, or floating-point errors. Numerical checks are finite and are not a proof of asymptotic statements. Although relevant primary papers, the thesis's quadrature section, and matched research records were compared, independent literature-priority validation remains outstanding.

## References

1. Anthony P. Austin, *Some New Results on and Applications of Interpolation in Numerical Computation*, University of Oxford D.Phil. thesis (2016), section 3.5.2, deposited December 8, 2016. https://www.mcs.anl.gov/~aaustin/pubs/DPhilThesis.pdf ; Oxford archive https://ora.ox.ac.uk/objects/uuid:11c16937-4a59-494d-a06f-6d27b634e2f3 .
2. Anthony P. Austin and Lloyd N. Trefethen, *Trigonometric Interpolation and Quadrature in Perturbed Points*, arXiv:1612.04018 (first posted December 13, 2016); *SIAM Journal on Numerical Analysis* 55 (2017), 2113–2122. https://arxiv.org/abs/1612.04018 ; https://people.maths.ox.ac.uk/trefethen/perturbed.pdf .
3. Annan Yu and Alex Townsend, *On the Stability of Unevenly Spaced Samples for Interpolation and Quadrature*, arXiv:2202.04722 (first posted February 9, 2022), section 4 and Appendices A–B. https://arxiv.org/abs/2202.04722 ; https://arxiv.org/html/2202.04722v1 .
