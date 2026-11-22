# All minimum string-attractor pairs in two-marker binary words and a linear mean law

## Finding

Let \(a,b,c\) be arbitrary positive integers and let
\[
W_{a,b,c}=0^a1\,0^b1\,0^c,
\qquad n=a+b+c+2.
\]
The complete collection of minimum *full* string attractors has size two at every parameter triple. Its exact number \(K(a,b,c)\) is
\[
\boxed{K(a,b,c)=F(a,b,c)+F(c,b,a)},
\]
where
\[
\boxed{
F(a,b,c)=
\begin{cases}
a+1,&b>a,\ c\le b,\\
0,&b>a,\ c>b,\\
a+b\mathbf1_{a=b}+c\mathbf1_{a=c},&b\le a,\ c\le b,\\
b+1,&b\le a,\ c>b,\ c\ge a,\\
0,&b\le a,\ b<c<a.
\end{cases}}
\]
This counts **distinct two-position subsets** (not distinct factors or runs). The formula classifies every minimum position pair, not just their number; see the explicit interval description below.

There is a sharp three-gap resonance:
\[
\boxed{K(a,b,c)\le 2(a+b+c),\quad
K(a,b,c)=2(a+b+c)\ \Longleftrightarrow\ a=b=c.}
\]
In particular, at \(a=b=c=t\) there are \(6t\) optimal pairs, while for \(a=c=t\ne b\) there are only \(2(\min(b,t)+1)\).

Choose \((a,b,c)\) uniformly from positive triples with \(a+b+c=n-2\), equivalently choose uniformly from weight-two length-\(n\) binary words whose ones are separated and have a positive zero-run at either end. Then
\[
\boxed{\lim_{n\to\infty}\frac{\mathbb E K(a,b,c)}{n}=\frac{10}{27}.}
\]
More precisely, if \((X,Y,Z)\) is uniform on the simplex \(X,Y,Z>0\), \(X+Y+Z=1\), the normalized number \(K/n\) converges in distribution to
\[
\Phi(X,Y,Z)=
\begin{cases}
1-Y,&Y>\max(X,Z),\\
\max(X,Z),&\min(X,Z)<Y<\max(X,Z),\\
Y,&Y<\min(X,Z).
\end{cases}
\]
The ties, a measure-zero part of the simplex limit, are governed exactly by the finite formula above.

## Assumptions and scope

A *factor* means a nonempty contiguous substring. A string attractor is a set of positions such that each distinct factor has at least one occurrence whose inclusive interval meets the selected set. An attractor is *minimum* when its cardinality is least. Positions are indexed from zero; all three zero runs and the central separation are strictly positive, and the word is linear, not cyclic. A bitwise complement of every word has the same attractor counts. Different selected position sets count separately, and a factor's different occurrences may be used for coverage.

For an exact pair description, set \(p=a\), \(q=a+b+1\), \(M=\max(a,b,c)\), and let \(Z_M\) be the set of all zero positions belonging to any zero run of length exactly \(M\). The valid pair sets containing \(p\), the first marker, are exactly \(\{p,z\}\) with \(z\) in the following disjoint cases:

- If \(b>a\) and \(c\le b\), \(z\in[q-a-1,q-1]\).
- If \(b\le a\), \(c>b\) and \(c\ge a\), \(z\in[q+1,q+b+1]\).
- If \(b\le a\) and \(c\le b\), \(z\in Z_M\).
- In all other cases there are none.

Every listed interval consists of zero positions in a longest run, so no further restrictions are implicit. The pairs containing \(q\) are exactly the reversals of the above pairs for \(W_{c,b,a}\): replace \((a,b,c)\) by \((c,b,a)\) in the list, then reflect each position \(i\) to \(n-1-i\). The two lists are disjoint because exactly one marker must be selected.

## Proof

