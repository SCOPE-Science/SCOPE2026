# A sharp fourth-cumulant transition for circular triads in uniform tournaments

## Finding

For every integer \(n\ge3\), orient each edge of the labeled complete graph on \(n\) vertices independently with probability \(1/2\) in either direction. Let \(C_n\) be the number of three-vertex sets whose edges form a directed cycle. With the fourth cumulant defined by

\[
\kappa_4(C_n)=\mathbb E[(C_n-\mathbb E C_n)^4]-3\operatorname{Var}(C_n)^2,
\]

the exact identity is

\[
\boxed{\kappa_4(C_n)=\frac{n(n-1)(n-2)(3n^2-30n+62)}{256}.}
\]

Consequently, \(\kappa_4(C_n)<0\) for \(3\le n\le7\), whereas \(\kappa_4(C_n)>0\) for every \(n\ge8\); it is never zero at an integer \(n\ge3\). The exact excess kurtosis is

\[
\frac{\kappa_4(C_n)}{\operatorname{Var}(C_n)^2}
=\frac{4(3n^2-30n+62)}{n(n-1)(n-2)}
\sim\frac{12}{n}.
\]

The mechanism is a signed line-graph identity: with \(A\) the signed adjacency matrix obtained by taking inner products of distinct oriented incidence columns of the complete graph, the sum over its unoriented simple four-cycles of the products of their four signed edge weights is exactly

\[
\boxed{\sum_{\gamma\in\mathcal C_4(A)}\prod_{e\in\gamma}A_e
=\frac{n(n-1)(n-2)(n-3)(n-7)}8.}
\]

## Assumptions and scope

The tournament has labeled vertex set \(\{1,\ldots,n\}\). Every one of its \(\binom n2\) orientation variables is an independent fair sign. A circular triad is a directed cycle of length three, counted once for each unordered triple, regardless of its clockwise orientation. The identity concerns all integers \(n\ge3\), without limiting assumptions, and is an exact population cumulant, not a sample estimator.

For an edge \(e=\{i,j\}\) with \(i<j\), fix an oriented incidence column \(b_e\) with \(+1\) at \(i\), \(-1\) at \(j\), and zeros elsewhere. Define \(B=[b_e]\), \(m=\binom n2\), and \(A=B^{\mathsf T}B-2I_m\). Its diagonal is zero and its nonzero off-diagonal entries are all \(+1\) or \(-1\). A simple four-cycle of this signed graph means four distinct edge-indices of the original complete graph connected cyclically by four nonzero off-diagonal entries of \(A\), counted once up to rotation and reversal.

## Proof

**1. Signed quadratic representation.** Give the fixed orientation of each edge an independent Rademacher sign \(X_e\). For each vertex \(v\), let \(S_v=(BX)_v\) be its signed score. On a triple \(a<b<c\), the quantity

\[
Y_{abc}=X_{ab}X_{ac}-X_{ab}X_{bc}+X_{ac}X_{bc}
\]

is \(+1\) for each of the six transitive orientations and \(-3\) for each of the two directed cycles. Hence the centered cyclic-triad indicator is \(-Y_{abc}/4\). Summing over triples and collecting the three products incident at each vertex gives

\[
C_n-\mathbb EC_n=-\frac14 Q_n,\qquad
Q_n=\sum_{e<f}A_{ef}X_eX_f
=\frac12\left(\sum_vS_v^2-n(n-1)\right).
\]

Here \(\mathbb E C_n=\binom n3/4\). The graph supporting \(A\) is the line graph of the complete graph. It has \(m=\binom n2\) vertices, each of degree \(d=2(n-2)\), and \(M=md/2=n(n-1)(n-2)/2\) edges. Orthogonality of distinct quadratic Rademacher monomials yields \(\mathbb EQ_n^2=M\), so \(\operatorname{Var}(C_n)=M/16=n(n-1)(n-2)/32\).

**2. General fourth-moment identity.** For any finite symmetric zero-diagonal matrix \(A\) with entries in \(\{0,+1,-1\}\), let \(Q=\sum_{i<j}A_{ij}X_iX_j\) and let \(M\) be the number of nonzero upper-triangle entries. The expectation of four edge monomials vanishes unless each coordinate sign appears an even number of times. The surviving four-edge multisets comprise four copies of one edge, two pairs of edges, or four distinct edges forming a simple four-cycle. Thus, writing \(S\) for the signed simple-four-cycle sum,

\[
\mathbb EQ^4=M+6\binom M2+24S=3M^2-2M+24S,
\qquad\boxed{\kappa_4(Q)=-2M+24S.}
\]

