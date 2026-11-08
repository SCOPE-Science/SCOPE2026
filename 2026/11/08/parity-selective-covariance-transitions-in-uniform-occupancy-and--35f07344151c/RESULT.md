# Parity-selective covariance transitions in uniform occupancy and hypercube walks

## Finding

Throw \(n\) distinguishable balls independently and uniformly into \(m\) labelled boxes, with integers \(m\ge3\), \(n\ge1\). Let \(N_j\) be the load of box \(j\), \(F_r=\sum_{j=1}^m\mathbf1\{N_j=r\}\) its frequency count at an integer \(1\le r\le n\), and \(H=\sum_{j=1}^m\mathbf1\{N_j\text{ is odd}\}\). In the equivalent simple random walk on the \(m\)-dimensional Boolean hypercube, each draw flips the selected coordinate, and \(H\) is exactly the Hamming distance from the initial vertex after \(n\) steps.

Put
\[
 u=\frac{m-3}{m-1},\qquad v=\frac{m-2}{m},\qquad p_r=\binom nr\frac{(m-1)^{n-r}}{m^n}.
\]
Then the complete finite-parameter covariance is
\[
\boxed{\operatorname{Cov}(F_r,H)=\frac{mp_r}{2}\left[(-1)^{r+1}-(m-1)u^{n-r}+mv^n\right].}
\tag{1}
\]
For \(m=3\), the convention \(u^0=1\) applies.

The covariance has the following exact sign structure:

1. For every **even** \(r\ge2\), it is strictly negative for all \(n\ge r\).
2. For \(r=1\), it is zero at \(n=1\) and strictly positive for all \(n\ge2\).
3. For every fixed **odd** \(r\ge3\), it is strictly negative at \(n=r\), strictly positive for every sufficiently large integer \(n\), and has precisely one negative-to-positive transition as \(n\) increases. There can be at most one zero-covariance integer, lying exactly at that transition. More formally, if \(T_{m,r}\) is the first positive-covariance integer \(n\ge r\), then all \(r\le n<T_{m,r}-1\) have negative covariance, \(n=T_{m,r}-1\) has nonpositive covariance, and all \(n\ge T_{m,r}\) have positive covariance.

For \(m=3\), the exact threshold is \(T_{3,r}=r+1\) for odd \(r\ge3\). For each fixed odd \(r\ge3\), as the number of boxes grows,
\[
\boxed{\lim_{m\to\infty}\frac{T_{m,r}}m=c_r,\qquad e^{2c_r}+2c_r=2r-1,\quad c_r>0,}
\tag{2}
\]
where the equation has exactly one positive solution. The threshold is therefore at the natural linear-in-dimension time scale, rather than the \(m\log m\) coupon-collection scale.

## Assumptions and scope

All allocations consist of a fixed number \(n\) of independent uniform box choices; the total number of balls is not Poissonized. The number of boxes \(m\ge3\), the frequency \(r\), and the sample length \(n\) are integer parameters, with \(1\le r\le n\). The covariance is between one frequency count and the total number of odd-load boxes, *not* between frequency count and the number of nonempty boxes. The Hamming-walk interpretation applies to a non-lazy walk starting at any vertex and independently selecting one of the \(m\) coordinate directions at every step. It does not concern vertex local times of the walk.

## Proof

For a fixed box \(j\), the load \(N_j\) is binomial with success probability \(1/m\), hence \(\Pr(N_j=r)=p_r\). The binomial parity identity gives
\[
\mathbb EH=\frac m2\left[1-\left(1-\frac2m\right)^n\right]=\frac m2(1-v^n).
\tag{3}
\]
Conditional on \(N_j=r\), the remaining \(n-r\) balls choose independently among the other \(m-1\) boxes, each with probability \(1/(m-1)\). Their individual odd-load probabilities are \([1-u^{n-r}]/2\). Thus
\[
\mathbb E[H\mid N_j=r]=\mathbf1\{r\text{ odd}\}+\frac{m-1}{2}(1-u^{n-r}).
\tag{4}
\]
Since \(F_r=\sum_j\mathbf1\{N_j=r\}\), exchangeability, (3), and (4) give
\[
\operatorname{Cov}(F_r,H)=m p_r\left(\mathbf1\{r\text{ odd}\}+\frac{m-1}{2}(1-u^{n-r})-\frac m2(1-v^n)\right),
\]
which is (1). Every prefactor \(mp_r/2\) is strictly positive.

For **even** \(r\), the bracket in (1) equals
\[
B_{m,r}(n)=-1-(m-1)u^{n-r}+mv^n.
\]
The identity \(v=[1+(m-1)u]/m\), together with strict convexity of \(x\mapsto x^n\) on \([0,1]\) for \(n\ge2\), yields
\[
 m v^n<1+(m-1)u^n\le1+(m-1)u^{n-r}.
\]
Here \(0\le u<1\) and \(n\ge r\ge2\). This proves \(B_{m,r}(n)<0\), including \(m=3\) with \(0^0=1\).

