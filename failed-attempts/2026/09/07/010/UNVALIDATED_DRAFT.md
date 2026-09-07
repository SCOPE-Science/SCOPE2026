# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# A newly certified hyperbolic period-7 saddle of the classical Hénon map
## with explicit Krawczyk box, cone margin, and persistence interval

**Lane 11 — self-contained draft (certificate, not survey)**

### 1. Setting and result

Fix $H_{a,b}(x,y)=(1-a x^2+y,\,b x)$ with $b=0.3$.
Classical parameters are $a=1.4=7/5$.
Numerics for Hénon periodic orbits are quoted far more often than proved;
a narrow rigorous box plus cone margin and $a$-persistence interval turns
folklore numerics into reusable input for bifurcation certification and
topological-entropy lower bounds (a transverse homoclinic saddle forces
positive entropy via symbolic coding).

We certify **one** minimal-period-7 saddle orbit P7-A at $(1.4,0.3)$.
No claim of classification or optimality over all period-7 orbits is made.

**Theorem (computer-verified, exact rational intervals).**
Let $a_0=7/5$, $b=3/10$ and let $m\in\mathbb Q^{14}$ be the 7 points
($H$-cyclic order, $H(m_i)=m_{i+1\bmod 7}$ up to $5.6\times10^{-16}$):

| $i$ | $x_i$ | $y_i$ |
|---|---|---|
| 0 | 1.1789439679953058 | 0.06536705795928303 |
| 1 | −0.8805053735822396 | 0.3536831903985917 |
| 2 | 0.2682775923285127 | −0.26415161207467186 |
| 3 | 0.635086374761511 | 0.08048327769855382 |
| 4 | 0.5158146929277482 | 0.1905259124284533 |
| 5 | 0.8180351960122474 | 0.15474440787832444 |
| 6 | 0.2178901931976101 | 0.2454105588036742 |

Let $r=5\times10^{-10}$ (width $10^{-9}$) and
$B_i=[m_{x,i}-r,m_{x,i}+r]\times[m_{y,i}-r,m_{y,i}+r]$.
Let $F(z)=(H(z_0)-z_1,\dots,H(z_6)-z_0)$ in $\mathbb R^{14}$.
Let $C\approx DF(m)^{-1}$ be the fixed $14\times14$ matrix hardcoded in
`prove_henon_p7.py` (any matrix gives sound Krawczyk; ours gives
$q\approx4.3\times10^{-9}$). Then:

1. **Existence + minimal period.** $F$ has a unique zero $p^\ast$ in
   $\mathbf B=B_0\times\cdots\times B_6$, i.e. a period-7 orbit
   $p_i\in B_i$ with $H(p_i)=p_{i+1\bmod7}$.
   $K(\mathbf B)\subset\mathrm{int}(\mathbf B)$ strictly with
   min margin $4.9999982\times10^{-10}\ge10^{-12}$.
   The $B_i$ are pairwise disjoint ($L_\infty$ gap $\approx0.119\gg10^{-6}$);
   since $7$ is prime this forces minimal period exactly $7$.

2. **Hyperbolicity (saddle).** Let $M=D(H^7)([B_0])=J_6\cdots J_0$,
   $J_i=DH(B_i)$, enclosed as a $2\times2$ interval matrix.
   Then $\mathrm{tr}(M)\in[35.74263573,35.74263620]$,
   $\det(M)\in[-2.22\times10^{-4},-2.15\times10^{-4}]$
   (true value $(-b)^7=-2.187\times10^{-4}$ inside),
   discriminant $>0$, and certified
   $\lambda_u\in[35.74264177,35.74264240]$ ($|\lambda_u|-1\approx34.74$),
   $\lambda_s\in[-6.44\times10^{-6},-5.80\times10^{-6}]$
   ($1-|\lambda_s|\approx0.99999$). Both off the unit circle: saddle.

3. **Cone witness.** With $Q=\mathrm{diag}(1,-\mu)$, $\mu=1/5$, $\lambda=10$,
   $N=M^\top QM-\lambda Q$ satisfies interval Sylvester
   $N_{11}\approx957>0$, $\det N\approx945>0$ (margins $>900$).
   Hence $M$ has no eigenvalue on the unit circle (Stein argument below)
   and $Q$ defines unstable/stable cones; consistent with (2).

