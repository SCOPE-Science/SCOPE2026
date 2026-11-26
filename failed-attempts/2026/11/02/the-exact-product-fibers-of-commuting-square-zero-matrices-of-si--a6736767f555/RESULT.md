# The exact product fibers of commuting square-zero matrices of size four

## Finding
Let \(k=\mathbb F_q\) be any finite field. Define \(\mathcal X_q=\{(A,B)\in M_4(k)^2:A^2=B^2=0,\ AB=BA\}\) and the multiplication map \(\mu(A,B)=AB\). For every nonzero square-zero rank-one matrix \(C\), the complete fiber of \(\mu\) over \(C\) has exactly \(q^3(q-1)(q^2-1)\) points. The image of \(\mu\) consists of zero and the nonzero square-zero rank-one matrices; the characterization of the image is already known, not a novelty claim. The zero fiber has the explicit count
\[
\#\mu^{-1}(0)=1+N_1+N_2+N_1(q^5+q^4-q^2)+N_2(2q^4-q^2)-N_1q^3(q-1)(q^2-1),
\]
where \(N_1=(q^4-1)(q^3-1)/(q-1)\) and \(N_2=(q^2+1)(q^2+q+1)(q^2-1)(q^2-q)\). Therefore every fiber is determined, uniformly in all characteristics. Equivalently the total number of commuting square-zero ordered pairs is
\[
1+N_1+N_2+N_1(q^5+q^4-q^2)+N_2(2q^4-q^2).
\]

## Assumptions and scope
Matrices have size exactly four; multiplication is ordinary associative matrix multiplication. Ordered pairs are counted individually, not modulo conjugation. Both factors square to zero, commute with each other, and are allowed to be zero. A square-zero matrix of size four has rank zero, one or two. All formulas apply for every prime power \(q\), including even characteristic. Here \(N_i\) denotes the number of square-zero matrices of rank \(i\), and the inverse-image notation concerns the set map on finite-field points.

## Proof
For a rank-one square-zero matrix, choose its image line, its kernel hyperplane containing that line, and a nonzero isomorphism between the resulting one-dimensional quotient and image. This gives \(N_1=(q^4-1)(q^3-1)/(q-1)\). A rank-two square-zero matrix has equal image and kernel \(K\), a two-plane; the induced map \(k^4/K\to K\) is invertible. Thus \(N_2={4\brack2}_q|\operatorname{GL}_2(k)|\), which is the stated product.

The centralizer of any rank-one square-zero \(A\) can be computed after choosing \(A=E_{12}\). Decompose \(k^4=k\oplus k\oplus k^2\). Every commuting \(B\) is uniquely
\[
 B=\begin{pmatrix}a&b&u\\0&a&0\\0&v&C\end{pmatrix},
\]
where \(u\) is a row of length two, \(v\) a column of length two and \(C\) a two-by-two matrix. Squaring gives \(a^2=0\), \(C^2=0\), \(uC=0\), \(Cv=0\), \(uv=0\) after \(a=0\). The parameter \(b\) is unconstrained. For \(C=0\), exactly \(q^3+q^2-q\) ordered pairs \((u,v)\) satisfy \(uv=0\): the zero row allows \(q^2\) choices, and each nonzero row allows \(q\). For nonzero \(C^2=0\), there are \(q^2-1\) possible matrices \(C\), each of rank one; \(u\) annihilates its image and \(v\) lies in its kernel, which equals its image. There are \(q^2\) such pairs and \(uv=0\) follows. Hence the number of admissible \(B\) is \(q[(q^3+q^2-q)+(q^2-1)q^2]=q^5+q^4-q^2\). The product \(AB\) is identically zero in this case.

