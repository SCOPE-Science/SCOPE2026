# Universal planar area spectrum of rational translated-cone-exchange cycles

## Finding
For the three-cone, zero-rotation translated-cone exchange with rational translation ratio \(\lambda=p/q\) in lowest terms, \(1\leq p<q\), the period spectrum of the invariant interpolation trapezium is exactly \(q,q+1,\ldots,p+q\). The normalized **two-dimensional Lebesgue area** occupied by least-period \(p+q-j\) points equals
\[
\mathbb P(\operatorname{per}=p+q-j)=\frac{2(p+q-j)w_j}{p(2q+p)},\quad
w_j=\begin{cases}\frac12&j\in\{0,p\},\\1&1\leq j\leq p-1.\end{cases}
\]
Every listed period occurs on a region of positive area; the probabilities are independent of both cone angles, despite the resulting trapezia having different shapes. For irrational \(\lambda\), all interior horizontal orbits are aperiodic and equidistributed along their own invariant horizontal interval. In particular, for \(\lambda=2/5\) the three periods \(7,6,5\) occupy respective area fractions \(7/24,1/2,5/24\).

## Assumptions and scope
Take \(0<\lambda<1\), \(\eta=1-\lambda\), and cone angles \(0<\alpha_0,\alpha_2<\pi/2\) with \(\alpha_1=\pi-\alpha_0-\alpha_2>0\). Let \(b_0=\cot\alpha_0\), \(b_2=\cot\alpha_2\), \(y_*=\lambda/(b_0+b_2)\), and set \(u=b_0y\), \(v=b_2y\) at height \(0<y<y_*\). The compact-height invariant region (with a half-open horizontal convention) is
\[
\mathcal T=\{(x,y):0<y<y_*,\quad u-1\leq x<\lambda-v\}.
\]
The map preserves height and acts on each interval \(J_y=[u-1,\lambda-v)\) by
\[
 h_y(x)=\begin{cases}x+\lambda&u-1\leq x<-v,\\
 x-\eta&-v\leq x<u,\\
 x-1&u\leq x<\lambda-v.
 \end{cases}
\]
This is exactly the three-interval exchange appearing in the interpolation trapezium of Cockram--Ashwin--Rodrigues, in the stated subfamily. The area spectrum refers exclusively to \(\mathcal T\), not to arbitrary points of the upper half-plane or its upper invariant strip. Rays and the two boundary heights are null sets and do not affect the normalized area formula. The half-open convention makes the slice dynamics a bijection everywhere on \(J_y\).

## Proof
**1. First-return representation.** On the circle \(C=[-1,\lambda)\) of circumference \(L=1+\lambda\), identify endpoints and let \(R(x)=x+\lambda\pmod L\), using representative coordinates in \(C\). The complement of \(J_y\) is one circular interval \(K_y=[\lambda-v,u-1)\) passing through the identified endpoint, with length \(c=u+v\). As \(0<c<\lambda\), the first return of \(R\) to \(J_y\) needs one step on the two outer branches of \(h_y\), and exactly two steps on its central branch. Indeed, for \(-v\leq x<0\), the first image is \(x+\lambda\in[\lambda-v,\lambda)\); for \(0\leq x<u\), it is \(x-1\in[-1,u-1)\). In both cases the second image is \(x-\eta\in J_y\). Therefore \(h_y=R_{J_y}\). The interval width is \(|J_y|=L-c\) and \(c=(\lambda/y_*)y\).

**2. Rational circle-orbit geometry.** Suppose \(\lambda=p/q\) in lowest terms and put \(N=p+q\). The circle rotation \(R\) has least period \(N\) at every point: \(N\lambda=p(1+\lambda)\), and coprimality rules out an earlier return. Each \(R\)-orbit consists of a translated uniform grid of \(N\) points spaced \(1/q\) on \(C\). Let \(z=qc=k+\theta\), with integer \(0\leq k\leq p-1\) and \(0\leq\theta<1\) (the equality cases are negligible in two-dimensional area). As the grid phase varies uniformly over one spacing \(1/q\), a circular deletion interval of length \((k+\theta)/q\) contains exactly \(k\) grid points for fraction \(1-\theta\) of phases and \(k+1\) for fraction \(\theta\). The induced map traverses **all** retained points of one original circle orbit before returning, so its least period is exactly \(N-k\) or \(N-k-1\), respectively.

