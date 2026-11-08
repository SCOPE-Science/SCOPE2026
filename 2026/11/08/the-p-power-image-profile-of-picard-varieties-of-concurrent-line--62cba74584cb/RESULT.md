# The \(p\)-power image profile of Picard varieties of concurrent lines

## Finding
Let \(k\) be algebraically closed of characteristic \(p>0\), let \(m\ge 3\), and let \(C_m\subset \mathbb P^2_k\) be the reduced union of \(m\) distinct lines through one point. Put \(J_m=\operatorname{Pic}^0(C_m)\), and, for every integer \(r\ge0\), put \(s=p^r\) and \(L=\lfloor (m-2)/s\rfloor\). Then \(J_m\) is a smooth connected commutative unipotent group of dimension \(\delta=(m-1)(m-2)/2\), and its multiplication-by-\(p^r\) image has dimension

\[
\boxed{\dim\operatorname{im}([p^r]:J_m\to J_m)=\sum_{j=1}^{L}(m-1-sj)=L(m-1)-\frac{sL(L+1)}2.}
\]

The exponent of \(J_m(k)\) is exactly \(p^{\lceil\log_p(m-1)\rceil}\). In particular, \([p]\) is nonzero precisely when \(m\ge p+2\). At the first possible example, \(m=4\) and \(p=2\), the three-dimensional group has a one-dimensional doubling image and contains a point of order four, so it is not a vector group.

The formula concerns the dimension of the *reduced scheme-theoretic image* of the multiplication map. It does not assert a classification of these groups up to isomorphism, nor that the multiplication maps are separable.

## Assumptions and scope
All \(m\) components are pairwise distinct projective lines, all passing through the same point, over one algebraically closed field. The curve is reduced, connected, and has one ordinary planar \(m\)-fold point. The characteristic is a prime \(p>0\). The claim is uniform in the directions of the lines and in every integer \(m\ge3\) and \(r\ge0\). The connected Picard variety is the smooth reduced neutral component; for these projective curves the Picard scheme itself is smooth along the identity.

## Proof
Write \(\nu:\widetilde C_m=\coprod_{i=1}^{m}\mathbb P^1\to C_m\) for normalization. Choose affine coordinates at the common point and distinct directions \((u_i:v_i)\in\mathbb P^1(k)\), and a uniformizer \(t_i\) on the \(i\)-th branch with \((x,y)=(u_it_i,v_it_i)\). The conductor of the completed local ring in its normalization contains precisely the branches' ideals \((t_i^{m-1})\). Indeed, the product of all line equations other than the \(i\)-th is zero on the other branches and is a unit times \(t_i^{m-1}\) on the \(i\)-th. The reverse containment follows from interpolation: a homogeneous binary form of degree smaller than \(m-1\) cannot vanish on the other \(m-1\) distinct directions while remaining nonzero on the selected one.

Let \(B=\prod_i k[t_i]/(t_i^{m-1})\), and let \(A\subset B\) be the image of the completed local ring. As a vector space, \(A\) consists of a common constant followed, in degree \(d\), by the evaluation vectors of binary homogeneous forms of degree \(d\), for \(1\le d\le m-2\). Write \(V_d\subset k^m\) for this evaluation space. Its dimension is exactly \(d+1\): a nonzero binary form of degree \(d<m\) has at most \(d\) zeros on \(\mathbb P^1\), so the evaluation map is injective.

The normalization gluing exact sequence for units and the vanishing \(\operatorname{Pic}^0(\mathbb P^1)=0\) identify \(J_m\) with the quotient of local normalized units by the local ring units and the \(m\) independent global constants on the normalized components. The constants eliminate the torus. In particular, put
\[
G=\prod_{i=1}^{m}(1+t_i k[t_i]/(t_i^{m-1})),\qquad
H=G\cap A^\times.
\]
Then \(J_m\cong G/H\). Both groups are connected smooth unipotent, and \(H\) has \(\sum_{d=1}^{m-2}(d+1)\) parameters while \(G\) has \(m(m-2)\); hence
\[
\dim J_m=m(m-2)-\sum_{d=1}^{m-2}(d+1)=\frac{(m-1)(m-2)}2.
\]

