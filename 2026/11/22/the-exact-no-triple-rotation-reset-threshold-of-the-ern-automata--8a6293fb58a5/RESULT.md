# The exact no-triple-rotation reset threshold of the Černý automata

## Finding

For every integer \(n\ge3\), let \(C_n\) be the deterministic automaton with states \(Q=\{0,\ldots,n-1\}\), cyclic letter \(a:i\mapsto i+1\pmod n\), and idempotent letter \(b\) mapping \(n-1\) to \(0\) while fixing all other states. A *reset word* maps \(Q\) to one state; it is *run-constrained* here if it does not contain the contiguous factor `aaa`. The exact minimum length of a run-constrained reset word is

\[
L_n=\left\lfloor\frac{3n^2-8n+6}{2}\right\rfloor.
\]

The result gives the **shortest length**, not merely an existence guarantee for words with rotation runs of length at most two. An explicit quadratic-length optimal word is constructible by the algorithm below for every \(n\). The formula starts \(4,11,20,33,48,67,88,113\) at \(n=3,\ldots,10\).

## Assumptions and scope

Letters are applied from left to right. All words are finite over \(\{a,b\}\); the constraint concerns consecutive occurrences of \(a\), not total occurrences. The automaton has \(n\ge3\) states; no assertion is made about arbitrary synchronizing automata, other forbidden factors, or unconstrained reset lengths.

A shortest constrained reset word may be assumed to begin with `b`, end with `b`, and have one or two `a` letters between successive `b` letters. Indeed, initial rotations leave \(Q\) invariant, repeated `b` letters are redundant because \(b^2=b\), and terminal rotations cannot cause a new rank decrease. Deleting these redundant portions does not introduce `aaa`. Moreover, the final letter `b` in a shortest reset word effects the final rank decrease, so its unique image is \(0\).

Set \(N=n-1\). The initial `b` changes the current image into \(S=\{0,\ldots,N-1\}\). Every subsequent block is either `ab` or `aab`; both preserve \(S\) as a universe. Write \(A=ab\) and \(B=aab\), with respective costs \(2\) and \(3\). Their transformations of \(S=\mathbb Z/N\mathbb Z\) are

\[
A(i)=i+1\pmod N,\qquad
B(i)=\begin{cases}
i+2,&0\le i\le N-3,\\
0,&i=N-2\text{ or }i=N-1.
\end{cases}
\]

Thus it is enough to optimize over block words \(\{A,B\}^*\) sending \(S\) to \(\{0\}\), with the cost of the compulsory initial `b` added afterward.

## Proof

**Step 1: interval invariance under full inverse images.** For \(1\le w\le N\) and \(0\le r<N\), define the cyclic interval

\[
I(w,r)=\{r-w+1,r-w+2,\ldots,r\}\pmod N.
\]

Work *backward* from the final image \(I(1,0)=\{0\}\), taking full set-theoretic preimages. For \(w<N\), the inverse of \(A\) sends \(I(w,r)\) to \(I(w,r-1)\) (endpoints modulo \(N\)). The full inverse of \(B\) has precisely the following possibilities:

- If \(r=0\), it gives \(I(w+1,N-1)\), enlarging the interval by one.
- If \(r=w\), it has size \(w-1\), with endpoint \(r-2\). For \(w=1\) it is empty and is inadmissible.
- Otherwise it gives \(I(w,r-2)\), with unchanged size.

All expressions with endpoints are interpreted modulo \(N\). In particular, **every nonempty preimage of a cyclic interval is a cyclic interval**. Once the full interval \(I(N,r)=S\) is reached, the reverse process can stop at zero additional cost. A block word resets \(S\) to \(\{0\}\) precisely when its full reverse preimage of \(\{0\}\) contains all of \(S\), i.e., equals \(S\).

**Step 2: a sharp cost potential.** For \(1\le w<N\) and \(0\le r<N\), set

\[
g_w(r)=\left\lceil\frac{3r}{2}\right\rceil+
\mathbf 1_{\{r\ \mathrm{even},\ w\ \mathrm{even},\ 2\le w\le r\}}.
\]

For \(r\ge1\), the direct parity check gives

\[
g_w(r)=\min\bigl(2+g_w(r-1),\ 
3+g_w(r-2)\ \text{if }r\ge2\text{ and }r\ne w\bigr),
\]

where an unavailable second term is omitted, and \(g_w(0)=0\). For example, the extra unit at even \(r\ge w\) with even \(w\) compensates for the inadmissible shrinking \(B^{-1}\) step at \(r=w\). Consequently, there is a width-preserving sequence of backward \(A^{-1}\) and \(B^{-1}\) steps taking \(I(w,r)\) to \(I(w,0)\) at exact cost \(g_w(r)\), always decreasing the representative endpoint \(r\) by one or two, never invoking the shrinking case.

Define \(H_N=0\), and, for \(1\le w<N\), recursively

\[
H_w=3+g_w(N-1)+H_{w+1}.
\]

Use the potential \(F(N,r)=0\) and \(F(w,r)=g_w(r)+3+H_{w+1}\) for \(w<N\). We claim that on **every** nonempty inverse transition \(I(w,r)\to I(v,s)\) of block cost \(c\in\{2,3\}\),

\[
F(w,r)\le c+F(v,s).
\]

