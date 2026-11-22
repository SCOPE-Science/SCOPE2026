# Sharp one-input versus two-input variation thresholds for sliding four-point central spacings

## Finding
For an integer \(n\geq4\), define \(F_n:\mathbb R^n\to\mathbb R^{n-3}\) by
\[
 (F_n(x))_i=x_{(3);i:i+3}-x_{(2);i:i+3},\qquad 0\leq i\leq n-4,
\]
where the parenthesized subscripts mean the third and second smallest of the four consecutive numbers \(x_i,x_{i+1},x_{i+2},x_{i+3}\), including multiplicities. Let \(V(z)=\sum_{i=0}^{m-2}|z_{i+1}-z_i|\) for a real path \(z\) of length \(m\), with the empty sum equal to zero. The sharp, *attained* two-input sensitivity is
\[
 K_n=\sup_{V(x-y)>0}\frac{V(F_n(x)-F_n(y))}{V(x-y)}=
 \begin{cases}0&n=4,\\2&n=5,\\4&n=6,\\5&n=7,\\6&n\ge8.\end{cases}
\]
The separately sharp one-input coefficient is
\[
 B_n=\sup_{V(x)>0}\frac{V(F_n(x))}{V(x)}=
 \begin{cases}0&n=4,\\1&n=5,\\2&n\ge6.\end{cases}
\]
In particular, ordinary variation of each output is bounded by twice the input variation for every path length, yet an arbitrarily small perturbation can increase the variation of an output *difference* sixfold as soon as eight input sites are present.

## Assumptions and scope
The inputs are arbitrary finite real sequences on open paths, with no padding and full consecutive windows of exactly four observations. The filter is the difference between the two middle order statistics, not a specific convention for sample interquartile range. The Lipschitz coefficient is taken on the quotient modulo constants: adding a constant to either input translates its order statistics but does not change the central spacing. The nonlinearity is continuous and piecewise affine. The first comparison uses two independent signals; the second compares each filtered signal with its own input variation.

## Proof
**Two-input upper bound.** Write \(h^{(j)}=(\mathbf1_{\{k>j\}})_{k=0}^{n-1}\) for each edge index \(0\le j\le n-2\). On every strict-order chamber, the derivative of a window's central-spacing output with respect to the direction \(h^{(j)}\) is
\[
 a_i^{(j)}=\mathbf1_{\{r_3(i)>j\}}-\mathbf1_{\{r_2(i)>j\}},
\]
where \(r_2(i),r_3(i)\) are the original positions of its second- and third-ranked observations. Hence \(a_i^{(j)}\in\{-1,0,1\}\), and it vanishes unless the window contains sites on both sides of the edge \(j\). Such windows have start indices among \(j-2,j-1,j\). Thus the derivative output has at most three consecutive nonzero entries, with all others zero. With output length \(n-3\), the maximal possible variation is at most \(0,2,4,5,6\) respectively for \(n=4,5,6,7,n\ge8\). Specifically, for lengths 1, 2, 3 these are the immediate \(0,2,4\) bounds; for length 4, at most three consecutive entries can be nonzero and the exterior zero costs at most one, so the bound is 5; arbitrary longer outputs cost at most six over two exterior transitions and two interior transitions.

For any input increment \(h\), its exact representation
\[
 h=h_0\mathbf1+\sum_{j=0}^{n-2}(h_{j+1}-h_j)h^{(j)}
\]
and translation invariance of \(F_n\) give the bound for the derivative in the variation seminorm. Integrate over the line segment between any two inputs; finitely many rank changes do not affect the absolutely continuous path-integral estimate. This proves the claimed global upper bound even at ties.

**Two-input equality.** In the following table, each listed integer baseline \(x\) has distinct entries and \(y=x+\frac14h^{(j)}\); the strict ordering is unchanged. The derivative vector \(a^{(j)}\) is therefore the *exact* central-spacing difference divided by \(1/4\), while \(V(y-x)=1/4\):

| Input length | \(x\) | \(j\) | \(a^{(j)}\) | Variation |
| --- | --- | --- | --- | --- |
| 5 | \((0,2,1,3,4)\) | 1 | \((-1,1)\) | 2 |
| 6 | \((0,1,3,2,4,5)\) | 2 | \((1,-1,1)\) | 4 |
| 7 | \((0,1,3,2,4,5,6)\) | 2 | \((1,-1,1,0)\) | 5 |
| 8 | \((0,1,2,4,3,5,6,7)\) | 3 | \((0,1,-1,1,0)\) | 6 |

For every \(n>8\), append \(8,9,\ldots,n-1\) to the eight-input baseline and keep \(j=3\). No new window straddles that cut, so the same variation 6 is attained. For \(n=4\) there is a single output coordinate, whose variation vanishes.

