# Unitarily rigid Aluthge orbits with opposite strong limits for affine monomial operators

## Finding

Let \(H=L^2((0,1),dx)\). For real \(a>0\) and \(b\in\mathbb R\), initially on compactly supported smooth functions, put
\[
 (T_{a,b}f)(x)=x^b f(x^a),\qquad
 \delta=b+\frac{1-a}{2},\qquad r=a^{-1/2}.
\]
The operator has a bounded extension exactly when \(\delta\geq0\), with norm \(r\). Write \(\Delta_\eta(T)=|T|^\eta U|T|^{1-\eta}\) for the generalized Aluthge transform of \(T=U|T|\), where \(0<\eta\leq1\). For every \(\delta>0\), let
\[
 q=1-\eta+\frac{\eta}{a}.
\]
Then the following assertions hold.

1. Under one fixed unitary logarithmic-coordinate identification, all iterates have the **exact** expression
   \[
   \Delta_\eta^{\circ n}(T_{a,b})\ \simeq\ A_{a,\delta q^n},\quad
   (A_{a,d}h)(y)=e^{-dy}h(ay),\qquad n=0,1,2,\ldots.
   \]
   All \(A_{a,d}\) with fixed \(a\) and positive \(d\) are mutually unitarily equivalent. Consequently every member of a positive-damping orbit has the same norm, spectrum, essential spectrum, point-spectrum multiplicities, and self-commutator norm.

2. If \(a>1\), the iterates converge in the **strong-star topology** to \(rV_a\), where \((V_ah)(y)=\sqrt a\,h(ay)\) is unitary. If \(0<a<1\), the iterates converge strongly-star to zero. For either \(a\ne1\), this convergence is **never** in operator norm, and the distance from every iterate to its strong-star limit is exactly \(r\). More strongly, the distance between **every pair of successive iterates** is the same strictly positive number
   \[
   \left\|\Delta_\eta^{\circ(n+1)}(T_{a,b})-\Delta_\eta^{\circ n}(T_{a,b})\right\|
   =r\,|1-q|\,q^{-q/(q-1)}.
   \]
   This formula also holds for \(\eta=1\). If \(a=1\), the operator is a normal multiplication operator fixed by every Aluthge transform.

3. For \(a\ne1\) and \(\delta>0\), the full spectrum and Fredholm essential spectrum coincide with the **closed disk** \(\{\lambda\in\mathbb C:|\lambda|\le r\}\). Each \(0<|\lambda|<r\) is an eigenvalue of infinite multiplicity when \(0<a<1\), but is a residual spectral value with an infinite-dimensional adjoint eigenspace when \(a>1\). The spectral values \(0\) and \(|\lambda|=r\) lie in the continuous spectrum. When \(\delta=0\) and \(a\ne1\), the operator is \(rV_a\), with both spectrum and Fredholm essential spectrum equal to the circle \(\{\lambda:|\lambda|=r\}\); it has no eigenvalues.

4. For \(a\ne1\) and \(\delta>0\), the self-commutator is a nonzero multiplication operator with the sign of \(a-1\) and the exact, damping-independent norm
   \[
   \|A_{a,\delta}^*A_{a,\delta}-A_{a,\delta}A_{a,\delta}^*\|
   =\frac{|a-1|}{a}\,a^{-a/(a-1)}.
   \]
   Hence the \(a>1\) branch is strictly hyponormal, the \(0<a<1\) branch strictly cohyponormal, and neither branch approaches normality in self-commutator norm despite its normal strong-star limit.

The boundary cases are explicit: at \(a=1\), \(\delta=b>0\), the operator is multiplication by \(x^b\) with continuous spectrum \([0,1]\); at \(a=1\), \(\delta=0\), it is the identity.

## Assumptions and scope

All Hilbert spaces are complex. A strong-star limit means strong convergence of both the operators and their adjoints, with no uniformity over unit vectors. The operator initially acts on \(C_c^\infty(0,1)\); the theorem concerns its unique bounded extension when one exists. For the main nontrivial orbit assume \(\delta>0\), \(a\ne1\), and a **fixed** parameter \(\eta\in(0,1]\). The Fredholm essential spectrum is defined by the non-Fredholm locus of \(T-\lambda I\). “Residual spectrum” means injectivity with nondense range. “Continuous spectrum” means injectivity and dense but nonclosed range. Unitary equivalence between orbit members is in the given infinite-dimensional Hilbert space, not identity of the operators.

## Proof

### 1. Logarithmic coordinates and polar decomposition

