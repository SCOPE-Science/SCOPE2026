# A sharp universal mean-zero stability constant for harmonic completion from cubical faces

## Finding
Let \(k,h\ge1\), and identify the \(k\)-dimensional coordinate face \(F=\{(u,0):u\in\{0,1\}^k\}\) of the unit-edge hypercube \(Q_{k+h}\). Extend complex boundary data \(f:F\to\mathbb C\) to the whole host by the unique graph-harmonic completion \(Ef\), using the unweighted combinatorial Laplacian and counting \(\ell^2\)-norms.

For \(t=1,\ldots,k\), define
\[
\lambda_{h,t}=2^h\frac{\displaystyle\sum_{j=0}^{h}\binom hj(j+t)^{-2}}{\left(\displaystyle\sum_{j=0}^{h}\binom hj(j+t)^{-1}\right)^2},\qquad \lambda_{h,0}=2^h.
\]
The Walsh characters on the face with Hamming frequency weight \(t\) are eigenvectors of \(E^*E\) with eigenvalue \(\lambda_{h,t}\) and multiplicity \(\binom kt\). These are all eigenvalues, and they satisfy
\[
1<\lambda_{h,k}\le\cdots\le\lambda_{h,1}<2^h.
\]
The inequalities between successive positive-weight eigenvalues are strict when the weights exist. In particular, the exact full-space frame bounds of \(WE\), for **any** Parseval analysis map \(W\) on the host, are \(A=\lambda_{h,k}\) and \(B=2^h\).

The substantive uniform extremal conclusion is
\[
\boxed{\ \|Ef\|_2^2\le \frac{3548}{2883}\,\|f\|_2^2\quad\text{whenever}\quad\sum_{u\in F}f(u)=0.\ }
\]
This constant is the smallest possible simultaneously for **all** \(k,h\ge1\): equality holds precisely when \(h=4\) and \(f\) is a nonzero linear combination of weight-one face Walsh characters. Thus arbitrary many additional host coordinates inflate the squared norm of a mean-zero signal by at most \(3548/2883=1.230662504\ldots\), while the constant signal is amplified by \(2^h\). This is a statement about energy after harmonic completion, not about the graph Dirichlet energy being minimized.

## Assumptions and scope
We use the ordinary undirected hypercube, one edge of weight one per coordinate flip; \(L_m\) denotes its degree-minus-adjacency graph Laplacian. Boundary values are prescribed on all \(2^k\) vertices of one coordinate face, and harmonicity \((L_{k+h}Ef)(x)=0\) is imposed at all remaining vertices. This Dirichlet problem has a unique solution. Inner products are sums over vertices, without division by the number of vertices. The Parseval map \(W\) may be the unitary host Walsh--Fourier transform or any host tight wavelet-analysis bank normalized so that \(W^*W=I\). The statement does not concern minimal host embeddings, non-face boundary sets, or noisy observations that have already been restricted to fewer than all face vertices.

## Proof
**1. Diagonalization.** Write a host vertex as \((u,v)\in\{0,1\}^k\times\{0,1\}^h\), and let \(\chi_S(u)=2^{-k/2}(-1)^{\sum_{i\in S}u_i}\), with \(t=|S|\). Since \(L_{k+h}=L_k\otimes I+I\otimes L_h\) and \(L_k\chi_S=2t\chi_S\), the harmonic extension of \(\chi_S\) is \(\chi_S(u)a_t(v)\), where \(a_t(0)=1\) and \((L_h+2tI)a_t(v)=0\) for \(v\ne0\). Uniqueness follows from the maximum principle (or positivity of the grounded Laplacian).

For \(t=0\), \(a_0\equiv1\). For \(t>0\), set \(G_t=(L_h+2tI)^{-1}\). Then
\[
a_t(v)=G_t(v,0)/G_t(0,0),
\]
since \((L_h+2tI)G_t(\cdot,0)=\delta_0\). Orthogonality of distinct face Walsh characters persists after completion, because their \(u\)-dependence remains orthogonal. Therefore the eigenvalue is \(\sum_v|a_t(v)|^2=G_t^2(0,0)/G_t(0,0)^2\). The host Walsh characters of weight \(j\) have Laplacian eigenvalue \(2j\), with multiplicity \(\binom hj\). Spectral decomposition of \(G_t\) gives exactly the displayed binomial formula, including normalization \(2^{-h}\) in both Green diagonal moments. Each weight on the face has multiplicity \(\binom kt\).

**2. Strict ordering.** Consider continuous-time unit-rate edge-flip random walk on \(Q_h\), and let \(T_0\) be its first hitting time of the origin. The function \(v\mapsto\mathbb E_v[e^{-2tT_0}]\) equals \(a_t(v)\), by conditioning on the first jump; it is the unique solution of the preceding killed Dirichlet problem. For every \(v\ne0\), the hitting time is finite and strictly positive almost surely. Consequently \(0<a_t(v)<1\), and \(a_t(v)\) strictly decreases with \(t>0\). The origin contribution remains one, so \(1<\lambda_{h,t}<2^h\) and \(\lambda_{h,t}\) strictly decreases for positive \(t\).

**3. Exact global maximization over the codimension.** It remains to maximize \(\lambda_{h,1}\) over positive integers \(h\). Put \(n=h+1\) and
\[
T_n=\sum_{m=1}^n\frac{2^m-1}{m},\qquad F_n=\frac{n2^{n-1}T_n}{(2^n-1)^2}.
\]
The identities
\[
\sum_{j=0}^{h}\frac{\binom hj}{j+1}=\frac{2^{h+1}-1}{h+1},\qquad
\sum_{j=0}^{h}\frac{\binom hj}{(j+1)^2}=\frac{T_{h+1}}{h+1}
\]
follow by integrating \((1+x)^h\) and then integrating once more. Hence \(\lambda_{h,1}=F_{h+1}\), and \(T_{n+1}=T_n+(2^{n+1}-1)/(n+1)\).

