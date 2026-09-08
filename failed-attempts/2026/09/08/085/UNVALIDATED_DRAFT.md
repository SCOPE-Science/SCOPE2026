# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Sharp Ehrhart-positivity threshold along the White p=2 diagonal

## Statement

Let $q=2k+1$ ($k\ge 1$) and
$$W_k=\operatorname{conv}\{(0,0,0),(1,0,0),(0,0,1),(2,q,1)\}\subset\mathbb R^3.$$
Let $L_k(t)=|tW_k\cap\mathbb Z^3|$ and write
$L_k(t)=c_3(k)t^3+c_2(k)t^2+c_1(k)t+1$.

**Theorem.** For every integer $k\ge 1$ and every integer $t\ge 0$,
$$L_k(t)=\binom{t+3}{3}+(q-1)\binom{t+1}{3}
      =\frac{qt^3+6t^2+(12-q)t+6}{6}.$$
In particular $c_2(k)=1$ and
$$c_1(k)=\frac{12-q}{6}=\frac{11-2k}{6},$$
which is strictly decreasing in $k$ (step $-1/3$) and vanishes at $k=5.5$.
Hence with $K^*=6$:
$$c_1(k)>0\iff k\le 5,\qquad c_1(k)\le 0\iff k\ge 6,$$
a unique sharp sign change. Moreover each $W_k$ is an empty lattice
tetrahedron of normalized volume $q=2k+1$ ($L_k(1)=4$) and lattice width
exactly $1$ (witness $(0,0,1)$). Its $h^*$-vector is $(1,0,q-1,0)$.

Numerically, $c_1(1..12)$ = $3/2,7/6,5/6,1/2,1/6,-1/6,-1/2,-5/6,-7/6,
-3/2,-11/6,-13/6$.

## Proof

Write $v_0=(0,0,0)$, $v_1=(1,0,0)$, $v_2=(0,0,1)$, $v_3=(2,q,1)$.
$\det(v_1-v_0,v_2-v_0,v_3-v_0)=-q$, so normalized volume is $q$.

For $t>0$, $p=(x,y,z)\in tW_k$ iff $p=\mu_1v_1+\mu_2v_2+\mu_3v_3$ with
$\mu_i\ge 0$, $\mu_1+\mu_2+\mu_3\le t$. Since $x=\mu_1+2\mu_3$,
$y=q\mu_3$, $z=\mu_2+\mu_3$:
$$\mu_3=y/q,\quad \mu_2=z-y/q,\quad \mu_1=x-2y/q.$$
Nonnegativity and the sum bound give the facet description (also valid at
$t=0$):
$$y\ge 0,\quad qz-y\ge 0,\quad qx-2y\ge 0,\quad q(x+z)-2y\le qt.\tag{1}$$
This is proved, not assumed: it is exactly the convex-combination
conditions solved for $(\mu_1,\mu_2,\mu_3)$.

Fix integer $y$. Put
$$X_0=\lceil 2y/q\rceil,\quad Z_0=\lceil y/q\rceil,\quad
  S=\lfloor t+2y/q\rfloor.$$
By (1), admissible integer $(x,z)$ satisfy $x\ge X_0$, $z\ge Z_0$,
$x+z\le S$. With $N=S-X_0-Z_0$, the count is $0$ if $N<0$ else
$\binom{N+2}{2}$ (shift $x'=x-X_0$, $z'=z-Z_0$: pairs with $x'+z'\le N$).

**Lemma.** Write $y=aq+s$, $0\le s<q$. Then
$N(y)=t-a$ if $s=0$, and $N(y)=t-a-2$ if $s>0$.

Indeed $2y/q=2a+2s/q$, so $S=t+2a+\lfloor 2s/q\rfloor$,
$X_0=2a+\lceil 2s/q\rceil$, $Z_0=a+\lceil s/q\rceil$, giving
$N=t-a+\lfloor 2s/q\rfloor-\lceil 2s/q\rceil-\lceil s/q\rceil$.
If $s=0$ all corrections vanish. If $s>0$, $\lceil s/q\rceil=1$, and
since $q$ is odd, $2s/q$ is never an integer ($0<2s<2q$, $2s=q$
impossible), so $\lfloor\cdot\rfloor-\lceil\cdot\rceil=-1$, and
$N=t-a-2$. ∎

Now $0\le y\le qt$. Summing over $a$ ($j=t-a$):
- $s=0$ slices ($a=0..t$): $\sum_{j=0}^{t}\binom{j+2}{2}=\binom{t+3}{3}$;
- $s\in\{1,\dots,2k\}$ slices ($a=0..t-1$): $2k\sum_{j=1}^{t}\binom{j}{2}
  =2k\binom{t+1}{3}$ (with $\binom{1}{2}=0$),
by hockey-stick. Since $2k=q-1$,
$$L_k(t)=\binom{t+3}{3}+(q-1)\binom{t+1}{3},$$
expanding to the stated cubic. The coefficient claims follow directly.
$c_1(k)=(11-2k)/6$ decreases by $1/3$ per step of $k$, positive for
$k\le 5$, non-positive for $k\ge 6$: unique cutoff $K^*=6$. ∎

**Corollaries.** $L_k(1)=(q+6+12-q+6)/6=4$ for all $k$: only the four
vertices, so $W_k$ is empty (hole-free). The functional
$u=(0,0,1)$ takes values $0,0,1,1$ on the vertices, so width $\le 1$,
hence $=1$ (full-dimensional lattice polytope). The $h^*$-vector
$(1,0,q-1,0)$ follows from the Ehrhart-series identity
$\sum_{t\ge 0}L_k(t)z^t=(\sum h^*_iz^i)/(1-z)^4$, checked by the
convolution $L_k(t)-4L_k(t-1)+6L_k(t-2)-4L_k(t-3)+L_k(t-4)$
($=h^*_t$ for $t\le 3$, $0$ after; the 4th finite difference of a cubic
vanishes so checking $t\le 6$ suffices).

## Verification
`output/artifacts/verify_wk.py` (stdlib-only) replays from the committed
vertices: (i) facet-vs-barycentric membership agreement on 9900 test
points; (ii) brute-force box counts equal the closed form for $k=1..12$,
$t=0..4$; (iii) interior counts equal $-L_k(-t)$ (reciprocity);
(iv) the $N(y)$ lemma; (v) the $h^*$ convolution identity; (vi) $L_k(1)=4$
and width $1$. Output: ALL VERIFY_OK.

## Originality and scope
The new content is the closed-form linear coefficient, its strict
monotonicity, and the exact cutoff $K^*=6$ over this infinite White
congruence class — a sharp positivity/non-positivity boundary. The
derivation is elementary (slice counting + hockey-stick); no depth is
claimed for the method. Small-$k$ Ehrhart rows are standard computations
and serve only as cross-checks. No prior source states this cutoff
(see admission triage in inputs/topic.json).
