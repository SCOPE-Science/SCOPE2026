# Exact online ranks and shattering polynomials of fixed-width intervals on finite chains

## Finding

Fix integers \(n\geq 1\) and \(1\leq r\leq n\). Write \(m=n-r+1\), \(X=[n]\), and \(I_s=\{s,s+1,\ldots,s+r-1\}\) for \(s\in[m]\). Consider the two binary membership concept classes \(\mathcal W^-_{n,r}=\{I_s:s\in[m]\}\) and \(\mathcal W^+_{n,r}=\mathcal W^-_{n,r}\cup\{\varnothing\}\). The exact Littlestone dimensions are

\[
\operatorname{Ldim}(\mathcal W^-_{n,r})
=\min\{\lfloor\log_2m\rfloor,\ 1+\lfloor\log_2r\rfloor\},
\qquad
\operatorname{Ldim}(\mathcal W^+_{n,r})
=\min\{\lfloor\log_2(m+1)\rfloor,\ 1+\lfloor\log_2r\rfloor\}.
\]

In particular, adding the null concept increases the online dimension by exactly one if and only if \(m=2^k-1\) for some integer \(k\geq1\) with \(r\geq2^{k-1}\); otherwise it has no effect.

Both complete shattering polynomials are explicit. Put \(k_0=\max\{0,m-r-1\}\) and \(t=\min\{r-1,k_0-1\}\). Any sum whose upper limit is smaller than its lower limit is zero. Then

\[
\Phi^-_{n,r}(z)=1+\bigl(n-\max\{0,r-m+1\}\bigr)z
+\left(2k_0(r-1)-\sum_{d=1}^{t}(k_0-d)\right)z^2,
\]

\[
\Phi^+_{n,r}(z)=1+nz+\left(\sum_{j=1}^{m-2}\min\{j,r-1\}\right)z^2.
\]

All coefficients of degree at least three vanish. For example, when \(n=2r\) and \(r\geq2\), the non-null class has VC dimension one but Littlestone dimension \(\lfloor\log_2(r+1)\rfloor\), which diverges as \(r\) grows. This is an exact static-versus-adaptive separation within equal-length intervals.

## Assumptions and scope

The ground set is a *finite linearly ordered chain* \([n]\); there is no cyclic wraparound. Windows have *exactly* \(r\) consecutive vertices, not lengths bounded above by \(r\). The only difference between the two classes is whether the all-zero concept is included. The empty queried support is counted as one shattered face. \(\operatorname{Ldim}\) means the maximal depth of a complete binary tree of adaptive membership queries with all root-to-leaf labelings realizable by concepts in the class. All claims hold for every integer pair \(1\leq r\leq n\), including \(m=1\), \(r=1\), and \(n=1\).

## Proof

**1. Upper bounds on the online ranks.** A depth-\(h\) complete binary mistake tree needs at least \(2^h\) *distinct* concepts. The two classes contain, respectively, \(m\) and \(m+1\) concepts; hence the cardinality upper bounds. At any query position \(x\in[n]\), at most \(r\) length-\(r\) windows contain \(x\): their start indices lie in \([x-r+1,x]\cap[m]\). If a complete mistake tree has positive depth \(h\), its positive root-child must contain at least \(2^{h-1}\) concepts. Therefore \(2^{h-1}\leq r\), giving the second upper bound for each class.

**2. Prefix-query lemma.** Consider any consecutive block \(B=\{a,a+1,\ldots,a+q-1\}\subseteq[m]\) of starting indices with \(q\leq r\). For any \(1\leq t\leq q\), the position \(x=a+t-1\in[n]\) satisfies \(x\in I_s\) for \(s\in B\) if and only if \(s\leq a+t-1\). Indeed, every \(s\in B\) lies in the integer range \([x-r+1,x]\) exactly when \(s\leq x\), because \(x-r+1\leq a\). Thus every *prefix threshold* of a contiguous block of at most \(r\) window starts can be implemented by an ordinary point-membership query. Balanced prefix queries on \(2^j\) consecutive starts yield a shattered complete tree of depth \(j\) whenever \(2^j\leq r\).

**3. Lower bound without a null concept.** Let \(h\geq1\) satisfy \(2^h\leq m\) and \(2^{h-1}\leq r\). Restrict the class to the first \(2^h\) consecutive windows. Query at \(x=2^{h-1}\): it selects exactly the first \(2^{h-1}\) starts as positive, and the remaining \(2^{h-1}\) as negative. Each branch is a consecutive block of length at most \(r\) and therefore has depth-\((h-1)\) shattered threshold trees by step 2. This proves the first equality. At \(m=1\), the class has one concept and rank zero, as the formula states.

**4. Lower bound with a null concept.** Induct on \(h\geq1\). Suppose \(m\geq2^h-1\) and \(r\geq2^{h-1}\); restrict to \(\varnothing\) and the first \(2^h-1\) windows. At \(h=1\), query position \(1\), separating \(I_1\) from \(\varnothing\). For \(h\geq2\), querying \(x=2^{h-1}\) produces a positive branch containing exactly \(2^{h-1}\) consecutive windows (rank at least \(h-1\) by step 2) and a negative branch containing \(\varnothing\) plus \(2^{h-1}-1\) consecutive windows. The induction hypothesis applies to the negative branch after translating all start positions by \(2^{h-1}\): the prefix-query lemma and the required width bound are invariant under this translation. Thus the null-completed class shatters depth \(h\), proving the second equality. The jump criterion follows from comparing the two integer floors and their common width cap.

