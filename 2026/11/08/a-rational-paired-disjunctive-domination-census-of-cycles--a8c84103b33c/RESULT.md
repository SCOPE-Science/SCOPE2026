# A rational paired-disjunctive domination census of cycles

## Finding

For each integer \(n\ge3\), let \(C_n\) be the simple cycle on the labeled vertex set \(\mathbb Z/n\mathbb Z\). A subset \(S\subseteq V(C_n)\) is **paired-disjunctive dominating** if every vertex outside \(S\) either has a neighbor in \(S\) or has two distinct vertices of \(S\) at graph distance exactly two, and the induced graph \(C_n[S]\) has a perfect matching. Write
\[
P_n(z)=\sum_{S\text{ paired-disjunctive dominating}}z^{|S|}.
\]

**Complete structural classification.** Either \(S=V(C_n)\) and \(n\) is even, or the cyclic indicator word of \(S\) consists of alternating runs
\[
1^{2a_1}0^{b_1}\cdots1^{2a_s}0^{b_s},\qquad
s\ge1,\quad a_i\ge1,\quad 1\le b_i\le3.
\]
The word is interpreted cyclically, with a fixed vertex labeling; no quotient by rotation is taken in \(P_n\).

**Exact coefficients.** With \(k\ge1\) and \(B=n-2k\),
\[
[z^{2k}]P_n(z)=\mathbf1_{\{n=2k\}}+
\sum_{s=1}^{k}\frac ns\binom{k-1}{s-1}
[u^{B}](u+u^2+u^3)^s,
\]
where coefficient extraction of a negative exponent or an infeasible index means zero. All odd powers of \(z\) have zero coefficient. In particular, the entire ordinary bivariate generating function is rational:
\[
\boxed{\displaystyle
\sum_{n\ge3}P_n(z)x^n=
\frac{z^2(2x^2+3x^3+4x^4+5x^5)}{1-z^2(x^2+x^3+x^4+x^5)}
-\frac{z^2x^2}{1-z^2x^2}-z^2x^2.}
\]

**Cardinality support and extremal multiplicities.** The positive cardinalities represented by \(P_n\) are exactly the even integers in
\[
\left[\,2\left\lceil n/5\right\rceil,\;2\left\lfloor n/2\right\rfloor\,\right].
\]
The lower endpoint \(2\lceil n/5\rceil\) was previously known as the paired-disjunctive domination number; the complete distribution and the following multiplicities are the refinements here. Put \(k=\lceil n/5\rceil\) and \(d=5k-n\in\{0,1,2,3,4\}\). The number \(N_n\) of minimum-cardinality sets is
\[
\boxed{\displaystyle
N_n=\begin{cases}
5,&d=0,\\
n,&d=1,\\
n(k+1)/2,&d=2,\\
n(k+1)(k+2)/6,&d=3,\\
n(k-1)(k^2+7k+18)/24,&d=4.
\end{cases}}
\]
For odd \(n\), the leading coefficient is \([z^{n-1}]P_n(z)=n\), and for odd \(n\ge5\) the next is \([z^{n-3}]P_n(z)=n(n^2-1)/24\). For even \(n\), the leading coefficient is \([z^n]P_n(z)=1\), and for even \(n\ge4\), \([z^{n-2}]P_n(z)=n^2/4\).

**Total-count asymptotic.** Let \(\rho\in(0,1)\) be the unique positive root of \(\rho^2+\rho^3+\rho^4+\rho^5=1\), numerically \(\rho\approx0.651823453823\). Then
\[
\boxed{P_n(1)\sim\rho^{-n}\quad(n\longrightarrow\infty).}
\]
The leading multiplicative constant is exactly one.

## Assumptions and scope

All cycles are finite, simple, unweighted graphs, but vertex subsets are counted on the fixed labeled vertex set \(\mathbb Z/n\mathbb Z\); in particular, rotationally equivalent sets are different unless identical as subsets. Distances are taken in the full graph \(C_n\), not in its selected induced subgraph. A perfect matching is a set of pairwise disjoint edges covering every selected vertex. Domination conditions apply to vertices outside the selected set. The empty selected set is not feasible. All identities hold for every integer \(n\ge3\), including triangles and four-cycles.

