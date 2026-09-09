# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# A certified primitive expanding train-track map on the 4-rose with enclosed stretch factor and gate/turn data

## Statement (fallback lemma; self-contained)

Let $F_4=\langle a,b,c,d\rangle$ and let $\phi\in\mathrm{End}(F_4)$ be defined on generators by

$$\phi(a)=bad,\quad \phi(b)=cd,\quad \phi(c)=ad,\quad \phi(d)=db.$$

Then:

1. **Automorphism.** $\phi$ is an automorphism of $F_4$ (it is the composition of four
   Nielsen transvections and one permutation; explicit history below).
2. **Positive train-track map.** $\phi$ is represented by a positive graph map on the 4-rose
   (all images positive words of length 2-3), hence a train-track map with no cancellation.
3. **Primitive/expanding.** Its transition matrix (rows/columns ordered $a,b,c,d$)
   $$M=\begin{pmatrix}1&0&1&0\\1&0&0&1\\0&1&0&0\\1&1&1&1\end{pmatrix}$$
   satisfies $\det M=+1$ and
   $$M^3=\begin{pmatrix}2&1&1&1\\4&3&3&2\\2&1&2&1\\7&4&5&4\end{pmatrix}>0,$$
   so $M$ is primitive (Perron-Frobenius irreducible and aperiodic); the map is expanding
   (all column sums $\ge 2$).
4. **Stretch factor.** The characteristic polynomial is exactly
   $$p(x)=x^4-2x^3-x+1,$$
   irreducible over $\mathbb{Q}$ (no rational root; checked $\pm 1$ fail).
   Its Perron-Frobenius eigenvalue satisfies
   $$2.117 < \lambda(M) < 2.118$$
   (since $p(2.117)<0<p(2.118)$ and $p'>0$ on the interval, so exactly one simple root lies
   there; the PF root is the unique root $>1$... see §Uncertainty for the precise scope).
   A Collatz-Wielandt certificate with the positive rational vector
   $v=(11769/100000,\ 1741/6250,\ 6577/50000,\ 47221/100000)$ gives
   $Mv/v\in[2.117676\ldots,2.117701\ldots]$.
5. **Gate/turn structure (proved direction data).** With directions
   $0,1,2,3=a,b,c,d$ and $4,5,6,7=\bar a,\bar b,\bar c,\bar d$, the derivative is
   $$D:\ 0\mapsto1,\ 1\mapsto2,\ 2\mapsto0,\ 3\mapsto3,\qquad
     4,5,6\mapsto7,\ 7\mapsto5.$$
   Hence there are 6 gates: $\{0\},\{1\},\{2\},\{3\},\{7\},\{4,5,6\}$.
   Illegal turns are exactly $(4,5),(4,6),(5,6)$.
   The turns taken by the edge images are
   $$\{(0,5),(1,7),(3,4),(3,6)\},$$
   which contains **no illegal turn**. The $D$-orbit closure of the taken turns has 10
   (unordered) turns and is connected as a graph on the 8 directions.
6. **Abelian atoroidality screen.** $\gcd(p,x^k-1)=1$ for $1\le k\le 12$ (exact Euclidean
   algorithm), so no eigenvalue of the abelianization is a root of unity of order $\le 12$.

## Proofs (replayable from the strings alone)

- (1): replay the history on $[a],[b],[c],[d]$: $a\mapsto ac$; $d\mapsto da$;
  $c\mapsto cd$ (giving $[acd],[bd],[cd],[da]$ after $b\mapsto bd$); then apply the
  permutation $a\mapsto b,b\mapsto c,c\mapsto a,d\mapsto d$ to get $[bad],[cd],[ad],[db]$.
  Each step is a Nielsen move, hence an automorphism. (`verify.py` replays this.)
- (2): inspection of the four words.
- (3): integer matrix multiplication gives $M^3$ above; all 16 entries $\ge 1$.
- (4): exact permutation-expansion of $\det(xI-M)$ gives $p$; $p(2.117)=-0.1739\ldots<0$,
  $p(2.118)>0$ as exact fractions; $p''(x)=12x(x-1)>0$ for $x>1$ so $p'$ is increasing and
  $p'(2.117)>0$, hence exactly one root in the interval. CW bounds are exact fractions.
- (5): first letters $(b,c,a,d)$, last letters $(d,d,d,b)$ give $D$; the rest is finite-set
  computation, all asserted equalities checked in `verify.py`.
- (6): exact polynomial gcd over $\mathbb{Q}$ (Fraction arithmetic, no floats).

## What is NOT proved (uncertainty, explicitly)

- **Full irreducibility (iwip):** primitivity + connected local Whitehead graph is the
  standard Bestvina-Handel input for full irreducibility, but the complete folding/Whitehead
  argument is quoted, not re-proved here. The certificate supplies exactly the verified
  input to that theorem.
- **PNP-free / ageometric status:** only the proved fragment "no taken illegal turn" (hence
  no period-1 indivisible Nielsen path using a taken illegal turn) is certified. A complete
  Pfaff PNP test and the 7-vertex ideal Whitehead graph computation are NOT included.
- **Atoroidality:** only the abelian screen (6) is proved; full atoroidality (no periodic
  conjugacy class) is NOT proved.
- **Minimality:** $\lambda\approx2.1177$ is logged, not claimed minimal in any stratum.

## Replay

Run `python3 output/artifacts/verify.py` (stdlib only) — expect `VERIFY_OK`.

## Data summary

- Images: `bad, cd, ad, db`; history: transvections $(a\!\to\!ac),(d\!\to\!da),(c\!\to\!cd),
  $(b\!\to\!bd)$, perm $(1,2,0,3)$.
- $M$, $M^3$, $p(x)=x^4-2x^3-x+1$, $\lambda\in(2.117,2.118)$.
- Spectrum (exploratory, sympy `nroots`, not part of certificate):
  $2.11768$, $0.64145$, $-0.37957\pm0.76948i$; disc $-643$.
