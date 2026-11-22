# Finite-jet reconstruction of complete multipartite Henson type spectra and the sharp tripartite threshold

## Finding
Let \(r\ge2\) and let \(A=K_{a_1,\ldots,a_r}\), with all \(a_i\) positive integers, be an induced finite complete \(r\)-partite graph whose vertices are named individually inside the countable homogeneous \(K_{r+1}\)-free graph. Put \(n=\sum_i a_i\). Let \(P_A(z)=\sum_{j=0}^n c_jz^j\) count complete nonalgebraic singleton types by their number of adjacent named parameters.

**Uniform bounded-jet reconstruction theorem.** For every \(r\ge2\), the coefficients \(c_0,c_1,\ldots,c_{3r-2}\) uniquely determine the unordered shore-size multiset \(\{a_1,\ldots,a_r\}\), without any advance knowledge of \(n\). An exact rational reconstruction algorithm uses even power sums and Newton identities. Thus the amount of grade information needed is bounded independently of the parameter size \(n\).

**Sharp tripartite theorem.** For \(r=3\), the coefficient at grade one together with the coefficients at grades three and five suffices; grade four is redundant. Grading only through degree four is insufficient, and the first collision at fixed total size occurs at \(n=13\): the nonisomorphic graphs \(K_{1,6,6}\) and \(K_{2,2,9}\) have identical coefficient prefixes \(c_0,\ldots,c_4\), but their grade-five counts are \(822\) and \(798\), respectively. This is the unique colliding unordered pair at total size thirteen. The same witnesses, padded by \(r-3\) singleton shores, show that for every \(r\ge3\), the prefix through grade \(r+1\) is insufficient: the first difference occurs at grade \(r+2\), with magnitude \(24\).

The underlying type polynomial
\[
P_A(z)=(1+z)^n-\prod_{i=1}^{r}\bigl((1+z)^{a_i}-1\bigr)
\]
is standard from the known Henson one-point-neighborhood criterion and is **not** claimed as a new identity. The contributions here are the bounded-grade inverse theorem, the explicit tripartite inversion, the first collision cutoff, and the uniform lower-bound witnesses.

## Assumptions and scope
All graphs are simple, undirected, and loopless. The finite parameter base \(A\) has exactly \(r\ge2\) nonempty independent shores and every edge between distinct shores. The ambient structure is the countable Fraïssé limit of finite \(K_{r+1}\)-free graphs; all old vertices are named separately. A type is complete over these parameters and is nonalgebraic, so it is not realized by an old parameter. Grade is the number of named neighbors, not tuple arity or the number of algebraic types. All assertions quantify over every positive integral shore-size vector, with unbounded total size. The integer \(r\) is specified by the ambient forbidden-clique rank. No result about arbitrary \(K_{r+1}\)-free bases is asserted.

## Proof
**1. Exact type/graph correspondence (prior).** A new vertex with named neighborhood \(S\subseteq A\) is admissible exactly if \(A[S]\) contains no \(K_r\). Indeed, a \(K_r\) in \(S\) creates a forbidden \(K_{r+1}\) together with the new vertex; conversely the new extension has no forbidden clique otherwise, hence is realized by universality, and homogeneity identifies diagrams precisely with complete types. In a complete \(r\)-partite graph, \(S\) contains \(K_r\) exactly when it intersects every shore. The generating polynomial for all subsets is \((1+z)^n\); that for subsets meeting every shore is \(\prod_i((1+z)^{a_i}-1)\). Subtraction proves the displayed identity. Define
\[
Q(z)=(1+z)^n-P_A(z)=\prod_{i=1}^{r}\bigl((1+z)^{a_i}-1\bigr)=\sum_{j\ge r}q_jz^j.
\]
Since \(r\ge2\), \(c_1=n\), and for every \(j\) the value \(q_j=\binom nj-c_j\) is determined by the type coefficients. In particular
\[
q_r=\prod_{i=1}^{r}a_i>0,\qquad q_{r+1}=\tfrac12q_r(n-r).
\]

