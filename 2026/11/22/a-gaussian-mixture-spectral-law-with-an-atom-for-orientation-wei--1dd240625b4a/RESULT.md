# A Gaussian-mixture spectral law with an atom for orientation-weighted interval maps

## Finding
For each integer \(n\ge3\), sample independently and uniformly an orientation word \(\varepsilon=(\varepsilon_0,\ldots,\varepsilon_{n-1})\in\{-1,+1\}^n\). Construct the specific equal-partition affine Markov map in Oliveira's Theorem 7.1 [1], with adjacency matrix \(M_\varepsilon\). Set its *orientation-weighted* matrix
\[
S_\varepsilon=\operatorname{diag}(\varepsilon_0,\ldots,\varepsilon_{n-1})M_\varepsilon.
\]
Let \(\rho\) denote spectral radius. With independent random variables \(Z\sim\mathcal N(0,1)\) and \(U,V\), each equally likely to be \(-1\) or \(1\), define
\[
R=\begin{cases}
 |Z|,&U=V,\\
 2^{-1/2},&U=1,\ V=-1,\ |Z|\le\sqrt2,\\
 \bigl(|Z|+\sqrt{Z^2-2}\bigr)/2,&U=1,\ V=-1,\ |Z|>\sqrt2,\\
 \bigl(|Z|+\sqrt{Z^2+2}\bigr)/2,&U=-1,\ V=1.
\end{cases}
\]
Then, as \(n\to\infty\),
\[
\frac{\rho(S_\varepsilon)}{\sqrt n}\ \Longrightarrow\ R,
\qquad \frac{\rho(M_\varepsilon)}n\longrightarrow1
\quad\text{uniformly in }\varepsilon.
\]
In particular, the limiting *signed* spectral law has exactly one atom, at \(1/\sqrt2\), with mass
\[
\boxed{\mathbb P\!\left(R=1/\sqrt2\right)=\frac{\operatorname{erf}(1)}4=0.2106751982\ldots.}
\]
The unsigned ordinary Markov growth remains of order \(n\), whereas the signed spectral radius is of order \(\sqrt n\) in distribution. Equivalently, the orientation-weighted formal Markov zeta function \(\exp(\sum_{k\ge1}\operatorname{tr}(S_\varepsilon^k)t^k/k)=\det(I-tS_\varepsilon)^{-1}\) typically has a singularity radius of order \(n^{-1/2}\), rather than the unsigned order \(n^{-1}\). The law is over **randomly chosen maps**, not random orbits of one fixed map.

## Assumptions and scope
Only Oliveira's canonical affine Markov realization [1, Theorem 7.1] is used; a different map with the same orientation word need not have this law. Index the \(n\) equal partition intervals by \(0,\ldots,n-1\). For \(1\le j<n\), define
\[
u_j=\mathbf1_{\{\varepsilon_{j-1}=-1,\varepsilon_j=+1\}},\qquad
v_j=\mathbf1_{\{\varepsilon_{j-1}=+1,\varepsilon_j=-1\}},
\quad u_0=v_0=0.
\]
Let \(A=\sum_j u_j\), \(B=\sum_j v_j\), \(E=\sum_j\varepsilon_j\), \(a=u_{n-1}\), \(b=v_{n-1}\), \(U=\varepsilon_0\), and \(V=\varepsilon_{n-1}\). Here \(U,V\) denote the finite-word endpoints, which converge jointly with the normalized bulk sum to the independent limit variables with the same letters. The published Markov construction has
\[
M_\varepsilon=\mathbf1\mathbf1^{\mathsf T}-u e_0^{\mathsf T}-v e_{n-1}^{\mathsf T}.
\]
The signed matrix weights each outgoing branch path by its orientation. For integer \(k\ge1\), \(\operatorname{tr}(S_\varepsilon^k)\) is the signed count of closed symbolic Markov walks of length \(k\), with weight the product of branch orientations. It is not asserted to count geometrically distinct periodic points without endpoint corrections.

