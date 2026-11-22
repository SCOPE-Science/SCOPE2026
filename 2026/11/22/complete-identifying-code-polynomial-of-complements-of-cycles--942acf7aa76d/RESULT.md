# Complete identifying-code polynomial of complements of cycles

## Finding

Let \(n\ge5\). On the labelled vertex set \(\mathbb Z/n\mathbb Z\), let \(G_n=\overline{C_n}\), and let \(P_n(z)=\sum_{S}z^{|S|}\), summed over **all** ordinary radius-one identifying codes \(S\) of \(G_n\). An identifying code has pairwise distinct, nonempty traces \(N_{G_n}[v]\cap S\) for all vertices \(v\). For each integer \(m\ge3\), define
\[
A_m(z)=z^m+\sum_{r=1}^{\lfloor m/3\rfloor}\frac mr\binom{m-2r-1}{r-1}z^{m-r},
\qquad
B_m(z)=\sum_{r=0}^{\lfloor(m-4)/3\rfloor}m\binom{m-2r-4}{r}z^{m-r-2}.
\]
An empty sum is zero. The **complete labelled cardinality polynomial** is
\[
\boxed{P_n(z)=\begin{cases}A_n(z)+B_n(z),&n\text{ odd},\\ A_m(z)^2+2A_m(z)B_m(z),&n=2m\text{ even}.\end{cases}}
\]
The theorem is a **one-defective-edge correction** to the known open locating-dominating (OLD) polynomial of ordinary cycles. In the notation above, the known OLD polynomial is \(A_n\) for odd \(n\), and \(A_m^2\) for \(n=2m\). The additional \(B_n\) or \(2A_mB_m\) counts codes with exactly one unresolved edge of an auxiliary cycle system; these are not counted by the OLD polynomial.

Writing \(N_n=P_n(1)\), let \(\lambda=1.465571231876768\ldots\) be the unique real root greater than one of \(\lambda^3-\lambda^2-1=0\), and write \(\rho=\lambda^{-1}\) and \(c=(1-\rho)/(1+3\rho^2)=0.132544907950900\ldots\). Then
\[
\boxed{N_n=(1+cn)\lambda^n+O\bigl(n(1.2)^n\bigr)\qquad(n\to\infty).}
\]
Thus the one-defect correction is asymptotically a factor linear in \(n\) larger than the OLD-code count, for either parity. Example polynomials are \(P_5(z)=5z^3+5z^4+z^5\), \(P_6(z)=9z^4+6z^5+z^6\), and \(P_8(z)=32z^5+24z^6+8z^7+z^8\).

## Assumptions and scope

Graphs are finite, simple and undirected; all vertices are labelled, and sets are not identified under dihedral symmetries. The graph \(G_n\) contains an edge precisely when two distinct cycle vertices are nonconsecutive. The ordinary identifying-code definition uses **closed** neighborhoods and distinguishes every vertex, including vertices in the code. The restriction \(n\ge5\) matters: the four-cycle complement has closed twins and no identifying code. No unproved minimum-code statement is needed to derive the polynomial.

## Proof

**1. Reduction to a two-regular auxiliary graph.** For each vertex \(v\),
\[
N_{G_n}[v]=V(G_n)\setminus\{v-1,v+1\}.
\]
Set \(E_v=S\cap\{v-1,v+1\}\). Then \(N_{G_n}[v]\cap S=S\setminus E_v\), so two identifying traces coincide exactly when their corresponding \(E_v\)'s coincide. The \(n\) sets \(E_v\) are the intersections of \(S\) with the \(n\) distinct edges \(\{v-1,v+1\}\) of the auxiliary graph \(H_n\). Because \(n\ge5\), these edges are distinct and \(H_n\) is a cycle on \(n\) vertices when \(n\) is odd, or two disjoint cycles on \(m=n/2\) vertices when \(n\) is even. Indeed \(H_n\) connects residues differing by two.