## Proof

**Step 1: matchings and cyclic one-runs.** If \(S\ne V(C_n)\) and \(S\ne\varnothing\), each connected component of \(C_n[S]\) is a path given by one maximal cyclic run of selected vertices. A finite path has a perfect matching if and only if its number of vertices is even: consecutive vertices pair from an endpoint, and odd order is impossible by parity. Thus every one-run has length \(2a_i\) with \(a_i\ge1\). If \(S=V(C_n)\), the selected graph is a cycle and has a perfect matching precisely for even \(n\).

**Step 2: domination and zero-runs.** For a zero-run of length one or two, every omitted vertex is adjacent to an endpoint in \(S\). For length three, its middle vertex has two distinct selected endpoints at graph distance two, and the other omitted vertices have selected neighbors. For a zero-run of length at least four, its second zero has two zero neighbors and at most one selected vertex at distance two, so disjunctive domination fails. These arguments also cover the small simple cycles because an even one-run leaves no permissible problematic all-zero boundary. Therefore all zero-runs have lengths in \(\{1,2,3\}\), and conversely this condition together with even one-runs suffices. This proves the structural classification.

**Step 3: labeled enumeration.** For a proper feasible set with \(s\) selected runs, write their half-lengths \(a_1,\ldots,a_s\) and intervening zero-lengths \(b_1,\ldots,b_s\). Given \(2k\) selected vertices, \(\sum a_i=k\), counted by \(\binom{k-1}{s-1}\). The zero-length compositions are counted by \([u^{n-2k}](u+u^2+u^3)^s\). To place a designated beginning of a run on the labeled cycle, there are \(n\) choices, and each selected set is represented by exactly \(s\) designated run beginnings. This gives the displayed \(n/s\) coefficient formula, adding the full cycle once when \(n\) is even.

**Step 4: rational generating function.** A run pair has bivariate weight
\[
W(x,z)=\frac{z^2x^2}{1-z^2x^2}(x+x^2+x^3).
\]
The proper-set contribution on cycles of order \(n\) is \(n[x^n]\sum_{s\ge1}W(x,z)^s/s\). Hence its ordinary generating function is \(x\,\frac{d}{dx}\log(1/(1-W(x,z)))\). Adding the full-cycle contribution \(z^2x^2/(1-z^2x^2)\) and removing the formal order-two term \(z^2x^2\) yields precisely the displayed rational function after differentiating and simplifying.

**Step 5: support and five-residue minimum count.** The run sum gives \(n=2k+\sum b_i\le2k+3s\le5k\) for any proper feasible set of size \(2k\). Conversely, for any \(k\ge\lceil n/5\rceil\) with \(2k<n\), put \(B=n-2k\). If \(B\le k\), choose \(s=B\) zero-runs of length one and distribute \(k\) positive units among the \(s\) one-runs. If \(B\ge k\), choose \(s=k\) one-runs of length two and distribute \(B\) zero vertices among \(k\) gaps of lengths one through three; this is possible since \(k\le B\le3k\). For even \(n\), the full cycle supplies the final endpoint. Hence every even size in the displayed interval occurs.

For minimum size put \(k=\lceil n/5\rceil\), \(d=5k-n\in\{0,1,2,3,4\}\). Each set with \(s\) runs has a deficit identity
\[
d=3(k-s)+\sum_{i=1}^{s}(3-b_i).
\]
Since \(d\le4\), one has \(s=k\) or \(s=k-1\). The former contributes \(\frac nk[u^d](1+u+u^2)^k\). The latter, possible only for \(d\ge3\), has exactly one doubled half-length and contributes \(n[u^{d-3}](1+u+u^2)^{k-1}\). Evaluating the coefficients for \(d=0,1,2,3,4\) gives the five displayed cases. For the high-degree coefficients, count zero-runs of total size one, two, or three in the same run formula; direct substitution produces the asserted closed expressions.

