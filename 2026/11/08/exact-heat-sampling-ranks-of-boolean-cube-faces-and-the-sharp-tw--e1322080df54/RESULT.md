# Exact heat-sampling ranks of Boolean-cube faces and the sharp two-snapshot horizon

## Finding
Consider heat evolution on the Boolean hypercube and observe every vertex in a fixed coordinate face at finitely many times. The complete space-time measurement rank on each graph Paley–Wiener band is explicitly determined by face codimension, bandwidth, and the number of distinct times. In particular, two observations of a codimension-one face recover *every* initial signal, whereas **no number** of observations of a coordinate face of codimension at least two recovers every nonconstant low-pass band. For full-band two-snapshot codimension-one sensing, every squared singular value and the uniquely D-optimal second observation time are explicit.

With the definitions below, the rank on the degree-\(\le K\) band is
\[
\boxed{\operatorname{rank}\mathcal M_{d,c,K,m}=\sum_{k=0}^{\min(K,d-c)}\binom{d-c}{k}\min\{m,1+\min(c,K-k)\}.}
\]
When \(c=1\) and \(K=d\), the two observation times are \(0,\tau\), where \(\tau>0\). Set \(r=e^{-2\tau/d}\). The square analysis operator has exactly two squared singular values for every \(0\le k\le d-1\), each repeated \(\binom{d-1}{k}\) times:
\[
\lambda_{k,\pm}=\frac{2+r^{2k}(1+r^2)\pm\sqrt{\left(2+r^{2k}(1+r^2)\right)^2-4r^{2k}(1-r)^2}}4.
\]
For every integer \(d\ge2\), its absolute determinant is
\[
\boxed{|\det\mathcal M_{d,1,d,2}(\tau)|=\left(\frac{1-r}{2}\right)^{2^{d-1}}r^{(d-1)2^{d-2}},}
\]
and the **unique** maximizer over finite \(\tau>0\) is
\[
\boxed{\tau_d^*=\frac d2\log\frac{d+1}{d-1}.}
\]
In particular \(\tau_d^*\to1\) as \(d\to\infty\). This maximizes the determinant of the Fisher information matrix for equal-variance independent noise in the individual vertex samples, within the two-snapshot one-face observation family.

## Assumptions and scope
Let \(d\ge1\), \(0\le c\le d\), \(0\le K\le d\), and \(m\ge1\) be integers. The Boolean hypercube graph \(Q_d\) has vertices \(\{0,1\}^d\), with two vertices adjacent when they differ in one coordinate. Its normalized Laplacian is \(L=I-A/d\), and it has Walsh eigenvectors
\[
\phi_S(x)=2^{-d/2}(-1)^{\sum_{j\in S}x_j},\qquad L\phi_S=(2|S|/d)\phi_S,
\]
for subsets \(S\subseteq\{1,\ldots,d\}\). All Hilbert norms use counting measure on vertices. Define the graph low-pass space \(V_K=\operatorname{span}\{\phi_S:|S|\le K\}\), of dimension \(\sum_{j=0}^{K}\binom dj\). Fix any codimension-\(c\) coordinate face by choosing \(c\) coordinate positions and fixing their Boolean values. At any \(m\) pairwise distinct finite nonnegative real times \(t_0,\ldots,t_{m-1}\), observe all point values of \(e^{-t_jL}f\) on that same face. Their linear analysis map on \(V_K\) is \(\mathcal M_{d,c,K,m}\). Its rank is independent of the fixed coordinate positions/values and of the distinct observation times. The singular-value and determinant formulas additionally assume \(c=1\), \(K=d\), times \(0,\tau\), and \(d\ge2\) for the finite optimal time.

## Proof
**Walsh diagonalization and face reduction.** By cube automorphisms one may take the face to be defined by \(x_1=\cdots=x_c=0\). Write any Walsh index uniquely as \(S\cup T\), where \(S\subseteq\{c+1,\ldots,d\}\) and \(T\subseteq\{1,\ldots,c\}\). On the face, all the Walsh characters with the same outside index \(S\) coincide, up to their common normalization. The heat multiplier at time \(t_j\) equals \(e^{-2t_j(|S|+|T|)/d}\). After applying the orthonormal Walsh transform to the observed face at each time, different \(S\) become orthogonal blocks. For \(k=|S|\), the face-time block depends only on the aggregated coefficient sums
\[
 b_{S,r}=\sum_{\substack{T\subseteq\{1,\ldots,c\}\\|T|=r}}\widehat f(S\cup T),\qquad 0\le r\le\min(c,K-k).
\]
Its time matrix, after removing the nonzero row factors \(2^{-c/2}e^{-2t_j k/d}\), has entries \(z_j^r\), where \(z_j=e^{-2t_j/d}\). The \(z_j\) are distinct positive real numbers. This consecutive-power Vandermonde matrix has rank \(\min\{m,1+\min(c,K-k)\}\), since every square minor using the first columns and any appropriate rows is nonzero. Aggregation onto the \(b_{S,r}\) is surjective: each relevant Hamming-weight class contains at least one \(T\). Summing the ranks over the \(\binom{d-c}{k}\) possible outside indices proves the exact rank formula.

**Sharp spatial obstruction and recovery.** If \(c\ge2\) and \(K\ge1\), the two different Walsh vectors \(\phi_{\{1\}}\) and \(\phi_{\{2\}}\) have the same Laplacian eigenvalue and identical restriction to the face. Their difference is nonzero, lies in \(V_K\), and vanishes on the face at every time. This rules out recovery even with infinitely many observations. If \(c=1\), every Hamming-weight class in the fixed coordinate has cardinality one, and two distinct times separate the two possible weights wherever both occur. Thus \(m\ge2\) is necessary and sufficient for all \(K\ge1\). For \(K=0\), one face snapshot suffices. For \(c=0\) the full vertex set is already observed, so one snapshot suffices. These assertions also follow directly by setting the rank formula equal to \(\dim V_K\).

