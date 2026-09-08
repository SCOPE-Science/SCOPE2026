# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified ECH-capacity obstructions for rational ellipsoids into polydisks
## A beyond-volume census in the Frenkel–Mueller window with two hand-checked witnesses

**Scope.** Rational 4D embeddings \(E(1,a)\hookrightarrow \lambda\cdot P(1,\beta)\),
\(a\in\mathbb Q_{\ge 1}\), \(\beta\in\{1,6/5,5/4\}\), \(a\) in the
Frenkel–Mueller staircase window (convergents/neighbours of \(3+2\sqrt2\) plus
integers \(5,\dots,8\)). ECH capacities via Hutchings' exact lattice formulas;
comparison against the volume bound (exact rational arithmetic); an inclusion
upper bound recorded as the construction side.

**Conventions.**
\[E(a,b)=\{\pi|z_1|^2/a+\pi|z_2|^2/b\le 1\},\quad
  P(a,b)=\{\pi|z_1|^2\le a,\ \pi|z_2|^2\le b\},\quad B(a)=E(a,a),\]
with the standard symplectic form. Write \(E(1,a)\), \(P(1,\beta)\) for the
surveyed shapes.

---

## 1. Background formulas (Hutchings, arXiv:1005.2260)

We use only the following quoted, standard results. Proofs are in Hutchings;
we restate them as the replay rules.

- **(E) Ellipsoid (Prop. 1.2).** \(c_k(E(a,b))\) is the \((k+1)\)-st smallest
  entry (counting multiplicity, starting from index \(k=0\) with value \(0\))
  of the matrix \((am+bn)_{m,n\in\mathbb N}\).
- **(P) Polydisk (Thm. 1.4).**
  \(c_k(P(a,b))=\min\{am+bn:(m,n)\in\mathbb N^2,\ (m+1)(n+1)\ge k+1\}\),
  with \(c_0=0\).
- **(B) Ball (Cor. 1.3).** \(c_k(B(a))=da\) where \(d\) is the unique integer
  with \((d^2+d)/2\le k\le (d^2+3d)/2\).
- **(M) Monotonicity (Thm. 1.1).** A symplectic embedding
  \(X_0\hookrightarrow\mathrm{int}(X_1)\) implies
  \(c_k(X_0)\le c_k(X_1)\) for all \(k\).
  Applied to \(E(1,a)\hookrightarrow\lambda P(1,\beta)\) with the scaling
  \(c_k(\lambda X)=\lambda c_k(X)\), every index \(k\) gives the lower bound
  \[\lambda \ge c_k(E(1,a))/c_k(P(1,\beta)) =: R_k(a,\beta).\]
- **(U) Packing/union (Prop. 1.5).** Capacities of a disjoint union are the
  max-convolution of the parts; McDuff's theorem identifies
  \(E(1,a)\) capacities with the ball-packing of its weight sequence
  \(w(a)\). Used only as an independent cross-check.
- **Volume.** \(\mathrm{vol}\,E(1,a)=a/2\), \(\mathrm{vol}\,P(1,\beta)=\beta\),
  so volume gives \(\lambda^2\ge a/(2\beta)\), i.e.
  \(\lambda_{\mathrm{vol}}=\sqrt{a/(2\beta)}\).
  An ECH index is *beyond volume* when \(R_k^2 > a/(2\beta)\),
  checked exactly in \(\mathbb Q\) (no floating point).
- **Construction side (baseline inclusion).** Since
  \(E(1,a)\subset P(1,a)\) (as \(\pi|z_1|^2\le 1,\ \pi|z_2|^2\le a\)),
  there is an explicit inclusion \(E(1,a)\hookrightarrow\lambda P(1,\beta)\)
  at \(\lambda\le\max(1,a/\beta)\). This is an upper bound, not an optimal
  folding; an ECH lower bound can never exceed the true optimal construction,
  so "beyond folding" is honestly read as: the ECH bound strictly improves
  the volume bound *inside* the volume-vs-construction gap.

