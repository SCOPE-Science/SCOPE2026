# Sharp finite-section numerical-radius error for four-periodic geometric shifts

## Finding

Let \(T\) be a compact unilateral weighted shift with geometrically decaying weights and four-periodic positive modulation. Its principal finite sections do more than converge in numerical radius: their **positive radius defect** has an exact first-order, computable prefactor. For all fixed \(0<q<1\), \(s,t>0\),
\[
\lambda-\lambda_N \sim C^2\lambda\prod_{j=0}^{N}\left(\frac{a_j}{\lambda}\right)^2.
\]
The constant \(C\) is a strictly positive convergent product of Jacobi tail Green values, defined below. Consequently
\[
\lim_{N\to\infty}\frac{\log(\lambda-\lambda_N)}{N^2}=\log q.
\]
The statement concerns the cutoff \(N\to\infty\) at fixed damping and modulation; it is distinct from the weak-damping limit \(q\uparrow1\).

## Assumptions and scope

Work on \(\ell^2(\mathbb N_0)\), over real or complex scalars, with standard basis \((e_j)_{j\ge0}\). Fix real \(q,s,t\) satisfying \(0<q<1\), \(s,t>0\). Set the positive four-periodic sequence by \(c_{4k}=c_{4k+2}=1\), \(c_{4k+1}=s\), and \(c_{4k+3}=t\), for every \(k\ge0\). Define
\[
Te_j=c_jq^j e_{j+1},\qquad a_j=\frac{c_jq^j}{2},\qquad J=\frac{T+T^*}{2}.
\]
The positive Jacobi matrix \(J\) has zero diagonal and adjacent entries \(a_j\). Denote its top eigenvalue by \(\lambda\), and its strictly positive normalized eigenvector by \(\psi=(\psi_j)_{j\ge0}\). For each integer \(N\ge0\), let \(P_N\) project onto \(e_0,\ldots,e_N\), \(J_N=P_NJP_N\) restricted to this \((N+1)\)-dimensional space, and \(\lambda_N=\lambda_{\max}(J_N)\). For \(j\ge1\), \(J^{[j]}\) is the Jacobi tail on indices \(j,j+1,\ldots\) and
\[
G_j=\langle e_j,(\lambda I-J^{[j]})^{-1}e_j\rangle,\qquad
C=\psi_0\prod_{j=1}^{\infty}(\lambda G_j).
\]
All the inverse operators in this definition exist. All asymptotic statements hold as \(N\to\infty\) for each fixed triple \((q,s,t)\); no uniform assertion in these parameters is made.

## Proof

**1. Positivity, compactness and gap.** Since \(a_j=O(q^j)\), the Jacobi matrix is compact. Its quadratic form can be increased by taking absolute values of vector coordinates. An eigenvector at the largest positive spectral value therefore can be chosen nonnegative and, by the strict positivity of every edge and the recurrence, is strictly positive. The same recurrence rules out a second eigenvector for that eigenvalue; thus \(\lambda>0\) is simple. The corresponding eigenvalue of every proper principal head or proper tail is strictly less than \(\lambda\): equality would produce a maximizer supported in the head or tail, incompatible with a strictly positive top eigenvector. Let \(\lambda_2<\lambda\) be the supremum of the remaining spectrum. Compactness gives the positive spectral gap \(\lambda-\lambda_2\). The numerical radius of a positive unilateral shift equals \(\max\sigma((T+T^*)/2)\) by the phase gauge and absolute-value inequality, including after principal compression; hence these eigenvalues are exactly the stated numerical radii.

**2. An endpoint product for the infinite eigenvector.** For each \(j\ge1\), solve the tail eigenvector equation \((\lambda-J^{[j]})\psi_{[j,\infty)}=a_{j-1}\psi_{j-1}e_j\). Its first coordinate yields
\[
\psi_j=a_{j-1}G_j\psi_{j-1};\qquad
\psi_N=\psi_0\left(\prod_{j=1}^{N}\lambda G_j\right)\lambda^{-N}\prod_{j=0}^{N-1}a_j.
\]
There is a uniform bound \(\|J^{[j]}\|=O(q^j)\). The zero Jacobi diagonal eliminates the linear term in the Neumann resolvent expansion at \(e_j\), giving \(\lambda G_j=1+O(q^{2j})\). Every factor is positive. Hence the infinite product defining \(C\) converges to a finite strictly positive value, and
\[
\psi_N\sim C\lambda^{-N}\prod_{j=0}^{N-1}a_j.
\]

**3. Relative convergence at the last coordinate.** Let \(\phi^{(N)}\) be the strictly positive, unit top eigenvector of \(J_N\). Since \(J_N\oplus0\to J\) in operator norm, \(\lambda_N\uparrow\lambda\), and the isolated simple eigenvector converges: \(\phi^{(N)}_0\to\psi_0\). Moreover, \(\delta_N:=\lambda-\lambda_N=O(q^N)\) by the operator-norm tail bound. For \(1\le j\le N\), write
\[
G_{j,N}(z)=\langle e_j,(z-J_{[j,N]})^{-1}e_j\rangle,
\qquad
\phi^{(N)}_j=a_{j-1}G_{j,N}(\lambda_N)\phi^{(N)}_{j-1}.
\]
For each fixed \(j\), norm convergence of the tail compressions and \(\lambda_N\to\lambda\) imply \(G_{j,N}(\lambda_N)\to G_j\). Uniformly for all sufficiently large \(j\) and \(N\ge j\), the same zero-diagonal Neumann expansion yields
\[
\lambda_N G_{j,N}(\lambda_N)=1+O(q^{2j}),\qquad \lambda G_j=1+O(q^{2j}),
\]
with constants independent of \(N,j\). For a fixed cutoff \(K\), the product of factors \(G_{j,N}(\lambda_N)/G_j\) over \(j\le K\) tends to one; over \(j>K\), its logarithm is bounded by a constant times \(\sum_{j>K}q^{2j}+N\delta_N\). Letting first \(N\to\infty\), then \(K\to\infty\), shows
\[
\frac{\phi^{(N)}_N}{\psi_N}\longrightarrow1.
\]
This relative endpoint estimate is needed: ordinary norm convergence alone would not control the vanishing last coordinate.

