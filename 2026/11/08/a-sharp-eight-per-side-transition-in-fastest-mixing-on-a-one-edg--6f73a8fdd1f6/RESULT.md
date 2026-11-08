# A sharp eight-per-side transition in fastest mixing on a one-edge-defective biclique

## Finding

For every integer \(n\ge3\), let \(G_n=K_{n,n}\setminus\{u_0v_0\}\). Consider all real symmetric, entrywise-nonnegative row-stochastic matrices \(P\) on its \(2n\) vertices for which \(P_{ij}=0\) whenever distinct vertices \(i,j\) are nonadjacent in \(G_n\); diagonal holding probabilities are permitted. Let \(\mu(P)=\|P-J_{2n}/(2n)\|_2\), the second-largest eigenvalue modulus (SLEM). Then the exact minimum is

\[
\boxed{\mu_n^*=\begin{cases}
1/\sqrt n,&3\le n\le7,\\[2mm]
\displaystyle\frac{n-2}{2(n-1)+\sqrt{n^2-8n+8}},&n\ge8.
\end{cases}}
\]

There is exactly one optimal matrix **invariant under the full graph automorphism group**. In it, each edge incident with exactly one of the two missing-edge endpoints has transition probability \(x_n\); each edge between two ordinary vertices of opposite sides has probability \(y_n\), where

\[
\boxed{(x_n,y_n)=\begin{cases}
\left(\frac1n,\frac{1}{2(n-1)}\right),&3\le n\le7,\\[2mm]
\left(\frac2{Z_n},\frac{n-2+\sqrt{n^2-8n+8}}{(n-1)Z_n}\right),&n\ge8,
\end{cases}\quad Z_n=2(n-1)+\sqrt{n^2-8n+8}.}
\]

Each diagonal entry is the residual probability needed for its row to sum to one. This invariant optimum is also a **global** optimum among all matrices, including non-invariant ones. We do **not** claim every global optimum is invariant or that the global optimizer is unique.

The threshold at \(n=8\) changes the active spectral constraints: below it the odd quotient pair \(\pm1/\sqrt n\) dominates, whereas at and above the new regime the positive ordinary within-class eigenvalue and both odd quotient extremes jointly bind. The minimum for \(G_8\) is \(3/(7+\sqrt2)\), compared with \(1/3\) for the intact \(K_{8,8}\). Moreover \(\mu_n^*\to1/3\) as \(n\to\infty\), despite the deleted edge.

## Assumptions and scope

All graph edges are simple and undirected; holding probabilities are permitted even though graph loops are not counted as ordinary edges. No reversibility condition beyond symmetry is added. The objective is the absolute value of both positive and negative nonconstant eigenvalues, not merely the second largest algebraic eigenvalue. For \(n\ge3\), the graph is connected; all entries of the exhibited off-diagonal edge weights are strictly positive, and every diagonal is nonnegative.

Write \(U=\{u_0,\ldots,u_{n-1}\}\), \(V=\{v_0,\ldots,v_{n-1}\}\), and delete only \(u_0v_0\). Symmetrizing an arbitrary admissible matrix over permutations of the ordinary vertices on each side and the swap \(u_i\leftrightarrow v_i\) leaves it admissible and cannot increase its operator-norm objective. Consequently at least one global optimum has the two-parameter form described above.

The two invariant edge orbits have sizes \(2(n-1)\) and \((n-1)^2\). For their probabilities \(x,y\), feasibility is exactly

\[
x\ge0,\quad y\ge0,\quad (n-1)x\le1,\quad x+(n-1)y\le1.
\]

The deficit endpoints have holding \(1-(n-1)x\), ordinary vertices have holding \(T=1-x-(n-1)y\).

## Proof

**1. Exact symmetry-reduced spectrum.** The independently varying subspaces of ordinary vertices, each of zero sum within one side, yield \(T\) with total multiplicity \(2(n-2)\). The exchange-even two-dimensional quotient has eigenvalues \(1\) and \(1-nx\). The exchange-odd quotient is the symmetric matrix

