# Exact rational enumeration of ternary adjacent-pair profiles of linear words

## Finding

Let \(\Sigma=\{0,1,2\}\). For a linear word \(w=w_1\cdots w_n\in\Sigma^n\), \(n\geq1\), define its ordered-pair profile by
\[
P(w)_{ij}=\#\{k:1\leq k<n,\ (w_k,w_{k+1})=(i,j)\},\qquad i,j\in\Sigma.
\]
Let \(a_n=\#\{P(w):w\in\Sigma^n\}\), counting distinct numerical profiles, not words or multisets of profiles. Then, with \(z\) a formal indeterminate,
\[
\boxed{\begin{aligned}
F(z):=\sum_{n\geq1} a_nz^{n-1}
={}&1+\frac{3z}{1-z}
+\frac{3(2z+z^2)}{(1-z)^2(1-z^2)}\\
&+\frac{1}{(1-z)^3}\left[
\frac{1+6z+6z^2+z^3}{(1-z^3)(1-z^2)^3}
-1-\frac{6z+3z^2}{1-z^2}
\right].
\end{aligned}}
\]
Equivalently,
\[
F(z)=\frac{1+5z-8z^2+8z^3+13z^4-4z^5-10z^6-8z^7+11z^8+2z^9-5z^{10}+2z^{11}}
{(1-z)^7(1+z)^2(1+z+z^2)}.
\]
In particular,
\[
(a_1,\ldots,a_{10})=(1,9,24,65,156,342,683,1272,2226,3708)
\]
and
\[
a_n\sim\frac{7}{8640}n^6\qquad(n\to\infty).
\]
For the noiseless ordered-length-two multiset reconstruction channel over three symbols, \(a_n\) is also the maximum possible size of a code with pairwise distinct observations.

## Assumptions and scope

Words are **linear**, not cyclic; the alphabet symbols are fixed and labeled. The observation retains exact multiplicities of each of the nine ordered length-two factors, and does not reveal either endpoint separately. A word of length one has the zero profile, so \(a_1=1\). The formulas hold for every integer \(n\geq1\) and all formal series coefficients; asymptotics refer to \(n\to\infty\). No quotient by symbol permutation, reversal, or rotation is taken.

## Proof

Set \(m=n-1\). Interpret a profile as a directed multigraph on vertices \(\{0,1,2\}\): the number of arcs \(i\to j\) is \(P(w)_{ij}\), including loops. A nonzero profile comes from a linear word precisely when its nonisolated vertices form a weakly connected graph and its outdegree-minus-indegree vector is either zero or has one \(+1\), one \(-1\), and one zero. Necessity follows from traversing consecutive letters. Sufficiency is the directed Euler-trail theorem: weak connectivity on positive-degree vertices, together with the stated degree balances, yields an Euler trail, whose successive vertices spell a realizing word.

Partition nonzero profiles according to the number of vertices incident with arcs.

**One active vertex.** There are three choices, and its single loop multiplicity is any positive integer. The corresponding series is \(3z/(1-z)\).

**Two active vertices.** Choose the pair in three ways. Writing \(p,q\) for its two opposing nonloop arc multiplicities, one needs \(p+q>0\) and \(|p-q|\leq1\). Their series is
\[
B_2(z)=\sum_{r\geq0}2z^{2r+1}+\sum_{r\geq1}z^{2r}
=\frac{2z+z^2}{1-z^2}.
\]
The two loop counts are unrestricted, giving \(3B_2(z)/(1-z)^2\). This includes precisely the profiles with exactly two active vertices because the positive nonloop arcs connect the pair.

**Three active vertices.** First count profiles using only nonloop arcs. Orient the edges of the triangle as \(0\to1\), \(1\to2\), \(2\to0\), with forward multiplicities \(a,b,c\) and reverse multiplicities \(A,B,C\). For a closed trail, the degree equations are equivalent to
\[
a-A=b-B=c-C=t\in\mathbb Z.
\]
Separating \(t=0\), \(t>0\), and \(t<0\) gives the generating function for all nonnegative nonloop matrices of zero imbalance,
\[
C_0(z)=\frac{1+z^3}{(1-z^3)(1-z^2)^3}.
\]
For one fixed choice of distinct start and end vertices, say \(0\to1\), the equations instead read
\[
a-A=t+1,\quad b-B=t,\quad c-C=t.
\]
Splitting into \(t\geq0\) and \(t\leq-1\) gives
\[
C_1(z)=\frac{z+z^2}{(1-z^3)(1-z^2)^3}.
\]
There are six ordered distinct endpoint choices, all related by permutations of the labeled vertices. These counts include nonloop graphs disconnected on the three vertices. In the zero-imbalance class, such graphs consist either of no nonloop arcs (one possibility), or opposing arcs between just one of three vertex pairs, with equal positive multiplicities: generating function \(1+3z^2/(1-z^2)\). For each prescribed open endpoint pair, the disconnected graph consists solely of that one pair, with opposing arc counts differing by one: generating function \(z/(1-z^2)\). Thus the series of **weakly connected nonloop graphs on all three vertices** with admissible degree balances is
\[
H_3(z)=C_0(z)-1-\frac{3z^2}{1-z^2}
+6\left(C_1(z)-\frac{z}{1-z^2}\right).
\]
Appending arbitrary loop multiplicities at the three already connected vertices multiplies this series by \((1-z)^{-3}\). Conversely loops cannot connect two separate components, so this counts all and only three-active-vertex realizable profiles. Substituting \(C_0\) and \(C_1\) yields the displayed bracket.

Together with the unique empty profile for \(m=0\), the three disjoint classes give
\[
F(z)=1+\frac{3z}{1-z}+\frac{3B_2(z)}{(1-z)^2}+\frac{H_3(z)}{(1-z)^3}.
\]
Elementary rational simplification gives the second displayed formula. At \(z=1\), the numerator of that form has value \(7\), whereas \((1+z)^2(1+z+z^2)\) has value \(12\). The other poles are roots of unity with smaller order, so coefficient extraction yields \(a_n=(7/12)\binom{n+5}{6}+O(n^5)\), proving the asymptotic equivalence.

## Verification

The standalone standard-library program `verify.py` computes the formal series from the disjoint graph classes, independently enumerates the distinct profiles of all ternary words of lengths \(1\) through \(10\), and independently enumerates connected degree-balanced nonnegative matrices with total arc counts \(0\) through \(7\). The two independent finite enumerations agree with the rational formula. Execute `python verify.py` in the directory containing this result. Finite checks are supporting regression tests, **not** the proof of the all-length claim; the proof above supplies that claim.

## Relationship to prior work

Jacquet, Knessl, and Szpankowski studied balanced frequency matrices of **closed** Markov types and obtained the exact ternary rational function \((1-z+z^2)/((1-z)^7(1+z)^2(1+z+z^2))\). This equals the closed-imbalance, all-matrix term \(C_0(z)/(1-z)^3\), and differs from the present linear-word series. In their 2012 account, Theorem 4.5 as reproduced by Kiah, Puleo, and Milenkovic already gives the **general leading asymptotic ratio** \(q^2-q+1\) between unrestricted and closed length-two profiles. Thus the leading coefficient \(7/8640\) obtained here is a **previously implied consequence**, not a new asymptotic theorem. The contribution assessed for originality is instead the **exact all-length rational generating function**, including six nonzero boundary-imbalance types, connectivity corrections, and every finite-length coefficient.

Kiah, Puleo, and Milenkovic formulate DNA substring-profile equivalence and state the asymptotic ratio cited above (Theorem 4.5). Their Table I gives the closed ternary coefficient \(1/8640\), so the unrestricted leading coefficient is already determined. Chang, Chrisnata, Ezerman, and Kiah give exact expressions only in the **short-word** regime \(\ell\leq n<2\ell\) and bounds for larger lengths; neither result contains the displayed exact all-length ternary \(\ell=2\) coefficient sequence. A published exact binary \(\ell=2\) enumeration does not determine labeled ternary counts by substitution.

## Limitations

The enumeration applies only to labeled ternary alphabets and adjacent-pair multiplicities of linear words. It does not count distinct words within a profile class, recover endpoints, cover arbitrary alphabet sizes, or establish analogous results for longer factors. Although the primary sources examined do not state the same ternary all-length rational formula, an unindexed equivalent enumeration remains a priority risk. An independent audit of the mathematical argument has not been performed.

## References

- P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), DOI: 10.46298/dmtcs.2768. Original publication record: https://dmtcs.episciences.org/en/articles/2768 (dated 2009-12-31).
- H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Storage Channels*, arXiv:1410.8837v1 (2014-10-31), https://arxiv.org/abs/1410.8837.
- Z. Chang, J. Chrisnata, M. F. Ezerman, H. M. Kiah, *Rates of DNA Sequence Profiles for Practical Values of Read Lengths*, arXiv:1607.02279v1 (2016-07-08), https://arxiv.org/html/1607.02279v1.
