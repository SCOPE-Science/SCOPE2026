# A vertex-boundary partition function for restrained Italian domination of leaf coronas

## Finding

Let \(H\) be a finite simple graph on \(n\ge1\) labeled vertices. Its *one-leaf corona* \(W(H)\) is obtained by adjoining a private leaf \(v'\) to each \(v\in V(H)\). A **restrained Italian dominating function** (RID function) is a map \(f:V(W(H))\to\{0,1,2\}\) such that (i) each zero-labeled vertex has neighbor-label sum at least two, and (ii) the graph induced by all zero-labeled vertices has no isolated vertices. An empty zero set is permitted. The weight is \(w(f)=\sum_x f(x)\).

For \(Z\subseteq V(H)\), say that \(Z\) is *admissible* if every \(v\in Z\) has a neighbor in \(Z\), and write
\[
 b_H(Z)=|\{v\in Z:N_H(v)\setminus Z\ne\varnothing\}|,\qquad
 \mathcal A(H)=\{Z\subseteq V(H):Z\text{ is admissible}\}.
\]
Thus \(\varnothing\in\mathcal A(H)\), and \(b_H(\varnothing)=0\). **Theorem:** the entire RID-function weight enumerator of the corona is
\[
 \boxed{\mathcal R_{W(H)}(z)=\sum_{Z\in\mathcal A(H)}z^{2n-b_H(Z)}(1+z)^{2(n-|Z|)+b_H(Z)}.}
\]
In particular, putting \(B(H)=\max_{Z\in\mathcal A(H)}b_H(Z)\),
\[
 \boxed{\gamma_{rI}(W(H))=2n-B(H),\qquad
 N_{\min}(W(H))=|\{Z\in\mathcal A(H):b_H(Z)=B(H)\}|.}
\]
Here \(N_{\min}\) counts actual vertex labelings, not symmetry classes. Every optimal labeling is uniquely determined by a maximizing set \(Z\).

For the *comb* \(W(P_n)\), for every \(n\ge1\),
\[
 \boxed{B(P_n)=\left\lfloor\frac{2n-2}{3}\right\rfloor,\qquad
 N_{\min}(W(P_n))=
 \begin{cases}
 2,&n\equiv0\pmod3,\\
 1,&n\equiv1\pmod3,\\
 2(n+1)/3,&n\equiv2\pmod3.
 \end{cases}}
\]
For the *sunlet* \(W(C_n)\), for every \(n\ge3\), set \(k=\lfloor n/3\rfloor\). Then
\[
 \boxed{B(C_n)=2k,\qquad
 N_{\min}(W(C_n))=
 \begin{cases}
 3,&n\equiv0\pmod3,\\
 2n,&n\equiv1\pmod3,\\
 n(2k+1),&n\equiv2\pmod3.
 \end{cases}}
\]
Thus \(\gamma_{rI}(W(P_n))=2n-\lfloor(2n-2)/3\rfloor\) and \(\gamma_{rI}(W(C_n))=2n-2\lfloor n/3\rfloor\). The optimum counts exhibit constant, linear, and quadratic growth in different residue classes.

## Assumptions and scope

All graphs are finite, simple, and undirected; isolated vertices and disconnected base graphs are allowed. A corona has exactly one new degree-one vertex per original vertex. The empty induced subgraph satisfies the no-isolated-zero condition vacuously. The graph \(P_1\) is a single vertex, \(P_2\) a single edge, and \(C_n\) denotes the ordinary simple cycle for \(n\ge3\). Powers of the indeterminate \(z\) record total function weight; coefficients count distinct assignments to individually distinguished vertices. The primary classification is graph domination, MSC2020 \(05\mathrm C69\).

## Proof

**1. Zero-leaf obstruction and factorization.** A private leaf cannot carry value zero. Indeed, restraint would require its only neighbor (its core) to have value zero; its neighbor sum would then be zero, contradicting Italian domination. Hence all private leaves carry value one or two. Let \(Z\) be the set of zero-labeled original vertices; restraint is now equivalent to \(Z\in\mathcal A(H)\). A positive original vertex and its leaf each independently receive value one or two, contributing \((z+z^2)^2\). At a zero original vertex \(v\), its leaf may receive one or two if \(v\) has any positive original neighbor; if not, the leaf is forced to receive two. These conditions are sufficient because at least one positive original neighbor contributes at least one, together with the positive leaf. Thus, with \(b=b_H(Z)\), the contribution of exactly this \(Z\) is
\[
 (z+z^2)^{2(n-|Z|)+b}z^{2(|Z|-b)}
 =z^{2n-b}(1+z)^{2(n-|Z|)+b}.
\]
Summing over \(Z\) proves the enumerator without cancellation or omitted labelings. Every summand has least exponent \(2n-b_H(Z)\), whose coefficient is exactly one. Consequently the global smallest exponent is \(2n-B(H)\) and its coefficient is the number of maximizing sets. More explicitly, for such \(Z\), all positive cores and their leaves receive one, every zero core bordering a positive core has leaf value one, and every remaining zero core has leaf value two. This constructs and uniquely classifies every optimizer.

**2. Paths.** Encode membership of \(Z\) by a binary word of length \(n\), with \(1\) for a zero core. Every run of ones has length at least two; the all-zero word is also admissible. Suppose there are \(r\ge1\) runs of ones and \(h\in\{0,1,2\}\) endpoint runs of zeros. There are \(r-1\) internal zero runs, each of positive length. Therefore
\[
 n\ge2r+(r-1)+h=3r-1+h.
\]
Each transition between a zero run and a one run contributes exactly one vertex to \(b_H(Z)\); the two endpoints of a one run are distinct because its length is at least two. Thus
\[
 b_H(Z)=2r-2+h.
\]
Combining these inequalities with \(h\le2\) gives \(n\ge3b_H(Z)/2+1\), or \(b_H(Z)\le\lfloor(2n-2)/3\rfloor\). The bound is attained by the following run patterns.

For \(n=3k\), the unique parameter choice at the maximum is \((r,h)=(k,1)\), with every run of minimum length, giving two endpoint orientations. For \(n=3k+1\) with \(k\ge1\), the choice is \((k,2)\) with all minimum runs, giving one word. For \(n=3k+2\) with \(k\ge1\), there are two choices: \((k+1,0)\) with all minimum runs, giving one word, or \((k,2)\) with one extra position distributed among its \(2k+1\) runs, giving \(2k+1\) words. At \(n=1\) the all-zero word is the unique optimizer. At \(n=2\), both the all-zero and all-one words are optimal. This proves the path count in every residue class.

**3. Cycles.** For a proper nonempty \(Z\subsetneq V(C_n)\), the binary cyclic word has \(r\ge1\) one runs, each of length at least two, alternating with exactly \(r\) nonempty zero runs. Each one run has two distinct boundary vertices, so \(n\ge3r\) and \(b_H(Z)=2r\). Both constant words have boundary zero and cannot be optimal when \(n\ge3\). The largest possible \(r\) is \(k=\lfloor n/3\rfloor\). Write \(n=3k+d\) with \(d\in\{0,1,2\}\). For \(r=k\), distribute \(d\) extra symbols among the \(2k\) alternating runs, in \(\binom{2k+d-1}{d}\) ways. Marking the start of a one run provides \(n\) choices of its labeled starting vertex, but counts each cyclic word exactly \(k\) times. Hence the number is
\[
 \frac nk\binom{2k+d-1}{d}=
 \begin{cases}3,&d=0,\\2n,&d=1,\\n(2k+1),&d=2.\end{cases}
\]
Together with Part 1, this proves all sunlet conclusions.

**4. An extremal structural consequence.** If \(n\ge2\), then \(B(H)\le n-1\). Equality is equivalent to the existence of a universal vertex \(u\) of \(H\) such that \(H-u\) has no isolated vertices. To see this, \(b_H(Z)=n-1\) forces \(|Z|=n-1\) and \(V(H)\setminus Z=\{u\}\); all vertices of \(Z\) must be adjacent to \(u\), and \(Z\) must have no induced isolates. The reverse is immediate. In this case \(\gamma_{rI}(W(H))=n+1\), and the number of optimizers equals the number of such vertices \(u\). For example, if \(n\ge3\), \(W(K_n)\) has minimum weight \(n+1\) and exactly \(n\) optimizers. In contrast, for the star \(K_{1,m}\) with \(m\ge2\), the maximum boundary is one, so its corona has minimum weight \(2m+1\) and exactly \(2^m-2\) optimizers (the center belongs to \(Z\), with a nonempty proper subset of leaves also in \(Z\)).

## Verification

The included independent Python-standard-library verifier tests the original labeling definition directly against the polynomial formula for every labeled graph on at most four vertices (\(75\) graphs) and five further five-vertex examples (\(80\) graphs total). It also checks the binary-run path and cycle formulas for all specified orders through \(18\), and independently brute-forces actual corona labelings for cycles of orders three through five. Execute `python3 verify.py` from the extracted package directory. Direct vertex-label enumeration and base-subset enumeration use separate routines, so agreement is not merely re-evaluation of the same formula. The mathematical proof, not the finite tests, establishes all orders.

## Relationship to prior work

Samadi, Alishahi, Masoumi, and Mojdeh introduced restrained Italian domination and established hardness, general bounds, tree extremal families, and special-order characterizations (arXiv:2009.12209; later RAIRO 2021). Volkmann (2023) studied sharp scalar bounds and specific graph families, including the ordinary paths and cycles, not the leaf coronas counted here. Velmurugan and Kala studied the *restrained domination polynomial*, which counts vertex subsets and is different from the present labeled-function polynomial. Abdulhasan and Mojdeh (online 2023, journal 2024) studied restrained Italian domination and state that they computed scalar parameters for some corona graphs; their full paper was not available for a definitive statement-by-statement comparison. Any scalar overlapping instances belong to that prior literature, not to a novelty claim here. The proposed contribution is the universal exact **labeled-function enumerator**, its induced-boundary mechanism, and the complete optimal-function census on combs and sunlets.

## Limitations

The formula concerns one-leaf coronas, not general corona products or independent domination parameters. The path and cycle optimum counts use labeled vertices and are not automorphism-orbit counts. The component-sum polynomial does not by itself establish the computational complexity of evaluation on arbitrary input graphs, and no such hardness claim is made. The 2023/2024 corona-related paper could only be checked by metadata and abstract, leaving a genuine overlap risk particularly for scalar corollaries. Nothing is asserted about independent validation or publication priority.

## References

1. B. Samadi, M. Alishahi, I. Masoumi, and D. A. Mojdeh, *Restrained Italian domination in graphs*, arXiv:2009.12209, publicly posted 2020-09-25; RAIRO Operations Research **55** (2021), 319–332, DOI:10.1051/ro/2021022.
2. L. Volkmann, *Remarks on the restrained Italian domination number in graphs*, Communications in Combinatorics and Optimization **8** (2023), 183–191, DOI:10.22049/CCO.2021.27471.1269.
3. S. Velmurugan and R. Kala, *Restrained domination polynomial of join and corona of graphs*, Discrete Mathematics, Algorithms and Applications **15** (2023), 2250118, DOI:10.1142/S179383092250118X.
4. A. M. Ridha Abdulhasan and D. A. Mojdeh, *Further results on (total) restrained Italian domination*, Discrete Mathematics, Algorithms and Applications **16** (2024), 2350017, DOI:10.1142/S1793830923500179.
5. A. Almulhim, B. Al Subaiei, and S. R. Mondal, *Survey on Roman \(\{2\}\)-Domination*, Mathematics **12** (2024), 2771, DOI:10.3390/math12172771.