\[
M(x,y)=\begin{pmatrix}
1-(n-1)x&-\sqrt{n-1}\,x\\
-\sqrt{n-1}\,x&1-x-2(n-1)y
\end{pmatrix}.
\]

These account for all \(2n\) eigenvalues, including the constant eigenvalue. Put

\[
c=\frac{n-2}{2},\quad A=1-(n-1)x,\quad t=1-\frac n2 x-(n-1)y.
\]

Then \(T=t+cx\), while \(M\) has trace \(2t\) and centered eigenvalue radius \(\sqrt{(A-t)^2+(n-1)x^2}\). Its operator norm is

\[
F(x,t)=|t|+\sqrt{(1-(n-1)x-t)^2+(n-1)x^2}.
\]

Hence, over the feasible region, the exact SLEM is

\[
\mu(x,y)=\max\{|1-nx|,\ |t+cx|,\ F(x,t)\}.
\]

**2. The small-size branch.** By the Euclidean triangle inequality, for every \(x\ge0\) and every real \(t\),

\[
F(x,t)\ge F(x,0)=\sqrt{1-2(n-1)x+n(n-1)x^2}\ge\frac1{\sqrt n}.
\]

The last identity follows by completing the square, with equality exactly at \(x=1/n\). For \(x>0\), the first inequality is strict if \(t\ne0\). Thus equality requires \(x=1/n\) and \(t=0\), which determine \(y=1/[2(n-1)]\). At these values the remaining nontrivial eigenvalues are \(1-nx=0\) and \(T=(n-2)/(2n)\). The required bound \(T\le1/\sqrt n\) holds precisely for integers \(3\le n\le7\), because it is equivalent to \((n-2)^2\le4n\). The candidate is feasible: the two row sums of off-diagonal probabilities are \((n-1)/n\) and \(1/n+1/2\), at most one for \(n\ge2\). This proves the first branch and the unique invariant optimizer there.

**3. The large-size candidate and exact spectral feasibility.** Fix \(n\ge8\) and let

\[
D=n^2-8n+8,\quad Z=2(n-1)+\sqrt D,\quad
x_*=2/Z,\quad y_*=(n-2+\sqrt D)/((n-1)Z),\quad r_*=(n-2)/Z.
\]

Here \(D>4\), \(D<n^2\), and \(D<(n-2)^2\). These give \(2/(3n-2)<x_*<1/n\). Substitution shows \(t_*=0\), \(T_*=r_*\), \(A_*=\sqrt D/Z\), and

\[
A_*^2+(n-1)x_*^2=(D+4(n-1))/Z^2=r_*^2.
\]

Thus the exchange-odd eigenvalues are exactly \(\pm r_*\). The remaining nonconstant exchange-even eigenvalue is \((\sqrt D-2)/Z\in(0,r_*)\). Both types of holding probability are nonnegative: \((n-1)x_*<1\) and \(x_*+(n-1)y_*=1-r_*<1\). Consequently the claimed candidate is feasible and achieves SLEM \(r_*\).

**4. Global optimality of the large-size candidate.** We prove an unconstrained lower bound, stronger than needed for feasibility. The function \(F\) is convex in \((x,t)\). At \((x_*,0)\), write \(r=r_*\) and

\[
g=\left.\partial_xF\right|_{(x_*,0)}=\frac{(n-1)(nx_*-1)}{r}<0.
\]

The partial subdifferential in the \(t\)-direction there is the interval

\[
\partial_tF(x_*,0)=[-1-A_*/r,\ 1-A_*/r].
\]

Choose \(v=g/c\). The inequality \(v\ge-1-A_*/r\) is equivalent, after multiplying positive denominators and using \(r=cx_*\), to \(x_*\ge2/(3n-2)\). The upper inequality follows from \(v<0\) and \(A_*<r\). Both inequalities are strict, so \(v\) is an interior subgradient.

Set \(\theta=c/(c-g)\in(0,1)\). Then the two subgradients \((g,v)\) of \(F\) and \((c,1)\) of \(T=t+cx\) satisfy

