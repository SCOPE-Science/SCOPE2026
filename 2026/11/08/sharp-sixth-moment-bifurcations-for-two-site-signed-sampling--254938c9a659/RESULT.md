# Sharp sixth-moment bifurcations for two-site signed sampling

## Finding
Fix any integer \(n\ge2\). Choose an unordered pair \(\{I,J\}\) uniformly among the \(\binom n2\) pairs of distinct indices, independently choose fair signs \(\varepsilon,\delta\in\{-1,1\}\), and let
\[
F_a=\varepsilon a_I+\delta a_J,\qquad a\in\mathbb R^n\setminus\{0\}.
\]
The exact attained range of the normalized sixth moment \(K_n(a)=\mathbb E F_a^6/(\mathbb E F_a^2)^3\) is the interval with endpoints
\[
K_{\min}(n)=\begin{cases}n^2/4,&n=2,3,\\4,&n\ge4,\end{cases}\qquad
K_{\max}(n)=\begin{cases}n^2(n+14)/[16(n-1)],&2\le n\le5,\\n^2/4,&n\ge6.\end{cases}
\]
All equality families are determined up to coordinate permutation, arbitrary coordinate signs, and a common nonzero scalar:

* At the minimum, exactly one coefficient is nonzero when \(n=2,3\); when \(n=4\), either exactly one is nonzero or all four have equal nonzero magnitudes; when \(n\ge5\), all \(n\) coefficients have equal nonzero magnitudes.
* At the maximum, exactly two coefficients have the same nonzero magnitude for \(2\le n\le5\); at \(n=6\), **every** nonzero coefficient vector with support of size at most two, and no other vector, maximizes; for \(n\ge7\), precisely single-coordinate vectors maximize.

For the \(n\)-dimensional real function space \(X_n=\{F_a:a\in\mathbb R^n\}\) with norm \(N_n(a)=(\mathbb E|F_a|^6)^{1/6}\), the Euclidean Banach--Mazur distance is exactly
\[
d_{\mathrm{BM}}(X_n,\ell_2^n(\mathbb R))^6=
\begin{cases}
4,&n=2,\\17/8,&n=3,\\3/2,&n=4,\\475/256,&n=5,\\n^2/16,&n\ge6.
\end{cases}
\]
No nonsymmetric Euclidean comparison norm improves this value.

## Assumptions and scope
The sample always has **exactly two** distinct occupied coordinates, each with an independent fair sign. Coefficients are real, the base probability is uniform over unordered pairs and signs, and \(n\) is any integer at least two. There is no assumption that the resulting coordinate random variables are independent; their nonzero indicators are negatively dependent. All expectations are with respect to this discrete probability. The classification is for the sixth and second moments of linear statistics, not higher-degree polynomials or other exponents.

## Proof
**1. Exact moment reduction.** Write \(S_j=\sum_{i=1}^n a_i^j\) for \(j=2,4,6\). Averaging over both signs for each pair, then over the \(\binom n2\) pairs, gives
\[
\mathbb EF_a^2=\frac2n S_2,
\qquad
\mathbb EF_a^6=\frac{2}{n(n-1)}\bigl(15 S_2S_4+(n-16)S_6\bigr).
\]
Indeed, for distinct \(i,j\), sign averaging of \((\varepsilon a_i+\delta a_j)^6\) yields \(a_i^6+a_j^6+15(a_i^4a_j^2+a_i^2a_j^4)\). Define the nonnegative normalized squares \(x_i=a_i^2/S_2\), so \(\sum_i x_i=1\). Then exactly
\[
K_n(a)=\frac{n^2}{4(n-1)}\Phi_n(x),
\quad\Phi_n(x)=15\sum_i x_i^2-(16-n)\sum_i x_i^3.
\]
The optimization therefore concerns a polynomial on the **entire closed probability simplex**.

