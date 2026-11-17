# Parity-locked eight- and twelve-step clocks in sequential XOR square bouquets

## Finding

Let \(G_k\) be the graph obtained by identifying one vertex (the hub) in \(k\ge1\) disjoint four-cycles. Perform a repeated one-pass sequential binary self-inclusive neighborhood-parity scan, updating the hub first and then the three remaining vertices of each square in cyclic path order away from the hub. The resulting full-scan bijection \(F_k\) on \(\mathbb F_2^{3k+1}\) has the following **complete linear similarity classification** over \(\mathbb F_2\):

\[
F_k\sim
\begin{cases}
I_2\oplus C(z^2+z+1)\oplus\displaystyle\bigoplus_{j=1}^{k-1}J_3(1),& k\text{ odd},\\[4pt]
J_5(1)\oplus I_2\oplus\displaystyle\bigoplus_{j=1}^{k-2}J_3(1),& k\text{ even}.
\end{cases}
\]

Here \(J_s(1)\) denotes a size-\(s\) unipotent Jordan block, \(C(z^2+z+1)\) is the degree-two companion matrix, and empty direct sums mean the zero-dimensional space. In particular,

\[
\operatorname{ord}(F_k)=
\begin{cases}3,&k=1,\\8,&k\ge2\text{ even},\\12,&k\ge3\text{ odd}.\end{cases}
\]

Thus the primitive-period spectra are \(\{1,3\}\) for one square, \(\{1,2,4,8\}\) for every even number of squares, and \(\{1,2,3,4,6,12\}\) for every odd number of squares at least three.

For every positive integer \(t\), put \(s(t)=2^{\nu_2(t)}\). Then the fixed-space dimension \(f_k(t)=\dim_{\mathbb F_2}\ker(F_k^t-I)\) is

\[
f_k(t)=\begin{cases}
2+2\mathbf1_{3\mid t}+(k-1)\min(3,s(t)),&k\text{ odd},\\
2+\min(5,s(t))+(k-2)\min(3,s(t)),&k\text{ even}.
\end{cases}
\]

Consequently the exact number of labelled states with least temporal period \(d\) and the number of such temporal orbits are

\[
P_d(k)=\sum_{t\mid d}\mu(d/t)2^{f_k(t)},\qquad O_d(k)=P_d(k)/d.
\]

The maximal-period states form exactly one half of all states when \(k\) is even. For odd \(k\ge3\), their fraction is \(3/4-3/2^{k+1}\), which tends to \(3/4\). These statements describe exact finite systems for every \(k\), not asymptotic approximations.

## Assumptions and scope

The simple graph \(G_k\) has hub \(h\) and, for each \(i\in\{1,\dots,k\}\), vertices \(a_i,b_i,c_i\) with exactly the edges \(ha_i,a_ib_i,b_ic_i,c_ih\). No other edges occur. A state assigns one bit to each vertex. Updating a vertex replaces its value by the XOR of its **then-current** value and every then-current neighbor value, leaving all other bits unchanged. One scan updates \(h,a_1,b_1,c_1,\dots,a_k,b_k,c_k\), and the same scan repeats indefinitely. Reordering whole three-site petal blocks after the hub does not change the full map, because local updates on different petals act on disjoint nonhub vertices once the hub has been updated. Claims do not concern the synchronous map, changing the cyclic order within a petal, or arbitrary scans interleaving petals.

A period is the least positive number of full scans returning the *entire labelled state*, and a temporal orbit is a cycle under this scan map. A single local update is an involution (its neighbor bits do not change during that local update), so the full scan is invertible. Every state therefore has transient entry time zero.

## Proof

**1. Exact petal scan.** Write \(x_i=(a_i,b_i,c_i)^T\), \(\ell=(1,0,1)\), and \(v=(1,1,0)^T\), all over \(\mathbb F_2\). Let \(S=\sum_{i=1}^k x_i\). Updating the hub first gives

\[
H=h+\ell S.
\]

Then updating \(a_i,b_i,c_i\) in order gives

\[
a_i'=a_i+b_i+H,\quad b_i'=a_i+c_i+H,\quad c_i'=a_i.
\]

