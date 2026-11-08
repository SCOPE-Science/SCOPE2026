# Fibonacci factorization of driven sandpile avalanches on fan graphs

## Finding

Let \(n\ge 2\) and let \(F_n=K_1\vee P_n\) be the fan graph: its vertices are a sink \(s\) and a path \(1,2,\ldots,n\), with an edge from \(s\) to each path vertex. Consider the standard Abelian sandpile with one grain added at a fixed path site \(j\in\{1,\ldots,n\}\), beginning at a uniformly chosen recurrent stable configuration. Let \(T\) be the number of individual nonsink topplings and \(I\) the set of toppled sites. Define the Fibonacci sequence by \(f_0=0\), \(f_1=1\), and \(f_{k+2}=f_{k+1}+f_k\). Set

\[
 w(0)=1,\qquad w(m)=f_{2m}\quad(m\ge1).
\]

There are exactly \(f_{2n}\) recurrent configurations. Every nonempty avalanche support is a contiguous interval \(I=[L,R]\cap\mathbb Z\) with \(1\le L\le j\le R\le n\), and its **exact support law** is

\[
\boxed{\mathbb P_j(I=[L,R])=\frac{w(L-1)w(n-R)}{f_{2n}}.}
\]

The remaining mass is at the empty support:

\[
\boxed{\mathbb P_j(T=0)=1-\frac{f_{2j-1}f_{2(n-j)+1}}{f_{2n}}.}
\]

In particular, conditional on \(T>0\), the left reach \(j-L\) and right reach \(R-j\) are **exactly independent even at finite \(n\)**, with

\[
\mathbb P_j(j-L=\ell\mid T>0)=\frac{w(j-\ell-1)}{f_{2j-1}},\qquad 0\le\ell\le j-1,
\]
\[
\mathbb P_j(R-j=r\mid T>0)=\frac{w(n-j-r)}{f_{2(n-j)+1}},\qquad 0\le r\le n-j.
\]

This also gives the *complete multivariate principal avalanche polynomial*. With the empty product equal to \(1\), write \(\mathcal A_n(\mathbf x)=\sum_{c\in\operatorname{Rec}(F_n)}\sum_{j=1}^{n}\prod_{i\in I(c,j)}x_i\). Then

\[
\boxed{
\mathcal A_n(\mathbf x)
=\sum_{j=1}^n\left(f_{2n}-f_{2j-1}f_{2(n-j)+1}\right)
+\sum_{1\le L\le R\le n}(R-L+1)w(L-1)w(n-R)\prod_{i=L}^R x_i.
}
\]

For any sequence \(j=j_n\) such that \(j_n\to\infty\) and \(n-j_n\to\infty\), let \(\varphi=(1+\sqrt5)/2\). Then the bulk avalanche-size law has the exact limit

\[
\boxed{
\lim_{n\to\infty}\mathbb P_{j_n}(T=0)=1-\frac1{\sqrt5},\qquad
\lim_{n\to\infty}\mathbb P_{j_n}(T=t)=\frac{t}{\sqrt5}\varphi^{-2t}\quad(t\ge1).
}
\]

Conditional on a positive bulk avalanche, the two arm lengths converge jointly to independent geometric random variables on \(\{0,1,\ldots\}\), each with probability \(\varphi^{-1}(\varphi^{-2})^k\) at \(k\). Moreover, **at every finite size and every drive site** \(\mathbb E_j[T]=1\).

## Assumptions and scope

All edges are unweighted and undirected. The sink \(s\) never topples. At a path site \(i\), the threshold is its full graph degree, \(2\) at the two endpoints and \(3\) elsewhere. A legal toppling sends one grain to each neighbor, including one grain to the sink; the sink grain is lost. Initial configurations are stable and uniformly recurrent for this fixed sink. Each experiment adds exactly one grain at the specified site \(j\), followed by complete stabilization. The theorem applies to all integers \(n\ge2\), including endpoint drive. The infinite-volume statement assumes that the driven site recedes from both path endpoints; it does not claim a critical power-law tail.

