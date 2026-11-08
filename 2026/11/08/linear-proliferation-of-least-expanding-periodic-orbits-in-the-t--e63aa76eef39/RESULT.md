# Linear proliferation of least-expanding periodic orbits in the three-dimensional twisted baker map

## Finding
For the three-dimensional twisted baker map, the optimal weakest periodic multiplier at every sufficiently long iterate has a simple exact value, but—unlike the planar case—its multiplicity grows quadratically with period.

For every integer \(n\geq1\), let \(\mathcal P_n\) be the nontrivial fixed points of \(F^n\), and define the least normalized multiplier
\[
\chi_n(x)=\min\bigl\{|\lambda|^{1/n}:\lambda\in\operatorname{spec}(DF^n(x))\bigr\}.
\]
Then, for every \(n\geq4\),
\[
\boxed{\min_{x\in\mathcal P_n}\chi_n(x)=2^{1/n}.}
\]
**Exactly \(n(n-3)\) points attain this minimum, grouped into precisely \(n-3\) distinct primitive cycles of least period \(n\).** They are characterized by their cyclic symbolic itineraries: exactly three symbols are \(R\), and at least one of the three cyclic gaps between successive \(R\)'s contains no \(L\). Equivalently, the symbolic itinerary has three right visits and at least one consecutive pair of right visits, allowing cyclic wraparound. For \(1\leq n\leq3\), every nontrivial fixed point of \(F^n\) has \(\chi_n=2^{1/3}\).

More explicitly, if an itinerary has \(t>0\) right visits, then for \(t\not\equiv0\pmod3\), every multiplier modulus of its derivative return equals \(2^{n/3}\). If \(t=3q\), let \(c_0,c_1,c_2\) count left visits with respectively \(0,1,2\) preceding right visits modulo three. The three derivative eigenvalue moduli are exactly
\[
\boxed{\bigl\{2^{q+c_0},\ 2^{q+c_1},\ 2^{q+c_2}\bigr\}.}
\]
This formula and the cyclic-gap count give the sharp bound and its full equality classification.

## Assumptions and scope
Let \(X=[-1,1]\times[0,1]^2\), and define
\[
F(x_1,x_2,x_3)=\begin{cases}
(1+2x_1,x_2,x_3),&x_1<0,\\
(1-2x_3,x_1,x_2),&x_1\ge0.
\end{cases}
\]
Exclude the fixed face \(N=\{(-1,x_2,x_3):0\leq x_2,x_3\leq1\}\). Define \(\mathcal P_n=\{x\in X\setminus N:F^n(x)=x\}\). This includes points whose least period divides \(n\), not only points of least period \(n\). Use the one-sided derivative specified by the branch convention at discontinuities. Saiki–Takahasi–Yorke's symbolic-coding theorem establishes a bijection between \(\mathcal P_n\) and the length-\(n\) words containing at least one \(R\), giving \(|\mathcal P_n|=2^n-1\). The present proof uses this prior coding theorem. The primary MSC2020 is 37C05.

## Proof
**Step 1: explicit signed-monomial Jacobians.** The two branch matrices are
\[
A_L=\operatorname{diag}(2,1,1),\qquad
A_R=\begin{pmatrix}0&0&-2\\1&0&0\\0&1&0\end{pmatrix}.
\]
Every \(R\) cyclically advances coordinate directions by one position, whereas every \(L\) leaves the coordinate labels unchanged and doubles the factor on the currently active direction. Thus a return with \(t\) right visits is a signed monomial matrix whose underlying permutation rotates the three coordinate labels by \(t\) modulo three.

If \(3\nmid t\), the permutation is a single three-cycle. A signed monomial matrix with a single three-cycle has characteristic polynomial \(u^3-\det(DF^n)\), and \(|\det(DF^n)|=2^n\) since every branch determinant has modulus two. Therefore all three eigenvalue moduli equal \(2^{n/3}\), and \(\chi_n=2^{1/3}\).

If \(t=3q\), the permutation is the identity, so the matrix is diagonal. Each set of three right visits wraps each coordinate exactly once and contributes one factor of two in absolute value to each diagonal entry. The remaining factors of two arise from left visits and are assigned to one of the three coordinate directions according to the residue class modulo three of the preceding right-visit count. Writing these counts as \(c_0,c_1,c_2\) gives diagonal moduli \(2^{q+c_0},2^{q+c_1},2^{q+c_2}\), up to cyclic reordering. In particular
\[
\chi_n=2^{(q+\min(c_0,c_1,c_2))/n}.
\]
The \(c_j\) are nonnegative integers with sum \(n-t\). This proves the detailed multiplier formula.

