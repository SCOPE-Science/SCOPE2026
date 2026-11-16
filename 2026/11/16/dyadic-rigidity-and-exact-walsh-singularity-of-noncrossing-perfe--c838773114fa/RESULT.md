# Dyadic rigidity and exact Walsh singularity of noncrossing perfect matchings

## Finding

For every integer \(n\ge1\), take \(2n\) labelled vertices in convex position and the noncrossing perfect matchings among them. Regard a matching as an indicator in \(\mathbb F_2^{E_n}\), where \(E_n\) consists of all \(n^2\) edges connecting vertices of opposite parity. For an arbitrary edge-sign assignment \(b\in\mathbb F_2^{E_n}\), let
\[
W_n(b)=\sum_{M\in\mathcal M_n}(-1)^{\langle b,\mathbf1_M\rangle}.
\]
Writing \(s_2(j)\) for the binary digit sum of the nonnegative integer \(j\), the *complete Fourier content* is
\[
\gcd\{W_n(b):b\in\mathbb F_2^{E_n}\}
     =2^{s_2(n+1)-1}.
\]
In addition,
\[
\big(\exists b:W_n(b)=0\big)
 \quad\Longleftrightarrow\quad n+1\text{ is not a power of two}.
\]
For each singular length \(n\), there are at least \(2^{2n-1}\) different zero frequencies. Consequently convolution by \(\mathbf1_{\mathcal M_n}\) on \(\mathbb F_2^{E_n}\) is invertible if and only if \(n=2^k-1\) for some integer \(k\ge1\).

## Assumptions and scope

The vertices are numbered \(0,1,\ldots,2n-1\) counterclockwise. A chord is allowed if its endpoints have opposite parity; these are exactly the chords that can occur in a noncrossing perfect matching. The set \(\mathcal M_n\) contains *all* noncrossing perfect matchings, including the boundary-edge matchings; it has cardinality \(C_n=\binom{2n}{n}/(n+1)\). The unnormalized Walsh convention is used. When discussing the gcd, it is the nonnegative gcd of all integral coefficients, and zeros do not affect that gcd. A zero-frequency lower bound concerns the full frequency cube with \(n^2\) coordinates, not frequencies modulo vertex switching.

## Proof

**Step 1: Catalan valuation.** Let \(v_2(a)\) be the exponent of two dividing a nonzero integer \(a\). Legendre's factorial valuation gives \(v_2(m!)=m-s_2(m)\). Applying this to \(C_j=(2j)!/(j!j!(j+1))\), we obtain \(v_2(C_j)=s_2(j)-v_2(j+1)\). Adding one to a binary integer changes its digit sum by \(s_2(j+1)=s_2(j)+1-v_2(j+1)\), so
\[
v_2(C_j)=s_2(j+1)-1\qquad (j\ge0).
\]
Equivalently this is the classical Catalan two-adic valuation formula. In particular, \(C_j\) is odd precisely for \(j=2^k-1\) (including \(j=0\) if needed).

**Step 2: Every signing has the stated divisibility.** Fix an arbitrary set \(B\subseteq E_n\) of negative chords, so the sign of chord \(e\) is \(1-2\mathbf1_{e\in B}\). Expand the weight of each matching and interchange sums:
\[
W_n(B)=\sum_{S\subseteq B}(-2)^{|S|}N_n(S),\qquad
N_n(S)=\#\{M\in\mathcal M_n:S\subseteq M\}.
\]
If the prescribed chords \(S\) intersect or share an endpoint, then \(N_n(S)=0\). Otherwise put \(r=|S|\). The \(r\) disjoint noncrossing chords divide the polygon into \(r+1\) regions. An extension must match all remaining vertices within each region, independently. If some region has an odd number of remaining vertices, no extension exists. In the other cases the regions contain \(2m_0,\ldots,2m_r\) unmatched vertices with \(m_i\ge0\) and \(\sum_{i=0}^{r}m_i=n-r\); their noncrossing matchings are counted by Catalan numbers, so
\[
N_n(S)=\prod_{i=0}^{r}C_{m_i}.
\]
Thus every nonzero summand in the expansion has valuation
\[
\begin{aligned}
v_2\big(2^rN_n(S)\big)
 &=r+\sum_{i=0}^{r}\big(s_2(m_i+1)-1\big)\\
 &=\sum_{i=0}^{r}s_2(m_i+1)-1\\
 &\ge s_2\!\left(\sum_{i=0}^{r}(m_i+1)\right)-1
 =s_2(n+1)-1.
\end{aligned}
\]
The inequality is binary-digit-sum subadditivity, valid for arbitrary nonnegative integer summands. This proves divisibility by \(2^{s_2(n+1)-1}\) of *every* Walsh coefficient. At \(B=\varnothing\), the coefficient equals \(C_n\), whose exact two-adic valuation was computed in Step 1; hence the gcd has precisely this exponent of two. **There can be no odd prime divisor of the gcd**: if an odd prime \(p\) divided every Walsh coefficient, Walsh inversion over \(\mathbb F_p\) (where the group order \(2^{n^2}\) is invertible) would imply that the matching indicator vanishes at every input modulo \(p\). But the indicator equals one at every matching incidence vector. Thus the gcd is exactly the claimed power of two.

**Step 3: Existence and nonexistence of zeros.** At \(n=2^k-1\) the Catalan count is odd; every signed sum has the same odd parity and is therefore nonzero.

