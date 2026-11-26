# Exact finite-sample area law and rhombus extremizers for boundary-random parallelograms

## Finding
Let \(Q\subset\mathbb R^2\) be any nondegenerate Euclidean parallelogram, with adjacent side lengths \(a,b>0\) and Euclidean area \(A>0\). For each integer \(N\ge3\), choose \(N\) independent points uniformly with respect to arclength on the full boundary, and let \(H_N\) be their convex hull. Put \(L=2(a+b)\) and \(k=N+2\). Then

\[
\frac{\mathbb E[\operatorname{area}(H_N)]}{A}=
1-\frac{2L^2}{ab(N+1)(N+2)}\left[1-
\left(1-\frac aL\right)^k-\left(1-\frac bL\right)^k+
\left(\frac aL\right)^k+\left(\frac bL\right)^k\right].
\]

The normalized mean is independent of the angle between the sides. For fixed \(N\), it is **strictly decreasing** in \(z=|a-b|/(a+b)\in[0,1)\). Consequently the sharp bounds over all nondegenerate parallelograms are

\[
1-\frac4{N+1}(1-2^{-N})
<\frac{\mathbb E[\operatorname{area}(H_N)]}{A}
\le 1-\frac{32}{(N+1)(N+2)}
\left[1-2\left(\frac34\right)^{N+2}+2\left(\frac14\right)^{N+2}\right].
\]

Equality on the right occurs exactly for **rhombi** (\(a=b\)); the lower bound is an unattained infimum as \(a/b\to0\) or \(a/b\to\infty\). For rectangles, this makes the square the unique maximizing similarity class. At \(N=3\), the entire law simplifies to \(\mathbb E[\operatorname{area}(H_3)]/A=\bigl(1+ab/(a+b)^2\bigr)/8\). For each fixed pair \(a,b>0\),

\[
1-\frac{\mathbb E[\operatorname{area}(H_N)]}{A}
=\frac{8(a+b)^2}{ab(N+1)(N+2)}+O_{a,b}\!\left(\frac{\rho^N}{N^2}\right),
\qquad\rho=1-\frac{\min(a,b)}{2(a+b)}<1.
\]

## Assumptions and scope
All boundary points are sampled **with replacement**, independently, according to normalized Euclidean arclength, not uniform area or equal probability per side. The zero-probability event of a sample exactly at a vertex does not affect any formula. The hull may be degenerate when all sampled points lie on one side; it is then assigned area zero. The statement concerns all nondegenerate parallelograms, including skew rhombi, for every integer \(N\ge3\). The angle-independence is for the normalized area, not the unnormalized Euclidean area.

## Proof
**1. Arclength-preserving affine reduction.** Let the adjacent edge vectors of \(Q\) be \(u,v\), with \(\|u\|=a\), \(\|v\|=b\). The affine map from the rectangle \(R=[0,a]\times[0,b]\) to \(Q\) taking its coordinate sides to \(u,v\) preserves Euclidean length separately on all four sides. It therefore transports normalized boundary arclength exactly. Its determinant has absolute value \(A/(ab)\), so the random hull area divided by the containing area is unchanged. It suffices to calculate the ratio for \(R\).

**2. Cyclic consecutive-pair identity.** Parameterize the rectangle counterclockwise by the arclength-periodic map \(P:[0,L)\to\partial R\), starting at \((0,0)\). For \(s\in[0,L]\), let

\[
C(s)=\int_0^L\det(P(t),P(t+s))\,dt,
\]

where the second argument is periodic. Ordering the \(N\) sampled parameters cyclically and applying the shoelace formula is valid even with collinear samples (their intermediate determinants telescope). A specified *ordered* pair of sampled labels is consecutive counterclockwise when all \(N-2\) other points avoid its intervening boundary arc of length \(s\), an event of probability \((1-s/L)^{N-2}\). Summing over the \(N(N-1)\) labeled ordered pairs gives the exact identity

\[
\mathbb E[\operatorname{area}(H_N)]=\frac{N(N-1)}{2L^2}
\int_0^L C(s)\left(1-\frac{s}{L}\right)^{N-2}ds.
\]