**One-input upper bound via coarea.** For each threshold \(t\), let \(b_k(t)=\mathbf1_{\{x_k>t\}}\), and let \(G\) map a binary path to the binary sequence whose sliding four-bit windows contain *exactly two ones*. The elementary layer-cake identity
\[
 (F_n(x))_i=\int_{\mathbb R} \mathbf1_{\{\sum_{k=i}^{i+3}b_k(t)=2\}}\,dt
\]
follows because exactly two samples exceed the threshold precisely for \(t\) between the second and third order statistics. We prove \(V(G(b))\le2V(b)\) for every binary path by the finite potential certificate below.

For a four-bit state \(s\), set \(g(s)=\mathbf1_{\{\text{exactly two bits of }s\text{ equal one}\}}\), and define \(p\) by the following complete list:

```
0000 0   0001 2   0010 0   0011 1
0100 0   0101 1   0110 1   0111 0
1000 0   1001 1   1010 1   1011 0
1100 1   1101 0   1110 2   1111 0
```

For every state \(s=abcd\), direct substitution in the sixteen entries shows \(0\le p(s)\le2(|b-a|+|c-b|+|d-c|)\). For each choice of appended bit \(e\in\{0,1\}\), direct substitution in all 32 edges verifies
\[
 p(abcd)\ge |g(bcde)-g(abcd)|-2|e-d|+p(bcde).
\]
Summing along the successive windows telescopes and yields \(V(G(b))\le2V(b)\) at every length: the initial potential is bounded by the variation of the first four bits and the final potential is nonnegative. The triangle inequality for the integral and the discrete coarea identity
\[
 \int_{\mathbb R}V(b(t))\,dt=V(x)
\]
prove \(V(F_n(x))\le 2V(x)\) for all real inputs.

When \(n=5\), the two windows differ by replacing just \(x_0\) with \(x_4\). For fixed other three observations, the gap between second and third order statistics is a 1-Lipschitz function of the replacement observation: on each of the four intervals separated by the fixed observations it is affine with slope in \(\{-1,0,1\}\). Consequently \(V(F_5(x))\le|x_4-x_0|\le V(x)\). Length four is trivial. Finally, \(x=(0,0,0,1,1)\) attains the one-input coefficient 1 at length five; \(x=(0,0,0,1,1,\ldots,1)\) attains coefficient 2 at every length at least six. This proves both sharp classifications.

## Verification
The standalone `check.py` uses exact rational arithmetic to check all sixteen potential values and all 32 transition inequalities; enumerates every strict rank chamber through eight input sites; checks the finite attaining pairs and binary one-input witnesses through thirty sites; and runs 3,500 independent rational stress pairs. The finite enumeration is a cross-check, **not** a substitute for the general proof via chamber integration and the sixteen-state certificate. Running `python3 check.py` prints `FOUR_POINT_CENTRAL_SPACING_ALL_CHECKS_PASS` when all checks succeed.

## Relationship to prior work
Classical median and order-statistic filtering motivate using order information to suppress extremes and preserve edges. The 2009 analysis of order-statistics vector filters by Celebi and collaborators addresses minimax computational approximations, not exact path-variation Lipschitz constants of the scalar middle-two spacing. Little and Jones's 2010/2011 piecewise-constant signal analysis gives variation properties of running medians, which select a single order statistic, rather than the difference of two consecutive central order statistics. Related published results on running medians, trimmed means, and local median absolute deviation use distinct nonlinear maps and hence do not imply these paired exact constants. In particular, a one-input variation bound for this central spacing cannot determine its two-input bound: the two constants separate by a factor of three in long paths.

## Limitations
The bounds concern only the full four-site central-spacing map, with ordinary unweighted adjacent variation. No claim is made about larger windows, conventional sample quartile conventions, wraparound, sampling on graphs, or higher-dimensional signals. Literature searches cannot exclude every unindexed or inaccessible historical equivalent; this is a mathematical proof with a self-review and no independent audit.

## References
1. M. E. Celebi, H. A. Kingravi, R. Lukac and F. Celiker, "Cost-effective implementation of order-statistics-based vector filters using minimax approximations," *J. Opt. Soc. Am. A* 26 (2009), 1518–1524. DOI: 10.1364/JOSAA.26.001518; publicly posted 2009-04-16 and published 2009-05-29; accessible manuscript arXiv:1009.0959.
2. M. A. Little and N. S. Jones, "Generalized methods and solvers for noise removal from piecewise constant signals. I. Background theory," *Proc. R. Soc. A* 467 (2011), 3088–3114. DOI: 10.1098/rspa.2010.0671; preprint arXiv:1012.5095.
3. G. Nikitin, "Nonlinear signal processing systems and methods," US20110112784A1 (published 2011-05-12), for continuous-time rank/quantile-filter context rather than the discrete result above.
