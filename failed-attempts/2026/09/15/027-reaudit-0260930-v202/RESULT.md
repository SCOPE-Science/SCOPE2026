# Regularity of weak-tracial-Rokhlin compact-group crossed products, with classification conditional on UCT

## Context

Let \(A\) be unital, separable, simple, infinite-dimensional and nuclear, with
\(\operatorname{TR}(A)\le 1\), and suppose \(A\) satisfies the UCT.  Let \(G\)
be a second-countable compact group and let
\(\alpha:G\to\operatorname{Aut}(A)\) have the weak tracial Rokhlin property
with comparison in the sense of Fang--Tian.  Put
\[
B=A^\alpha,\qquad C=A\rtimes_\alpha G .
\]

The weak tracial Rokhlin results give strong regularity and stable
Morita-equivalence conclusions.  They do **not**, under the hypotheses above,
supply the UCT for \(B\) or \(C\).  That distinction is essential for applying
the current Elliott-classification theorems.

## Result

1. \(B\) is unital, separable, simple, nuclear and \(\mathcal Z\)-stable.
   The crossed product \(C\) is separable, simple, nuclear and
   \(\mathcal Z\)-stable, and \(B\) and \(C\) are strongly Morita equivalent
   (equivalently, \(B\otimes\mathcal K\cong C\otimes\mathcal K\)).

2. The UCT for \(A\) alone does **not currently justify** a conclusion that
   \(B\) or \(C\) satisfies the UCT.  In particular, UCT permanence cannot be
   inserted merely because \(G\) is compact/amenable.  Even preservation of
   the UCT by arbitrary finite-group crossed products is intertwined with the
   general UCT problem.

3. If one adds the hypothesis that \(B\) satisfies the UCT (equivalently here,
   that \(C\) satisfies the UCT, by Morita invariance), then
   \[
   \operatorname{gTR}(B\otimes Q)\le 1,
   \]
   and \(B\) is classified, within the usual unital simple stably finite
   nuclear \(\mathcal Z\)-stable UCT class, by its Elliott invariant.

4. Under the same additional UCT hypothesis, the stable isomorphism class of
   \(C\) is determined by that of \(B\).  If \(G\) is finite, then \(C\) is
   unital; in that finite-group case the same unital classification machinery
   applies directly to \(C\), yielding
   \(\operatorname{gTR}(C\otimes Q)\le1\) and Elliott classification.

No assertion is made that \(\operatorname{TR}(C)\le1\) under the weak
tracial Rokhlin property with comparison.

## Proof / evidence

- Tracial rank at most one places \(A\) in the stably finite regularity regime;
  the standard Lin--Winter/classification regularity results give
  \(\mathcal Z\)-stability in the present simple nuclear setting.

- Fang--Tian prove that the fixed-point algebra inherits tracial
  \(\mathcal Z\)-stability and, for amenable \(A\), becomes
  \(\mathcal Z\)-stable.  Their Theorem 5.11 gives
  \(\mathcal Z\)-stability for both \(A^\alpha\) and \(A\rtimes_\alpha G\).
  Their Section 4 gives simplicity and stable isomorphism of the fixed-point
  algebra and crossed product.

- None of those weak-tracial-Rokhlin results supplies the UCT.  This is not a
  routine amenability permanence issue: work of Barlak--Szabó and Barlak--Li
  shows that UCT preservation for suitable finite cyclic crossed products is
  strong enough to characterize the general UCT problem.  By contrast,
  stronger Rokhlin-type hypotheses have separate UCT-permanence theorems.

- If \(B\) is assumed UCT, then \(B\) is unital, simple, separable, nuclear,
  stably finite and \(\mathcal Z\)-stable.  Finite nuclear dimension and
  quasidiagonality of traces in the UCT setting feed the
  Elliott--Gong--Lin--Niu generalized-tracial-rank theorem, giving
  \(\operatorname{gTR}(B\otimes Q)\le1\), and the standard Elliott invariant
  classifies \(B\).

- The UCT is invariant under stable isomorphism/Morita equivalence, so the
  added UCT assumption can equivalently be placed on \(B\) or \(C\).  For an
  infinite compact group the crossed product need not be unital (already the
  trivial action of an infinite compact group illustrates this phenomenon),
  so a blanket unital Elliott invariant containing \([1_C]\) is not available
  without an additional unitality assumption.

## Limitations

This record does not prove UCT permanence for weak-tracial-Rokhlin compact
group actions, and it does not prove exact tracial-rank-one permanence.
The classification conclusion is therefore conditional on UCT for the
fixed-point algebra/crossed product.  For arbitrary infinite compact groups
the crossed product is treated stably/Morita-theoretically rather than as a
unital algebra.

## References

- X. Fang and H. Tian, *Crossed products by compact group actions with the
  weak tracial Rokhlin property*, arXiv:2508.06844.
- S. Barlak and G. Szabó, *Approaching the UCT problem via crossed products
  of the Razak--Jacelon algebra*, arXiv:1712.00823.
- E. Gardella, *Equivariant KK-theory and the continuous Rokhlin property*,
  arXiv:1406.1208.
- G. Gong, H. Lin and Z. Niu, *A classification of finite simple amenable
  Z-stable C*-algebras, II*, arXiv:1909.13382.
- G. Elliott, G. Gong, H. Lin and Z. Niu, *On the classification of simple
  amenable C*-algebras with finite decomposition rank, II*,
  arXiv:1507.03437.