## Proof
**1. Exact three-dimensional signed reduction.** Because \(\varepsilon_j=+1\) at a \(-\to+\) switch and \(\varepsilon_j=-1\) at a \(+\to-\) switch,
\[
S_\varepsilon=\varepsilon\mathbf1^{\mathsf T}-u e_0^{\mathsf T}+v e_{n-1}^{\mathsf T}.
\]
Factor as \(S=XY\), with columns of \(X\) equal to \(\varepsilon,u,v\), and the three rows of \(Y\) equal to \(\mathbf1^{\mathsf T},-e_0^{\mathsf T},e_{n-1}^{\mathsf T}\). Sylvester's determinant identity makes the nonzero spectra of \(S\) and \(YX\) identical, including multiplicities, and yields
\[
\det(zI_n-S)=z^{n-3}\det(zI_3-H),\qquad
H=\begin{pmatrix}E&-A&B\\U&0&0\\V&-a&b\end{pmatrix}.
\]
Direct expansion gives the exact cubic
\[
q_\varepsilon(z)=z^3-(E+b)z^2+(AU-BV+Eb)z+U(Ba-Ab).
\]
No unproved eigenvalue estimate is used in this reduction.

**2. Bulk statistics jointly with endpoint signs.** The interior \(n-2\) signs are independent of \((U,V)\). Thus the classical central limit theorem gives
\[
(E/\sqrt n,U,V)\Longrightarrow(Z,U,V)
\]
with mutually independent limits. The switch indicators \((u_j)\) and \((v_j)\) are bounded one-dependent sequences; each has expectation \(1/4\), and a weak law (or separate laws on even and odd indices) yields \(A/n\to1/4\) and \(B/n\to1/4\) in probability. Terminal indicators \(a,b\) are bounded. Consequently, with \(z=\sqrt n\,x\),
\[
\frac{q_\varepsilon(\sqrt n\,x)}{n^{3/2}}
\Longrightarrow x\bigl(x^2-Zx+(U-V)/4\bigr)
\]
in coefficient distribution. The coefficient of \(x\) is \(AU/n-BV/n+Eb/n\); the last term vanishes in probability. The constant term is bounded by \(n/n^{3/2}\). Root multisets of monic fixed-degree polynomials vary continuously with coefficients. By the continuous mapping theorem the largest root modulus, namely \(\rho(S_\varepsilon)/\sqrt n\), converges in law to the largest root modulus of the displayed limiting polynomial.

**3. Solve the limiting quadratic and locate the atom.** When \(U=V\), the quadratic is \(x(x-Z)\), and its largest root modulus is \(|Z|\). When \(U=1,V=-1\), it is \(x^2-Zx+1/2\). For \(|Z|<\sqrt2\) its conjugate roots both have modulus \(\sqrt{1/2}\); for \(|Z|>\sqrt2\) the displayed real-root formula follows. When \(U=-1,V=1\), the quadratic is \(x^2-Zx-1/2\), whose two real roots have largest modulus \((|Z|+\sqrt{Z^2+2})/2\). Endpoints are independent fair signs, so the conjugate-root regime contributes mass \(\tfrac14\mathbb P(|Z|\le\sqrt2)=\operatorname{erf}(1)/4\). Every other branch of the mixture has a continuous distribution, hence there is no other atom. The limiting random variable is strictly positive almost surely.

**4. Contrast with unsigned growth and zeta radius.** Every row of the published unsigned \(M\) has \(n\) or \(n-1\) ones; the Perron-Frobenius row-sum bounds give \(n-1\le\rho(M)\le n\) for every word. The logarithmic trace-determinant identity is a formal power-series identity for every finite matrix. If \(\rho(S)>0\), the nearest zero of \(\det(I-tS)\) has modulus \(1/\rho(S)\); a zero spectral radius corresponds to a polynomial zeta function with infinite radius. Since the limiting \(R\) is positive almost surely, the asserted typical singularity scale follows in distribution. No identification of this orientation-weighted determinant with an uncorrected geometric periodic-point zeta function is required.