For any simple graph whose connected components are cycles, two different edge-intersections \(S\cap e\) are equal only in one of two ways: two unoccupied edges both give the empty set, or two distinct edges meeting at an occupied vertex \(s\) both give the singleton \(\{s\}\) because their other endpoints are unoccupied. An intersection of size two identifies its edge uniquely. Consequently **all edge-intersections are distinct** exactly when \(H_n[V\setminus S]\) has at most one edge and \(H_n[S]\) has no isolated vertices. If all intersections are distinct then \(n\le2^{|S|}\), forcing \(|S|\ge3\) for \(n\ge5\); hence no identifying trace \(S\setminus E_v\) can be empty (each \(E_v\) has size at most two). This proves the criterion including the nonemptiness requirement.

**2. Cyclic words.** Represent membership in \(S\) by a cyclic binary word in each component of \(H_n\), with \(1\) for a selected vertex and \(0\) for an unselected one. A selected vertex is isolated precisely when the word contains a cyclic factor \(010\). An unoccupied edge is precisely an occurrence of \(00\). Therefore valid codes are exactly the words with no \(010\) and with at most one occurrence of \(00\) **across all components**. Such a word has either all zero-runs of length one or a unique zero-run of length two, and consecutive zero-runs are separated by at least two ones. The all-one word is allowed.

**3. Zero-run enumeration.** On a labelled cycle of length \(m\), if there are \(r\ge1\) singleton zero-runs and no \(00\), there are \(r\) cyclic gaps of ones, each of length at least two. Stars and bars counts \(\binom{m-2r-1}{r-1}\) ordered gap compositions. Choosing the label of the first zero gives \(m\) choices, while each final word was counted \(r\) times. Its count is therefore \(\frac mr\binom{m-2r-1}{r-1}\), and its code size is \(m-r\). Adding the all-one word gives \(A_m(z)\).

If there is exactly one double-zero run and \(r\ge0\) other singleton zero-runs, the double run has \(m\) possible labelled starts and the \(r+1\) successive one-gaps are at least two. Their sum is \(m-r-2\). Stars and bars gives exactly \(\binom{m-2r-4}{r}\) possibilities, with no overcount because the double run is unique. The code size is \(m-r-2\), giving \(B_m(z)\). The ranges of the sums are exactly the gap-feasibility bounds.

**4. Odd and even cycles.** If \(n\) is odd, the auxiliary graph has one component, so we may use zero or one double run, giving \(A_n+B_n\). For \(n=2m\), the two labelled components are distinct. Either neither contains a double run, giving \(A_m^2\), or exactly one contains a double run, giving \(2A_mB_m\). This proves the claimed polynomial for every integer \(n\ge5\), without recourse to finite experiments.

