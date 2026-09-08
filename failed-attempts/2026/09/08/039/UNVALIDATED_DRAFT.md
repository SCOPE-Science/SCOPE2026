# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Vacuity of the Exoo–Janssen–Kolokolnikov–Salamon diameter bound for
4-regular diameter-2 graphs, with verified witness records

## 1. Background

Exoo, Janssen, Kolokolnikov, Salamon (arXiv:2307.07308), Theorem 1.2, bound the
algebraic connectivity (second Laplacian eigenvalue) of a $d$-regular graph of
diameter $D$ by

$$\mathrm{AC} \le d - 2\sqrt{d-1}\cos\theta,$$

where, for even diameter $D = 2K$, $\theta$ is the smallest positive root of

$$\tan(\theta K) = -\frac{d}{d-2}\tan\theta, \qquad (2)$$

with $\pi/(2K) < \theta K \le \pi$. Their Table 1 tabulates this bound for
diameters $D \ge 3$; no $D = 2$ row is tabulated, and no $4$-regular $D = 2$
attainability is decided there. For $d = 4$, $D = 2$ we have $K = 1$.

## 2. The $D = 2$ bound is always vacuous (proved)

**Theorem.** For connected $4$-regular graphs of diameter $2$, the Exoo et al.
diameter bound equals $B := 4 + 2\sqrt{3} \approx 7.4641$ and is never attained,
at any order $n$.

*Proof.* With $d = 4$, $K = 1$, equation (2) is
$\tan\theta = -2\tan\theta$, i.e. $3\tan\theta = 0$.
On the admissible interval $(\pi/2, \pi]$ (Lemma 2.1 of the paper: smallest
eigenvalue satisfies $\pi/2 < \theta K \le \pi$), the unique root is
$\theta = \pi$. Substituting,

$$B = 4 - 2\sqrt{3}\cos\pi = 4 + 2\sqrt{3} \approx 7.46410.$$

For any non-complete connected graph, Fiedler's bound
$a(G) \le n\delta/(n-1)$ (Fiedler, *Czechoslovak Math. J.* 23 (1973), 298–305)
applies with $\delta = 4$:

$$a(G) \le \frac{4n}{\,n-1\,} \le 5 \quad (n \ge 5),$$

since $4n/(n-1)$ decreases in $n$. Because $B = 4 + 2\sqrt{3} > 7.46 > 5 \ge
a(G)$ for every admissible $G$, equality $a(G) = B$ is impossible at every
order, including $n \in \{15,16,17\}$. ∎

**Corollary (quantified gaps at the Moore orders).** No connected 4-regular
diameter-2 graph attains the bound at $n = 15, 16, 17$, with gaps

| $n$ | gap $B - 4n/(n-1)$ |
|-----|--------------------|
| 15  | $\approx 3.1784$   |
| 16  | $\approx 3.1974$   |
| 17  | $\approx 3.2141$   |

(bound minus the Fiedler ceiling no graph can exceed; any graph's true gap is
at least this large).

*Remark.* This vacuity is strictly stronger than the planned Moore-defect
lemma (which would rule out only a subset of orders): it closes the entire
$n \in \{15,16,17\}$ attainability table negatively in one step, independent
of any exhaustive generation or of the Hoffman–Singleton nonexistence theorem.

## 3. Verified witness records (computed evidence, not needed for the proof)

All records below were verified by the accompanying script
`output/artifacts/verify.py` (stdlib + numpy 1.26.4 + sympy 1.12; diameter by
BFS, spectra by `numpy.linalg.eigvalsh`, exact polynomials by sympy):

- **Octahedron $K_{2,2,2}$** ($n = 6$): 4-regular, BFS diameter $2$,
  $\mathrm{AC} = 4.000000000000$, girth $3$,
  exact characteristic polynomial $\lambda^3(\lambda-4)(\lambda+2)^2$.
  Smallest 4-regular diameter-2 graph; attains the Fiedler ceiling
  $4n/(n-1) = 4.8$? No — attains $4 < 4.8$; it is the minimal-order witness,
  still $B - 4 \approx 3.4641$ below the Exoo bound.
- **$K_{4,4}$** ($n = 8$): 4-regular, BFS diameter $2$,
  $\mathrm{AC} = 4.000000000000$, girth $4$,
  exact characteristic polynomial $\lambda^6(\lambda-4)(\lambda+4)$.
- **Petersen graph** ($n = 10$, cubic girth-5 baseline in place of the
  un-recomputed 19-vertex Robertson cage): BFS diameter $2$,
  $\mathrm{AC} = 2.000000000000$, girth $5$, 3-regular.
- **Random 4-regular diameter-2 witness on $n = 15$** (seeded hill-climb;
  edge list in script output): BFS diameter $2$,
  $\mathrm{AC} \approx 2.2087121525$ (so true gap $B - \mathrm{AC} \approx
  5.2554$), girth $3$. Establishes the scope is non-empty of diameter-2
  graphs while the bound stays unattained.

The script additionally reproduces the published Table 1 values
$d = 4, D = 4 \to 2.0$ and $d = 4, D = 3 \to 3.0$ to 9+ decimals, validating
the formula implementation whose $K = 1$ degeneration gives the theorem.

## 4. What is NOT claimed

- No claim about $D \ge 3$ attainability (the paper's own territory).
- No Smith/interlacing structural lemma is claimed: a candidate argument
  (non-edge pair neighbourhood inducing $P_4$) was found to have an
  induced-subgraph gap and is recorded only as conjecture.
- The 16-vertex simulated-annealing run (residual 2 uncovered pairs after
  120k steps) is reported as heuristic evidence only and plays no role in
  the proof.
- The 19-vertex Robertson $(4,5)$-cage baseline was not re-verified in this
  run; the Petersen graph serves as the verified girth-5 baseline instead.

## 5. Reproduction

Run `python3 output/artifacts/verify.py` (requires numpy, sympy). Seeded RNG;
deterministic outputs listed in Section 3. The theorem itself is analytic and
needs no computation beyond the two-line derivation in Section 2.