**3. Horizontal area and size bias.** Parameterize grid phases by \(t\in[0,1/q)\); one phase corresponds to \(N-k\) or \(N-k-1\) retained starting points in \(J_y\). Thus the **horizontal Lebesgue lengths** of the two period classes are
\[
\ell_{N-k}(y)=\frac{(1-\theta)(N-k)}q,\qquad
\ell_{N-k-1}(y)=\frac{\theta(N-k-1)}q.
\]
These lengths sum to \(L-c=(N-k-\theta)/q\), as they must. In particular, assigning bare probabilities \(1-\theta\), \(\theta\) to starting points would be incorrect: the phase probabilities must be weighted by the numbers of retained points.

**4. Integrate over the trapezium.** Because \(c=(\lambda/y_*)y\), the band \(k<qc<k+1\) has \(dy=(y_*/\lambda q)d\theta\). Integrating \(\ell_{N-k}\) and \(\ell_{N-k-1}\) over \(\theta\in(0,1)\) gives respective (absolute) areas
\[
\frac{y_*}{2\lambda q^2}(N-k),\qquad
\frac{y_*}{2\lambda q^2}(N-k-1).
\]
For an interior integer \(1\leq j\leq p-1\), the class \(N-j\) receives one contribution from each adjacent band; for \(j=0,p\), it receives only one. The trapezium's total area is
\[
|\mathcal T|=\int_0^{y_*}(1+\lambda-(\lambda/y_*)y)dy
=y_*\left(1+\frac\lambda2\right)
=\frac{y_*(2q+p)}{2q}.
\]
Dividing contributions by this area and substituting \(\lambda=p/q\) yields the asserted formula. Its positivity proves that each stated period occurs on positive area; the two adjacent classes in each height band rule out other interior periods. The factor \(y_*\), which carries all angular dependence, cancels identically.

**5. Irrational parameter.** If \(\lambda\) is irrational then \(\lambda/(1+\lambda)\) is irrational. Its circle rotation is minimal and uniquely ergodic; the first return to a nonempty interval is an interval exchange preserving normalized Lebesgue measure and is also minimal and uniquely ergodic. Thus every orbit of \(h_y\) is aperiodic and equidistributed in \(J_y\) (with the specified half-open convention); the claim does not assert equidistribution across different heights.

## Verification
The self-contained Python program `check.py` uses only exact rational arithmetic. Running `python3 check.py` yields `PASS 9728 exact-rational assertions`. It verifies the three-branch first-return identity, exact point periods for finite rational grids, and integration identities for all coprime translation pairs with \(2\leq q\leq8\), using finitely many rational heights and phases. This confirms arithmetic and boundary bookkeeping in examples but cannot establish the all-parameter theorem; Steps 1--5 are the infinite proofs.

## Relationship to prior work
Cockram, Ashwin and Rodrigues construct the invariant interpolation trapezium and explicitly identify its three-interval slice exchange and its two Rauzy-related boundary exchanges (Theorem 3.1 and Eq. (3.7)); these structural facts are premises, not new claims here. Classical induced-rotation theory already explains why a three-interval exchange of this form has rational periodicity. The additional statement proved here is the **joint geometric area law**: its finite full period spectrum, size-biased horizontal lengths, and angular-independent proportions for normalized planar area, for every coprime \(p,q\). Related works on translated-cone-exchange renormalization and general IET periods do not in their inspected statements provide the stated normalized two-dimensional distribution.

## Limitations
The law is limited to the zero-rotation, three-cone invariant trapezium and uses normalized planar Lebesgue area, not natural measure on a fixed height or outside the trapezium. On the partition lines the original planar map may prescribe a different boundary convention; the area statement is invariant under those choices. No claim is made about nonlinear perturbations, general cone permutations, higher cone counts, or absolute publication priority. The source's earliest posting date is 2023-12-29; the section-3 presentation consulted is the later publicly accessible revision of that work. The exact origin date of that revision was not needed to date the originating paper, and the 2025 journal publication is not substituted for the original public date.

## References
- N. Cockram, P. Ashwin, and A. Rodrigues, *Construction of invariant curves for some Piecewise Isometries*, arXiv:2312.17412, first posted 2023-12-29; Theorem 3.1, Eq. (3.7), and discussion of the invariant trapezium in the accessible revised text. https://arxiv.org/abs/2312.17412 ; https://arxiv.org/html/2312.17412v1 (earlier version; four-cone presentation).
- N. Cockram, P. Ashwin, and A. Rodrigues, *Renormalization of Translated Cone Exchange Transformations*, arXiv:2312.17405, 2023. https://arxiv.org/abs/2312.17405
- P. Peres and A. Rodrigues, *On the Dynamics of Translated Cone Exchange Transformations*, arXiv:1809.05496, 2018. https://arxiv.org/abs/1809.05496
- F. Bas and D. López, *New Results on the Computation of Periods of IETs*, Mathematics 13 (2025), 3175, general IET period analysis. https://doi.org/10.3390/math13193175