Indeed, at the second update the already-updated \(a_i'\) is used, and at the third the already-updated \(b_i'\) is used, so both cancellations use characteristic two. Hence

\[
x_i'=Ax_i+vH,\quad
A=\begin{pmatrix}1&1&0\\1&0&1\\1&0&0\end{pmatrix}.
\]

Writing \(N=A+I_3\), multiplication gives \(\operatorname{rank}N=2\), \(\operatorname{rank}N^2=1\), and \(N^3=0\). Thus \(A\sim J_3(1)\).

**2. Odd numbers of petals.** Suppose \(k\) is odd. Introduce \(z_i=x_i+x_k\) for \(i<k\), together with the hub \(h\) and sum \(S\). This is an invertible change of coordinates, since \(x_k=S+\sum_{i<k}z_i\). The update equations yield

\[
H=h+\ell S,\qquad S'=AS+vH,\qquad z_i'=Az_i,
\]

because the common \(vH\) contribution appears \(k\) times in the sum and twice in each difference. The four-dimensional \((h,S)\) block is exactly the single-square scan matrix \(B\). Direct multiplication gives \(B^3=I_4\) and \(\dim\ker(B-I_4)=2\). Since \(z^3-1=(z+1)(z^2+z+1)\) has no repeated factor over \(\mathbb F_2\), this implies \(B\sim I_2\oplus C(z^2+z+1)\). The odd-case similarity decomposition follows.

**3. Even numbers of petals.** Suppose \(k\) is even. Let \(y_i=x_i+x_1\) for \(2\le i\le k\) and \(z_i=y_i+y_2\) for \(3\le i\le k\). Define \(Y=\sum_{i=2}^k y_i\). Because \(k\) is even, \(Y=S\). The coordinates \((h,x_1,Y,z_3,\dots,z_k)\) are invertible: \(y_2=Y+\sum_{i=3}^k z_i\), the other \(y_i\) then follow, and \(x_i=y_i+x_1\). Their evolution is

\[
H=h+\ell Y,\qquad x_1'=Ax_1+vH,\qquad Y'=AY,\qquad z_i'=Az_i.
\]

The seven-dimensional \((h,x_1,Y)\) block has the same linear similarity class as the two-square scan matrix \(C\), since for \(k=2\) these are invertible coordinates on its full state space. In its original labelled-site basis \((h,a_1,b_1,c_1,a_2,b_2,c_2)\), \(C\) has binary row strings

```
1101101
1011101
1000101
0100000
1101011
1101000
0000100
```

Direct row reduction of successive powers of \(C+I_7\) gives ranks \(4,3,2,1,0\) for exponents \(1,2,3,4,5\). These ranks force exactly one unipotent Jordan block of size five and two blocks of size one: \(C\sim J_5(1)\oplus I_2\). This proves the even-case decomposition for all \(k\).

