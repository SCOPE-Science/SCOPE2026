# Three-scale collapse of path-length variance in strongly root-biased recursive trees

## Finding
For the independent-parent recursive tree with weights \(w_i=i^\alpha\), \(\alpha\in\mathbb R\), let \(T_n=\sum_{i=1}^nD_i\) be the total path length, where \(D_i\) is vertex depth from root \(1\). The known finite positive variance coefficient \(\sigma_\alpha^2=\lim_{n\to\infty}n^{-2}\operatorname{Var}(T_n)\) admits the sharp boundary expansion
\[\boxed{\sigma_\alpha^2=18^\alpha+32^\alpha-4\,36^\alpha+O(48^\alpha),\qquad \alpha\to-\infty.}\]
In particular, the leading decay rate is \(18^\alpha\), and the successive corrections are governed by the distinct exponential scales \(32^\alpha\) and \(36^\alpha\). The three terms identify contributions from the earliest nontrivial attachment innovations and their normalization.

## Assumptions and scope
The root is vertex \(1\). For every integer \(j\ge2\), independently of previous parent choices, vertex \(j\) chooses a parent \(i\in\{1,\ldots,j-1\}\) with probability \(i^\alpha/\sum_{k=1}^{j-1}k^\alpha\). The weights remain strictly positive for each fixed finite \(\alpha\). Set \(S_j=\sum_{k=1}^jk^\alpha\) and \(p_j=j^\alpha/S_j\). The finding concerns first taking \(n\to\infty\) at fixed \(\alpha\), then taking \(\alpha\to-\infty\). No simultaneous \(n\)-\(\alpha\) limit is asserted.

## Proof
The established independent-attachment innovation identity gives
\[\sigma_\alpha^2=\sum_{j=3}^{\infty}p_j^2v_j,\qquad v_2=0,\qquad v_{j+1}=(1-p_j^2)v_j+p_j(1-p_j).\]
Here \(v_j\) is the expected conditional variance of the depth of vertex \(j\) given the preceding tree. The cited original article proves convergence and this recurrence for the present positive weights; we evaluate its previously untreated strong-root-bias parameter boundary.

Write \(t=-\alpha\to+\infty\), \(a=2^{-t}\), \(b=3^{-t}\), \(c=4^{-t}\). The first nonzero variance is \(v_3=p_2(1-p_2)=a/(1+a)^2\), so its contribution is exactly
\[p_3^2v_3=\frac{ab^2}{(1+a)^2(1+a+b)^2}=18^{-t}-4\,36^{-t}+O(54^{-t}).\]
For the next vertex the recurrence gives \(v_4=(1-p_3^2)v_3+p_3(1-p_3)=a+O(b+a^2)\). Because \(p_4=c/(1+a+b+c)\),
\[p_4^2v_4=32^{-t}+O(48^{-t}).\]
It remains to bound **all** vertices \(j\ge5\). For \(t\ge2\), \(0<p_j\le j^{-t}\), and the recurrence implies \(0\le v_j\le\sum_{k=2}^{j-1}p_k\le\sum_{k=2}^\infty k^{-t}\le C2^{-t}\) for an absolute constant \(C\). Likewise \(\sum_{j=5}^\infty j^{-2t}\le C'5^{-2t}\). Hence
\[0\le\sum_{j=5}^\infty p_j^2v_j\le CC'50^{-t}.\]
Summing the three pieces and using \(50^{-t}=O(48^{-t})\) proves the stated expansion. All bounds are absolute for sufficiently large \(t\). Positivity and the exact order of the successive terms also prove the claimed ratio limits.

## Verification
The standalone program `verify_ultraold.py` enumerates complete parent-choice trees through six vertices with exact rational arithmetic at three negative integer exponents and matches the recurrence-based finite variance identically. It then evaluates the convergent coefficient numerically for seven exponents, checking the stated three-scale approximation against an explicit conservative multiple of \(48^\alpha\). There were ten successful assertions. This computational evidence is supplementary to the analytic remainder estimates above.

## Relationship to prior work
Gałązka and Wdowicka (2026), arXiv:2610.00614v1, prove the variance-coefficient series and the innovation recurrence, and explicitly list the dependence of the coefficient on the power-weight exponent as an open topic. Their paper evaluates the coefficient at \(\alpha=0\) and \(\alpha=1\), but does not give the strong root-preference asymptotic above. The present statement is **not** a new variance recurrence or a new path-length limit theorem: it supplies a resolved singular-parameter endpoint, with three distinct scales and an explicit uniform remainder. Classical uniform-recursive-tree work provides further background, not the same strongly nonuniform boundary.

## Limitations
The result treats the root-biased endpoint only. The displayed expansion has no assertion of monotonicity for finite \(\alpha\), no simultaneous parameter-size uniformity, and no corresponding positive-exponent asymptotic. Priority against an unlocated equivalent asymptotic in earlier studies of highly nonuniform recursive trees has not been independently established.

## References
Gałązka, M., and Wdowicka, H., *Total Path Length in Power-Weight Recursive Trees: Martingale Limits and Global Fluctuations*, arXiv:2610.00614v1, first public September 30, 2026. See the innovation recursion in Section 5, the variance limit in Section 6, and the parameter-asymptotics discussion in Section 10.

Dobrow, R. P., and Fill, J. A., *Total path length for random recursive trees*, Combinatorics, Probability and Computing 8 (1999), 317–333, doi:10.1017/S0963548399003855 (historical uniform-model background, not asserted to contain the new boundary expansion).
