# Cubic Fourier recovery and the orientation-blind quadratic frame of the thirty labelled Fano planes

## Finding
Fix the labelled point set \(X=\{1,2,3,4,5,6,7\}\), let \(\mathcal T=\binom X3\) be its 35 possible triples, and let \(\mathcal F\) consist of the 30 Steiner triple systems of order seven on \(X\). Represent \(P\in\mathcal F\) by the incidence vector \(x(P)\in\{0,1\}^{\mathcal T}\). For \(0\le d\le35\), let \(V_d\subseteq\mathbb R^{\mathcal F}\) be the span of the restrictions of Walsh characters \(\chi_S(x)=(-1)^{\sum_{t\in S}x_t}\), for \(|S|\le d\). Equivalently, \(V_d\) is the space of all joint membership observations for at most \(d\) specified triples.

The exact degree hierarchy is
\[
\boxed{(\dim V_0,\dim V_1,\dim V_2,\dim V_3)=(1,15,29,30).}
\]
The one-dimensional orthogonal complement of \(V_2\) has generator \(\varepsilon:\mathcal F\to\{-1,1\}\), assigning the parity of a permutation taking the standard Fano plane to \(P\). This is well-defined because all 168 standard-plane automorphisms are even. There are 15 planes of each sign. Consequently, the uniform laws on these two sets of 15 have identical joint membership marginals for every set of at most two triples, but are distinguished by a three-triple event: the three lines \(123\), \(145\), \(246\) are simultaneously present in exactly one of the 30 planes. Their probabilities under the two uniform laws are \(1/15\) and zero (in one order or the other).

The unnormalized real Gram matrices formed from the constant function and all squarefree *membership monomials* of degree at most one and two respectively have exact spectra
\[
G_1:\quad72^{[1]},\ 12^{[14]},\ 0^{[15]},
\qquad
G_2:\quad114^{[1]},\ 39^{[14]},\ 15^{[14]},\ 0^{[1]},
\]
where superscripts in brackets are multiplicities. These Gram spectra are for monomial features, not orthonormally normalized Walsh features; the ranks agree because the two feature systems are related by invertible degree-preserving triangular transformations.

## Assumptions and scope
All planes and triples are fully labelled. A Steiner triple system means seven 3-element blocks partitioning the 21 unordered point-pairs exactly once. A probability law is any real nonnegative vector on the 30 planes of total mass one. Observations involve joint *presence* of specified triples; joint absence and mixed membership patterns have the same linear span. No restriction to the uniform law is imposed for the identifiability statement.

## Proof
**Step 1 (labelled orbit and parity).** Use the canonical plane
\[
P_* = \{123,145,167,246,257,347,356\}.
\]
The permutation orbit of \(P_*\) has size \(7!/168=30\). Its automorphism group, isomorphic to \(\operatorname{GL}(3,2)\), is simple and acts by even permutations of the seven points. Thus the sign \(\varepsilon(P)=\operatorname{sgn}(\pi)\) for \(P=\pi P_*\) is well-defined, splitting \(\mathcal F\) into two classes \(A,B\) of size 15 each.

**Step 2 (quadratic invisibility).** Any collection of at most two triples partitions the seven points into at most four membership-pattern cells. Some cell has at least two points; their transposition is odd and fixes each specified triple setwise. Hence this transposition pairs every plane of sign \(+1\) containing the chosen triples with a plane of sign \(-1\) containing them. Therefore
\[
\sum_{P\in\mathcal F}\varepsilon(P)\prod_{t\in S}x_t(P)=0
\quad\text{for every } |S|\le2,
\]
including the empty product. Walsh characters of degree at most two are linear combinations of these monomials, so \(\varepsilon\in V_2^\perp\).

**Step 3 (exact upper bound is sharp).** The 30 planes have a 15-plus-15 decomposition in which distinct planes from the same class share exactly one line. A plane in one class shares exactly three lines with seven planes in the other class, and zero with the other eight. The 15-by-15 cross-incidence matrix \(B_0\), whose entries indicate three shared lines, obeys
\[
B_0\mathbf1=7\mathbf1,\quad B_0^T\mathbf1=7\mathbf1,\quad B_0B_0^T=4I+3J.
\]
These finite geometric identities can be checked *exhaustively* from all \(7!\) relabellings using `verify_permutation.py` and independently via exact-cover enumeration using `verify_exact_cover.py`; the latter avoids taking the standard plane's permutation orbit as an enumeration assumption.

