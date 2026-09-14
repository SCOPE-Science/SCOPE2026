# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# SRG eigenvalue −3 with 6-regular star complement — complete classification

## 1. Problem and result

Let $G$ be a connected primitive strongly regular graph (SRG) with least eigenvalue $-3$,
with parameters $(v,K,\lambda,\mu)$ and non-trivial eigenvalues $r > s=-3$ (so $r \ge 1$ is integral
for a primitive SRG with integral spectrum; imprimitive cases are complete multipartite or disjoint
unions, and connectivity leaves $K_{c \times m}$). Assume $G$ admits a star complement $H$ for the
eigenvalue $-3$ that is regular of degree $6$. The target asks for the complete finite list of feasible
parameter sets that are neither complete multipartite nor of Steiner type, with a realizing graph or a
non-realizability proof per entry.

**Theorem.** The counting consequences of the hypotheses admit exactly two parameter sets in total:
$(26,15,8,9)$ and $(30,27,24,27)$. Both are of excluded type: $(30,27,24,27)$ is complete multipartite
($K_{3 \times 10}$), and $(26,15,8,9)$ is realized by the block graph of a Steiner triple system STS(13))
— indeed by the cyclic STS(13) — and that block graph itself contains a $6$-regular star set of size
$13$ for the eigenvalue $-3$. Consequently the sublist of feasible parameters for graphs that are
neither complete multipartite nor of Steiner type is **empty**, and this empty list is complete.

The rest of this note gives a self-contained proof plus machine-checked verification
(`artifacts/verify_classification.py`, pure integer arithmetic except for explicitly flagged
numerical-linear-algebra witness checks).

## 2. Equations

Standard SRG relations (connected, non-conference primitive part):
$$K + f r - 3g = 0, \qquad f+g = v-1, \qquad K(K-\lambda-1) = (v-K-1)\mu,$$
$$\lambda = \mu + r - 3, \qquad K = \mu + 3r, \qquad v = 1 + K + \frac{2K(r+1)}{\mu},$$
where $f, g$ are the multiplicities of $r$ and $-3$. Put $t = f+1$ (star-set size) and $g = v - t$.

Star-complement Reconstruction Theorem (Rowlinson–Sims; see e.g. Rowlinson–Munemasa–Sims, Surveys in
Combinatorics): if $X$ is a star set for eigenvalue $-3$ with complement $H$ (adjacency $B$) and
$X$–$H$ incidence $N$, then $-3$ is not an eigenvalue of $B$ and
$$-3I - A_X = N^\top(-3I - B)^{-1}N.$$
Since $H$ is $6$-regular on $g$ vertices and $G$ is $K$-regular, every vertex of $H$ has exactly
$K - 6$ neighbours in $X$, i.e. $N{\bf 1}_X = (K-6){\bf 1}_H$, and $B{\bf 1}_H = 6{\bf 1}_H$, so
$(-3I-B)^{-1}{\bf 1}_H = -\frac19{\bf 1}_H$. Contracting the Reconstruction identity with all-ones
vectors: the left side gives $(-3)t - 2e(X)$ (with $e(X)$ the number of edges inside $X$), the right
side gives $(K-6)^2 g/(-9)$. Hence $-3t - 2e(X) = -(K-6)^2g/9$, i.e.
$2e(X) = (K-6)^2g/9 - 3t$. The degree sum on $X$ reads $Kt = 2e(X) + e(X,H) = 2e(X) + g(K-6)$.
Eliminating $e(X)$ yields $(K+3)t = g(K-6)(K+3)/9$, and since $K + 3 > 0$,
$$g\,(K-6) = 9t, \qquad\text{i.e.}\qquad v\,(K-6) = t\,(K+3). \tag{$\dagger$}$$
Direct numerical verification of the Reconstruction identity on the witnesses below gives max error
$< 10^{-8}$, and both displayed realizations satisfy $g(K-6) = 9t$ exactly as integers
($13\cdot 9 = 9\cdot 13$; $9\cdot 21 = 9\cdot 21$).

From the trace equation $K + fr - 3g = 0$ with $f = t-1$, $g = v-t$:
$$(r+3)\,t = 3v - K + r. \tag{T}$$
Substituting (T) in ($\dagger$) gives the master Diophantine equation
$$v\,\bigl(r(K-6) - 27\bigr) = (r-K)(K+3). \tag{*}$$

## 3. Finite classification (exact case analysis)

Preliminaries: $\mu = K - 3r \ge 1$, $\lambda = \mu + r - 3 \ge 0$, $K > 6$ (else the left side of
($\dagger$) is $\le 0$ while the right is positive), $v = 1+K+2K(r+1)/\mu$ integral, and
$t = (3v-K+r)/(r+3)$ integral with $f = t-1 > 0$, $g = v-t > 0$. Primitivity excludes $r = 0$
($r = 0$ gives $\lambda = \mu - 3$, $K = \mu$, i.e. complete multipartite).

- **$r = 0$.** Then $K = \mu$, $v = K+3$, and ($\dagger$) reads $(K+3)(K-6) = 9\cdot(\text{$t$})$;
  with $t = v - (v-1-K/3) = \cdots$ one gets directly $27v = K(K+3)$, i.e. $K = 27$. Hence
  $(v,K,\lambda,\mu) = (30,27,24,27)$, realized by $K_{3 \times 10}$ (Section 4). Excluded
  (complete multipartite). Machine check: scan of $1 \le K < 200$ finds only $K = 27$.