**2. Pair-smoothing lemma.** Put \(c=16-n\). For two coordinates \(u,v\ge0\), with sum \(s=u+v\) and product \(p=uv\), their contribution to \(\Phi_n\) is **exactly**
\[
15(u^2+v^2)-c(u^3+v^3)
=15s^2-cs^3+3(cs-10)p.
\]
At fixed sum, the allowed product ranges from zero to \(s^2/4\), with endpoints at \((s,0)\) and \((s/2,s/2)\). Thus whenever \(cs<10\), strictly averaging two unequal positive coordinates decreases \(\Phi_n\), while merging them increases it. Whenever \(cs>10\), the reverse holds. When \(cs=10\), the contribution is independent of the split. These statements remain true when \(c\le0\).

**3. Maximum and its equality cases.** Suppose a global maximum has at least three positive coordinates. The two smallest then have sum at most \(2/3\); since \(c\le14\) for \(n\ge2\), \(c(2/3)\le28/3<10\). Merging those two strictly raises \(\Phi_n\), a contradiction. Therefore every maximizer has support of size at most two. On support at most two, let \(p=x_1x_2\), with \(0\le p\le1/4\). The preceding identity reduces to
\[
\Phi_n=n-1+3(6-n)p.
\]
For \(n=2,3,4,5\), the unique maximizing product is \(p=1/4\), forcing equal magnitudes. For \(n=6\), every \(p\) attains the same maximum. For \(n\ge7\), only \(p=0\) maximizes, forcing a single nonzero coefficient. Substitution gives the displayed maximum.

**4. Minimum and its equality cases.** When \(n\ge6\), \(c\le10\). Any pair of positive coordinates in a vector of support at least three has \(s<1\), hence \(cs<10\); averaging unequal ones strictly lowers \(\Phi_n\). Likewise, any positive coordinate paired with a zero may be split to lower \(\Phi_n\) (the only edge case is a single-coordinate vector at \(n=6\), whose value is \(5\), greater than the all-equal value \(20/9\)). Thus the unique minimum for \(n\ge6\) has \(x_i=1/n\) for all indices. Its polynomial value is \(16(n-1)/n^2\).

For \(n=3,4,5\), one has \(10<c\le13\). A minimum with exactly two positive coordinates is impossible: their sum is one, so merging reduces \(\Phi_n\). A minimum with at least three positive coordinates has **all of them equal**, as follows. Any positive pair with sum greater than \(10/c\) can be merged to lower the value; any positive pair with sum less than \(10/c\) must be equal. Suppose an unequal positive pair \(u>v\) has sum exactly \(10/c\) and there is a third positive coordinate \(w\). The pair \((u,w)\) cannot have sum above \(10/c\); if its sum is below \(10/c\), minimality forces \(u=w\), which makes its sum greater than \(u+v\), also impossible. Hence \(u+w=10/c\), so \(w=v\). Now perturb \((u,v)\) to \((u-\eta,v+\eta)\) for sufficiently small \(\eta>0\). The pair-smoothing identity says this leaves the objective unchanged, so the perturbed vector would also minimize. But the pair \((v+\eta,w=v)\) has sum strictly less than \(10/c\) and unequal positive entries, permitting a strict decrease. Contradiction. Therefore a minimum supported on at least three coordinates is uniform on its support.

For \(n=2\) the two-coordinate identity immediately yields the minimum at a vertex. For \(n=3,4,5\) it remains only to compare the vertex with the uniform-on-\(s\)-coordinates candidates, whose values are \(15/s-(16-n)/s^2\) for \(3\le s\le n\). At \(n=3\), the vertex gives \(2\), less than \(32/9\); at \(n=4\), the vertex and fully uniform vector both give \(3\), while the three-coordinate candidate gives \(11/3\); at \(n=5\), full uniformity gives \(64/25\), less than the vertex \(4\), the three-coordinate value \(34/9\), and the four-coordinate value \(49/16\). These strict comparisons give every asserted minimizing equality class.

