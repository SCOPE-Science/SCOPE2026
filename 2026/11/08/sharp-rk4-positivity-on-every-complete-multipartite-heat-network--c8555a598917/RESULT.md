# Sharp RK4 positivity on every complete multipartite heat network

## Finding

Let \(G=K_{n_1,\ldots,n_r}\) be an unweighted, undirected complete multipartite graph with \(r\ge2\) nonempty parts of sizes \(n_i\ge1\), and put \(N=\sum_i n_i\). Consider the heat equation \(u'(t)=-Lu(t)\), with \(L\) the combinatorial Laplacian. Its classical fourth-order Runge–Kutta *end-step* is

\[
T_h=f(hL),\qquad f(x)=1-x+\frac{x^2}{2}-\frac{x^3}{6}+\frac{x^4}{24}.
\]

Let \(\beta=2.7852935634052816\ldots\) denote the unique positive root of

\[
\beta^3-4\beta^2+12\beta-24=0.
\]

**Theorem.** For every graph and every real \(h\ge0\) in this domain,

\[
\boxed{T_h\text{ is entrywise nonnegative}\quad\Longleftrightarrow\quad 0\le h\le\frac{\beta}{N}.}
\]

Exactly the same interval gives scalar absolute stability of RK4 on the nonpositive spectrum \(-\sigma(L)\). This sharp interval is independent of the sizes of the individual parts, even when the graph is highly irregular.

At the positive endpoint \(h=\beta/N\), all transitions between different parts vanish exactly. For every \(h>\beta/N\), *every* entry linking two distinct parts becomes negative. Meanwhile all diagonal entries remain strictly positive and all within-part off-diagonal entries remain strictly positive for every \(h>0\). These claims refer to the numerical end-step, not to individual Runge–Kutta stages.

## Assumptions and scope

The graph is simple, unweighted, undirected and has all edges between different parts and none within a part. The heat generator is \(-L\) with unit edge rates. Part sizes and the number of parts are arbitrary positive integers, subject to \(r\ge2\); hence \(N\ge2\). All statements concern exact arithmetic and all nonnegative initial vectors. Graphs with a single part have zero generator and are excluded. Repeated vertices at the same graph location are not assumed. The step \(h\) is nonnegative.

Entrywise nonnegativity is equivalent to positivity preservation of all nonnegative initial vectors. Because \(L\mathbf 1=0\), every \(T_h\) has row and column sums one; on the stated interval it is a stochastic matrix.

## Proof

Write \(J_m=\mathbf1_m\mathbf1_m^\mathsf T\) and define the mutually orthogonal projectors

\[
E_0=\frac{J_N}{N},\quad B=\operatorname{diag}_i\frac{J_{n_i}}{n_i},\quad E_N=B-E_0,\quad E_i=I_{n_i}-\frac{J_{n_i}}{n_i},
\]

where each \(E_i\) is extended by zero outside part \(i\). For singleton parts \(E_i=0\). On the constant space the Laplacian eigenvalue is zero, on block-constant zero-sum vectors it is \(N\), and on zero-sum vectors within part \(i\) it is \(d_i=N-n_i\). Thus

\[
L=NE_N+\sum_i d_iE_i,\qquad
T_h=E_0+f(Nh)E_N+\sum_i f(d_ih)E_i.
\]

If vertices \(u,v\) lie in different parts, the formula immediately yields

\[
(T_h)_{uv}=\frac{1-f(Nh)}{N}.
\]

For distinct vertices in the same part \(i\), put \(d=d_i\). A direct subtraction of the projector coefficients, followed by polynomial simplification, gives

\[
\begin{aligned}
(T_h)_{uv}&=\frac{1-f(Nh)}{N}+\frac{f(Nh)-f(dh)}{N-d}\\
&=\frac{dh^2}{24}\left[12-4(N+d)h+(N^2+Nd+d^2)h^2\right].
\end{aligned}
\]

The quadratic in square brackets has positive leading coefficient and discriminant

\[
16(N+d)^2-48(N^2+Nd+d^2)
=-32N^2-16Nd-32d^2<0.
\]

It is therefore strictly positive for every real \(h\), so all actual same-part off-diagonal entries are positive whenever \(h>0\). For a diagonal entry in part \(i\), the same algebraic off-diagonal expression plus \(f(d_ih)\) gives its value; this remains valid when the part is a singleton. For \(x>0\), Taylor's formula for \(e^{-x}\) gives

\[
f(x)=e^{-x}+\frac{e^{-\xi}x^5}{120}>0
\]

for some \(0<\xi<x\), while \(f(0)=1\). Consequently every diagonal is strictly positive for all \(h\ge0\).

The cross-part sign is governed by

\[
1-f(x)=\frac{x}{24}\left(24-12x+4x^2-x^3\right).
\]

The cubic \(g(x)=x^3-4x^2+12x-24\) has derivative \(g'(x)=3x^2-8x+12>0\) for every real \(x\) (its discriminant is negative), and \(g(0)<0\) while \(g(x)\to+\infty\). It therefore has precisely one positive zero \(\beta\). Hence \(1-f(x)\ge0\) on \([0,\infty)\) precisely for \(0\le x\le\beta\). Since the graph has at least two parts, a cross-part entry exists, and this condition is necessary and sufficient for every entry of \(T_h\) to be nonnegative. Substituting \(x=Nh\) proves the theorem, including the boundary assertions.

For the spectral comparison, the Laplacian eigenvalues are \(0\), \(N\) (multiplicity \(r-1\)) and \(d_i\) (multiplicity \(n_i-1\)); in particular all lie in \([0,N]\) and \(N\) is present. As \(f(x)>0\) for all \(x\ge0\), \(|f(x)|\le1\) is equivalent to \(f(x)\le1\), which for \(x\ge0\) holds exactly on \([0,\beta]\). Therefore spectral absolute stability is equivalent to \(h\le\beta/N\), just as positivity is.

Finally, forward Euler has update \(I-hL\), which is nonnegative precisely for \(h\le 1/\max_i d_i=1/(N-\min_i n_i)\). The ratio of the two sharp endpoints is \(\beta(1-\min_i n_i/N)\). Because the smallest of at least two parts has size at most \(N/2\), this ratio is at least \(\beta/2>1\), with equality for two equal-sized parts.

## Verification

The standalone script `verify.py` uses only Python's standard library and exact rational arithmetic. It reconstructs graph Laplacians directly for all integer partitions of \(N=2,\ldots,9\), compares the matrix-polynomial end-step with the independent projector-derived entry formulas for nine rational timestep choices, checks unit row sums and every entry's sign, checks the quadratic discriminant identity for all integer \(2\le N<300\) and \(1\le d<N\), and rationally brackets the unique threshold. Its execution reported `VERIFY_OK assertions=96054 numerical_domain=partitions_of_2_to_9 exact_fractions=True`. This is finite corroboration only; the all-dimension and all-step theorem follows from the preceding algebraic proof.

Run `python3 verify.py` from the extracted artifact directory. No third-party libraries, numerical root solver or external datasets are required.

## Relationship to prior work

Blanes, Iserles and Macnamara (arXiv:2102.08242, first public 2021-02-16) articulate positivity difficulties for high-order time integrators on graph-Laplacian systems and use classical RK4 as a numerical comparator. Their methods and graph examples do not give an if-and-only-if RK4 interval for every complete multipartite network. Horváth's 1998 and 2005 papers give broad Runge–Kutta positivity-radius and cone results; the 1998 discussion explicitly gives classical RK4 zero *universal* positivity radius. That statement does not rule out positive end-steps on a restricted concrete generator family, and neither paper supplies the present classification. Klee and Stamps (arXiv:2008.01669, §3.2, Proposition 6) derive the complete multipartite Laplacian characteristic polynomial, which supplies the **known** spectral structure but does not determine entrywise positivity of a fourth-order matrix polynomial. The spectrum is therefore not claimed novel.

The two-state complete graph case is an elementary specialization and is not claimed new. The contribution assessed here is the full arbitrary-partition connected complete multipartite family, including all sizes and arbitrary irregularity, and its exact equivalence between positivity and spectral stability. General graph spectral data alone do not establish entrywise nonnegativity of the numerical propagator.

## Limitations

The graph must be complete multipartite with all cross-part edges of equal unit weight. Nothing here claims the same threshold for arbitrary weighted graphs, incomplete multipartite networks, path or cycle graphs outside overlapping special cases, nonnormal generators, other Runge–Kutta polynomials or internal RK stages. Spectral absolute stability in general does **not** imply entrywise positivity; the equivalence is family-specific. The source comparison is evidence of a distinct statement rather than a proof of publication priority; unindexed specialized numerical-analysis literature is a residual risk. Independent external validation has not been performed.

## References

1. S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for ordinary differential equations*, arXiv:2102.08242 (first public February 16, 2021), https://arxiv.org/abs/2102.08242.
2. S. Klee and M. T. Stamps, *Eigenvalues of graph Laplacians via rank-one perturbations*, arXiv:2008.01669 (August 4, 2020), §3.2, https://arxiv.org/abs/2008.01669.
3. Z. Horváth, *Positivity of Runge–Kutta and diagonally split Runge–Kutta methods*, Applied Numerical Mathematics 28 (1998), 309–326, https://doi.org/10.1016/S0168-9274(98)00050-6.
4. Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, Applied Numerical Mathematics 53 (2005), 341–356 (online October 27, 2004), https://doi.org/10.1016/j.apnum.2004.08.026.
