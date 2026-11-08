# Parity law for Taylor heat positivity on complete multipartite graphs

## Finding

Let \(G=K_{a_1,\ldots,a_k}\) be an unweighted complete multipartite graph with \(k\ge2\), positive integer part sizes \(a_j\), and \(n=\sum_j a_j\ge2\). Let \(L\) be its combinatorial Laplacian and define the order-\(p\) Taylor heat update
\[
T_p(h)=\sum_{j=0}^{p}\frac{(-hL)^j}{j!},\qquad h\ge0,\quad p\ge2.
\]
Write \(F_p(x)=\sum_{j=0}^p(-x)^j/j!\), and put \(x=nh\). The update is row-stochastic in the row-sum sense at every step; entrywise nonnegativity is the issue.

**Even-order universality.** For every even \(p\ge2\), there is exactly one positive \(\beta_p\) satisfying \(F_p(\beta_p)=1\). For *every* complete multipartite partition of \(n\),
\[
T_p(h)\ge0\text{ entrywise}\quad\Longleftrightarrow\quad 0\le h\le\beta_p/n.
\]
Every diagonal and every within-part off-diagonal entry is positive for all \(h>0\), whenever the within-part entry exists. Entries between distinct parts turn negative for all \(h>\beta_p/n\). In particular \(\beta_2=2\), \(\beta_4=2.785293563405\ldots\); the latter is the classical RK4 end-step threshold on this entire family regardless of unequal vertex degrees.

**Odd-order root law and no reentry.** For odd \(p\ge3\), and for each part size \(a\), set \(c_a=1-a/n\in(0,1)\) and
\[
J_{p,a}(x)=c_aF_p(x)+(1-c_a)-F_p(c_ax),
\]
\[
D_{p,a}(x)=\frac1n+\left(1-\frac1a\right)F_p(c_ax)
 +\left(\frac1a-\frac1n\right)F_p(x).
\]
For every part size \(a\ge2\), \(J_{p,a}\) has exactly one positive zero \(\zeta_{p,a}\) other than its double zero at zero, is positive for \(0<x<\zeta_{p,a}\), and negative thereafter. For every part size \(a\ge1\), \(D_{p,a}\) is strictly decreasing from 1 to minus infinity, and hence has exactly one positive zero \(\delta_{p,a}\). The exact positivity criterion is
\[
T_p(h)\ge0\quad\Longleftrightarrow\quad 0\le nh\le
\min\bigl(\{\zeta_{p,a_j}:a_j\ge2\}\cup\{\delta_{p,a_j}:1\le j\le k\}\bigr).
\]
There is no later recovery. Cross-part entries stay strictly positive for *all* \(h>0\). Empty sets in the minimum are omitted.

**Explicit third-order partition law.** For \(p=3\), let \(s\) be the smallest part size at least 2, if one exists, and let \(\gamma_n>0\) be the unique solution of \(1+(n-1)F_3(\gamma_n)=0\). Define \(u=3/(2-s/n)\) if such \(s\) exists, and \(u=+\infty\) otherwise; define \(v=\gamma_n\) if any part has size one, and \(v=+\infty\) otherwise. Then
\[
T_3(h)\ge0\quad\Longleftrightarrow\quad 0\le nh\le\min\{u,v\}.
\]
For example, at the same \(n=12\), normalized third-order thresholds are \(2\) for \(K_{6,6}\), \(18/11\) for \(K_{2,2,2,2,2,2}\), and \(\gamma_{12}=1.722676294164\ldots\) for \(K_{11,1}\). Every one of these graphs has the same fourth-order normalized threshold \(\beta_4\).

## Assumptions and scope

All graph edges have unit conductance; graph parts may have unequal sizes and may include singleton classes. At least two parts are required. The update is the *endpoint* of the degree-\(p\) Taylor approximation of \(e^{-hL}\), not a claim about intermediate stages of a particular Runge--Kutta realization, nonlinear systems, or arbitrary graphs. Orders \(p\ge2\) are integers. For \(p=2,3,4\) these are the standard order-matched linear stability polynomials; higher orders mean the stated Taylor polynomial update. All inequalities are exact and include their endpoints.

## Proof

