# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Finite-$n$ Delsarte–MacWilliams primal barrier below the $\xi_1$ branch of the ABL range at two BCH localizations

## 1. What is proved (narrow, local claim)

Fix the **real** Delsarte–MacWilliams LP relaxation for binary linear codes:
dual variables $B_0=1$, $B_j=0$ for $1\le j<d'$, $\sum_j B_j=2^{\,n-k}$, and
$A_i=(KB)_i/2^{\,n-k}\ge 0$ for all $i$, with $K$ the binary Krawtchouk matrix.
Let $P_w=\max A_w$ over this polytope. By LP weak duality over the reals,
$P_w$ lower-bounds the value of **every real-LP Krawtchouk certificate**
(nonnegative combination of the polytope's defining linear constraints)
that upper-bounds $A_w$; integrality is not used on either side.

**Theorem (local $\xi_1$-branch barrier).** At $(n,k,d')=(15,7,4)$ and
$(31,15,7)$:

| $(n,k,d')$ | $w$ | $w/n$ vs $\xi_1$ | primal max $P_w$ | binomial $2^{k-n}\binom nw$ | ratio |
|---|---|---|---|---|---|
| (15,7,4) | 2 | $0.1333<0.1601$ | $5.63636$ | $0.410156$ | $13.74$ |
| (31,15,7) | 4 | $0.1290<0.1835$ | $22.2762$ | $0.480118$ | $46.40$ |
| (31,15,7) | 5 | $0.1613<0.1835$ | $29.4919$ | $2.59264$ | $11.38$ |

Hence no real-LP Krawtchouk certificate valid on the MacWilliams polytope
certifies the binomial upper bound at these tabulated below-$\xi_1$ points.
The polytopes are certifiably nonempty (the dual $[15,8,4]$ exists by the
BCH/dual construction; the $[31,16,7]$ BCH code exists), and all constraint
residuals of the exhibited optima are $\lesssim 10^{-4}$
(`output/artifacts/lp_verify.txt`). The ratios $11$–$46$ exceed $1$ with
margin robust to any solver tolerance.

**$\xi_2$-branch accounting.** With $\xi_1=(1/2)(1-\sqrt{\delta'(2-\delta')})$
and $\xi_2$ the ABL root of
$R=(1-\delta')H((\omega^\star-\delta'/2)/(1-\delta'))+1+\delta'-H(\omega^\star)$
($\omega^\star(\xi)=1/2-\sqrt{\xi(1-\xi)}$; "if the root is negative, put
$\xi_2=0$"), the scan `output/artifacts/xi2_scan.csv` shows that at both
localizations the right-hand side minus $R$ is strictly positive
($\ge 0.23$) over the entire admissible $\omega^\star\in[\delta'/2,1/2]$,
so no root exists and $\xi_2=0$ by the ABL convention. Therefore
$\xi_{ABL}=\min\{\xi_1,\xi_2\}=\xi_1$ binds at both localizations, and the
barrier above is a barrier below the operative ABL threshold branch there.
No global or asymptotic open-set claim is made.

## 2. Method

Any real-LP Krawtchouk upper certificate for $A_w$ is a nonnegative
combination of the defining linear constraints plus a constant; its value is
therefore $\ge P_w$ (LP weak duality, reals). The LPs (16 and 32 variables)
use the exact integer Krawtchouk matrix (`math.comb`), are solved to
optimality (PuLP/CBC), and the optimizer $B^\star$ is retrieved with every
residual verified. The $\xi_1$ values and the strict monotonicity
$d\xi_1/d\delta' < 0$ are tabulated in `xi1_curve.csv`; the $\xi_2$ gap scan
is in `xi2_scan.csv`.

## 3. Scope, limits, and what is NOT claimed

- **Real-LP certificates only.** The theorem covers certificates by real
linear consequence on the MacWilliams polytope. It does not cover
certificates that essentially use dual integrality, and it makes no claim
about true extremal code weight distributions or existence of violating
codes.
- **Heuristic on integrality (not a lemma).** We record only the heuristic
suggestion that, for a *fixed* certificate of fixed degree, dual
integrality plausibly enters as polynomial-factor ($o(1)$-in-exponent)
shifts or in the wrong direction for upper bounds — but this is explicitly
**unproved** here (no uniform degree accounting is given), and the theorem
does not rely on it.
- **ABL citation correction.** Ashikhmin–Barg–Litsyn
(doi:10.1109/18.915662) state their free-parameter choice is optimal but
leave that optimality assertion unproved ("we leave this fact without
proof"); we therefore claim no ABL family-optimality of our own, and no
global LP-optimality of $\xi_{ABL}$.
- **Local, not asymptotic.** The barrier is proved at the two finite-$n$
BCH localizations; no open set of $(R,\delta')$, no $\varepsilon$-extension
ruling, and no asymptotic primal-extremal family is claimed.
- Originality check: one consolidated literature call (20 fused results)
showed the ABL source, Delsarte-LP uniqueness work, and LP hierarchies, but
no prior finite-$n$ primal-duality certificate-nonexistence computation at
these BCH parameters for the ABL binomiality range.

## 4. Reproduction

`python3 output/artifacts/lp_optimality_check.py` writes `lp_primal.csv`
and `xi1_curve.csv`; `python3 output/artifacts/lp_verify.py` writes
`lp_verify.txt` with all residuals; `python3 output/artifacts/xi2_branch.py`
writes `xi2_scan.csv`. Source formulas verified against the publisher PDF of
doi:10.1109/18.915662 (`dd.pdf`, pp. 1054–1055).
