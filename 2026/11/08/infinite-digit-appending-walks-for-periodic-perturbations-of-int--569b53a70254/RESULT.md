# Infinite digit-appending walks for periodic perturbations of integer powers

## Finding

Consider any integers \(A,B\ge2\) and a periodic integer-valued sequence \((c_n)_{n\ge0}\) of positive period \(h\). Set \(u_n=A^n+c_n\) and \(C=\max_{0\le i<h}|c_i|\). A base-\(B\) digit-appending step from an eventually positive term \(u_m\) to \(u_{m+k}\) means
\[
u_{m+k}=B^t u_m+d,\qquad k,t\in\mathbb Z_{\ge1},\quad 0\le d<B^t.
\]
A walk consists of such steps with strictly increasing indices; the number \(t\) of digits appended at a step is unrestricted.

**Theorem (dependent-base periodic-offset classification).** Suppose \(A\) and \(B\) are multiplicatively dependent. There exists an integer \(M\) such that, for every \(m\ge M\):

1. Every digit-appending step from \(u_m\), *regardless of its appended digit length*, satisfies \(A^k=B^t\), and its exact admissibility criterion is
\[
c_m=\left\lfloor\frac{c_{m+k}}{B^t}\right\rfloor.
\]
2. An infinite walk starts at \(u_m\) **if and only if** \(c_m\in\{0,-1\}\). Such a walk can always use the same digit and index lengths at every step.
3. If \(c_m\notin\{0,-1\}\), every walk starting at \(u_m\) has **at most** \(\lfloor\log_2 C\rfloor\) edges when \(C\ge2\), and zero edges when \(C\le1\).

