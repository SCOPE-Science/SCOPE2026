# Full parameter dimension for binary and ternary independent ranking laws

## Finding

Let \(n\ge4\), and let \(\mathcal A_{n,k}\subset\Delta(S_n)\) be the set of probability distributions of the ordering permutation of \(n\) independent, almost surely non-tied real random variables, each supported on at most \(k\) points. For the first two nonconstant support sizes, the precise real semialgebraic dimensions are

\[
\boxed{\dim_{\mathrm{sa}}\mathcal A_{n,2}=n,\qquad
\dim_{\mathrm{sa}}\mathcal A_{n,3}=2n\quad(n\ge4).}
\]

More strongly, for each \(k\in\{2,3\}\), one fixed global ordering of the labeled atoms and strictly positive atom masses realizes a smooth \(n(k-1)\)-parameter family whose induced permutation law has full Jacobian column rank \(n(k-1)\) on a nonempty open mass domain.

## Assumptions and scope

The indices are \(1,\ldots,n\). The law of a permutation \(\pi\in S_n\) is \(p_\pi=\Pr(X_{\pi(1)}<\cdots<X_{\pi(n)})\). Independence is mutual, not merely pairwise. No tie between distinct variables is permitted, including positive-probability atomic ties. The dimension refers to the real semialgebraic dimension of the achievable subset of the permutation probability simplex, not the number of points in that subset or an ambient dimension.

A single support point per variable produces a deterministic ranking, so this first nonconstant case is \(k=2\). The statement holds for all integer \(n\ge4\), without asymptotics or genericity assumptions on arbitrary rank laws. The witnesses use exactly \(k\) strictly positive atoms per variable and disjoint supports across variables.

## Proof

**1. Universal upper bounds.** For each fixed interleaving pattern of at most \(k\) labeled support atoms per variable, all ranking probabilities are multiaffine polynomials in the atom masses, with \(k-1\) free masses per variable. Indeed, a choice of one atom for each variable yields a deterministic permutation, and its probability is the product of the chosen masses. There are finitely many interleaving patterns, including all reduced support sizes. Therefore \(\mathcal A_{n,k}\) is a finite union of polynomial images of simplex products, and its semialgebraic dimension is at most \(n(k-1)\). This argument handles arbitrary real atom positions because their only influence on the ranking law is their finite global interleaving order.

**2. The one-moved-label Jacobian principle.** Fix baseline atoms \(b_i=i\), giving the identity ranking \(\iota=(1,2,\ldots,n)\). Give each variable \(X_i\) up to \(k-1\) alternative atoms, all distinct from every other atom. Denote by \(u_{ij}\) the mass at alternative \(j\), with baseline mass \(1-\sum_j u_{ij}\). Suppose choosing exactly that alternative for variable \(i\) while all other variables take baselines yields permutation \(\sigma_{ij}\). At the algebraic boundary \(u=0\), differentiation of the polynomial ranking-law map gives

\[
\frac{\partial p}{\partial u_{ij}}\biggr|_{u=0}
=e_{\sigma_{ij}}-e_{\iota}.
\]

Consequently, if the \(n(k-1)\) permutations \(\sigma_{ij}\) are all distinct and nonidentity, these Jacobian columns are linearly independent: each has its own exclusive nonidentity coordinate. The corresponding nonzero minor is polynomial in \(u\), so its nonvanishing at \(u=0\) persists at some small vector with **all** masses strictly positive. The constant-rank/inverse-function criterion then gives dimension at least \(n(k-1)\).

**3. Binary witnesses.** Put the second atom of \(X_1\) after baseline \(n\). For every \(i=2,\ldots,n\), put the second atom of \(X_i\) before baseline \(1\). Here 'after' and 'before' mean in the total order on the real line when the other variables retain their baseline atoms. The resulting \(n\) nonidentity permutations are

\[
(2,3,\ldots,n,1),\quad (i,1,2,\ldots,i-1,i+1,\ldots,n),
\qquad 2\le i\le n.
\]

They are pairwise distinct for \(n\ge3\). Hence \(\dim\mathcal A_{n,2}\ge n\).

**4. Ternary witnesses.** For \(n\ge4\) place two alternative atoms for each variable at the indicated relative positions (choose distinct real values in the relevant open intervals):

