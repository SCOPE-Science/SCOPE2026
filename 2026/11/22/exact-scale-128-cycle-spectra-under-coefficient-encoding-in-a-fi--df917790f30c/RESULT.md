# Exact scale-128 cycle spectra under coefficient encoding in a fixed-point-free four-branch map

## Finding

The García-Grimaldo–Campos-Cantón piecewise-affine map studied in a 2023 fixed-point hardware implementation experiment has markedly different *complete finite-state recurrent structures* depending on whether its outer multiplier is kept exact until state rounding or first encoded on a seven-fractional-bit grid. These are two deliberately specified numerical dynamical systems, not undocumented claims about a hardware pipeline.

On the complete \(6401\)-state scale-128 grid, the exact-multiplier and encoded-multiplier maps have, respectively, **two** and **six** recurrent cycles. Counting a cycle by its least period and its whole-state basin size gives

\[
\begin{aligned}
A:&\quad(34,238),\ (40,6163),\\
B:&\quad(8,68),\ (20,2830),\ (24,253),\ (24,442),\ (28,1404),\ (28,1404).
\end{aligned}
\]

The longest preperiods are \(107\) and \(80\), respectively. Precisely \(5122\) of the \(6401\) states have different immediate successors. No transient or recurrent state is omitted from the basin counts.

## Assumptions and scope

Let \(I=[-25,25]\) and define the discontinuous four-branch map

\[
F(x)=\begin{cases}
\frac45 x+4,&-25\le x\le-5,\\
5x+25,&-5<x<0,\\
5x-25,&0\le x<5,\\
\frac45 x-4,&5\le x\le25.
\end{cases}
\]

Its control values \((4/5,5,4,25)\) are those in the cited source's chaotic example. Use the finite set \(S=\{i/128:i\in\mathbb Z,-3200\le i\le3200\}\) and \(R(u)=k/128\), where \(k\) is the nearest integer to \(128u\), resolving exact half-integer ties by choosing even \(k\). Define \(A(x)=R(F(x))\). Define \(F_q\) by replacing only the two occurrences of outer slope \(4/5\) by its nearest scale-128 representation \(51/64=102/128\); the branch cuts remain \(\pm5\), and the affine constants remain exactly \(\pm4,\pm25\). Define \(B(x)=R(F_q(x))\). Both act on all of \(S\).

The two definitions specify idealized **per-iterate nearest-even state rounding**, without intermediate truncation. In particular, \(B\) need not reproduce any vendor's multiplier or saturation behavior, and the comparison is about coefficient encoding, not a comparison of different algebraic evaluation orders.

## Proof

Encode a state \(x=i/128\) as its signed integer \(i\), from \(-3200\) to \(3200\) inclusive. Let \(Q(n,d)\) denote the integer closest to the rational \(n/d\), ties to even. The two successor functions in signed-integer coordinates are

\[
T_A(i)=\begin{cases}
Q(4i,5)+512,&i\le-640,\\
5i+3200,&-640<i<0,\\
5i-3200,&0\le i<640,\\
Q(4i,5)-512,&i\ge640,
\end{cases}
\]

and \(T_B\) is the same formula with \(Q(4i,5)\) replaced by \(Q(51i,64)\) on the outer branches. The integer constants arise from exact shifts by \(4\) and \(25\) before multiplying by \(128\). The formulas follow directly from the map definitions, including each boundary convention.

Every output remains in \([-3200,3200]\): the inner branches take values strictly between \(-3200\) and \(3200\) except the right branch at \(i=0\), where the output is \(-3200\); the outer branches lie between \(-2048\) and \(0\) on the left and between \(0\) and \(2048\) on the right for \(A\), with the encoded-slope outer values also strictly within the state interval. Therefore each formula induces a deterministic directed graph on exactly \(6401\) vertices.

The attached standalone Python certificate `verify_cycles.py` exhaustively creates all graph edges by integer division, with no floating-point operations. It independently reconstructs every edge by evaluating the four rational expressions through Python's exact `Fraction` type and nearest-even integer rounding. Two independent algorithms then produce the complete graph invariants: (i) elimination of indegree-zero vertices followed by direct cycle enumeration and reverse propagation of basin identities and preperiod depths, and (ii) a fresh repeated-vertex search from *each* of the 6401 initial states, grouping identical cycle vertex sets. Both produce the period/basin pairs and maximum preperiods shown above, and an exact edge-by-edge comparison gives \(5122\) changed successors.

These procedures are exhaustive finite verifications; they assert nothing about the recurrence structure of the exact-real map on infinitely many starting states or other grid scales.

## Verification

Run `python3 verify_cycles.py` in any Python 3 installation with the standard library. Its final line is `PASS` only after asserting the prescribed tables, exact equality of integer and rational successor evaluations for every state, agreement of both global decompositions, and the changed-edge count. It does not require input files, third-party packages, random seeds, or a network connection. The exact quotient/tie rule for negative and positive integer numerators is implemented explicitly.

## Relationship to prior work

García-Grimaldo and Campos-Cantón (2021) introduced this four-branch family and studied exact-real fixed points and chaotic dynamics. García-Grimaldo and collaborators (2023) investigated fixed-point arithmetic implementations, specifically reported discrepancies in 16-bit trajectories at the same chaotic parameters, and compared simulated time series and histograms across implementation widths. Their results motivate the complete finite-state invariant computed here but do not provide its exact two-model cycle/basin census. Previously reported exact-real analyses of the same map's Lyapunov bounds, period-three orbits, and attracting resonance windows concern real trajectories rather than the 6401-state rounded graph. Other finite-precision exact cycle censuses concern different maps.

## Limitations

The result describes exactly the two written idealized semantics; there is no assertion of equivalence to the published FPGA implementation's operator order, parameter storage, rounding, overflow, or truncation. The 2021 originating article was accessible only in publisher preview, so a complete-text comparison remains a publication-priority limitation. An exhaustive finite-state computation supplies no claim about entropy, cryptographic security, or infinite-precision recurrence. Mathematical assertions are subject to independent validation.

## References

1. C. García-Grimaldo and E. Campos-Cantón, *Chaotic Features of a Class of Discrete Maps without Fixed Points*, International Journal of Bifurcation and Chaos **31** (2021), 2150200. DOI: https://doi.org/10.1142/S021812742150200X.
2. C. García-Grimaldo, C. F. Bermudez-Marquez, E. Tlelo-Cuautle, and E. Campos-Cantón, *FPGA Implementation of a Chaotic Map with No Fixed Point*, Electronics **12** (2023), 444. DOI: https://doi.org/10.3390/electronics12020444.
