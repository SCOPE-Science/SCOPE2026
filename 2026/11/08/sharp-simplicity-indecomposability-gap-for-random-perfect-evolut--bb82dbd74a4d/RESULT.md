# Sharp simplicity–indecomposability gap for random perfect evolution algebras

## Finding

Fix a prime power \(q\ge 2\). On the vector space \(\mathbb F_q^n\) with labeled natural basis \(e_1,\dots,e_n\), choose a structure matrix \(M=(m_{ij})\) uniformly from \(\operatorname{GL}_n(\mathbb F_q)\) and define the evolution algebra \(E_M\) by \(e_ie_j=0\) for \(i\ne j\) and \(e_i^2=\sum_jm_{ij}e_j\). Write \(S_{n,q}\) for the probability that \(E_M\) is not simple and \(D_{n,q}\) for the probability that it decomposes as a direct sum of two nonzero ideals. Put

\[
\rho_n(q)=\prod_{j=1}^n(1-q^{-j}),\qquad
u_{n,q}=\frac{q-1}{q^n-1},\qquad
\delta_{n,q}=\frac{(q-1)q^{-2n+1}}{1-q^{-n}}.
\]

**Theorem (uniform sharp failure laws).** For every \(n\ge16\) and every prime power \(q\ge2\), with the absolute constant \(\kappa=\bigl(\prod_{j\ge1}(1-2^{-j})\bigr)^{-1}\),

\[
\bigl|S_{n,q}-2n\nu_{n,q}\bigr|\le6\kappa n^2q^{-2n+4},\qquad
\bigl|D_{n,q}-n\delta_{n,q}\bigr|\le5\kappa n^2q^{-4n+8}.
\]

In particular, both relative errors tend to zero as \(n\to\infty\), **uniformly over all prime powers \(q\ge2\)**, even when \(q\) varies with \(n\). Since decomposability implies nonsimplicity,

\[
\Pr(E_M\text{ decomposable}\mid E_M\text{ not simple})
=\frac1{2q^{n-1}}(1+o(1)),
\]

with a uniform \(o(1)\). Conditional on nonsimplicity, asymptotically almost surely its support digraph has exactly one vertex with all off-diagonal entries in its row **or** column zero, and the graph on the remaining vertices is strongly connected. Conditional on decomposability, asymptotically almost surely exactly one vertex has all off-diagonal entries in both its row and column zero, and the remaining support graph is weakly connected.

**Theorem (exact decomposition profile).** Let \(g_0(q)=1\), \(g_n(q)=|\operatorname{GL}_n(\mathbb F_q)|\) for \(n\ge1\), and \(c_n(q)\) be the number of matrices in \(\operatorname{GL}_n(\mathbb F_q)\) whose associated evolution algebra is indecomposable. Then \(c_1(q)=q-1\) and

\[
 c_n(q)=g_n(q)-\sum_{k=1}^{n-1}\binom{n-1}{k-1}c_k(q)g_{n-k}(q).
\]

As formal power series in \(z\),

\[
 \sum_{n\ge1}\frac{c_n(q)}{n!}z^n
 =\log\left(\sum_{n\ge0}\frac{g_n(q)}{n!}z^n\right).
\]

The number of such invertible matrices with exactly \(r\) nonzero indecomposable direct summands is

\[
 \frac{n!}{r!}[z^n]\left(\sum_{k\ge1}\frac{c_k(q)}{k!}z^k\right)^r.
\]

For an unconditioned uniformly selected matrix in \(M_n(\mathbb F_q)\), the corresponding evolution algebra is simple with probability \(\rho_n(q)(1-S_{n,q})\). Hence, for each fixed \(q\), this probability tends to the positive Euler product \(\prod_{j\ge1}(1-q^{-j})\).

## Assumptions and scope

All algebras are finite-dimensional, commutative, generally nonassociative evolution algebras over \(\mathbb F_q\). A matrix is sampled uniformly as a *labeled natural-basis structure matrix*; isomorphic algebras are not weighted equally. An algebra is called decomposable if it is a direct sum of two nonzero algebra ideals. Simplicity uses the usual absence of proper nonzero ideals together with nonzero multiplication. Because \(M\) is invertible, \(E_M^2=E_M\); it is perfect and non-degenerate. Edges of its support digraph are \(i\to j\) whenever \(m_{ij}\ne0\), including possible loops. Weak connectivity ignores edge directions.

The sharp probability inequalities are asserted for \(n\ge16\); the exact counting identities hold for every \(n\ge1\). The conditional statements concern \(n\to\infty\), uniformly in the field order. None of the results counts isomorphism classes.

## Proof

**1. Algebra–graph dictionary.** For a perfect evolution algebra the graph is strongly connected precisely when the algebra is simple; for a non-degenerate evolution algebra, indecomposability is equivalent to weak connectivity of the support graph. Both are established structural criteria in the cited literature. The unique direct-sum decomposition of a perfect algebra corresponds to weakly connected components. In particular, a disconnected support graph becomes block diagonal after simultaneously permuting rows and columns, and each diagonal block is invertible.