**Step 6: asymptotic.** At \(z=1\), put \(B(x)=x^2+x^3+x^4+x^5\). The rational generating function becomes
\[
\frac{xB'(x)}{1-B(x)}-\frac{x^2}{1-x^2}-x^2.
\]
The unique real root \(\rho\in(0,1)\) of \(B(\rho)=1\) is a simple pole. If \(|x|=\rho\), the triangle inequality gives \(|B(x)|\le B(\rho)=1\). Equality with \(B(x)=1\) forces the phases of \(x^2,x^3,x^4,x^5\) to agree; since both exponents two and three occur, \(x=\rho\). There are therefore no other singularities of the same smallest modulus. Near \(\rho\), the first fraction is \((1-x/\rho)^{-1}\) plus a function analytic there. The remaining fractions are analytic at \(\rho\). Standard coefficient extraction from the isolated simple dominant pole yields \(P_n(1)\sim\rho^{-n}\) with leading constant one.

## Verification

The supplied standalone script `verify.py` builds each cycle as an adjacency list, obtains shortest-path distances by graph traversal, and tests every nonempty vertex subset for the original domination condition and a perfect matching through a generic recursive matching test. No cyclic-run condition enters this graph-level decision procedure. It separately constructs the rational coefficient table using the recurrence for the denominator \(1-z^2(x^2+x^3+x^4+x^5)\), and then compares the full cardinality distributions. It also tests the five-residue minimum multiplicities, consecutive even-size support, and leading two coefficients by exact arithmetic through order 250.

Execution on the packaged script:

```text
VERIFY_OK graph_orders=3..17 candidate_nonempty_subsets=262121 paired_disjunctive_sets=4136 rational_coefficients_orders=3..250 minimum_residue=PASS support=PASS leading_coefficients=PASS
```

In particular, \(P_8(z)=12z^4+16z^6+z^8\) and \(P_{10}(z)=5z^4+40z^6+25z^8+z^{10}\). Finite verification is supporting evidence, not an unrestricted proof; the unrestricted proof appears above.

## Relationship to prior work

Henning, Pandey, and Tripathi introduced and studied paired-disjunctive domination and determined the minimum cardinality for cycles; the reported value \(2\lceil n/5\rceil\) is not claimed as new here. Their accessible abstract concerns optimization and algorithms. The complete cardinality polynomial, five-residue minimum-set multiplicities, leading coefficients, and total-count asymptotic are the distinct claims here. Related work on ordinary paired domination concerns a stronger, different neighborhood condition, and cannot by itself imply these disjunctive counts. Search comparisons did not identify an equivalent census. The full text of the closest 2023 paper was not accessible, so publication priority remains provisional rather than definitively established.

## Limitations

The counting is for labeled vertex subsets of simple cycles only, and does not count perfect matchings separately when a selected induced subgraph has more than one. The exact polynomial counts **all** paired-disjunctive dominating sets; it is not the polynomial of inclusion-minimal sets. Independent mathematical validation has not been performed. The closest original full paper was not available for line-by-line comparison and could contain related enumerative observations not apparent in its abstract; this is a residual originality risk.

## References

1. M. A. Henning, A. Pandey, and V. Tripathi, *Algorithmic aspects of paired disjunctive domination in graphs*, Theoretical Computer Science 966–967 (2023), 113990, DOI: 10.1016/j.tcs.2023.113990. An earlier version was posted on SSRN September 3, 2022 (DOI: 10.2139/ssrn.4209056).
2. *A Novel Bondage Parameter for Network Analysis*, Symmetry 17 (2025), 1170, Section 2, Theorem 1 (quotes the previously known cycle minimum-cardinality formula); DOI: 10.3390/sym17081170.
3. H. Jiang, P. Wu, J. Zhang, and Y. Rao, *Upper paired domination in graphs*, AIMS Mathematics 7 (2022), 1185–1197; DOI: 10.3934/math.2022069. This treats ordinary paired domination rather than the disjunctive variant.