**5. Growth.** The gap formulas imply the exact ordinary generating functions
\[
\sum_{m\ge1}A_m(z)x^m=-x\frac{\partial}{\partial x}\log(1-zx-z^2x^3),\qquad
\sum_{m\ge4}B_m(z)x^m=x\frac{\partial}{\partial x}\left(\frac{z^2x^4}{1-zx-z^2x^3}\right),
\]
where the first identity uses the harmless formal extensions \(A_1(z)=z\), \(A_2(z)=z^2\). The second follows immediately by writing \(m=3r+4+s\) and summing \(\sum_{s\ge0}\binom{r+s}{r}(zx)^s\). At \(z=1\), \(f(x)=1-x-x^3\) has its unique smallest-modulus zero \(\rho\in(0,1)\), with \(f'(\rho)=-1-3\rho^2\). Simple-pole expansions give
\[
A_m(1)=\lambda^m+O(\beta^m),\qquad
B_m(1)=cm\lambda^m+O(m\beta^m),
\]
where \(\beta=\lambda^{-1/2}<1\) bounds the moduli of the other reciprocal roots, and \(c=\rho^3/(1+3\rho^2)=(1-\rho)/(1+3\rho^2)\). Combining these for both parities yields the displayed asymptotic; \(1.2>\sqrt{\lambda\beta}\) safely dominates the even-parity cross-terms.

## Verification

The standalone `verify.py` independently implements closed-neighborhood identification, the two local forbidden patterns, the binomial formulas, and a sixteen-state transfer trace for lengths \(5\) through \(16\). It compares **every** vertex subset at those lengths, not samples. An exact symbolic determinant computation additionally proves the transfer identity
\[
\det(I-xM)=\bigl(1-zx-z^2x^3+t(zx^2-x)\bigr)\bigl(1+z^3x^4-z^4x^6+t(z^2x^4-zx^2)\bigr),
\]
where \(M\) is explicitly constructed in `verify.py` using four-bit states and the variable \(t\) marking an empty edge trace. This is an independent algebraic cross-check, not the basis for the infinite proof. Install the listed SymPy dependency and run `python3 verify.py` from the extracted files. The checker returned `DETERMINANT_IDENTITY_OK`, twelve `EXHAUSTIVE_OK` lines, `BINOMIAL_AND_TRANSFER_OK`, and `VERIFY_OK`. All infinite claims follow from the mathematical proof above, not from the finite tests.

## Relationship to prior work

Nikandish, Khani Nasab and Dodonge (2020) explicitly determined **minimum identifying-code cardinalities** for complements of cycles and paths. Their published abstract does not state a complete all-size polynomial; their full text was unavailable for inspection, so priority relative to any unstated enumeration remains a residual risk. Gravier, Moncel and Semri (2006) treated minimum-radius-identifying-code sizes on cycles, including an odd-cycle case with equivalent exclusion-edge geometry; this is prior extremal information, not a claim of new minimum size here.

An accessible published census of **open locating-dominating codes of ordinary cycles** establishes exactly the \(A_n\) or \(A_m^2\) part above using cycle-square independent sets (see the prior published census listed below). It does **not** imply the additional, asymptotically dominant single-defect terms \(B_n\) or \(2A_mB_m\): those sets violate total domination in the auxiliary open-neighborhood model at precisely one edge. The 2015 complementary-prism study concerns the different graph \(C_n\overline{C_n}\), with twice as many vertices and added matching edges. The claim of new work is the full identifying-code polynomial of \(\overline{C_n}\), its explicit defect correction, and the common-parity growth law; neither the previously known OLD polynomial nor the known minimum-code values are represented as new.

## Limitations

The theorem applies to ordinary radius-one closed-neighborhood identifying codes on complements of simple cycles with \(n\ge5\), and counts labelled sets, not dihedral classes. It does not give optimal-code reconfiguration graphs or a classification for complements of arbitrary two-regular graphs. The inaccessible 2020 source could contain a stronger unpublished-in-abstract count; the current originality assessment is therefore provisional. No independent mathematical validation has been performed.

## References

1. R. Nikandish, O. Khani Nasab, E. Dodonge, *Minimum identifying codes in some graphs differing by matchings*, Discrete Mathematics, Algorithms and Applications **12** (2020), article 2050046, first published May 7, 2020. DOI: https://doi.org/10.1142/S1793830920500469.
2. S. Gravier, J. Moncel, A. Semri, *Identifying codes of cycles*, European Journal of Combinatorics **27** (2006), 767–776. DOI: https://doi.org/10.1016/j.ejc.2004.09.005.
3. *An exact census of open locating-dominating codes on cycles*, publicly available research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-an-exact-census-of-open-locating-dominating-codes-on-cycles--2cf44e5818fe.
4. M. R. Cappelle, E. M. M. Coelho, H. Coelho, L. D. Penso, D. Rautenbach, *Identifying Codes in the Complementary Prism of Cycles*, arXiv:1507.05083, initial public version July 17, 2015. https://arxiv.org/abs/1507.05083.