**Step 2: sharp least expansion.** If \(3\nmid t\), \(\chi_n=2^{1/3}\). If \(t=3q\), then \(q\ge1\) and \(\chi_n\ge2^{q/n}\ge2^{1/n}\). For every \(n\ge4\), the strict inequality \(2^{1/3}>2^{1/n}\) holds. Equality in the lower bound is therefore possible precisely when \(t=3\) and at least one \(c_j\) vanishes. Under a cyclic word with exactly three right symbols, the \(c_j\) are exactly the three lengths of the left-symbol blocks between successive right symbols, up to a cyclic relabeling. Consequently equality holds exactly when at least one cyclic gap is empty. Such words exist for each \(n\ge4\), e.g. \(L^{n-3}RRR\), proving sharpness. For \(n\le3\), all non-all-left words have \(t\in\{1,2,3\}\); when \(t=3\) there are no left symbols, so all have normalized modulus \(2^{1/3}\).

**Step 3: count all equality points.** Fix \(n\ge4\), and put \(k=n-3\). Every cyclic itinerary with exactly three right symbols has three ordered cyclic gap lengths \((a_0,a_1,a_2)\), with \(a_j\ge0\) and \(a_0+a_1+a_2=k\). Distinguish one of the three right symbols and choose its position among the \(n\) positions of the word; the number of such marked configurations is
\[
n\binom{k+2}{2}=n\binom{n-1}{2}.
\]
Those with all gaps positive number \(n\binom{k-1}{2}\) when \(k\ge3\), and zero otherwise. Each unmarked word corresponds to exactly three marked configurations, hence the number of words with a zero gap is
\[
\frac n3\left(\binom{n-1}{2}-\binom{n-4}{2}\right)=n(n-3),
\]
where the second binomial coefficient is interpreted as zero when its upper index is smaller than two. This equality is also valid directly for \(n=4,5\). The coding bijection identifies exactly these many distinct points of \(\mathcal P_n\) attaining the minimum.

**Step 4: all equality points have least period \(n\).** Suppose one of the equality words is a proper power of a shorter cyclic word, repeated \(r>1\) times. The total number of right symbols is three, so \(r=3\). Therefore \(n\) is divisible by three and the shorter word has exactly one right symbol. Repeating it three times forces all three cyclic gaps between right visits to be equal. When \(n\ge4\), their common length is \(n/3-1>0\) whenever such a proper power exists. This contradicts the zero-gap condition. Thus all \(n(n-3)\) equality points have least period exactly \(n\). Each such orbit contains exactly \(n\) distinct points, proving the exact orbit count \(n-3\).

## Verification
The supplied `check_spectrum.py` uses exact rational arithmetic and no third-party packages. For each \(1\le n\le9\) and every non-all-left length-\(n\) word, it solves the three-dimensional affine fixed-point equation, verifies the branch itinerary and the actual forward return, constructs the complete derivative product, and checks the claimed exponent decomposition. For \(4\le n\le9\), it checks the equality census \(n(n-3)\). Running `python check_spectrum.py` in the package directory prints `CHECK_OK 13177 exact assertions`. The infinite family is proved analytically above, not established by this finite enumeration.

## Relationship to prior work
The originating work of Saiki, Takahasi and Yorke establishes the twisted baker map, the fixed-point coding, nonuniform periodic expansion, and a division between real and complex derivative spectra. A later indexed mathematical note, *Exact real-spectrum residue law for the twisted baker map*, identifies the all-dimensional residue criterion and characteristic-polynomial factorization, but does not identify the optimal normalized multiplier or enumerate its attaining primitive orbits. The dimension-two spectral-gap classification is distinct: its exact two-coordinate histogram does not imply the three-gap geometry or the linear growth of least-expanding orbit classes in dimension three. The present statement counts a natural extremal orbit family for the first higher-dimensional twisted map and remains within the original source's dimension-three model.

## Limitations
This is a complete classification only of the **least-expanding** periodic points of the three-dimensional map, not the entire multiplier histogram or higher-dimensional minimizer counts. It uses the original symbolic-coding theorem and assumes the specified branch convention. No independent mathematical audit or independent publication-priority certification has been performed. Equivalent extremal enumerations in unindexed works cannot be excluded by the searches performed.

## References
1. Y. Saiki, H. Takahasi and J. A. Yorke, *The twisted baker map*, arXiv:2202.04304, first posted 9 February 2022, especially Theorems A and B, Sections 2.1–2.3 and Appendix A. https://arxiv.org/html/2202.04304v3
2. *Exact real-spectrum residue law for the twisted baker map*, mathematical note (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-real-spectrum-residue-law-for-the-twisted-baker-map--f1bd1c74fb3b
3. H. Takahasi, *Distributions of periodic points for the Dyck shift and the heterochaos baker maps*, arXiv:2409.01261 (2024), on a different family. https://arxiv.org/html/2409.01261v1
