# Forbidden-clique parameter from tuple-orbit entropy of generically ordered Henson graphs

## Finding
For each integer \(r\ge 3\), let \(M_r\) be the Fraïssé limit of the class of finite \(K_r\)-free graphs equipped with an arbitrary linear order. Let \(a_r(n)\) be the number of \(\operatorname{Aut}(M_r)\)-orbits on injective ordered \(n\)-tuples, and let \(f_r(n)\) be the number of labeled \(K_r\)-free graphs on vertex set \([n]\). Then
\[
a_r(n)=n!\,f_r(n).
\]
Consequently the quadratic tuple-orbit entropy exists and is
\[
\lambda_r:=\lim_{n\to\infty}\frac{\log_2 a_r(n)}{n^2}
=\frac{r-2}{2(r-1)}.
\]
The forbidden clique size is therefore recovered exactly from this single asymptotic group invariant:
\[
r=1+\frac{1}{1-2\lambda_r}.
\]
For the generically ordered random graph, with no finite clique forbidden, \(a_\infty(n)=n!2^{\binom n2}\) and the corresponding endpoint is \(\lambda_\infty=1/2\). Thus the Henson/random branch of the homogeneous ordered-graph catalog is strictly stratified by tuple-orbit entropy.

## Assumptions and scope
Here “generically ordered \(K_r\)-free graph” means the Fraïssé limit of all finite \(K_r\)-free graphs with an unrestricted added linear order. This avoids indexing conventions for the Henson graphs themselves. The orbit count is for injective ordered tuples; repeated-coordinate tuples are not needed for the entropy statement.

The model-theoretic input is homogeneity and universality of the generic ordered expansion. The enumerative input is the Erdős–Kleitman–Rothschild asymptotic count of labeled \(K_r\)-free graphs, together with Turán's theorem for \(\operatorname{ex}(n,K_r)\).

## Proof
Fix \(n\). An injective ordered tuple \((x_1,\ldots,x_n)\) induces two labeled structures on the coordinate set \([n]\): a \(K_r\)-free graph, and the restriction of the ambient linear order. There are \(f_r(n)\) possibilities for the first structure and exactly \(n!\) possibilities for the second.

Every such pair occurs because \(M_r\) is universal for finite ordered \(K_r\)-free graphs. Two injective tuples lie in the same automorphism orbit exactly when the coordinate-preserving map between them is an isomorphism of the induced ordered graphs; by homogeneity every such finite isomorphism extends to an automorphism. Hence
\[
a_r(n)=n!f_r(n).
\]

Erdős–Kleitman–Rothschild gives
\[
\log_2 f_r(n)=\operatorname{ex}(n,K_r)+o(n^2).
\]
Turán's theorem gives
\[
\operatorname{ex}(n,K_r)
=\frac{r-2}{2(r-1)}n^2+O(1).
\]
Since \(\log_2(n!)=o(n^2)\), division of \(\log_2 a_r(n)=\log_2(n!)+\log_2 f_r(n)\) by \(n^2\) proves
\[
\lambda_r=\frac{r-2}{2(r-1)}.
\]
Finally \(1-2\lambda_r=1/(r-1)\), yielding the recovery formula. The constants are strictly increasing in \(r\) and tend to \(1/2\), which agrees with the unrestricted random-graph branch.

## Verification
A standard-library verifier exhaustively enumerates labeled \(K_r\)-free graphs for small \(n\), checks the triangle-free counts
\[
1,1,2,7,41,388,5789\qquad(n=0,\ldots,6),
\]
and checks explicit graph/order encodings through \(n=4\). It also verifies symbolically, using exact rational arithmetic, that the entropy constants are strictly increasing for \(3\le r\le 30\) and that the inversion formula recovers each \(r\). The resulting injective orbit profile for the generically ordered triangle-free Henson graph begins
\[
1,4,42,984,46560,4168080\qquad(n=1,\ldots,6).
\]
The replay terminates with `VERIFY_OK`.

## Relationship to prior work
Cherlin's classification contains the generically ordered Henson graphs as a homogeneous ordered-graph family; that structural classification is prior work. Erdős–Kleitman–Rothschild's asymptotic enumeration of \(K_r\)-free labeled graphs and Turán's extremal theorem are also prior work and are not claimed here.

The contribution isolated here is the bridge from those two literatures: the exact injective tuple-orbit identity \(a_r(n)=n!f_r(n)\), followed by the observation that its quadratic entropy is a complete numerical fingerprint of the forbidden clique parameter throughout the Henson/random branch. Searches for equivalent formulations, Henson-specific orbit-growth formulas, and broader oligomorphic growth results did not locate this parameter-recovery statement. Braunfeld's work studies growth spectra of \(\omega\)-categorical structures in other regimes and does not supply this Henson-specific calculation in the inspected material.

## Limitations
The argument is short once the two standard inputs are placed together, so an unindexed folklore antecedent remains possible. The result concerns the generic ordered expansion; the unordered Henson graph has a different exact labeled-orbit count. The entropy only records the leading quadratic term, although in this family that leading term already determines \(r\). No claim is made here about finer lower-order asymptotics of \(f_r(n)\).

## References
1. Gregory Cherlin, *Homogeneous Ordered Graphs, Metrically Homogeneous Graphs, and Beyond, Volume I: Ordered Graphs and Distanced Graphs*, prepublication draft dated October 27, 2021; Cambridge University Press, 2022. DOI: 10.1017/9781009229661.
2. József Balogh, Felix Christian Clemen, and Letícia Mattos, *Counting r-graphs without forbidden configurations*, arXiv:2107.14798. Its abstract recalls the Erdős–Kleitman–Rothschild theorem that the number of labeled \(K_r\)-free graphs is \(2^{\operatorname{ex}(n,K_r)+o(n^2)}\).
3. Pál Turán, classical theorem determining \(\operatorname{ex}(n,K_r)\) via the balanced \((r-1)\)-partite Turán graph.
4. Samuel Braunfeld, *Monadic stability and growth rates of \(\omega\)-categorical structures*, Proc. London Math. Soc. 124 (2022), 373–386. DOI: 10.1112/plms.12429.
