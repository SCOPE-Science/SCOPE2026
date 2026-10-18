# Four-erasure spectra and sharp stability of quadratic-residue harmonic frames

## Finding
For every prime \(p\ge7\) with \(p\equiv3\pmod4\), the four-erasure Gram matrices of the quadratic-residue harmonic Parseval frame have exactly three possible characteristic polynomials, determined by the four-point induced Paley tournament. Their extremal eigenvalues admit a strict ordering: the unique worst-case erasure geometry is the strongly connected four-vertex tournament. If \(y_p\) is the largest real root of
\[
P_S(y)=y^4-6(p+1)y^2-8(p-1)y+p^2+14p-3,
\]
then the **sharp universal lower frame bound** after any four coefficient erasures is
\[
L_p=\frac{p+1-y_p}{2p}>0.
\]
Equality holds for precisely \(p(p-1)(p-3)(p+1)/64\) unordered four-element erasure sets, a fraction \(3(p+1)/(8(p-2))\) of all \(\binom p4\) possible sets. These are exactly the sets inducing a strongly connected four-vertex Paley tournament. The complete spectral and multiplicity classification is stated below; the already-published count of transitive Paley subtournaments is included only for comparison, not claimed as independently new.

## Assumptions and scope
Let \(p\) be any rational prime satisfying \(p\equiv3\pmod4\) and \(p\ge7\). Let \(D\subset\mathbb F_p^{\times}\) be its nonzero quadratic residues, and \(k=(p-1)/2\). Equip \(\mathbb C^D\) with its standard inner product. For \(a\in\mathbb F_p\), define
\[
f_a(d)=p^{-1/2}\exp(2\pi i da/p),\qquad d\in D.
\]
These \(p\) vectors form a Parseval frame: \(\sum_{a\in\mathbb F_p}f_af_a^*=I_k\). For an unordered four-point set \(B\subset\mathbb F_p\), let \(G_B=(\langle f_a,f_b\rangle)_{a,b\in B}\) and let \(S_{B^c}=\sum_{a\notin B}f_af_a^*\) be the retained frame operator. The Paley tournament on \(\mathbb F_p\) has an arrow \(a\to b\) when \(b-a\) is a nonzero square.

The four induced tournament types, classified by their sorted outdegree sequences, are \(T:(0,1,2,3)\) (transitive), \(O:(1,1,1,3)\) (one source above a triangle), \(I:(0,2,2,2)\) (one sink below a triangle), and \(S:(1,1,2,2)\) (strongly connected). Type \(T\) does not occur for \(p=7\). No genericity or random-erasure assumption is imposed.

Define the three monic polynomials
\[
\begin{aligned}
P_T(y)&=y^4-6(p+1)y^2+8(p+1)y+(p-3)(p+1),\\
P_O(y)&=y^4-6(p+1)y^2+8y+9p^2+6p-3,\\
P_S(y)&=y^4-6(p+1)y^2-8(p-1)y+p^2+14p-3.
\end{aligned}
\]
For type \(T\), \(O\) or \(I\), \(S\), respectively, the complete multiset of four eigenvalues of \(G_B\) is \(\{(p-1+y)/(2p):P_T(y)=0\}\), \(\{(p-1+y)/(2p):P_O(y)=0\}\), or \(\{(p-1+y)/(2p):P_S(y)=0\}\), with algebraic multiplicities. In particular, \(P_O(y)=((y+1)^2-(3p+4))((y-1)^2-3p)\).

The exact numbers of unordered four-point sets of these types are
\[
\begin{aligned}
n_T&=p(p-1)(p-3)(p-7)/64,\\
n_O=n_I&=p(p-1)(p-3)(p+1)/192,\\
n_S&=p(p-1)(p-3)(p+1)/64.
\end{aligned}
\]
For \(p\ge11\), the largest roots satisfy \(y_S>y_T>y_O=y_I\); for \(p=7\), \(y_S>y_O=y_I\). The smallest eigenvalue of \(S_{B^c}\) is \(1-\lambda_{\max}(G_B)\). The stated sharp bound and its complete equality classification follow.