**2. Reconstruction from finitely many grades.** Work in exact formal power series over the rationals, setting \(z=e^t-1\). For \(g=q_r\), the identity \(e^{at}-1=at\,e^{at/2}\,\sinh(at/2)/(at/2)\) gives
\[
\frac{Q(e^t-1)}{gt^r}=e^{nt/2}\prod_{i=1}^r\frac{\sinh(a_it/2)}{a_it/2}.
\]
The power series has constant term one, so its formal logarithm is well-defined. Using the standard Bernoulli expansion, with the rational Bernoulli numbers defined by \(t/(e^t-1)=\sum_{j\ge0}B_jt^j/j!\), yields
\[
\log\frac{Q(e^t-1)}{gt^r}=\frac n2t+\sum_{j\ge1}\frac{B_{2j}}{2j(2j)!}\Bigl(\sum_{i=1}^r a_i^{2j}\Bigr)t^{2j}.
\]
Here every nonzero even Bernoulli number \(B_{2j}\) is nonzero, so the coefficient of \(t^{2j}\) recovers \(s_j=\sum_i(a_i^2)^j\) exactly. Importantly, the coefficient of \(t^{2j}\) on the left depends only on \(q_r,\ldots,q_{r+2j}\): higher terms of \(Q\) cannot affect it. Hence the known grade prefix through \(3r-2\) yields \(s_1,\ldots,s_{r-1}\), i.e. the first \(r-1\) power sums of the squared shore sizes.

Newton identities successively determine the elementary symmetric functions \(e_1,\ldots,e_{r-1}\) of the positive numbers \(a_i^2\) from these power sums, while the missing final symmetric function is already
\[
e_r=\prod_{i=1}^r a_i^2=q_r^2.
\]
Thus all coefficients of the monic polynomial
\[
R(X)=X^r-e_1X^{r-1}+e_2X^{r-2}-\cdots+(-1)^re_r=\prod_{i=1}^r(X-a_i^2)
\]
are fixed. Its multiset of positive roots is the squared shore-size multiset, and taking positive square roots uniquely recovers all \(a_i\). This proves the all-rank reconstruction bound. The inversion uses exact rational arithmetic; it is not an asymptotic approximation or a numerical root-recovery assertion.

**3. A sharper tripartite inversion.** When \(r=3\), denote \(a_1,a_2,a_3\) by \(a,b,c\), put \(g=abc\), and let \(e_2=ab+ac+bc\). Extracting the next two product coefficients gives
\[
q_3=g,\qquad q_4=\frac{g(n-3)}2,\qquad q_5=\frac g{12}(2n^2-12n-e_2+21).
\]
To check the third formula directly, set \(u_i=a_i-1\). After dividing \(Q(z)\) by \(gz^3\), each factor begins \(1+u_i z/2+u_i(u_i-1)z^2/6\). The quadratic coefficient equals \(\sum_i u_i(u_i-1)/6+\sum_{i<j}u_iu_j/4\), which simplifies to the displayed expression using \(\sum_i a_i=n\) and \(\sum_{i<j}a_ia_j=e_2\). Hence
\[
e_2=2n^2-12n+21-\frac{12q_5}{g}.
\]
The triple of shore sizes is exactly the positive-integer root multiset of \(X^3-nX^2+e_2X-g\). Here \(n=c_1\), \(g=\binom n3-c_3\), and \(q_5=\binom n5-c_5\), so only grades one, three and five are needed. No separate size input or grade-four input is necessary.

**4. Sharpness in degree four and first size.** Because the complete tripartite product \(Q\) has no coefficients below grade three, and the grade-four coefficient depends only on \(n\) and \(g\), two tripartite profiles of the same size have identical coefficients through degree four if and only if their products agree. The vectors \((1,6,6)\) and \((2,2,9)\) both have sum \(13\) and product \(36\), so they agree through grade four, with \(c_3=250\) and \(c_4=535\). But their values of \(e_2\) are \(48\) and \(40\); the preceding formula gives \(q_5=465\) and \(489\), and hence \(c_5=822\) and \(798\).

To establish *first* and *unique*, enumerate all nondecreasing triples \(1\le a\le b\le c\) with \(a+b+c=n\), for every \(3\le n\le13\). The included short exact program loops over \(1\le a\le\lfloor n/3\rfloor\), \(a\le b\le\lfloor(n-a)/2\rfloor\), and sets \(c=n-a-b\), so it visits every unordered triple exactly once and checks collisions of the pair \((n,abc)\). The run found no collision for \(n<13\) and the sole colliding pair above at \(n=13\). Because the finite search exhausts a precisely bounded set with explicit loop limits and integer operations, this proves the claimed finite first threshold, rather than extrapolating sampled values.

