# Harmonic reciprocal-degree spectrum and threefold isolation variance in random threshold digraphs

## Finding

Let \(n\ge 2\). For every label \(i\in\{1,\dots,n\}\), sample an independent pair \((X_i,Y_i)\) uniformly from \([0,1]^2\). Make a directed arc \(i\to j\), for distinct labels, exactly when \(X_i+Y_j>1\). Retain an undirected edge \(\{i,j\}\) **only when both opposite directed arcs occur**. Call the resulting undirected graph the *reciprocal graph*, write \(D_i\) for its degree, and let \(N_{n,k}=\#\{i:D_i=k\}\). Put \(H_0=0\) and \(H_m=\sum_{r=1}^m r^{-1}\).

**Theorem.** For every integer \(0\le k\le n-1\),
\[
\Pr(D_i=k)=\frac{H_n-H_k}{n},\qquad
\mathbb E N_{n,k}=H_n-H_k.
\]
In particular, if \(Z_n=N_{n,0}\) is the number of vertices incident to **no reciprocal edge**, then
\[
\mathbb E Z_n=H_n,\qquad
\lim_{n\to\infty}\frac{\operatorname{Var}(Z_n)}{\log n}=3,\qquad
\frac{Z_n}{\log n}\xrightarrow{\Pr}1.
\]
The variance constant is *three*, not one: rare reciprocal isolation events are sufficiently dependent to add two more logarithmic units of variance to the marginal contribution. This statement concerns reciprocal-edge isolation, which differs from having neither incoming nor outgoing directed arcs.

## Assumptions and scope

All \(2n\) coordinates are mutually independent and continuous uniform random variables. The graph has no loops; the strict threshold is indistinguishable from a weak threshold almost surely. The degree formula is exact for all finite \(n\ge2\) and all permissible \(k\). The variance and concentration statements concern \(n\to\infty\); the theorem does not claim a Gaussian central limit theorem, Poisson approximation, or a finite-sample closed form for the isolation variance.

## Proof

**1. The exact reciprocal-degree law.** Conditional on \((X_i,Y_i)=(x,y)\), a different label \(j\) is a reciprocal neighbor precisely when \(X_j>1-y\) and \(Y_j>1-x\). The conditional neighbor probability is \(xy\), and the neighbors are conditionally independent. Therefore
\[
D_i\mid(X_i,Y_i)=(x,y)\sim\operatorname{Bin}(n-1,xy).
\]
For independent uniforms, their product \(T=XY\) has density \(-\log t\), for \(0<t<1\). Consequently
\[
\Pr(D_i=k)=\binom{n-1}{k}\int_0^1 t^k(1-t)^{n-1-k}(-\log t)\,dt.
\]
Differentiating the beta integral in its first parameter (or expanding the polynomial and integrating termwise) gives
\[
\int_0^1 t^k(1-t)^{n-1-k}(-\log t)\,dt
=\frac{k!(n-1-k)!}{n!}(H_n-H_k).
\]
This proves the first formula. Exchangeability gives the second formula and \(\mathbb E Z_n=H_n\).

**2. Exact two-vertex isolation expression.** Write \(A_i=\{D_i=0\}\), \(z_i=X_iY_i\) for \(i=1,2\), and
\[
m=\min(X_1,X_2)\min(Y_1,Y_2),\qquad q=1-z_1-z_2+m.
\]
For each other vertex, the events of being a reciprocal neighbor of labels 1 and 2 are two rectangles of respective areas \(z_1,z_2\), whose intersection has area \(m\). Conditional on the four displayed coordinates, the probability that a third vertex is a neighbor of neither label is \(q\). Thus, letting \(E_{12}\) denote the direct reciprocal edge between labels 1 and 2,
\[
\Pr(A_1\cap A_2)=\mathbb E[\mathbf 1_{E_{12}^{\mathrm c}}q^{n-2}].
\]
With \(p_n=H_n/n\), exchangeability gives the exact identity
\[
\operatorname{Var}(Z_n)
=np_n(1-p_n)+n(n-1)\{\Pr(A_1\cap A_2)-p_n^2\}.
\]
We prove that the second term is \(2\log n+o(\log n)\).

**3. The direct-edge correction is negligible.** Let \(\varepsilon_n=10\log n/n\) for sufficiently large \(n\). Since \(q\le1-\max(z_1,z_2)\), the contribution of \(\max(z_1,z_2)>\varepsilon_n\) to \(\mathbb E[\mathbf 1_{E_{12}}q^{n-2}]\) is at most \((1-\varepsilon_n)^{n-2}=o(n^{-2})\). On \(z_1,z_2\le\varepsilon_n\) and \(E_{12}\), the inequalities \(X_1+Y_2>1\), \(X_2+Y_1>1\) force the following alternative: either both \(X_i\le2\varepsilon_n\) and both \(Y_i\ge1-2\varepsilon_n\), or both \(Y_i\le2\varepsilon_n\) and both \(X_i\ge1-2\varepsilon_n\). Indeed, split on \(X_1\le\sqrt{\varepsilon_n}\) and use \(X_iY_i\le\varepsilon_n\) plus the two cross inequalities. Those two four-dimensional boxes have total volume at most \(32\varepsilon_n^4=o(n^{-2})\). Hence
\[
n^2\mathbb E[\mathbf 1_{E_{12}}q^{n-2}]\longrightarrow0.
\]
It remains to study the covariance of the no-third-neighbor events.

**4. Logarithmic-coordinate overlap and the variance coefficient.** Define \(b=(1-z_1)(1-z_2)\). Because \(m\ge z_1z_2\), we have \(0\le b\le q\le1\). Independence of the two tagged coordinate pairs implies \(p_n^2=\mathbb E[b^{n-1}]\). Decompose
\[
q^{n-2}-b^{n-1}=(q^{n-2}-b^{n-2})+b^{n-2}(1-b).
\]
For each tag substitute \(u_i=-\log X_i\) and \(t_i=nX_iY_i\). The Jacobian is \(n^{-1}\,du_i\,dt_i\); the transformed domain is \(0<t_i<n\), \(0\le u_i\le L_i=\log(n/t_i)\). Since \(1-b\le (t_1+t_2)/n\) and \(b\le\exp[-(t_1+t_2)/n]\), the second term, after multiplying its expectation by \(n^2\), contributes at most
\[
\frac1n\int_0^n\!\int_0^n
L_1L_2(t_1+t_2)e^{-(n-2)(t_1+t_2)/n}\,dt_1\,dt_2
=O\!\left(\frac{(\log n)^2}{n}\right)=o(1).
\]
For the first term write \(\delta=u_1-u_2\). Its intersection area has a translation length \(\ell_n(t_1,t_2,\delta)\) with \(\ell_n/\log n\to1\) for each fixed \(t_1,t_2>0\), \(\delta\in\mathbb R\). More explicitly, for \(\delta\ge0\), \(\ell_n=(\min(L_1-\delta,L_2))_+\), while for \(\delta<0\), \(\ell_n=(\min(L_1,L_2+\delta))_+\). In these coordinates the common-neighbor rectangle area, multiplied by \(n\), equals
\[
a(t_1,t_2,\delta)=nm=
\begin{cases}
\min(t_1,t_2e^{-\delta}),&\delta\ge0,\\
\min(t_1e^{\delta},t_2),&\delta<0.
\end{cases}
\]
In particular \(q=1-(t_1+t_2-a)/n\) and \(b=(1-t_1/n)(1-t_2/n)\). For each fixed \(t_1,t_2,\delta\),
\[
q^{n-2}-b^{n-2}\longrightarrow
 e^{-t_1-t_2}(e^{a}-1).
\]
This limit can be integrated after division by \(\log n\). To justify it, for \(n\ge6\) the mean-value inequality gives
\[
0\le q^{n-2}-b^{n-2}
\le(n-2)(q-b)q^{n-3}
\le a\exp[-\max(t_1,t_2)/2],
\]
because \(q-b=(a-t_1t_2/n)/n\in[0,a/n]\) and \(q\le1-\max(t_1,t_2)/n\). For \(\delta\ge0\), \(a\le t_2e^{-\delta}\), and for \(\delta<0\), \(a\le t_1e^{\delta}\). Also \(0\le\ell_n/\log n\le1+|\log t_1|\) when \(n\ge3\). These bounds are integrable in \((t_1,t_2,\delta)\), so dominated convergence applies, yielding
\[
\begin{aligned}
&\lim_{n\to\infty}\frac{n^2}{\log n}
\bigl(\mathbb E[q^{n-2}]-p_n^2\bigr)\\
&\quad=\int_0^\infty\!\int_0^\infty e^{-t_1-t_2}
\int_{-\infty}^{\infty}(e^{a(t_1,t_2,\delta)}-1)\,d\delta\,dt_2\,dt_1.
\end{aligned}
\]
For \(\delta\ge0\), if \(T_1,T_2\) are independent unit-rate exponentials then \(a(T_1,T_2,\delta)=\min(T_1,e^{-\delta}T_2)\), an exponential variable of rate \(1+e^{\delta}\). Hence \(\mathbb E[e^a-1]=e^{-\delta}\). For \(\delta<0\) the expectation is \(e^{\delta}\) by symmetry. The displayed triple integral is therefore
\[
\int_0^\infty e^{-\delta}\,d\delta
+\int_{-\infty}^0 e^{\delta}\,d\delta=2.
\]
The previous step removes the direct-edge correction. Therefore
\[
n(n-1)\{\Pr(A_1\cap A_2)-p_n^2\}=2\log n+o(\log n).
\]
Finally \(np_n(1-p_n)=H_n+o(1)=\log n+O(1)\). Combining both contributions proves \(\operatorname{Var}(Z_n)=3\log n+o(\log n)\). Chebyshev's inequality and \(\mathbb E Z_n=H_n\sim\log n\) prove the stated convergence in probability.

## Verification

The included standalone `checker.py` implements exact rational beta-mixture computations and compares them with the harmonic formula for every degree of sample sizes through \(30\); it checks the rectangle intersection expression on a rational grid, the exponential overlap identity, and a fast independent graph construction against direct adjacency tests. It additionally performs seeded simulations as a non-proof sanity check for the logarithmic fluctuation size. Run it with `python3 checker.py` using Python's standard library. The asymptotic limit follows from the integrable bounds and analytical argument above, **not** from computational enumeration or Monte Carlo estimates.

## Relationship to prior work

Reilly, Scheinerman and Zhang introduced and studied exactly the underlying two-uniform-coordinate random threshold digraph. Their work gives in/out-degree, arc, connectivity and colorability properties and distinguishes the undirected graph formed by keeping an edge when **at least one** direction occurs. The reciprocal graph here instead keeps an edge only when **both** directions occur. The preceding harmonic reciprocal-degree profile and its threefold isolation variance are not stated in the inspected sections of their full paper (including the definitions and Section 4 results).

More recent general inhomogeneous-random-graph connectivity studies provide criteria for the existence of isolated vertices in broad graphon models, but do not, from the inspected statements, imply this particular finite degree spectrum and logarithmic variance coefficient. Results for fixed-outdegree reciprocal arcs and independent-arc directed graphs concern different edge dependencies. This evidence supports a provisional originality assessment, not a claim of exhaustive historical priority: an unlocated specialized symmetrization theorem may imply parts of the result.

## Limitations

The empirical checks are finite. The variance theorem gives only the leading coefficient, not an exact finite-\(n\) variance, limiting centered law, or concentration stronger than convergence in probability. The result relies on two independent uniform coordinates per vertex and the mutual-arc rule; it is not asserted for arbitrary directed graphons, other weight distributions, or the underlying at-least-one-arc undirected graph. Historical coverage cannot be excluded by unsuccessful literature or database searches alone.

## References

1. E. Reilly, E. R. Scheinerman and Y. Zhang, *Random Threshold Digraphs*, Electronic Journal of Combinatorics 21(2) (2014), P2.48, published 2014-06-09. DOI: https://doi.org/10.37236/4050 . Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v21i2p48/pdf/ .
2. J. Hladký and S. Viswanathan, *Connectivity of Inhomogeneous Random Graphs II*, Random Structures & Algorithms (2026). DOI: https://doi.org/10.1002/rsa.70098 . General graphon connectivity theory used only as a literature comparison.
3. *A Scalable Null Model for Directed Graphs Matching All Degree Distributions: In, Out, and Reciprocal*, arXiv:1210.5288 (2012). https://arxiv.org/abs/1210.5288 . Distinct model, considered for potential reciprocal-degree coverage.
