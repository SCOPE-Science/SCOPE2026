# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified short-mixed-sum envelopes on five prime-power moduli

## 1. Statement

Let $q=p^m$ ($p$ odd prime), $\chi$ a Dirichlet character mod $q$,
$e_q(t)=\exp(2\pi i t/q)$, and for integers $M,N\ge 1$, $a\bmod q$,

$$S(M,N;a,\chi,q)=\sum_{\substack{M<n\le M+N\\(n,q)=1}}\chi(n)\,e_q(an).$$

For $N\ge 1$ put the Burgess-shape ratio

$$R(M,N;a,\chi,q)=\frac{|S(M,N;a,\chi,q)|}{N^{1/2}\,q^{3/16}\log q}.$$

**Theorem (certified finite envelope; verified computation).**
For each $q\in\{9,25,27,49,121\}$, the exact maximum of $R$ over all
primitive $\chi\bmod q$, all $a\bmod q$, all $M\bmod q$, and all
$1\le N\le q$ is:

| $q$ | $\max R$ | argmax $(j,a,M,N)$ | $|S|$ at argmax |
|-----|----------|--------------------|-----------------|
| 9   | 0.4505560523783483 | (4,4,4,7)    | 3.9545108072573854 |
| 25  | 0.3293580374213483 | (8,23,2,17)  | 7.993016354745021 |
| 27  | 0.2760840231329556 | (16,9,13,9)  | 5.06417777247592 |
| 49  | 0.27601891969144815 | (4,14,30,10) | 7.046985787472473 |
| 121 | 0.2152686026952103 | (4,102,63,40) | 16.046974098322146 |

Here $j$ indexes the character $\chi_j(n)=\exp(2\pi i j\,\mathrm{ind}_g(n)/\varphi(q))$
with $g$ the certified generator below. In particular, on these five moduli,

$$|S(M,N;a,\chi,q)|\le 0.451\,N^{1/2}q^{3/16}\log q$$

for every primitive $\chi$, every $a,M$, and every $1\le N\le q$.
The constant $0.451$ is best possible for this five-modulus family and shape
(it is attained up to rounding at $q=9$).

Certified generators and counts used:
$(q,g,\varphi(q),\#\text{primitive})$ =
$(9,2,6,4)$, $(25,2,20,16)$, $(27,2,18,12)$, $(49,3,42,36)$, $(121,2,110,100)$.
Independent direct-summation recomputation of each argmax agrees with the
envelope value to better than $7\times 10^{-14}$ (see §3).

## 2. What is and is not claimed

*Proved (machine-verified exact enumeration):* the table above. Every
quantifier is exhausted: all primitive characters, all $a$, all $M$, all
$N\le q$. No sampling, no heuristic search, no floating-point optimization
over a continuum — the domain is finite and fully enumerated.
*Computed evidence:* per-$N$ envelope files
`output/artifacts/envelope_q{q}.csv` giving $\max_{M,a,\chi}|S|$ at each $N$.
*Not claimed:* the lane's original analytic target (twist-uniform Burgess
bound with $C_2\le 2.2$ for all $q>2\times 10^5$, exhaustion to $Q_0=2\times
10^5$, $\ge 15\%$ improvement over evaluated Trevino/Jain–Sharma constants,
crossover atlas) is **not** proved here. No analytic Burgess lemma, no
Cochrane–Granville-moment argument, and no evaluated-constant comparison are
offered. The constant $0.451$ is a small-modulus observation, not a general
Burgess constant. No originality is claimed for the enumeration method itself
(prefix sums, discrete logarithms); the citable content, if any, is the
certified five-modulus table.

## 3. Method and verification

**Group and characters.** For each $q$, the script finds $g$ with
$g^{\varphi(q)/\ell}\not\equiv 1\bmod q$ for every prime $\ell\mid\varphi(q)$;
hence $g$ generates $(\mathbb Z/q\mathbb Z)^\times$ (cyclic for odd prime
powers). A full discrete-log table $\mathrm{ind}_g$ is built, and
$\chi_j(u)=\exp(2\pi i j\,\mathrm{ind}_g(u)/\varphi(q))$ enumerates all
$\varphi(q)$ characters. Primitivity: for $q=p^2$ or $p^3$, $\chi_j$ factors
through a smaller modulus iff $p\mid j$ (the subgroup $1+p\mathbb Z$ has order
$p^{m-1}$ and $\chi_j$ is trivial on it iff $p\mid j$); the script keeps
exactly $j$ with $p\nmid j$, i.e.\ $\varphi(q)(1-1/p)$ primitive characters
(4, 16, 12, 36, 100 — matching theory).

**Sums.** For each $(j,a)$, with $w_a=e_q(a)$, the length-$2q$ array
$b_n=\chi_j(n\bmod q)w_a^{\,n}$ on units ($0$ else) and its prefix $P$ give
$S(M,N)=P[M+N+1]-P[M+1]$ for every $M\in[0,q)$, $1\le N\le q$ simultaneously
via a $q\times q$ matrix of absolute values; the running per-$N$ envelope and
the global argmax are recorded. This covers all residue classes of $M$ and
all $N\le q$; periodicity mod $q$ makes this complete.

**Independent check.** Each argmax triple was recomputed by a separate code
path (pure-Python/`cmath` direct summation over $M<n\le M+N$, no prefix
arrays, no vectorization): agreement $1.4\times10^{-15}$ ($q=9$),
$2.4\times10^{-14}$ ($q=25$), $7.2\times10^{-15}$ ($q=27$),
$4.5\times10^{-15}$ ($q=49$), $6.8\times10^{-14}$ ($q=121$). CSV row counts
equal $q$; envelope entries are monotone-consistent with the trivial bound.

## 4. Reproduction

Requires only Python 3 + numpy (run used 3.12.3 / numpy 1.26.4):

    python3 output/artifacts/verify_twist.py   # q = 9, 25, 27, 49
    python3 output/artifacts/verify121.py      # q = 121 (imports verify_twist.py)

Rerun time is seconds-to-minutes on a laptop; outputs rewrite the
`envelope_q*.csv` files and print the max-$R$ table with direct-recompute
agreement. Exact expected values are the table in §1.

## 5. Limitations and uncertainties

(i) Only five small moduli; nothing is proved for large $q$ or for the
$Q_0=2\times10^5$ exhaustion. (ii) Floating-point complex exponentials are
used, but every reported digit is cross-validated by two independent code
paths to $<10^{-13}$, and the safety margin to the rounded majorant $0.451$
exceeds $4\times10^{-4}$. A fully interval-arithmetic certificate was not
constructed. (iii) The $N\le q$ range is complete per modulus by periodicity;
$N>q$ is not tabulated (the shape bound is homogeneous, but no claim is made
there). (iv) Near-neighbor literature (Treviño explicit Burgess; Jain–Sharma
et al.\ composite Burgess; Cochrane–Granville complete mixed sums) was
surveyed from the lane brief; no new comparison computation is offered here.
