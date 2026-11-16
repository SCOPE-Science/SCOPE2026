# Sharp Fourier-frame bounds for three hard-core particles on a cycle

## Finding
For every integer \(n\ge7\), let \(\mathcal I_{n,3}\) be the set of all three-element independent sets of the simple cycle \(C_n\), represented by their indicator vectors \(x\in\{0,1\}^n\). Equip this set with uniform probability. For \(0\le j<n\), define the centered first-degree Walsh character
\[
 \psi_j(x)=(-1)^{x_j}-\mathbb E[(-1)^{x_j}]=-2(x_j-3/n),
\]
and let \(G_n=(\mathbb E[\psi_i\psi_j])_{0\le i,j<n}\). Write
\[
 T_n=\frac{n(n-4)(n-5)}6,\qquad \theta_k=\frac{2\pi k}{n}.
\]
The exact eigenvalues of \(G_n\), in cyclic Fourier modes \(k=0,1,\ldots,n-1\), are
\[
 \boxed{\gamma_{n,0}=0,\qquad
 \gamma_{n,k}=4\left[\frac3n-\frac{(n-6)(1+2\cos\theta_k)-2\cos(2\theta_k)}{T_n}\right],\quad1\le k<n.}
\]
Every nonconstant eigenvalue is strictly positive. Its smallest value occurs **only** at the two Fourier frequencies \(k=1,n-1\). Its largest value occurs only at \(k=n/2\) when \(n\) is even, or at \(k=(n-1)/2,(n+1)/2\) when \(n\) is odd. Consequently the sharp squared-energy conditioning after quotienting the unique constant-sum dependence is
\[
 \boxed{\kappa_n=\frac{\gamma_{n,\lfloor n/2\rfloor}}{\gamma_{n,1}}
      =1+\frac8n+O(n^{-2})\quad(n\to\infty).}
\]
The boundary is sharp: at \(n=6\) there are just two complementary alternating configurations; then \(G_6\) has one eigenvalue \(6\) and five zero eigenvalues. For \(n<6\) the three-particle independent-set ensemble is empty.

## Assumptions and scope
The cycle is indexed by \(\mathbb Z/n\mathbb Z\), and the edges include the last-to-first pair. The inner product is the **probability-normalized** uniform inner product, not unnormalized counting measure. The Gram is on the centered degree-one coordinate characters, so the deterministic particle-number constraint generates the zero eigenvalue at the constant spatial Fourier mode. The condition ratio refers to the positive eigenvalues, not to the singular full Gram. All eigenvalue multiplicities are spatial Fourier multiplicities; the two conjugate nonreal modes together give a two-dimensional real eigenspace. The result is not claimed for any other particle number, arbitrary graphs, or a grand-canonical particle-number mixture.

## Proof
**1. Uniform triple counts.** Denote by \(T_n\) the size of \(\mathcal I_{n,3}\). Fix a distinguished occupied position. The three cyclic gaps between successive occupied positions must be at least two and sum to \(n\); the number of ordered compositions is \(\binom{n-4}{2}\). Each triple is counted at its three occupied positions, giving
\[
 T_n=\frac n3\binom{n-4}{2}=\frac{n(n-4)(n-5)}6.
\]
Rotation invariance yields \(\mathbb E[x_0]=3/n\). For two prescribed sites at cyclic separation \(r\), the number of admissible third sites is zero for \(r=1,n-1\); it is \(n-5\) for \(r=2,n-2\); and it is \(n-6\) for every \(3\le r\le n-3\). These cases exhaust \(n\ge7\). Put \(C_n=(\operatorname{Cov}(x_i,x_j))\) and \(p=3/n\). Its first row has entries
\[
 C_n(0,0)=p-p^2,\quad C_n(0,1)=C_n(0,n-1)=-p^2,
\]
\[
 C_n(0,2)=C_n(0,n-2)=\frac{n-5}{T_n}-p^2,
 \qquad C_n(0,r)=\frac{n-6}{T_n}-p^2\quad(3\le r\le n-3).
\]
The sum of the first row is zero because \(\sum_jx_j=3\) on every sampled configuration.

**2. The exact spectrum.** Circulant matrices are diagonalized by \(v_k(j)=e^{2\pi i kj/n}\). On \(k\ne0\), the constant centering term vanishes; also
\(\sum_{r=1}^{n-1}e^{ir\theta_k}=-1\). The off-diagonal uncentered moment row is a constant \((n-6)/T_n\), modified by \(-(n-6)/T_n\) at distances one and by \(1/T_n\) at distances two. Thus the \(k\)-th eigenvalue of \(C_n\) is
\[
 \lambda_{n,k}=p-\frac{n-6}{T_n}(1+2\cos\theta_k)
                         +\frac2{T_n}\cos(2\theta_k).
\]
Since \(\psi_j=-2(x_j-p)\), \(G_n=4C_n\); hence \(\gamma_{n,k}=4\lambda_{n,k}\). Its zero mode vanishes exactly by the fixed particle number.

