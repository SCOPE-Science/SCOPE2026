# Exact five-mode Fourier observability on two equal circle arcs

## Finding
Let \(0<a<\pi/2\), and let \(E_{a,\beta}\subset\mathbb T=\mathbb R/(2\pi\mathbb Z)\) be the union of two arcs of half-width \(a\) centered at \(\pm\beta\), with disjoint interiors. For the five-character space \(V_2=\operatorname{span}\{e^{ik\theta}:-2\le k\le2\}\), define
\[
\Lambda(a,\beta)=\inf_{0\ne f\in V_2}\frac{\int_{E_{a,\beta}}|f(\theta)|^2\,d\theta}{\int_{\mathbb T}|f(\theta)|^2\,d\theta}.
\]
The unique maximizer over relative arc placements, modulo common rotation and interchange, is the antipodal placement \(\beta=\pi/2\). Its **exact** worst-case captured-energy fraction for every admissible half-width is
\[
\boxed{\max_\beta\Lambda(a,\beta)=\frac{2a}{\pi}-\frac{\sin(2a)}{\pi}\,\frac{\sqrt{\bigl(\cos(2a)\bigr)^2+8}-\cos(2a)}2.}
\]
In particular,
\[
\max_\beta\Lambda(a,\beta)=\frac{64}{135\pi}a^5+O(a^7)\qquad(a\downarrow0).
\]
The finite-width assertion is new relative to the inspected all-band small-arc asymptotic and exact three-mode results; no worldwide priority assertion is made.

## Assumptions and scope
All integrals are Lebesgue integrals, and normalization cancels in the energy ratio; calculations use normalized Haar measure \(d\theta/(2\pi)\). Without loss of generality by common rotation, interchange, and complementary angle reflection, take \(a\le\beta\le\pi/2\). Meeting endpoints at \(\beta=a\) are allowed: they have measure zero. Throughout \(0<a<\pi/2\), so the two arcs have total length \(4a<2\pi\); degeneracies at empty/full measure are excluded.

Let \(c=\cos a\in(0,1)\), \(s=2\sin a/\pi\), \(L=2a/\pi\), \(p=2c^2-1=\cos(2a)\), and
\[
 h=\frac{\sqrt{p^2+8}-p}{2},\qquad y=ch.
\]
Thus \(h\) is the unique positive root of \(h^2+ph-2=0\). The statement is \(\Lambda(a,\beta)\le L-sy\), with equality exactly at antipodal separation.

## Proof
**1. Exact antipodal value.** In the orthonormal character basis indexed by \(-2,-1,0,1,2\), the observation Gram matrix has entries \(G_{jk}=M_{|j-k|}\), where
\[
 M_0=L,\qquad M_k=\frac{2\sin(ka)}{\pi k}\cos(k\beta)\quad(1\le k\le4).
\]
At \(\beta=\pi/2\), odd differences vanish. The odd-character block of size two has eigenvalues \(L\pm sc\). The even-character block of size three has off-diagonals \(-sc\) and second off-diagonal \(scp\); its eigenvalues are
\[
 L-scp,\quad L+\frac{scp\pm sc\sqrt{p^2+8}}2.
\]
The least of all five is \(\lambda_*=L-sy\), since \(h>1\) and \(-1<p<1\). It is simple for \(0<a<\pi/2\).

**2. A two-dimensional strict comparison for every other placement.** Put \(t=\cos\beta\), so \(0<t\le c\) for nonantipodal placements. Choose the two-dimensional subspace of \(V_2\) spanned by \(1\) and \((\cos\theta-t)^2\). Their coefficient vectors, in the five-character basis, are
\[
 v_0=(0,0,1,0,0)^{\mathsf T},\qquad
 v_1=(\tfrac14,-t,\tfrac12+t^2,-t,\tfrac14)^{\mathsf T}.
\]
Write \(B=[v_0\ v_1]\). The Gram form of the energy **relative to the claimed sharp value** is \(H=B^*(G-\lambda_* I)B\). Elementary cosine-Chebyshev expansion, using \(h^2+ph=2\), gives the exact determinant identity
\[
 \det H=s^2t^2\bigl(A(c,y)+t^2D(c,y)\bigr),
\]
where
\[
\begin{aligned}
 A(c,y)&=(-6c^3+4c^2+c-2)y+5c^2-2c,\\
 D(c,y)&=(2c^3-\tfrac{16}{3}c^2+3c+\tfrac43)y-c^2+4c-4.
\end{aligned}
\]
We prove both coefficients strictly negative for \(0<c<1\).

