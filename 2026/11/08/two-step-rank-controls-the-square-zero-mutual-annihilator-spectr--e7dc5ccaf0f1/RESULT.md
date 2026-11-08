# Two-step rank controls the square-zero mutual-annihilator spectrum of a finite-field matrix

## Finding
Let \(q\) be a prime power, \(n\geq1\), and \(A\in M_n(\mathbb F_q)\). Set
\[
r=\operatorname{rank}A,\qquad \rho=\operatorname{rank}(A^2),\qquad k=n-r,\qquad \delta=r-\rho.
\]
For nonnegative integers \(b,t\), let \(S_A(b,t)\) count matrices \(B\in M_n(\mathbb F_q)\) satisfying
\[
B^2=AB=BA=0,\quad \operatorname{rank}B=b,\quad
\dim(\operatorname{im}A\cap\operatorname{im}B)=t.
\]
Then **the entire two-variable distribution depends on the fixed matrix \(A\) only through \(r\) and \(\rho\)**, and is given by
\[
\boxed{S_A(b,t)=
|\mathrm{GL}_b(\mathbb F_q)|
\begin{bmatrix}\delta\\t\end{bmatrix}_q
\begin{bmatrix}k-\delta\\b-t\end{bmatrix}_q
q^{(\delta-t)(b-t)}
\begin{bmatrix}k-b+t\\b\end{bmatrix}_q.}
\]
A Gaussian coefficient is defined to be zero when its bottom argument is negative or exceeds its nonnegative top argument; \(|\mathrm{GL}_0(\mathbb F_q)|=1\). All unlisted strata are zero. In particular, every integer rank from zero up to the following sharp maximum occurs:
\[
\boxed{\max\{\operatorname{rank}B:B^2=AB=BA=0\}=
\left\lfloor\frac{n-\operatorname{rank}(A^2)}2\right\rfloor.}
\]
The maximum involves \(\operatorname{rank}(A^2)\) alone, even though the individual multiplicities generally require both \(\operatorname{rank}A\) and \(\operatorname{rank}(A^2)\).

For example, over \(\mathbb F_2\), two rank-two matrices in dimension four exhibit sharply different annihilator spectra. For \(A=\operatorname{diag}(1,1,0,0)\), the counts by \(\operatorname{rank}B=0,1,2\) are \((1,3,0)\); for \(A=J_2(0)\oplus J_2(0)\) they are \((1,9,6)\). Thus a restriction to \(\operatorname{rank}A\) alone loses information, while the stated pair of rank invariants determines every count.

## Assumptions and scope
All matrices are ordinary linear endomorphisms of the same labeled \(n\)-dimensional space over \(\mathbb F_q\), not simultaneous-conjugacy classes. The fixed matrix \(A\) may have nilpotent, semisimple, or mixed primary components, and arbitrary characteristic is permitted. Write \(\begin{bmatrix}m\\j\end{bmatrix}_q=\prod_{i=0}^{j-1}(q^m-q^i)/(q^j-q^i)\) when \(0\le j\le m\) and \(|\mathrm{GL}_b(\mathbb F_q)|=\prod_{i=0}^{b-1}(q^b-q^i)\). The empty product is one.

## Proof
Let \(E=\mathbb F_q^n\), \(U=\operatorname{im}A\), \(K=\ker A\), and \(D=U\cap K\). We have \(\dim U=r\), \(\dim K=k\), and
\[
\dim D=\dim\ker(A|_U)=r-\operatorname{rank}(A^2)=\delta.
\]
Fix a matrix \(B\) of rank \(b\), and write \(L=\operatorname{im}B\) and \(H=\ker B\). The three zero-product conditions are equivalent to
\[
L\subseteq K,\qquad U+L\subseteq H,
\]
together with the assertion that the map induced by \(B\) from \(E/H\) onto \(L\) is an isomorphism. Indeed, \(AB=0\) is \(L\subseteq K\), \(BA=0\) is \(U\subseteq H\), and \(B^2=0\) is \(L\subseteq H\). Conversely, any such triple \((L,H,\varphi)\), where \(\varphi:E/H\to L\) is an isomorphism, defines exactly one required \(B\).

