# Exact degree spectrum of homopolymer-free words under admissible adjacent swaps

## Finding

**Theorem (complete all-length constrained-swap spectrum).** Fix an integer alphabet size \(q\ge3\) and a length \(n\ge3\). Let \(\mathcal P_{q,n}\) be the words \(x=x_1\cdots x_n\) over a labeled \(q\)-symbol alphabet with \(x_i\ne x_{i+1}\) for all \(1\le i<n\). An *admissible adjacent swap* interchanges two consecutive letters, and its output must also belong to \(\mathcal P_{q,n}\). Write \(s(x)\) for the number of **distinct nonidentity outputs** after one such swap.

Put \(a=q-2\). The complete enumerator, including the number of words of each attainable degree, is

\[
H_{q,n}(t)=\sum_{x\in\mathcal P_{q,n}}t^{s(x)}
=q(q-1)\,(1,at)
\begin{pmatrix}1&a\\1&at\end{pmatrix}^{n-3}
\begin{pmatrix}1\\t\end{pmatrix}.
\tag{1}
\]

Equivalently, its **rational all-length generating series** is

\[
\sum_{n\ge3}\frac{H_{q,n}(t)}{q(q-1)}u^{n-2}
=\frac{u\,[1+at^2+aut(1-t)]}{1-(1+at)u+a(t-1)u^2}.
\tag{2}
\]

The exact degree support is

\[
\{s(x):x\in\mathcal P_{q,n}\}=\{0,1,\ldots,n-3,n-1\};
\tag{3}
\]

**the penultimate degree \(n-2\) is impossible**, but every other integer between zero and the maximum occurs. Exactly \(q(q-1)(q-2)^{n-2}\) labeled words have maximum degree \(n-1\). Exactly \(q(q-1)\) words are isolated at \(n=3\). For \(n\ge4\), the number of isolated words is

\[
q(q-1)I_{n-4}(q-2),\qquad
I_0(z)=1,\quad I_1(z)=1+z,\quad I_m(z)=I_{m-1}(z)+zI_{m-2}(z)\quad(m\ge2).
\tag{4}
\]

For a uniformly chosen proper word and \(p=(q-2)/(q-1)\), the degree has exact mean
\[
\mathbb E[s]=2p+(n-3)p^2,
\tag{5}
\]
with variance \(4p(1-p)\) at \(n=3\), and, for \(n\ge4\),
\[
\operatorname{Var}(s)=2p(1-p)+(n-3)p^2(1-p^2)
+2(n-4)p^3(1-p)+4p^2(1-p).
\tag{6}
\]
The associated undirected graph has \(q(q-1)^{n-1}\) vertices and exactly
\[
\frac{q(q-1)^{n-1}}2\bigl[2p+(n-3)p^2\bigr]
\tag{7}
\]
edges. The closed radius-one constrained error ball about \(x\) has size \(1+s(x)\); no claim about multi-swap distance or optimal error-correcting code capacity is made.

## Assumptions and scope

The symbols are labeled and distinct. Words are **linear, indexed**, not circular and not identified under relabeling, rotation, reverse complement, or strand reversal. Both source and output are required to have no equal adjacent symbols. Only one swap of **neighboring unequal symbols** is allowed. In a proper word all neighboring symbols are already unequal. Two different swap locations yield two different nonidentity output words. The reported degree is the graph degree, not the number of possible swap histories with repeated outputs. Parameter ranges for (1)–(7) are as explicitly stated; in particular \(q=2\) is not covered by the support characterization.

## Proof