**5. Entire interval and Euclidean distortion.** The normalized sixth-moment quotient is continuous on the connected Euclidean unit sphere (because \(\mathbb E F_a^2=2\|a\|_2^2/n>0\)). Hence it takes every value between its attained extrema. The law of \((I,J,\varepsilon,\delta)\) is invariant under signed coordinate permutations of \(a\). If a Euclidean quadratic form \(Q\) gives a two-sided comparison \(\alpha^2 Q(a)\le N_n(a)^2\le\beta^2 Q(a)\), then averaging all the inequalities under signed coordinate permutations yields the **same** distortion ratio \(\beta/\alpha\) for the positive scalar form \(\overline Q(a)=t\|a\|_2^2\). Thus \(\ell_2\) is an optimal Euclidean comparator. Its comparison radius is \(K_{\max}^{1/6}/K_{\min}^{1/6}\), because the second moment is a fixed multiple of \(\|a\|_2^2\). Substitution gives the displayed exact Banach--Mazur distances.

## Verification
Run `python3 verify_sparse_pairs.py` with Python 3.8 or later; only its standard library is required. The independent checker enumerates pairs and four sign assignments and computes moments in exact rational arithmetic on 420 seeded rational inputs. It also checks exact endpoint witnesses for all dimensions 2 through 100, the pair-smoothing polynomial identity on additional rational inputs, and the distortion formula. The checker does not certify the global optimization for infinitely many dimensions; that step is the foregoing analytic argument.

## Relationship to prior work
The exact-two-site model is the smallest nontrivial fixed-support signed-sampling model. Kane and Nelson's *Sparser Johnson--Lindenstrauss Transforms* (arXiv:1012.1577, initially posted 2010-12-07), Section 1.1, uses independent random signs with fixed-cardinality, without-replacement placement indicators in sparse embeddings, but studies dimensionality-reduction guarantees and high-moment bounds, not the present sharp sixth-moment norm or equality classification. Pass and Spektor's *On Khinchine type inequalities for pairwise independent Rademacher random variables* (arXiv:1412.7859, initially posted 2014-12-25), Theorem 2.1 and Corollary 2.4, optimize laws supported on fully signed vectors with pairwise-independent \(\{\pm1\}\)-marginals; those assumptions are incompatible with the present zero-containing, exactly-two-active random vector. Havrilla and Tkocz's *Sharp Khinchin-type inequalities for symmetric discrete uniform random variables* (arXiv:1912.13345, initially posted 2019-12-31), Section 2, treats i.i.d. three-point and other discrete marginals; in contrast, the nonzero indicators here have a fixed sum and cannot be independent when \(n>2\). These results and related published exact-moment norm classifications do not state the dimension-three/four minimum geometry, dimension-six maximizing plateau, or this exact distortion formula.

## Limitations
The result is restricted to real coefficients, exactly two distinct active sites, uniform sampling without replacement, independent unbiased signs, and exponent six. It does not assert the corresponding sharp classification for an arbitrary fixed number of active sites, independent Bernoulli sparsification, biased sampling, or general exponents. The primary-source comparison covers inspected accessible literature and semantic searches; absence of an indexed match does not establish bibliographic uniqueness, and an equivalent formulation in a different literature remains possible. No independent mathematical audit is claimed.

## References
1. D. M. Kane and J. Nelson, *Sparser Johnson--Lindenstrauss Transforms*, arXiv:1012.1577, first posted 2010-12-07; https://arxiv.org/html/1012.1577v6 .
2. B. Pass and S. Spektor, *On Khinchine type inequalities for pairwise independent Rademacher random variables*, arXiv:1412.7859, first posted 2014-12-25; https://arxiv.org/abs/1412.7859 .
3. A. Havrilla and T. Tkocz, *Sharp Khinchin-type inequalities for symmetric discrete uniform random variables*, arXiv:1912.13345, first posted 2019-12-31; https://arxiv.org/abs/1912.13345 .
4. A. Eskenazis, P. Nayar and T. Tkocz, *Distributional stability of the Szarek and Ball inequalities*, *Mathematische Annalen*, published online 2023-07-15; https://doi.org/10.1007/s00208-023-02669-9 .
