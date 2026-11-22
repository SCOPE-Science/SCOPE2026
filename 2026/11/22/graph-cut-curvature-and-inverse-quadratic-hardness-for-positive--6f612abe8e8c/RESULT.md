# Graph-cut curvature and inverse-quadratic hardness for positive stochastic quadratics

## Finding

Let \(G\) be any undirected simple cubic graph with an even number \(n\ge4\) of vertices and adjacency matrix \(A_G\). Define
\[
 W_G=\frac34\left(I-\frac1{12}A_G\right)^{-1},\qquad
 \theta=\frac1{100n},\qquad
 K_G=(1-\theta)W_G+\frac\theta n\mathbf 1\mathbf1^{\mathsf T}.
\]
For any real symmetric positive-definite \(K\), its sharp \(\ell_1\)-strong-convexity modulus is
\[
 \mu_1(K)=\inf_{x\ne0}\frac{x^{\mathsf T}Kx}{\|x\|_1^2}
 =\inf_{x\ne0}\frac{\|Kx\|_\infty^2}{x^{\mathsf T}Kx}.
\]
Write \(c_G\) for the maximum number of edges in a cut of \(G\). Among all maximum cuts, let \(b_G\) be the smallest possible absolute difference between the numbers of vertices in the two parts. Then the **exact** law is
\[
 \boxed{\displaystyle
 \mu_1(K_G)^{-1}=\frac{n+\tfrac49c_G-\tfrac\theta n b_G^2}{1-\theta}.}
\]
The matrix \(K_G\) is rational, strictly entrywise positive, symmetric, doubly stochastic, and positive definite, and its spectral condition number is less than \(17/10\), independent of graph size. Nevertheless, approximating \(\mu_1(K_G)\) to absolute error at most \(1/(100n^2)\), given the rational matrix, is NP-hard (by a polynomial-time reduction from cubic-graph MAX CUT). This is hardness of **sharp rate-parameter evaluation**, not of carrying out one coordinate update.

For each optimal cut encoded by a sign vector \(s\in\{-1,1\}^n\) with \(\left|\sum_i s_i\right|=b_G\), the vector \(x=K_G^{-1}s/(s^{\mathsf T}K_G^{-1}s)\) is a norm-one minimizer of the first variational expression above. Conversely, every minimizer arises in this way up to a nonzero scalar. Thus the worst-case gradient signs precisely encode the most balanced maximum cuts.

## Assumptions and scope

The graph is simple and 3-regular; connectivity is not required. The matrix is built by exact rational inversion from the adjacency matrix, and the standard real \(\ell_1\) and \(\ell_\infty\) norms are used. All statements are for arbitrary even \(n\ge4\) for which a cubic graph exists. In the quadratic \(f(x)=x^{\mathsf T}K_Gx/2\), \(\mu_1\) is the exact sharp dual-gradient/error ratio used in the Gauss–Southwell bound. It is not the actual rate along every nonlinear greedy trajectory, nor the optimum of coordinate-dependent exact-line-search rules.

## Proof

**1. Stochasticity, positivity and conditioning.** Since \(G\) is cubic, \(A_G\mathbf1=3\mathbf1\), and its symmetric eigenvalues belong to \([-3,3]\). Hence \(B=I-A_G/12\) has eigenvalues in \([3/4,5/4]\) and \(W_G=(3/4)B^{-1}\) has eigenvalues in \([3/5,1]\). Moreover \(W_G\mathbf1=\mathbf1\). The Neumann series \(B^{-1}=\sum_{k\ge0}(A_G/12)^k\) is entrywise nonnegative; therefore every entry of \(K_G\) is at least \(\theta/n=1/(100n^2)>0\). By splitting the constant-vector eigenspace from its orthogonal complement, \(K_G\) has eigenvalue one on constants and eigenvalues in \([(1-\theta)3/5,1-\theta]\) otherwise. Thus \(\kappa_2(K_G)\le5/[3(1-\theta)]<17/10\). Rational inversion has polynomial bit complexity for these rational inputs.

**2. Exact dual curvature.** For any SPD \(K\), writing \(y=Kx\),
\[
 \inf_{x\ne0}\frac{\|Kx\|_\infty^2}{x^{\mathsf T}Kx}
 =\left(\max_{\|y\|_\infty\le1}y^{\mathsf T}K^{-1}y\right)^{-1}.
\]
The maximum of this strictly convex quadratic over the cube is attained only at sign vertices. The same reciprocal equals \(\inf_{x\ne0}x^{\mathsf T}Kx/\|x\|_1^2\) by \(\ell_1/\ell_\infty\) duality and Cauchy–Schwarz in the \(K\)-metric. Therefore
\[
 \mu_1(K)^{-1}=\max_{s\in\{-1,1\}^n}s^{\mathsf T}K^{-1}s.
\]

**3. Cut identity.** The stochasticity of \(W_G\) gives
\[
 K_G^{-1}=\frac1{1-\theta}\left(\frac43I-\frac19A_G-\frac\theta n\mathbf1\mathbf1^{\mathsf T}\right).
\]
Let \(c(s)\) be the number of graph edges with opposite endpoint signs, and \(b(s)=|\sum_i s_i|\). Since the cubic graph has \(3n/2\) edges, \(s^{\mathsf T}A_Gs=3n-4c(s)\). Consequently
\[
 s^{\mathsf T}K_G^{-1}s
 =\frac{n+\tfrac49c(s)-\tfrac\theta n b(s)^2}{1-\theta}.
\]
An increase by one cut edge gains \(4/9\) in the bracket, while the entire imbalance penalty lies in \([0,\theta n]=[0,1/100]\). Hence every maximizing sign vector is a maximum cut, and among such cuts the maximizing signs minimize \(b(s)\). The boxed formula follows.

