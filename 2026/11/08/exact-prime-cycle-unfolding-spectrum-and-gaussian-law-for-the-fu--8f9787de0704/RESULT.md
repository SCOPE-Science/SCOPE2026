# Exact prime-cycle unfolding spectrum and Gaussian law for the full tent map

## Finding

Let \(T:[0,1]\to[0,1]\) be the full tent map
\[
T(x)=\begin{cases}2x,&0\le x\le\frac12,\\2-2x,&\frac12\le x\le1.\end{cases}
\]
Its nonzero fixed point is \(a=2/3\). For every nonfixed periodic orbit \(\mathcal O\) with least period \(n\), put
\[
k(\mathcal O)=\#\{x\in\mathcal O:x>a,\ T(x)<a\}.
\]
The over-rotation number is \(k(\mathcal O)/n\); by the unimodal equality theorem for unfolding numbers [1, Corollary 4.11], this is also its unfolding number.

For integers \(m\ge2\) and \(1\le j\le\lfloor m/2\rfloor\), define
\[
C_{m,j}=\frac{m}{m-j}\binom{m-j}{j}2^j,
\qquad
E_{m,j}=C_{m,j}-2\,\mathbf1_{\{m=2j\}}.
\]
Then, for **every** \(n\ge2\) and \(1\le k\le\lfloor n/2\rfloor\), the exact number of **distinct primitive periodic orbits** with unfolding number \(k/n\) is
\[
\boxed{N_{n,k}=\frac1n\sum_{d\mid\gcd(n,k)}\mu(d)E_{n/d,k/d},}
\]
where \(\mu\) is the number-theoretic Möbius function. In particular \(N_{2,1}=1\), while \(N_{n,1}=2\) for every \(n\ge3\). The count is by geometric cycles, not by marked periodic points.

Choose uniformly among the primitive period-\(n\) cycles and write \(K_n=k(\mathcal O)\). As \(n\to\infty\),
\[
\boxed{\frac{K_n-n/3}{\sqrt n}\ \Longrightarrow\ \mathcal N\!\left(0,\frac{2}{27}\right).}
\]
Thus the unfolding numbers of most long primitive cycles approach \(1/3\), with the specified Gaussian fluctuations.

## Assumptions and scope

The map is **exactly** the slope-two full tent map, not an arbitrary unimodal map. A cycle has least period \(n\), may have a non-reduced unfolding fraction, and is counted once up to cyclic reindexing. The two fixed points \(0\) and \(2/3\) are excluded. No periodic point of least period greater than one lies at a partition boundary \(0,1/2,2/3,1\). The classical over-rotation statistic is well-defined because the displacement \(T(x)-x\) is positive for \(0<x<a\) and negative for \(a<x\le1\). Thus there are equal numbers of crossings in each direction and the half-count of direction switches equals \(k(\mathcal O)\). A nonfixed orbit must cross the fixed-point level at least once.

## Proof

**1. Exact Markov coding.** Partition the open nonboundary interval into
\[
A=(0,1/2),\quad B=(1/2,2/3),\quad C=(2/3,1).
\]
Their image-covering transitions are \(A\to A,B,C\), \(B\to C\), and \(C\to A,B\). The transition from \(C\) to either other state contributes one right-to-left crossing of \(a\). The marked adjacency matrix is
\[
M(z)=\begin{pmatrix}1&1&1\\0&0&1\\z&z&0\end{pmatrix},
\quad \det(tI-M(z))=t(t^2-t-2z).
\]
Every closed length-\(m\) admissible path has exactly one point with that periodic itinerary in the **closed** Markov intervals: compose its inverse affine branches, a contraction of factor \(2^{-m}\). Away from boundaries, this is a bijection between closed symbolic paths and actual points of \(\operatorname{Fix}(T^m)\), with the path weight equal to the number of right-to-left crossings.