Define \(J:H\to L^2(0,\infty)\) by \((Jf)(y)=e^{-y/2}f(e^{-y})\). Change of variables \(x=e^{-y}\) shows this is unitary, with
\[
 JT_{a,b}J^{-1}=A_{a,\delta},\qquad
 (A_{a,\delta}h)(y)=e^{-\delta y}h(ay).
\]
The norm identity
\[
 \|A_{a,\delta}h\|^2
 =\frac1a\int_0^\infty e^{-2\delta t/a}|h(t)|^2\,dt
\]
proves boundedness and norm \(r\) for \(\delta\ge0\), and proves absence of a bounded extension for \(\delta<0\) by testing unit vectors on increasingly remote compact intervals. For \(\delta\ge0\),
\[
 |A_{a,\delta}|=rM_{e^{-\delta y/a}},\qquad
 A_{a,\delta}=V_a|A_{a,\delta}|,
 \qquad (V_ah)(y)=\sqrt a\,h(ay).
\]
Both \(A_{a,\delta}\) and its adjoint are injective, so \(V_a\) is exactly the polar unitary. Therefore
\[
 |A_{a,\delta}|^\eta V_a|A_{a,\delta}|^{1-\eta}
 =A_{a,\delta(1-\eta+\eta/a)}=A_{a,\delta q}.
\]
Iteration proves the formula for every integer \(n\ge0\), without assuming a differentiable or invertible modulus. Let \((W_ch)(y)=\sqrt c\,h(cy)\). This is unitary and satisfies
\[
 W_c^{-1}A_{a,d}W_c=A_{a,d/c},\qquad c,d>0.
\]
Thus any two strictly positive damping parameters produce unitary equivalents. Their equal essential spectra and spectral-type multiplicities follow immediately, while the common essential spectrum is determined below.

### 2. Two opposite strong-star limits and exact fixed norm gaps

For \(a>1\), \(0<q<1\), hence \(\delta q^n\downarrow0\). The factors \(e^{-\delta q^ny}\to1\) and their adjoint counterparts \(e^{-\delta q^ny/a}\to1\) pointwise for \(y>0\), bounded by one. Dominated convergence for multiplication operators gives
\[
 A_{a,\delta q^n}\xrightarrow{\mathrm{SOT}^*}A_{a,0}=rV_a.
\]
For \(0<a<1\), \(q>1\), so \(\delta q^n\uparrow\infty\). Both multipliers converge pointwise to zero, giving strong-star convergence to the zero operator. In both regimes the distance from an iterate to its limit is exactly \(r\), since multiplication by \(e^{-dy}-1\) has essential supremum one for \(d>0\), and multiplication by \(e^{-dy}\) has essential supremum one.

For the successive gap, unitary multiplication on the right yields
\[
 \|A_{a,dq}-A_{a,d}\|=r\sup_{z\ge0}|e^{-qz}-e^{-z}|,
\]
where the substitution \(z=dy\) removes \(d\). For \(q>0\), \(q\ne1\), the unique positive maximizing point is \(z=\log q/(q-1)\). Its value is \(|1-q|q^{-q/(q-1)}\). The fixed positive gap is compatible with strong-star convergence because its maximizing vectors escape toward \(y=\infty\) when \(q<1\), and toward \(y=0\) when \(q>1\).

### 3. Exact disk and spectral-type orientation

For \(a\ne1\), apply the unitary \((Ph)(s)=e^{s/2}h(e^s)\) from \(L^2(0,\infty)\) to \(L^2(\mathbb R)\). Writing \(h_0=\log a\),
\[
 (PA_{a,\delta}P^{-1}F)(s)
 =r e^{-\delta e^s}F(s+h_0).
\]
Disintegrate \(\mathbb R\) into translates of any interval of length \(|h_0|\). On each fiber \(\ell^2(\mathbb Z)\), the operator, divided by \(r\), is
\[
 (B_\xi z)_k=w_k(\xi)z_{k+1},
 \quad w_k(\xi)=\exp(-\delta\exp(\xi+kh_0))\in(0,1),
 \quad 0\le\xi<|h_0|.
\]
For \(a<1\), \(w_k\to0\) as \(k\to-\infty\) and \(w_k\to1\) as \(k\to+\infty\); for \(a>1\), these endpoints reverse. Fix \(\mu\) with \(0<|\mu|<1\). In the first orientation the recurrence
\[
 z_{k+1}=\frac{\mu}{w_k}z_k
\]
produces a nonzero \(\ell^2(\mathbb Z)\) eigenvector: toward \(+\infty\) its ratio is eventually less than one in modulus, while toward \(-\infty\) the backward ratio \(w_k/|\mu|\) tends to zero. For the second orientation no such eigenvector exists, since forward growth is unbounded where \(w_k\to0\). Instead the adjoint recurrence
\[
 z_k=\frac{w_{k-1}}{\bar\mu}z_{k-1}
\]
produces a nonzero \(\ell^2\) adjoint eigenvector, using decay at both ends. These recurrence solutions depend measurably on \(\xi\); choosing arbitrary independent square-integrable scalar functions of \(\xi\) gives infinite-dimensional eigenspaces (of \(B\) or \(B^*\), respectively). Thus all \(0<|\lambda|<r\) are of the stated point or residual type, and each lies in the Fredholm essential spectrum.