**2. Exact cut probabilities.** For a nonempty proper \(S\subset[n]\) of cardinality \(k\), put \(T=[n]\setminus S\). Define \(U_S\) by \(m_{ij}=0\) for all \(i\in S,j\in T\). Define \(V_S\) by \(U_S\) and the reverse block of zeros \(m_{ji}=0\) for all such \(i,j\). A directed graph is not strongly connected exactly when at least one \(U_S\) occurs; an undirected support graph is disconnected exactly when at least one \(V_S\) occurs. In the first event, the matrix has block lower-triangular form with invertible diagonal blocks and an arbitrary \((n-k)\)-by-\(k\) lower block. In the second it is block diagonal. Thus the *exact* numbers of invertible matrices satisfying these events are

\[
 N(U_S)=g_k(q)g_{n-k}(q)q^{k(n-k)},\qquad
 N(V_S)=g_k(q)g_{n-k}(q).
\]

Using \(g_j(q)=q^{j^2}\rho_j(q)\) gives

\[
 \Pr(U_S)=q^{-k(n-k)}\frac{\rho_k(q)\rho_{n-k}(q)}{\rho_n(q)},
 \quad
 \Pr(V_S)=q^{-2k(n-k)}\frac{\rho_k(q)\rho_{n-k}(q)}{\rho_n(q)}.
\]

For \(k=1\) or \(n-1\), \(\Pr(U_S)=\nu_{n,q}\). For \(k=1\), \(\Pr(V_S)=\delta_{n,q}\). These equalities use no asymptotic approximation.

**3. Uniform estimates for nonsingleton cuts.** Define \(\rho_\infty(2)=\prod_{j\ge1}(1-2^{-j})>0\) and \(\kappa=1/\rho_\infty(2)\). For all \(q\ge2\) and \(j\ge1\), \(\rho_j(q)\ge\rho_\infty(2)\), so the ratios in step 2 are at most \(\kappa\). If \(2\le k\le n/2\), the exact identity

\[
 k(n-k)=2(n-2)+(k-2)(n-k-2)
\]

implies, using \(\binom nk\le n^k\), symmetry about \(n/2\), and \(nq^{-n/2+2}\le\tfrac12\) for \(n\ge16\),

\[
 \sum_{k=2}^{n-2}\binom nk q^{-k(n-k)}\le4n^2q^{-2n+4},\qquad
 \sum_{k=2}^{n-2}\binom nk q^{-2k(n-k)}\le4n^2q^{-4n+8}.
\]

The second estimate follows by the same argument, using \(nq^{-n+4}\le\tfrac12\). These bounds are uniform in \(q\).

**4. Exceptional singleton cuts and their overlaps.** The \(2n\) directed singleton-cut events are the \(n\) events \(U_{\{i\}}\) (only the diagonal entry of row \(i\) can be nonzero) and the \(n\) events \(U_{[n]\setminus\{i\}}\) (only the diagonal entry of column \(i\) can be nonzero). Each has probability \(\nu_{n,q}\). Two distinct such events force at least \(2n-3\) distinct matrix entries to vanish. Under unconditioned independent uniform entries this has probability at most \(q^{-2n+3}\); conditioning on invertibility increases it by at most the factor \(\kappa\). Bonferroni's inequalities and step 3 therefore yield

\[
 |S_{n,q}-2n\nu_{n,q}|
 \le\kappa\binom{2n}{2}q^{-2n+3}+4\kappa n^2q^{-2n+4}
 \le6\kappa n^2q^{-2n+4}.
\]

The \(n\) undirected singleton-cut events \(V_{\{i\}}\) each have probability \(\delta_{n,q}\). Two distinct such events force at least \(4n-6\) zeros, including both directions between the two isolated vertices. Again by Bonferroni and step 3,

\[
 |D_{n,q}-n\delta_{n,q}|
 \le\kappa\binom n2q^{-4n+6}+4\kappa n^2q^{-4n+8}
 \le5\kappa n^2q^{-4n+8}.
\]

**5. Sharp gap and typical exceptional forms.** Relative to their main terms the two errors are bounded, respectively, by quantities of order \(nq^{-n+4}\) and \(nq^{-2n+7}\), uniformly for \(q\ge2\). Both tend to zero as \(n\to\infty\). Moreover, the main terms have the *exact ratio*

\[
 \frac{n\delta_{n,q}}{2n\nu_{n,q}}=\frac1{2q^{n-1}}.
\]

