# Sharp simplicity asymptotics for random finite-field evolution algebras

## Finding

Fix a prime power \(q\ge2\). For each \(n\), choose a labelled structure matrix \(M\) uniformly from \(\operatorname{GL}_n(\mathbb F_q)\) and let \(E_M\) be the evolution algebra with natural basis \(e_1,\ldots,e_n\) and products \(e_i e_j=0\) for \(i\ne j\), \(e_i^2=\sum_j M_{ij}e_j\). Let \(r_{n,q}\) be the probability that \(E_M\) is **not simple**. Set

\[
\phi_n(q)=\prod_{j=1}^n(1-q^{-j}),\qquad
\phi_\infty(q)=\prod_{j=1}^\infty(1-q^{-j})>0.
\]

**Theorem (single-cut simplicity law).** For \(n\ge3\),

\[
\left|r_{n,q}-\frac{2n(q-1)}{q^n-1}\right|
\le \frac{1}{\phi_n(q)}\left[
\binom{2n}{2}q^{-(2n-3)}+
\sum_{k=2}^{n-2}\binom nkq^{-k(n-k)}\right]. \tag{1}
\]

Consequently, for each fixed \(q\), as \(n\to\infty\),

\[
r_{n,q}=\frac{2n(q-1)}{q^n-1}+O_q(n^2q^{-2n+4}),
\qquad \lim_{n\to\infty}\frac{q^n r_{n,q}}n=2(q-1). \tag{2}
\]

Conditional on nonsimplicity, the support digraph has, with probability tending to one, **exactly one** of the following \(2n\) elementary cuts: a vertex with no outgoing edges to other vertices, or a vertex with no incoming edges from other vertices. By transpose symmetry, the two types are asymptotically equally likely. More precisely, the conditional probability of a failure that does not have exactly one elementary cut is \(O_q(nq^{-n+4})\).

If instead \(M\) is uniform in **all** \(n\)-by-\(n\) matrices over \(\mathbb F_q\), the exact identity

\[
\Pr(E_M\text{ simple})=\phi_n(q)(1-r_{n,q}) \tag{3}
\]

implies

\[
\lim_{n\to\infty}\Pr(E_M\text{ simple})=\phi_\infty(q),
\quad
\lim_{n\to\infty}\frac{q^n}{n}
\bigl[\phi_\infty(q)-\Pr(E_M\text{ simple})\bigr]
=2(q-1)\phi_\infty(q). \tag{4}
\]

These statements concern the uniform distribution on **labelled natural-basis structure matrices**, not the distribution on isomorphism classes.

## Assumptions and scope

Throughout, \(q\) is a prime power and \(n\ge3\) except when an auxiliary statement specifies otherwise. The matrix entries may lie in any finite field, including nonprime extension fields. A directed arc \(i\to j\) exists exactly when \(M_{ij}\ne0\); loops are allowed. The field \(\mathbb F_q\) is fixed in the asymptotics. An **elementary outgoing cut** is the singleton subset \(\{i\}\) with no outgoing arc to its complement. An **elementary incoming cut** is its complement \([n]\setminus\{i\}\) with no outgoing arc to \(\{i\}\). For \(n\ge3\) these are \(2n\) distinct events. No assumption of independence among nonzero-pattern entries is made after conditioning on invertibility.

## Proof

**1. Algebraic-to-graph reduction.** An invertible structure matrix makes \(e_1^2,\ldots,e_n^2\) a basis. If \(I\ne0\) is an ideal, choose \(x=\sum_i x_i e_i\in I\) with \(x_i\ne0\). Then \(xe_i=x_i e_i^2\in I\). If \(M_{ij}\ne0\), multiplying \(e_i^2\) by \(e_j\) puts \(e_j^2\) in \(I\). If the support digraph is strongly connected, every \(e_j^2\) belongs to \(I\), so \(I=E_M\). Conversely, if the graph is not strongly connected, a terminal strongly connected component (or the union of such components) gives a proper nonempty set \(S\) with no edge leaving \(S\). Then \(\operatorname{span}\{e_i:i\in S\}\) is a proper nonzero ideal. Thus for invertible \(M\), simplicity is equivalent to strong connectivity of the support digraph.

**2. An exact coordinate-cut probability.** For every proper nonempty \(S\subset[n]\) with \(|S|=k\), write \(B_S\) for the event that every entry \(M_{ij}\) with \(i\in S\) and \(j\notin S\) is zero. Simultaneous permutation of rows and columns then puts \(M\) in block triangular form with diagonal block sizes \(k\) and \(n-k\), and an unrestricted opposite off-diagonal block. Such a matrix is invertible exactly when both diagonal blocks are invertible. Hence

\[
\#\{M\in\operatorname{GL}_n(\mathbb F_q):B_S\}
=|\operatorname{GL}_k(\mathbb F_q)|\,
|\operatorname{GL}_{n-k}(\mathbb F_q)|\,q^{k(n-k)},
\]

\[
\Pr(B_S\mid M\in\operatorname{GL}_n)
=q^{-k(n-k)}\frac{\phi_k(q)\phi_{n-k}(q)}{\phi_n(q)}. \tag{5}
\]

In particular, for \(k=1\) or \(n-1\), the last quantity simplifies **exactly** to

\[
p_1=\frac{q-1}{q^n-1}. \tag{6}
\]

