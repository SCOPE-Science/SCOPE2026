# Finite-parameter type spaces of the almost-sure metric theory are explicit unions of cubes

## Finding

Let \(T_{\mathrm{AS}}\) be the almost-sure theory of finite metric spaces of Goldbring, Hart and Kruckman, and let \(A\) be a finite parameter set of size \(m\) in a monster model of \(T_{\mathrm{AS}}\). For every \(n\geq 1\), the complete continuous-logic type space \(S_n(A)\) is a finite disjoint union of ordinary cubes.

For a type, collapse equal variables and mark every resulting equality class that is equal to a named parameter. If exactly \(k\) equality classes remain genuinely new, then the corresponding clopen piece of \(S_n(A)\) is homeomorphic to
\[
[1/2,1]^{\,mk+\binom{k}{2}}.
\]
The number of such pieces is
\[
N_{m,n,k}=\frac{1}{k!}\sum_{i=0}^k(-1)^i\binom{k}{i}(m+k-i)^n
=\sum_{j=0}^{\min(m,n-k)} {n\brace j+k}\binom{j+k}{j}(m)_j.
\]
Consequently the total number of connected components is
\[
C_{m,n}=\sum_{k=0}^nN_{m,n,k}
       =\sum_{q=0}^n\binom nq m^{n-q}B_q,
\]
with exponential generating function
\[
\sum_{n\geq0}C_{m,n}\frac{z^n}{n!}=\exp(mz+e^z-1).
\]
Its covering dimension is exactly
\[
\dim S_n(A)=mn+\binom n2.
\]
In particular,
\[
S_1(A)\cong A_{\mathrm{disc}}\ \sqcup\ [1/2,1]^m,
\]
so \(S_1(A)\) has \(m+1\) connected components and dimension \(m\).

## Assumptions and scope

Type spaces are taken in the standard continuous-logic sense, with the logic topology, over a finite parameter set \(A\) inside a sufficiently saturated monster model of \(T_{\mathrm{AS}}\). The result uses the corrected almost-sure theory from arXiv:1911.01260, not the Urysohn-sphere theory discussed as the failed earlier candidate in that paper.

Goldbring--Hart--Kruckman define \(T_{\mathrm{AS}}\) so that distinct points have distances in \([1/2,1]\), and prove that it eliminates quantifiers and is the model completion of the universal theory imposing that distance gap. No assumption is made about the particular metric induced on \(A\) beyond what the theory already requires.

The component count uses the conventions \(B_q\) for the Bell numbers, \({n\brace r}\) for Stirling numbers of the second kind, and \((m)_j=m(m-1)\cdots(m-j+1)\). For the component formula with \(m=0\), the usual convention \(0^0=1\) is used.

## Proof

The source observes that once every nonzero distance lies in \([1/2,1]\), all triangle inequalities are automatic: the largest side is at most \(1\), while the sum of the other two nonzero sides is at least \(1\). It also proves quantifier elimination for \(T_{\mathrm{AS}}\) and identifies it as the model completion of the theory asserting the same distance gap.

Fix a complete \(n\)-type \(p\) over \(A\). The atomic equalities determine a finite pattern: variables are partitioned into equality classes, some classes are identified with distinct members of \(A\), and the remaining \(k\) classes represent distinct elements outside \(A\). Because distances are either \(0\) or at least \(1/2\), each fixed equality/parameter-identification pattern is clopen in \(S_n(A)\).

Once the pattern is fixed, all distances involving only old parameters are already fixed. The free coordinates are exactly the \(mk\) distances from the \(k\) new classes to the \(m\) parameters and the \(\binom{k}{2}\) distances among the new classes. Every one of these coordinates can be chosen independently anywhere in \([1/2,1]\): all triangles, including triangles containing one or two parameters, automatically satisfy the triangle inequality. The resulting finite metric extension is a model of the universal distance-gap theory, hence is consistent with \(T_{\mathrm{AS}}\) by model completion. Quantifier elimination says that these atomic distances determine the complete type.

