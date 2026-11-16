# Sharp all-degree interpolation stability on five icosahedral axes

## Finding

Fix the following five points on the unit sphere:
\[
v_j=\frac1{\sqrt5}\bigl(2\cos(2\pi j/5),\,2\sin(2\pi j/5),\,1\bigr),\qquad j=0,\ldots,4.
\]
They are the five unoriented axes remaining after deleting one antipodal axis from a regular icosahedron; choosing the displayed representatives produces a pentagonal ring. Each pair has inner product \(\pm1/\sqrt5\).

Let \(\mathcal H_\ell\) be the complex spherical harmonics of exactly degree \(\ell\) on \(S^2\), with norm from probability surface measure. Define the row-normalized evaluation operator \(E_\ell:\mathcal H_\ell\to\mathbb C^5\) by
\[
(E_\ell f)_j=\frac{f(v_j)}{\sqrt{2\ell+1}}.
\]
Let \(P_\ell\) be the Legendre polynomial normalized by \(P_\ell(1)=1\), and put
\[
q_\ell=5^{(\ell\bmod2)/2}P_\ell(1/\sqrt5).
\]
Then the nonzero sampling singular values squared are the nonzero members of the following full five-dimensional Gram spectra, including zero eigenvalues and multiplicity:
\[
\operatorname{Spec}(E_\ell E_\ell^*)=
\begin{cases}
\{1+4q_\ell,\,(1-q_\ell)^{[4]}\}, &\ell\text{ even},\\
\{1,\,(1+q_\ell)^{[2]},\,(1-q_\ell)^{[2]}\}, &\ell\text{ odd}.
\end{cases}
\]
Here a bracketed exponent is multiplicity, not a power. The evaluation rank is \(1\) at \(\ell=0\), \(3\) at \(\ell=1,3\), and \(5\) at every other degree.

**Sharp degree-uniform conclusion.** For every integer \(\ell\ge2\) except \(\ell=3\),
\[
\lambda_{\min}(E_\ell E_\ell^*)\ge\frac15,
\qquad\frac{\lambda_{\max}(E_\ell E_\ell^*)}{\lambda_{\min}(E_\ell E_\ell^*)}\le6.
\]
Equality in either inequality holds **if and only if** \(\ell\in\{2,4,8,14\}\). At those four degrees the spectrum is exactly \(\{1/5,(6/5)^{[4]}\}\). In the injective-on-data degrees the sharp singular-value condition-number bound is \(\sqrt6\).

## Assumptions and scope

All degrees are nonnegative integers and the sampling grid is precisely the five displayed points. The normalization uses the standard spherical addition theorem with the probability surface measure, so \(E_\ell E_\ell^*=(P_\ell(v_i\cdot v_j))_{i,j}\). Full row rank means every **five-point data vector** can be interpolated by a pure degree-\(\ell\) harmonic; for \(\ell\ge3\), this does *not* mean that five samples determine an arbitrary harmonic in \(\mathcal H_\ell\), whose dimension is \(2\ell+1\).

## Proof

**1. Exact Gram diagonalization.** For distinct indices, elementary trigonometry gives
\[
v_i\cdot v_j=\frac{1+4\cos(2\pi(i-j)/5)}5
=\begin{cases}1/\sqrt5,&i-j\equiv\pm1\pmod5,\\-1/\sqrt5,&i-j\equiv\pm2\pmod5.\end{cases}
\]
The addition theorem gives \(E_\ell E_\ell^*=G_\ell=(P_\ell(v_i\cdot v_j))\). For even degree, Legendre parity makes all off-diagonal entries equal to \(q_\ell\), so \(G_\ell=(1-q_\ell)I+q_\ell J\), with eigenvalues \(1+4q_\ell\) on the constant vector and \(1-q_\ell\) four times. For odd degree, the off-diagonal entries on the five-cycle are \(q_\ell/\sqrt5\) and on its complementary five-cycle are \(-q_\ell/\sqrt5\). The signed circulant difference has eigenvalues \(0,\sqrt5,\sqrt5,-\sqrt5,-\sqrt5\). This yields the asserted odd-degree spectrum.

**2. Exceptional ranks and finite arithmetic.** The standard Legendre three-term relation yields exact rational numbers \(q_0=q_1=1\) and, for every integer \(n\ge1\),
\[
(n+1)q_{n+1}=(2n+1)c_nq_n-nq_{n-1},\qquad
c_n=\begin{cases}1/5,&n\text{ odd},\\1,&n\text{ even}.\end{cases}
\]
Thus \(q_3=-1\), yielding ranks \(1,3,3\) for degrees \(0,1,3\), respectively. Exact rational evaluation of the recurrence for all degrees \(2\le\ell\le18\) gives:

