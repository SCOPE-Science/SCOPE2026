# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Disproof of the claimed 7-point census for C1: y^2 = x^5 - 2x^3 + x + 1

## Statement
Let $C_1/\mathbf{Q}$ be the projective smooth model of the affine curve
$y^2 = f(x) = x^5 - 2x^3 + x + 1$ (plus one point $\infty$ at infinity).
The target claim that
$$C_1(\mathbf{Q}) = \{\infty,(0,\pm 1),(1,\pm 1),(-1,\pm 1)\}$$
is **false**. In fact $C_1(\mathbf{Q})$ contains at least the further distinct
rational points
$$(7,\pm 127),\qquad (17/16,\pm 1033/1024).$$

## Proof
$f(x)=x^5-2x^3+x+1$ has discriminant $\mathrm{Res}(f,f')=2869=19\cdot 151\ne 0$
(computed by exact Bareiss determinant of the $9\times 9$ Sylvester matrix of
$f=x^5-2x^3+x+1$, $f'=5x^4-6x^2+1$), so $f$ is separable and $C_1$ is a smooth
genus-$2$ curve; the displayed points below are therefore well-defined rational
points wherever the equation holds.

(a) $(7,\pm 127) \in C_1(\mathbf{Q})$.
Indeed $7^5 = 16807$, $2\cdot 7^3 = 686$, and
$$f(7) = 16807 - 686 + 7 + 1 = 16129 = 127^2,$$
verified by exact integer arithmetic ($127^2 = 16129$). Hence
$(\pm 127)^2 = f(7)$.

(b) $(17/16,\pm 1033/1024) \in C_1(\mathbf{Q})$.
Write $x=a/b$ with $a=17$, $b=16$. Then
$$f(a/b) = \frac{N(a,b)}{b^5},\quad
N(a,b) = a^5 - 2a^3b^2 + ab^4 + b^5.$$
Exact integer arithmetic gives
$$N(17,16) = 1419857 - 2\cdot 4913\cdot 256 + 17\cdot 65536 + 1048576
= 1067089 = 1033^2,$$
$$b^5 = 16^5 = 1048576 = 1024^2.$$
Hence $f(17/16) = 1033^2/1024^2 = (1033/1024)^2$, so
$(\pm 1033/1024)^2 = f(17/16)$.

(c) These points are new.
The $x$-coordinates $7$ and $17/16$ are not in $\{0,1,-1\}$, so none of the four
new points coincides with any of the six claimed affine points; they are affine
($y\ne 0$ gives distinct $\pm$ pairs) and distinct from $\infty$. Thus
$C_1(\mathbf{Q})$ strictly contains the claimed $7$-element set.

## Remarks
- This refutes the target equality outright; no statement is made here about the
  full (larger) set $C_1(\mathbf{Q})$, the Jacobian rank, or the $p=5$ Coleman /
  $29$,$43$ sieve apparatus, none of which is needed for the disproof.
- Every identity above uses only exact integer arithmetic and is replayed by
  `output/artifacts/verify.py` (stdlib only), which prints `VERIFY_OK`.

## Replay
```
python3 output/artifacts/verify.py   # -> VERIFY_OK
```