**4. Exact extremizers.** For every sign vector \(s\), each coordinate of \(K_G^{-1}s\) has the same sign as \(s\), because its sign-adjusted numerator is at least \(4/3-3/9-\theta=1-\theta>0\). For a maximizing \(s\), put \(M=s^{\mathsf T}K_G^{-1}s\). Then \(\|K_G^{-1}s\|_1=M\), and \(x=K_G^{-1}s/M\) has \(\|x\|_1=1\) and \(x^{\mathsf T}K_Gx=1/M\). Conversely, equality in the strictly convex cube maximum forces the gradient direction to be a maximizing sign vertex, giving the stated characterization.

**5. Robust recovery of MAX CUT.** Given a cubic graph, the displayed construction computes a rational \(K_G\) in polynomial time. Put \(M=1/\mu_1(K_G)\). Then
\[
 R=\frac94\bigl((1-\theta)M-n\bigr)
 =c_G-\frac{9\theta}{4n}b_G^2,
 \qquad |R-c_G|\le\frac9{400}.
\]
Since \(c_G\le3n/2\), \(M\le 5n/[3(1-\theta)]<17n/10\). If a reported \(\widehat\mu\) differs from \(\mu_1\) by at most \(1/(100n^2)\), the reciprocal changes by less than \(0.03\), by \(|1/\widehat\mu-1/\mu_1|\le\eta M^2/(1-\eta M)\) with \(\eta=1/(100n^2)\). Therefore the corresponding approximate \(R\) differs from the integer \(c_G\) by less than \(9/400+(9/4)(0.03)<0.1\), and rounding recovers \(c_G\) exactly. MAX CUT is NP-hard on cubic graphs by the published APX-hardness theorem of Alimonti and Kann, so the advertised additive-approximation problem is NP-hard. No claim that \(\mathrm P\ne\mathrm{NP}\) has been proved is needed: the hardness assertion is an ordinary many-one/Turing reduction under standard complexity definitions.

## Verification

Run `python3 VERIFY.py`, using only the Python standard library. Exact rational Gauss–Jordan inversion checks the matrix identity, positivity, row sums, sign-vector cut identity, optimizing cut balance, curvature value and extremizing sign conditions for four natural cubic graphs: the tetrahedron, the six-vertex complete bipartite graph, the triangular prism and the eight-vertex cube. Their respective pairs \((c_G,\mu_1)\) are \((4,3591/20800)\), \((9,599/6000)\), \((7,1797/16400)\) and \((12,2397/32000)\). These finite checks are not a proof of the general reduction or NP-hardness; those follow from the analytical steps above and the cited cubic MAX CUT theorem.

## Relationship to prior work

Nutini et al. (2015, §§3–4) establish the significance of the sharp \(\ell_1\) curvature in Gauss–Southwell convergence estimates and explicitly calculate it for diagonal quadratic Hessians. Their theorem is not itself a MAX CUT representation on strictly positive, well-conditioned stochastic Hessians. Alimonti and Kann (2000, §4) prove cubic MAX CUT APX-hardness, which supplies the graph-theoretic hardness input, not the present stochastic-matrix representation. Bodlaender et al. (1990) and Hendrickx–Olshevsky (2010) establish broader complexity phenomena for hypercube quadratic maximization and matrix norms; the general hardness statements alone do not assert the strictly positive, doubly stochastic, condition-bounded inverse-resolvent restriction proved here. The exact source-level overlap risk is discussed in `REVIEW.md`.

## Limitations

The constant \(1/(100n^2)\) is an additive precision threshold, not a constant relative inapproximability factor. The theorem does not establish hardness of one Gauss–Southwell step, of spectral condition-number computation, or of optimization over arbitrary positive matrices. The matrices are dense but polynomially representable rational matrices. A potentially overlapping 1990 full-text argument could not be completely inspected; independent priority verification remains necessary.

## References

1. J. Nutini, M. Schmidt, I. Laradji, M. Friedlander and H. Koepke, *Coordinate Descent Converges Faster with the Gauss–Southwell Rule than Random Selection*, ICML/PMLR 37 (2015), 1632–1641. https://proceedings.mlr.press/v37/nutini15.html
2. P. Alimonti and V. Kann, *Some APX-completeness results for cubic graphs*, Theoretical Computer Science 237 (2000), 123–134. https://doi.org/10.1016/S0304-3975(98)00158-3
3. H. Bodlaender, P. Gritzmann, V. Klee and J. van Leeuwen, *Computational complexity of norm-maximization*, Combinatorica 10 (1990), 203–225. https://doi.org/10.1007/BF02123011
4. J. Hendrickx and A. Olshevsky, *Matrix p-norms are NP-hard to approximate if p differs from 1, 2, infinity*, SIAM J. Matrix Anal. Appl. 31 (2010), 2802–2812. https://doi.org/10.1137/09076773X