**All singular values for full-band face recovery.** With \(c=1\), times \(0,\tau\), and the orthonormal Walsh transform on the face applied independently at each time, the \(2^d\times2^d\) analysis matrix is an orthogonal direct sum of blocks
\[
 B_k=\frac1{\sqrt2}\begin{pmatrix}1&1\\r^k&r^{k+1}\end{pmatrix},\qquad k=0,\ldots,d-1,
\]
with block \(B_k\) repeated \(\binom{d-1}{k}\) times. This follows from the normalization \(2^{-d/2}\) in the full-cube Walsh basis versus \(2^{-(d-1)/2}\) on the face. The Gram matrix of each block is
\[
 B_k^*B_k=\frac12\begin{pmatrix}1+r^{2k}&1+r^{2k+1}\\1+r^{2k+1}&1+r^{2k+2}\end{pmatrix}.
\]
Its trace is \(\{2+r^{2k}(1+r^2)\}/2\), and its determinant is \(r^{2k}(1-r)^2/4\), yielding the two claimed eigenvalues and proving positivity for every finite \(\tau>0\).

**Determinant and unique optimal time.** Since \(|\det B_k|=(1-r)r^k/2\), multiplying the block determinants and using \(\sum_{k=0}^{d-1}\binom{d-1}k=2^{d-1}\) and \(\sum_{k=0}^{d-1}k\binom{d-1}k=(d-1)2^{d-2}\) gives the determinant formula. For \(d\ge2\), take logarithms and differentiate with respect to \(r\in(0,1)\). The derivative is
\[
 -\frac{2^{d-1}}{1-r}+\frac{(d-1)2^{d-2}}r,
\]
which has exactly one zero at \(r=(d-1)/(d+1)\), positive before and negative after. The determinant tends to zero at both endpoints, hence this is its unique global maximum. The inverse substitution \(r=e^{-2\tau/d}\) gives \(\tau_d^*\). The limit follows by expanding \(\log((d+1)/(d-1))\). Equal independent measurement-noise variances multiply the information determinant by a constant independent of \(\tau\), so the maximizer is unchanged.

## Verification
Run the included `CHECK.py` with Python 3 and NumPy. It constructs the graph heat-sampling matrices directly from normalized Walsh characters, for \(d=2,\ldots,6\), all coordinate-face codimensions and graph low-pass cutoffs, and up to three distinct times. The 405 finite-rank comparisons agree with the exact formula. It separately computes full Gram spectra through dimension seven, compares the values against the closed two-by-two block formula, and checks the predicted determinant and a nearby strict optimum. Reported output: `CHECK_OK rank_cases= 405  two_time_spectrum_dimensions=6`. These finite computations are sanity checks; the unrestricted proof uses Walsh and Vandermonde identities.

## Relationship to prior work
Dynamical sampling of graph Paley–Wiener spaces has a general finite-frame criterion in the work of Aldroubi, Cabrelli, Molter and Tang (2014/2017), used by Aldroubi and collaborators (2024) and by Bulai, Cabrelli, Cordero, Molter and Saliani (2026). Those criteria say how eigenvalue-wise sensor restrictions control recoverability; the rank formula above is compatible with those necessary and sufficient conditions. They do not themselves give the explicit complete face-codimension/low-pass/time rank profile, the full singular spectrum of the exact two-face-snapshot square measurement, or the uniquely optimal two-time heat horizon for hypercubes. The 2026 paper explicitly explores numerical graph-sensor conditioning for path graphs and does not study Boolean hypercube faces.

A related published treatment of D-optimal observation horizons for arithmetic-spectrum flows considers amplitude and decay-slope sensors measured at multiple times. Its confluent-Vandermonde design is not the face-restricted Walsh heat observation operator here, and its exact objective and dimension dependence are different. Standard Walsh diagonalization, the Vandermonde determinant, and the eigenspace-wise general dynamical sampling criterion are cited as background, not claimed as independently original ingredients.

## Limitations
This theorem is about a **fixed coordinate face** and spectral heat evolution \(e^{-tL}\), not arbitrary moving sensor sets, arbitrary graph operators, or non-coordinate half-sets. The rank formula assumes distinct finite times; repeated times do not add rank. The determinant optimum fixes the first time at zero, the second time at a common \(\tau>0\), and the raw point-sampling normalization; it does not optimize the minimum singular value or a more general sensor placement. The existence of general frame criteria makes these results special-purpose exact evaluations, not a replacement for general graph-sampling theory. An older equivalent computation under hypercube observability or product-graph terminology remains possible. No independent scientific audit has been performed.

## References
1. I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter and S. Saliani, *Dynamical Sampling in Graph Paley–Wiener Spaces*, arXiv:2609.25472v1 (2026-09-21), https://arxiv.org/abs/2609.25472.
2. A. Aldroubi, V. Bailey, I. Krishtal, B. Miller and A. Petrosyan, *Reconstructing Graph Signals from Noisy Dynamical Samples*, arXiv:2411.12670v1 (2024-11-19), https://arxiv.org/abs/2411.12670.
3. A. Aldroubi, C. Cabrelli, U. Molter and S. Tang, *Dynamical sampling*, arXiv:1409.8333v1 (2014-09-29); Applied and Computational Harmonic Analysis 42 (2017), https://arxiv.org/abs/1409.8333.
4. *A universal optimal observation horizon for arithmetic-spectrum flows*, published-finding corpus repository (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-universal-optimal-observation-horizon-for-arithmetic-spectrum--64dbf45b5739.