**Local characterization.** Set \(L=n-2\), and define \(Y_i=\mathbf1\{x_i\ne x_{i+2}\}\) for \(1\le i\le L\). Since \(x\) is proper, swapping positions \(j,j+1\) automatically preserves their mutual inequality. For \(j=1\) the only new adjacency constraint is \(x_1\ne x_3\), so the swap is admissible exactly when \(Y_1=1\). Similarly the last swap is admissible exactly when \(Y_L=1\). For an internal swap \(2\le j\le n-2\), the newly created neighboring comparisons are \(x_{j-1}\ne x_{j+1}\) and \(x_j\ne x_{j+2}\), precisely \(Y_{j-1}=Y_j=1\). Therefore the degree has the **exact center-specific formula**
\[
s(x)=Y_1+Y_L+\sum_{i=1}^{L-1}Y_iY_{i+1}.
\tag{8}
\]
No two different locations can have the same result because the two modified coordinates of each nonidentity swap uniquely identify its location.

**Multiplicity and probabilistic independence.** Fix any binary word \((y_1,\ldots,y_L)\). First select \(x_1\) in \(q\) ways and \(x_2\ne x_1\) in \(q-1\) ways. Having chosen consecutive unequal letters, choosing \(x_{i+2}=x_i\) enforces \(Y_i=0\) and has exactly one choice; choosing \(x_{i+2}\ne x_i,x_{i+1}\) enforces \(Y_i=1\) and has exactly \(q-2=a\) choices. Thus the number of words realizing binary profile \(y\) is exactly
\[
q(q-1)a^{\sum_i y_i}.
\tag{9}
\]
Since \(|\mathcal P_{q,n}|=q(q-1)^{n-1}\), under the uniform proper-word law the \(Y_i\) are independent Bernoulli variables of parameter \(p=a/(a+1)\). This independence holds **despite** the dependence of the original letters.

**Matrix and rational series.** Weight a profile by \(a^{\sum_i y_i}t^{y_1+y_L+\sum y_i y_{i+1}}\). The initial-state weights are \((1,at)\): a one pays both its multiplicity \(a\) and the left-end contribution. The transition from previous bit \(i\) to new bit \(j\) has weight \(a^j t^{ij}\), giving the matrix \(M=\left(\begin{smallmatrix}1&a\\1&at\end{smallmatrix}\right)\). The terminal weights \((1,t)^{\mathsf T}\) account for the right endpoint. There are \(L-1=n-3\) transitions, proving (1). Multiplying \(u(1,at)(I-uM)^{-1}(1,t)^{\mathsf T}\) and clearing its determinant proves (2), for formal indeterminates \(u,t\), including all boundary lengths.

**Gap, maxima and isolated centers.** The all-one profile has degree \(2+(L-1)=L+1=n-1\); equation (9) gives exactly \(q(q-1)a^L\) corresponding words. If a profile has a zero, at least two contributions to (8) disappear from the all-one maximum: a zero at an endpoint destroys that endpoint's term and its incident product, while an interior zero destroys its two incident products (the \(L=1\) case destroys both endpoint terms). Thus \(n-2\) is impossible. The zero profile has degree zero. For each \(1\le k\le L-1\), the profile \(1^k0^{L-k}\) has degree exactly \(k\). Because \(a\ge1\), every such profile is realized; hence (3) is exact. For \(L=1\) the zero profile is isolated. For \(L\ge2\), (8) vanishes precisely when both endpoint bits are zero and no two interior one-bits are adjacent. The weighted independence polynomial for a path with \(L-2=n-4\) vertices has recurrence in (4), proving the isolated count.

**Moments and edges.** From (8) and independent Bernoulli profile bits, there are two endpoint indicators, each of mean \(p\), and \(L-1=n-3\) adjacent-one products of mean \(p^2\), proving (5). At \(L=1\), \(s=2Y_1\), giving the stated variance. At \(L\ge2\), the endpoint indicators are distinct, each having variance \(p(1-p)\). Each adjacent product has variance \(p^2(1-p^2)\). Only overlapping adjacent products have nonzero covariance, namely \(p^3(1-p)\), with \(L-2=n-4\) such pairs. Each endpoint correlates with its neighboring product by \(p^2(1-p)\), giving two more covariance pairs. Summing variances and twice the covariances proves (6). Finally the degree sum equals twice the graph edge count; substituting (5) and the known vertex count gives (7).