## Proof
**1. Parseval normalization and Gauss reduction.** Character orthogonality gives
\[
\sum_{a\in\mathbb F_p} f_a(d)\overline{f_a(e)}
 =p^{-1}\sum_{a\in\mathbb F_p}\exp(2\pi i a(d-e)/p)=\delta_{d,e}
\]
for all \(d,e\in D\). Let \(\chi\) be the quadratic character extended by \(\chi(0)=0\). For distinct \(a,b\), the usual quadratic Gauss sum with positive additive character has value \(i\sqrt p\), so
\[
\langle f_a,f_b\rangle=\frac{-1+i\sqrt p\chi(b-a)}{2p},
\qquad
\langle f_a,f_a\rangle=\frac{p-1}{2p}.
\]
Consequently \(G_B=((p-1)I_4+H_B)/(2p)\), where \((H_B)_{aa}=0\) and \((H_B)_{ab}=-1+i\sqrt p\chi(b-a)\) off the diagonal. This \(H_B\) is Hermitian.

**2. Four tournament matrices and exact characteristic polynomials.** Every tournament on four vertices has exactly one of the four outdegree sequences listed above. Up to simultaneous row and column permutations, its skew-sign matrix \(\sigma_{ij}=\chi(b_j-b_i)\) is uniquely specified by the six upper-triangular entries in order \((01,02,03,12,13,23)\):
\[
\begin{array}{c|c}
T &(+1,+1,+1,-1,+1,+1)\\
O &(+1,-1,-1,+1,-1,-1)\\
I &(+1,-1,+1,+1,+1,+1)\\
S &(+1,-1,+1,+1,-1,+1).
\end{array}
\]
Set \(\sigma_{ji}=-\sigma_{ij}\), and substitute \((H_B)_{ij}=-1+i\sqrt p\sigma_{ij}\) for \(i\ne j\). Direct expansion of the four \(4\times4\) determinants \(\det(yI_4-H_B)\) yields, respectively, \(P_T,P_O,P_O,P_S\). The attached standalone checker verifies **these determinant identities formally for arbitrary indeterminate \(p\)** using only integer polynomial arithmetic and the relation \((i\sqrt p)^2=-p\), not floating point sampling. As spectral shifts and scales preserve eigenvalues, the classification of \(G_B\) follows.

**3. Enumeration of each type for all primes.** In the Paley tournament every vertex has outdegree \(d=(p-1)/2\). Every distinct pair of vertices has exactly \(t=(p-3)/4\) common outneighbors, by \(\sum_x\chi(x-a)\chi(x-b)=-1\). The outneighborhood and inneighborhood of each vertex therefore induce regular tournaments of order \(d=2t+1\) and outdegree \(t\). A regular tournament on \(d\) vertices has \(d\binom t2\) transitive triangles (count each at its unique source) and \(d(d^2-1)/24\) directed cyclic triangles. Choosing a source for a four-point transitive tournament gives \(n_T=p d\binom t2\). Choosing the unique global source of an \(O\)-type tournament and then a cyclic triangle among its outneighbors gives \(n_O=pd(d^2-1)/24\). Reversing all arrows gives \(n_I=n_O\). Subtraction from \(\binom p4\) gives \(n_S\). These expressions simplify to the formulas above. The transitive count \(n_T\) was already obtained in published Paley-tournament work and is not an originality component of this finding.

**4. Exact worst-case comparison.** Write \(y_T,y_O,y_S\) for largest roots when the corresponding type occurs. Direct subtraction gives
\[
P_T(y)-P_S(y)=16p(y-1),\qquad
P_O(y)-P_S(y)=8p(y+p-1).
\]
The largest eigenvalue of any \(H_B\) is at least \(\sqrt{p+1}>1\), by interlacing with a two-row principal submatrix. Hence \(P_S(y_T)<0\) and \(P_S(y_O)<0\). Because \(P_S(y)\to+\infty\) for \(y\to+\infty\), it has a root strictly larger than either \(y_T\) or \(y_O\); thus \(y_S\) is strictly maximal. Moreover \(P_T(y)-P_O(y)=8p(y-p-1)\). For \(p\ge11\), every \(H_B\) has maximum eigenvalue at most \(3\sqrt{p+1}<p+1\), by its row-sum norm bound. Evaluating this last identity at \(y_O\) proves \(y_T>y_O\). Thus the strongly connected type is **exactly** the set of worst four-erasure patterns.

