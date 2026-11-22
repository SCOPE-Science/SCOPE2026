# Exact Euclidean chord spectra and Gaussian fluctuations of alternating shard polytopes

## Finding
Let \(r\ge1\) be an integer. In the standard coordinate realization of Padrol–Pilaud–Ritter, let \(P_r\subset\mathbb R^{2r}\) be the shard polytope whose arc has upper positions \(U=\{1,3,\ldots,2r-1\}\) and lower positions \(D=\{2,4,\ldots,2r\}\). Write \(V_r=\operatorname{Vert}(P_r)\), and let
\[
W_r(q)=\sum_{v,w\in V_r}q^{\|v-w\|_2^2/2}.
\]
This is an **ordered** vertex-pair enumerator; the diagonal is included. Its exact values satisfy
\[
\boxed{W_0(q)=1,\quad W_1(q)=2+2q,\quad W_2(q)=5+16q+4q^2,}
\]
and, for every \(r\ge3\),
\[
\boxed{W_r(q)=4(1+q)W_{r-1}(q)-4(1+q^2)W_{r-2}(q)+W_{r-3}(q).}
\tag{1}
\]
Equivalently, as a formal power series,
\[
\boxed{\sum_{r\ge0}W_r(q)t^r
=\frac{1-2(1+q)t+t^2}{1-4(1+q)t+4(1+q^2)t^2-t^3}.}
\tag{2}
\]
All possible squared distances among distinct vertices are exactly \(2,4,\ldots,2r\), and the unordered distinct-pair enumerator is \((W_r(q)-F_{2r+1})/2\), where \(F_0=0,F_1=1\) are the Fibonacci numbers. In particular, the squared diameter is \(2r\), with \(2^{r-1}\) unordered diametral vertex pairs. For \(r\ge2\), exactly \(r^2 2^{r-1}\) unordered pairs attain the second-largest squared distance \(2r-2\). The latter count is not a count of diagonal pairs even when \(r=1\): that exceptional case is deliberately excluded.

If \(v,w\) are sampled independently and uniformly from \(V_r\), and \(K_r=\|v-w\|_2^2/2\), then
\[
\boxed{\frac{K_r-\mu r}{\sqrt{\nu r}}\ \Longrightarrow\ N(0,1),\qquad
\mu=\frac{2(\sqrt5-1)}5,\qquad
\nu=\frac{22\sqrt5-30}{125}>0.}
\tag{3}
\]
The same limit holds for a uniformly selected unordered pair of **distinct** vertices. In particular, the exact outer two chord shells are exponentially rare relative to the typical, linearly scaling squared distance.

## Assumptions and scope
For \(r\ge1\), the arc is \(\alpha_r=(1,2r,A_r,B_r)\) with \(A_r=\{3,5,\ldots,2r-1\}\), \(B_r=\{2,4,\ldots,2r-2\}\). The notation \(P_0=\{0\}\) and \(W_0=1\) is a convenient initial convention and not an additional arc.

An alternating matching is a possibly empty ordered collection of disjoint pairs of positions \((u_1,d_1),\ldots,(u_k,d_k)\), where \(u_i\in U\), \(d_i\in D\), and \(u_1<d_1<\cdots<u_k<d_k\). Its characteristic vector \(\chi(M)\) equals \(1\) on the selected upper positions, \(-1\) on selected lower positions, and zero elsewhere. The primary source establishes that these characteristic vectors are exactly the vertices of the standard shard polytope. The Euclidean metric is the **unscaled** ambient coordinate metric; this theorem is not an affine-invariant statement.

The recurrence enumerates all ordered vertex pairs, including coincidences. The limiting distribution concerns Euclidean vertex chords, not distances between two uniformly volume-sampled interior points or shortest paths in the one-skeleton.

## Proof
**1. Binary-state representation.** Encode a matching by its open/closed state \(s_i\in\{0,1\}\) after each coordinate position: a selected odd upper coordinate makes \(0\to1\), a selected even lower coordinate makes \(1\to0\), and an unselected coordinate leaves the state unchanged. Start and end in state \(0\). The monotonicity restrictions at odd and even coordinates ensure a bijection with alternating matchings. The number of matchings after \(r\) upper–lower blocks is the \((0,0)\) entry of the \(r\)-th power of \(\begin{psmallmatrix}2&1\\1&1\end{psmallmatrix}\), hence it equals \(F_{2r+1}\).

Two matching vectors have the same sign on any coordinate at which both are nonzero. Thus
\[
\|\chi(M)-\chi(N)\|_2^2=|\operatorname{supp}(M)\triangle\operatorname{supp}(N)|.
\tag{4}
\]
Both matchings have even-sized support, so (4) is even. Introduce \(z\) as a weight for one mismatched coordinate; then \(q=z^2\) weights half the squared distance.