For the squarefree membership monomials of degree at most \(d=1,2\), the Gram entry between planes \(P,Q\) is
\[
G_d(P,Q)=\sum_{j=0}^d\binom{|P\cap Q|}{j}.
\]
When planes are ordered by the two parity classes, the resulting matrices have the block forms
\[
G_1=\begin{pmatrix}6I+2J&J+3B_0\\J+3B_0^T&6I+2J\end{pmatrix},
\quad
G_2=\begin{pmatrix}27I+2J&J+6B_0\\J+6B_0^T&27I+2J\end{pmatrix}.
\]
On vectors constant on each half, the eigenvalues are \(72,0\) for \(G_1\) and \(114,0\) for \(G_2\). On the 28-dimensional space orthogonal to the all-ones vector in each half, the cross-incidence singular values are all \(2\), by \(B_0B_0^T=4I+3J\). Thus \(G_1\) has eigenvalues \(12\) and \(0\), each 14-fold on this subspace, while \(G_2\) has eigenvalues \(39\) and \(15\), each 14-fold. The ranks are therefore exactly \(15\) and \(29\); the unique degree-two blind direction is \(\varepsilon\).

**Step 4 (cubic recovery).** The three triples \(123,145,246\) have exactly one common extension to a labelled Steiner triple system, namely
\[
\{123,145,167,246,257,347,356\}.
\]
To see uniqueness directly, the unpaired partners of point \(1\) are \(6,7\), forcing line \(167\); those of point \(2\) are \(5,7\), forcing \(257\); those of point \(4\) are \(3,7\), forcing \(347\). The remaining uncovered pairs force \(356\). The exact-cover enumeration separately checks the unique extension. Hence the cubic product \(x_{123}x_{145}x_{246}\) has nonzero inner product \(\pm1\) with \(\varepsilon\). Since \(V_2\) already has codimension one, adjoining this product gives \(V_3=\mathbb R^{\mathcal F}\).

## Verification
Run, with standard-library Python, `python verify_permutation.py` and `python verify_exact_cover.py` from the extracted package directory. The first checks the 5040 labelled permutations, the 168 even stabilizer elements, the 15-plus-15 partition, every cross-incidence entry, the symmetric \(2\)-\((15,7,3)\) identity, both exact Gram formulas, and the unique cubic witness. The second enumerates all solutions to the 21-pair exact-cover problem without using the orbit construction, finds the two overlap-one classes, and confirms degree-two and degree-three ranks modulo the independent primes 1009 and 1013. The structural block-matrix calculation proves the ranks over \(\mathbb R\); modular checks are supplementary, not a substitute for that proof.

## Relationship to prior work
The 30 labelled planes, their two 15-element classes and the possible overlap sizes are classical and appear explicitly in Saniga's 2015 preprint and 2016 article. The present statement concerns a different functional invariant: exact restricted Fourier spans, a unique quadratic blind probability contrast, a cubic recovery threshold, and the complete low-degree Gram spectra. The general design intersection framework of Lindner–Rosa and the geometric identification discussed by Hall provide related incidence structures, but do not explicitly state this three-stage sampling result in the accessible material. The 2024 work of Costa–Pavone treats common automorphism groups of orthogonal/oriented Fano planes, not this measurement map.

## Limitations
This is a theorem about exactly 30 labelled planes on seven points; it does not establish a similar reconstruction threshold for Steiner triple systems of other orders. The 15-plus-15 classes and their overlap structure are prior knowledge, not claimed new. The spectral/reconstruction conclusion is a deduction using that structure and an exact finite certificate. A previously unindexed account of the identical restricted incidence ranks could affect priority. No independent external audit is claimed.

## References
1. M. Saniga, *Combinatorial Intricacies of Labeled Fano Planes*, arXiv:1509.06009, first submitted 2015-09-20; *Entropy* 18 (2016), 312, https://arxiv.org/abs/1509.06009 and https://doi.org/10.3390/e18090312.
2. C. C. Lindner and A. Rosa, *Steiner Triple Systems Having a Prescribed Number of Triples in Common*, *Canadian Journal of Mathematics* 27 (1975), 1166–1175, https://doi.org/10.4153/CJM-1975-122-4.
3. J. I. Hall, *On Identifying PG(3,2) and the Complete 3-Design on Seven Points*, *Annals of Discrete Mathematics* 7 (1980), 131–141, https://doi.org/10.1016/S0167-5060(08)70177-8.
4. S. Costa and M. Pavone, *Orthogonal and oriented Fano planes, triangular embeddings of K7, and geometrical representations of F21*, *AIMS Mathematics* 9 (2024), 35274–35292, https://doi.org/10.3934/math.20241676.
