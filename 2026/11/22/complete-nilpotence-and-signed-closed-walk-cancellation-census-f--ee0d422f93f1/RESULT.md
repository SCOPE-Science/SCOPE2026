# Complete nilpotence and signed-closed-walk cancellation census for canonical interval maps

## Finding

For the canonical affine minimal-jump-rank Markov construction of Oliveira, the entire orientation-weighted symbolic closed-walk spectrum vanishes in every length exactly for a simple global-and-boundary balance condition. For every integer \(n\ge2\) and word \(\varepsilon=(\varepsilon_0,\ldots,\varepsilon_{n-1})\in\{-1,+1\}^n\), the signed adjacency matrix \(S_\varepsilon\) is nilpotent precisely when

\[
\sum_{j=0}^{n-1}\varepsilon_j=0,\qquad \varepsilon_0=\varepsilon_{n-2}=\varepsilon_{n-1}.
\]

In this case \(S_\varepsilon^4=0\), so \(\operatorname{tr}(S_\varepsilon^k)=0\) for every integer \(k\ge1\). There are exactly \(2\binom{2m-3}{m-3}\) such words at length \(n=2m\ge6\), and none at other lengths. Their fraction among all words satisfies

\[
\frac{2\binom{2m-3}{m-3}}{2^{2m}}\sim\frac1{4\sqrt{\pi m}}.
\]

This is exact cancellation of *signed* symbolic closed paths, despite the unsigned matrix's exponentially many paths and spectral radius at least \(n-1\).

## Assumptions and scope

Fix an integer \(n\ge2\). Use the equal-branch canonical affine interval map of Oliveira's Theorem 7.1, *not* an arbitrary orientation-compatible interval map. Let \(M_\varepsilon\) be its \(n\times n\) zero-one Markov adjacency matrix, and define \(S_\varepsilon=\operatorname{diag}(\varepsilon)M_\varepsilon\). The signed closed-path sum at length \(k\) is \(\operatorname{tr}(S_\varepsilon^k)\); each path is weighted by the product of its visited branch orientations. No assertion about literal periodic points at partition boundaries is made.

For \(1\le j<n\), set \(u_j=1\) if \((\varepsilon_{j-1},\varepsilon_j)=(-1,+1)\) and zero otherwise; set \(v_j=1\) for \((+1,-1)\), and let \(u_0=v_0=0\). Write \(A=\sum_j u_j\), \(B=\sum_j v_j\), \(a=u_{n-1}\), \(b=v_{n-1}\), \(e=\varepsilon_0\), \(f=\varepsilon_{n-1}\), and \(s=\sum_j\varepsilon_j\).

## Proof

The affine Markov construction has the exact matrix decomposition

\[
M_\varepsilon=\mathbf1\mathbf1^{\mathsf T}-u e_0^{\mathsf T}-v e_{n-1}^{\mathsf T}.
\]

Multiplication by the orientation diagonal and Sylvester's determinant identity reduce \(\det(I-tS_\varepsilon)\) to a \(3\times3\) determinant associated with

\[
N=\begin{pmatrix}s&A&-B\\-e&0&0\\-f&-fa&-fb\end{pmatrix}.
\]

Expansion gives the **exact** polynomial identity

\[
\det(I-tS_\varepsilon)=1+(bf-s)t+(eA-fB-sbf)t^2+ef(Ab+Ba)t^3.
\]

A finite matrix is nilpotent exactly when this polynomial is identically one. The last-step types \((a,b)\) are mutually exclusive.

If \(a=1\), then \(f=1\) and \(A\ge1\). Vanishing of the cubic coefficient forces \(B=0\), while the linear and quadratic coefficients force \(s=0\) and \(eA=0\), a contradiction.

If \(b=1\), then \(f=-1\) and \(B\ge1\). Vanishing of the cubic coefficient forces \(A=0\). The linear coefficient requires \(s=-1\), and the quadratic coefficient requires \(B=1\). A word with no \((-1,+1)\) transitions and a unique \((+1,-1)\) transition at the final cut consists of \(n-1\) plus symbols and one minus symbol. It has \(s=n-2\ne-1\) for \(n\ge2\); contradiction.

Thus \(a=b=0\): the final two signs coincide. The linear coefficient requires \(s=0\); the quadratic coefficient requires \(eA=fB\). The telescoping identity \(A-B=(f-e)/2\) shows that this condition holds when \(e=f\), while for \(e=-f\) it equals \(e(A+B)\ne0\), since a sign change is unavoidable. This proves the precise criterion.

For the criterion, the reduced matrix \(N\) has trace, second and third characteristic coefficients zero, so \(N^3=0\) by Cayley–Hamilton. The factorization \(S_\varepsilon=XY\), \(YX=N\), therefore yields \(S_\varepsilon^4=XN^3Y=0\).

A balanced word has even length \(n=2m\). Fix the common sign of the first and last two positions. The remaining \(2m-3\) positions must contain \(m-3\) more occurrences of that sign, giving \(2\binom{2m-3}{m-3}\) possibilities for \(m\ge3\). Stirling's formula gives the displayed asymptotic. Finally, Oliveira's Markov-matrix row-sum bound \(n-1\le\rho(M_\varepsilon)\le n\) establishes the contrast with the unsigned system.

## Verification

The accompanying standalone Python script checks the exact reduced determinant and the nilpotence classification for every orientation word of lengths \(2\) through \(9\), and confirms the exact census at each length. It also checks \(S^4=0\) directly for each qualifying word up to length \(9\). These finite checks supplement, but do not replace, the all-length proof above. Run with `python3 checker.py`; Python 3 and SymPy are required.

## Relationship to prior work

Oliveira's 2026 paper supplies the canonical affine Markov model, its rank-three factorization and the unsigned determinant, and explicitly examines two orientation-weighted examples. Those inputs are credited. The classification and exact population of *all* words yielding complete signed-walk cancellation are the distinct conclusion here. A related result on the random orientation-weighted spectral-radius limit concerns typical sizes and does not determine these exactly nilpotent words; the present exception set has vanishing probability but a precise polynomial rarity.

## Limitations

The result does not extend automatically to other interval maps sharing the same orientation word. Signed Markov traces are not identified with geometric periodic-point counts, which may have partition-boundary corrections. The calculation follows closely from a published low-rank factorization; independent priority evaluation against other twisted-transfer or kneading treatments remains important. No independent audit has been performed.

## References

1. Henrique M. Oliveira, *Homological reduction and entropy of discontinuous interval maps*, arXiv:2611.03287v1 (first public November 2, 2026), Theorem 7.1, Theorem 7.2 and Section 7.2. https://arxiv.org/abs/2611.03287
2. *Universal switching statistics and a sharp physical-entropy gap*, published published-finding corpus finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-universal-switching-statistics-and-a-sharp-physical-entropy-gap--d13a003ecd84
