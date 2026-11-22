# The exact four-coordinate exchangeability reserve of a uniform perfect matching

## Finding

Fix an integer \(m\ge1\). Let \(R\) be uniformly distributed over the perfect matchings of \(2m\) labeled vertices, and fix a perfect matching \(H=\{e_1,\ldots,e_m\}\). Put \(X_i=\mathbf 1\{e_i\in R\}\). A finite sequence is exchangeable when its joint law is invariant under coordinate permutations; an exchangeable extension to length \(N\ge m\) is an exchangeable binary vector whose first \(m\) coordinates have exactly the law of \((X_1,\ldots,X_m)\).

**Theorem.** When \(m=1\) or \(m=2\), the vector admits exchangeable extensions of every length, including an infinite extension. For every \(m\ge3\), it has an exchangeable extension to length \(N\) **if and only if**
\[
 m\le N\le m+4.
\]
For every admissible \(N\), its exchangeable extension law is unique. In particular, the precise excess length is four, independently of \(m\).

Here is an explicit construction at the longest length \(N=m+4\). Set \(q=1/(2m-1)!!\), where \((2j-1)!!=1\cdot3\cdots(2j-1)\) and \((-1)!!=1\). Define
\[
 S_k=\sum_{j=0}^{k}(-1)^j\binom{k+4}{j}\bigl((2(k-j)-1)!!-1\bigr).
\]
Choose the total number \(T\) of ones in a length-\(N\) vector according to
\[
 \Pr(T=t)=\begin{cases}
 q\binom{N}{t}S_{m-t},&0\le t\le m-2,\\
 q,&t=N,\\
 0,&\text{otherwise}.
 \end{cases}
\]
Then conditionally on \(T\), choose the \(T\) positions of the ones uniformly. The coefficients are nonnegative, sum to one, and reproduce the required matching-indicator marginal. For example, at \(m=3\) the length-seven extension has \(\Pr(T=1)=14/15\) and \(\Pr(T=7)=1/15\).

## Assumptions and scope

The perfect matching \(H\) is deterministic and covers all \(2m\) distinct vertices; the random matching \(R\) is uniform over all \((2m-1)!!\) perfect matchings of the complete graph. No independence of the indicators is assumed. \(N\) is a positive integer with \(N\ge m\). The theorem concerns **binary exchangeability of the chosen edge indicators**, not exchangeability of random matchings themselves, and it makes no claim for nonuniform graph matching measures.

## Proof

**1. Exact matching moments.** For any \(r\) distinct designated edges, fixing them leaves a uniform matching on \(2(m-r)\) vertices. Thus
\[
 c_r:=\Pr(X_1=\cdots=X_r=1)
 =\frac{(2(m-r)-1)!!}{(2m-1)!!},\qquad 0\le r\le m.
\]
By symmetry these all-one moments determine the entire binary law by inclusion–exclusion. In particular \(c_{m-1}=c_m=q\), \(c_{m-2}=3q\), and \(c_{m-3}=15q\), whenever \(m\ge3\).

**2. Support rigidity and the upper bound.** For any exchangeable binary extension of length \(N\), write \(T\) for its total number of ones and \(p_t=\Pr(T=t)\). Sampling the first \(m\) positions is hypergeometric. Since \(c_{m-1}=c_m\),
\[
 0=\mathbb E\left[\frac{\binom T{m-1}}{\binom N{m-1}}
 -\frac{\binom Tm}{\binom Nm}\right]
 =\mathbb E\left[\frac{\binom T{m-1}(N-T)}{\binom N{m-1}(N-m+1)}\right].
\]
Every summand is nonnegative, so \(T\in\{0,1,\ldots,m-2,N\}\) almost surely, and \(p_N=q\). The next two moment equations are triangular and give
\[
 p_{m-2}=2q\binom N{m-2},\qquad
 p_{m-3}=2q\binom N{m-3}(m+4-N).
\]
As \(p_{m-3}\ge0\), necessarily \(N\le m+4\). Furthermore, the remaining moment equations determine \(p_{m-4},p_{m-5},\ldots,p_0\) successively, so **any** exchangeable extension law is unique at every allowable \(N\).

**3. Constructing the extremal extension.** At \(N=m+4\), define \(p_t\) as in the finding. The binomial-coefficient identity
\[
 \binom N r\binom r t=\binom N t\binom{N-t}{r-t}
\]
shows that the coefficient of \(z^t\) in
\[
 F(z)=q\sum_{r=0}^{m-2}\binom N r
 \bigl((2(m-r)-1)!!-1\bigr)(z-1)^r
\]
is exactly \(q\binom Nt S_{m-t}\) for \(0\le t\le m-2\). Thus the candidate probability generating function is \(P(z)=F(z)+qz^N\). Its binomial moments, obtained by differentiating at \(z=1\), equal \(\binom Nr c_r\) for all \(0\le r\le m\), including \(r=m-1,m\). In particular \(P(1)=1\). It remains to prove coefficient nonnegativity.