At \(\mu=0\), the shifts and their adjoints are injective, but the multiplier weights approach zero on one tail; therefore their ranges are dense and nonclosed. At \(|\mu|=1\), neither the shift nor its adjoint has a fiber eigenvector. Indeed, at the end with \(w_k\to1\), the defect is summable, \(\sum(1-w_k)<\infty\), since \(1-e^{-v}\le v\) and the relevant \(e^{\xi+kh_0}\) form a decaying geometric progression. Thus finite products of the tail weights tend to a strictly positive limit, and the forward/backward recurrence cannot produce a nonzero square-summable vector. Long, normalized truncated plane waves placed in that tail provide singular sequences, showing nonclosed range and failure of Fredholmness at every point of the boundary circle. The operator and its adjoint are injective there, so the circle is continuous spectrum. Conversely \(\|A_{a,\delta}\|=r\) excludes any spectrum outside the disk. When \(\delta=0\), the logarithmic model is the scalar unitary translation \(rF(s+h_0)\), which is unitarily equivalent by Fourier transform to multiplication by \(re^{ith_0}\); its spectrum and Fredholm essential spectrum equal the circle and it has no point spectrum.

### 4. Self-commutator and exceptional cases

Directly from the polar formula,
\[
 A_{a,\delta}^*A_{a,\delta}-A_{a,\delta}A_{a,\delta}^*
 =\frac1a M_{e^{-2\delta y/a}-e^{-2\delta y}}.
\]
Its sign is the sign of \(a-1\). For \(\delta>0\) let \(t=2\delta y\). The absolute difference \(|e^{-t/a}-e^{-t}|\) has a single positive maximum at \(t=a\log a/(a-1)\), yielding the stated constant. The commutator vanishes when \(\delta=0\) or \(a=1\). If \(a=1\), \(T_{1,b}f=x^bf\) is multiplication on \(L^2(0,1)\), bounded exactly when \(b\ge0\), with spectrum \([0,1]\) for \(b>0\) and \(\{1\}\) for \(b=0\); its transforms are fixed.

## Verification

A standalone, standard-library Python checker is provided at `checks/check.py`. Run it from the package root using `python checks/check.py`; it reports `CHECKS_OK 17378`. It checks the pointwise polar/iteration identity over several parameter families, dilation intertwining, the two calculus maximizers against grids, and small finite-shift eigen/adjoint-eigen residuals in both orientation regimes. These are **supplementary diagnostics**. Infinite-dimensional spectral multiplicity, absence of boundary eigenvalues, strong-star convergence and strict norm gaps are proved analytically above; no finite truncation is claimed to prove them.

## Relationship to prior work

Benhida, Budzyński and Trepkowski (2018) establish the generalized Aluthge transform of weighted composition operators on \(L^2\), an input that is explicitly **not claimed as new**. Agler and McCarthy (2022) introduce and analyze monomial operators on \(L^2(0,1)\); Chalendar and Partington (2022) investigate affine-index monomial boundedness and compactness. These works supply the setting and techniques, but their inspected statements do not give the above joint classification of fixed unitary Aluthge orbits, opposite strong-star limits, invariant residual/point spectral disk, and exact constant norm gaps. Classical weighted-translation and weighted-shift Aluthge iteration literature is also relevant; special-case implications remain a priority question. The claim concerns this precise explicit family, not a general convergence theorem for all weighted composition operators.

## Limitations

The result requires fixed \(\eta>0\) and a strictly positive damping parameter for the nontrivial orbit. It does not classify arbitrary affine-index monomial operators with nonconstant monomial coefficients, or arbitrary weight functions. A general theorem on Aluthge convergence of weighted translations may imply some convergence assertions in a transformed model; the distinctive exact unitary-orbit and quantitative norm-gap statement must be distinguished from such implications. Inaccessible or unindexed older literature may contain an equivalent formulation.

## References

1. C. Benhida, P. Budzyński, J. Trepkowski, *Aluthge transforms of unbounded weighted composition operators in \(L^2\)-spaces*, arXiv:1809.01205, first posted 4 September 2018. https://arxiv.org/abs/1809.01205
2. J. Agler, J. E. McCarthy, *Monomial Operators*, arXiv:2205.01857, first posted 4 May 2022. https://arxiv.org/abs/2205.01857
3. I. Chalendar, J. R. Partington, *Boundedness and compactness of weighted composition operators and monomial operators*, arXiv:2212.02172, first posted 5 December 2022. https://arxiv.org/abs/2212.02172
4. C. Burnap, I. Jung, M. Lee, J. Park, *Aluthge iterations of weighted translation semigroups*, Journal of Mathematical Analysis and Applications 354 (2009), relevant general convergence comparison.
5. S. Lahiri, S. Ojha, R. Birbonshi, *Iterated Aluthge transforms of some composition operators on weighted Bergman spaces*, arXiv:2604.27762 (2026), related but on a different function space. https://arxiv.org/abs/2604.27762
