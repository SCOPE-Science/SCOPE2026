# Reentrant edge–isolation covariance in circular random geometric graphs

## Finding

Take \(n\ge2\) independent uniform points on a circle of circumference one, joining two distinct labeled points precisely when their *shorter circular distance* is at most \(0<r<1/2\). Let \(E_n\) be the number of edges and \(I_n\) the number of isolated vertices. Put \(q=1-2r\) and
\[
h(r)=1-\left(\frac{(1-3r)_+}{1-2r}\right)^2,\qquad (t)_+=\max(t,0).
\]
Then for every such \(n,r\),
\[
\boxed{\operatorname{Cov}(E_n,I_n)=\binom n2 q^{n-1}\bigl((n-2)h(r)-2nr\bigr).}
\]
The covariance is strictly negative at every \(0<r<1/2\) when \(2\le n\le5\). For every \(n\ge6\) it changes sign **twice**, in the exact order negative, positive, negative. Its two unique zeros are
\[
\boxed{r_-(n)=\frac{3n+10-\sqrt{9n^2-68n+100}}{16n},\qquad
r_+(n)=\frac{n-2}{2n}.}
\]
In particular, the smallest graph order permitting positive covariance is \(n=6\), with strict positivity exactly when \(1/4<r<1/3\). At fixed \(\lambda>0\), the sparse-regime asymptotic is
\[
\lim_{n\to\infty}\frac1n\operatorname{Cov}(E_n,I_n)\bigg|_{r=\lambda/n}
=\frac12 e^{-2\lambda}(3\lambda^2-4\lambda),
\]
while \(nr_-(n)\to4/3\) and \(r_+(n)=1/2-1/n\).

## Assumptions and scope

Points have independent Lebesgue-uniform positions in \(\mathbb R/\mathbb Z\), with coincidences of distinct labels permitted as null events. The graph is the hard-threshold, **fixed-size binomial** circular random geometric graph; no Poissonization or independent random edge thinning is applied. Distances use the geodesic metric on the circle. All theorems hold for integers \(n\ge2\), real \(0<r<1/2\); equalities at either zero have covariance zero. At \(r=0\) and \(r\ge1/2\), the graph is almost surely deterministic and the covariance is zero, outside the strict-sign domain stated here.

## Proof

Write \(A_{ij}\) for the edge indicator of labels \(i,j\) and \(B_k\) for the isolation indicator of label \(k\). By rotation invariance,
\[
\mathbb E A_{12}=2r,\qquad \mathbb E B_1=q^{n-1},\quad q=1-2r.
\]
An edge incident to a given vertex rules out its isolation, hence \(\mathbb E[A_{12}B_1]=\mathbb E[A_{12}B_2]=0\). Conditional on \(B_3=1\), the positions of the remaining \(n-1\) labeled vertices are independent and uniform on the complement of the open radius-\(r\) arc around vertex 3. That complement is a single arc of length \(q\). For two independent points in this arc, the circular route through the excluded arc has length at least \(2r>r\). Thus they are adjacent exactly if their absolute separation within the complement arc is at most \(r\), which has conditional probability
\[
\frac{1}{q^2}\int_0^q\!\int_0^q\mathbf1\{|u-v|\le r\}\,du\,dv
=1-\frac{(q-r)_+^2}{q^2}=h(r).
\]
Consequently \(\mathbb E[A_{12}B_3]=q^{n-1}h(r)\). Summing over the \(\binom n2\) edge candidates and \(n\) isolation candidates gives
\[
\begin{aligned}
\mathbb E(E_nI_n)&=n\binom{n-1}{2}q^{n-1}h(r),\\
\mathbb E E_n\,\mathbb E I_n&=\binom n2(2r)nq^{n-1},
\end{aligned}
\]
which proves the boxed exact covariance (the first formula also holds for \(n=2\), since its binomial coefficient is zero).

Since \(\binom n2q^{n-1}>0\), only \(F_n(r)=(n-2)h(r)-2nr\) determines the sign. For \(0<r\le1/3\), elementary expansion yields
\[
F_n(r)=-\frac{r}{(1-2r)^2}\bigl(8nr^2-(3n+10)r+4\bigr).
\]
For \(1/3\le r<1/2\), one has \(h(r)=1\) and
\[
F_n(r)=n-2-2nr.
\]
The two expressions agree at \(r=1/3\).