No originality is claimed for (E), (P), (B), (M), (U); the contribution is
the certified finite census and the two hand-verified witnesses below.

---

## 2. Main results

### Theorem A (hand-checked beyond-volume witness; primary claim).
For \(E(1,5)\) into dilates of the cube \(P(1,1)\):
\[c_5(E(1,5)) = 5,\qquad c_5(P(1,1)) = 3,\]
so any symplectic embedding \(E(1,5)\hookrightarrow\lambda P(1,1)\) needs
\(\lambda\ge 5/3\). Since \(\lambda_{\mathrm{vol}}=\sqrt{5/2}\),
\[(5/3)^2 - 5/2 = 25/9-5/2 = 5/18 > 0,\]
an exact positive gap. Hence ECH strictly beats volume; with the inclusion
upper bound \(\lambda\le 5\), \(5/3\) lies strictly inside the
\([\sqrt{5/2},\,5]\) volume-vs-construction gap.

*Proof by hand.* For (E) with \(a=5\), values \(m+5n\) sorted:
\((0,0)\to0\); \((1,0)\to1\); \((2,0)\to2\); \((3,0)\to3\); \((4,0)\to4\);
\((0,1)\to5\) and \((5,0)\to5\). Since every other \((m,n)\) gives
\(m+5n\ge 5\) (as \(m\ge 6\Rightarrow m\ge 6>5\), \(n\ge 2\Rightarrow\ge10\),
\(n=1\Rightarrow m+5\ge 5\)), the 6th entry (index \(k=5\)) is \(5\).
For (P) with \(k=5\), need \((m+1)(n+1)\ge 6\): candidates include
\((5,0)\to5\), \((2,1)\to3\), \((1,2)\to3\), \((0,5)\to5\);
any other admissible pair has \(m+n\ge 3\) (if \(m,n\ge 1\) then
\((m+1)(n+1)\ge 6\) forces \(m+n\ge 3\) except \((1,1)\) which is inadmissible
since \(2\cdot2=4<6\); if one coordinate is \(0\), say \(n=0\), then
\(m+1\ge 6\) gives \(m\ge 5\)), so the minimum is \(3\), attained at
\((1,2)\) [and \((2,1)\)]. Then (M) gives \(\lambda\ge 5/3\), and the gap
computation above is exact rational arithmetic. ∎

### Theorem B (second hand-checked witness).
For \(E(1,6)\) into dilates of \(P(1,1)\):
\[c_8(E(1,6)) = 7\quad\text{(witness }(m,n)=(1,1)\text{)},\qquad
  c_8(P(1,1)) = 4\quad\text{(witness }(2,2)\text{)},\]
so \(\lambda\ge 7/4\), while \(\lambda_{\mathrm{vol}}=\sqrt3\);
\((7/4)^2-3=49/16-3=1/16>0\).

*Proof by hand.* Values \(m+6n\): \(0,1,2,3,4,5,6\) (from \((0..6,0)\)),
then \(7\) from \((1,1)\) and \((7,0)\); nothing else is \(<7\).
Index count: entries \(0\)–\(6\) are indices \(0\)–\(6\), so \(7\) is index
\(7\) and \(8\) (multiplicity 2); hence \(c_8=7\).
For the polydisk, \((m+1)(n+1)\ge 9\): \((2,2)\to4\); any admissible pair has
\(m+n\ge 4\) (if \(m=0\) then \(n\ge 8\); \(m=1\) then \(n\ge 3\) giving sum
\(\ge 4\); \(m=2\) then \(n\ge 2\) giving sum \(\ge 4\); \(m\ge 3\) symmetric),
so the minimum is \(4\). ∎