**Lower bound and shape of every pair.** Both one-letter factors \(0\) and \(1\) occur and cannot be attracted by the same position. Thus at least two positions are needed. In any two-position attractor, one position must be a marker (because the factor \(1\) has only singleton occurrences at \(p\) and \(q\)), and the other must be a zero. The longest pure-zero factor is \(0^M\). Its occurrences lie precisely in the zero runs of maximum length \(M\); therefore the selected zero must belong to \(Z_M\). Conversely, one position anywhere in a length-\(M\) zero run attracts every pure-zero factor \(0^h\) with \(1\le h\le M\): there is a length-\(h\) interval of that run containing the selected position.

**All remaining factors reduce to one-marker rectangles.** Every factor involving both ones crosses both markers, so any pair containing either marker attracts it. A factor involving exactly one one is \(0^i1\,0^j\), with nonnegative \(i,j\). It occurs around the first marker precisely when \(0\le i\le a\) and \(0\le j\le b\); it occurs around the second marker precisely when \(0\le i\le b\) and \(0\le j\le c\). Thus, for a pair containing \(p\), only the factors in the second rectangle \([0,b]\times[0,c]\) but outside the first rectangle \([0,a]\times[0,b]\) remain to be covered. Each such factor has its only one-marker occurrence crossing \(q\). It must instead cross the selected zero \(z\).

**Diagnostic interval intersection.** If \(b>a\), the second-only factor \(0^{a+1}1\) has occurrence interval \([q-a-1,q]\). Every other second-only factor with \(i>a\) contains this interval within its occurrence, so the necessary and sufficient common restriction from all left-excess factors is \(q-a-1\le z\le q\). If \(c>b\), the second-only factor \(1\,0^{b+1}\) has interval \([q,q+b+1]\), and the analogous common restriction from right-excess factors is \(q\le z\le q+b+1\). The selected zero cannot be at \(q\). If both excess inequalities hold, their intersection contains no zero. If neither holds, the second rectangle lies inside the first and there is no one-marker restriction on \(z\). When exactly one holds, intersect its diagnostic interval with \(Z_M\). This gives precisely the four cases in the pair description: \(a+1\) interior zero positions for the left-excess case; \(b+1\) right-run zero positions when \(c\ge a\) for the right-excess case; and all positions of \(Z_M\) when neither excess occurs. The latter has \(a+b\mathbf1_{a=b}+c\mathbf1_{a=c}\) positions because \(a\ge b\ge c\).

Every factor has been covered, proving that the listed pairs are attractors and that no other pair containing \(p\) qualifies. Reversal preserves factor occurrences and interval intersections, so the other marker contributes \(F(c,b,a)\) pairs. In every positive triple at least one of the displayed families is nonempty (consider the position of the largest of \(a,b,c\)); hence a two-position attractor exists. The lower bound makes every such pair minimum, proving the classification and count.

**Sharp resonance.** There are \(a+b+c\) zero positions, and a two-position attractor must consist of exactly one of these and one of the two markers. Therefore \(K\le2(a+b+c)\). When \(a=b=c=t\), the two one-marker occurrence rectangles coincide and every zero position works with either marker, giving \(K=6t\). Conversely, if every marker-zero pair were an attractor, the first-marker choice must cover every one-marker factor of the second marker without a restriction on its zero position, forcing the second rectangle to be contained in the first. The reversed choice forces the reverse containment, hence \(a=b=c\). For \(a=c=t\ne b\), substituting in the proven piecewise formula gives \(2(\min(b,t)+1)\).

**Simplex limit and mean.** Uniform positive compositions of \(n-2\) into three parts, divided by \(n\), converge to the uniform simplex law. Off the equality planes \(a=b\), \(b=c\), and \(a=c\), the exact count simplifies: if the middle zero gap is strictly largest, \(K=a+c+2\); if it is strictly intermediate, \(K=\max(a,c)\); if it is strictly smallest, \(K=b+1\). This proves the stated distributional limit \(\Phi\). Since \(0\le K\le2(n-2)\), expectations converge as well.

