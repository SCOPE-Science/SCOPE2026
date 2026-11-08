# Arm-permutation Lefschetz characters of the Braun–Hough comb complexes

## Finding

For all integers \(n\geq0\) and \(m\geq2\), let \(\Delta_n^m\) be the comb graph defined below, and let \(S_m\) permute its \(m\) arms. For every \(\sigma\in S_m\), put \(c(\sigma)\) equal to the number of cycles in its arm permutation, counting fixed points. The reduced Lefschetz character of the action on the ordinary independence complex is

\[
\mathcal L_{n,m}(\sigma)=\sum_{q\geq0}(-1)^q\operatorname{tr}\!\left(\sigma\mid\widetilde H_q(\operatorname{Ind}(\Delta_n^m);\mathbb Q)\right)
=\begin{cases}E_n,&c(\sigma)\text{ even},\\O_n,&c(\sigma)\text{ odd},\end{cases}
\]

where \(E_0=1\), \(E_1=-2\), \(E_2=1\), \(E_n=E_{n-3}-E_{n-2}-E_{n-1}\) for \(n\geq3\), and \(O_n=0\) for odd \(n\) while \(O_{2r}=(-1)^r\). Equivalently, their generating functions are

\[
\sum_{n\geq0}E_nt^n=\frac{1-t}{1+t+t^2-t^3},\qquad
\sum_{n\geq0}O_nt^n=\frac{1}{1+t^2}.
\]

In the rational representation ring of \(S_m\), the entire alternating reduced homology module is

\[
\boxed{\displaystyle\sum_{q\geq0}(-1)^q[\widetilde H_q]=
\frac{E_n+O_n}{2}[\mathbf1]+\frac{(-1)^m(E_n-O_n)}2[\operatorname{sgn}].}
\]

In particular, every other irreducible representation has zero **alternating** multiplicity. At \(n=2\), the already-known sphere homotopy type upgrades to an integral equivariant statement:

\[
\widetilde H_q(\operatorname{Ind}(\Delta_2^m);\mathbb Z)
\cong\begin{cases}\mathbb Z_{\operatorname{sgn}},&q=m,\\0,&q\ne m.\end{cases}
\]

Here \(\mathbb Z_{\operatorname{sgn}}\) is the rank-one lattice on which an arm permutation acts by its sign.

## Assumptions and scope

The finite simple graph \(\Delta_n^m\) has two pole vertices \(a,b\), central vertices \(z_k\) for \(1\leq k\leq n\), and arm vertices \(p_{j,k}\) for \(1\leq j\leq m\) and \(1\leq k\leq n+1\). Its edges, and no others, are \(ap_{j,1}\), \(bp_{j,n+1}\), \(p_{j,k}p_{j,k+1}\), \(z_kp_{j,k}\), and \(z_kp_{j,k+1}\) for every applicable pair \((j,k)\). The group \(S_m\) fixes \(a,b,z_k\) and maps \(p_{j,k}\) to \(p_{\sigma(j),k}\). All homology is reduced simplicial homology, and the zero-dimensional convention includes the augmented empty face when computing reduced Lefschetz numbers. For \(n=0\), there are no central vertices. The auxiliary one-arm graph \(\Delta_n^1\) uses the same edge definition but is not asserted to be in the original \(m\geq2\) family.

## Proof

**1. Equivariant simplicial trace.** A basis face in the augmented reduced chain complex is fixed by \(\sigma\) as an unoriented set precisely when it is a union of \(\sigma\)-orbits of vertices. If a nonempty invariant face is a union of \(r\) vertex orbits with total size \(s\), then its orientation sign under \(\sigma\) is \((-1)^{s-r}\). Its contribution in degree \(s-1\) to the alternating chain trace is therefore \((-1)^{s-1}(-1)^{s-r}=(-1)^{r-1}\). The empty face contributes \(-1\). Hopf's trace formula identifies this augmented alternating chain trace with the reduced homological Lefschetz number; no assumption about homology concentration is used.

**2. Orbit quotient.** An arm orbit under \(\sigma\) consists of vertices \(p_{j,k}\) at the same position \(k\) across arms belonging to one permutation cycle; no two vertices within that orbit are adjacent. Pole and center vertices are fixed singleton orbits. Between different vertex orbits there is an edge exactly when the corresponding orbit-vertices are adjacent in \(\Delta_n^{c(\sigma)}\). Thus invariant independent faces correspond bijectively to independent subsets of \(\Delta_n^{c(\sigma)}\), with each selected orbit contributing one factor \(-1\). Writing \(I(G;t)=\sum_{A\in\operatorname{Ind}(G)}t^{|A|}\), we obtain the exact identity

\[
\mathcal L_{n,m}(\sigma)=-I(\Delta_n^{c(\sigma)};-1).
\]

