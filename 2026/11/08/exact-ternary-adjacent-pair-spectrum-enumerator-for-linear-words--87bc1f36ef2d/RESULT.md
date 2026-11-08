# Exact ternary adjacent-pair spectrum enumerator for linear words

## Finding

Fix the labeled ternary alphabet \(\Sigma=\{0,1,2\}\). For every word \(w=w_1\cdots w_n\in\Sigma^n\), \(n\ge1\), define its **adjacent-pair spectrum** as the ordered nonnegative integer matrix
\[
M(w)_{ij}=\#\{t:1\le t<n,\ w_t=i,\ w_{t+1}=j\},\qquad i,j\in\Sigma.
\]
No initial symbol, terminal symbol, or separate letter-count information is included in the observation. Let \(a_m\) count distinct matrices \(M(w)\) among all linear words of length \(m+1\), with \(m\ge0\). Then
\[
\boxed{\sum_{m\ge0}a_m z^m=\frac{1+5z-8z^2+8z^3+13z^4-4z^5-10z^6-8z^7+11z^8+2z^9-5z^{10}+2z^{11}}{(1-z)^7(1+z)^2(1+z+z^2)}.}
\]
In particular, the coefficient sequence beginning at \(m=0\) is
\[
1,9,24,65,156,342,683,1272,2226,3708,5919,9120,13625,19827,28188,39269,53721,72315,95934.
\]
The exact leading asymptotic is
\[
\boxed{a_m\sim \frac{7m^6}{8640}\quad(m\to\infty).}
\]
Equivalently, the maximum size of a fixed-length ternary code whose distinct codewords have different complete length-two adjacent-pair multiplicity vectors is exactly \(a_{n-1}\).

## Assumptions and scope

Words are **linear**, not cyclic. The terminal-to-initial pair is not counted. The alphabet's three letters remain labeled, and only equality of the complete nine-entry spectrum defines the observational equivalence. Reversal, letter relabeling, and different word endpoints are *not* identified as symmetries; they may nonetheless yield the same matrix if the nine counts coincide. At \(m=0\), all three one-letter words yield the unique zero matrix, hence \(a_0=1\). The generating series is formal over the integers, with convergence not required for the identity.

## Proof

**1. Euler-trail characterization.** Interpret any nonnegative \(3\times3\) integer matrix \(M\) as a directed multigraph on \(\Sigma\), containing \(M_{ij}\) distinguishable occurrences of the directed edge \(i\to j\). Its ordered edges are the adjacent pairs of a linear word exactly when this multigraph has an Euler trail. Write
\[
\delta_i=\sum_j M_{ij}-\sum_j M_{ji}.
\]
The Euler-trail theorem says that this happens precisely when all vertices incident with an edge belong to one component of the underlying undirected support and either \(\delta=(0,0,0)\) or \(\delta=e_s-e_t\) for two different symbols \(s,t\). The zero-edge graph also represents the unique zero matrix. Edge multiplicity labels do not affect existence, and one counts each matrix once regardless of the number of trails.

**2. All nonnegative matrices satisfying the divergence condition.** For each unordered pair of different vertices, record the signed difference of the two opposite directed multiplicities:
\[
p=M_{01}-M_{10},\qquad q=M_{02}-M_{20},\qquad r=M_{12}-M_{21}.
\]
For a fixed signed difference \(d\in\mathbb Z\), the possible ordered nonnegative multiplicity pairs are exactly
\[
(\max(d,0)+t,\max(-d,0)+t),\quad t\in\mathbb Z_{\ge0},
\]
whose total-edge generating function is \(z^{|d|}/(1-z^2)\). The three diagonal counts are independently nonnegative and contribute \((1-z)^{-3}\).

The divergence equations read \(\delta_0=p+q\), \(\delta_1=-p+r\), and \(\delta_2=-q-r\). For zero divergence they require \((p,q,r)=(p,-p,p)\), giving the off-diagonal series
\[
T_0(z)=\sum_{p\in\mathbb Z}\frac{z^{3|p|}}{(1-z^2)^3}
=\frac{1+z^3}{(1-z^3)(1-z^2)^3}.
\]
For one specified ordered pair of distinct start and finish symbols, symmetry reduces the divergence to \(\delta=e_0-e_1\). Its signed differences are \((p,1-p,p-1)\). Thus the off-diagonal series is
\[
T_1(z)=\sum_{p\in\mathbb Z}\frac{z^{|p|+2|p-1|}}{(1-z^2)^3}
=\frac{z+z^2}{(1-z^3)(1-z^2)^3}.
\]
There are exactly six different ordered start/finish pairs. A matrix cannot have two different nonzero divergence patterns, so the total count subject only to flow balance or one unit of imbalance has series \((T_0+6T_1)/(1-z)^3\).

**3. Precisely exclude disconnected matrices.** There are only three vertices. When every off-diagonal entry is zero, all diagonal combinations counted by \((1-z)^{-3}\) are present in the flow calculation. Of these, only the zero matrix and the graphs with loops at *one* vertex are realizable by one trail: their generating function is \(1+3z/(1-z)\). Hence replace the no-off-diagonal contribution \((1-z)^{-3}\) by \(1+3z/(1-z)\).