**1. Spectral projectors and three entry types.** For each part \(A_j\), put \(P_j=I_{A_j}-J_{A_j}/a_j\), embedded as a zero matrix outside that part, where \(J\) denotes an all-ones matrix. Define \(P_0=J_n/n\) and \(P_n=\bigoplus_j J_{a_j}/a_j-J_n/n\). These are mutually orthogonal projectors resolving the identity. Direct multiplication of the graph Laplacian gives
\[
L=nP_n+\sum_j(n-a_j)P_j,\qquad LP_0=0.
\]
Thus for every scalar polynomial \(F\) with \(F(0)=1\),
\[
F(hL)=P_0+F(nh)P_n+\sum_jF((n-a_j)h)P_j.
\]
We apply this identity to \(F(hL)=T_p(h)\) by taking \(F(t)=F_p(t)\). Write \(x=nh\). Entries in different parts equal
\[
C_p(x)=\frac{1-F_p(x)}{n}.
\]
For distinct vertices in the same part of size \(a\ge2\), they equal
\[
W_{p,a}(x)=\frac{c_aF_p(x)+1-c_a-F_p(c_ax)}{a}
=\frac{J_{p,a}(x)}a.
\]
A diagonal entry belonging to that part equals
\[
D_{p,a}(x)=W_{p,a}(x)+F_p(c_ax)
=\frac1n+\left(1-\frac1a\right)F_p(c_ax)+\left(\frac1a-\frac1n\right)F_p(x).
\]
These exhaust all matrix entries, proving row sums one and reducing positivity to scalar inequalities.

**2. Scalar Taylor signs.** Differentiation gives \(F_p'=-F_{p-1}\) and \(F_p''=F_{p-2}\). For every even \(2r\ge0\), \(F_{2r}(x)>0\) on \(x\ge0\): the integral Taylor remainder for \(e^{-x}\) gives \(F_{2r}(x)=e^{-x}+\frac{x^{2r+1}}{(2r)!}\int_0^1e^{-tx}(1-t)^{2r}\,dt\), with the harmless zero case at \(x=0\). Consequently, every odd \(F_{2r+1}\) is strictly decreasing from \(1\) to \(-\infty\). Also every even \(F_{2r}\), \(r\ge1\), is strictly convex, since \(F_{2r}''=F_{2r-2}>0\). Its derivative starts negative and changes sign exactly once because \(F_{2r}'=-F_{2r-1}\) and the odd function has exactly one zero. Therefore \(F_{2r}(x)-1\) has precisely the zeros zero and \(\beta_{2r}>0\), is negative between them, and positive thereafter.

**3. Even orders.** Convexity yields
\[
F_{2r}(c_ax)\le c_aF_{2r}(x)+(1-c_a)F_{2r}(0),
\]
strict for \(x>0\), so all existing within-part off-diagonal entries are strictly positive at every positive step. The diagonal is a positive-coefficient sum of positive scalar values by the projector formula, hence is always positive. Only the cross-part sign matters, and by Step 2 its condition is exactly \(x\le\beta_{2r}\). Since distinct parts exist, cross-part entries witness sharp failure for every \(x>\beta_{2r}\).

**4. Odd orders.** For odd \(p\ge3\), \(F_p\) decreases strictly from one to minus infinity, so \(C_p(x)>0\) for all \(x>0\). For each part, \(D_{p,a}(x)\) is a positive weighted combination of \(1,F_p(c_ax),F_p(x)\), with at least one strictly positive coefficient of \(F_p(x)\); it decreases strictly from 1 to minus infinity and has a unique positive zero. For the within-part Jensen gap, linear-interpolation error has the exact positive-kernel representation
\[
\frac{J_{p,a}(x)}{x^2}
=(1-c_a)\int_0^{c_a}tF_p''(xt)\,dt
+c_a\int_{c_a}^1(1-t)F_p''(xt)\,dt.
\]
Here \(F_p''=F_{p-2}\) is an odd Taylor polynomial, strictly decreasing on \([0,\infty)\) and tending to minus infinity. Therefore the displayed quotient decreases strictly from \(c_a(1-c_a)/2>0\) at \(x\downarrow0\) to minus infinity as \(x\to\infty\). This proves a unique positive zero \(\zeta_{p,a}\), with the stated sign pattern. Since each potentially negative entry type has precisely one permanent sign change, taking the minimum of their roots is both necessary and sufficient and excludes reentry.

