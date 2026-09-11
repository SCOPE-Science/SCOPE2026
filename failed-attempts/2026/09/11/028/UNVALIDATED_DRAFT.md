# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Explicit isotropic-constant certificate for the vertex-axis section of the isotropic regular 10-simplex

## Claim (preset fallback)

Let $\Delta_{10}\subset H_0\subset\mathbb R^{11}$ be the regular $10$-simplex in
isotropic position (volume $1$, barycenter $0$, covariance $L^2I_{10}$).
Let $u_*$ be a normalized vertex direction and
$K^*_{10}=\Delta_{10}\cap u_*^\perp$. Then

$$L_{K^*_{10}}\le 2.2,$$

in fact $0.347\le L_{K^*_{10}}\le 0.349$, with the full $9\times 9$
covariance spectrum $\{\sigma^2\times 9\}$,
$\sigma^2=\mu^2/110\approx 0.121237$, $\mu=\tfrac{10}{11}\lambda$,
$\lambda^{10}=10!/\sqrt{11}$, $\mathrm{Vol}_9(K^*_{10})=\mu^9\sqrt{10}/9!
\approx 1.0066$. Referee replay:
`output/artifacts/verify_fallback.py` ($\to$ `VERIFY_OK`, stdlib only,
threshold checks by exact integer arithmetic).

## 1. Isotropic simplex: explicit coordinates and affine map

Let $S=\mathrm{conv}\{e_1,\dots,e_{11}\}\subset H:=\{x:\sum x_i=1\}\subset
\mathbb R^{11}$ (regular, edge $\sqrt2$) with centroid
$c=\frac1{11}{\bf 1}$. Centered vertices $v_i=e_i-c$ span
$H_0=\{\sum x_i=0\}\cong\mathbb R^{10}$.
The $10$-volume is $\mathrm{Vol}_{10}(S)=\sqrt{11}/10!$.

Put $\lambda=\mathrm{Vol}_{10}(S)^{-1/10}$, i.e.
$\lambda^{10}=10!/\sqrt{11}\approx 4.017^{10}$ (rigorous coarse bracket
$4\le\lambda\le 41/10$ is certified in the replay script by integer
arithmetic from $3.3166^2<11<3.3167^2$), and $W_i=\lambda v_i$.
Then $\Delta_{10}:=\mathrm{conv}\{W_i\}$ has volume $1$ and barycenter $0$.

Covariance. Uniform law on $S$ is Dirichlet$(1,\dots,1)$:
$\mathbb EX_i=1/11$, $\mathbb EX_i^2=2/(11\cdot12)$,
$\mathbb EX_iX_j=1/(11\cdot12)$ ($i\ne j$), so on $H_0$

$$\Sigma_S=\frac{11I-J}{11^2\cdot 12},\qquad
\Sigma_S|_{H_0}=\frac1{11\cdot 12}I_{10}=\frac1{132}I_{10},$$

since $11I-J$ has eigenvalue $1$ on ${\bf 1}$ and $11$ on $H_0$.
Hence with the dilation $\lambda$,

$$\mathrm{Cov}(\Delta_{10})=\frac{\lambda^2}{132}\,I_{10},$$

so $\Delta_{10}$ is isotropic with $L_{\Delta_{10}}^2=\lambda^2/132
\approx 0.122247$. This is item (i): the affine map
$x\mapsto\lambda(x-c)$ and the vertices $W_i$ are fully explicit; no
constant is missing.

## 2. Section combinatorics: $K^*_{10}$ is a regular $9$-simplex

Take $u_*=W_{11}/|W_{11}|$ (any vertex axis; all are congruent under
$S_{11}$). In units of $\lambda^2$,

$$\langle v_i,v_j\rangle=\delta_{ij}-\tfrac1{11},\quad\text{i.e.}\quad
\langle W_{11},W_{11}\rangle=\tfrac{10}{11}\lambda^2>0,\ \
\langle W_j,W_{11}\rangle=-\tfrac1{11}\lambda^2<0\ (j\le 10).$$

Thus $u_*^\perp$ strictly separates $W_{11}$ from the other ten vertices.
Every edge $(i,j)$ with $i,j\le 10$ has both endpoints strictly negative,
hence does not meet the hyperplane; exactly the ten edges $(11,j)$ cross
it, at parameter
$t=\frac{10/11}{10/11+1/11}=\frac{10}{11}$:

$$p_j=\tfrac1{11}W_{11}+\tfrac{10}{11}W_j,\qquad j=1,\dots,10,$$
$$\langle p_j,W_{11}\rangle
 =\tfrac1{11}\tfrac{10}{11}\lambda^2-\tfrac{10}{11}\tfrac1{11}\lambda^2=0.$$