For rank-two \(A\), identify \(k^4\) with \((k[t]/(t^2))^2\), with \(A\) multiplication by \(t\). The full commuting centralizer consists of \(B=P+tQ\), for arbitrary \(2\times2\) matrices \(P,Q\) over \(k\). The square-zero condition is precisely \(P^2=0\) and \(PQ+QP=0\), without division by two. For \(P=0\), all \(q^4\) choices of \(Q\) work and \(AB=0\). There are \(q^2-1\) nonzero square-zero \(P\), all conjugate to \(E_{12}\); in this normal form \(PQ+QP=0\) imposes two independent linear constraints on the four entries of \(Q\). Thus there are \(q^2\) choices for each such \(P\), with \(AB=tP\ne0\), of rank one. Consequently a fixed rank-two \(A\) contributes \(2q^4-q^2\) partners and exactly \(q^4-q^2\) nonzero products.

For rank zero \(A\), every square-zero \(B\) works, giving \(1+N_1+N_2\). Partitioning by rank of \(A\) proves the total formula. Any product of commuting square-zero matrices squares to zero; when \(A\) has rank at most one it vanishes; when \(A\) has rank two its rank is at most one, as shown above. Conversely choose rank-two \(A\) and nonzero \(P\) above, obtaining a nonzero rank-one square-zero product. All such targets are conjugate under \(\operatorname{GL}_4(k)\), which preserves the fibers by simultaneous conjugation. Thus all \(N_1\) nonzero targets have the same fiber size. Dividing the \(N_2(q^4-q^2)\) nonzero-product pairs by \(N_1\) gives \(q^3(q-1)(q^2-1)\), completing the proof of both fibers. Every argument remains valid in characteristic two.

## Verification
Run `python3 verify.py`. It independently enumerates all square-zero four-by-four matrices over \(\mathbb F_2\), all commuting pairs and actual multiplication products, and compares every fiber to the formulas. It also enumerates the normal-form centralizers over \(\mathbb F_3\). The execution observed for \(q=2\): \(N_1=105\), \(N_2=210\), total pairs \(10816\), zero fiber \(8296\), each of \(105\) nonzero fibers \(24\). For \(q=3\): \(N_1=1040\), \(N_2=6240\), total pairs \(1289601\), \(449280\) nonzero-product pairs, and uniform nonzero fiber \(432\). These finite experiments are independent corroboration, not proof over all finite fields.

## Relationship to prior work
Kokol Bukovšek, Košir, Novak and Oblak classified images of products of commuting square-zero operators and exhibited the first nonzero case in size four (2007, Proposition 2.2 and Example 2.1). Their qualitative image characterization is explicitly treated as known here. The present claim is the exact counting measure on every fiber of that multiplication map over finite fields. Britnell and Wildon (2010) study which nilpotent similarity classes contain commuting representatives; this does not enumerate the multiplication-map fibers. Ngo and Šivic (2013) study geometry of nilpotent commuting varieties, without the special simultaneous square-zero product-fiber formula in the inspected material. The relation to known commuting-graph classifications is different: rank-one square-zero commuting pairs have zero product, whereas the nonzero fibers here require rank-two factors.

## Limitations
Only size four and commuting square-zero factors are covered. The theorem does not count conjugacy orbits of factorizations, and does not determine scheme multiplicities, singularities, higher dimensions, or factorizations by unrestricted nilpotent matrices. The historical comparison cannot exclude an equivalent arithmetic identity in unlocated literature; independent peer verification has not been performed.

## References
1. D. Kokol Bukovšek, T. Košir, N. Novak and P. Oblak, *Products of commuting nilpotent operators*, Electronic Journal of Linear Algebra 16 (2007), 237–247. https://journals.uwyo.edu/index.php/ela/article/download/455/455/455 . Full text, especially Example 2.1 and Proposition 2.2.
2. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811, first posted 2010-01-06. https://arxiv.org/abs/1001.0811 .
3. N. V. Ngo and K. Šivic, *On varieties of commuting nilpotent matrices*, arXiv:1308.4438 (2013). https://arxiv.org/abs/1308.4438 .
