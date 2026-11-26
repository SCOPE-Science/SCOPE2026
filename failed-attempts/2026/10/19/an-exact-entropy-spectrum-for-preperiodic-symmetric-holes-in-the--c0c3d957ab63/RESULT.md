# An exact entropy spectrum for preperiodic symmetric holes in the negative-doubling map

## Finding

Let \(T:[0,1]\setminus\{1/2\}\to[0,1]\) be the negative-doubling map
\[
T(x)=\begin{cases}1-2x,&0\le x<1/2,\\2-2x,&1/2<x\le1.\end{cases}
\]
For every integer \(m\ge1\) set
\[
a_m=\frac12-\frac{1}{3\cdot2^{m+1}},\qquad
b_m=1-a_m,\qquad
S_m=\bigl\{x\in[0,1]:T^j(x)\notin(a_m,b_m)\ \text{for all }j\ge0\bigr\}.
\]
Because the hole contains \(1/2\), all survivor iterates are unambiguously defined. There is a unique real \(\lambda_m\in(1,2)\) satisfying
\[
\lambda_m^{m+1}=2\sum_{j=0}^{m-1}\lambda_m^j,
\tag{1}
\]
and the exact entropy and Hausdorff dimension are
\[
\boxed{h_{\rm top}(T|_{S_m})=\log\lambda_m,\qquad
\dim_{\rm H} S_m=\frac{\log\lambda_m}{\log2}.}
\tag{2}
\]
Moreover \(\lambda_m\) increases strictly to \(2\), and
\[
\log2-h_{\rm top}(T|_{S_m})
=\frac{1}{3\cdot2^m}\left(1+O(m2^{-m})\right)
=|b_m-a_m|\left(1+O(m2^{-m})\right).
\tag{3}
\]
For example, \(m=1\) gives the open hole \((5/12,7/12)\), entropy \(\tfrac12\log2\), and Hausdorff dimension \(1/2\). For \(m=2\), the hole is \((11/24,13/24)\) and \(\lambda_2\) solves \(\lambda_2^3-2\lambda_2-2=0\).

## Assumptions and scope

The parameter is any integer \(m\ge1\), with the map and **open** central hole as above. Its endpoints remain in the allowed set. The topology and dimension are those inherited from the real interval, not a circle quotient; \(0\) and \(1\) are distinct. The assertion concerns precisely this infinite, finite-preperiod boundary family; no entropy formula is claimed for an arbitrary symmetric or asymmetric hole. The maps on the compact survivor sets are continuous because the open hole removes the discontinuity. The Hausdorff dimension is the usual Euclidean dimension.

## Proof

**1. Exact finite Markov partition.** Write \(z_j=1/(3\cdot2^j)\) for \(0\le j\le m\). Subdivide the left permitted interval \([0,a_m]\) into \(m+2\) closed intervals with disjoint interiors:
\[
I_0=[0,z_m],\quad
I_i=[z_{m-i+1},z_{m-i}]\ (1\le i\le m),\quad
I_{m+1}=[z_0,a_m].
\]
Set \(J_i=1-I_i\) for their reflected right-side intervals. The finite endpoint set is mapped into itself: the two hole endpoints map to \(z_m\) and \(1-z_m\), and the numbers \(z_j\) map to \(1-z_{j-1}\) for \(j\ge1\), while \(z_0=1/3\) is fixed; reflections give the other endpoint orbits. The endpoints \(0,1\) form a two-cycle. Thus the following exact image relations are genuine Markov relations, where intersections with the permitted union \(K_m=[0,a_m]\cup[b_m,1]\) discard the hole:
\[
\begin{aligned}
T(I_0)&=J_0\cup J_1,\\
T(I_i)&=J_{i+1}&& (1\le i<m),\\
T(I_m)\cap K_m&=I_{m+1}\cup J_{m+1},\\
T(I_{m+1})&=I_1\cup\cdots\cup I_m.
\end{aligned}
\tag{4}
\]
The reflected relations are obtained by exchanging \(I\) and \(J\). In particular every allowed target interval is covered in full, with no partially covered interior; the discarded portions are precisely the middle hole or partition endpoints.