## Verification

The included `checker.py`, using only Python's standard library, implements three separate counting routes: direct enumeration of admissible source words and explicit legal swaps, direct enumeration of all binary second-neighbor profiles using (8)–(9), and a polynomial dynamic program independently applying the weighted transfer transitions. All three degree histograms match for \(q=3\) and lengths \(3\)–\(9\), for \(q=4\) and lengths \(3\)–\(7\), and for \(q=5\) and lengths \(3\)–\(6\). It also checks every asserted spectrum support, total count, maximum multiplicity, and (4) when applicable. Run `python3 checker.py`; successful completion ends with `ALL_CHECKS_PASSED`. A separate symbolic rational-matrix calculation checks (2). These exhaustive **finite checks** corroborate the proof; they are not extrapolated into an infinite proof.

## Relationship to prior work

Gabrys, Guruswami, Ribeiro and Wu (arXiv:2112.09971, first submitted 2021-12-18) study near-optimal codes for deletion/edit and transposition error models, including binary codes correcting either a deletion or an adjacent transposition. Their code redundancy assertions do not provide an exact one-swap **restricted-output** neighbor-degree distribution over all proper nonbinary source words. Li, Chen and Wu (2022) study DNA code constructions with homopolymer and GC constraints; their construction results likewise do not state the complete legal-swap degree polynomial. The graph/reconfiguration comparison *Median swap graphs for binary words with bounded monochromatic runs* concerns binary fixed-weight run-constrained words, and gives medianity/geodesic structure in a different parameter regime, not the distribution (1). The published published-finding corpus finding *Sharp sphere volumes and extremizers for one permutation burst* counts outputs without requiring that the resulting word remain homopolymer-free, and its universal unrestricted-output formula does not imply the present constraint-conditioned degree polynomial. The finite DNA four-mer adjacent-swap capacity finding adds GC and complement restrictions and computes maximum codebook sizes rather than the graph degree spectrum.

These are statement-level comparisons, not claims that a search proves novelty. Equivalent work might be described as proper-coloring Glauber/swap dynamics, reconfiguration of path colorings, constrained transposition channels, or weighted local pattern statistics. That historical-priority risk remains.

## Limitations

No optimal transposition-correcting code size, multi-swap ball distribution, graph diameter, biochemical strand performance, cyclic-word counterpart, or arbitrary forbidden-pattern generalization is established. The auxiliary polynomial \(I_m\) is a classical path independence polynomial, and the transfer-matrix technique is standard; the asserted contribution is their exact application to the simultaneously constrained source/output adjacent-transposition degree problem, particularly the complete spectrum and sharp support gap. The closest GC-constrained primary article was assessed using publicly accessible text and abstract rather than its complete publisher full text. Independent mathematical audit has not been performed.

## References

1. R. Gabrys, V. Guruswami, J. Ribeiro and K. Wu, *Beyond Single-Deletion Correcting Codes: Substitutions and Transpositions*, arXiv:2112.09971v1, publicly posted 2021-12-18, https://arxiv.org/abs/2112.09971.
2. X. Li, M. Chen and H. Wu, *Multiple errors correction for position-limited DNA sequences with GC balance and no homopolymer for DNA-based data storage*, Briefings in Bioinformatics, https://doi.org/10.1093/bib/bbac484, first online 2022-11-21.
3. *Median swap graphs for binary words with bounded monochromatic runs*, published published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-median-swap-graphs-for-binary-words-with-bounded-monochromatic-r--b743472fbcd0.
4. *Sharp sphere volumes and extremizers for one permutation burst*, published published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-sphere-volumes-and-extremizers-for-one-permutation-burst--6f89836efb99.
5. *Exact one-adjacent-swap capacity of GC-balanced reverse-complement DNA four-mers*, published published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-one-adjacent-swap-capacity-of-gc-balanced-reverse-compleme--70adcf8157b1.
