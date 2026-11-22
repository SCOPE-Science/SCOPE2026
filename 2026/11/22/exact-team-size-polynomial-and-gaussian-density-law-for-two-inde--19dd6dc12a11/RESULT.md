# Exact team-size polynomial and Gaussian density law for two independent rectangles

## Finding

Let \(Y\) and \(Z\) be fixed, labelled nonempty sets of respective sizes \(m,n\). In ordinary lax team semantics, let \(\varphi=(y\perp z)\lor(y\perp z)\), where \(\perp\) is unconditional relational independence and \(\lor\) is lax splitting. Define the **team-size polynomial**
\[
P_{m,n}(t)=\sum_{X\subseteq Y\times Z\, :\, X\models\varphi}t^{|X|}.
\]
For \(k\in\{1,2,3\}\), positive integers \(d_1,\dots,d_k\), define
\[
D^{(m)}_k(d_1,\dots,d_k;t)=
\sum_{J\subseteq[k]}(-1)^{k-|J|}
\left(1+\sum_{j\in J}t^{d_j}\right)^m.
\]
Writing \(\mathcal S_n=2^{[n]}\setminus\{\varnothing\}\), the exact polynomial for every \(m,n\ge1\) is
\[
\begin{aligned}
P_{m,n}(t)={}&1+
\sum_{A\in\mathcal S_n}D^{(m)}_1(|A|;t)\\
&+\sum_{\{A,B\}\subseteq\mathcal S_n,\ A\ne B}
D^{(m)}_2(|A|,|B|;t)\\
&+\sum_{\substack{\{A,B\}\subseteq\mathcal S_n\\
A\not\subseteq B,\ B\not\subseteq A}}
D^{(m)}_3(|A|,|B|,|A\cup B|;t).
\end{aligned}
\]
Every sum is over actual subsets of the fixed labelled column set; unordered pairs are counted once. In particular, the coefficients are nonnegative integers and specify the entire cardinality distribution of satisfying teams, not merely the total number.

For a uniformly chosen satisfying team \(X_N\subseteq[N]\times[N]\), define \(H_N=|X_N|/N^2\). Then
\[
H_N\xrightarrow{\mathrm P}\frac7{16},\qquad
\sqrt N\left(H_N-\frac7{16}\right)
\xrightarrow{\mathrm d}\mathcal N\!\left(0,\frac{19}{128}\right).
\]
More precisely, the law of the uniform satisfying team is within \(O((3/4)^N)\) total variation of an explicitly defined two-factor model. In that model the mean of \(H_N\) is exactly \(7/16\) and its variance is exactly \((38N+25)/(256N^2)\).

## Assumptions and scope

A team is a **set**, without repeated assignments, on exactly the two variables \(y,z\). An independence atom \(y\perp z\) holds precisely when the team is the full product of its row and column projections, allowing the empty product. Lax splitting means \(X=X_1\cup X_2\), with both subteams satisfying the atom; the subteams need not be disjoint. Thus satisfaction is exactly Boolean matrix rank at most two, or equivalently a union of at most two complete Cartesian rectangles. The alphabets are separately labelled, and \(m,n\ge1\). Probability is uniform on **distinct satisfying teams**, not on their ordered factor decompositions.

## Proof

**1. Complete row-pattern classification.** For any team \(X\), let \(N_X(y)\subseteq Z\) denote its row neighbourhood. If \(X=(R_1\times C_1)\cup(R_2\times C_2)\), every nonempty neighbourhood is among \(C_1,C_2,C_1\cup C_2\), after discarding empty or repeated patterns. Conversely any team having at most two distinct nonempty row neighbourhoods is a union of two rectangles. A team with exactly three distinct nonempty row neighbourhoods is a union of two rectangles if and only if these neighbourhoods are \(A,B,A\cup B\) with \(A,B\) nonempty and incomparable by inclusion. In that situation the incomparable pair \(\{A,B\}\) is uniquely determined: its members are the two minimal nonempty row neighbourhoods. This gives four disjoint cases: zero, one, two, and the specified three nonempty row-pattern types.