## Verification
The accompanying standalone `verify.py` uses Python 3 standard library. It reconstructs both full matrices \(S\) and reduced matrices \(H\) and computes characteristic polynomials by exact integer arithmetic. Exhaustive enumeration covers all \(2^n\) orientations for every \(3\le n\le9\), namely 1016 words, verifying both the dimension-reduction identity and all cubic coefficients. Seeded finite sampling at three additional sizes checks the behavior of the normalized signed sum and switch densities, without replacing the probabilistic limit argument. Run `python3 verify.py`. The numerical atom value uses the standard Gaussian integral, not a finite Monte Carlo frequency. These finite checks are corroboration; the convergence and atom are proved above for all sufficiently large \(n\).

## Relationship to prior work
Oliveira [1] constructs the canonical affine family, its unsigned adjacency matrix and rank-three reduction; Section 6.3 and Corollary 7.3 explicitly introduce orientation-weighted matrices and compare individual signed trace sequences. The deterministic ingredients and the very notion of orientation weights are not new. The present additional result is the full *random-word asymptotic spectral distribution* for those orientation-weighted matrices, including the positive Gaussian discriminant atom and the signed/unsigned growth-scale split.

The related published study *Sharp uniform Parry mixing in all-orientation high-entropy interval maps* [3] gives a unit-disk bound for the **non-Perron unsigned eigenvalues** and a Parry mixing rate, but its operator is \(M\), not \(\operatorname{diag}(\varepsilon)M\). The companion *Universal switching statistics and a sharp physical-entropy gap in minimal-rank interval maps* [4] gives a two-state switching factor under a fixed map's physical invariant probability, for words with equal terminal signs; its probability is on time-orbits, not uniformly random orientation words. Neither statement implies the three-case signed spectral law. Rugh and Tan [2] develop general weighted kneading and zeta identities, but the inspected development does not specialize to the present random-orientation, three-root Gaussian law. Previous calculations of unsigned entropy across all orientation words are likewise not a claim to the random signed spectral distribution. Literature searches found no verified equivalent, not a proof that none exists.

## Limitations
The statement is asymptotic in the *number of branches*, with one independently sampled orientation word for each size. It does not claim almost-sure convergence along a coupled sequence, or a Gaussian fluctuation law for time iterates of any one map. The signed trace sums can cancel at individual periods; their general pointwise exponential growth is not asserted. The denominator \(\det(I-tS)\) is a symbolic orientation-weighted Markov determinant; endpoint corrections may be needed to identify a geometric signed periodic-point zeta function. An equivalent special case in older signed-transfer or random-matrix literature remains a priority risk. Independent mathematical validation has not been performed.

## References
[1] Henrique M. Oliveira, *Homological reduction and entropy of discontinuous interval maps*, arXiv:2611.03287v1, first publicly posted 2026-11-02, Sections 6.3 and 7.1–7.2. https://arxiv.org/html/2611.03287v1

[2] Hans Henrik Rugh and Lei Tan, *Kneading with weights*, arXiv:1407.5313; *Journal of Fractal Geometry* 2 (2015), 339–375, DOI 10.4171/JFG/24. https://arxiv.org/abs/1407.5313

[3] *Sharp uniform Parry mixing in all-orientation high-entropy interval maps*, published mathematical result, 2026-11-17. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-uniform-parry-mixing-in-all-orientation-high-entropy-inter--f035502a5c10

[4] *Universal switching statistics and a sharp physical-entropy gap in minimal-rank interval maps*, published mathematical result, 2026-11-17. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-universal-switching-statistics-and-a-sharp-physical-entropy-gap--d13a003ecd84