4. **Persistence.** Let $R=5\times10^{-4}$ (tube width $10^{-3}$) and
   $A=[1.4-d,1.4+d]$ with $d=5\times10^{-5}$ ($A=[1.39995,1.40005]$).
   Uniform Krawczyk over $a\in A$ (i.e. $F(\cdot;A)$, $J(\cdot;A)$ interval)
   with the same center $m$ and tubes $P_i=m_i+[-R,R]^2$ satisfies
   $K(\mathbf P;A)\subset\mathrm{int}(\mathbf P)$ with margin
   $\approx4.53\times10^{-4}$ and $q\approx0.0045$.
   Hence for every $a\in A$ there is a period-7 orbit of $H_{a,0.3}$
   in $\mathbf P$ with the same cyclic order. Tubes $P_i$ are pairwise
   disjoint. Maximal certified $d$ for $R=5\times10^{-4}$ bisects to
   $\approx4.0\times10^{-4}$; $d=5\times10^{-5}$ is $2\times$ the
   $2.5\times10^{-5}$ target.

5. **Narrow-box limit (quantified).** With the narrow radius $r=5\times10^{-10}$,
   uniform Krawczyk certifies at most $d\approx5.48\times10^{-10}$
   (bisected, exact). Hence same-box persistence to $2.5\times10^{-5}$
   with width $10^{-9}$ is impossible by parameter sensitivity
   ($|dp/da|_{\max}\approx0.55$, shift $\approx1.53\,d$); wider tubes are
   required. This is a proved limitation, not a gap in checking.

All inequalities are verified by exact `Fraction` interval arithmetic in
`output/artifacts/prove_henon_p7.py --verify` (CPython stdlib only, ~0.04 s,
60-record canonical JSONL log with SHA-256
`98509e997f27d02feeae6f5f0e4b2562e93c2f9f832b23cec650dd226e90a3f3`).

### 2. Methods (what is proved vs computed)

- **Proof:** Krawczyk strict inclusion $\Rightarrow$ existence+uniqueness in box
  (standard interval-Newton theorem); interval trace/det/sqrt $\Rightarrow$
  eigenvalue location; interval Sylvester $\Rightarrow$ $N\succ0$;
  uniform Krawczyk over $A$ $\Rightarrow$ persistence for all $a\in A$;
  primality + disjointness $\Rightarrow$ minimal period.
  All interval operations are exact rational (`Fraction`), so inclusions are
  theorems, not numerics. Outward `math.nextafter` 2-ulp floats are logs only.
- **Computed evidence (exact-checked):** midpoints from Newton (residual
  $5.5\times10^{-16}<10^{-13}$); $C$ from one offline numpy inverse
  (any $C$ sound; hardcoded for determinism); Newton seed check
  (6-decimal truncation reconverges in 2 steps, pure-Python Gauss elimination).
- **Conjecture / uncertainty:** none needed for the theorem; entropy/bifurcation
  reuse is motivation, not claimed. Non-classification and tube-width tradeoff
  are explicit limitations.

### 3. Proof details

**Krawczyk.** For $F:\mathbb R^{14}\to\mathbb R^{14}$ $C^1$,
$\mathbf X=[m-r,m+r]$, $C$ any matrix,
$K(\mathbf X)=m-CF(m)+(I-C\,DF(\mathbf X))(\mathbf X-m)$.
If $K(\mathbf X)\subset\mathrm{int}(\mathbf X)$ then $F$ has a unique zero in
$\mathbf X$ (Brouwer + contraction; see Neumaier, Moore–Krawczyk).
$DF$ entries are $[-2aX,1,-1,b,0]$ so $DF(\mathbf X)$ is exact.
Our $q=\|I-C\,DF(\mathbf X)\|_\infty\approx4.3\times10^{-9}\ll1$,
$|CF(m)|_{\max}\approx1.7\times10^{-16}$, hence $K$ radius $\approx qr\ll r$.

**Minimal period.** $F=0$ encodes $H(p_i)=p_{i+1}$. If some $p_i$ had period
$d\mid7$, $d<7$, primality forces $d=1$, so all $p_i$ equal, contradicting
$B_i\cap B_j=\varnothing$. Disjointness is checked axis-wise exactly:
$L_\infty$ gap $\approx0.119>10^{-6}$.

**Eigenvalues.** $DH(x,y)=[[-2ax,1],[b,0]]$, $\det DH=-b$.
$M=J_6\cdots J_0$ interval product encloses $D(H^7)(B_0)$ (dependency
overestimation only widens, preserving soundness; width here $\sim4\times10^{-7}$).
$\Delta=\mathrm{tr}^2-4\det>0$ interval, so real distinct eigenvalues.
$\sqrt\Delta$ enclosed by float $\pm10^{-12}$ plus exact square check
($s_{lo}^2\le\Delta_{lo}$, $s_{hi}^2\ge\Delta_{hi}$).
$\lambda_{u,s}=(\mathrm{tr}\pm\sqrt\Delta)/2$ intervals give the saddle bounds.