**2. Weighted use of exact patterns.** For fixed distinct nonempty column patterns \(A_1,\ldots,A_k\), choose each of the \(m\) labelled rows as zero or one of these \(k\) patterns; give a row of pattern \(A_j\) weight \(t^{|A_j|}\). Requiring that every nonzero pattern actually occurs and applying inclusion–exclusion yields exactly \(D_k^{(m)}(|A_1|,\ldots,|A_k|;t)\). Sum over all pattern families in step 1. Disjointness and uniqueness of the incomparable generating pair prevent overcounting, proving the polynomial identity for all positive \(m,n\).

**3. A polynomial-size intersection sum.** The formula can also be evaluated by grouping ordered pairs of column patterns according to \(a=|A|\), \(b=|B|\), \(c=|A\cap B|\). For \(1\le a,b\le n\), \(\max(0,a+b-n)\le c\le\min(a,b)\), let
\[
W_n(a,b,c)=\frac{n!}{c!(a-c)!(b-c)!(n-a-b+c)!}.
\]
Then the second sum equals one half the sum of \(W_n(a,b,c)D_2^{(m)}(a,b;t)\) over all these triples except \(a=b=c\). The third equals one half the sum of \(W_n(a,b,c)D_3^{(m)}(a,b,a+b-c;t)\) over triples with \(a>c\) and \(b>c\). The first sum is \(\sum_{a=1}^n\binom na D_1^{(m)}(a;t)\). This produces an exact intersection-size formula using \(O(n^3)\) summands, each expanded by finite binomial arithmetic. No enumeration of \(2^{mn}\) teams is required.

**4. Asymptotically uniform factorization.** Independently sample row codes \(U_1,\ldots,U_N\) and column codes \(V_1,\ldots,V_N\), each uniformly from the four two-bit strings. Form \(B_{ij}=1\) iff some coordinate is one in both \(U_i\) and \(V_j\). This is always a union of two rectangles. With probability \(1-O((3/4)^N)\), every row code occurs and both column codes \(10\) and \(01\) occur. On that event the output has row neighbourhoods \(\varnothing,A,B,A\cup B\) with \(A,B\) incomparable. By step 1, \(A,B\) are intrinsically recoverable up to swapping. Hence every such output matrix has exactly two ordered factor encodings (the coordinate swap), each with the same probability \(16^{-N}\). Moreover every non-generic satisfying matrix has at least one non-generic ordered factor encoding. Its number is at most the number of non-generic encodings, which is \(O(16^N(3/4)^N)\); the number of generic matrices is \((16^N/2)(1-O((3/4)^N))\). It follows that the uniform-on-matrices law and this independent-factor law differ by \(O((3/4)^N)\) in total variation.

**5. Mean, variance, and Gaussian limit.** Put \(f(u,v)=\mathbf1\{(u\mathbin{\&}v)\ne0\}\), where the symbol denotes coordinatewise Boolean conjunction. For either argument define \(g(u)=\mathbb E_V f(u,V)\). For the codes \(00,10,01,11\), respectively, the four values of \(g\) are \(0,\frac12,\frac12,\frac34\). Thus \(\mu=\mathbb E f=7/16\), \(\operatorname{Var}(g(U))=19/256\), and \(\operatorname{Var}(f(U,V))=63/256\). The exact two-sample decomposition is
\[
\frac1{N^2}\sum_{i,j}f(U_i,V_j)-\mu
=\frac1N\sum_i(g(U_i)-\mu)
+\frac1N\sum_j(g(V_j)-\mu)+R_N,
\]
where \(R_N=N^{-2}\sum_{i,j}h(U_i,V_j)\) and \(h(u,v)=f(u,v)-g(u)-g(v)+\mu\). Its conditional expectations given either argument vanish. Consequently all unequal terms in its squared sum are orthogonal, and \(\mathbb E R_N^2=25/(256N^2)\). The two leading sums are independent, so their combined variance is \(38/(256N)\) and the total variance is \((38N+25)/(256N^2)\). The ordinary bounded-i.i.d. central limit theorem applied to the two leading sums, together with \(\sqrt N R_N\to0\) in \(L^2\), proves the stated Gaussian law in the factor model. Step 4 transfers this limit and the limiting density to uniform distinct satisfying teams.