For every other \(n\) we construct zero signs by induction on \(n\). Reflect the labelled polygon by the involution \(R(j)=-j\pmod{2n}\); it fixes vertices \(0\) and \(n\). Assign root-chord signs \(\sigma(0,j)=+1\) for odd \(j<n\), and \(\sigma(0,j)=-1\) for odd \(j>n\). For every nonroot chord impose \(\sigma(R(e))=\sigma(e)\); the remaining values can be assigned \(+1\) unless specified below.

Every matching pairs vertex \(0\) to a unique odd \(j\). The signed contribution for the root chord \((0,j)\) is the root sign multiplied by the signed noncrossing matching sums on the two arcs cut off by that chord. Reflection interchanges the contributions for \(j\) and \(2n-j\) and reverses exactly the root sign, so these contributions cancel in pairs. If \(n\) is even there is no odd fixed choice \(j=n\), hence the complete signed sum is zero.

If \(n\) is odd but not one less than a power of two, write \(n=2m+1\). Then \(m+1=(n+1)/2\) is not a power of two. By induction obtain a zero signing on a convex polygon with \(2m\) vertices. Place those negative signs inside the consecutive arc \(1,2,\ldots,n-1\), and place their reflected negatives inside \(n+1,\ldots,2n-1\). Set all other nonroot chords to positive signs, and retain the antisymmetric root signs above. For the unique fixed root chord \((0,n)\), the two arcs independently have signed matching sums zero, so its contribution vanishes as well. This supplies a zero signing for every non-Mersenne \(n\), and establishes the equivalence.

**Step 4: Count distinct zeros.** Switching the sign on every chord incident to any chosen vertex changes each matching weight by the same factor, because each perfect matching uses exactly one chord incident to every vertex. Therefore every vertex-switch translate of a zero signing remains zero. The graph of eligible chords is the connected complete bipartite graph \(K_{n,n}\), so the vertex-switch action on signings has kernel exactly the two constant vertex-sign choices and each orbit has cardinality \(2^{2n-1}\). This yields the stated zero-frequency lower bound.

**Step 5: Operator interpretation.** Walsh characters diagonalize convolution by the indicator on the finite abelian group \(\mathbb F_2^{E_n}\), with eigenvalues precisely \(W_n(b)\). Therefore convolution is invertible exactly when all coefficients are nonzero, completing the theorem.

## Verification

The accompanying standalone program `check.py` uses integer arithmetic and no external dependencies. It enumerates *all* edge-sign frequencies for \(n=1,2,3,4\), checks complete signed matching enumeration for \(n\le3\), verifies recursive zero witnesses for every eligible \(n\le131\) and for \(n=256\), checks the vertex-switch orbit bound at \(n=2,4,5\), and checks divisibility for additional randomized signings through \(n=32\). The successful output ends with `NONCROSSING_WALSH_EXACT_PASS`. These are finite checks corroborating the proof, not a substitute for its all-length argument or independent validation. Run with `python3 check.py`.

## Relationship to prior work

The Catalan enumeration of convex noncrossing matchings and the Catalan valuation formula are classical inputs, **not newly claimed**. Postnikov and Sagan (2006) prove two-adic valuation results for Dyck-path weights drawn from a single height-indexed sequence subject to finite-difference divisibility conditions; these weights do not represent every independently signed polygon chord. Kemp, Mahlburg, Rattan and Smyth (2009) study counts of noncrossing pairings on bit strings; Asinowski (2015) studies the Catalan minimum among plane point sets; Gao and Gu (2019) extend height-dependent weighted-Catalan divisibility. Their inspected formulas do not assert the exact gcd of **all independent edge-sign Walsh coefficients**, the zero-freeness classification, or the vertex-switch multiplicity lower bound.

Related work on first-degree Fourier sampling over noncrossing matchings concerns the Gram matrix of low-degree characters, rather than the all-character Fourier transform of the matching indicator. The current conclusions are not obtained by specializing that Gram rank statement. Full historical priority beyond the inspected sources is not established.

## Limitations

The theorem applies to unweighted indicators of noncrossing perfect matchings of convex polygons and edge signs in \(\{+1,-1\}\). It does not compute exact zero multiplicities, the minimum positive coefficient, complex-weighted analogues or endpoint \(\ell^1\) inverse norms. A general signed-Catalan identity in earlier literature could overlap with some of the divisibility argument; this has not been exhaustively ruled out. The proof and finite checks have not undergone an independent audit.

## References

1. A. Postnikov and B. E. Sagan, *What power of two divides a weighted Catalan number?*, arXiv:math/0601339, first public version January 13, 2006, especially Theorems 1.1 and 2.1; https://arxiv.org/abs/math/0601339.
2. A. Kemp, K. Mahlburg, A. Rattan, and C. Smyth, *Enumeration of non-crossing pairings on bit strings*, arXiv:0906.2183, first public version June 11, 2009; https://arxiv.org/abs/0906.2183.
3. A. Asinowski, *The number of non-crossing perfect plane matchings is minimized (almost) only by point sets in convex position*, arXiv:1502.05332, first public version February 18, 2015; https://arxiv.org/abs/1502.05332.
4. Y. Gao and Y. Gu, *Arithmetic of weighted Catalan numbers*, arXiv:1908.03914, first public version 2019; https://arxiv.org/abs/1908.03914.