## Proof

**1. Recurrence criterion.** A stable sandpile is recurrent if and only if it has no forbidden subconfiguration, i.e. no nonempty subset \(S\) of nonsink sites with every \(i\in S\) satisfying \(c_i<\deg_S(i)\). On a path, every component of a proposed forbidden set is an interval. A singleton is impossible because \(\deg_S(i)=0\) and \(c_i\ge0\). For an interval of length at least two, the two endpoints must have height \(0\), and every interior vertex must have height at most \(1\). Conversely, two zeros with no intervening height \(2\) define such a forbidden interval. Thus recurrence is equivalent to the word rule: **between any two zeros, at least one height \(2\) appears**. This criterion is also stated for fans in Austin et al., Proposition 43 (arXiv:1605.02713).

**2. Counting a fan segment.** The reduced Laplacian is tridiagonal with diagonal entries \(2,3,\ldots,3,2\) and adjacent off-diagonal entries \(-1\). Its determinant, hence the number of recurrent configurations by the matrix-tree theorem, is \(f_{2n}\). One direct check: determinants of path prefixes with first diagonal \(2\) and subsequent diagonal \(3\) satisfy \(D_0=1\), \(D_1=2\), \(D_k=3D_{k-1}-D_{k-2}\), so \(D_k=f_{2k+1}\); restoring the last diagonal \(2\) yields \(2f_{2n-1}-f_{2n-3}=f_{2n}\). For a tail of \(m\ge2\) path vertices, require its original path endpoint to have height at most \(1\), all other internal sites to have height at most \(2\), and the site touching a prescribed toppled interval to have height at most \(1\). The recurrence word rule identifies these exactly with recurrent words on a fan of length \(m\), giving \(f_{2m}=w(m)\) possibilities. For a one-site tail the only permitted height is \(0\), giving \(w(1)=1\); an empty tail has one choice, giving \(w(0)=1\).

**3. Identifying the avalanche.** Each path vertex topples at most once after a single grain addition: if one were the first vertex to topple a second time, it could have received at most one initial added grain plus one grain from each path neighbor. Its original stable height is at most its degree minus one, so after its first toppling its height would still be below its threshold, a contradiction. Thus only a single wave of topplings is possible. The driven site topples if and only if its initial height is maximal stable (height \(1\) at a path endpoint, or \(2\) internally). A toppling can propagate along the path only through successive sites of maximal stable height. A site outside this maximal-height run cannot be activated by both neighbors because the farther neighbor cannot topple before the intervening site. Consequently the toppled set is exactly the maximal consecutive run of maximal-height sites containing \(j\), or empty.

Fix \([L,R]\) containing \(j\). The heights inside the interval are uniquely fixed at their maximal stable values. If \(L>1\), the preceding site must have a nonmaximal height, and likewise if \(R<n\) for the following site. The two exterior tails are independently recurrent fan words as counted in Step 2. They cannot create a forbidden interval crossing the saturated run: if both tails are present the run contains an internal height \(2\); if it contains no such site, at most one tail is present. The number of recurrent initial configurations producing this support for a fixed \(j\) is therefore exactly \(w(L-1)w(n-R)\). Divide by \(f_{2n}\) to obtain the support law.

**4. Normalization and exact independence.** For every integer \(h\ge1\), the Fibonacci identity

\[
\sum_{m=0}^{h-1}w(m)=1+\sum_{m=1}^{h-1}f_{2m}=f_{2h-1}
\]

follows from the Fibonacci recurrence. Summing the factorized interval weights over \(1\le L\le j\le R\le n\) yields \(f_{2j-1}f_{2(n-j)+1}\). Subtraction from the total gives the empty-support probability, while division by this product gives independent left and right reaches. The multivariate polynomial follows by summing over the \(R-L+1\) possible drive positions inside each nonempty interval.