## Verification

The accompanying standalone `VERIFY.py` uses only the Python standard library. It computes the exact polynomial by row-pattern inclusion–exclusion and separately enumerates unions of all zero, one or two rectangles for every rectangular alphabet size \(1\le m,n\le5\) (25 complete cases); it verifies transposition, the independent intersection-size formula, and the square unweighted totals. It separately enumerates all ordered two-factor encodings through order four, verifies the exact factor-model mean and variance, and confirms generic encoding multiplicity two at square order four. Output includes `VERIFY_OK`, `WEIGHTED_MULTINOMIAL_OK`, and `FACTOR_MOMENTS_OK`. These finite checks support but do not replace steps 1–5, which prove every claimed all-size and asymptotic statement.

For reference, the polynomial for \(m=n=3\) has ascending coefficients
\[
1,9,36,78,90,54,42,36,9,1.
\]
The sum is \(356\). For \(m=n=4\) the sum is \(8776\). These totals agree with the previously known rank-zero, rank-one and rank-two Boolean matrix counts, and agreement at \(t=1\) does **not** establish or imply the size-refined identity.

## Relationship to prior work

The **2026** work of Barbero, Girlando, Müller, and Yang gives proof-theoretic developments for team logics with tensor disjunction. It motivates quantifying split-team behavior but is not cited as a source for the present polynomial or limit theorem. Haak, Kontinen, Müller, Vollmer, and Yang previously studied the complexity of counting teams in first-order team logics; their theorems concern expressive/counting complexity, not the complete cardinality polynomial or typical density of this fixed formula. The literature on Boolean matrix rank and biclique covers identifies the relevant matrix class; the exact unweighted square rank-two count is already recorded in OEIS A354741. We make no claim to have discovered that unweighted count, or the general notion of Boolean factorization/uniqueness. The claimed contribution is the all-rectangular **edge-count-refined polynomial** together with the **uniform-distinct-team Gaussian law and its explicit constants**.

A semantically similar counting result might occur in older matrix-pattern or team-model-counting literature under alternative terminology; the priority of the size-weighted and probabilistic refinements has not been independently established.

## Limitations

Only two variables, one repeated independence atom, lax splitting into two parts, and labelled finite alphabets are covered. The Gaussian statement is for square alphabets tending to infinity with no extra restrictions. It does not assert a central limit theorem for fixed-size teams, Boolean rank larger than two, strict disjunction, multiteams, or probabilistic independence atoms. The transferred finite-sample law for uniformly **distinct** satisfying teams is exponentially close to the factor law but is not claimed to have exactly the factor-model mean or variance for any finite order. The numerical checker is exhaustive only for its stated finite ranges. Historical priority is provisional; relevant older results might provide an equivalent weighted enumerator or Gaussian limit.

## References

1. F. Barbero, M. Girlando, V. Müller, F. Yang, *Labelled Sequent Calculi for Propositional Team Logics*, first arXiv posting 2026-06-30, https://arxiv.org/abs/2606.31860, https://doi.org/10.4204/EPTCS.447.7.
2. A. Haak, J. Kontinen, F. Müller, H. Vollmer, F. Yang, *Counting of Teams in First-Order Team Logics*, arXiv first posted 2019-02-01, https://arxiv.org/abs/1902.00246; 2025 expanded version https://doi.org/10.1145/3771721.
3. M. Parnas, A. Shraibman, *A study of the binary and Boolean rank of matrices with small constant real rank*, first posted 2025-07-08, https://arxiv.org/abs/2507.05824, https://doi.org/10.1016/j.dam.2026.02.014.
4. G. Critzer, *OEIS A354741: triangular array counting Boolean matrices by row rank*, first entered 2022-06-12, https://oeis.org/A354741.
5. M. Parnas et al., *Factorization of Binary Matrices: Rank Relations, Uniqueness and Model Selection of Boolean Decomposition*, https://doi.org/10.1145/3522594.