\[
\theta(g,v)+(1-\theta)(c,1)=(0,0).
\]

The subgradient inequality for the convex function \(\theta F+(1-\theta)T\) therefore gives, for every real \(x,t\),

\[
\max\{F(x,t),T(x,t)\}\ge\theta F(x,t)+(1-\theta)T(x,t)
\ge\theta r+(1-\theta)r=r.
\]

As \(\mu\ge\max\{F,T\}\), no feasible invariant matrix can beat \(r\). The reduction in the assumptions then proves optimality against **every** admissible matrix, not just invariant matrices.

**5. Uniqueness among invariant matrices.** In the first branch the strict equality conditions in step 2 determine \(x,y\) uniquely. For \(n\ge8\), because \(v\) lies strictly inside the subdifferential interval for \(|t|\), the supporting inequality used above is strict whenever \(t\ne0\). When \(t=0\), the function \(F(x,0)=\sqrt{(1-(n-1)x)^2+(n-1)x^2}\) is strictly convex in \(x\) (its second derivative is positive for finite \(x\)), so equality in its supporting inequality forces \(x=x_*\). Then \(t=0\) forces \(y=y_*\). Hence the invariant optimum is unique; no statement about uniqueness among all non-invariant optima follows from averaging.

## Verification

Run `python verify.py` from a directory containing the complete supplied script. The verifier builds the full \(2n\)-vertex matrix independently of the block formula, diagonalizes it with a pure-Python symmetric Jacobi method, and compares every eigenvalue to the claimed representation. A reproducible local run passed 196 full-matrix eigenvalue comparisons, exact polynomial and boundary checks for \(3\le n\le399\), 21,000 feasible invariant-design comparisons, and 397 proposed-kernel feasibility/attainment comparisons. The exact symbolic proof in the preceding section covers all integers \(n\ge3\); these finite tests do not establish the infinite quantifier or novelty.

## Relationship to prior work

Boyd, Diaconis and Xiao formulate FMMC as a convex semidefinite program, prove symmetry averaging, and solve the **intact** complete bipartite graph with a single uniform edge probability. Boyd, Diaconis, Parrilo and Xiao develop orbit and block methods, again explicitly solve the intact complete biclique, and discuss other symmetric graph families. Jafarizadeh evaluates multipartite pseudo-distance-regular networks whose complete-crossing and straight-edge patterns differ from deleting one isolated crossing edge. None of the examined statements directly gives the defect graph's two edge orbits, the exact small-size \(1/\sqrt n\) branch, or the transition at eight vertices per part. These are comparisons to actual inspected claims, not proof of universal priority.

The central claim here is the **closed-form evaluation** of that established convex optimization problem for the minimally defective balanced biclique; the general SDP, symmetry reduction principle and complete-biclique optimum are not claimed as new. Other graph-specific results and unindexed equivalent reductions remain possible.

## Limitations

The classification covers balanced complete bipartite graphs with precisely one absent crossing edge, \(n\ge3\), uniform stationary law, symmetric transition matrices, unconstrained holding and the spectral SLEM objective. It does not give optimal mixing in total-variation at each finite time, nonuniform-stationary fastest mixing, unequal bipartitions, arbitrary edge failures, or every non-invariant optimizer. No independent mathematical audit has been performed. General published literature cannot be certified exhaustive.

## References

1. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. Primary full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf (published electronically 2004-10-29).
2. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1, first public arXiv date 2007-09-06, https://arxiv.org/abs/0709.0955. See especially Sections 3.1.2, 4 and 5.3.1.
3. S. Jafarizadeh, *Fastest Mixing Markov Chain on Symmetric K-Partite Network*, arXiv:1008.2588v1, 2010-08-16, https://arxiv.org/abs/1008.2588. See Section III on pseudo-distance-regular networks.
4. AMS, *MSC2020*, 90C22 (Semidefinite programming), https://mathscinet.ams.org/mathscinet/msc/msc2020.html.