**2. The spectral polynomial.** Let \(A_m\) be the nonnegative \(2(m+2)\)-square transition matrix of these directed interval coverings, using the ordered states \(I_0,\ldots,I_{m+1},J_0,\ldots,J_{m+1}\). Reflection interchanges the \(I\) and \(J\) blocks. Its reflection-even quotient \(B_m\) has \(m+2\) states numbered \(0,\ldots,m+1\), with nonzero entries
\[
(B_m)_{0,0}=(B_m)_{0,1}=1,\qquad
(B_m)_{i,i+1}=1\quad(1\le i<m),
\]
\[
(B_m)_{m,m+1}=2,\qquad
(B_m)_{m+1,j}=1\quad(1\le j\le m).
\tag{5}
\]
The value \(2\) counts two distinct reflected target intervals and is **not** a doubled geometric length. Because \(A_m\) commutes with reflection, a nonnegative Perron eigenvector of \(A_m\) can be averaged with its reflection. Consequently the spectral radii of \(A_m\) and \(B_m\) agree. For a strictly positive eigenvalue \(\lambda>1\), the eigenvector equations on indices \(1,\ldots,m+1\) yield
\[
v_i=\lambda^{i-1}v_1\quad(1\le i\le m),\qquad
v_{m+1}=\lambda^mv_1/2,
\]
and then
\[
\lambda v_{m+1}=v_1+\cdots+v_m
\quad\Longleftrightarrow\quad
\lambda^{m+1}=2\sum_{j=0}^{m-1}\lambda^j.
\]
Conversely, every root \(\lambda>1\) of this equation supplies a positive eigenvector of \(B_m\): take \(v_1=1\) and \(v_0=1/(\lambda-1)\), then the displayed coordinates. Descartes' rule of signs, or monotonicity of the positive-return generating function, gives exactly one positive root of the polynomial on the right of (1). Since its value is \(1-2m<0\) at \(1\) and \(2>0\) at \(2\), this root lies in \((1,2)\). Its strictly positive eigenvector identifies it as \(\rho(B_m)=\rho(A_m)\).

**3. Entropy and dimension.** Every admissible infinite path in the finite directed graph determines a unique point in \(S_m\) by intersecting its successive inverse-branch intervals, whose diameters are at most \(2^{-n}\) times their initial diameter after \(n\) inverse steps. Conversely every survivor determines a path; only partition-endpoint points may have two descriptions, and such ambiguities are countable. Standard finite Markov coding therefore gives the topological entropy \(\log\rho(A_m)=\log\lambda_m\). Alternatively, the exponential growth of admissible cylinders with disjoint interiors gives the same number directly. The inverse edges are similarities of common contraction ratio \(1/2\) whose interval interiors are disjoint, so the graph-directed dimension formula, or a Perron mass-distribution and cylinder-cover argument, gives \(\dim_{\rm H}S_m=\log\lambda_m/\log2\). Equivalently, the constant-slope entropy/dimension identity for this map is established in [1, Section 4.4]. Endpoint identifications, being countable, do not alter dimension or entropy.