Fix \(r\ge0\) and \(s=p^r\). In characteristic \(p\), taking the \(s\)-th power of a normalized unit kills all coefficients except those at powers \(t_i^{sj}\). Conversely every unit with only those powers is an \(s\)-th power over the algebraically closed field \(k\). Thus the reduced image \(G_s=[p^r]G\) has dimension \(mL\), with independent degree-\(sj\) coefficients for \(1\le j\le L\). The intersection \(G_s\cap H\) consists of ring units whose expansion has coefficients only in degrees divisible by \(s\). In each degree \(sj<m-1\) these coefficients lie in \(V_{sj}\), a space of dimension \(sj+1\); coefficients at the other degrees are zero. This statement is scheme-theoretically valid for the *reduced* intersection since the conditions are linear on the unit coordinates. It follows that
\[
\dim(G_s\cap H)=\sum_{j=1}^L(sj+1),\qquad
\dim\operatorname{im}([p^r]|_{J_m})=mL-\sum_{j=1}^L(sj+1).
\]
This proves the displayed formula.

For \(p^e\ge m-1\), all truncated normalized units have \(p^e\)-th power equal to one, hence \([p^e]=0\) on \(J_m\). Conversely if \(p^r\le m-2\), take the normalized unit \((1+t_1,1,\ldots,1)\). Its \(p^r\)-th power has a nonzero coefficient at degree \(p^r\) on exactly one branch. Such a coordinate vector is not in \(V_{p^r}\): a degree-\(p^r\) homogeneous form with \(m-1>p^r\) distinct zeros is zero. Hence that power is nontrivial in \(J_m(k)\). The exact exponent and threshold follow.

## Verification
The accompanying standalone `verify.py` implements finite fields using integer polynomial arithmetic. It independently constructs evaluation matrices for homogeneous binary forms, computes exact modular ranks, and checks the formula for every \(m\) in the ranges \(3\le m\le10\) in characteristics two and five, \(3\le m\le9\) in characteristic three, and \(3\le m\le7\) in characteristic seven. It additionally enumerates the square-image quotient over \(\mathbb F_4\) for four concurrent lines (cardinality four) and tests the order-four witness. Running `python3 verify.py` reproduces the accompanying `verify_output.txt`, ending with `ALL_CHECKS_PASSED`. These finite computations validate the interpolation calculations in sample fields; the proof above establishes all admissible \(m,p,r\).

## Relationship to prior work
Generalized Jacobians and Picard varieties of singular curves have a classical normalization-and-unit-group description. Geisser's *The affine part of the Picard scheme* describes the maximal affine structure of Picard varieties (originally available in 2007; its 2021 arXiv revision incorporates corrections). Brion's *Which algebraic groups are Picard varieties?* (2013) identifies relative unit quotients from finite pinching as a general framework, studies their unipotent periods, and exhibits a different two-dimensional period-four example (Remark 4.19). Those results provide context and are not claimed as new.

The present contribution is the specific **complete all-\(r\) image-dimension profile** for the geometrically natural ordinary \(m\)-fold line pencil, proved by identifying the exact interpolation subspaces in every branch degree. The general framework in the inspected papers does not state this profile or imply its numerical formula without the interpolation and intersection analysis performed here. Targeted exact and semantic comparisons located no directly covering published formula; historical priority has not been established independently.

## Limitations
The result is for a reduced union of *concurrent* lines over an algebraically closed field, not arbitrary line arrangements, nonreduced pencils, or arbitrary singular curves. It gives image dimensions and group exponent, not a product decomposition into Witt groups or a classification of all group extensions. The literature comparison cannot exclude a different formulation in unlocated specialist sources.

## References
- T. Geisser, *The affine part of the Picard scheme*, arXiv:0704.0479 (first posted 2007-04-04; corrected version 2021), especially the introduction and structure results.
- M. Brion, *Which algebraic groups are Picard varieties?*, arXiv:1310.0186 (first posted 2013-10-01), especially Proposition 4.1, Proposition 4.11, and Remark 4.19.
- M. Rosenlicht, *Generalized Jacobian varieties*, Annals of Mathematics 59 (1954), 505–530, DOI:10.2307/1969715 (foundational background; no priority claim is based on unread portions of this source).