| Variable | Alternative 1 | Alternative 2 |
|---|---|---|
| \(1\) | just after baseline \(3\) | just after baseline \(4\) |
| \(2\) | before baseline \(1\) | just after baseline \(4\) |
| \(3\) | before baseline \(1\) | just after baseline \(1\) |
| \(4\) | before baseline \(1\) | just after baseline \(1\) |
| each \(i\ge5\) | before baseline \(1\) | just after baseline \(1\) |

For example, with four indices the eight single-alternative rankings, written as concatenated labels, are

\[
2314,\ 2341,\ 2134,\ 1342,\ 3124,\ 1324,\ 4123,\ 1423.
\]

These are distinct. For \(n>4\), the first eight rankings extend by preserving the new labels' baseline order. Every additional label \(i\ge5\) supplies exactly two new permutations: one starts with \(i,1\), the other starts with \(1,i\). They are different from all earlier permutations because those retain the new label in its baseline position. Thus all \(2n\) single-alternative permutations are distinct and nonidentity for every \(n\ge4\). By step 2, \(\dim\mathcal A_{n,3}\ge2n\).

Together with step 1 this proves the two stated equalities. The existence of a single positive-mass chamber attaining full rank follows from the same polynomial-minor argument. \(\square\)

## Verification

Run `python3 verify.py` from a directory containing the included checker. It uses only the Python standard library. The checker constructs the binary witnesses for \(3\le n\le100\), the ternary witnesses for \(4\le n\le100\), and checks that each list has the required number of distinct nonidentity permutations. It also independently enumerates the \(3^3\) atomic draws for a separate three-variable benchmark and verifies an exact rational Jacobian minor \(-2/2187\). The recorded run passed 30,465 scalar witness conditions plus the separate exact-matrix assertions.

The finite checker is **not** an infinite proof. The all-\(n\) claim is established by the explicit insertion patterns and the Jacobian argument in the proof. The three-variable benchmark is illustrative rather than a new part of this theorem; the analogous small-order full-dimensional case already follows from published earlier work.

## Relationship to prior work

Turvey (2026) proves the unrestricted ranking-law dimension formula \(d(n)=\sum_{j=2}^n\binom nj(j-1)!\) and asks explicitly in Section 6, Problem 2, for \(\dim\mathcal A_{n,k}\) for each atom-support bound \(k\). The result here answers that question at \(k=2,3\) for every \(n\ge4\). In particular, the dimension of each of these bounded-support loci equals its natural mass-parameter count despite possible algebraic dependencies among ranking probabilities.

Babson, Duchin, Iseli, Poggi-Corradini, Thurston and Tucker-Foltz developed the weighted-word and Jacobian/draw-matrix framework for ranking laws, proved a general unrestricted upper bound, and in their Section 5.4 exhibited the word `abcabcba` with draw-matrix rank six. That earlier witness already implies full dimension for three labels with at most three atoms each; it is not claimed as new here. Neither that example nor the unrestricted dimension theorem states the present all-order sharp bounds for exactly two or three atoms. The rank proof here is specialized to short support and uses \(n(k-1)\) distinct single-deviation permutations; it is not a corollary of matching a title or merely of the unrestricted dimension.

## Limitations

This is a semialgebraic **dimension** result only. It does not characterize the full shapes, defining inequalities, connectivity, volume, or boundary of \(\mathcal A_{n,2}\) and \(\mathcal A_{n,3}\); it does not determine the least \(k\) needed to represent every ranking law and does not establish corresponding formulas for \(k\ge4\). It does not assert that the rank map is globally injective or that every law has a unique atomic representation. Historical novelty of a dimension identity can be difficult to certify because equivalent lower-dimensional parameterizations may occur in earlier random-utility literature; the relevant primary works were compared, but an exhaustive historical-priority certification is not claimed.

## References

1. L. Turvey, *Permutations from ranking independent random variables*, arXiv:2610.11895, first posted 2026-10-08. https://arxiv.org/abs/2610.11895. Relevant: §1, Theorem 1.1, §4, §6 Problem 2, Appendix A.
2. E. Babson, M. Duchin, A. Iseli, P. Poggi-Corradini, D. Thurston and J. Tucker-Foltz, *Models of random spanning trees*, arXiv:2407.20226, first posted 2024-07-29; accessible full text https://www.jamie.tuckerfoltz.com/Papers/2026-04-Treehouse/main.pdf. Relevant: §§5.2, 5.4; Theorem 5.13; Lemma 5.16; Proposition 5.17.
3. J. Bochnak, M. Coste and M.-F. Roy, *Real Algebraic Geometry*, Springer, 1998. Standard semialgebraic dimension and polynomial-image principles (see also Turvey Appendix A).