**5. Positivity and the sharp retained operator bound.** On \(y\ge2\sqrt{p+1}\), the derivative \(P_S'(y)=4y(y^2-3(p+1))-8(p-1)\) is positive. Direct substitution gives
\[
P_S(2\sqrt{p+1})=-7p^2-2p-11-16(p-1)\sqrt{p+1}<0
\]
and \(P_S(p+1)=p^2(p^2-2p-19)>0\) for every allowed \(p\). Hence \(y_S\) is the unique root in \((2\sqrt{p+1},p+1)\), showing \(L_p>0\). The nonzero eigenvalues of \(\sum_{a\in B}f_af_a^*\) coincide with those of \(G_B\), and its operator norm equals \(\lambda_{\max}(G_B)\). Therefore \(\lambda_{\min}(S_{B^c})=1-\lambda_{\max}(G_B)\), which is minimized precisely by type \(S\) and equals \(L_p\). Since \(n_S>0\), equality is attained for exactly the stated number of erasure patterns.

## Verification
The complete self-contained verifier is `verify.py`. Run `python3 verify.py` using Python 3 without any third-party packages. It reconstructs all four tournament representatives, expands each characteristic polynomial **symbolically in the indeterminate \(p\)** over \(\mathbb Z[p,i\sqrt p]/((i\sqrt p)^2+p)\), and compares with the asserted coefficients. It also checks the precise polynomial subtraction identities giving spectral dominance. Separately, it exhaustively enumerates all \(\binom p4\) erasure sets for \(p=7,11,19,23,31\), classifies them by tournament outdegrees, and exactly verifies all multiplicity formulas. The total number of checked four-element sets in these five primes is \(35+330+3876+8855+31465=44561\). Formal determinant expansion and the unrestricted mathematical argument, not this finite census, establish the arbitrary-prime theorem.

## Relationship to prior work
Renes introduced Paley-tournament equiangular tight frames and explicit related Gram matrices (arXiv:math/0408287, original public date 2004-08-20); this construction and the underlying Gauss sums are **prior**, not new. Hoffman and Solazzo (arXiv:1107.2267) classify uniformity of complex equiangular tight frames under three and four erasures and discuss four-row compressions, but do **not** supply the quadratic-residue harmonic frame's three quartic spectral laws, sharp four-erasure lower bound, or extremizer counts. Fickus, Iverson, Jasper and Mixon (arXiv:2112.14267, publicly submitted 2021-12-28; primary MSC 42C15) study harmonic Grassmannian constructions and Gauss sums, not this adversarial four-erasure classification. McCarthy and Springfield (arXiv:2311.02135, 2023) give the transitive Paley-subtournament count \(n_T\) as a special case: that count is explicitly **not** claimed as new. Their tournament enumeration does not give the Gram spectral classification or determine which type minimizes frame stability. The additional \(O,I,S\) counts follow simply from double regularity and are auxiliary to the spectral result. General uniform-subframe-bounds literature supplies a broader formal context, but no covering Paley four-erasure formula was found among the inspected accessible materials.

## Limitations
Only rational primes \(p\equiv3\pmod4\) are covered; no assertion is made for prime powers, primes of other congruence classes, weighted or non-quadratic-residue windows, or five or more erasures. The claim classifies four-erasure Gram spectra and the sharp retained **lower** bound, not the complete spectrum of a retained frame at arbitrary larger erasure sets. Full-text checks do not exclude an unindexed equivalent statement in older tournament matrix or ETF literature; independent audit and validation have not been performed. Numerical examples and finite enumeration alone are not substitutes for the algebraic proof.

## References
1. J. M. Renes, *Equiangular Tight Frames from Paley Tournaments*, arXiv:math/0408287 (first posted 2004-08-20), https://arxiv.org/html/math/0408287v2.
2. T. R. Hoffman and J. P. Solazzo, *Complex Equiangular Tight Frames and Erasures*, arXiv:1107.2267 (2011), https://arxiv.org/html/1107.2267v1.
3. M. Fickus, J. W. Iverson, J. Jasper and D. G. Mixon, *Harmonic Grassmannian codes*, arXiv:2112.14267 (first posted 2021-12-28), https://arxiv.org/html/2112.14267v1.
4. D. McCarthy and M. Springfield, *Transitive subtournaments of k-th power Paley digraphs and improved lower bounds for Ramsey numbers*, arXiv:2311.02135 (first posted 2023-11-03), https://arxiv.org/html/2311.02135v2.
5. Q. Cheng, F. Lv and W. Sun, *Frames of uniform subframe bounds with applications to erasures*, Linear Algebra and its Applications 555 (2018), https://doi.org/10.1016/j.laa.2018.05.025 (abstract accessed; complete text not inspected).