| \(\ell\) | \(q_\ell\) | \(\ell\) | \(q_\ell\) |
|---:|---:|---:|---:|
|2|\(-1/5\)|4|\(-1/5\)|
|5|\(11/25\)|6|\(41/125\)|
|7|\(29/125\)|8|\(-1/5\)|
|9|\(-73/125\)|10|\(-131/3125\)|
|11|\(1409/3125\)|12|\(3301/15625\)|
|13|\(-31/3125\)|14|\(-1/5\)|
|15|\(-5897/15625\)|16|\(3223/78125\)|
|17|\(34007/78125\)|18|\(10181/78125\)|

In this finite range every even \(\ell\ge2\) has \(-1/5\le q_\ell\le1/2\), with \(q_\ell=-1/5\) exactly at \(2,4,8,14\), while every odd \(\ell\ge5\) has \(|q_\ell|<5/7\). Substitution into the two spectra gives \(\lambda_{\min}\ge1/5\) and \(\lambda_{\max}\le6\lambda_{\min}\), with exactly the displayed equality cases. The standalone exact-arithmetic verifier tests every finite degree in this exhaustive range.

**3. Uniform tail.** The classical Bernstein inequality for Legendre polynomials (quoted in Wang, Lemma 2.1) gives, for all \(\ell\ge0\),
\[
(1-x^2)^{1/4}|P_\ell(x)|<\sqrt{\frac2\pi}\,\bigl(\ell+\tfrac12\bigr)^{-1/2},\quad -1<x<1.
\]
At \(x=1/\sqrt5\), for every \(\ell\ge19\),
\[
|P_\ell(1/\sqrt5)|^2<\frac{\sqrt5}{\pi(\ell+1/2)}
\le\frac{9/4}{3(39/2)}=\frac1{26}<\frac1{25},
\]
where the weak middle inequality uses \(\sqrt5<9/4\) and \(\pi>3\). Thus even degrees have \(|q_\ell|<1/5\), making both desired inequalities strict. Odd degrees have \(|q_\ell|<\sqrt5/5<5/7\), again making both strict. This proves the all-degree rank statement, sharp lower frame bound on five-point data, optimal uniform conditioning, and complete equality classification.

## Verification

Run `python verify.py` with Python, NumPy, and SciPy. The test recomputes all \(q_\ell\) for \(0\le\ell\le18\) with exact rational arithmetic, checks multiplicities, ranks, sharp inequalities and equality degrees, and independently builds normalized spherical-harmonic evaluation matrices for degrees zero through twelve. It verifies their Gram entries against Legendre kernels and their numerical spectra against the exact formulas. The strict tail cutoff is analytic rather than inferred from numerical testing.

## Relationship to prior work

Zandieh, Han and Avron (2022) provide the spherical-harmonic sampling framework and addition-theorem normalization, emphasizing randomized stable recovery on general spheres; no evaluated five-axis all-degree condition-number theorem was identified there. Hitchin (2007), Proposition 1, already proves the four-dimensional space of cubic harmonics vanishing on the complete icosahedron; therefore the **cubic rank obstruction is prior knowledge** and is not claimed as the novel contribution. Hitchin also records the \(1/\sqrt5\) axis inner-product geometry. Wang (2018) states the pre-existing sharp Bernstein inequality used for the infinite-degree tail. The asserted new contribution is the all-degree five-axis Gram spectrum together with the sharp uniform interpolation bound and its four equality degrees.

## Limitations

The five evaluations interpolate arbitrary data only in the full-row-rank degrees. They do not reconstruct a whole degree-\(\ell\) harmonic when \(\dim\mathcal H_\ell>5\). The priority search cannot exclude unindexed equivalent specialist calculations; an independent mathematical audit has not been performed.

## References

1. A. Zandieh, I. Han and H. Avron, *Near Optimal Reconstruction of Spherical Harmonic Expansions*, arXiv:2202.12995, first public 2022-02-25, https://arxiv.org/abs/2202.12995.
2. N. Hitchin, *Spherical harmonics and the icosahedron*, arXiv:0706.0088, https://arxiv.org/html/0706.0088v1.
3. H. Wang, *A new and sharper bound for Legendre expansion of differentiable functions*, arXiv:1803.00336, Lemma 2.1, https://arxiv.org/abs/1803.00336.