The bound in item 3 is optimal at every integral logarithmic scale: for every integer \(L\ge0\), there are such sequences with \(C=2^L\) and walks having exactly \(L\) edges from arbitrarily large nonterminal starting indices. In particular, the natural density of starting indices admitting infinite walks in the dependent case is exactly
\[
\frac{\#\{0\le i<h:c_i\in\{0,-1\}\}}{h}.
\]

For comparison, when \(A\) and \(B\) are multiplicatively independent, the published theorem of Mosahab–Boyyakar–Bruda–Kominers–Miller implies that every sufficiently large term \(u_m\) begins an infinite walk with unrestricted appended digit lengths. **This independent-base statement is prior work, not a new theorem.**

## Assumptions and scope

All parameters \(A,B\) are fixed integers at least two. The periodic offsets \(c_n\) may be positive, zero, or negative and are bounded by \(C\); the terms \(u_n\) are automatically positive and strictly increasing for all sufficiently large indices. A multiplicative dependence means \(A^a=B^b\) for some positive integers \(a,b\). No bound is imposed on \(k\) or \(t\). The threshold \(M\) can be any integer such that \(A^m>4C+2\) and the terms are positive and strictly increasing for all \(m\ge M\). This is a tail classification, not a claim about a fixed finite prefix.

## Proof

**Uniform resonance without a digit-length cap.** Since \(A\) and \(B\) are multiplicatively dependent positive integers, comparison of their prime-exponent vectors gives an integer \(g\ge2\) and positive integers \(a,b\) such that \(A=g^a\), \(B=g^b\). For every pair of positive integers \(k,t\), either \(A^k=B^t\) or
\[
\left|\frac{A^k}{B^t}-1\right|=|g^{ak-bt}-1|\ge\frac12.
\]
Rearranging a digit-appending step gives
\[
A^m\left(\frac{A^k}{B^t}-1\right)
=c_m+\frac{d-c_{m+k}}{B^t}.
\]
The right side has absolute value at most \(2C+1\) because \(0\le d<B^t\) and \(|c_i|\le C\). If \(m\ge M\) with \(A^m>4C+2\), the left side would exceed \(2C+1\) in absolute value unless \(A^k=B^t\). Thus all sufficiently late steps are exactly resonant, even when \(t\) and \(k\) are unbounded.

In the resonant case, the digit condition becomes
\[
0\le c_{m+k}-B^t c_m<B^t,
\]
which is equivalent, for integer offsets, to \(c_m=\lfloor c_{m+k}/B^t\rfloor\).

**Obstructions and maximal walk length.** If \(c_m\ge1\), the last display implies \(c_{m+k}\ge B^t c_m\ge2c_m\). Thus every further step doubles the positive offset, which never enters \(\{0,-1\}\). After \(j\) edges, the resulting offset is at least \(2^j\), while it is at most \(C\). Consequently \(j\le\lfloor\log_2 C\rfloor\).

If \(c_m\le-2\), put \(r_m=-c_m-1\ge1\). The same digit condition implies
\[
c_{m+k}\le B^t(c_m+1)-1,\qquad
r_{m+k}\ge B^t r_m\ge2r_m.
\]
Again the offset can never enter \(\{0,-1\}\); also \(r_n\le C-1\), so any such walk has at most \(\lfloor\log_2(C-1)\rfloor\) edges when \(C\ge2\). If \(C\le1\) no nonterminal offset can support even one step. This proves the upper bounds and nonexistence of infinite walks for nonterminal offsets.

**Constructive infinite walks.** Write \(A=g^a\) and \(B=g^b\) as above. Choose \(k=bh\) and \(t=ah\), so \(A^k=B^t\) and the period ensures \(c_{m+k}=c_m\). If \(c_m=0\), the required appended block has value \(d=0\). If \(c_m=-1\), it has value \(d=B^t-1\). Both lie in the permitted interval; repeating this fixed step gives an infinite walk from each sufficiently large index with either offset. Exactly one of the terminal and nonterminal cases holds for every index. Periodicity gives the claimed natural density.

**Sharpness.** For arbitrary \(L\ge0\), take \(A=B=2\), period \(h=L+1\), and \(c_i=2^i\) for \(0\le i\le L\), extended periodically. Here \(C=2^L\). From any sufficiently large index divisible by \(h\), the next \(L\) consecutive steps have \(k=t=1\), \(d=0\), since successive offsets double. The general bound forbids a longer walk. This attains \(\lfloor\log_2 C\rfloor=L\), including the zero-edge case.

**Context for independent bases.** A periodic integer sequence satisfies a linear recurrence with characteristic divisor \(X^h-1\). Hence \(u_n=A^n+c_n\) satisfies a recurrence whose unique simple dominant characteristic root is \(A\). The independent-root existence theorem (Theorem 1.3 of the cited 2026 paper) therefore applies exactly to this family; no new argument for that branch is asserted here.

## Verification

The standalone script `verify.py` computes digit-appending equations with exact Python integers for eight dependent-base configurations, including different resonant exponent ratios and positive and negative periodic offsets. It checks \(32{,}256\) finite step candidates, of which \(230\) are admissible; every admitted step is resonant and satisfies the floor criterion. It checks the finite-state obstruction and the sharp examples for \(0\le L\le11\). Execute `python3 verify.py` with the standard library. This is corroboration of the algebraic proof, not a proof by bounded enumeration.

## Relationship to prior work

Mosahab, Boyyakar, Bruda, Kominers, and Miller (arXiv:2610.18919v1, first posted October 12, 2026) establish a general resonance statement only **when appended digit length is bounded** (Theorem 1.2), existence for multiplicatively independent dominant root and unrestricted lengths (Theorem 1.3), and two opposite dependent-root examples \(B^n-1\) (Example 1.1) and \(B^n+1\) (Example 3.3). The classification above concerns a whole family of *dependent-root* periodic perturbations, gives resonance uniformly over **all** appended lengths, identifies every infinite-walk starting residue, and provides a sharp length bound for all remaining starts. The two earlier examples are special cases and are not separately claimed as novel.

Kominers (arXiv:2512.06446, 2025) develops bounded-digit-length termination estimates for Fibonacci and certain Lucas recurrences, whose dominant roots do not instantiate this dependent-base periodic-power family. Banks and Luca (2005) treat concatenation of *recurrence terms* into another term, not arbitrary appended digits in an iterated walk; their rank hypothesis does not cover the dependent-base examples here. None of these cited papers is claimed to prove the new dependent-base classification.

## Limitations

The theorem concerns eventual behavior, not exceptional low indices. It assumes an integer pure power plus bounded periodic *integer* offset; no conclusion is asserted for arbitrary lower-order exponential, quasiperiodic, or polynomial perturbations. The independent-base conclusion is quoted from an earlier theorem. No independent mathematical audit or priority certification has been performed; overlapping work not located by the searches could exist.

## References

1. Arya Mosahab, Sahitya Boyyakar, Glenn Bruda, Scott Duke Kominers, and Steven J. Miller, *On Digit-Appending Walks Along Linear Recurrences*, arXiv:2610.18919v1, October 12, 2026. https://arxiv.org/abs/2610.18919 .
2. Scott Duke Kominers, *Uniform Bounds for Digit-Appending Fibonacci Walks*, arXiv:2512.06446v1, December 6, 2025. https://arxiv.org/abs/2512.06446 .
3. William D. Banks and Florian Luca, *Concatenations with Binary Recurrent Sequences*, Journal of Integer Sequences 8 (2005), Article 05.1.3. https://cs.uwaterloo.ca/journals/JIS/VOL8/Banks/banks81.pdf .