**4. Exact Schur complement and the radius defect.** Separate \(J\) at the edge between indices \(N\) and \(N+1\). The Schur complement at its top eigenvalue gives
\[
1=a_N^2G_{N+1}\langle e_N,(\lambda I-J_N)^{-1}e_N\rangle.
\]
Decompose this finite-head resolvent into its top eigenspace and orthogonal complement:
\[
\langle e_N,(\lambda I-J_N)^{-1}e_N\rangle
=\frac{(\phi^{(N)}_N)^2}{\lambda-\lambda_N}+R_N,
\qquad 0\le R_N\le\frac1{\lambda-\lambda_2}.
\]
The spectral bound follows from the min-max inequality for all non-top eigenvalues of \(J_N\). Solving for the defect yields the exact identity
\[
\lambda-\lambda_N=
\frac{a_N^2G_{N+1}(\phi^{(N)}_N)^2}{1-a_N^2G_{N+1}R_N}.
\]
As \(N\to\infty\), \(a_N\to0\), \(G_{N+1}\to1/\lambda\), and the denominator tends to one. By Step 3 this is asymptotic to \(a_N^2\psi_N^2/\lambda\). Substitution from Step 2 gives
\[
\lambda-\lambda_N\sim C^2\lambda\prod_{j=0}^{N}\left(\frac{a_j}{\lambda}\right)^2
=C^2\lambda q^{N(N+1)}\prod_{j=0}^{N}\left(\frac{c_j}{2\lambda}\right)^2.
\]
The modulation \(c_j\) remains in a bounded, four-periodic positive set, so the final logarithm equals \(N(N+1)\log q+O(N)\), proving the logarithmic limit. All limits involve infinitely many indices and are established analytically, not by finite enumeration.

## Verification

A standalone script `CHECK.py` calculates high-precision finite Jacobi eigenvalues from the exact three-term continuant and independently approximates the tail Green product and normalized eigenvector using backward continued fractions. On multiple dampings and positive modulations, the ratio of the observed defect to the stated first-order formula approaches one. The script is a supplementary finite check, not an infinite-dimensional proof. Its dependencies are Python 3, `mpmath`, `numpy`, and `scipy`; run `python CHECK.py` in the extracted directory. The mathematical proof above supplies the infinite quantifiers.

## Relationship to prior work

Ghosh, Birbonshi and Ojha (2026) investigate the *same four-periodic geometrically damped shift* and identify its numerical radius through an entire-function zero, inequalities and finite-dimensional computation. Their accessible abstract and summaries do not state the relative finite-section asymptotic with its positive Green-product coefficient; their full manuscript was not available for line-by-line inspection, so priority remains qualified. Chien and Nakazato (2009) treat the unmodulated geometric shift and a hypergeometric radius identity. Chakraborty, Ojha and Birbonshi (2022) derive determinantal recurrences for eventually periodic positive shifts. Chakraborty and Ojha (2025) study bounds for alternating generalized-geometric weights; only their bibliographic abstract was available. Neither of the inspected earlier primary texts gives this relative \(N\to\infty\) cutoff law. Comparisons with research on geometric shift modulation, infinite-matrix Airy limits as \(q\uparrow1\), and small-\(q\) Taylor-jet rigidity involve different limiting problems; no novelty is asserted for those prior topics.

## Limitations

The constant \(C\) depends on the normalized infinite eigenvector and convergent infinite Green product; no elementary closed form is claimed. No uniform relative error bound in \(N\), \(q\), \(s\), or \(t\) is established, nor is this result an automatic certified finite-precision interval algorithm. The 2026 motivating preprint was checked through its abstract and available mathematical summaries, not full text; an equivalent result within it or older Jacobi finite-section literature remains a bibliographic risk.

## References

1. A. Ghosh, R. Birbonshi and S. Ojha, *On the numerical radius of a class of weighted shift operators*, arXiv:2608.17486 (first version 18 August 2026), https://arxiv.org/abs/2608.17486.
2. M.-T. Chien and H. Nakazato, *The numerical radius of a weighted shift operator with geometric weights*, Electronic Journal of Linear Algebra **18** (2009), 58–63, https://journals.uwyo.edu/index.php/ela/article/download/587/587.
3. B. Chakraborty, S. Ojha and R. Birbonshi, *Numerical radii of weighted shift operators using determinantal polynomials*, Operators and Matrices **16** (2022), 1155–1174, https://doi.org/10.7153/oam-2022-16-75.
4. B. Chakraborty and S. Ojha, *On the numerical radius of weighted shift operators with generalized geometric weights*, Journal of Mathematical Analysis and Applications **543** (2025), 129021, https://doi.org/10.1016/j.jmaa.2024.129021.