**3. Strict ordering for \(n\ge10\).** Regard the nonzero eigenvalue as a polynomial in \(c=\cos\theta\):
\[
 F_n(c)=\frac3n+\frac{4c^2-2(n-6)c-(n-4)}{T_n},\quad -1\le c\le1.
\]
It has derivative \(F_n'(c)=[8c-2(n-6)]/T_n\), strictly negative on \([-1,1)\) for every \(n\ge10\). The available cosines are strictly decreasing from \(\cos(2\pi/n)\) down to \(\cos(2\pi\lfloor n/2\rfloor/n)\) on the half-spectrum. Therefore the asserted minimum and maximum frequencies are exact and unique apart from complex-conjugate symmetry. Moreover
\[
 F_n(1)=\frac{3(n^2-15n+60)}{n(n-4)(n-5)}>0,
\]
since the quadratic in the numerator has negative discriminant and positive leading coefficient. Hence every nonconstant eigenvalue is positive for these lengths.

**4. The three short lengths.** For \(n=7,8,9\), the parabola \(F_n\) has vertex at \(c_*=(n-6)/4\). Its value is
\[
 F_n(c_*)=\frac3n-\frac{n-4+(n-6)^2/4}{T_n}.
\]
For \(n=8,9\), this equals \(1/16\) and \(11/120\), respectively, proving positivity. The vertex is at \(1/2\) and \(3/4\). For \(n=8\), the half-spectrum cosines are \(\sqrt2/2,0,-\sqrt2/2,-1\), so the vertex-nearest and vertex-farthest modes are visibly the first and last. For \(n=9\), the three nontrivial roots of \(8c^3-6c+1\) are \(\cos(2\pi/9)\), \(\cos(4\pi/9)\), and \(\cos(8\pi/9)\), located respectively in the exact rational intervals \((3/4,4/5)\), \((1/6,1/5)\), and \((-1,-9/10)\); the fourth half-spectrum cosine is \(\cos(6\pi/9)=-1/2\). The first is uniquely closest to \(3/4\) and the last uniquely farthest. These rational isolations follow from substituting interval endpoints into the cubic, obtaining opposite signs on every interval, which together contain its three distinct real roots.

For \(n=7\), \(F_7(c)=2c(2c-1)/7\), and its vertex is \(1/4\). The roots of \(8c^3+4c^2-4c-1\), which are \(\cos(2\pi/7)\), \(\cos(4\pi/7)\), \(\cos(6\pi/7)\), respectively lie in \((3/5,2/3)\), \((-1/4,-1/5)\), and \((-1,-4/5)\). The first cosine is greater than \(1/2\), the other two are negative, so all sampled eigenvalues are positive. Their distances to \(1/4\) show the first mode uniquely minimizes and the last uniquely maximizes. In particular, the upper distance bound \(2/3-1/4=5/12\) for the first mode is less than the lower distance bound \(1/4+1/5=9/20\) for the second. This completes the all-length ordering and strict positivity. For \(n=6\), only the alternating occupied triples remain, making \(G_6\) a rank-one matrix with the stated eigenvalues.

**5. Sharp asymptotics.** As \(n\to\infty\), \(T_n=n^3/6+O(n^2)\), \(\cos(2\pi/n)=1+O(n^{-2})\), and \(\cos(2\pi\lfloor n/2\rfloor/n)=-1+O(n^{-2})\). Inserting these expansions into the exact formula gives
\[
 \lambda_{n,1}=\frac3n-\frac{18}{n^2}+O(n^{-3}),\qquad
 \lambda_{n,\lfloor n/2\rfloor}=\frac3n+\frac6{n^2}+O(n^{-3}).
\]
Their ratio, unchanged by the common Walsh factor four, equals \(1+8/n+O(n^{-2})\). Exact extremal frequencies make this the sharp, not merely an upper, condition estimate.

## Verification
Run `python3 verify.py` with Python 3 and only its standard library. The checker independently enumerates every admissible triple for \(7\le n\le26\), compares exact rational two-site covariances with the formula, checks all Fourier eigenvalues, tests the exact rational cubic brackets, and evaluates mode orderings for \(7\le n\le1000\) and the leading asymptotic coefficient at larger lengths. It also checks the exceptional six-site rank-one sample. These are finite reproducibility checks, not a substitute for the preceding proof for all lengths.

## Relationship to prior work
The standard nearest-neighbor hard-core lattice gas and cycle independent-set enumerations supply the objects and elementary counting background; these counting identities are not claimed as new. Jain, Perkins, Sah and Sawhney (2021) study efficient sampling of fixed-size independent sets on bounded-degree graphs and Fourier inversion of the particle-number distribution, but do not classify spatial Fourier sampling eigenvalues for fixed-size cycle ensembles. Vavro (2001) studies the canonical one-dimensional lattice-gas partition function rather than sharp spatial Fourier frame bounds. Published Lucas-cube covariance analyses treat the **mixture of all independent-set sizes** (and, separately, vertex sampling of the full stable-set polytope), not its conditional three-particle layer. Their complete spectra cannot be substituted for the conditional Gram spectrum, which has an exact zero mode and a different limiting condition number. The contribution is the all-length sharp mode identification, precise rank threshold, and limiting \(8/n\) stability law for this first genuinely three-particle microcanonical hard-core layer.

## Limitations
This result is confined to exactly three occupied, nearest-neighbor-excluding sites; no statement is made for general fixed density, arbitrary particle count, higher Walsh degrees, or different exclusion ranges. Older canonical one-dimensional lattice-gas structure-factor calculations may imply portions of the elementary moment formula after reparameterization; the full historical priority of the sharp finite-length mode and conditioning classification remains open to further specialist inspection. The full four-page manuscript of Vavro (2001) was examined: its periodic-cluster partition counts do not give the specific spatial covariance, extremal frequency classification or sharp condition ratio.

## References
- V. Jain, W. Perkins, A. Sah, M. Sawhney, *Approximate counting and sampling via local central limit theorems*, arXiv:2108.01161, first public version 2021-08-02. https://arxiv.org/abs/2108.01161
- J. Vavro, *Exact solution for the lattice gas model in one dimension*, Physical Review E 63 (2001), 057104. https://doi.org/10.1103/PhysRevE.63.057104
- P. Codara and O. M. D'Antona, *Generalized Fibonacci and Lucas cubes arising from powers of paths and cycles*, arXiv:1410.4080, first public version 2014-10-15. https://arxiv.org/abs/1410.4080