**2. Four-state transfer.** For an ordered pair of matchings, use four states in order \(00,01,10,11\). At an odd upper coordinate the permissible transitions, with one factor \(z\) for an unequal selection, are encoded by
\[
P(z)=\begin{pmatrix}
1&z&z&1\\0&1&0&z\\0&0&1&z\\0&0&0&1
\end{pmatrix}.
\]
At an even lower coordinate they are encoded by
\[
N(z)=\begin{pmatrix}
1&0&0&0\\z&1&0&0\\z&0&1&0\\1&z&z&1
\end{pmatrix}=P(z)^{\mathsf T}.
\]
Their two-coordinate transfer is
\[
T(z)=P(z)N(z)=\begin{pmatrix}
2+2z^2&2z&2z&1\\
2z&1+z^2&z^2&z\\
2z&z^2&1+z^2&z\\
1&z&z&1
\end{pmatrix}.
\tag{5}
\]
Since both matchings begin and finish closed,
\[
\boxed{W_r(q)=\bigl(T(\sqrt q)^r\bigr)_{00,00}.}
\tag{6}
\]
The factor \(z\) enters twice for each full mismatched pair because every matching has as many selected upper as selected lower coordinates. Thus the right side of (6) is a polynomial in \(z^2=q\), with the intended exponents.

**3. Cubic reduction.** The antisymmetric vector \((0,1,-1,0)\) is a \(T\)-eigenvector of eigenvalue \(1\) and is orthogonal to the starting coordinate vector \(e_{00}\). Direct determinant expansion yields
\[
\det(xI-T(z))=(x-1)\bigl(x^3-4(1+z^2)x^2+4(1+z^4)x-1\bigr).
\tag{7}
\]
The other three eigenmodes, which contain \(e_{00}\), satisfy the cubic relation. Cayley–Hamilton applied to the invariant symmetric-state subspace gives (1). From (5), \(W_0,W_1,W_2\) have the displayed exact values, and routine formal-series elimination of (1) gives (2).

**4. Extremal coefficients and complete support.** Taking \(q=1\) in (6) counts all ordered pairs, so \(W_r(1)=F_{2r+1}^2\). Taking \(q=0\) counts identical pairs and gives \([q^0]W_r=F_{2r+1}\). The degree of \(W_r\) is at most \(r\), since each of the \(2r\) coordinates contributes at most one to (4). The recurrence, using the three initial polynomials, proves inductively
\[
[q^r]W_r=2^r\quad(r\ge1),\qquad
[q^{r-1}]W_r=r^2 2^r\quad(r\ge2).
\tag{8}
\]
For the first identity, the top coefficient of \(4qW_{r-1}-4q^2W_{r-2}\) is \(4\cdot2^{r-1}-4\cdot2^{r-2}=2^r\); the other contributions have smaller degree. For the second, writing \(b_r=[q^{r-1}]W_r\), the next-to-top recurrence is \(b_r=4b_{r-1}+4\cdot2^{r-1}-4b_{r-2}\); the formula follows from the initial values, with the lower-degree boundary at \(r=3\) checked directly. Alternatively the same counts can be extracted from the rational function (2).

Every exponent \(0,1,\ldots,r\) occurs: compare the zero matching with the matching occupying the first \(k\) consecutive upper–lower blocks, which has squared length \(2k\). Subtracting the \(F_{2r+1}\) diagonal contributions and halving proves the unordered distinct-pair statements. For \(r\ge2\), \([q^{r-1}]\) is an off-diagonal coefficient. Convexity of Euclidean distance shows that the diameter of the full convex body is attained at vertices, so the asserted vertex diameter also equals the polytope diameter. (Only the enumerator itself concerns vertex pairs.)

**5. Gaussian fluctuations.** For each real \(q>0\), the symmetric matrix \(T(\sqrt q)\) has strictly positive entries. Its largest eigenvalue \(\lambda(q)>0\) is simple, with an analytic positive eigenprojection near \(q=1\). Because the initial vector has nonzero positive projection onto that eigenspace,
\[
W_r(e^t)=c(t)\lambda(e^t)^r\bigl(1+O(\rho^r)\bigr)
\tag{9}
\]
locally uniformly for sufficiently small complex \(t\), with analytic \(c(t)\), \(c(0)>0\), and \(0<\rho<1\). This follows from the spectral gap at the positive matrix \(T(1)\) and analytic spectral perturbation. The largest eigenvalue is the largest real root of
\[
\lambda^3-4(1+q)\lambda^2+4(1+q^2)\lambda-1=0.
\tag{10}
\]
At \(q=1\), \(\lambda(1)=(7+3\sqrt5)/2\). Differentiating (10) implicitly gives
\[
\left.\frac{d}{dt}\log\lambda(e^t)\right|_{t=0}=\frac{2(\sqrt5-1)}5=\mu,
\quad
\left.\frac{d^2}{dt^2}\log\lambda(e^t)\right|_{t=0}=\frac{22\sqrt5-30}{125}=\nu>0.
\tag{11}
\]
The moment generating function of \(K_r\) is \(W_r(e^t)/W_r(1)\). Substituting \(t=u/\sqrt{\nu r}\) into the Taylor expansion of (9), after subtracting \(\mu r\), yields the limiting moment generating function \(\exp(u^2/2)\). This proves the Gaussian limit (3). The probability of a diagonal ordered pair is \(1/F_{2r+1}\to0\), so conditioning on distinct endpoints and forgetting their order does not alter the limit.