For **odd** \(r\), define
\[
S_{m,r}(n)=1-(m-1)u^{n-r}+mv^n,\qquad n\ge r.
\]
Its exact first difference is
\[
S_{m,r}(n+1)-S_{m,r}(n)=2\bigl[u^{n-r}-v^n\bigr].
\tag{5}
\]
If \(m>3\), both \(u,v\) lie in \((0,1)\), with \(u<v\), and the ratio \(u^{n-r}/v^n=u^{-r}(u/v)^n\) strictly decreases from \(1/v^r>1\) to zero. Therefore the sequence first strictly increases and then strictly decreases, except that one flat step can occur at its unique maximum. Its limiting value is \(1\), and all values on its eventual decreasing tail exceed \(1\). If \(m=3\), then \(S_{3,r}(r)=2-3+3(1/3)^r\), whereas \(S_{3,r}(n)=1+3(1/3)^n>0\) for \(n>r\). This also gives the stated exact threshold.

For \(r=1\), \(S_{m,1}(1)=0\), and (5) at \(n=1\) is \(2(1-v)>0\). The preceding unimodality and positive limiting value imply \(S_{m,1}(n)>0\) for all \(n\ge2\).

For odd \(r\ge3\), the initial value obeys
\[
S_{m,r}(r)=2-m+mv^r\le2-m+mv^2=-2+\frac4m<0.
\]
Unimodality and the positive limiting value then prove that the positive values form a nonempty final interval of integers, preceded by negative values and possibly one zero. This is the unique sign transition asserted above.

Finally fix odd \(r\ge3\) and \(c>0\), and take \(n=\lfloor cm\rfloor\). The expansions
\[
\log u=-\frac2m-\frac4{m^2}+O(m^{-3}),\qquad
\log v=-\frac2m-\frac2{m^2}+O(m^{-3})
\]
show, uniformly for \(c\) in compact subsets of \((0,\infty)\), that
\[
S_{m,r}(\lfloor cm\rfloor)\longrightarrow g_r(c):=1+(2c-2r+1)e^{-2c}.
\tag{6}
\]
The sign of \(g_r(c)\) equals that of \(e^{2c}+2c-(2r-1)\), which increases strictly from a negative value at \(c=0\) to infinity. Thus \(g_r\) has exactly one positive zero \(c_r\). For each \(0<c_-<c_r<c_+\), (6) makes the covariance negative at \(n=\lfloor c_-m\rfloor\) and positive at \(n=\lfloor c_+m\rfloor\) for all sufficiently large \(m\). The proved unique integer transition then forces \(c_-\le\liminf T_{m,r}/m\le\limsup T_{m,r}/m\le c_+\). Sending \(c_-\) and \(c_+\) to \(c_r\) gives (2).

## Verification

The standalone \(\texttt{verify\_parity\_occupancy.py}\) independently enumerates multinomial occupancy vectors with their exact combinatorial weights for small parameters and compares their direct covariance against (1). It also performs larger-grid exact-rational sign and one-transition checks, without floating-point sign decisions. The checker is invoked by \(\texttt{python\ verify\_parity\_occupancy.py}\) using only the Python standard library. The general statements in (1)–(2) follow from the analytical proof, not from this finite set of checks.

## Relationship to prior work

The classical frequency counts and their multinomial moment representation appear in Gnedin, Hansen and Pitman (2007). Barbour and Gnedin (2008) study the full family of frequency counts through Poissonization, their covariances and joint normal approximation, primarily in infinite unequal-box regimes. More recent work by Sagitov (2026) refines classical approximations for the covariances of individual occupancy frequency counts. These moment methods can be used to recover the raw covariance in (1) by summing over odd frequencies; the *raw moment identity alone is not asserted as novel*.

The additional statement here is a strict, all-finite-parameter **parity-dependent sign classification in sample length**, including uniqueness of the transition and the universal linear-time asymptotic constant (2). It is different from the established one-switch law for the covariance of the number of occupied boxes with one frequency count: occupied boxes are not odd-occupied boxes, and that law varies the frequency at fixed sample length rather than varying the sample length at fixed odd frequency. Hypercube-mixing papers study the marginal Hamming-distance law and convergence, not the frequency-resolved covariance sign threshold. No claim of exhaustive historical priority is made.

## Limitations

The strict sign theorem is for independent uniform allocations and \(m\ge3\), not heterogeneous box probabilities, random sample sizes, or nonuniform coordinate choices. The result concerns covariance rather than full positive/negative association, and does not determine whether the single possible threshold zero ever occurs for some integer parameters. At fixed \(r\), (2) establishes a scaling limit but no finite-\(m\) error estimate. Classical occupancy literature may contain an implicit equivalent via general mixed moments or generating functions; this remains a historical-priority risk and is distinct from mathematical correctness.

## References

1. A. Gnedin, B. Hansen and J. Pitman, *Notes on the occupancy problem with infinitely many boxes: general asymptotics and power laws*, arXiv:math/0701718, initially public 2007-01-24; *Probability Surveys* **4** (2007), 146–171. https://arxiv.org/abs/math/0701718
2. A. D. Barbour and A. V. Gnedin, *Small counts in the infinite occupancy scheme*, arXiv:0809.4387, initially public 2008-09-25; *Electronic Journal of Probability* **14** (2009), 365–384. https://arxiv.org/abs/0809.4387
3. S. Sagitov, *The Multinomial Allocation Model and the Size of a Randomly Chosen Box*, arXiv:2604.15152, initially public 2026-04-16. https://arxiv.org/abs/2604.15152
4. P. Diaconis, R. L. Graham and J. A. Morrison, *Asymptotic analysis of a random walk on a hypercube with many dimensions*, *Random Structures & Algorithms* **1** (1990), 51–72. https://doi.org/10.1002/rsa.3240010105