Therefore the coordinate map from a fixed pattern to \([1/2,1]^{mk+\binom{k}{2}}\) is a continuous bijection. The pattern piece is compact and the cube is Hausdorff, so the map is a homeomorphism. Each cube is connected, and distinct patterns are separated by clopen conditions, hence these pieces are exactly the connected components.

To count the pieces with \(k\) new classes, temporarily label those classes. A function from the \(n\) variable positions to the \(m\) named parameters plus the \(k\) temporary new labels represents a pattern precisely when every new label is used. Inclusion--exclusion gives
\[
\sum_{i=0}^k(-1)^i\binom{k}{i}(m+k-i)^n.
\]
Dividing by \(k!\) forgets the temporary labels and gives the first formula for \(N_{m,n,k}\). Alternatively, if exactly \(j\) equality classes are identified with parameters, first partition the variables into \(j+k\) blocks, choose \(j\) of the blocks, and injectively label them by parameters, giving the Stirling form.

For the total component count, choose the \(q\) variable positions that belong to genuinely new classes, partition those positions arbitrarily, and send each remaining position independently to one of the \(m\) parameters. This gives
\[
C_{m,n}=\sum_{q=0}^n\binom nq m^{n-q}B_q.
\]
The displayed exponential generating function follows by multiplying the exponential generating functions for parameter-labeled singleton choices and set partitions. Finally, a finite disjoint union of cubes has covering dimension equal to the largest cube dimension, and the maximum occurs at \(k=n\), giving \(mn+\binom n2\).

## Verification

The bundled script `artifacts/verify.py` independently enumerates equality/parameter-identification patterns in restricted-growth form for parameter sizes \(0\leq m\leq3\) and arities \(1\leq n\leq6\). For every \((m,n,k)\), it compares the direct count with both closed formulas for \(N_{m,n,k}\), and compares the total with the Bell-convolution formula for \(C_{m,n}\). It also checks the claimed maximum cube dimension and tests the distance-gap triangle observation on a rational grid in \([1/2,1]\).

The replay prints `VERIFY_OK`. The computation checks the finite combinatorial identities only; the type-space homeomorphism and the infinite-theory consistency step are proved above from quantifier elimination and model completion.

## Relationship to prior work

Goldbring, Hart and Kruckman introduce \(T_{\mathrm{AS}}\), prove that all nontrivial distances in its models are at least \(1/2\), and prove quantifier elimination plus model completion. They also use the freedom to assign a new distance in \([1/2,1]\) when showing instability. Their paper does not state the finite-parameter type-space decomposition above, the cube dimensions, the connected-component formulas, or the exponential generating function.

General metric Fraisse theory and the model theory of the Urysohn sphere provide broad context for describing types via finite metric-extension data. Those frameworks do not, by themselves, yield this product-of-cubes decomposition: the simplification here comes from the special \([1/2,1]\) gap in \(T_{\mathrm{AS}}\), which removes every triangle-inequality coupling among the free distance coordinates.

Searches using the exact source title together with `type space`, `types`, `cube`, `S_n(A)`, and the component formulas found the primary paper and general Urysohn/Katetov background, but no prior statement of this decomposition or enumeration. The result should nevertheless be regarded as an explicit structural corollary of the source's quantifier-elimination/model-completion theorem rather than as an independent strengthening of that theorem.

## Limitations

The statement is only for finite parameter sets. For infinite parameter sets, distance coordinates need not reduce to a finite-dimensional cube and compactness/topology require a different analysis.

The result describes the logic topology and its finite-dimensional components; it does not compute the canonical type metric or claim bi-Lipschitz equivalence with a standard cube metric.

Because the proof is a short specialization of standard continuous-model-theoretic ideas, an unindexed folklore statement may exist even though targeted searches did not locate one.

## References

1. Isaac Goldbring, Bradd Hart, Alex Kruckman, *The almost sure theory of finite metric spaces*, arXiv:1911.01260; *Bulletin of the London Mathematical Society* 53 (2021), 1740--1748, DOI 10.1112/blms.12538.
2. Itaï Ben Yaacov, *Fraisse limits of metric structures*, arXiv:1203.4459.
3. Gabriel Conant, Caroline Terry, *Model theoretic properties of the Urysohn sphere*, arXiv:1401.2132.