If \(n=2\), the quadratic is \(4(2r-1)^2>0\) on the first range; for \(n=3,4,5\), its discriminant \(9n^2-68n+100\) is respectively \(-23,-28,-15\), hence it is positive there. The second-range linear expression is at most \((n-6)/3<0\). This proves strict negativity for \(n\le5\).

If \(n=6\), the quadratic is \(48(r-1/4)(r-1/3)\); accordingly its contribution is negative before \(1/4\), positive on \((1/4,1/3)\), and zero at the endpoints. Above \(1/3\) the linear expression is negative. If \(n>6\), the quadratic \(Q_n(r)\) satisfies \(Q_n(0)=4>0\), \(Q_n(1/3)=(6-n)/9<0\), and has positive leading coefficient. Its smaller root is the displayed \(r_-(n)\) in \((0,1/3)\), and the larger root exceeds \(1/3\). On \([1/3,1/2)\) the linear expression crosses zero exactly once at \(r_+(n)=(n-2)/(2n)>1/3\). This establishes the complete two-crossing sign classification and the uniqueness of both zeros.

Expanding the smaller quadratic root gives \(r_-(n)=4/(3n)+O(n^{-2})\). For fixed \(\lambda>0\) set \(r=\lambda/n\) for sufficiently large \(n\). Then \(q^{n-1}\to e^{-2\lambda}\), and the exact identity
\[
h(r)-2r=\frac{r^2(3-8r)}{(1-2r)^2}
\]
shows \(nF_n(\lambda/n)\to3\lambda^2-4\lambda\). Together with \(\binom n2/n^2\to1/2\), this proves the sparse limit. Finally, the upper root is exact and already has the stated dense-boundary form.

## Verification

The accompanying standalone \(\texttt{verify.py}\) uses only the Python standard library. Executing \(\texttt{python3 verify.py}\) passes 588 exact algebraic, rational-sign, finite-grid enumeration, and grid-to-continuum checks. In particular it independently enumerates small discrete circular samples with replacement and checks their covariance against a conditional lattice-count formula; those *discrete* data are consistency checks, not a substitute for the integral proof. The rational examples \((n,r)=(6,3/10)\) and \((6,2/5)\) produce \(72/3125>0\) and \(-12/3125<0\) respectively. The proof itself establishes the continuum statement for all stated parameters.

## Relationship to prior work

Decreusefond and Ferraz (2010) analyze one-dimensional Poisson geometric graphs, principally connectivity-component distributions, with a section on circular coverage. They use random **Poisson** point counts and do not give the fixed-sample edge-versus-isolation covariance or its two sign crossings. Penrose (2015, later revised) studies isolated-vertex and edge counts in broader random connection models, but the inspected full-text results address marginal Poisson/normal approximation rather than a joint finite-sample covariance sign classification. Zhao, Yağan and Gligor (2015) study one-dimensional interval isolation/connectivity thresholds, not this circular joint count. Thus the reported result is a separately derived exact mixed-moment and sharp reentrant sign law; general stochastic-geometric factorial-moment techniques remain a possible unexamined route to implicit prior coverage.

## Limitations

This is an exact statement for the one-dimensional *circle* with a fixed number of iid uniform points and deterministic geodesic edge threshold. The theorem does not assert the same sign diagram for a bounded interval, a Poisson point process, soft edges, nonuniform points, or higher-dimensional tori. The covariance approaches zero in the near-complete dense regime; sign should not be confused with a uniformly large effect. The finite-grid checker does not prove any continuous/infinite-parameter assertion. Historical novelty has not been independently certified, and broader general-purpose moment formulae may imply its first identity without explicitly recording its phase boundaries.

## References

1. L. Decreusefond and E. Ferraz, *On the One dimensional Poisson Random Geometric Graph*, first arXiv release 2010-08-30, https://arxiv.org/abs/1008.5140 .
2. M. D. Penrose, *Inhomogeneous random graphs, isolated vertices, and Poisson approximation*, first arXiv release 2015-07-25, https://arxiv.org/abs/1507.07132 .
3. J. Zhao, O. Yağan, and V. Gligor, *A curious gap in one-dimensional geometric random graphs between connectivity and the absence of isolated node*, first arXiv release 2015-02-02, https://arxiv.org/abs/1502.00404 .
