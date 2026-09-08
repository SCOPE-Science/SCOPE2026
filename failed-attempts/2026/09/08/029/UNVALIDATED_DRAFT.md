# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Towards a thin-but-not-quasi-alternating certificate: certified table audit and a sound–complete finite lattice-embedding decision procedure

**Status: partial theorem only. No quasi-alternating status of any knot is decided here.**

## Abstract

We record two fully verified steps toward the audit plan in `inputs/topic.json`
for deciding a homologically thin QA-unresolved 11–12 crossing knot via a
branched-cover definite-manifold obstruction (Greene route):

(A) a machine-checked audit of the candidate source table (Jablan Table
“Lost”: candidates for 12-crossing homologically thin non-QA knots) from the
committed source `jablan_QATables.tex`; and

(B) a proved sound-and-complete finite decision procedure for the lattice-embedding
question at the heart of the Greene obstruction, with an exact-integer
stdlib-only implementation and passing self-tests.

No Goeritz matrix was built from any diagram/DT code, no correction terms
(d-invariants) or Turaev torsion were computed, and **no claim is made about
the QA status of any knot**. All demonstration lattices in §3 are explicitly
pattern-scale examples, not Goeritz lattices of any knot.

## 1. Certified audit of the candidate table

**Proposition A (Lost-table audit).** The committed Jablan source contains a
table captioned “Candidates for 12-crossing homologically thin non-QA knots’’
(Table Lost) with exactly six knot labels and the following Conway strings
(verbatim modulo TeX spacing `\,`):

| label | Conway string (verbatim) |
|---|---|
| 12n139 | `.2.(-2\,1,2).2` |
| 12n331 | `(-3,-2\,-1)\,(3,2+)` |
| 12n397 | `2\,1\,1:-2\,-1\,0:2\,0` |
| 12n414 | `-2\,-1\,0.3.2.2\,0` |
| 12n768 | `2:-3\,-1\,0:3\,0` |
| 12n838 | `-2.-2.-2\,0.2.2.2\,0` |

*Evidence.* Script `artifacts/audit_lost_table.py` extracts the verbatim block
and asserts the label list equals `[139,331,397,414,768,838]`; log
`artifacts/lost_table_audit.txt` records the pass. The block is quoted in the
log so any checker can compare by eye against the source.

**Remark R (12n397 source ambiguity, unresolved).** The same source states,
two paragraphs above the table, that “$12n_{397}$ = $2\,1\,1:-2\,1\,0:2\,0$
has another minimal diagram which is QA’’ (note `-2\,1\,0`), while the Lost
table lists $12n_{397}$ = `$2\,1\,1:-2\,-1\,0:2\,0$` (note `-2\,-1\,0`) as a
non-QA candidate. The two Conway strings differ. We flag this without
resolving it: any future Kstar nomination of 12n397 must first disambiguate
which diagram/DT code is meant. This remark is a verification caveat, not a
classification claim.

## 2. Lattice-embedding decision procedure

### 2.1 Setup

Let $G$ be a negative-definite Goeritz Gram matrix (order $r$) and put
$P=-G$, symmetric positive-definite $r\times r$ integer. The Greene-type
question is whether the lattice defined by $P$ embeds isometrically into a
standard diagonal lattice $I_N=(\mathbb Z^N,\mathrm{id})$, i.e. whether there
exists an integer $r\times N$ matrix $M$ with

$$M M^T = P.$$

### 2.2 Lemma N (necessary conditions)

**Lemma N.** If such $M$ exists then:
(i) $r \le N$ (rank bound);
(ii) each diagonal entry $P_{ii}=\sum_k M_{ik}^2$ is a sum of $N$ integer squares;
(iii) $\det P \le \prod_i P_{ii}$ (Hadamard bound), with equality only if $P$
is diagonal;
(iv) if $r=N$ then $\det P$ is a nonzero perfect square, namely $(\det M)^2$.

*Proof.* (i) $\mathrm{rank}(P)=r$ since $P$ is positive-definite; $\mathrm{rank}(M)\le\min(r,N)$
and $\mathrm{rank}(MM^T)\le\mathrm{rank}(M)$, so $r\le N$.
(ii) is the $(i,i)$ entry of $MM^T=P$.
(iii) Write the exact rational Cholesky factorisation $P=LL^T$ ($L$ lower
triangular, $L_{ii}>0$); then $\det P=\prod_i L_{ii}^2$ while
$P_{ii}=\sum_{k\le i}L_{ik}^2\ge L_{ii}^2$, and multiplying gives the bound;
equality forces all off-diagonal $L_{ik}=0$, i.e. $P$ diagonal.
(iv) $\det P=\det(MM^T)=(\det M)^2$ for square $M$, and $\det M\in\mathbb Z$.
∎