**5. Third-order simplification.** The cubic identity is
\[
J_{3,a}(x)=\frac{c_a(1-c_a)x^2}{6}\bigl(3-(1+c_a)x\bigr),
\]
so \(\zeta_{3,a}=3/(1+c_a)=3/(2-a/n)\). If \(x\le\zeta_{3,a}\), then \(c_ax\le3c_a/(1+c_a)\le3/2\). Since \(F_3\) decreases and \(F_3(3/2)=1/16>0\), the diagonal in that nonsingleton part, \(D_{3,a}=J_{3,a}/a+F_3(c_ax)\), remains strictly positive throughout its within-part nonnegativity interval. Thus *no nonsingleton diagonal* can determine the first positivity loss. Among \(a\ge2\), \(3/(2-a/n)\) increases with \(a\), so the smallest such part determines the earliest within-part loss. A singleton part has diagonal \(D_{3,1}(x)=[1+(n-1)F_3(x)]/n\), whose sole positive zero is \(\gamma_n\). The displayed minimum in the finding follows, including graphs with only singleton parts or no singleton parts.

## Verification

The standalone Python 3 verifier `verify.py` uses only the standard library and exact rational arithmetic. It independently constructs complete multipartite Laplacians, forms the Taylor matrix by successive exact matrix multiplication, and compares every entry with all three projector formulas. It checks even-order positivity equivalence, the complete cubic partition criterion, and the exact cubic Jensen identity. The observed output was:

`VERIFY_OK exact_matrix_entry_and_cubic_identity_checks= 430180 partitions= 247`

Cases enumerate every ordered composition of orders \(2\le n\le8\) with at least two parts, every degree \(1\le p\le8\) at four rational normalized steps, and an additional 18,424 cubic-identity substitutions. These finite checks supplement the all-order proof above; they do not establish its infinite quantifiers independently. Scalar evaluations give \(\beta_2=2\), \(\beta_4\approx2.785293563405\), \(\beta_6\approx3.553441258462\), \(\beta_8\approx4.313627227774\).

## Relationship to prior work

Gottlieb, Shu and Tadmor (2001) study strong-stability-preserving higher-order time discretizations and give general linear-method CFL results; their inspected sections 2--3 do not determine exact entrywise positivity cutoffs for complete multipartite Laplacians. Horváth (2005) addresses positivity thresholds for Runge--Kutta methods in general; the available abstract does not resolve the graph-family classification, but its full specialist treatment was not inspected. Horváth, Song and Terlaky (2014 preprint; 2015 publication) prove general computable sufficient first-zero thresholds for Taylor and other discretizations on polyhedra; their inspected full text, especially section 3.1, does not give the present **exact** partition-independent even-order horizon, unique odd-order crossing law, or third-order minimum-part/singleton formula. A previously obtained theorem for regular bipartite graphs already covers the balanced \(K_{d,d}\), \(p=4\) special case; that special case is not claimed as new. The contribution here concerns all orders and arbitrary unequal multipartite partitions, with the odd/even structural distinction and complete sharpness.

## Limitations

The theorem concerns unweighted undirected complete multipartite graphs only, nonnegative final-step entries, and degree-\(p\) Taylor exponential polynomials. It neither claims intermediate Runge--Kutta stages are positive nor provides total-variation or nonlinear monotonicity guarantees. The full text of one relevant specialist positivity article (Horváth 2005) was not accessible in the inspected sources; the publication-priority assessment is therefore qualified. Related unindexed literature may contain equivalent specializations, and independent validation has not been performed.

## References

1. S. Gottlieb, C.-W. Shu and E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review **43** (2001), 89--112. Publicly released 2001-02-02. DOI: https://doi.org/10.1137/S003614450036757X ; author-authorized copy: https://drum.lib.umd.edu/bitstreams/faa96f40-0fbb-4af0-84a3-5e3b80c908df/download
2. Z. Horváth, *On the positivity step size threshold of Runge-Kutta methods*, Applied Numerical Mathematics **53** (2005), 341--356. DOI: https://doi.org/10.1016/j.apnum.2004.08.026
3. Z. Horváth, Y. Song and T. Terlaky, *Steplength thresholds for invariance preserving of discretization methods of dynamical systems on a polyhedron*, Discrete and Continuous Dynamical Systems **35** (2015), 2997--3013. First arXiv public version dated 2014-06-26, https://arxiv.org/abs/1406.6755 ; freely readable preprint: https://optimization-online.org/wp-content/uploads/2014/06/4408.pdf
