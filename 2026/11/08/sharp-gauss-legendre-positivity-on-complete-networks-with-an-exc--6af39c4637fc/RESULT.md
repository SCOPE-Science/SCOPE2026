# Sharp Gauss–Legendre positivity on complete networks with an exceptional matching

## Finding
Let \(n\ge3\), and start with the complete graph on \(n\) vertices with unit conductances. Let \(M\) be any matching, possibly empty, and replace the conductance of each \(e\in M\) by an arbitrary \(t_e>0\); all other conductances remain one. For the resulting weighted Laplacian \(L\), the completed two-stage fourth-order Gauss–Legendre graph-heat step is
\[
T(h)=F(hL),\qquad F(x)=\frac{x^2-6x+12}{x^2+6x+12},\qquad h\ge0.
\]
Then \(T(h)\) is entrywise nonnegative for **every** \(h\ge0\) precisely when
\[
\boxed{t_e\le \frac{2(n-1)}{n-2}\quad\text{for every }e\in M.}
\]
In that case every entry of \(T(h)\) is strictly positive for \(h>0\). If the condition fails for one or more exceptional edges, its corresponding endpoint-to-endpoint entry becomes strictly negative for all sufficiently large \(h\), with exactly one positive zero and no subsequent recovery. The cutoff depends on \(n\), but neither on the number nor the positions nor the other conductances of the exceptional matching edges. When \(n=2\), the single-edge graph has a strictly positive completed transition for every positive conductance and every \(h>0\).

## Assumptions and scope
The graph is finite, undirected, with a symmetric combinatorial **weighted** Laplacian and strictly positive conductances. The modified edges form a matching, so they have pairwise disjoint endpoints. No restriction to strengthened edges is imposed: \(0<t_e<1\) is permitted. The assertion concerns the completed matrix \(F(hL)\), not stage values, strong-stability-preserving coefficients, nonlinear dynamics, or arbitrary weighted graphs. At \(h=0\), \(T(0)=I\). All quantified timesteps are real.

## Proof
For an exceptional edge \(e=\{a,b\}\), put \(v_e=\mathbf e_a-\mathbf e_b\) and \(P_e=v_ev_e^{\mathsf T}/2\). Because the edges of \(M\) are disjoint, the matrices \(P_e\) are pairwise orthogonal rank-one projectors, all orthogonal to \(P_0=J/n\). Writing \(L_0=nI-J\) for the unit-conductance complete-graph Laplacian gives the exact simultaneous spectral decomposition
\[
L=L_0+2\sum_{e\in M}(t_e-1)P_e
=\sum_{e\in M}\lambda_eP_e+n\biggl(I-P_0-\sum_{e\in M}P_e\biggr),
\qquad \lambda_e=n-2+2t_e>0.
\]
Consequently, since \(F(0)=1\),
\[
T(h)=P_0+F(nh)\biggl(I-P_0-\sum_{e\in M}P_e\biggr)
+\sum_{e\in M}F(\lambda_eh)P_e.
\tag{1}
\]
If distinct vertices \(i,j\) do not form an exceptional edge, the corresponding off-diagonal entry of every \(P_e\) is zero, giving
\[
T(h)_{ij}=\frac{1-F(nh)}{n}=
\frac{12h}{n^2h^2+6nh+12}>0\qquad(h>0).
\tag{2}
\]
For one exceptional edge \(e=\{a,b\}\) of conductance \(t\), put \(\lambda=n-2+2t\) and \(D_s(h)=s^2h^2+6sh+12\). Formula (1) gives the exact identity
\[
T(h)_{ab}=\frac1n+\frac{n-2}{2n}F(nh)-\frac12F(\lambda h)
=\frac{6h\,Q_{n,t}(h)}{D_n(h)D_\lambda(h)},
\tag{3}
\]
where
\[
Q_{n,t}(h)=\lambda\bigl[n^2-(n-2)\lambda\bigr]h^2+12\lambda h+24t.
\tag{4}
\]
All denominators and the last two coefficients are strictly positive for \(h\ge0\) and \(t>0\). Hence \(T(h)_{ab}>0\) for every \(h>0\) if and only if the quadratic coefficient is nonnegative. Since \(\lambda>0\) and \(n>2\), this is equivalent to
\[
n^2-(n-2)(n-2+2t)\ge0
\iff t\le 2(n-1)/(n-2).
\]
If \(t\) exceeds this cutoff, the coefficient in (4) is negative; the polynomial has one positive root, with positive values before and negative values after. In fact, on setting \(A=\lambda[(n-2)\lambda-n^2]>0\), this unique crossing time is
\[
h_* = \frac{12\lambda+\sqrt{144\lambda^2+96At}}{2A}.
\]
Thus the exceptional endpoint transition becomes negative exactly for \(h>h_*\). Its sign is unaffected by any other exceptional weights.

It remains to check diagonal entries. For all \(x\ge0\), the numerator of \(F\) is \((x-3)^2+3>0\) and the denominator is positive. The graph Laplacian is positive semidefinite, so \(F(hL)\) is positive definite for every finite \(h\ge0\); consequently its diagonal entries are strictly positive. Formulae (2)–(4) now establish the full entrywise criterion. Moreover \(T(h)\mathbf1=\mathbf1\) by \(F(0)=1\). For \(n=2\) the only nonzero Laplacian eigenvalue is \(2t\) and the off-diagonal entry is \((1-F(2th))/2>0\) for \(h>0\), as asserted.

## Verification
The accompanying standalone `verify.py` implements exact rational matrix inverses and independently checks the full matrix identity (1), the exceptional entry formula (3), row conservation, and the threshold coefficient for many sizes, disjoint matchings, rational conductances, and timesteps. Run `python3 verify.py`. It prints `VERIFY_OK` after the rational tests. This finite replay is a check of the algebra, not a replacement for the all-size and all-step proof above.

## Relationship to prior work
Lóczi and Ketcheson studied radii of absolute monotonicity for rational Runge–Kutta stability functions, a general tool for positivity preservation. Their global method-level criteria do not evaluate the entrywise positivity domain on this fixed, nonuniform family of graph Laplacians. Previously studied unweighted complete-graph and complete-multipartite cases correspond to setting all exceptional conductances equal to one and do not imply the sharp upper cutoff under heterogeneous matching perturbations. The key additional observation here is simultaneous diagonalization of mutually orthogonal edge-Laplacian perturbations, leading to an independent necessary-and-sufficient test for every exceptional edge.

## Limitations
No conclusion is asserted for exceptional edges that share a vertex, signed conductances, arbitrary weighted complete networks, nonlinear systems, or intermediate Runge–Kutta stages. The result is a direct exact classification within a specified structured family, not a theorem about universal preservation of positivity by Gauss–Legendre methods. The self-review does not constitute independent confirmation or an exhaustive priority determination.

## References
Lajos Lóczi and David I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651, first publicly submitted 26 March 2013; LMS Journal of Computation and Mathematics 17 (2014), 159–205. https://arxiv.org/abs/1303.6651
