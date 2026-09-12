# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# X9 canonical isotropic: Seifert divisibility is 1, not 2 — target falsified; monodromy acts trivially on the radical

## 1. Setup (fixed before computation)
- X9 is $f(x,y)=x^4+y^4$, $\mu=9$. Stabilize by $+z^2$ for the symmetric $H_2$ picture.
- Distinguished tensor basis $e_{ij}= \Delta^1_i\otimes\Delta^2_j$ ($i,j=1,2,3$), ordered
  $(11,12,13,21,22,23,31,32,33)$.
- $A_3$ Seifert block (one variable, AGV/Ebeling convention): $U_3=[[-1,1,0],[0,-1,1],[0,0,-1]]$.
- X9 Seifert: $L=U_3\otimes U_3$ (Sebastiani–Thom; cf. AGV vol. II, Ebeling 1985).
  Symmetric Gabrielov form $S=-L-L^T$. Monodromy/reflection group $\Gamma=\langle s_1,\dots,s_9\rangle$
  with Picard–Lefschetz $s_i(v)=v+S(v,e_i)e_i$; each $s_i$ preserves $L$ and $S$.
- Seifert divisibility: $d(u)=\gcd\{L(u,x):x\in M\}=\gcd$ of entries of the covector $u^TL$
  (equivalently $L^Tu$ up to transpose convention).

## 2. Radical (exact)
$L$ is unimodular ($\det L=+1$, machine-checked by fraction-free elimination).
$S$ has rank 7, nullity 2. Two independent kernel vectors:
$$w_0=(0,1,1,1,2,1,1,1,0),\qquad w_1=(-1,-2,-1,-2,-2,0,-1,0,1),$$
with $Sw_0=Sw_1=0$ (exact), $L(w_0,w_0)=L(w_1,w_1)=0$ (isotropic), content $\gcd=1$ each.
The $9\times 2$ matrix $[w_0\mid w_1]$ has entry-gcd $1$ and $2\times2$-minor-gcd $1$,
so invariant factors $(1,1)$: $\mathbb{Z}w_0+\mathbb{Z}w_1$ is saturated.
Since the radical $R=\ker(S)$ is saturated (kernel of an integral map) and
$\ker(S)\otimes\mathbb{Q}=\mathbb{Q}w_0+\mathbb{Q}w_1$ (checked by exhibiting every rational
nullvector as a combination), $R=\mathbb{Z}w_0\oplus\mathbb{Z}w_1$.

## 3. Divisibility = 1 (exact covectors)
$$L^Tw_0=(0,1,0,1,0,-1,0,-1,0),\quad \gcd=1,$$
$$L^Tw_1=(-1,-1,1,-1,1,1,1,1,-1),\quad \gcd=1.$$
Row convention $Lw_0=(0,-1,0,-1,0,1,0,1,0)$ also has gcd 1. Hence $d(w_0)=d(w_1)=1$, not 2.

## 4. Universal lemma (covers every admissible canonical $u_0$)
For $v=aw_0+bw_1$ the covector is exactly
$$L^Tv=(-b,\ a-b,\ b,\ a-b,\ b,\ b-a,\ b,\ b-a,\ -b).$$
Any common divisor of the entries divides $(a-b)+b=a$ and $b$, hence divides $\gcd(a,b)$.
So every primitive radical vector ($\gcd(a,b)=1$) — whichever one the
"longest-root-plus-extra" construction names as $u_0$ — has divisibility exactly 1.
No primitive isotropic in $R$ has divisibility 2. Verified symbolically and on the grid
$a,b\in[-5,5]$ by `verify_x9.py`.

## 5. Convention-independence
Any valid distinguished Seifert matrix is $L'=P^TLP$ with $P$ unimodular; the same lattice
vector has covector $u^TLP$, right-multiplication by $P$ preserving entry-gcds.
Sign/transpose/row-vs-column conventions likewise preserve gcds. So $d=1$ is intrinsic,
not an artefact of our basis.

## 6. Orbit analysis (reflection/monodromy group)
Since $w_0,w_1\in\ker S$, $S(v,e_i)=0$ for every $v\in R$, so every generator
$s_i(v)=v+S(v,e_i)e_i$ fixes $R$ pointwise. Hence $\Gamma$ acts trivially on $R$:
$\Gamma$-orbits on $R$ are singletons. In particular no $g\in\Gamma$ sends $w_0$ to $w_1$
(distinct singletons), and the negative-polarity transporter does not exist in $\Gamma$.
A bounded BFS to depth 6 from $w_0$ confirms the orbit is $\{w_0\}$ (only fixed-point
reflections, frontier empty).

## 7. Verdict on the target
The target conjunction — "$u_0$ has divisibility 2 AND lies in a distinct monodromy orbit
from $u_1$" — is FALSE: the divisibility clause fails (it is 1) for every primitive
choice of $u_0$. The orbit-separation clause alone is true but trivially so (singleton
orbits). Neither admitted polarity holds as stated: the positive polarity's $d=2$ is wrong,
and the negative polarity's transporter in $\Gamma$ is impossible. Corrected theorem:
every primitive $v\in R$ has Seifert divisibility 1, and $\Gamma$ fixes $R$ pointwise.

## 8. Replay
`python3 output/artifacts/verify_x9.py` → `VERIFY_OK` (stdlib only, 19 checks).