The expression for \(S\) is signed: negative cycle products are retained rather than discarded. For a \(d\)-regular signed adjacency matrix with all nonzero weights of magnitude one, classification of length-four closed walks gives

\[
\operatorname{tr}(A^4)=8S+2M+2m d(d-1).
\]

The terms respectively count simple four-cycles, twice-traversed edges, and the remaining backtracking walks.

**3. Exact trace by incidence spectrum.** For the complete-graph oriented incidence matrix,

\[
BB^{\mathsf T}=nI_n-J_n.
\]

Therefore \(A=B^{\mathsf T}B-2I_m\) has eigenvalue \(n-2\) with multiplicity \(n-1\), and eigenvalue \(-2\) with multiplicity \(m-n+1\). Consequently,

\[
\operatorname{tr}(A^4)
=(n-1)(n-2)^4+16(m-n+1)
=n(n-1)(n-2)(n^2-6n+12).
\]

Inserting this trace, \(d=2(n-2)\), and \(M=m(n-2)\) in the closed-walk identity yields the exact signed-cycle sum

\[
S=\frac{n(n-1)(n-2)(n-3)(n-7)}8.
\]

Substituting in the general cumulant formula and using the homogeneity of cumulants under scaling gives

\[
\begin{aligned}
\kappa_4(C_n)
&=\frac{\kappa_4(Q_n)}{4^4}
=\frac{-2M+24S}{256}\\
&=\frac{n(n-1)(n-2)\{3(n-3)(n-7)-1\}}{256}\\
&=\frac{n(n-1)(n-2)(3n^2-30n+62)}{256}.
\end{aligned}
\]

**4. Sharp sign boundary.** The quadratic \(p(n)=3n^2-30n+62\) equals \(-1\) at \(n=7\), \(+14\) at \(n=8\), and is strictly increasing on integers \(n\ge5\). Direct evaluation gives \(p(3),p(4),p(5),p(6)<0\). Its two real roots \((15\pm\sqrt{39})/3\) are not integers. This proves the claimed sign classification. Division by the square of the exact variance proves the excess-kurtosis identity and asymptotics.

## Verification

The self-contained standard-library script `VERIFY.py` performs exact independent checks: direct enumeration of all orientations for \(3\le n\le6\), explicit signed incidence/trace/four-cycle enumeration for \(3\le n\le9\), and integer sign checks through \(n=100\). The script completed with 156 exact assertions passing. Finite testing corroborates the result; the all-order proof is the incidence-spectrum and Rademacher-moment calculation above.

## Relationship to prior work

The independence-of-edge-orientations model and random-orientation correlations are developed in Narayanan (2016), which publicly appeared on September 5, 2016 and has primary classification 60C05. Circular-triad counting and its classical first and second moments belong to Kendall and Babington Smith (1940), and the random-tournament score identity is classical. Bruss and Ferguson (2018, especially Lemmas 2, 3, and 5) prove zero pairwise covariances, classify possible supports of three- and four-triangle mixed moments, and establish asymptotic normality; their inspected full text does not state the signed line-graph four-cycle sum, the exact all-order fourth cumulant here, or its sign threshold. Harris and McShane (2024) develop exact counting generating functions for fixed circular-triad numbers and review historical finite tables, rather than computing this full-size fourth-cumulant polynomial. The theorem does not claim novelty for the signed-score representation, variance, triangular-support restrictions, or central limit theorem.

## Limitations

The theorem holds only for independent unbiased orientations of a complete graph; neither unequal edge probabilities nor missing comparisons are covered. The earlier full text of Kendall and Babington Smith (1940) could not be accessed in this inspection, although its bibliographic record and summaries were checked. Consequently priority concerning possible implicit fourth-moment formulas in older paired-comparison treatments is not conclusively resolved. Numerical checks do not prove the formula outside tested sizes; the general proof is algebraic.

## References

1. B. Narayanan, *Connections in randomly oriented graphs*, arXiv:1609.01003 (first public September 5, 2016), https://arxiv.org/abs/1609.01003.
2. M. G. Kendall and B. Babington Smith, *On the Method of Paired Comparisons*, Biometrika **31** (1940), 324–345, https://doi.org/10.1093/biomet/31.3-4.324.
3. F. T. Bruss and T. S. Ferguson, *Testing equality of players in a round-robin tournament*, The Mathematical Scientist **43** (2018), 125–136, https://www.math.ucla.edu/~tom/papers/testing.pdf.
4. I. R. Harris and R. P. A. McShane, *Counting Tournaments with a Specified Number of Circular Triads*, Journal of Integer Sequences **27** (2024), Article 24.8.7, https://cs.uwaterloo.ca/journals/JIS/VOL27/McShane/mcshane1.pdf.