**3. Exact rectangle cross-correlation.** The arclength coordinates of the four vertices are \(0,a,a+b,2a+b\). Writing \(\Delta_i\) for the jump in the unit velocity \(P'\) at each vertex yields, in cyclic order,

\[
\Delta_0=(1,1),\quad\Delta_1=(-1,1),\quad
\Delta_2=(-1,-1),\quad\Delta_3=(1,-1).
\]

Differentiate the correlation distributionally four times. Since \(P''\) is the sum of these velocity jumps at the vertex parameters, the contributions from all ordered vertex pairs reduce, on \((0,L)\), to

\[
C^{(4)}(s)=4\delta_a+4\delta_b-4\delta_{L-a}-4\delta_{L-b}.
\]

Here \(\delta_t\) denotes a unit Dirac point mass at \(t\), with coincident masses added when \(a=b\). The identity \(C(-s)=-C(s)\), \(C(0)=0\), the shoelace integral \(C'(0)=2ab\), and periodicity of \(C''\) determine \(C''(0)=0\) and \(C'''(0+)=-4\). Four integrations therefore give, for \(0\le s\le L\),

\[
C(s)=2ab\,s-\frac23s^3+\frac23\left[(s-a)_+^3+(s-b)_+^3
-(s-L+a)_+^3-(s-L+b)_+^3\right],
\]

where \((x)_+=\max(x,0)\). This identity also follows by direct piecewise integration of the four edges.

**4. Beta integration.** For \(0\le u\le L\),

\[
\int_0^L(s-u)_+^3\left(1-\frac{s}{L}\right)^{N-2}ds
=\frac{6L^4}{(N-1)N(N+1)(N+2)}
\left(1-\frac uL\right)^{N+2},
\]

and \(\int_0^Ls(1-s/L)^{N-2}ds=L^2/[N(N-1)]\). Substitution into the consecutive-pair identity gives the displayed exact formula with \(\operatorname{area}(R)=ab\), and Step 1 transfers it to \(Q\).

**5. Sharp shape order.** Set \(z=|a-b|/(a+b)\) and \(k=N+2\). The normalized missed-area fraction can be rewritten as

\[
D_N(z)=1-\frac{\mathbb E[\operatorname{area}(H_N)]}{A}
=\frac{32}{k(k-1)}\frac{F_k(z)}{1-z^2},
\]

with

\[
F_k(z)=1-\frac{(3+z)^k+(3-z)^k-(1+z)^k-(1-z)^k}{4^k}.
\]

Because \(F_k(1)=0\), binomial expansion gives the positive-coefficient identity

\[
\frac{F_k(z)}{1-z^2}
=\sum_{j=1}^{\lfloor(k-1)/2\rfloor}
\frac{2\binom{k}{2j}(3^{k-2j}-1)}{4^k}
\left(1+z^2+\cdots+z^{2(j-1)}\right).
\]

Every coefficient is positive; in particular the \(j=2\) term is present for \(k\ge5\). Hence \(D_N(z)\) is strictly increasing in \(z\in[0,1)\), proving the unique length-ratio maximizer \(z=0\). Its value is obtained by substituting \(z=0\). Taking \(z\uparrow1\) and using \(F_k'(1)=-k(1-2^{2-k})/4\) yields the sharp unattained lower bound. For fixed \(a,b\), the four terms raised to \(k\) decay exponentially with maximum base \(\rho<1\), giving the stated asymptotic remainder. Finally \(N=3\) follows by evaluating \(k=5\) and simplifying.

## Verification
The companion standalone `CHECK.py` checks 36 cross-correlation integral instances against the explicit cubic spline, 24 independent arclength Monte Carlo configurations with \(6{,}000\) draws each, and exact rational positivity and polynomial identities for every integer \(3\le N\le64\). It also checks the exact three-point values \(5/32\) for equal sides and \(11/72\) for side ratio \(1:2\). These finite checks corroborate, but do not replace, the general analytical argument in Steps 1–5.

## Relationship to prior work
Reitzner, Schütt and Werner (first public preprint 2019, journal article 2023) study random boundary-point convex hulls of simple polytopes and derive asymptotics for face counts and missed volumes. Their primary results do not state this all-sample-size parallelogram expression, the angle-independence, or the exact rhombus extremizer. The finite-sample result here is not claimed as a theorem about arbitrary polygons or higher-dimensional simple polytopes. Earlier interior-point square formulas and chord-length statistics correspond to different probability experiments.

## Limitations
The formula is for Euclidean arclength sampling on four-sided parallelograms only. It is not asserted for general quadrilaterals, unequal edge sampling conventions, or uniform interior points. It does not determine the distribution or variance of the random hull area. Originality remains subject to possible unindexed historical exact evaluations; no independent audit has been performed.

## References
1. M. Reitzner, C. Schütt and E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917, first version 2019-11-14; *Discrete & Computational Geometry* **69** (2023), 453–504, DOI:10.1007/s00454-022-00460-2.
2. N. Turchi and F. Wespi, *Limit theorems for random polytopes with vertices on convex surfaces*, arXiv:1706.02944 (2017); treats smooth convex surfaces, not the finite-size parallelogram law.