Put \(t=\dim(L\cap U)=\dim(L\cap D)\). First choose \(T=L\cap D\), a \(t\)-plane of \(D\), in \(\begin{bmatrix}\delta\\t\end{bmatrix}_q\) ways. Choose the image of \(L\) in \(K/D\), a \((b-t)\)-plane in dimension \(k-\delta\), in \(\begin{bmatrix}k-\delta\\b-t\end{bmatrix}_q\) ways. With those choices fixed, \(L/T\) is a graph of a linear map into \(D/T\); there are \(q^{(\delta-t)(b-t)}\) such maps. These choices enumerate every \(L\) exactly once.

Since \(\dim(U+L)=r+b-t\), a kernel \(H\supseteq U+L\) of codimension \(b\) exists in exactly
\[
\begin{bmatrix}n-r-b+t\\b\end{bmatrix}_q=
\begin{bmatrix}k-b+t\\b\end{bmatrix}_q
\]
ways. For each such \(H\), there are precisely \(|\mathrm{GL}_b(\mathbb F_q)|\) isomorphisms \(E/H\to L\). Multiplication proves the formula without case restrictions on the similarity class of \(A\).

For any contributing pair, the final Gaussian coefficient forces \(2b\le k+t\), and \(t\le\delta\). Hence \(2b\le k+\delta=n-\rho\). Conversely, let \(0\le b\le\lfloor(k+\delta)/2\rfloor\), and choose
\[
t=\max\{0,\ 2b-k,\ b-(k-\delta)\}.
\]
Because \(\delta\le k\), this \(t\) obeys \(0\le t\le\min(b,\delta)\), \(b-t\le k-\delta\), and \(2b-t\le k\). Consequently all four counting factors are positive, producing a required \(B\) of rank \(b\). This proves both sharpness and absence of rank gaps up to the maximum.

## Verification
Run the standalone script `verify.py` with Python 3. It enumerates every square-zero \(B\) in \(M_2(\mathbb F_4)\), \(M_3(\mathbb F_3)\), and \(M_4(\mathbb F_2)\), tests all three products directly against representative fixed matrices \(A\), computes image intersections by independent elimination, and compares every nonempty stratum with the formula. It includes matrices with invertible, idempotent, nilpotent, and mixed parts, as well as non-similar matrices having identical \((r,\rho)\). The script returns `VERIFY_OK`. This finite exercise is not the proof for arbitrary \(q,n\); the Grassmannian count above is.

## Relationship to prior work
Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity* (arXiv:2110.15566, first public October 29, 2021), §3.1, counts all \(B\) with \(AB=BA=0\) for a fixed \(A\): there are \(q^{(n-r)^2}\) choices. It does not impose \(B^2=0\), nor stratify by rank and intersection. V. Bondarenko, T. Gerasimova, and V. Sergeichuk (arXiv:0812.2155), Theorem 7, give canonical forms under simultaneous similarity for general mutually annihilating pairs, but not the present fixed-\(A\) finite-field fiber cardinalities. J. Schröer (arXiv:math/0211293), Theorems 1.1–1.4, studies irreducible components and strata of varieties of nilpotent annihilating pairs, rather than the displayed conditional point counts. The case \(A^2=0\) specializes to the previously studied mutually annihilating square-zero pair locus; the general fixed matrix and its two-step-rank rigidity are essential to the present scope.

## Limitations
This is a labeled-count result for a fixed matrix \(A\); it does not enumerate the possible matrices \(A\) by similarity type or classify simultaneous-similarity orbits. It constrains \(B\) to have nilpotency index at most two and does not address higher-index nilpotents or coefficient rings that are not finite fields. Published broader counting or Hall-polynomial results could potentially imply these conditional formulas; publication priority is not independently established. The enumeration examples support but do not establish the universal statement.

## References
1. Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566, first submitted October 29, 2021, §3.1 and Theorem 1.2.
2. V. M. Bondarenko, T. G. Gerasimova, V. V. Sergeichuk, *Pairs of mutually annihilating operators*, arXiv:0812.2155 (2008), Theorem 7.
3. J. Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, arXiv:math/0211293 (2002), Theorems 1.1–1.4.