**3. Quantitative Bonferroni bounds.** Nonsimplicity is the union of \(B_S\) over all nonempty proper \(S\). Let \(\mathcal A\) consist of the \(2n\) elementary events (the subsets of sizes \(1\) and \(n-1\)). Every pair of *different* elementary events forces at least \(2n-3\) distinct matrix entries to be zero: two row constraints or two column constraints force \(2n-2\), while one row plus one column constraint force \(2n-3\) or \(2n-2\). Before conditioning on invertibility, independent uniform entries make the probability of such an intersection at most \(q^{-(2n-3)}\). As the probability of invertibility is \(\phi_n(q)\), conditional probability is at most \(q^{-(2n-3)}/\phi_n(q)\).

The elementary-event union therefore satisfies

\[
2np_1-\binom{2n}{2}\frac{q^{-(2n-3)}}{\phi_n(q)}
\le \Pr(\bigcup\mathcal A\mid\operatorname{GL}_n)\le2np_1.
\]

Every additional cut has size between \(2\) and \(n-2\). For each, the unconditional probability of the prescribed \(k(n-k)\) zero entries is \(q^{-k(n-k)}\); conditioning on invertibility gives an upper bound \(q^{-k(n-k)}/\phi_n(q)\). The union bound and the preceding Bonferroni bound imply (1).

**4. Asymptotics.** The infinite product \(\phi_\infty(q)\) is positive because \(\sum_{j\ge1}q^{-j}<\infty\), and \(\phi_n(q)\ge\phi_\infty(q)\). For the middle-cut sum, the terms \(k=2,n-2\) are at most \(n(n-1)q^{-2n+4}\). For \(3\le k\le n-3\), \(k(n-k)\ge3(n-3)\), so the remaining sum is at most \(2^nq^{-3n+9}\le q^{-2n+9}\). These estimates prove the error term in (2) for each fixed \(q\). Its ratio to the leading term tends to zero.

If nonsimplicity occurs but *not exactly one* elementary cut, either a non-elementary cut occurs or at least two elementary events occur. Their combined probability is bounded by the right-hand error term in (1). Dividing by \(r_{n,q}\asymp_q nq^{-n}\) proves the stated conditional concentration. Transposition preserves the uniform invertible-matrix distribution and exchanges the two types, giving the asymptotic one-half split.

Finally, a uniformly sampled matrix is invertible with probability \(\phi_n(q)\), and a simple evolution algebra must be perfect, so (3) follows. The tail of the infinite product gives \(\phi_n(q)-\phi_\infty(q)=O_q(q^{-n})\). Substitute (2) into (3); the \(O_q(q^{-n})\) product-tail correction is smaller than the leading \(nq^{-n}\) simplicity deficit. This proves (4).

## Verification

The accompanying standalone Python 3 checker `verify.py` exhaustively enumerates all matrices in five small prime-field cases. It computes invertibility by modular Gaussian elimination, computes strong connectivity twice (direct cut search and directed reachability), checks the exact event count (5) for every proper nonempty coordinate subset, and compares observed nonsimplicity against bound (1). Its output is:

```text
q=2 n=2: GL=6; simple=3; nonsimple=3; VERIFIED
q=3 n=2: GL=48; simple=28; nonsimple=20; VERIFIED
q=2 n=3: GL=168; simple=80; nonsimple=88; VERIFIED
q=3 n=3: GL=11232; simple=7504; nonsimple=3728; VERIFIED
q=2 n=4: GL=20160; simple=11658; nonsimple=8502; VERIFIED
VERIFY_OK
```

The \(n=2\) cases test the graph/algebra criterion and (5), not (1), which begins at \(n=3\). These are exhaustive finite checks but are not substituted for the proof for arbitrary \(n\) or extension fields.

## Relationship to prior work

The October 2026 survey by Kaygorodov, Martín González, and Viruel explicitly asks for asymptotic probabilities of simplicity under uniform finite-field structure matrices (Question 22); it supplies the perfectness-and-strong-connectivity criterion (Theorem 6) but no corresponding sharp asymptotic. Wei and Zou (2023) enumerate **isomorphism-class orbits** of invertible evolution algebras, a different measure than uniform labelled matrices. Alshatnawi, Costoya, and Viruel (2026) study tensor decomposition and graph balance, and mention probabilistic classification as a prospective direction. The present estimate uses uniform invertible-matrix cut probabilities, not orbit enumeration or ordinary independent-edge digraph probabilities. A broader theorem on coordinate-irreducibility of random invertible matrices could still imply this result; no absolute priority claim is made.

## Limitations

The quantitative error is asymptotic in \(n\) for **fixed** \(q\); no uniform sparse-support threshold is claimed. The sampling model fixes a labelled natural basis, not an isomorphism-class weighting. The result does not settle asymptotics for indecomposability, automorphism rigidity, real idempotents or a random sparse support. The finite computational verifier covers only listed small prime fields; all finite extension fields follow from the symbolic argument. Historical-priority evaluation is limited by any unlocated general combinatorial matrix theorem.

## References

1. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248 (first submitted 2026-10-15), especially Theorem 6 and Question 22. https://arxiv.org/abs/2610.22248
2. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368 (2023), Sections 1–2 and enumeration sections. https://arxiv.org/abs/2310.12368
3. I. Alshatnawi, C. Costoya and A. Viruel, *On the Grothendieck Ring of Finite-Dimensional Non-Degenerate Evolution Algebras*, arXiv:2607.15154 (first submitted 2026-07-16), introduction and Theorem A. https://arxiv.org/abs/2607.15154