There are precisely two boundary exceptions. The point \(0\), encoded by the all-\(A\) loop, contributes the constant \(1\) to the trace and is fixed. The other fixed point \(2/3\), sitting on the common \(B,C\) boundary, has two alternating \(BC\) phase codes of each **even** length \(m\); each has weight \(z^{m/2}\). There are no other periodic boundary points because \(1/2\mapsto1\mapsto0\) and \(1\mapsto0\). Consequently
\[
\sum_{\substack{x\in\operatorname{Fix}(T^m)\\x\notin\{0,2/3\}}}
 z^{\,\#\{0\le i<m:T^i(x)>a,\ T^{i+1}(x)<a\}}
=\operatorname{tr}(M(z)^m)-1-2\mathbf1_{\{2\mid m\}}z^{m/2}.
\]

**2. Closed-form weighted trace.** The nonzero eigenvalues of \(M(z)\) are
\[
\lambda_\pm(z)=\frac{1\pm\sqrt{1+8z}}2.
\]
By the binomial/Lucas recurrence \(u_m=u_{m-1}+2z\,u_{m-2}\), with \(u_0=2\), \(u_1=1\), the exact trace polynomial is
\[
\operatorname{tr}(M(z)^m)=\lambda_+(z)^m+\lambda_-(z)^m
=1+\sum_{j=1}^{\lfloor m/2\rfloor}\frac{m}{m-j}\binom{m-j}{j}2^j z^j.
\]
Subtracting the two boundary contributions gives precisely \(E_{m,j}\) as the number of nonfixed points fixed by the \(m\)-th iterate and exhibiting \(j\) crossings in those \(m\) iterates.

**3. Primitive-orbit inversion.** Let \(P_{n,k}\) denote the number of points of **least period** \(n\) making \(k\) crossings. If such a point is repeated \(d\) times to produce an \(m=dn\) iterate-fixed itinerary, the crossing number becomes \(dk\). Thus
\[
E_{m,j}=\sum_{d\mid\gcd(m,j)}P_{m/d,j/d}.
\]
Möbius inversion in the repeat factor gives \(P_{n,k}=\sum_{d\mid\gcd(n,k)}\mu(d)E_{n/d,k/d}\). Dividing by \(n\), the number of points in each primitive cycle, yields \(N_{n,k}\). For \(k=1\), only \(d=1\) occurs and \(E_{n,1}=2n\) for \(n\ge3\), proving the stated extremal count.

**4. Gaussian limit.** Put \(z=e^t\). For real \(t\) near zero, \(\lambda_+(e^t)\) is analytic and dominates \(\lambda_-(e^t)\). Direct differentiation gives
\[
\lambda_+(1)=2,\qquad
\left.\frac{d}{dt}\log\lambda_+(e^t)\right|_{t=0}=\frac13,\qquad
\left.\frac{d^2}{dt^2}\log\lambda_+(e^t)\right|_{t=0}=\frac{2}{27}.
\]
The weighted fixed-iterate polynomial is \(\lambda_+(e^t)^n+\lambda_-(e^t)^n-1-2\mathbf1_{\{2\mid n\}}e^{tn/2}\). Its nonprimitive points contribute at most \(O(n2^{n/2}e^{|t|n/2})\), since their least period divides a proper divisor of \(n\). Thus for \(t=s/\sqrt n\), for each fixed real \(s\), the ratio of the primitive-period polynomial to \(\lambda_+(e^t)^n\) tends to \(1\) exponentially. Normalize by the number of prime-\(n\) points, asymptotic to \(2^n\), and remove the deterministic centering \(s\sqrt n/3\). Taylor expansion gives the limiting moment-generating function \(\exp(s^2/27)\), that of \(\mathcal N(0,2/27)\). Uniform cycle sampling equals uniform primitive-point sampling because each cycle has exactly \(n\) points. The moment-generating-function convergence theorem proves the limit law.

## Verification

The standalone `CHECK.py` independently enumerates every branch-affine solution of \(T^m(x)=x\) with exact rational arithmetic for \(2\le m\le12\). It validates all symbolic branch conditions, tallies crossings, calculates least periods, and compares both the weighted iterate-fixed coefficients and Möbius-inverted primitive-orbit counts. The included program reports 8,202 exact comparisons. These finite checks do **not** replace the proof for all periods. Running `python CHECK.py` uses only the Python standard library.

## Relationship to prior work

Bhattacharya [1, Corollary 4.11] establishes equality of unfolding and over-rotation numbers for unimodal/bimodal patterns, enabling the interpretation of the statistic here. Blokh and Misiurewicz [2] establish over-rotation forcing and realization; Blokh and Snider [3] study unimodal over-rotation intervals and twist patterns. Han–Sun–Xi–Su [4] give an expanding-map existence theorem for particular over-rotation pairs. Those inspected results provide a **set of possible types or existence thresholds**, not the exact multiplicity of *every* primitive period/unfolding pair of the full tent map or its Gaussian limit. Markov trace methods are classical, but the marked boundary correction and the resulting joint orbit-count formula are the specific assertions here. An exact equivalent in unindexed symbolic-dynamics literature has not been ruled out.

## Limitations

The result is specific to the full tent map; it does not give counts for arbitrary slopes, kneading sequences or unimodal maps, nor a local limit theorem or large-deviation estimates. The identification with the unfolding invariant uses the published low-modality equivalence theorem [1]; the orbit-counting and Gaussian parts are proved independently from the piecewise-affine dynamics. The originality assessment is bounded by the inspected sources; it is not a claim of priority certification. Independent review has not been performed.

## References

[1] S. Bhattacharya, *Unfolding numbers for interval maps*, arXiv:2403.16549v1 (first posted 2024-03-25), Corollary 4.11; journal version, *Journal of Difference Equations and Applications* (2025), DOI:10.1080/10236198.2025.2459225. https://arxiv.org/html/2403.16549v1

[2] A. Blokh and M. Misiurewicz, *A new order for periodic orbits of interval maps*, *Ergodic Theory and Dynamical Systems* 17 (1997), 565–574. https://bpb-us-w2.wpmucdn.com/sites.uab.edu/dist/0/610/files/2025/09/ovefinal.pdf

[3] A. Blokh and K. Snider, *Over-rotation numbers for unimodal maps*, arXiv:1201.2861 (2012); *Journal of Difference Equations and Applications* 19 (2013), 1108–1132. https://people.cas.uab.edu/~ablokh/unim-12-12-11.pdf

[4] C. Han, T. Sun, H. Xi and G. Su, *Over-rotation pairs ... for periodic orbits of unimodal expanding self-maps on the interval*, *Journal of Mathematics* (2026), DOI:10.1155/jom/1678945. https://onlinelibrary.wiley.com/doi/10.1155/jom/1678945

[5] J. Olivares-Vinales, *Artin–Mazur zeta function for interval maps* (2024), arXiv:2405.10560. https://arxiv.org/abs/2405.10560