**4. Exact periods and counts.** In characteristic two, \(J_s(1)=I+N\) with nilpotent \(N\) has order the least power of two not smaller than \(s\). Moreover \(\ker(J_s(1)^t-I)\) has dimension \(\min(s,2^{\nu_2(t)})\), since the odd part of \(t\) contributes an invertible polynomial in \(N\). The quadratic companion summand has order three and contributes zero fixed dimensions unless \(3\mid t\), when it contributes two. Summing the direct-summand dimensions gives the displayed \(f_k(t)\), and the largest block orders give exactly the stated global orders. Because \(\#\operatorname{Fix}(F_k^t)=2^{f_k(t)}\), Möbius inversion yields the primitive state counts and division by \(d\) gives distinct cycles. All periods listed occur: their \(P_d(k)\) are positive by direct substitution, while the global order excludes all others.

For even \(k\), subtracting the fixed states of \(F_k^4\) from all \(2^{3k+1}\) states gives \(P_8(k)=2^{3k}\). For odd \(k\ge3\), inclusion-exclusion over proper divisors of twelve gives \(P_{12}(k)=3\cdot2^{3k-1}-3\cdot2^{2k}\), yielding the claimed fractions.

## Verification

The standalone standard-library program `verify_matrices.py` constructs the exact full-scan linear matrices; checks the size-three, quadratic-plus-fixed, and size-five-plus-two-fixed base decompositions; and compares the nullity of every power through the predicted global order for \(k=1,\dots,12\). A separately implemented microscopic vertex-update simulator, `verify_states.py`, exhaustively follows all \(16+128+1024+8192+65536=74{,}896\) labelled initial states for \(k=1,\dots,5\), comparing every least-period count to Möbius inversion. Its updates use adjacency masks and in-place bit flips rather than the derived matrix formula. The recorded outputs are in `verification_output.txt`. Both programs run with Python 3 without third-party dependencies; from the directory containing the files run `python3 verify_matrices.py` and `python3 verify_states.py`. These finite verifications supplement, but do not replace, the all-parameter algebraic proof.

## Relationship to prior work

Macauley and Mortveit, *Cycle Equivalence of Graph Dynamical Systems* (arXiv:0802.4412), establish equivalence phenomena for general sequential graph dynamical systems and acyclic orientations, but not this precise fixed-power census or the parity-dependent square-bouquet normal form. Macauley, McCammond and Mortveit, *Dynamics Groups of Asynchronous Cellular Automata* (arXiv:0808.1238), analyze Rule 150 on **single cycles** through its generated dynamics group; the linked-squares hub coupling here is not a single cycle and the global group result does not imply the derived two-case Jordan decompositions. Defant, *Flexible Toggles and Symmetric Invertible Asynchronous Elementary Cellular Automata* (arXiv:1511.06966), studies in particular the Rule 150 identity scan on a **single binary ring**. Its periodic-point formulas do not cover hub-glued squares.

For further scope comparison, the published study *Scan-order phase diagram and exact Rule 150 cycle census on binary rings* (2026) gives an arbitrary-scan classification on a single cycle. The published *Exact recurrent-orbit census for majority dynamics on bouquets of squares* and *Uniform six-step entrance and exact excitation waves on bouquets of squares* use this graph family but different local rules (synchronous majority and three-state excitable updates, respectively). Matching graph names or local-rule names alone is not statement coverage. No inspected source provides the displayed direct-sum classification on \(G_k\).

## Limitations

Only the stated deterministic **hub-first** simple scan and binary self-inclusive XOR rule are classified. Arbitrary permutations, synchronous neighbor-parity dynamics, other finite fields, and mixed petal lengths are not covered. The computational checks cover finitely many dimensions, not an independent verification of all \(k\). The literature comparisons are evidence of a gap, not a proof of absolute historical priority: differently described or inaccessible prior work might establish an equivalent theorem. No independent mathematical audit was conducted.

## References

- Matthew Macauley and Henning S. Mortveit, *Cycle Equivalence of Graph Dynamical Systems*, arXiv:0802.4412, first submitted 2008-02-29. Accessible paper: https://www.math.clemson.edu/~macaule/papers/CycleEquivalence_Nonlinearity.pdf
- Matthew Macauley, Jon McCammond and Henning S. Mortveit, *Dynamics Groups of Asynchronous Cellular Automata*, arXiv:0808.1238, first submitted 2008-08-08. https://arxiv.org/pdf/0808.1238
- Colin Defant, *Flexible Toggles and Symmetric Invertible Asynchronous Elementary Cellular Automata*, arXiv:1511.06966, first submitted 2015-11-22. https://arxiv.org/pdf/1511.06966
- *Scan-order phase diagram and exact Rule 150 cycle census on binary rings*, public mathematical research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-scan-order-phase-diagram-and-exact-rule-150-cycle-census-on-bina--a8edc73752da
- *Exact recurrent-orbit census for majority dynamics on bouquets of squares*, public mathematical research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-recurrent-orbit-census-for-majority-dynamics-on-bouquets-o--a6794acbe334
- *Uniform six-step entrance and exact excitation waves on bouquets of squares*, public mathematical research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-uniform-six-step-entrance-and-exact-excitation-waves-on-bouquets--15a728a38ba4