**5. Static shattering, null completed.** Since every concept is an interval or empty, no three positions \(u<v<w\) can be shattered: label \(u,w\) positive and \(v\) negative. Every singleton is shattered because it appears in a window and \(\varnothing\) realizes its negative label. For a pair \(u<v\), the four labels are realizable exactly when (i) \(v-u<r\) (a window contains both), (ii) \(v>r\) (a window contains \(u\) but not \(v\)), and (iii) \(u<m\) (a window contains \(v\) but not \(u\)); the all-negative trace is realized by \(\varnothing\). To count pairs, write \(v=r+j\), where \(1\leq j\leq m-2\). The permissible positions \(u\) number \(\min\{m-1-j,r-1\}\). Reindexing gives the stated quadratic coefficient.

**6. Static shattering, non-null.** The intersection of all \(m\) windows is the interval \([m,r]\) when \(m\leq r\), and is empty otherwise. Hence exactly \(n-\max\{0,r-m+1\}\) singleton positions are shattered. In addition to conditions (i)–(iii), a two-point support needs an all-negative window. Because \(v-u<r\), no length-\(r\) window fits strictly between \(u\) and \(v\), so the all-negative trace exists precisely if \(u>r\) (a window strictly to its left) or \(v<m\) (a window strictly to its right). Put \(k_0=\max\{0,m-r-1\}\). The cases \(v<m\) and \(u>r\) each contribute \(k_0(r-1)\) eligible pairs. Their overlap consists of pairs drawn from \(k_0\) consecutive positions with separation at most \(r-1\), contributing \(\sum_{d=1}^{\min\{r-1,k_0-1\}}(k_0-d)\). Inclusion-exclusion proves the second quadratic coefficient. Triple shattering remains impossible, completing both polynomials.

## Verification

The standalone script `verify_windows.py` independently enumerates both concept classes, computes their exact finite Littlestone dimensions by the defining child-recursion with memoization, and tests all candidate supports through size three against the two displayed shattering polynomials. The executed sweep covered all \(136\) parameter pairs \(1\leq r\leq n\leq16\) for both online dimensions (\(272\) concept classes); polynomial checks cover \(1\leq r\leq n\leq14\). Its terminal marker is `WINDOW_RANK_AND_TRACE_PASS 136 n_r_pairs 272 rank_classes n_max 16 polynomial_n_max 14`. This is a finite corroboration of the proof, not a substitute for the all-parameter arguments.

## Relationship to prior work

Chase and Freitag (2018) identify Littlestone dimension with finite Shelah \(2\)-rank and relate this rank to model-theoretic stability; this supplies the natural foundational context. Alon, Beimel, Moran and Stemmer (2020), Ghazi, Golowich, Kumar and Manurangsi (2021), and Malliaris and Moran (2021) develop general online-dimension methods, closure results and stability connections. Their general theorems do not state these exact finite fixed-window coefficients or ranks.

A previously recorded result for *cyclic* windows gives \(1+\lfloor\log_2\min\{r,N-r\}\rfloor\) for all translates of an \(r\)-window on \(\mathbb Z/N\mathbb Z\). That setting has wraparound windows and no isolated null hypothesis, unlike either class considered here. For instance, at \((n,r)=(10,4)\), the three relevant ranks are \(2\) for linear windows, \(3\) for their null completion, and \(3\) for cyclic windows; the cyclic statement therefore does not imply the two linear formulas. The novelty assessment here concerns the *paired exact linear ranks, the null-concept jump boundary, and the full static coefficients*, not the elementary cardinality bound, threshold binary search, or the cyclic result.

## Limitations

The proof concerns equal-length intervals on a finite chain only; arbitrary lengths, weighted positions, cyclic wraparound, multiclass observations and other query models are not covered. The only validation beyond the proof is finite exact enumeration, and no independent mathematical audit has occurred. Historical priority under alternative terminology such as banded consecutive-ones matrices, interval translation classes, or active window identification remains an unresolved literature risk; unsuccessful searches alone do not establish novelty.

## References

1. H. Chase and J. Freitag, *Model Theory and Machine Learning*, arXiv:1801.06566v1 (first public 2018-01-19), Section 4, https://arxiv.org/abs/1801.06566 .
2. N. Alon, A. Beimel, S. Moran and U. Stemmer, *Closure Properties for Private Classification and Online Prediction*, Proceedings of Machine Learning Research 125 (2020), https://proceedings.mlr.press/v125/alon20a.html .
3. B. Ghazi, N. Golowich, R. Kumar and P. Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, Proceedings of Machine Learning Research 132 (2021), https://proceedings.mlr.press/v132/ghazi21a.html .
4. M. Malliaris and S. Moran, *Agnostic Online Learning and Excellent Sets*, arXiv:2108.05569 (first public 2021-08-12), https://arxiv.org/abs/2108.05569 .