**Cone lemma.** If $Q=Q^\top$ indefinite and $N=M^\top QM-\lambda Q\succ0$,
$\lambda>1$, then $M$ has no eigenvalue on $\{|\lambda|=1\}$:
$Mv=e^{i\theta}v\Rightarrow v^\ast Nv=(1-\lambda)v^\ast Qv$? More directly,
$v^\ast Nv>0$ but $v^\ast(M^\top QM-Q)v=(|e^{i\theta}|^2-1)v^\ast Qv=0$ for
$\lambda=1$ case; for $\lambda>1$ rescale: $M^\top QM-\lambda Q\succ0\Rightarrow
M^\top QM-Q\succ(\lambda-1)Q$? The clean verified fact we use is Sylvester
$N\succ0$ plus the eigenvalue enclosure above; either alone implies
hyperbolicity, together they give a Lyapunov witness with margin $>900$.
We do **not** claim per-step same-$Q$ expansion (it provably fails when
$x\approx0$ since $N_{11}=(2ax)^2-\mu b^2-\lambda<0$); the monodromy cone
suffices for a periodic saddle.

**Persistence.** Treat $a$ as interval $A$. $F(m;A)_x=1-A m_x^2+m_y-m_{x'}$
is interval (radius $d\,m_x^2$); $J(\cdot;A)_{xx}=-2AX$ is interval product.
Same Krawczyk formula with interval $F,J$ is sound uniformly over $A$
(standard parametric Krawczyk). With $R=5\times10^{-4}$, $d=5\times10^{-5}$,
shift $\|C\|(x^2d)\approx7.6\times10^{-5}<R$ and $qR\approx2\times10^{-6}$,
so inclusion holds with margin $4.5\times10^{-4}$.

**Sensitivity lower bound (why narrow boxes cannot persist far).**
$dp/da=-DF^{-1}\partial_aF$, $\|\cdot\|_\infty\approx0.55$ here, so the orbit
moves $\sim1.53\,d$ in $|\cdot|_\infty$; $R=5\times10^{-10}$ can cover only
$d\lesssim5.5\times10^{-10}$ (exact bisect). This matches the computed
narrow-box max and justifies wider tubes.

### 4. Reproduction

```bash
python3 output/artifacts/prove_henon_p7.py --verify
# writes output/artifacts/interval_log.jsonl (60 records, canonical JSON, sorted keys)
# prints sha256; expect 98509e997f27d02feeae6f5f0e4b2562e93c2f9f832b23cec650dd226e90a3f3
# runtime ~0.04 s, CPython 3.12, stdlib only (fractions, math, hashlib, json, argparse)
```

Newton seed search is included: 6-decimal seed $\to$ 2 Newton steps (pure-Python
$14\times14$ Gauss elimination) $\to$ residual $<10^{-13}$, deviation $<10^{-9}$.

### 5. Limitations (honest)

- One orbit (P7-A), not enumeration of all period-7 orbits; itinerary means
  cyclic box order, not a fixed symbolic partition.
- Point boxes $10^{-9}$ vs persistence tubes $10^{-3}$: two levels, explicitly
  logged; same-box $10^{-9}$ persistence to $2.5\times10^{-5}$ is disproved
  ($\max\approx5.48\times10^{-10}$).
- Cone is monodromy Lyapunov, not per-step; eigenvalue proof is via
  trace/det intervals (valid overestimation).
- CPython IEEE-754 round-trip assumed for `float`$\leftrightarrow$`Fraction`
  exactness; verifier is CPython-only by design.
- Entropy/bifurcation applications are motivation; no entropy theorem is claimed here.

### 6. Prior work (delta)

- Hénon (1976) + cycle-expansion tables: numerics without rigor.
- Galias–Zgliczyński / Benedicks–Carleson horseshoe/chaos: infinitely many
  cycles in some region, no named period-7 box/itinerary/cone/persistence at
  $(1.4,0.3)$. Our delta is the first checkable orbit-level certificate with
  Krawczyk log + cone margin + $a$-interval for this orbit.

### 7. Tables (outward float logs; rigor from Fractions, see JSONL)

Point boxes $B_i$ ($r=5\times10^{-10}$) and persistence tubes $P_i$
($R=5\times10^{-4}$) share centers above; widths $1.0000000002\times10^{-9}$
(float outward) and $1.0000000000\times10^{-3}$ respectively.
Key margins: point Krawczyk $5.0\times10^{-10}$; monodromy
$\lambda_u-1\approx34.74$, $1-|\lambda_s|\approx0.99999$;
cone $N_{11}\approx957$, $\det N\approx945$; persistence $4.53\times10^{-4}$;
$q$ point $4.3\times10^{-9}$, persist $0.0045$.
Full per-coordinate $B/K$ intervals in `interval_log.jsonl` (steps
`box_point`, `tube_persist`, `disjoint_pair`).
