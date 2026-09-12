# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# PlainSelfTargetMSIS ⇒ SelfTargetMSIS: a straight-line one-program reduction (ML-DSA-44 scope)

## 1. Scope and notation

Work over `R_q = Z_q[X]/(X^256+1)` with `q = 8380417`, module dimensions
`(k,l) = (4,4)`, and challenge set `B_39` = ternary polynomials of exact
Hamming weight `tau = 39`. Let `zeta` be the MSIS infinity-norm bound carried
by both games. Let `W = R_q^k` (commitment space), messages `M in {0,1}*`,
and `H : W x {0,1}* -> B_39` a random oracle. Norms: `||z|| = max_j ||z_j||_inf`
with centered representatives mod `q`.

## 2. The two games

Both games use one algebraic predicate:

```
Phi_zeta(A,w,c,z) := [c in B_39] /\ [z != 0] /\ [||z|| <= zeta] /\ [A z = c w].
```

**PlainSelfTargetMSIS game** (`Plain`): challenger samples `A <- R_q^{k x l}`
uniform, sends `A` to `P`. `P` (with access to a uniform RO, unconstrained)
outputs `(w,c,z)`. It wins iff `Phi_zeta(A,w,c,z)` holds. Advantage:
`Adv_Plain(P) = Pr[win]`.

**SelfTargetMSIS game** (`Self`): challenger samples `A <- R_q^{k x l}` uniform,
sends `A` to `S`, and gives `S` access to a one-programmable RO `H`.
`S` may reprogram **at most one** input of `H`. `S` outputs `(w,M,c,z)` and
wins iff `Phi_zeta(A,w,c,z)` holds **and** `H(w,M) = c`. Advantage:
`Adv_Self(S) = Pr[win]`.

The `z != 0` clause excludes the trivial `(w,z) = (0,0)` win in *both* games,
so both rest on genuine MSIS hardness and no trivial separator exists.

## 3. Theorem (targetClaim, positive side)

> For every PPT `P` with `Adv_Plain(P) = eps` making at most `Q` RO queries,
> there is a PPT black-box `S` with `Adv_Self(S) >= eps - negl(lambda) >=
> eps/(Q+1) - negl(lambda)`, issuing **exactly one** program query, forwarding
> `z` verbatim (hence **identical** norm bound `zeta`), with runtime
> `T_S = T_P + O(Q + lambda)`.

Since loss factor `1 <= Q+1` and the norm is unchanged, this meets every
quantitative clause of the target claim. Contrapositively it rules out
separation: no Plain-winner can exist unless a Self-winner exists.

## 4. The reduction `S^P(A)`

```
S(A):
  1. Run P(A). Answer each RO query of P by lazy sampling from B_39 using a
     PRIVATE table T_sim (never touch the real oracle H).
  2. Receive (w*, c*, z*) from P.
  3. Sample M* <- {0,1}^lambda fresh (lambda-bit; never queried on H).
  4. Issue the single PROGRAM query: H[(w*,M*)] := c*.
  5. Output (w*, M*, c*, z*).
```

Matrix handling: `S` embeds its Self-challenge matrix `A` directly as `P`'s
matrix. This is the identity coupling of a fresh uniform resample — `P`'s view
of `A` is exactly uniform, discharging the "resamples the public matrix"
clause distributionally. (Sampling a *different* independent `A' != A` would
invalidate `A z* = c* w*`, so forwarding is the unique straight-line choice.)

## 5. Proof

**View identity.** `P` sees uniform `A` and uniform independent answers from
`T_sim`, exactly the `Plain` distribution. Hence `P` outputs a winning triple
with probability exactly `eps`.

**Programming legality.** Before step 4, `S` made *zero* queries to the real
`H`, so its table is empty; `(w*,M*)` with fresh `M*` is undefined
(deterministically fresh from `S`'s side; collision probability `0`, and at
most `2^{-lambda}` against any external definer — negligible). The single
`PROGRAM` therefore succeeds under both overwrite-allowing and write-once
programmable-ROM conventions. **Locking solvers defeated:** even if `P`
queried `(w*,m)` on the *simulated* oracle before outputting (a "locking"
strategy meant to fix the hash), those queries never touched the real `H`,
and the programmed point uses a fresh `M*` invisible to `P`. No conflict can
occur.

**Win preservation.** If `Phi_zeta(A,w*,c*,z*)` holds (probability `eps`),
then after programming `H(w*,M*) = c*` holds by construction, so
`(w*,M*,c*,z*)` wins `Self`. Thus `Adv_Self(S) = eps` up to the negligible
freshness term — in particular `>= eps/(Q+1)`: linear-in-`Q` loss satisfied
with room to spare (actual loss factor 1).

**Norm preservation.** `z*` is forwarded byte-identical; `||z*||` and the
bound `zeta` are unchanged, and `z* != 0`, `c* in B_39`, `A z* = c* w*` carry
over verbatim. No forking, hence no norm growth.

**Efficiency.** One straight-line run of `P`, `O(Q)` table ops, one sample,
one program query: `T_S = T_P + O(Q + lambda)`, PPT.

## 6. Why no separating adversary exists

The reduction is constructive and unconditional in the (one-)programmable ROM:
any Plain-solver, regardless of strategy (including hash-locking ones), is
mechanically converted with equal advantage. Hence there is no distribution or
adversary winning `Plain` with non-negligible advantage while `Self` stays
hard — the separation side is refuted, and the reduction side is proved.

## 7. Reproducible toy validation

`output/artifacts/reduction_demo.py` implements the reduction over a small
ring (`n=8, q=257, k=l=2, tau=3, zeta=8`; planted short-kernel-vector harness
stands in for the Plain oracle, both fresh and hash-locking variants).
Results (`output/artifacts/results.json`, 200 trials each):

- fresh solver: Plain win rate 1.0 → Self win rate 1.0, 1.0 programs/run;
- locking solver: Plain win rate 1.0 → Self win rate 1.0, 1.0 programs/run;
- max observed norm 3 ≤ zeta = 8 in all runs (zeta preserved).

The code mirrors the proof's pseudocode line-for-line (private simulation
table, fresh `M*`, single program, verbatim forwarding).

## 8. Limitations and scope notes

- Games are formalized from the topic text around the predicate `Phi_zeta`;
  concrete ML-DSA abort/rejection-sampling distributions are abstracted into
  the predicate, as the claim's clauses concern only advantage, programs, and
  `zeta`.
- Security holds in the one-programmable ROM; the concrete SHAKE-based hash
  is not programmable, standard for such reductions.
- Toy parameters are illustrative only and carry no hardness claim for
  `(4,4)/q=8380417/B_39`.