By permutation symmetry, \(Y\) is equally likely to be largest, intermediate, or smallest. For a uniform simplex triple, the expected maximum component is \(11/18\) and expected minimum is \(1/9\) (the latter follows by integrating \(\Pr[\min(X,Y,Z)>u]=(1-3u)^2\) on \([0,1/3]\); the former follows by simplex inclusion-exclusion or the standard three-uniform-spacing calculation). Consequently
\[
\mathbb E\Phi=\frac13\left[(1-11/18)+(11/18)+(1/9)\right]=\frac{10}{27}.
\]
This completes the infinite-parameter and asymptotic proofs.

## Verification

The standalone program `verify_pairs.py` exhaustively reconstructs all distinct factors and all their occurrence-position masks, tests every pair of positions, and compares the resulting number against \(F(a,b,c)+F(c,b,a)\) for all \(1\le a,b,c\le10\). It reports 1000 exhaustive triples. The independent program `verify_intervals.py` constructs both proposed position families by intersecting run positions with the diagnostic intervals, checks literal factor coverage for every proposed pair in the 512 triples with \(1\le a,b,c\le8\) (4220 pairs), and evaluates all positive-run composition sums through total zero length 110. Both programs use only the Python standard library. Execute `python3 verify_pairs.py` and `python3 verify_intervals.py` in the directory containing these documents. Their exact recorded outputs are included. Finite checks corroborate but cannot replace the preceding all-parameter argument.

## Relationship to prior work

Banbara et al. (arXiv:2602.16152, first public version February 18, 2026) explicitly classify *all* smallest attractor position sets for Fibonacci, period-doubling and later Thue–Morse finite words, motivating the multiplicity invariant, but those morphic word families and their proofs do not imply the three-gap two-marker formula here. Mantaci et al. (2021), notably their Example 24 and surrounding discussion, give families having two-position attractors and pose the general binary size-two characterization; they do not present the present entire three-gap pair classification. Published results for three- and four-run binary words have different run patterns; a five-run family with a single outer zero and a singleton second one determines a four-position regime elsewhere in parameter space, without enumerating these minimum pairs. Earlier classifications of the minimum *size* for symmetric five-run palindromes cover the \(a=c\) subfamily when the one runs are singletons, but do not give this pair-count law or its simplex mean. Related truncated two-attractor results concern factors of length at most two rather than all factors. None of those statements yields the complete unrestricted positive-three-gap optimum-pair classification by direct implication.

## Limitations

Only binary words with exactly two isolated ones and positive zero gaps at both ends are classified; adjacent markers, empty outer gaps, arbitrary weights, and circular attractors are not covered. The mean is conditional on a uniform positive three-part composition, not on uniformly sampled binary length-\(n\) strings. The distributional limit is weak convergence; the equality-plane anomalies do not persist at positive probability in that limit. Finite experiments are supplementary to the proof. An earlier unindexed equivalent classification remains a priority risk. No independent scientific validation is claimed.

## References

1. M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno, Y. Okamoto, *The Smallest String Attractors of Fibonacci and Period-Doubling Words*, arXiv:2602.16152 (v1 submitted 2026-02-18; later expanded with Thue–Morse), https://arxiv.org/abs/2602.16152 and https://arxiv.org/html/2602.16152.
2. S. Mantaci, A. Restivo, G. Romana, G. Rosone, M. Sciortino, *A Combinatorial View on String Attractors*, Theoretical Computer Science 850 (2021) 236–248, https://pages.di.unipi.it/rosone/Papers/MRRRS_TCS2021.pdf, especially Example 24.
3. D. Kempa, A. Policriti, N. Prezza, E. Rotenberg, *String Attractors: Verification and Optimization*, ESA 2018, arXiv:1803.01695.
4. *All minimum string attractors of three-run binary words and the mean–typical gap*, published-finding corpus publication (2026-10-26), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-all-minimum-string-attractors-of-three-run-binary-words-and-the--671c96898290.
5. *Sharp size-two string-attractor phase diagram for four-run binary words*, published-finding corpus publication (2026-11-01), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-size-two-string-attractor-phase-diagram-for-four-run-binar--0020a8b06c9c.
6. *Sharp four-position attractor criterion for a five-run binary family*, published-finding corpus publication (2026-10-25), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-four-position-attractor-criterion-for-a-five-run-binary-fa--199f2b51eb0f.