When an inverse transition preserves width and decreases the representative endpoint without wrap, this follows from the displayed recurrence for \(g_w\). A wrapped inverse step has strictly larger nonnegative right-hand potential, so it cannot violate the inequality. A growth step occurs only at \(r=0\); it has cost \(3\) and yields equality \(F(w,0)=3+F(w+1,N-1)\), including growth into full width. A shrinking step occurs only at \(r=w\ge2\). As \(g_w\) is nondecreasing and \(w\le N-1\), we have

\[
F(w,w)=g_w(w)+3+H_{w+1}\le H_w,
\]

whereas its destination potential is at least \(3+H_w\), so the inequality again holds. These four cases exhaust the inverse edges. Summing the potential inequalities along any backward path from \(I(1,0)\) to \(S\) proves a lower bound of \(F(1,0)\) for its total block cost.

**Step 3: attainment.** Begin at \(I(1,0)\). At endpoint \(r=0\), take the inverse \(B\) step, which increases width and sets endpoint \(N-1\). At each intermediate width \(2\le w<N\), follow the exact-cost \(g_w(N-1)\) endpoint-decreasing steps of Step 2 until the endpoint reaches \(0\), then take the next growth step. Repeat until the width is \(N\). Every step is a valid nonempty inverse transition, so the total cost is exactly \(F(1,0)\). Reverse the ordered inverse blocks to obtain a forward block word, replace \(A\) with `ab` and \(B\) with `aab`, and prepend `b`. The resulting literal word contains no `aaa` and resets \(Q\), proving the lower bound is sharp.

**Step 4: evaluation.** Put \(d=N-1=n-2\). From Step 3, counting the initial `b`, all \(d\) growth steps and all intermediate width adjustments,

\[
L_n=1+3d+\sum_{w=2}^{d}g_w(d)
=1+3d+(d-1)\left\lceil\frac{3d}{2}\right\rceil
+\begin{cases}\lfloor d/2\rfloor,&d\ \mathrm{even},\\0,&d\ \mathrm{odd}.\end{cases}
\]

Elementary parity simplification gives \(L_n=\lfloor(3n^2-8n+6)/2\rfloor\), as claimed. The case \(n=3\) is included: the intermediate sum is empty and the optimal word is `baab`.

## Verification

Two self-contained Python standard-library programs accompany this result:

- `verify_full_bfs.py` explores the **literal** constrained power automaton, storing both the occupied-state subset and the current run length of `a`. It obtains exact shortest lengths for all \(3\le n\le14\) without using the interval theorem.
- `verify_interval.py` independently constructs full inverse interval images, solves their weighted shortest path problems for \(3\le n\le35\), checks the potential inequality on all inverse edges for \(3\le n\le80\), and constructs and simulates optimal admissible words for \(3\le n\le150\).

Each program can be run directly with Python 3, independently of the other, in the same directory as this document. The checks are finite corroboration; **the all-order guarantee rests on the proof above**, not the finite computations.

## Relationship to prior work

Constrained synchronization for regular languages was developed in Fernau, Gusev, Hoffmann, Holzer, Volkov and Wolf (2019), and complexity results specifically for binary automata with simple idempotents, including the Černý family, appear in Hoffmann (2021). Both address decidability/complexity and structure of allowed reset languages, not the optimal length for the precise `aaa`-avoidance constraint in this theorem.

The standard unrestricted Černý shortest-reset problem has optimum \((n-1)^2\). Existing results on the minimum permitted maximum rotation-run (two for this same family) establish *feasibility* of this constraint, not the sharp constrained minimum word length. Published classifications of the inverse-extension length of a *single* subset and of early-rank compression address different objectives; the former does not optimize a complete inverse-extension path under weighted `ab`/`aab` blocks, and the latter only covers initial rank reductions. Neither gives this full constrained reset length. The published coordinatewise positive-weight optimum is also distinct: its unique unrestricted minimizing word has long rotation runs and is not `aaa`-free when \(n\ge4\). No priority is claimed for those foundational facts.

## Limitations

This theorem applies to a fixed explicit automaton family and the single exact forbidden factor `aaa`, with unit cost per input letter. Different forbidden patterns, weighted inputs, or arbitrary defect-one circular automata are outside its scope. The originality comparison checked accessible primary papers and indexed related records; equivalence to unindexed historical work cannot be categorically excluded.

## References

1. H. Fernau, V. V. Gusev, S. Hoffmann, M. Holzer, M. V. Volkov, P. Wolf, *Computational Complexity of Synchronization under Regular Constraints*, MFCS 2019, Article 63, DOI: [10.4230/LIPIcs.MFCS.2019.63](https://doi.org/10.4230/LIPIcs.MFCS.2019.63).
2. S. Hoffmann, *Constrained Synchronization for Commutative Automata and Automata with Simple Idempotents*, arXiv:2109.02743v1, first public September 6, 2021, [arXiv PDF](https://arxiv.org/pdf/2109.02743).
3. *Uniform weighted-reset optimality in the Černý automata*, published mathematical record, [complete result](https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-uniform-weighted-reset-optimality-in-the-ern-automata--6527a70965c4).
4. *A mandatory reset subsequence and exact one-step multiplicity for the Černý automata*, published mathematical record, [complete result](https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-a-mandatory-reset-subsequence-and-exact-one-step-multiplicity-fo--8a725fd1702c).
5. *Exact inverse-extension lengths and their distribution in the Černý automata*, published mathematical record, [complete result](https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-inverse-extension-lengths-and-their-distribution-in-the-er--784204d15f86).
6. *Exact early deficiency profile of the Černý automata*, published mathematical record, [complete result](https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-early-deficiency-profile-of-the-ern-automata--766d362d36d3).