A hyperplane section of a simplex is the convex hull of its edge crossings,
so $K^*_{10}=\mathrm{conv}\{p_1,\dots,p_{10}\}$.
Moreover $\sum_j p_j=\frac{10}{11}W_{11}+\frac{10}{11}\sum_{j\le10}W_j
=\frac{10}{11}\sum_{i=1}^{11}W_i=0$ (verified coordinate-wise over
$\mathbb Q$ in the script), so the section is central with centroid $0$;
and $p_j-p_{10}=\frac{10}{11}\lambda(e_j-e_{10})$, $j\le 9$, are nine
linearly independent vectors, so $K^*_{10}$ is a $9$-simplex. All mutual
distances agree,
$|p_j-p_k|^2=2(\frac{10}{11}\lambda)^2$, so it is regular of edge
$a=\mu\sqrt2$ with $\mu:=\frac{10}{11}\lambda\approx 3.65186$.

Volume (item (ii)). A regular $9$-simplex of edge $a=\mu\sqrt2$ has

$$\mathrm{Vol}_9(K^*_{10})=\mu^9\,\frac{\sqrt{10}}{9!}\approx 1.00661,$$

with rigorous enclosure $[0.9688,1.2099]$ from $\lambda\in[4,41/10]$
($\mathrm{Vol}_9^2$ is monotone in $\lambda$; endpoints are exact
rationals compared by integer arithmetic in the script). The polytope is
given in closed form by the vertices $p_j$ above.

## 3. Spectrum and isotropic constant (item (iii))

The stabilizer $S_{10}$ permuting $\{W_1,\dots,W_{10}\}$ fixes $u_*$ and
acts transitively on $\{p_j\}$ by isometries of the section hyperplane;
hence $\mathrm{Cov}(K^*_{10})=\sigma^2I_9$ for a scalar $\sigma^2$.
The standard $9$-simplex $S_9=\mathrm{conv}\{e_1,\dots,e_{10}\}$ has, by the
same Dirichlet computation with $10$ variables,
$\Sigma_{S_9}|=\frac1{10\cdot 11}I_9=\frac1{110}I_9$.
$K^*_{10}$ is isometric to $\mu S_9$, so the full eigenvalue list is

$$\mathrm{spec}\,\mathrm{Cov}(K^*_{10})
 =\{\sigma^2\times 9\},\qquad
 \sigma^2=\frac{\mu^2}{110}=\frac{10}{1331}\lambda^2\approx 0.121237.$$

($\mu^2/110=(100/121)\lambda^2/110=(10/1331)\lambda^2$; exact
cancellation logged in the script.)

Isotropic constant. With $\mathrm{Vol}_9=\mu^9\sqrt{10}/9!$,

$$L_{K^*_{10}}^2=\frac{\sigma^2}{\mathrm{Vol}_9^{2/9}}
 =\frac{(9!)^{2/9}}{110\cdot 10^{1/9}},\qquad
 L_{K^*_{10}}^{18}=\frac{(9!)^2}{10\cdot 110^9}
 =\frac{5143824}{921073316796875}\approx 0.00558429,$$

the similitude ratio $\mu$ cancelling exactly (affine invariance: every
$9$-simplex shares this $L$). Threshold checks are pure integer
comparisons, e.g. $L\le 11/5\iff (9!)^2\cdot 5^{18}\le 11^{18}\cdot 10
\cdot 110^9$ (bit-lengths $\sim$79 vs $\sim$127, both sides exact).
Consequences, all machine-checked in `verify_fallback.py`:

- $L_{K^*_{10}}\le 11/5=2.2$ (fallback threshold, huge margin);
- sharp enclosure $0.347\le L_{K^*_{10}}\le 0.349$
  ($L_{K^*_{10}}\approx 0.3479361$), i.e. the certificate is not merely a
  loose upper bound but pins the invariant.

Spectrum consistency: the script recomputes
$L=\sigma/\mathrm{Vol}_9^{1/9}$ from the logged $\sigma^2$ and volume and
recovers the same float, closing the loop eigenvalues
$\to$ volume $\to L$.

## 4. Scope notes (honest boundaries)

- The vertex orbit has $11$ congruent sections (full $S_{11}$ symmetry maps
  any vertex axis to any other), so the same number holds uniformly over
  $F_{\mathrm{vert}}$; the fallback claims only the named section.
- The target's mandated Eldan one-stage estimate
  $\mathbb E[\mathrm{tr}(A_t^2)]\le 10+4t$ is NOT proved here and is not
  needed for the numeric conclusion; see `output/target_exit.json`.
- Classical inputs used: Dirichlet moments of uniform simplices,
  volume $\sqrt{10}/9!$ of the regular $9$-simplex, affine invariance of
  $L_K$. No stochastic-localization or thin-shell estimate is invoked.
- The value $L\approx 0.348$ is far below the $2.2$ threshold, so the
  certificate has large slack; it is a first explicit benchmark for this
  suspected-extremal family, not a sharp-constant result.
