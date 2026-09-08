# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Minimal integer-point length-6 y-AP record on a Mordell curve, with rank lower bound and a certified no-length-7 integer envelope bound

## Theorem (fallback; proved by finite exact computation)
Let $E_k: y^2=x^3+k$ with $k\ne 0$ sixth-power-free. Then:

1. **Record.** For $k^*=197225 = 5^2\cdot 7^3\cdot 23$ the six points
   $$(70,\pm 735),\; (-14,\pm 441),\; (-56,\pm 147) \in E_{k^*}(\mathbb Q)$$
   are on the curve (exact integer check below) and their $y$-coordinates
   $$-735,\,-441,\,-147,\,147,\,441,\,735$$
   are distinct and form an arithmetic progression with difference $d=294\ne 0$.
2. **Rank.** $\operatorname{rank} E_{k^*}(\mathbb Q)\ge 2$.
3. **Envelope minimality / cutoff.** Inside the envelope
   $$\mathcal B = \{(x,y,k)\in\mathbb Z^3 : |x|\le 2000,\ |k|\le 2\,000\,000\},$$
   the tuple of (1) is, up to order/sign, the *unique* maximal integer-coordinate
   $6$-term $y$-AP on any $E_k$, and *no* integer-coordinate $7$-term $y$-AP occurs
   on any $E_k$ in $\mathcal B$. Both statements were verified by two
   independently coded exhaustive enumerations with identical results.

## Proof
**Record (exact arithmetic).**
$$735^2 = 540225 = 343000 + 197225 = 70^3 + k^*,$$
$$441^2 = 194481 = -2744 + 197225 = (-14)^3 + k^*,$$
$$147^2 = 21609 = -175616 + 197225 = (-56)^3 + k^*,$$
and the same with $y\mapsto -y$. Successive $y$-differences are all $294$.
$k^* = 5^2 7^3 23$ is nonzero with all prime exponents $<6$, hence sixth-power-free.
The three points $A=(70,735)$, $B=(-14,441)$, $C=(-56,147)$ are distinct modulo
$\pm$ and none has $y=0$, so all six listed points are distinct.

**Rank $\ge 2$.** $E_{k^*}$ has good reduction at $p=13$ ($13\nmid k^*$; discriminant
$\Delta=-27(2k^*)^2$). Direct counting gives $\#E(\mathbb F_{13})=19$ (prime) and
$\#E(\mathbb F_{19})=27$. Torsion $E(\mathbb Q)_{\mathrm{tors}}$ is trivial: reduction
mod $13$ is injective on prime-to-$13$ torsion, and neither $13$ nor $19$ can divide
$|E(\mathbb Q)_{\mathrm{tors}}|$ by Mazur's classification (no group of order
$13$ or $19$ occurs over $\mathbb Q$), so $|T|\mid 19$ forces $|T|=1$ (order $19$
is likewise excluded by Mazur).
At $p=19$, $|3E(\mathbb F_{19})|=3$ and the reductions
$\bar A=(5,7)$, $\bar B=(5,6)$ satisfy: the nine combinations $i\bar A+j\bar B$,
$0\le i,j\le 2$, occupy $9$ distinct cosets of $3E(\mathbb F_{19})$ (machine check
in `artifacts/verify_record.py`). If $\mathrm{rank}\le 1$ with trivial torsion,
$E(\mathbb Q)/3E(\mathbb Q)\cong(\mathbb Z/3)^r$ has order $\le 3$, so its image in
$E(\mathbb F_{19})/3E(\mathbb F_{19})$ would have at most $3$ cosets — contradiction.
Hence $r\ge 2$. (Stronger: $(\bar A,\bar B)$ are independent mod $3$ at $p=19$;
$(\bar A,\bar C)$ likewise; several further $(p,\ell)$ witnesses exist, e.g.
$\ell=5$ at $p=61$.)

**Envelope certificate.** Enumerate every integer triple in $\mathcal B$ by two
independent programs: (A) $x$-outer/$y$-inner grouping $y$-values by $k$; (B)
$x$-outer with $y$-range $[\lceil\sqrt{\max(0,x^3-K)}\rceil,\lfloor\sqrt{x^3+K}\rfloor]$
in both signs. Both found $499{,}256$ values of $k$ with at least one integer point,
exactly one maximal $6$-term integer-$y$ AP (the record above), and zero $7$-term
integer-$y$ APs. Loop bounds provably cover every integer point with
$|x|\le 2000$, $|k|\le K$ since $y^2=x^3+k\le |x|^3+K$. Minimality is by
$\max|y|$ ($735$); it is the only maximal length-$6$ occurrence, hence a fortiori
minimal.

## Replay
`python3 artifacts/verify_record.py` (stdlib only, seconds) checks R1–R5:
factorisation of $k^*$, six on-curve identities, AP property, the counts
$\#E(\mathbb F_{13})=19$, $\#E(\mathbb F_{19})=27$, and the nine mod-$19$
$3$-quotient cosets. It prints `VERIFY_OK`.

## What is NOT claimed
- No length-$7$ $y$-AP witness (integral or rational) is exhibited; the July-2026
  paper's "length $7$ open" status for rational points is unchanged.
- Minimality/uniqueness is inside the integer-coordinate envelope $\mathcal B$,
  not over all of $\mathbb Q$; rational points with non-integral coordinates are
  outside this certificate.
- Rank is a lower bound ($\ge 2$), not the exact rank; no regulator, generators
  completeness, or BSD claim is made.
- Length-$6$ infinite families are prior art (Lee–Velez; Dey–Maji; Theorem 2.4 of
  arXiv:2607.06998); the novelty here is the certified minimal integer record,
  the machine-checked rank witness, and the exhaustive integer envelope cutoff,
  none of which appear in that paper.

## Prior art (separation)
arXiv:2607.06998 gives parametric length-$6$ families with no minimality or
envelope-exhaustion claim; arXiv:1910.14485 (AP-forces-rank) and arXiv:1806.01158
(consecutive-cube $x$-patterns) neither construct nor imply this tuple; LMFDB has
no AP-pattern field. The integer tuple above is used as a seed-free direct record.
