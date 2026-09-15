# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — Lane 20225: the literal stationary-profile target on the Cayley tree is provably false as stated; what survives

## 1. Model and exact identities (no mean field)

Finite rooted $N$-level $q$-ary tree, $q\ge 2$ fixed: level $i$ has $q^i$ sites.
Root entry at rate $\alpha>0$ iff empty; each bulk particle jumps at total rate $1$
to a uniformly chosen child (rate $1/q$ per directed edge), succeeding iff the child
is vacant; each level-$(N-1)$ particle exits at rate $\beta>0$.
By level symmetry the stationary per-site means $\rho_i^{(N)}$ are well defined,
and stationarity across every parent–child cut gives the exact conservation law

$$I^{(N)} := I_q^{(N)} = \alpha(1-\rho_0^{(N)}) = \beta q^{N-1}\rho_{N-1}^{(N)} = q^i\, \mathbb{E}^{(N)}[\eta_x(1-\eta_y)]$$

for every parent–child edge $x\to y$ at any levels, where $I^{(N)}$ is the total
stationary current between successive levels. In particular $0<I^{(N)}<\alpha$ and
$0<\rho_0^{(N)}<1$ for every finite $N$ (entry current positive since the root empties
at positive rate; root not identically full since entry requires emptiness).

## 2. What the target asserts (literal reading)

For each fixed $q\ge 2$, $\alpha>0$, $\beta>0$, as $N\to\infty$:

- (a) $I^{(N)}\to I(\alpha)=\alpha(1-r)$, $r=\rho_0(\alpha)\in(0,1)$ the physical root of
  $(1-J/r)^{1/q}=J/q$ with $J=\alpha(1-r)$ (equivalently $J/r+(J/q)^q=1$);
- (b) $\rho_i^{(N)}\to I(\alpha)/q^i$ for **each fixed level $i$** (no $i\ge 1$ restriction stated);
- (c) $\rho_{N-1}^{(N)}=c(\alpha,\beta)/q^{N-1}$, $c=I(\alpha)/\beta$;
- (d) absence of 1D-type boundary layers at fixed $i$, $\beta$-independence of bulk current.

## 3. Theorem (literal conjunction is impossible)

**Claim.** There are no numbers $J>0$, $r\in(0,1)$ satisfying simultaneously
$J=\alpha(1-r)$ [clause (a)], $\lim_N\rho_0^{(N)}=J$ [clause (b) at $i=0$],
and $(1-J/r)^{1/q}=J/q$ [clause (a) root equation], for any $\alpha>0$, $q\ge 2$.

**Proof.** Assume all three. From (b) at $i=0$ and exact $I^{(N)}=\alpha(1-\rho_0^{(N)})$,
passing to the limit gives $J=\alpha(1-J)$, i.e. $J=r=\alpha/(1+\alpha)$
(using $r=1-J/\alpha$ from (a)). Then $1-J/r=0$ while $(J/q)^q>0$ since $J>0$,
so $(1-J/r)^{1/q}=0\ne J/q>0$. Direct violation: e.g. $\alpha=0.5,q=2$ forces
$J=r=1/3$ with LHS $0$ vs RHS $1/6$. ∎

Hence the target **as written is rigorously false** — a complete TARGET-route
resolution (disproof), not a fallback. The proof uses only the target's own clauses
plus the exact finite-$N$ conservation identity; it assumes no mean-field
factorization and no numerics. Numerics in `output/artifacts/` corroborate which
clause must give: the Basu–Mohanty Eq.17 root $f(J)=J/(1-J/\alpha)+(J/q)^q-1=0$ is
strictly monotone hence uniquely defined (e.g. $J=0.33025\ne 1/3$ at $\alpha=0.5,q=2$),
while the profile must fail at $i=0$ (exact/Gillespie $\rho_0\approx 0.36\ne 0.319\approx J$).

## 4. Supporting evidence (not the proof; orients the repair)

- Exact generator nullspace ($q=2$, $N=2,3$; `exact_small.py`, `exact_corr.py`):
  $J=0.31970, 0.31877$ at $\alpha=0.5,\beta=1$ vs MF $0.33025$; parent–child and
  sibling covariances negative ($-0.017$, $-0.0075$), so no FKG closure.
- Gillespie to $N=8$ (`gillespie.py`): bulk $i\ge 1$ profile matches $J/q^i$ within
  $\sim 2\%$; last-level $q^{N-1}\rho_{N-1}=J/\beta$ within $\sim 2\%$ across
  $\beta=0.2,1,3$; $\beta$-decoupling emerges (TV of root+level-1 law between
  $\beta=0.2,3.0$ drops $0.705\to 0.162$ from $N=2$ to $3$; $N=6$ currents identical
  to 5dp across $\beta$).
- Source audit (Basu–Mohanty arXiv:1003.3313 via 1 method-blocker search + inspect):
  target's root equation is exactly their Eq.17; their Eq.16 profile at $i=0$ is where
  the inconsistency originates (their own $\rho_0=0.422$ at $\alpha=0.7$ violates
  $\rho_0=J=0.405$); extracted Eq.18 closed form fails Eq.17 under all branch variants.

## 5. Limitations and the surviving repaired conjecture (not claimed)

Proved: literal conjunction false. Not proved: any repaired positive statement
(e.g. profile for $i\ge 1$ with Eq.17 root, $\beta$-independence, exact current value).
The repaired core is supported numerically but needs new decorrelation/coupling
technology (mean-field gap $3$–$10\%$, $O(1)$-relative negative correlations).
The $q=2$ explicit Eqs.18–19 pointer could not be verified from the extracted text.
Finite-$N$ exact data stop at $N=3$; Monte Carlo is evidence only.

## 6. Artifact inventory

`output/artifacts/impossibility_cert.py` + `.txt` (formal certificate table);
`exact_small.py`, `exact_corr.py` (exact stationary solves); `gillespie.py` (Monte Carlo);
`mfroot2.py`, `cubic18.py`, `cubic_rho.py` (MF/root audit); `monocheck.py`,
`decoup_tv.py`, `beta_audit.py` (monotonicity/decoupling); WORKLOG.md.