Remarks: (iv) already rules out e.g. the $A_2$ lattice
$\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right)$,
$\det=3$, from embedding into $I_2$ (see T3a below). The method is standard;
our contribution is only the certified packaging for this program.

### 2.3 Theorem S (soundness and completeness of the search)

**Theorem S.** The procedure `find_embeddings` in
`artifacts/lattice_embed.py` is sound and complete for the stated question:
for input $(P,N)$ with $P$ symmetric positive-definite,
every matrix it returns satisfies $MM^T=P$ (soundness), and every integer
matrix satisfying $MM^T=P$ is returned unless a caller-supplied cap stops the
search, in which case the returned exhaustive flag is False (completeness).
All arithmetic is exact integer arithmetic (Bareiss determinants, integer
norm-shell enumeration, integer inner-product checks).

*Proof.* Positive-definiteness is checked exactly via Sylvester’s criterion
with Bareiss determinants. If $r>N$ the procedure returns $(\emptyset,
\mathrm{exhaustive})$ which is correct by Lemma N(i). Otherwise, row $i$ of
any solution must satisfy $\|v\|^2=P_{ii}$ by Lemma N(ii), and
`enum_vectors` enumerates that shell exactly (bounded product scan with exact
norm test). Backtracking keeps exactly those partial rows whose pairwise inner
products match $P_{ij}$ — a necessary condition from $MM^T=P$ — and accepts a
full $r$-tuple iff all inner products match, i.e. iff $MM^T=P$. Hence every
returned matrix is a solution and every solution is visited. The exhaustive
flag is True iff no cap fired. ∎

## 3. Computed evidence (pattern-scale demos, NOT knot Goeritz lattices)

Self-tests in `artifacts/lattice_embed.py`, log
`artifacts/lattice_embed_tests.txt` (all exhaustive, all returned solutions
re-verified by $MM^T=P$):

- T1: $P=[2]$, $N=1$: 0 embeddings (no integer square root of 2).
- T2: $P=[2]$, $N=2$: exactly 4 embeddings $(\pm1,\pm1)$.
- T3a: $P=A_2$, $N=2$: 0 embeddings; $\det=3$ nonsquare (Lemma N(iv)).
- T3b: $P=A_2$, $N=3$: 48 embeddings, all verified.
- T4: $P=I_3$, $N=2$: 0 embeddings by rank bound (Lemma N(i)).
- T5: $P=\left(\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\right)$,
  $N=3$: 24 embeddings, all verified; $\det=8$.

These demonstrate the procedure on the same matrix sizes ($r\sim 2$–$3$,
small norms) expected for small-crossing Goeritz lattices, but **no linkage
to any knot’s Goeritz lattice is established** — the numbers carry no knot
consequences.

## 4. Separation of proof / evidence / conjecture / uncertainty

- **Proved:** Lemma N, Theorem S, Proposition A (table audit).
- **Computed evidence:** T1–T5 counts with exhaustive flags and re-verification;
  audit log. Replays in seconds with stdlib Python 3.12.
- **Conjecture (not claimed):** that the nominated Kstar is non-QA via this
  route. No evidence for it is presented here.
- **Uncertainty / gaps:** (a) no Goeritz matrix from committed diagram/DT
  codes was ever constructed in this lane; (b) no d-invariant/Turaev-torsion
  computation was run; (c) the 12n397 Conway-string ambiguity (Remark R) is
  unresolved; (d) the search enumerates norm shells by bounded product scan,
  so it is practical only for small $r,N$ and small diagonal entries — no
  scaling claim is made.

## References (prior art; no originality claimed over these)

- Jablan, Tables of quasi-alternating knots with at most 12 crossings,
  arXiv:1404.4965 (committed source `jablan_QATables.tex`).
- Greene, Homologically thin, non-quasi-alternating links, arXiv:0906.2222
  (Donaldson/definite-manifold obstruction; closes 11n50/pretzels only).
- Greene–Watson, Turaev torsion, definite 4-manifolds, and quasi-alternating
  knots, arXiv:1106.5559 (torsion/correction-term technology).
- Manolescu–Ozsváth, On the Khovanov and knot Floer homologies of
  quasi-alternating links, arXiv:0708.3249 (QA implies thin; thickness silent
  on thin candidates).
- Qazaqzeh–Chbili, arXiv:1406.0279 (Q-degree obstruction does not
  characterize QA).