The cubic \(A_1(c)=-6c^3+4c^2+c-2\) is negative on \((0,1)\): its degree-three Bernstein coefficients on \([0,1]\) are \((-2,-5/3,0,-3)\). Define \(\delta=1-c^2\) and \(h_-=1+2\delta/3\). Substitution into the strictly increasing positive-branch quadratic \(q(v)=v^2+pv-2\) gives \(q(h_-)=-8\delta^2/9<0\), hence \(h>h_-\) and \(y>ch_-\). Therefore
\[
 A(c,y)< A(c,ch_-)=\frac{4c(c-1)^3(c+1)(3c+4)}3<0.
\]

The cubic \(D_1(c)=2c^3-16c^2/3+3c+4/3\) is strictly positive on \([0,1]\), as its degree-three Bernstein coefficients are \((4/3,7/3,14/9,1)\). Put \(h_+=1+2\delta/3+\delta^2/3\). Then \(q(h_+)=c^4\delta^2/9>0\), whence \(h<h_+\) and \(y<ch_+\). Direct factorization gives
\[
 D(c,y)< D(c,ch_+)=\frac{(c-1)^2(c+1)}9 P(c),
\]
with \(P(c)=6c^5-10c^4-19c^3+33c^2+24c-36\). Its degree-five Bernstein coefficients on \([0,1]\) are \((-36,-156/5,-231/10,-68/5,-33/5,-2)\), all strictly negative, so \(P(c)<0\) and \(D(c,y)<0\).

Consequently \(\det H<0\) whenever \(t>0\), so \(H\) has a negative eigenvalue. Some nonzero member of the trial subspace therefore has observed energy strictly below \(\lambda_*\) times its total energy. This proves \(\Lambda(a,\beta)<\lambda_*\) for every nonantipodal placement. The formula and uniqueness follow.

**3. Small-arc boundary.** Taylor expansion of the exact radical expression, at the excluded endpoint \(a=0\), yields \(\lambda_*=64a^5/(135\pi)+O(a^7)\). This agrees with the previously published two-arc Legendre asymptotic at bandwidth two, but that asymptotic alone does not imply the finite-width theorem.

## Verification
The standalone `check.py` constructs exact symbolic Fourier moments, reduces the trial-space determinant modulo the quadratic for \(y\), verifies both bounding polynomials and their Bernstein coefficients, checks the \(a^5\) coefficient, and independently diagonalizes numerical Gram matrices for 31 widths and 101 placements each. Run `python check.py` with `sympy` and `numpy`. The checked output is `FIVE_MODE_TWO_ARC_CHECK_PASS 3140`. These computations are supplementary to the uniform algebraic proof above.

## Relationship to prior work
The 2026 componentwise time-frequency localization work of Azimifard studies transition-eigenvalue counts, not this finite five-mode smallest-eigenvalue design. The published sharp two-arc observability theorem in published-finding corpus gives an exact **small-arc leading coefficient** for every odd Fourier band and exact finite-width optimality only for three modes, explicitly leaving higher-band finite widths outside its claim. Another published published-finding corpus result treats exactly the three-mode version and supplies its strict two-by-two determinant certificate; the present argument is a distinct higher-dimensional trial-space calculation and an all-width algebraic sign proof. The broad concentration-operator bounds of Marceca, Romero and Speckbacher concern eigenvalue counts and bounds, not an exact five-mode minimax placement. Implication comparisons and residual risks are detailed in `AUDIT.json`.

## Limitations
Two arcs must have the **same** positive width, their interiors must not overlap, and observation is continuous and noiseless. Only the five consecutive integer Fourier modes are covered; no result is asserted for larger bandwidths, arbitrary measurable observation masks, unequal arc lengths, or general sample grids. The leading coefficient was known from previous work; the asserted contribution is its sharp finite-width extension and uniqueness. The checked literature is not an exhaustive proof of worldwide publication priority. Independent mathematical validation has not been performed.

## References
1. A. Azimifard, *Componentwise and Measure-Sensitive Bounds for One-Dimensional Time-Frequency Localization*, arXiv:2609.14946v1 (first public 2026-09-14), https://arxiv.org/abs/2609.14946.
2. *Sharp two-arc Fourier observability: a Legendre constant and asymptotic antipodal design*, published published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-two-arc-fourier-observability-a-legendre-constant-and-asym--900ee56c5370.
3. *Antipodal two-arc observation uniquely optimizes three-mode Fourier stability*, published published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-antipodal-two-arc-observation-uniquely-optimizes-three-mode-four--87a22b9723ef.
4. F. Marceca, J. L. Romero, M. Speckbacher, *Eigenvalue estimates for Fourier concentration operators on two domains*, arXiv:2301.11685 (first public 2023-01-27), https://arxiv.org/abs/2301.11685.