**3. The odd-cycle-count value.** For the auxiliary one-arm graph, sum \(I(\Delta_n^1;-1)\) over choices of the vertices \(z_k\) and the poles. If neither \(p_{1,k}\) nor \(p_{1,k+1}\) is selected, the free vertex \(z_k\) causes cancellation, so only alternating selections of consecutive arm vertices survive. Similarly the free poles force both endpoints \(p_{1,1}\) and \(p_{1,n+1}\) to be selected. This occurs only for even \(n\), when exactly \(n/2+1\) arm vertices are selected, contributing \((-1)^{n/2+1}\). Hence \(-I(\Delta_n^1;-1)=O_n\). This also holds at \(n=0\), where the unique surviving choice selects the sole arm vertex.

**4. Dependence on parity, and the even-cycle-count value.** Braun and Hough's published comb matching (Corollary 4.3 and Proposition 4.1 of the 2016 first version cited below) proves for every \(r\geq2\) that the reduced Euler number \(F_n^{(r)}=-I(\Delta_n^r;-1)\) obeys

\[
F_n^{(r)}=(1+(-1)^r)F_{n-3}^{(r)}+(-1)^{r+1}F_{n-4}^{(r)}\quad(n\geq4).
\]

Its initial values are \((1,-2,1,2)\) for even \(r\) and \((1,0,-1,0)\) for odd \(r\). Thus \(F_n^{(r)}\) depends only on the parity of \(r\). In the odd case its recurrence is period four, agreeing with the one-arm calculation. In the even case it obeys the equivalent cubic recursion defining \(E_n\). Independently, for \(r=2\), \(\Delta_n^2\) is the line graph of the two-row ladder with \(n+2\) columns; signed matchings are counted by the transfer matrix

\[
T=\begin{pmatrix}0&-1&-1&1\\1&0&-1&0\\1&-1&0&0\\1&0&0&0\end{pmatrix}.
\]

With boundary states \(0,1,2,3\) indicating occupied vertices from the previous column, a horizontal matching contributes a sign per chosen edge and a vertical matching contributes an additional sign, giving this matrix directly. The identity \(F_n^{(2)}=-(T^{n+2})_{00}\) and elementary rational matrix inversion yield \(-\bigl(T^2(1-tT)^{-1}\bigr)_{00}=(1-t)/(1+t+t^2-t^3)\). The orbit quotient now gives the first boxed statement in full generality.

**5. Representation-ring and integral consequences.** The sign of a permutation of \(m\) letters with \(c\) cycles is \((-1)^{m-c}\). Therefore the character equals \(E_n\) when \(\operatorname{sgn}(\sigma)=(-1)^m\) and equals \(O_n\) otherwise. Solving for its trivial and sign components gives exactly the displayed virtual representation. The coefficients are integers since the two integer-valued sequences have matching parity (by their stated recursions and initial values). At \(n=2\), \(E_2=1\) and \(O_2=-1\), so the reduced Lefschetz trace is \((-1)^m\operatorname{sgn}(\sigma)\). The known integral homotopy equivalence \(\operatorname{Ind}(\Delta_2^m)\simeq S^m\) implies reduced homology is free of rank one in degree \(m\) only. Thus its genuine integral action is the sign character, as claimed. The nonequivariant homotopy equivalence is not claimed to be equivariant.

## Verification

The accompanying standalone Python program constructs \(\Delta_n^m\), enumerates every independent face recursively, and computes signed simplicial chain traces directly by permutation inversions; the empty face is included with reduced sign \(-1\). It checks **498 individual group elements** in **18 parameter cases**, including all permutations of up to five arms, against the closed formula, and independently computes a signed matching transfer for the even-branch sequence through degree 28. Every check passed. These finite checks corroborate, but do not replace, the uniform proof for arbitrary \(m,n\).

## Relationship to prior work

Braun and Hough established the nonequivariant Euler recurrences and the sphere type at \(n=2\); they explicitly asked for the \(S_m\)-module structure of the homology. Matsushita subsequently established non-equivariant wedge-of-spheres homotopy types for the full comb family, with a different index convention: Matsushita's graph parameter is two greater than the \(n\) used here. Neither work provides the entire arm-permutation alternating character, its uniform trivial/sign support, or the integral action at \(n=2\). The Euler recurrences and sphere type are cited prior premises, not newly claimed results.

## Limitations

The representation-ring identity is **virtual**: it determines an alternating sum, not the full separately graded \(S_m\)-module when \(n\ne2\), and distinct higher irreducibles may cancel across homological degrees. It is not an equivariant homotopy classification. A pre-existing equivalent computation absent from the inspected literature cannot be excluded. The result uses standard rational Lefschetz theory; only the \(n=2\) action is identified integrally.

## References

1. B. Braun and W. K. Hough, *Matching and Independence Complexes Related to Small Grids*, arXiv:1606.01204v1 (public 2016-06-03), especially Sections 1, 4 and 5. https://arxiv.org/html/1606.01204v1
2. T. Matsushita, *Matching Complexes of Small Grids*, arXiv:1812.11000 (first public 2018-12-28), especially Theorem 1.2 and Proposition 4.1. https://arxiv.org/pdf/1812.11000