**4. Positivity lemma.** The defining sums satisfy
\[
 S_0=S_1=0,\quad S_2=2,\quad S_3=0,\quad S_4=48,
\]
and, for every \(k\ge2\), the exact recurrence
\[
 S_k=2(k-1)S_{k-1}+2(k+3)S_{k-2}
 +(-1)^k\frac{k(k-1)(k+1)}3.
\]
Here is a derivation rather than an experimental assertion. Let \(d_j=(2j-1)!!\) and introduce the formal series
\[
 D(x)=\sum_{j\ge0}\frac{d_jx^j}{(j+4)!},
 \quad U(x)=e^{-x}D(x).
\]
The recursion \(d_{j+1}=(2j+1)d_j\) gives the formal differential identity
\[
 x(1-2x)D'(x)+(4-x)D(x)=\frac16,
\]
hence
\[
 x(1-2x)U'(x)+(4-2x^2)U(x)=\frac{e^{-x}}6.
\]
The coefficient of \(x^k\) in \(U(x)\) is \(F_k/(k+4)!\), where
\(F_k=\sum_{j=0}^k(-1)^j\binom{k+4}j(2(k-j)-1)!!\). The subtracted constant transform is exactly
\(G_k=\sum_{j=0}^k(-1)^j\binom{k+4}j=(-1)^k\binom{k+3}3\), and \(S_k=F_k-G_k\). Coefficient comparison in the differential identity yields the displayed recurrence (including \(k=2\)).

Put \(b_k=k(k-1)(k+1)/3\). We have \(S_4=48\ge b_4=20\). For even \(k\ge4\), the recurrence and nonnegative preceding terms imply \(S_k\ge b_k>0\). For odd \(k\ge5\), the preceding even value satisfies \(S_{k-1}\ge b_{k-1}\), and
\[
 2(k-1)b_{k-1}\ge2b_k
 \quad\text{because}\quad(k-1)(k-2)\ge k+1.
\]
Thus \(S_k\ge b_k\) for odd \(k\ge5\), while \(S_3=0\). This proves \(S_k\ge0\) for every \(k\ge0\). Consequently \(P\) is a genuine probability generating function and achieves \(N=m+4\). Marginalizing its exchangeable law proves existence for every intermediate \(N\).

**5. Small cases.** When \(m=1\), the sole indicator equals one. When \(m=2\), the two indicators are equal, being simultaneously one with probability \(1/3\), so choose a Bernoulli\((1/3)\) variable and repeat it indefinitely. Conversely, \(m\ge3\) has the proved finite bound.

## Verification

The standalone Python program `checker.py` uses exact rational arithmetic. It compares the direct binomial sums with the recurrence through \(k=85\), tests nonnegative extremal probabilities and all \(m+1\) binomial moment identities for \(3\le m\le30\), checks the negative obstruction coefficient at \(N=m+5\), and independently enumerates every matching on up to twelve labeled vertices. It passed 1,258 exact assertions. These finite computations corroborate, but do not replace, the all-parameter proof above.

## Relationship to prior work

The fixed-pair moment formula is an immediate consequence of classical enumeration of perfect matchings. Finite exchangeability, urn decompositions and general extendibility criteria are developed by Janson–Konstantopoulos–Yuan (2014) and Konstantopoulos–Yuan (2015). Godsil–Meagher (2015) studies intersecting families and the matching derangement graph, using the same matching count but for a different extremal question. The claim here is the explicit, **unique, exact-length** extension law and sharp universal reserve of four positions for this particular random-matching marginal. Neither the general extendibility criterion nor the matching-intersection results directly state this specialization.

## Limitations

The theorem applies only to a uniform perfect matching and its designated pair-presence indicators. It does not establish a new general criterion for all finitely exchangeable Bernoulli laws or a result for arbitrary weighted matchings. Priority among older specialized sources, beyond the checked literature, remains open to independent verification. No independent mathematical audit has been performed.

## References

- S. Janson, T. Konstantopoulos and L. Yuan, *On a representation theorem for finitely exchangeable random vectors*, arXiv:1410.1777v1, publicly submitted 2014-10-07. https://arxiv.org/abs/1410.1777
- T. Konstantopoulos and L. Yuan, *On the extendibility of finitely exchangeable probability measures*, arXiv:1501.06188v1, publicly submitted 2015-01-25. https://arxiv.org/abs/1501.06188
- C. Godsil and K. Meagher, *An algebraic proof of the Erdős–Ko–Rado theorem for intersecting families of perfect matchings*, arXiv:1506.08770v1, publicly submitted 2015-06-29. https://arxiv.org/abs/1506.08770