For general \(r\ge3\), append \(r-3\) shores of size one to each of the two witness triples. Each extra shore multiplies \(Q\) by exactly \(z\), so the two resulting \(Q\) polynomials agree through degree \(r+1\) and their first discrepancy is at degree \(r+2\), of absolute size \(24\). Their \(P\) polynomials therefore have the same grade prefix through \(r+1\) and differ at grade \(r+2\). This supplies a uniform lower bound without asserting that \(3r-2\) is optimal for all \(r\).

## Verification
The accompanying Python 3 file `verify.py` uses only the standard library. For all nondecreasing positive shore profiles with \(2\le r\le5\) and \(n\le12\), it independently enumerates all \(2^n\) vertex subsets and checks the forbidden transversal condition against the product polynomial; this makes 184 direct profiles. It then performs exact rational Stirling-transform, formal-logarithm, Bernoulli-coefficient and Newton-identity inversion for 1,465 profiles, including up to eight shores. It enumerates every unordered positive tripartite profile for \(3\le n\le39\), verifies the explicit coefficient formulas and first size-thirteen product collision, and checks padded collisions for all \(3\le r\le10\). The observed exact terminal line was:

`VERIFY_OK direct_profiles=184 reconstructed_profiles=1465 first_collision=13 witness_p3_p4=[250, 535] witness_p5=(822, 798)`

Finite checks support the constructive algebra and prove the explicitly finite first-collision statement. The unbounded uniform reconstruction is proved in Step 2 rather than inferred from tests. The checker never depends on a preexisting output file and has no nonstandard dependencies.

## Relationship to prior work
Henson's homogeneous forbidden-clique structures and Herwig's extension-property analysis provide the ambient setting. Conant analyzes model-theoretic types, forking and dividing in these structures. The published published-finding corpus result *Exact finite-parameter 1-type counting in Henson graphs is #P-complete* already proves the general identification between one-point types and forbidden-clique-free induced subsets. For the complete multipartite bases here, the displayed product polynomial follows directly and is expressly credited as prior. The published work on ordered pair types over maximal multipartite parameters also contains this ungraded unary count as a preliminary; it does not reconstruct shores from a fixed number of graded unary coefficients. Previously recorded three-shore work on defective multipartite bases and on asymptotic tuple types similarly does not assert finite-jet recovery or the first low-degree collision.

The reconstruction result is mathematically equivalent to a truncated inverse problem for \(\prod_i((1+z)^{a_i}-1)\), or to recovering a multiset of positive integers from finitely many coefficients of an exponential product. Relevant published and mathematical-text searches using these aliases, even-moment inversion, Bernoulli series, first product collisions, and graph type spectra found no covering claim. This is a bounded best-knowledge novelty comparison, not a proof that unindexed or folklore results cannot exist.

## Limitations
The rank \(r\) and the restriction to exactly \(r\) nonempty complete multipartite shores are essential. The result does not reconstruct arbitrary finite bases or arbitrary induced \(K_r\)-free subset polynomials. The \(3r-2\) degree bound is sufficient, but general optimality is not claimed; the degree-five cutoff is sharp only for \(r=3\). The size-thirteen first-collision classification is exactly finite, not a description of all larger collisions. Historical-priority searches cannot rule out unindexed equivalent finite-jet results.

## References
1. B. Herwig, *Many \(\omega\)-categorical Structures Have the Small Index Property*, arXiv:math/9502206, publicly available 1995-02-14. https://arxiv.org/abs/math/9502206
2. G. Conant, *Forking and dividing in Henson graphs*, arXiv:1401.1570, first public 2014-01-08. https://arxiv.org/abs/1401.1570
3. *Exact finite-parameter 1-type counting in Henson graphs is #P-complete*, previously published mathematical result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-finite-parameter-1-type-counting-in-henson-graphs-is-p-com--7c84dde7c650/RESULT.md
4. *A collision law for two-types over maximal multipartite parameter graphs in Henson structures*, previously published mathematical result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-a-collision-law-for-two-types-over-maximal-multipartite-paramete--8c8e5c9b100b/RESULT.md
