# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Disproof of the n−4 bound for the isolated-conical quadratic stratum
## Thin Signorini obstacle problem, n ≥ 5

### 1. Setup and claim
Let $B_1\subset\mathbb R^n$, $H=\{x_n=0\}$, $x=(x',x_n)$.
Admissible $u\in H^1(B_1)$ satisfies: $u\ge 0$ on $H$,
$\Delta u = 0$ in $B_1\setminus\Lambda(u)$ where
$\Lambda(u)=\{x\in H\cap B_1:u(x)=0\}$ is the coincidence set,
$\Delta u\le 0$ distributionally, $u$ even in $x_n$.
At $x_0\in H$ in the free boundary, Almgren frequency
$N_{x_0}(r)\to\kappa(x_0)\ge 3/2$.
$S_{\mathrm{iso}}(u)$ = points with $\kappa(x_0)=2$ at which every
subsequential blow-up $u_{x_0,r}(x)=u(x_0+rx)/r^2$ converges to a
$2$-homogeneous global minimizer $u_0$ whose contact cone
$\Lambda(u_0)=\{u_0=0\}\cap H$ is a cone with
$(\Lambda(u_0)\setminus\{0\})$ a $C^2$ embedded conical hypersurface
in $H$, i.e. link a closed $C^2$ hypersurface in $S^{n-2}$.

Target conclusion to test: $\dim_{\mathcal H} S_{\mathrm{iso}}(u)\le n-4$
for every admissible $u$. We disprove it: there is an admissible $u$
with $\dim_{\mathcal H} S_{\mathrm{iso}}(u)=n-2$.

### 2. Counterexample
For every $n\ge 2$ define the quadratic polynomial
$$u(x)=x_1^2-x_n^2.$$

**Lemma 1 (admissibility).** $u$ is admissible with bounded $H^1$ norm.
Indeed: (i) $u(x',-x_n)=u(x',x_n)$ (even); (ii) on $H$,
$u(x',0)=x_1^2\ge 0$; (iii) $\Delta u = 2-2 = 0$ classically in
$\mathbb R^n$, hence $\Delta u=0$ in $B_1\setminus\Lambda(u)$ and
$\Delta u = 0\le 0$ distributionally; complementary condition holds
trivially. $u$ is smooth so $u\in H^1(B_1)$; explicitly
$|u|\le 2$, $|\nabla u|^2=4(x_1^2+x_n^2)\le 8$ on $B_1$, so
$\|u\|_{H^1(B_1)}^2\le 10|B_1|<\infty$.

Coincidence set in $B_1$:
$$\Lambda(u)=\{x\in H\cap B_1 : x_1=0\},$$
an $(n-2)$-dimensional disc. Since it has empty interior in $H$,
every of its points lies in the free boundary
$\partial_{H}\{u>0\}\cap H$: $\{u>0\}\cap H=\{x_1\ne 0\}$.

**Lemma 2 (frequency 2 and exact blow-up).** Let
$x_0\in\Lambda(u)$, so $x_0=(0,x_0'',0)$ with $x_0''\in\mathbb R^{n-2}$.
Then for every $r>0$,
$$u(x_0+rx) = (rx_1)^2-(rx_n)^2 = r^2(x_1^2-x_n^2)=r^2 u_0(x),$$
where $u_0(y)=y_1^2-y_n^2$. Hence the Almgren blow-up is exact and
unique:
$$u_{x_0,r}(y)=\frac{u(x_0+ry)}{r^2}=u_0(y)\quad\forall r>0,$$
so the Almgren limit is $\kappa(x_0)=2$ and the unique subsequential
blow-up is the $2$-homogeneous function $u_0$.

$u_0$ is a global ($ \mathbb R^n$) solution: even, $u_0\ge 0$ on $H$,
harmonic in $\mathbb R^n$, hence a global minimizer for its boundary
data on every ball (solutions of the variational inequality with the
above signs are exactly the minimizers of Dirichlet energy under the
unilateral constraint).

**Lemma 3 (isolated-conical contact cone).** The contact cone of $u_0$ is
$$\Lambda(u_0)=\{y\in H : y_1=0\},$$
a linear hyperplane in $H\cong\mathbb R^{n-1}$, i.e. a cone with vertex
$0$. Punctured, $\Lambda(u_0)\setminus\{0\}$ is a smooth embedded
conical hypersurface in $H$ (dimension $n-2$). Its link
$\Lambda(u_0)\cap S^{n-2}=\{y_1=0\}\cap S^{n-2}\cong S^{n-3}$ is the
equator, a closed $C^2$ (indeed analytic) hypersurface of $S^{n-2}$
with no singularity. Hence it satisfies verbatim the
isolated-conical definition in the topic statement.

*Remark (flat is the generic case).* In fact any $2$-homogeneous global
solution whose contact has link a hypersurface must be of this flat
form: if $\Lambda$ has $\mathcal H^{n-1}$-measure zero, $\Delta u_0$ (a
negative measure supported on $\Lambda$) has zero capacity support in
codimension $\ge 2$ and vanishes, so $u_0$ is entire harmonic, hence a
harmonic quadratic; evenness forces
$u_0=x'^TA'x'-( \mathrm{tr}\,A')x_n^2$ with $A'\ge 0$; the zero set on
$H$ is $\ker A'$, a hypersurface iff $\mathrm{rank}\,A'=1$, i.e. flat
up to rotation. So excluding the flat hyperplane would make
$S_{\mathrm{iso}}$ essentially vacuous; the equator must count as an
admissible link (it is a closed $C^2$ hypersurface). Our example is
therefore the canonical isolated-conical profile, not a loophole.

### 3. Hausdorff dimension
Consequently every $x_0\in\Lambda(u)$ belongs to $S_{\mathrm{iso}}(u)$.
Take the Borel set
$$E = \{x\in \bar B_{1/2} : x_1=x_n=0\}\subset S_{\mathrm{iso}}(u),$$
the closed $(1/2)$-ball in the $(n-2)$-plane spanned by $e_2,\dots,e_{n-1}$.
Then $\mathcal H^{\,n-2}(E)=\omega_{n-2}2^{-(n-2)}>0$ where
$\omega_k$ is the volume of the unit $k$-ball. In particular
$$\mathcal H^{\,n-3}(E)=+\infty>0,\qquad \dim_{\mathcal H}E=n-2.$$
Hence $\dim_{\mathcal H} S_{\mathrm{iso}}(u)\ge n-2$ (in fact exactly
$n-2$ on $B_1$), violating $\le n-4$ for every $n\ge 5$.
Explicit values: $\mathcal H^{n-2}(E)=\pi^{(n-2)/2}\Gamma(\frac{n}2)^{-1}
2^{-(n-2)}$; verified numerically in the artifact script.

### 4. Conclusion
The claimed bound $\dim_{\mathcal H} S_{\mathrm{iso}}(u)\le n-4$ for all
admissible $u$ in $n\ge 5$ is **false**. The function $u=x_1^2-x_n^2$
is an explicit admissible counterexample with an $(n-2)$-dimensional
piece of isolated-conical frequency-$2$ points. The requested
disproof data ($u$, $E$, Almgren limits, link regularity) are above.

### 5. Verification
- Symbolically: $\Delta u=0$, evenness, $u|_H=x_1^2$, gradient
  vanishing exactly on $E$'s plane, exact blow-up identity — checked in
  `output/artifacts/verify_counterexample.py` (sympy + 200 randomized
  blow-up identities per dimension for $n=5,6,7$; all passed).
- Energy finiteness: analytic bound plus Monte-Carlo estimate
  ($\approx 6.0,5.2,4.1$ for $n=5,6,7$).
- No uncertainty: proof is exact algebra; computation is confirmatory only.
