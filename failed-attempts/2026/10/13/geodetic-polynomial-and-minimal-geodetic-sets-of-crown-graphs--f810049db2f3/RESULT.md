# Geodetic polynomial and minimal geodetic sets of crown graphs
## Finding
For every integer \(n\ge 3\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\) have bipartition
\(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(a_i b_i\) is the deleted perfect-matching edge. For \(S\subseteq V(\operatorname{Cr}_n)\), write
\[
I=\{i:a_i\in S\},\qquad J=\{i:b_i\in S\}.
\]
Then \(S\) is a geodetic set if and only if exactly one of the following structural alternatives holds:

1. \(I\cap J\ne\varnothing\);
2. \((I,J)=([n],\varnothing)\) or \((I,J)=(\varnothing,[n])\);
3. \(I\cap J=\varnothing\) and \(|I|\ge3\), \(|J|\ge3\).

Consequently, if
\[
\mathcal G_n(x)=\sum_{S\text{ geodetic}}x^{|S|},
\]
then
\[
\mathcal G_n(x)
=(1+x)^{2n}-(1+2x)^n+2x^n
+\sum_{k=6}^{n}\binom{n}{k}\bigl(2^k-k^2-k-2\bigr)x^k,
\]
where the final sum is empty for \(3\le n\le5\).

The inclusion-minimal geodetic sets are exactly the \(n\) deleted-matching pairs \(\{a_i,b_i\}\), the two partite classes \(A\) and \(B\), and, when \(n\ge6\), the sets with \(|I|=|J|=3\) and \(I\cap J=\varnothing\). Hence the upper geodetic number is
\[
g^+(\operatorname{Cr}_n)=n,
\]
and the number of inclusion-minimal geodetic sets is
\[
n+2+20\binom{n}{6},
\]
with the binomial term interpreted as zero when \(n<6\).

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. A set \(S\) is geodetic when every vertex lies on at least one shortest path whose two endpoints belong to \(S\). The statement concerns ordinary geodetic sets, not strong, edge, connected, dominating, or hull variants. The family starts at \(n=3\), the connected crown graphs.

## Proof
The metric of \(\operatorname{Cr}_n\) has three relevant forms. Distinct vertices in the same part are at distance \(2\); unmatched cross-part vertices \(a_i,b_j\) with \(i\ne j\) are adjacent; and each deleted-matching pair \(a_i,b_i\) is at distance \(3\).

Fix an omitted vertex \(a_i\notin S\). A shortest path with \(a_i\) as an internal vertex can only have one of two endpoint types. First, two selected vertices \(b_j,b_k\) can use the length-two geodesic \(b_j-a_i-b_k\), which requires distinct \(j,k\ne i\). Second, a selected deleted-matching pair \(a_j,b_j\), with \(j\ne i\), has a length-three geodesic through \(a_i\): because \(n\ge3\), choose an index \(k\notin\{i,j\}\) and use
\[
a_j-b_k-a_i-b_j.
\]
No other endpoint type can have \(a_i\) internally on a geodesic: same-part \(A\)-endpoints have their internal vertices in \(B\), unmatched cross-part endpoints are adjacent, and every length-three cross-part geodesic joins a deleted-matching pair. Therefore \(a_i\) is covered exactly when either \(|J\setminus\{i\}|\ge2\) or \(I\cap J\ne\varnothing\). The symmetric condition holds for an omitted \(b_i\).

If \(I\cap J\ne\varnothing\), one selected deleted-matching pair covers every omitted vertex, so \(S\) is geodetic. Suppose instead that \(I\cap J=\varnothing\). If \(I=[n]\), then necessarily \(J=\varnothing\), and every omitted \(b_i\) lies between two selected \(A\)-vertices whose indices differ from \(i\); thus \(A\) is geodetic, and symmetrically so is \(B\). In every other disjoint case, there are omissions in both parts. For an omitted \(a_i\) whose index belongs to \(J\), exactly \(|J|-1\) selected \(B\)-vertices avoid index \(i\); hence all omitted \(A\)-vertices are covered if and only if \(|J|\ge3\). Symmetrically, all omitted \(B\)-vertices are covered if and only if \(|I|\ge3\). This proves the structural classification.

For the polynomial, first count all sets with \(I\cap J\ne\varnothing\). There are four local states at each matched index, while the disjoint condition allows only none, \(A\)-only, or \(B\)-only, so the weighted enumerator is
\[
(1+x)^{2n}-(1+2x)^n.
\]
The two full partite classes contribute \(2x^n\). For a disjoint geodetic set with total size \(k\ge6\), choose the \(k\) occupied indices and assign each to side \(A\) or side \(B\), with at least three indices assigned to each side. Among the \(2^k\) assignments, the forbidden ones have one side of size \(0\), \(1\), or \(2\), giving
\[
2\left(\binom{k}{0}+\binom{k}{1}+\binom{k}{2}\right)=k^2+k+2
\]
forbidden assignments. This gives the stated coefficient correction.

For minimality, any geodetic set with \(I\cap J\ne\varnothing\) contains a two-vertex deleted-matching pair that is itself geodetic, so the only minimal sets of this type are those pairs. Each full partite class is minimal because deleting one vertex leaves a disjoint one-sided set that fails the criterion. Finally, a disjoint two-sided geodetic set is minimal exactly when both side sizes are exactly \(3\). There are \(\binom{n}{3}\binom{n-3}{3}=20\binom{n}{6}\) such sets. Their sizes are \(6\), while the two full partite classes have size \(n\); therefore the maximum size of a minimal geodetic set is always \(n\).

## Verification
A standalone verifier independently constructs \(\operatorname{Cr}_n\), computes all-pairs graph distances, tests the geodetic condition directly from shortest-path equalities, and compares every subset with the structural criterion for \(3\le n\le8\). It also checks every coefficient of the polynomial and independently tests inclusion-minimality by deleting each selected vertex. The replay result is:

`VERIFY_OK n_range=3..8 subset_checks=87360 geodetic_sets=79076 minimal_sets=765 coefficient_checks=72 minimal_checks=79076 max_order=16`

The finite computation is a verification of the symbolic proof on small orders; it is not used as an infinite proof.

## Relationship to prior work
Harary, Loukakis, and Tsouros introduced the geodetic number in 1993, and Chartrand, Harary, and Zhang subsequently developed geodetic and upper geodetic sets. A 2012 paper of Vijayan and Dafini develops geodetic polynomials for paths and wheels. A 2024 paper on edge removal explicitly records \(g(\operatorname{Cr}_n)=2\) and exhibits deleted-matching pairs as geodetic witnesses for a crown graph; thus the scalar minimum is not claimed here as new. The contribution above is the complete all-cardinality classification and polynomial together with the classification and count of every inclusion-minimal geodetic set.

The closest previously checked exact polynomial result for complete multipartite graphs does not imply this formula: a crown graph is obtained by deleting a perfect matching from \(K_{n,n}\), and those deleted edges create distance-three matched pairs. In fact, that metric change is precisely why every selected deleted-matching pair already geodetically covers the crown.

## Limitations
The proof is specific to ordinary crown graphs \(K_{n,n}-M_n\) for \(n\ge3\); it does not assert a formula for unbalanced bipartite graphs with a deleted matching or for geodetic variants. The full text of the 2013 article introducing the geodetic polynomial was not available through the access route used here, and two 2021 conference references cited by the 2024 crown paper were not located in accessible full text. Their available descriptions concern the scalar geodetic number rather than an all-set polynomial, but this remains a literature-coverage risk.

## References
1. F. Harary, E. Loukakis, C. Tsouros, “The geodetic number of a graph,” Mathematical and Computer Modelling 17(11) (1993), 89–95. DOI: 10.1016/0895-7177(93)90259-2.
2. G. Chartrand, F. Harary, P. Zhang, “Geodetic sets in graphs,” Discussiones Mathematicae Graph Theory 20(1) (2000), 129–138. DOI: 10.7151/dmgt.1112.
3. A. Vijayan, K. Vijila Dafini, “On geodetic sets and geodetic polynomials of wheels and paths,” International Journal of Mathematical Sciences and Engineering Applications 6(3) (2012), 123–137. Public PDF: https://ascent-journals.com/IJMSEA/Vol6No3/12-vijayan.pdf.
4. A. Vijayan, T. Binu Selin, “An introduction to geodetic polynomial of a graph,” Bulletin of Pure & Applied Sciences—Mathematics and Statistics 31E(1) (2012), 25–32; online publication page dated 2013-01-11: https://indianjournals.com/article/bpasms-31e-1-004.
5. G. Micheal Antony Gnana Santhiyagu, R. Arul Ananthan, S. Balamurugan, “Changing and Unchanging the Geodetic Number: Edge Removal,” Mapana Journal of Sciences 22(4) (2023), 115–121; published online 2024-03-19. DOI: 10.12723/mjs.67.8.