### Theorem C (certified census; machine-checked, exact arithmetic).
Over 13 surveyed \(a\)-values
(\(5,11/2,45/8,17/3,29/5,99/17,169/29,35/6,41/7,6,19/3,7,8\))
\(\times\) \(\beta\in\{1,6/5,5/4\}\) with \(k\le 80\) (\(39\) pairs),
all capacity comparisons were computed in exact rational arithmetic
(`output/artifacts/ech_census.py`, `census.json`):
- **ECH-decided (beyond volume in scope):** e.g. at \(\beta=1\):
  \(a=5\) (12 indices, best \(5/3\) at \(k=5\));
  \(a=6\) (best \(7/4\) at \(k=8\));
  \(a=11/2\) (best \(5/3\) at \(k=5\));
  \(a=45/8,17/3\) (best at \(k=35\): \(27/16\), \(17/10\));
  \(a=35/6,41/7\) (best at \(k=8\): \(41/24\), \(12/7\));
  \(a=7\) (best \(15/8\) at \(k=24\), gap \((15/8)^2-7/2=1/64\));
  \(a=19/3\) (sole index \(k=63\): \(25/14\)).
  At \(\beta=6/5\) and \(5/4\) every surveyed \(a\) has at least one
  beyond-volume index (e.g. \(k=5\) throughout, ratio \(25/16\) resp. \(20/13\)).
- **Volume-only in scope (\(k\le 80\)):** at \(\beta=1\),
  \(a\in\{29/5,\ 99/17,\ 169/29,\ 8\}\) show no index with
  \(R_k^2>a/2\). These are classified *left open by ECH in scope*
  (volume vs. beyond-capacity criteria needed), not as non-embeddings.
- Every row logs the McDuff weight sequence \(w(a)\) (with the exact
  identity \(\sum w_i^2=a\) asserted in-script), the minimizing lattice
  pairs on both sides for the best index, \(R^2\) vs.\ volume\(^2\) as
  exact fractions, and the full beyond-volume index list.
- The four focused certificates re-derive \(c_k(E)\) independently via the
  max-convolution (U) over weight balls and agree
  (`packing_agrees: true`).

---

## 3. Reproduction

```
cd output/artifacts && python3 ech_census.py
```
Stdlib only (`json`, `fractions`, `math` for the CF convergents of
\(3+2\sqrt2=[5;\overline{1,4}]\), verified in-script as
\(5,6,29/5,35/6,169/29,\dots\)).
Truncation is exact: ellipsoid search \(m,n\le K+2\) suffices for the first
\(K+1\) values when \(a\ge 1\) (the \((K+1)\)-st value is \(\le K\), attained
on the \(m\)-axis); polydisk search \([0,k+1]^2\) contains \((k,0)\).
No floating point enters any comparison (squares compared in \(\mathbb Q\)).

## 4. Limitations and honest framing (read before citing)

1. **Formulas are Hutchings';** the new content is the concrete witnesses and
   the finite census with minimizing-path logs, not the method.
2. **"Beyond folding":** no optimal folding threshold is computed; the
   construction side is the crude inclusion \(\lambda\le\max(1,a/\beta)\).
   The theorems prove ECH strictly above *volume* inside the
   volume-vs-construction gap — a beyond-volume obstruction fragment — not
   "ECH beats the optimal folding".
3. **Finite scope:** "volume-only" verdicts are relative to \(k\le 80\);
   a higher index could still give an ECH gap (nothing is claimed about
   sharpness or about \(C_\beta\) staircase functions).
4. **Theorems A–B are hand-provable** (§2 proofs); Theorem C rests on the
   replay script (exact arithmetic, auditable logs in `census.json`).
5. **Prior art:** McDuff–Schlenk (ball leg), Hutchings (formulas),
   Hutchings-Beyond (opposite direction), Usher / Frenkel–Mueller /
   Farley et al. (staircase structure) are structural; this note adds the
   per-rational certified \((a,\beta,k)\) witnesses absent from those tables.