Because decomposability implies nonsimplicity, this proves the conditional asymptotic. The same bounds show that, among nonsimple algebras, occurrence of no singleton cut or of at least two singleton cuts has vanishing conditional probability. If there is exactly one singleton directed cut and no other cut, the induced graph on the remaining vertices is strongly connected: a nontrivial directed cut there would combine with (or be disjoint from) the exceptional vertex to produce a second cut in the full graph. Likewise, the complement of a unique isolated weak component is weakly connected. This establishes both conditional structural assertions.

**6. Exact decomposition profile.** Let \(c_n(q)\) count invertible matrices whose undirected support graph is connected. The component of vertex \(1\) has some size \(k\); its other \(k-1\) vertices can be chosen in \(\binom{n-1}{k-1}\) ways, its restriction can be chosen in \(c_k(q)\) ways, and the matrix on the other vertices is arbitrary in \(\operatorname{GL}_{n-k}(\mathbb F_q)\). All cross-block entries vanish. Conversely, every such choice yields an invertible matrix whose component at vertex \(1\) is the designated block. Hence

\[
 g_n(q)=\sum_{k=1}^{n}\binom{n-1}{k-1}c_k(q)g_{n-k}(q).
\]

This rearranges to the stated recurrence. The labeled-set exponential formula, or equivalently the differential equation \(G'(z)=C'(z)G(z)\) with \(G(0)=1\), proves \(G(z)=\exp C(z)\). Taking coefficients of \(C(z)^r/r!\) counts matrices with exactly \(r\) weakly connected components. The correspondence in step 1 identifies these with the indecomposable algebra summands.

**7. Unconditioned sampling.** An evolution algebra with a singular structure matrix cannot be simple, because a simple evolution algebra must be perfect. A uniformly chosen matrix in \(M_n(\mathbb F_q)\) is invertible with probability \(\rho_n(q)\), and conditional on invertibility it is uniform in \(\operatorname{GL}_n(\mathbb F_q)\). Thus its simplicity probability is exactly \(\rho_n(q)(1-S_{n,q})\), tending for fixed \(q\) to \(\rho_\infty(q)>0\).

## Verification

The included standalone \(\texttt{verify.py}\) enumerates *all* matrices in six finite-field parameter cases: \((n,q)=(2,2),(3,2),(4,2),(2,3),(3,3),(2,4)\). For each case it enumerates the invertible matrices, tests directed strong connectivity and undirected weak connectivity, counts each individual one-way and two-way cut, and compares these exact counts with the formulas in step 2. It independently computes \(c_n(q)\) using the recurrence and compares it with the exhaustive connected count. The characteristic-two extension field \(\mathbb F_4\) is implemented as \(\mathbb F_2[t]/(t^2+t+1)\). The recorded output concludes \(\texttt{VERIFY_OK cases=6}\).

Finite enumeration is **not** evidence for the universal estimates by itself; those follow from the symbolic block counts and uniform cut bounds. The verification code does not certify historical novelty.

## Relationship to prior work

Cabrera Casado–Siles Molina–Velasco (arXiv:1601.01832; Corollary 5.8, Theorem 5.11) proved the indecomposability/connectedness dictionary and uniqueness of the decomposition. Elduque–Labra (arXiv:1312.4685) developed the graph approach. These statements are used as known inputs, not presented as new. Alshatnawi–Costoya–Viruel (arXiv:2607.15154) studied structural decomposition and its Grothendieck-ring behavior, and explicitly motivated a probabilistic classification, without the conditional finite-field counts here. Kaygorodov–Martín González–Viruel (arXiv:2610.22248, Question 22) explicitly asks about the asymptotic probability of simplicity and indecomposability for random evolution algebras. The results here supply exact labeled perfect-algebra decomposition enumerators, uniform sharp conditional asymptotics, and an unconditional simplicity limit for the dense finite-field model. They do not solve that question for arbitrary sparse random patterns or uniformly sampled isomorphism classes.

## Limitations

The probability space weights labeled invertible structure matrices, not algebra isomorphism types. All sharp rates concern the dense uniform finite-field model. The full indecomposability probability for *singular* random structure matrices is not determined; only the joint event of perfection and indecomposability is determined by conditioning. Neither sparse-entry thresholds nor automorphism-group probabilities are addressed. No independent mathematical audit or historical-priority certification has been performed.

## References

1. I. Alshatnawi, C. Costoya, A. Viruel, *On the Grothendieck Ring of Finite-Dimensional Non-Degenerate Evolution Algebras*, arXiv:2607.15154, first posted 2026-07-16. https://arxiv.org/abs/2607.15154
2. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248, first public version 2026-10-15. https://arxiv.org/abs/2610.22248
3. Y. Cabrera Casado, M. Siles Molina, M. V. Velasco, *Evolution algebras of arbitrary dimension and their decompositions*, arXiv:1601.01832, first posted 2016-01-08. https://arxiv.org/abs/1601.01832
4. A. Elduque, A. Labra, *Evolution algebras and graphs*, arXiv:1312.4685, first posted 2013-12-17. https://arxiv.org/abs/1312.4685
