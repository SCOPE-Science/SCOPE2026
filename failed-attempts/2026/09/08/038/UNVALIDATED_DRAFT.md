# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified finite-word trace-minimum census over a Bolza-value Fricke window

## Claim (fallback-level; proved by exact computation + rigorous intervals)

Fix **Fricke–Vogt coordinates** $(x,y,z)=(\operatorname{tr}A,\operatorname{tr}B,\operatorname{tr}AB)$
on the $\mathrm{SL}(2)$-character variety $X(F_2)$ (no polynomial relation; every
triple occurs). Let

$$B=\left[\tfrac{13}{3},\tfrac{16}{3}\right]^3,\qquad
c_0=\tfrac{29}{6}\approx 4.8333,\quad |c_0-(2+2\sqrt2)|<0.005,$$

so the box centre is within $0.005$ of the **Bolza systole trace value**
$T=2+2\sqrt2\approx 4.8284$ (which gives $2\,\mathrm{arccosh}(T/2)\approx 3.057$,
the Bolza systole; cf. Fortier Bourque–Rafi, arXiv:1807.08367).

Let $W_8$ be the set of **all reduced words** in $F(a,b)$ of length $\le 8$
($\sum_{k=1}^8 4\cdot 3^{k-1} = 13\,120$ words). For $p=(x,y,z)$ define the
**finite-word trace minimum** $m(p)=\min_{w\in W_8}|\operatorname{tr}\rho_p(w)|$
and $\ell(p)=2\,\mathrm{arccosh}(m(p)/2)$.

**Theorem (census).** Over the $5\times5\times5$ rational grid
$G=\{c_0+k/4: k=-2,\dots,2\}^3\subset B$ (125 points) plus a $3\times3\times3$
half-step refinement around the grid maximum clipped to $B$ (7 new points,
132 rows total), the following hold, each row certified by exact rational
arithmetic plus rigorous $\cosh$/$\sinh$ Taylor interval bounds:

1. **Grid maximum** at $(16/3,16/3,16/3)$: min word `a`, trace $16/3$,
   $$\ell \in [3.273612035\ldots,\,3.273614036\ldots]\quad
     (\text{mid } 3.273613036,\ \text{width }2\times10^{-6}).$$
2. **Grid minimum** at $(13/3,13/3,13/3)$: min word `a`, trace $13/3$,
   $$\ell \in [2.816482703\ldots,\,2.816484703\ldots]\quad
     (\text{mid } 2.816483703,\ \text{width }2\times10^{-6}).$$
3. **Certified extremal gap**: $\min$ grid-max lower bound minus grid-min
   upper bound is $\ge 0.457127332\ldots > 0.15$ (exceeds the admission
   $\delta\ge 0.15$ bar threefold).
4. **Window sup bound for the word proxy**: for every $p\in B$,
   $\ell(p)\le 2\,\mathrm{arccosh}(B_{\max}/2)\le U=3.273614036$
   (since $m(p)\le\min(x,y,|z|)\le 16/3$ and $L$ is increasing); the bound is
   sharp at the box corner.
5. Every row also carries a certified **collar width**
   $w=\mathrm{arcsinh}(1/\sinh(\ell/2))$ interval (collar lemma quantity).

## Method (exact, stdlib-only; self-checking lift)

For each rational $(x,y,z)$ with $z^2>4$, explicit lift to $\mathrm{SL}(2)$ over
$R=\mathbb{Q}(\sqrt{D})$, $D=z^2-4$:

$$A=\begin{pmatrix}0&-1\\1&x\end{pmatrix},\qquad
  B=\begin{pmatrix}y&z+c\\c&0\end{pmatrix},\quad
  c=\frac{-z+s}{2},\ s^2=D.$$

Then $\det A=1$; $\det B=-c(z+c)=1$ because $c^2+zc+1=(D-z^2)/4+1=0$;
$\operatorname{tr}A=x$, $\operatorname{tr}B=y$,
$\operatorname{tr}AB=z$ (since $AB=\bigl(\begin{smallmatrix}-c&0\\y+xc&z+c\end{smallmatrix}\bigr)$).
All four facts are **asserted exactly** at every grid point (both branches).
Every word trace is an element of $R$ whose $\sqrt{D}$-part **must vanish**
(it equals the Fricke integer trace polynomial at $(x,y,z)$); this is asserted
for **all 13,120 words at all 132 points** ($1.73\times10^6$ exact checks) —
the lift is self-verifying. Word enumeration is BFS over reduced words
($4,12,36,\dots$ per length; total asserted $=13\,120$ per point, logged in
column `nchecked`).

Length/collar intervals: $N=20$ cosh/sinh Taylor partial sums with Lagrange
remainder $t_{N+1}/(1-r)$ in exact `Fraction` arithmetic; bisection-free
adaptive widening from a float estimate. All interval widths $\le 2.1\times10^{-6}$.

## Scope delimitations (explicit; not overclaimed)

- The census certifies the **finite-word proxy** $m(p)$ over words of length
  $\le 8$, **not** the full infinite-word systole. It is therefore the
  admission-approved **fallback census** (reusable length-spectrum benchmark
  table), not the target window-best bound $U(B)$ with $U-L^\*\le 0.05$.
- $(x,y,z)$ parametrize $X(F_2)$ (one-holed-torus / rank-2 character variety),
  used here as **Fricke trace coordinates of a Bolza-value window**; no claim
  is made that every point is a closed genus-2 surface holonomy
  (that would require the genus-2 trace relations). The gap, intervals, and
  replay logs are statements about certified trace-length data over $B$.
- Within this window the length-$\le 8$ minima are all attained at words of
  length 1–2 (column `wlen` $\in\{1,2\}$), with runner-up words and traces
  logged per row (`run_word`, `run_trace`); longer words never beat the
  minimum on $G$ — a genuine empirical finding of the census, re-provable from
  `table.csv` + `verify.py`.

## Reproduction

```
python3 output/artifacts/census.py output/artifacts   # ~60 s, regenerates table.csv + summary.json
python3 output/artifacts/verify.py output/artifacts   # replays 132/132 word traces + intervals;
                                                      # exhaustive 13,120-word minimality re-proof at 12 sampled points
```

Artifacts: `output/artifacts/table.csv` (132 rows, 18 columns),
`output/artifacts/summary.json` (box, argmax/argmin, gap, $U$, timings),
`output/artifacts/census.py`, `output/artifacts/verify.py`
(both vendored; stdlib only; verifier passed: 132/132 traces + intervals,
12/12 exhaustive minimality spot-checks, gap $\ge 0.457 > 0.15$).