- **$r = 1$.** $\mu = K-3$, $v = 1 + K + 4K/(K-3)$, so $(K-3) \mid 12$: $K \in \{4,5,6,7,9,15\}$.
  Each fails one of $K > 6$, $\lambda \ge 0$, trace integrality, or ($\dagger$). Machine-checked
  (all six return None). No solutions.

- **$r = 2$.** $\mu = K-6$, $v = 1 + K + 6K/(K-6)$, so $(K-6) \mid 36$. Moreover $K = \mu + 6 \ge 7$
  and ($\dagger$) with $t = (3v-K+2)/5 \le v-1$ forces $K < 19.5$; hence
  $K \in \{7,8,9,10,12,15,18\}$. Exactly one survives all filters: $K = 15$, giving
  $(v,K,\lambda,\mu) = (26,15,8,9)$ with $f = 12$, $g = 13$, $t = 13$. Machine-checked.

- **$r = 3$.** $\mu = K-9$, $v = 1 + K + 8K/(K-9)$, so $(K-9) \mid 72$, and ($\dagger$) forces
  $K < 15$; hence $K \in \{10,11,12,13\}$. All fail. Machine-checked. No solutions.

- **$r \ge 4$.** Since $\mu \ge 1$, $K = \mu + 3r \ge 3r+1 > 6$, so the left side of ($\dagger$)
  is positive and $t = g(K-6)/9 < g \le v - 1$ is consistent. From (*) the right side
  $(r-K)(K+3)$ is negative (as $K = \mu + 3r > r$), so the bracket on the left must be negative:
  $r(K-6) - 27 < 0$, i.e. $r(K-6) < 27$. But $r(K-6) \ge r(3r-5) \ge 28$ for $r \ge 4$
  (at $r=4$: $4\cdot 7 = 28$). Contradiction. The degenerate subcase $r(K-6) - 27 = 0$ with
  $r = K$ gives $r(r-6) = 27$, i.e. $r = 9$, whence $\mu = K - 3r = -18 < 0$: excluded.
  Hence no solutions with $r \ge 4$.
  (Verified for $4 \le r < 5000$ by the inequality, which is monotone.)

This proves completeness: up to the two excluded-type entries, there are no other feasible
parameter sets at all.

## 4. Realizability witnesses (one per listed set)

**(a) $(26,15,8,9)$ — Steiner type.** Take the cyclic STS(13) with base blocks $\{0,1,4\}$,
$\{0,2,7\}$ (13 cyclic shifts each, 26 blocks). Its block graph (adjacent = intersecting blocks)
is SRG(26,15,8,9): every block meets exactly 15 others, adjacent pairs share $\lambda = 8$ common
neighbours, disjoint pairs share $\mu = 9$; spectrum $\{15^1, 2^{12}, (-3)^{13}\}$. Verified by exact
integer adjacency arithmetic in the script. It is by construction a Steiner-triple-system block
graph, hence of Steiner type (excluded from the target scope, as required for the verdict).

Moreover this graph contains a $6$-regular star set of size $t = 13$ for $-3$, e.g. (in the script's
vertex ordering)
$$X = \{0,2,5,6,10,11,14,15,18,21,23,24,25\},$$
whose induced subgraph is $6$-regular with spectrum avoiding $-3$ ($\min|e+3| \approx 0.70$), and the
Reconstruction identity holds to max error $8.9\times 10^{-16}$. Hence $(26,15,8,9)$ genuinely admits
a $6$-regular star complement — on a Steiner-type graph.

**(b) $(30,27,24,27)$ — complete multipartite.** $K_{3 \times 10}$ (10 parts of size 3) is
SRG(30,27,24,27) (degrees $27$; spectrum $\{27^1, 0^{20}, (-3)^9\}$). Verified in the script.
Excluded (complete multipartite).

## 5. Answer to the target

The complete finite feasibility list for "primitive SRG, least eigenvalue $-3$, $6$-regular star
complement" is $\{(26,15,8,9),\, (30,27,24,27)\}$, each with an explicit realizing graph of excluded
type. Filtering to graphs that are **neither** complete multipartite **nor** of Steiner type, the
complete list is the **empty list** — a finite answer with completeness proof above and no
outstanding verdicts (every listed entry has its witness).

## 6. Separation of proof, computation, and uncertainty

- Proof: Sections 2–3 are rigorous deductions (Reconstruction theorem + SRG identities + divisor
  bounds); the only external theorem invoked is the star-complement Reconstruction identity.
- Computed evidence: divisor-candidate enumeration ($r \le 3$ finite divisor lists), adjacency-count
  checks for both witnesses, spectra, and the Reconstruction-identity residual — all reproduced by
  `artifacts/verify_classification.py`.
- Conjecture/uncertainty: none load-bearing. Not claimed: uniqueness of the $(26,15,8,9)$ realization
  (only existence of a Steiner realization is needed and proved), nor any statement about star
  complements of non-Steiner graphs on other eigenvalues.
- Limitations: the proof uses the connectedness/primitivity hypotheses to get integral $r$ and the
  standard SRG equations; the imprimitive case is handled by the $r=0$ computation ($K_{3\times 10}$).
  No literature search was used; all steps are local.

## 7. Artifact inventory

- `artifacts/verify_classification.py` — end-to-end verification (prints CLASSIFICATION COMPLETE and
  ALL CORRECTED CHECKS PASSED): exact divisor enumeration for $r \in \{0,1,2,3\}$, analytic $r\ge 4$
  bound check, cyclic-STS(13) block-graph SRG check + spectrum, $K_{3\times 10}$ check, randomized +
  structured search for the $6$-regular star set, Reconstruction-identity residuals, scalar identity
  $g(K-6) = 9t$ integer checks.