## Verification
The standalone `verify.py` independently enumerates alternating matchings as integer bit masks and counts their pairwise Hamming distances, without using the matrix transfer. It agrees coefficient-for-coefficient with recurrence (1) for \(1\le r\le7\), checking 435,664 ordered pairs. Exact arithmetic also checks the total count and both extremal coefficients through \(r=16\). The executed program printed:

```
ALTERNATING_SHARD_CHORD_PASS checked_ordered_pairs=435664 max_r=16
```

The transfer characteristic polynomial and the first two derivatives of its dominant root were additionally checked symbolically with exact algebra. All finite computations are corroborative; equations (4)–(11), not a bounded enumeration, prove the unbounded statements.

## Relationship to prior work
Padrol, Pilaud, and Ritter (2020, Definition 39 and Proposition 40) establish the alternating-matching realization and the shard-polytope vertex description. Their focus is Minkowski summands, normal fans, and related combinatorial geometry, not the full Euclidean chord enumerator.

*A run-length formula for the Euclidean diameter of every shard polytope* establishes the diameter from the run structure; for an all-singleton alternating arc, that stronger-general-domain diameter theorem already implies \(\operatorname{diam}(P_r)^2=2r\). **The diameter alone is therefore not claimed as novel here.** The same published result does not give multiplicities of all chord lengths or a limit distribution. *Shard polytopes have a canonical vertex sphere with a balanced-prefix minimum-sphere criterion* gives all-vertex sphere information for general arcs, not pairwise distance multiplicities. *Four-state Euclidean distance spectrum and antipodal rigidity of linked type-C snake polytopes* gives the total chord enumerator of a related, **larger** zero–one feasible polytope. More precisely, if \(S=\{2,4,\ldots,2r-2\}\) and \(D=\{2,4,\ldots,2r\}\), translating \(P_r\) by \(\mathbf1_D\) identifies it with the rank-\(r\) face of the linked type-C interval polytope \([S,S\cup\{2r\}]\). The latter also has rank-\(r-1\) vertices, so its all-vertex chord enumerator mixes same-rank and cross-rank pairs and does not isolate (2). No source statement gives the needed rank-conditioned polynomial, near-top count, or Gaussian constants.

The later work *Skew shapes, Ehrhart positivity, and beyond* applies shard polytopes to Ehrhart counting, a different invariant. The closest identified published sources were compared by their actual implications rather than by titles alone. The search is bounded and does not certify worldwide uniqueness.

## Limitations
The complete chord formula is restricted to the fully alternating, singleton-run arc family, not all shard polytopes. The Gaussian law is for uniformly sampled vertices, not random supporting directions or volume measure. The explicit near-diameter coefficient is stated only for \(r\ge2\). The Euclidean metric depends on the original coordinate embedding. The original all-shard diameter theorem covers our diameter value, and that antecedent is fully credited. Unindexed equivalent distance enumerators may exist; independent historical-priority assessment has not been performed.

## References
1. Arnau Padrol, Vincent Pilaud, and Julian Ritter, *Shard Polytopes*, arXiv:2007.01008, first public version 2020-07-02, https://arxiv.org/abs/2007.01008.
2. *A run-length formula for the Euclidean diameter of every shard polytope*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-run-length-formula-for-the-euclidean-diameter-of-every-shard-p--4ffb07614719.
3. *Shard polytopes have a canonical vertex sphere with a balanced-prefix minimum-sphere criterion*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-shard-polytopes-have-a-canonical-vertex-sphere-with-a-balanced-p--6152ee04b3f8.
4. *Four-state Euclidean distance spectrum and antipodal rigidity of linked type-C snake polytopes*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-four-state-euclidean-distance-spectrum-and-antipodal-rigidity-of--0acaa0ef9409.
5. Luis Ferroni, Alejandro H. Morales, and Greta Panova, *Skew Shapes, Ehrhart Positivity and Beyond*, arXiv:2503.16403, https://arxiv.org/abs/2503.16403.