**5. Bulk limit and mean.** Binet's formula gives \(f_k=(\varphi^k-(-\varphi)^{-k})/\sqrt5\), where the second term equals the usual contribution from \((1-\sqrt5)/2\) after taking the appropriate integer power. For fixed \(\ell,r\ge0\) and a drive site far from both endpoints, the joint unconditioned probability of left and right reaches \((\ell,r)\) tends to \(\varphi^{-2(\ell+r+1)}/\sqrt5\). The probability of any nonempty avalanche tends to \(1/\sqrt5\); conditional reach probabilities tend to \(\varphi^{-1}(\varphi^{-2})^k\), independently. Summing the \(t\) ordered decompositions \(\ell+r=t-1\) gives the displayed bulk size law. Finally, adding a grain at one fixed site permutes the finite sandpile group, so the uniform recurrent law is invariant. Each toppling removes exactly one grain to the sink. Conservation of the expected number of nonsink grains before and after stabilization therefore gives \(\mathbb E_j[T]=1\) exactly.

## Verification

The included executable `check_exhaustive.py` determines recurrence by an independently implemented Dhar burning test, separately checks the zero-word criterion, and simulates legal topplings without imposing the proposed formula. For every \(2\le n\le9\), every possible stable state and every addition site are checked; this gives 35,044 recurrent-state/addition trials, verifying interval coefficients, no-toppling probabilities, counts and exact means. `check_identities.py` separately tests the tridiagonal determinant, Fibonacci normalization, factorization and activity identities for 536 finite parameter pairs through length \(100\), plus 25 two-sided local limits at length \(200\). Both programs require only Python 3 and its standard library. Finite checks support but do not replace the infinite proof in Steps 1–5.

## Relationship to prior work

Austin, Chambers, Funke, García Puente and Keough introduced the multivariate avalanche polynomial and explicitly calculated it for trees, cycles, complete graphs and **wheel graphs** (arXiv:1605.02713, especially Section 6, Proposition 43, Theorem 44). They already supplied the fan recurrence word condition and the Fibonacci count as ingredients in counting **wheel** avalanches. Their wheel formula implies a closely related bulk size law; that limiting marginal is not claimed as an independent discovery. The claim here concerns the *finite fan* with a specified injection site: its complete support-resolved avalanche polynomial, exact endpoint effects and independent two-arm conditional factorization. Those finite fan statements do not follow by substituting parameters in the published wheel polynomial, because deleting a cycle edge changes the recurrence measure and the toppling support distribution.

Selig, *Combinatorial aspects of sandpile models on wheel and fan graphs* (arXiv:2202.06487, Section 5, Theorems 5.6 and 5.12) gives bijections and level enumeration of recurrent fan configurations, but does not calculate their driven principal avalanche support law. The exact finite factorization here is a dynamic observable not determined directly by the published level enumerator. Prior universal burning, matrix-tree and group-stationarity facts are expressly used, not presented as new.

## Limitations

This is an exact finite-graph and local bulk-limit result, not a claim of power-law self-organized-critical scaling. The sink must be the dominating fan vertex, the addition is one grain and there are no stochastic toppling rules, multiple sinks or site-dependent edge weights. The bulk limit requires the driven site to move away from both endpoints. Any previous unindexed calculation of the fan's full avalanche polynomial could affect priority; the examined sources establish related ingredients and wheel analogues, not this full finite fan support law. Independent external validation has not been performed.

## References

1. D. Austin, M. Chambers, R. Funke, L. D. García Puente and L. Keough, *The Avalanche Polynomial of a Graph*, first publicly posted 2016-05-09, arXiv:1605.02713, https://arxiv.org/abs/1605.02713 (especially Sections 2 and 6, Proposition 43 and Theorem 44).
2. T. Selig, *Combinatorial aspects of sandpile models on wheel and fan graphs*, first publicly posted 2022-02-14, arXiv:2202.06487, https://arxiv.org/abs/2202.06487 (especially Section 5).