**4. Strict monotonicity and the first-order hole law.** Put \(p_m(t)=t^{m+1}-2\sum_{j=0}^{m-1}t^j\). The identity \(p_{m+1}(t)=t p_m(t)-2\) implies \(p_{m+1}(\lambda_m)=-2<0\), hence \(\lambda_{m+1}>\lambda_m\). Multiplying \(p_m(\lambda_m)=0\) by \(\lambda_m-1\) and factoring gives the exact equation
\[
(2-\lambda_m)(\lambda_m+1)\lambda_m^m=2.
\tag{6}
\]
If \(\lambda_m\) were bounded away from \(2\), its lower bound \(\lambda_m\ge\sqrt2\) and (6) would yield a contradiction, hence \(\lambda_m\uparrow2\). Writing \(\delta_m=2-\lambda_m\), (6) first shows \(\delta_m\le C(\sqrt2)^{-m}\), so \(m\delta_m\to0\). Then
\[
\delta_m=\frac{2}{(3-\delta_m)(2-\delta_m)^m}
=\frac{2}{3\cdot2^m}\bigl(1+O(m2^{-m})\bigr).
\]
Finally \(\log2-\log(2-\delta_m)=\delta_m/2+O(\delta_m^2)\), which is exactly (3) because the hole length equals \(1/(3\cdot2^m)\). \(\square\)

## Verification

The accompanying standalone program `verify_markov.py` uses only the Python standard library. It checks **exact rational** partition-image containment and the reflection quotient for each \(1\le m\le12\); independently computes exact matrix characteristic polynomials, verifying \(\det(tI-B_m)=(t-1)p_m(t)\) for \(1\le m\le7\), and the full \(A_m\) polynomial for \(1\le m\le4\). It also checks sample roots numerically for \(1\le m\le24\). Run `python3 verify_markov.py`; success prints `VERIFY_OK`. These bounded checks do not establish the infinite statement; equations (4)–(6) do.

## Relationship to prior work

Ding, Steiner, and Sun [1] study exactly the negative-doubling map with an open hole and establish symbolic plateau classification and qualitative Hausdorff-dimension staircases; their entropy/dimension correspondence is used in step 3. Their inspected full text does not specify the preperiodic symmetric family above or calculate its exact Perron polynomials and shrinking-hole asymptotic. Glendinning and Hege [2] analyze boundaries of positive-dimensional survivor sets in the broader two-branch decreasing class, without the stated infinite sequence of exact positive-entropy values. Related explicit work [3] classifies **zero-entropy** periodic spectra for symmetric holes with \(a\le2/5\), whereas our parameters all satisfy \(a_m\ge5/12>2/5\). The parity law [4] computes widths of *parameter plateaux*, not survivor entropy at the present parameter family. Neither statement implies (1)–(3). A published formula under different negative-base or kneading-determinant terminology remains a bibliographic possibility.

## Limitations

Only the countable explicit family \(a=a_m\), \(b=1-a_m\) is classified; the theorem does not interpolate between these holes, determine full parameter plateaux, give a pressure function, or claim statistical escape laws for general initial distributions. The spectral/Markov results concern the invariant compact survivor set, not one-step escape probabilities. The asymptotic is for the sequence of **integer** parameters \(m\to\infty\). Independent validation of this result has not been performed.

## References

[1] Y. Ding, W. Steiner, Y. Sun, *Open dynamical systems in topologically expansive decreasing Lorenz maps*, arXiv:2610.03327v1 (first public 2026-10-02), https://arxiv.org/html/2610.03327v1 .

[2] P. Glendinning, C. Hege, *The boundary of chaos for piecewise smooth maps and the boundary of positive Hausdorff dimension for survivor sets of open maps*, arXiv:2508.21429v1 (2025), https://arxiv.org/html/2508.21429v1 .

[3] *A three-phase periodic-orbit and zeta trichotomy for symmetric negative-doubling holes*, published-finding corpus research record `2026/10/11/SCOPE-a-three-phase-periodic-orbit-and-zeta-trichotomy-for-symmetric-n--8027a957802c`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-three-phase-periodic-orbit-and-zeta-trichotomy-for-symmetric-n--8027a957802c .

[4] *Exact parity law for negative-doubling survivor-plateau address widths*, published-finding corpus research record `2026/10/11/SCOPE-exact-parity-law-for-negative-doubling-survivor-plateau-address--195a748d0893`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-parity-law-for-negative-doubling-survivor-plateau-address--195a748d0893 .