Write \(z=2^n\), \(C_n=2(n-1)z^2+4z-(n+2)\), and \(R_n=2(2z-1)(z-1)^2\). Direct cross-multiplication shows
\[
F_{n+1}<F_n\ \Longleftrightarrow\ C_nT_n>R_n.
\]
For \(n\ge8\), expand \(1/(n-r)\ge n^{-1}+rn^{-2}+r^2n^{-3}\) for integer \(0\le r<n\), then sum \((2^{n-r}-1)/(n-r)\). This gives
\[
T_n\ge U_n:=\frac{(2n^2+2n+6)z-(11n^3/6+5n^2+37n/6+6)}{n^3}.
\]
The resulting difference has the **exact** expansion
\[
\begin{aligned}
n^3(U_nC_n-R_n)={}&(8n-12)z^3\\
&+(-11n^4/3+11n^3/3+17n^2/3+25n/3+36)z^2\\
&-(52n^3/3+26n^2+104n/3+36)z\\
&+(11n^4/6+32n^3/3+97n^2/6+55n/3+12).
\end{aligned}
\]
For every integer \(n\ge8\), \(z=2^n\ge n^3/2\); the inequality holds at \(n=8\) and propagates because \(2n^3\ge(n+1)^3\) for \(n\ge4\). Dividing the expansion by \(z^2\), keeping its positive terms, and using \(z\ge n^3/2\) yields
\[
\frac{n^3(U_nC_n-R_n)}{z^2}
\ge\frac{n^3(n-7)}3-
\left(\frac{104}3+\frac{52}n+\frac{208}{3n^2}+\frac{72}{n^3}\right)
>\frac{512}3-43>0.
\]
Thus \(F_n\) is strictly decreasing for all \(n\ge8\). For \(h=1,\ldots,7\), the successive exact values are
\[
\frac{10}9,\ \frac{58}{49},\ \frac{824}{675},\ \frac{3548}{2883},\ \frac{24272}{19845},\ \frac{291824}{241935},\ \frac{8096384}{6827625}.
\]
They increase strictly through \(h=4\) and decrease thereafter. The unique global maximum is \(3548/2883\), attained at \(h=4\). Combined with Step 2, the only extremizing mean-zero Walsh frequencies have weight one. This proves the uniform inequality, the equality classification, and the sharp frame bounds.

**4. Parseval stability.** For every host Parseval analysis operator \(W\), \((WE)^*(WE)=E^*W^*WE=E^*E\). Hence all the spectrum and stability statements pass verbatim to host Fourier and normalized wavelet analysis.

## Verification
Run `python3 check_face_spectrum.py` after installing NumPy. The independent direct host Dirichlet solver computes the extension matrix, conjugates \(E^*E\) by the face Walsh matrix, and compares every diagonal/off-diagonal entry to the formula for fourteen \((k,h)\) pairs with \(k\le3\), \(h\le5\) and \(k+h\le7\). The maximum absolute entry discrepancy was \(4.26\times10^{-14}\). The checker separately verifies exact rational low-codimension values and finite monotonicities. The all-dimensional theorem and global maximum rely on the proof above, not on these finite checks.

## Relationship to prior work
Fokam Souop and Bitjoka (2026) motivate harmonic completion as an energy-minimizing lift before host Parseval Fourier/wavelet analysis. Their accessible summary establishes the general grounded-Laplacian construction, not this cubical-face spectral classification or sharp uniform constant; the full manuscript was not accessible for a complete implication check. Chung and Yau (2000) compute general discrete Green functions and hypercube hitting times, providing conceptual precedents for the resolvent step; neither the cited hypercube example nor its formula states the sharp \(3548/2883\) universal mean-zero norm. Beck et al. (2024) construct Cayley graph frames by representation theory without this harmonic-lift stability optimization. The present novelty claim is the exact **all-codimension extremal constant and equality classification**, not the basic Green-resolvent identity, Walsh diagonalization, or abstract harmonic completion.

## Limitations
The host dimension can be much larger than the smallest possible isometric host; the result describes deliberate coordinate-face embedding, a natural nested-cube signal-extension model, not an optimal-host selection theorem. The \(2^h\) constant-sector inflation is not uniformly bounded. The upper constant \(3548/2883\) holds for mean-zero data on a complete coordinate face, not for arbitrary boundary shapes. The motivating preprint was available through public metadata and a detailed third-party technical synopsis, but its primary full text could not be obtained, leaving a residual risk that an equivalent special-case result appears there. Independent mathematical review has not been performed.

## References
1. R. Fokam Souop and L. Bitjoka, *Tight Wavelet Frames on Graphs via Isometric Group Embedding*, first public July 15, 2026, https://arxiv.org/abs/2607.14168 .
2. F. Chung and S.-T. Yau, *Discrete Green's Functions*, Journal of Combinatorial Theory Series A **91** (2000), 191–214, https://doi.org/10.1006/jcta.2000.3094 .
3. K. Beck, M. Ghandehari, S. Hudson and J. Paltenstein, *Frames for Signal Processing on Cayley Graphs*, Journal of Fourier Analysis and Applications **30** (2024), https://doi.org/10.1007/s00041-024-10128-5 .