If there is at least one off-diagonal edge but the support is disconnected, all off-diagonal edges lie between exactly two vertices, and the third vertex has a positive loop count. In the balanced case the two directed multiplicities on this pair are equal to an integer \(t\ge1\). There are three possible unordered pairs, yielding the forbidden series
\[
3\frac{z^2}{1-z^2}\frac{z}{1-z}\frac1{(1-z)^2}
=\frac{3z^3}{(1-z)^3(1-z^2)}.
\]
In the nonzero-imbalance case the two directed multiplicities differ by exactly one. There are six oriented pairs and their two-edge contribution is \(z/(1-z^2)\); together with a positive isolated loop and arbitrary loops at the connected pair this gives the forbidden series
\[
6\frac{z}{1-z^2}\frac{z}{1-z}\frac1{(1-z)^2}
=\frac{6z^2}{(1-z)^3(1-z^2)}.
\]
No other disconnected support is possible on three vertices with an off-diagonal edge. These exclusions are disjoint, so exactly
\[
F(z)=\frac{T_0(z)+6T_1(z)-1}{(1-z)^3}+1+\frac{3z}{1-z}
-\frac{6z^2+3z^3}{(1-z)^3(1-z^2)}.
\]
Inserting the explicit expressions for \(T_0,T_1\) and combining rational functions produces the boxed rational function. Every subtraction removes exactly a forbidden matrix and every remaining matrix has an Euler trail, establishing both directions for all \(m\ge0\).

**4. Asymptotics.** As \(z\to1\), both \(T_0(z)\) and \(T_1(z)\) have leading singular term \(\frac1{12}(1-z)^{-4}\). The disconnected corrections have poles of order at most four, whereas multiplication by the diagonal factor gives \(\frac7{12}(1-z)^{-7}\). All other roots of the denominator have pole order strictly below seven. By the binomial coefficient expansion of \((1-z)^{-7}\), the leading coefficient is \(\frac7{12}\frac{m^6}{6!}=\frac{7m^6}{8640}\), as claimed.

## Verification

The standalone programs `verify.py` and `verify_independent.py` use only the Python standard library and are included with this result. Run them in the same directory using `python3 verify.py` and `python3 verify_independent.py`.

`verify.py` obtains coefficients from the displayed rational function by an integer polynomial recurrence. Separately, it enumerates all nonnegative nine-entry integer matrices with a given total, tests their Euler divergence and weak support connectivity, and checks the coefficients for \(0\le m\le9\). It reports `MATRIX_ENUM_OK` and `RATIONAL_COEFFS_OK`.

`verify_independent.py` enumerates all actual ternary words of lengths \(1\) through \(12\), deduplicates their complete nine-entry bigram counts, and compares those counts with a separately implemented signed-flow expansion for \(0\le m\le18\). It reports `DIRECT_WORD_ENUM_OK` and `SIGNED_FLOW_SERIES_OK`. The attached `census.csv` contains the complete coefficient list for \(0\le m\le20\). These finite checks test the derivation but are not substitutes for the all-length combinatorial proof.

## Relationship to prior work

Jacquet, Knessl and Szpankowski's *Markov Types Again Revisited* (manuscript dated 2009-09-02) and *Counting Markov Types* (public journal record dated 2009-12-31) explicitly restrict their exact matrix enumeration to the **balanced cyclic** setting. They obtain the all-nonnegative-balanced generating function for three letters
\[
F_3^*(z)=\frac{1-z+z^2}{(1-z)^7(1+z)^2(1+z+z^2)}.
\]
This is exactly the balanced-flow component \(T_0/(1-z)^3\), before subtracting disconnected loop configurations. It does **not** enumerate the six endpoint-imbalanced classes required for linear words, nor enforce the trail-support connectivity corrections. The balanced component and general coefficient-extraction framework are credited to that work, not claimed here.

Karhumäki, Puzynina, Rao and Whiteland's *On cardinalities of k-abelian equivalence classes* (arXiv:1605.03319, first version 2016-05-11) studies the finer \(2\)-abelian equivalence: alongside bigram counts, the initial and terminal symbols must agree. The present observation deliberately does *not* retain them. Existing published exact counts for the binary adjacent-pair spectrum concern a different alphabet and do not imply the ternary formula. The graph-trail criterion and rational-series methods are classical; the contribution here is the exact ternary linear-spectrum count with its disconnected-support exclusions and leading coefficient.

## Limitations

The result treats exactly three labeled symbols and windows of length two, with no cyclic wraparound. It does not produce an all-alphabet formula or count the sizes of individual reconstruction fibers. The finite coefficient census is not an independent infinite proof. Historical priority is qualified: a related 2012 journal extension of the Markov-type work was identified, but its full text could not be checked here; the accessible public abstract emphasizes balanced frequency matrices, and the earlier original full texts were inspected. An unindexed exact linear-spectrum computation cannot be excluded.

## References

1. P. Jacquet, C. Knessl and W. Szpankowski, *Markov Types Again Revisited*, manuscript dated 2009-09-02. Author-hosted copy: https://www.cs.purdue.edu/homes/spa/papers/markov-types.pdf . The dated manuscript is not treated as evidence of its public posting date.
2. P. Jacquet, C. Knessl and W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM, 387–400 (2010); publisher record public date 2009-12-31, https://doi.org/10.46298/dmtcs.2768 ; full text: https://dmtcs.episciences.org/en/articles/2768/download .
3. P. Jacquet, C. Knessl and W. Szpankowski, *Counting Markov Types, Balanced Matrices, and Eulerian Graphs*, IEEE Transactions on Information Theory 58(7), 4261–4272 (2012), https://doi.org/10.1109/TIT.2012.2191476 . Full text not obtained for comparison.
4. J. Karhumäki, S. Puzynina, M. Rao and M. A. Whiteland, *On cardinalities of k-abelian equivalence classes*, arXiv:1605.03319 (first posted 2016-05-11), https://arxiv.org/abs/1605.03319 .
