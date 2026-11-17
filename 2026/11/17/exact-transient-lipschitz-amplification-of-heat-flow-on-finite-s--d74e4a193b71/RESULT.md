# Exact transient Lipschitz amplification of heat flow on finite stars

## Finding
For every integer \(m\ge1\), let \(S_m=K_{1,m}\) be a star with center \(o\), leaves \(v_1,\ldots,v_m\), unit edges, and graph distance. Put \(L_m=D-A\) (the **unnormalized** graph Laplacian), \(H_t=\exp(-tL_m)\), and
\[\operatorname{Lip}(f)=\max_{1\le i\le m}|f(v_i)-f(o)|.\]
The exact operator Lipschitz norm for all \(t\ge0\) is
\[\boxed{\mathcal A_m(t)=\frac{2(m-1)}m e^{-t}-\frac{m-2}m e^{-(m+1)t}.}\]
This covers \(m=1\), when the value is \(e^{-2t}\). The norm is nonincreasing and at most one for \(m\le3\). For \(m\ge4\) it rises strictly above one immediately after zero and has a unique strict global maximum at
\[\boxed{t_m=\frac1m\log\left(\frac{(m+1)(m-2)}{2(m-1)}\right)>0.}\]
The resulting sharp time-independent Lipschitz amplification constant is
\[\boxed{\mathcal C_m=\frac{2(m-1)}{m+1}\left(\frac{2(m-1)}{(m+1)(m-2)}\right)^{1/m}.}\]
For \(m\ge4\), \(\mathcal C_m>1\), and
\[\mathcal C_m=2-\frac{4+2\log(m/2)}m+O((\log m)^2/m^2).\]
In particular the supremum of these constants over finite stars is exactly \(2\), but no single finite star attains two. Thus a positivity-preserving Markov heat semigroup can transiently almost double the graph-Lipschitz seminorm.

## Assumptions and scope
Functions are real-valued on all vertices. The semigroup is that of the degree-minus-adjacency Laplacian, **not** the normalized random-walk Laplacian. The graph metric has every edge length one. Operator norms are on the quotient of real functions by constants, whose norm is the Lipschitz seminorm above. The sign classification below is for \(m\ge2\), \(t>0\). At \(t=0\) every input class is trivially norming if its norm is one.

## Proof
Write \(d_i=f(v_i)-f(o)\) and \(\bar d=m^{-1}\sum_{i=1}^m d_i\). The edge-difference map \(f\mapsto d\) is onto \(\mathbb R^m\), with kernel the constants, and is an isometry onto \(\ell_\infty^m\). Directly from \(\partial_t f=-L_mf\),
\[\dot d_i=-(d_i+\sum_{j=1}^m d_j).\]
Consequently the mean difference evolves by \(\bar d(t)=e^{-(m+1)t}\bar d(0)\), and the transverse components by \(d_i(t)-\bar d(t)=e^{-t}(d_i(0)-\bar d(0))\). Hence the induced edge operator is the exact matrix
\[E_t=e^{-t}\left(I-\frac1m J\right)+e^{-(m+1)t}\frac1mJ,\]
where \(J\) is the all-ones matrix. Its diagonal entry is \((m-1)e^{-t}/m+e^{-(m+1)t}/m>0\), while every off-diagonal entry equals \((e^{-(m+1)t}-e^{-t})/m<0\) when \(t>0\). Summing absolute values in any row gives the displayed \(\mathcal A_m(t)\), and because the edge map is onto there is no hidden cycle constraint: this is the **exact** Lipschitz norm, not merely an upper estimate. For \(m\ge2\) and \(t>0\), each row has no zero coefficients. Equality in the scalar triangle inequality forces \(d_i\) to share one sign and every other \(d_j\) the opposite sign, all with equal absolute magnitude. All rows have the same absolute sum, giving precisely the claimed norming classes.

For \(m=1\) the expression simplifies to \(e^{-2t}\). For \(m\ge2\), differentiating gives
\[\mathcal A_m'(t)=-\frac{2(m-1)}m e^{-t}+\frac{(m+1)(m-2)}m e^{-(m+1)t}.\]
When \(m=2\), the norm is \(e^{-t}\); when \(m=3\), the derivative is zero at \(t=0\) and strictly negative thereafter. For \(m\ge4\), the derivative at zero is \(m-3>0\) and its unique zero is \(t_m\); the derivative is negative afterward, and \(\mathcal A_m(t)\to0\). Inserting \(e^{-mt_m}=2(m-1)/((m+1)(m-2))\) into the row-sum expression yields \(\mathcal C_m\). Since \(\mathcal A_m(0)=1\) and its initial derivative is positive, \(\mathcal C_m>1\). Finally, with \(Q_m=(m+1)(m-2)/(2(m-1))\), we have \(\log Q_m=\log(m/2)+O(1/m)\) and \(2(m-1)/(m+1)=2-4/m+O(m^{-2})\). Expanding \(Q_m^{-1/m}\) proves the asymptotic statement and the nonattainment of the family supremum.

For the Wasserstein interpretation, finite Kantorovich–Rubinstein duality identifies \(\sup_{\operatorname{Lip}(f)\le1}|(H_tf)(u)-(H_tf)(v)|\) with the \(W_1\) distance between the heat kernels started from \(u,v\). The maximal ratio over vertex pairs occurs on an edge, by concatenating a shortest path and applying the triangle inequality. The previous operator calculation therefore also gives the exact largest normalized heat-kernel \(W_1\) distance over pairs of distinct vertices. No probabilistic independence or diffusion approximation is involved.

## Verification
The included standalone `verify_star_heat.py` checks the exact edge matrix from two independently constructed representations: the semigroup's action on the center and individual leaves via its spectral projections, and the claimed direct edge formula. It then exhaustively tests all sign corners of the Lipschitz unit cube for a range of star sizes and rational exponential time values. These finite calculations corroborate, but are not the proof of, the all-\(m\), all-\(t\) assertion. The analytical argument above establishes that assertion.

## Relationship to prior work
Bauer–Horn–Lin–Lippner–Mangoubi–Yau studied graph heat-kernel gradient estimates and graph curvature; their first public arXiv version is dated 11 June 2013. Münch–Wojciechowski (arXiv:1712.00875, Theorem 3.8) proved that Ollivier-type curvature lower bounds are equivalent to exponential Lipschitz semigroup estimates on general graph Laplacians. In particular, qualitative nonexpansivity and its failure must not be presented as a new curvature principle. The present result instead gives the **complete exact finite-time operator norm**, unique time of peak amplification, rigidity of all maximizing inputs, and asymptotically sharp factor two specifically for the unnormalized star family. No claim of general-tree or normalized-Laplacian formulas is made. Exact star graph spectra are elementary and are used transparently; a historical implicit evaluation of this particular sharp norm remains possible.

## Limitations
The theorem does not concern metric graphs with continuous edges, normalized Laplacians, weighted edges, arbitrary trees, or target-valued nonlinear heat flows. The supremum two is over the star family, not all finite graphs or trees. The source comparison does not establish bibliographic uniqueness, and the contribution is quantitative rather than a new abstract semigroup framework.

## References
1. F. Bauer, P. Horn, Y. Lin, G. Lippner, D. Mangoubi, S.-T. Yau, *Li-Yau inequality on graphs*, arXiv:1306.2561, public version 11 June 2013, https://arxiv.org/abs/1306.2561.
2. F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875, public version 4 December 2017, https://arxiv.org/abs/1712.00875. See especially Theorem 3.8.
