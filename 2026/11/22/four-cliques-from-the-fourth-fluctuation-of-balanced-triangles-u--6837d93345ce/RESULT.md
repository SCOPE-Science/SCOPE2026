# Four-cliques from the fourth fluctuation of balanced triangles under fair edge signs

## Finding

Let \(G=(V,E)\) be an arbitrary finite simple undirected graph. Write \(t=t(G)\) for its number of triangles and \(q=q(G)\) for its number of four-vertex cliques. Sign every edge independently, with \(\Pr(\varepsilon_e=+1)=\Pr(\varepsilon_e=-1)=1/2\). A triangle is balanced if its three edge signs have product \(+1\), and \(B_G\) is the number of balanced triangles. With the fourth cumulant normalized as \(\kappa_4(Z)=\mathbb E[(Z-\mathbb EZ)^4]-3\operatorname{Var}(Z)^2\), one has the exact finite-graph identities

\[
\mathbb E B_G=\frac t2,\qquad \operatorname{Var}(B_G)=\frac t4,\qquad
\kappa_4(B_G)=\frac{3q}{2}-\frac t8.
\]

In particular, the **complete one-dimensional law** of \(B_G\) determines both motif counts:

\[
t(G)=4\operatorname{Var}(B_G),\qquad
q(G)=\frac{2\kappa_4(B_G)+\operatorname{Var}(B_G)}3.
\]

The stronger structural statement underlying this inversion is that any four **distinct** triangle signs have a nonzero joint product expectation exactly when those triangles are the four faces of a single four-clique. Two different triangle signs are always independent, but four signs can have a rigid tetrahedral dependence.

## Assumptions and scope

The graph is fixed, finite, undirected and simple; its vertex count is arbitrary. All existing edges receive independent **unbiased** signs. Only triangles whose three edges are present are counted. The graph may be disconnected or have no triangles. There is no asymptotic assumption and no inference guarantee from finitely many independent signing observations. For \(t=0\), \(B_G=0\) and both recovered motif counts are zero.

## Proof

For each triangle \(T\), define its sign character \(Y_T=\prod_{e\in E(T)}\varepsilon_e\), and put \(S=\sum_TY_T\). Then \(B_G=(t+S)/2\). Independence and symmetry of edge signs give, for every collection of triangle indices,

\[
\mathbb E\prod_{j=1}^rY_{T_j}=\begin{cases}1,&\text{every edge occurs an even number of times in the multiset of triangles},\\0,&\text{otherwise.}\end{cases}
\]

Each \(Y_T\) has mean zero and square one. Distinct triangles have distinct edge sets, so \(\mathbb E Y_TY_U=0\) for \(T\ne U\). Therefore \(\mathbb ES=0\) and \(\mathbb ES^2=t\).

For the fourth moment, a quadruple of triangle indices whose union has even edge multiplicities is of one of two types. If indices repeat, every distinct index must occur an even number of times. Indeed, a triangle occurring once while the others occur in a repeated pair would require its unique edge set to equal that of the remaining singleton; a triple occurrence with one different index likewise leaves the symmetric difference of two triangle edge sets nonempty. Thus the repeated-index contributions are \(t+6\binom t2=3t^2-2t\).

Suppose instead that \(T_1,T_2,T_3,T_4\) are distinct and have every edge appearing evenly. Write \(T_1=abc\). No other distinct triangle can share two edges with \(abc\); each of its three edges must therefore occur in one of the three remaining triangles, and each of those triangles contains precisely one edge of \(abc\). After relabeling, these triangles are \(abx\), \(bcy\), and \(caz\), with \(x,y,z\notin\{a,b,c\}\). The edge \(ax\) forces \(x=z\), and the edge \(bx\) forces \(x=y\). Consequently \(x=y=z\): the four triangles are precisely the faces of the clique on \(\{a,b,c,x\}\). Conversely all four faces of every four-clique have even aggregate edge multiplicities. Each four-clique contributes \(4!=24\) ordered distinct quadruples.

It follows that

\[
\mathbb ES^4=3t^2-2t+24q,\qquad
\kappa_4(S)=(3t^2-2t+24q)-3t^2=24q-2t.
\]

Since fourth cumulants scale by the fourth power of the multiplicative constant, \(\kappa_4(B_G)=\kappa_4(S)/16=3q/2-t/8\), while \(\operatorname{Var}(B_G)=\operatorname{Var}(S)/4=t/4\). Solving yields both stated recovery formulas. All arguments are identities for each finite graph.

## Verification

Run `python3 signed_triangle_checker.py` with Python 3 (standard library only). The program enumerates every labeled graph with up to five vertices and four selected graphs on six vertices, and for each graph enumerates every possible edge signing. It accumulates exact integer moments and checks the fourth-cumulant identity, variance, and motif recovery using rational arithmetic. Completed output:

`PASS: 1103 labeled graphs, 117154 exact sign assignments; 5 assertions per graph`

This independent finite enumeration is a boundary check, not a substitute for the all-graph combinatorial proof. The file is self-contained and requires no downloaded data.

For a structural contrast, a four-clique and a disjoint union of four triangles both have \(t=4\) and hence variance \(1\) for \(B_G\), but their fourth cumulants differ: \(1\) in the first graph and \(-1/2\) in the second. The fourth cumulant detects the four-clique that the variance cannot detect.

## Relationship to prior work

Signed-graph structural balance and random-sign models precede this result. El Maftouhi, Manoussakis and Megalakaki (2012) study global balance thresholds and asymptotic relative balance in randomly signed Erdős–Rényi graphs; Estrada and Benzi (2014) formulate triadic and walk-based balance diagnostics; and Tian and Feng (2025) treat first and second moments and Gaussian fluctuations for balanced and unbalanced triangle counts in sparse signed Erdős–Rényi graphs. None of the inspected material provides the **fixed arbitrary support graph** identity recovering four-clique count from the **fourth cumulant** of balanced triangle count. Elementary Walsh-character orthogonality is used as a proof ingredient, not claimed as new.

## Limitations

Unbiased independent signs are essential to the simple edge-parity orthogonality. This work does not derive a corresponding identity for biased or dependent signs, estimate motif counts from a limited sample of signings, or claim computational superiority over direct clique enumeration. The comparison with historical literature is evidence of distinct statement scope, not proof of priority; unindexed equivalent Walsh-cumulant treatments could exist. The 2025 publisher article was accessible through indexed sections rather than a full printable copy. Independent mathematical audit has not been performed.

## References

1. A. El Maftouhi, Y. Manoussakis, O. Megalakaki, *Balance in Random Signed Graphs*, Internet Mathematics 8 (2012), 364–380. DOI: https://doi.org/10.1080/15427951.2012.675413. An author's version: https://www.lri.fr/~yannis/randsigned.pdf.
2. E. Estrada, M. Benzi, *Walk-based measure of balance in signed networks: Detecting lack of balance in social networks*, Physical Review E 90 (2014), 042802, published 2014-10-03. DOI: https://doi.org/10.1103/PhysRevE.90.042802. Lawful full text: https://strathprints.strath.ac.uk/68212/1/Estrada_Benzi_PRE_2014_a_walk_based_measure_of_balance_in_signed_networks_detecting_a_lack_of_balance.pdf.
3. Y. Tian, Q. Feng, *Degree of balance in random signed graphs*, Statistics & Probability Letters 225 (2025), 110459. DOI: https://doi.org/10.1016/j.spl.2025.110459.
