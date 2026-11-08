# Quartic two-step predecessor law for the checkerboard in cyclic Rule 50

## Finding

Let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be synchronous elementary cellular automaton Rule 50 on an **indexed circular ring**, with all indices taken modulo \(n\), and local rule
\[
(F_n(x))_i=(1-x_i)(x_{i-1}\lor x_{i+1}).
\]
For every integer \(m\ge1\), write \(n=2m\), and let \(c^{(0)}=(01)^m\) and \(c^{(1)}=(10)^m\), with the two possible checkerboard phases treated as separate indexed outputs. Define the two-step predecessor count
\[
a_m=\#\{x\in\{0,1\}^{2m}:F_{2m}^2(x)=c^{(0)}\}.
\]
Then the entire two-step predecessor spectrum over period-dividing-two output configurations is
\[
\#F_{2m}^{-2}(y)=
\begin{cases}
2,&y=0^{2m},\\
0,&y=1^{2m},\\
a_m,&y\in\{c^{(0)},c^{(1)}\}.
\end{cases}
\]
The checkerboard count is characterized exactly by
\[
\sum_{m\ge1}a_m z^m=\frac{z+4z^2+6z^3+4z^4}{1-z-2z^2-2z^3-z^4},
\]
so \(a_1=1\), \(a_2=5\), \(a_3=13\), \(a_4=29\) and
\[
a_m=a_{m-1}+2a_{m-2}+2a_{m-3}+a_{m-4}\qquad(m\ge5).
\]
If \(\rho\) is the unique positive root of \(t^4-t^3-2t^2-2t-1\), then \(\rho=2.316512429\ldots\) and \(a_m\sim\rho^m\). In particular, under a uniform random initial condition, the two-step probability of any one specified checkerboard phase is asymptotic to \((\rho/4)^m\).

## Assumptions and scope

Inputs and outputs are indexed, not identified up to rotation. The map is iterated **twice**, not once. The assertion covers exactly the four output words with spatial period dividing two on each even ring; no claim is made that checkerboards maximize two-step inverse-branching over all outputs. In the length-two case the update uses repeated neighborhood sites, as prescribed by periodic indexing; the theorem includes this boundary case. Here \(F_n^{-2}(y)\) denotes the ordinary set of initial states mapped to \(y\) by \(F_n^2\).

## Proof

**Constant outputs.** No configuration maps to the all-one output: to produce a one at every site would require every input bit to be zero, which instead produces all zeros. Moreover, the only one-step predecessors of the all-zero output are the two constant inputs. Indeed, if an input contains both symbols, some zero is adjacent to a one, and its output bit is one. Thus \(\#F_n^{-2}(0^n)=\#F_n^{-1}(0^n)+\#F_n^{-1}(1^n)=2\), while \(\#F_n^{-2}(1^n)=0\), for any \(n\ge2\).

**Two-step transfer.** For any five input bits \((b_0,b_1,b_2,b_3,b_4)\), let
\[
g(b_0,b_1,b_2,b_3,b_4)=f(f(b_0,b_1,b_2),f(b_1,b_2,b_3),f(b_2,b_3,b_4)),
\]
where \(f(a,b,c)=(1-b)(a\lor c)\). For \(u\in\{0,1\}\), define a \(16\times16\) nonnegative integer matrix \(T_u\), indexed by four-bit states \(s\), as follows. Whenever the five-bit window consists of the four bits of \(s\) followed by \(b\in\{0,1\}\), put one directed edge from \(s\) to the state obtained by shifting left and appending \(b\) in \(T_{g(s,b)}\). This standard de Bruijn construction is exact even at small cyclic lengths, since a closed walk of length \(n\) is in bijection with an indexed cyclic input of length \(n\).

For an output starting with zero and alternating, the number of two-step predecessors is therefore \(\operatorname{tr}((T_0T_1)^m)\). A direct check of the 32 possible five-bit windows gives the following **complete nonzero row list** for \(B=T_0T_1\); entries are destination four-bit states, written as integers from 0 to 15. Every listed edge has multiplicity one.

| Source state | Destination states |
|---|---|
| 0 | 1 |
| 1, 5, 9, 13 | 4, 5, 6, 7 |
| 4, 12 | 0, 1 |
| 7, 15 | 12, 13 |

All other rows vanish. States 9 and 15 have no incoming edges; state 6 has no outgoing edges. Hence none occurs on a closed walk. Restricting to the recurrently relevant states \(\{0,1,4,5,7,12,13\}\), partition them into four classes
\[
A=\{0\},\quad B'=\{1,5,13\},\quad C=\{4,12\},\quad D=\{7\}.
\]
Every source in any given class has exactly one allowed destination in each of the classes indicated by the adjacency matrix
\[
K=\begin{pmatrix}
0&1&0&0\\
0&1&1&1\\
1&1&0&0\\
0&1&1&0
\end{pmatrix},
\]
where the class ordering is \((A,B',C,D)\). Crucially, within each allowed source-class/destination-class pair, the **individual destination state is uniquely specified**, independently of which state in the source class was used: for example, transitions into \(B'\) from \(A,B',C,D\) land at states \(1,5,1,13\), respectively. Consequently every closed class-walk has exactly one lifted closed state-walk (the incoming class transition determines its starting state). Thus for all \(m\ge1\),
\[
a_m=\operatorname{tr}(B^m)=\operatorname{tr}(K^m).
\]
The same count holds for the shifted checkerboard phase by rotation equivariance of \(F_n\).

**Recurrence and growth.** Direct expansion gives
\[
\det(I-zK)=1-z-2z^2-2z^3-z^4.
\]
For a finite square matrix, \(\sum_{m\ge1}\operatorname{tr}(K^m)z^m=-z\,\frac{d}{dz}\log\det(I-zK)\). Substitution yields the displayed rational generating function, first values, and fourth-order recurrence. The characteristic polynomial is \(t^4-t^3-2t^2-2t-1\). Matrix \(K\) is irreducible and aperiodic (it has a loop at \(B'\)), so its Perron eigenvalue is a strictly dominant positive root \(\rho\) of this polynomial. Since the trace is the sum of eigenvalue powers, \(a_m/\rho^m\to1\). This establishes all assertions.

## Verification

The included `check.py` reconstructs the five-bit local table and both 16-state transfer matrices independently from the stated local rule. It checks every row of \(T_0T_1\), the four-state determinant, 40 terms of the recurrence, the first 12 pairs of transfer-matrix traces, and direct exhaustive two-step preimages of all period-dividing-two output patterns at even lengths from 2 through 18. Run with `python3 check.py`; the successful output starts with `VERIFY_OK`. Direct finite tests are checks on the proof, not the basis for extending the result to all lengths.

## Relationship to prior work

Wolfram's original elementary-automaton framework supplies the rule and its standard one-step dynamics. Jen (1989) gives general one-step preimage enumeration for finite spatial blocks, explicitly illustrating Rule 50 using Fibonacci-type terms. Fukś (2003; arXiv reproduction posted 2013) studies the evolution-time sequence of preimages for fixed short blocks on an infinite lattice, including a Rule 50 entry. These are distinct from the present fixed-two-time, growing-even-ring, spatially checkerboard target and its quartic spatial-length law. General de Bruijn methods can in principle be applied to the composed rule; the new content is the particular reduced four-state representation and evaluated exact law, not the transfer-matrix method itself. A search of related published records and accessible prior work did not identify an equivalent evaluated formula. Absence of a search hit is not proof of historical novelty.

## Limitations

The work concerns synchronous Rule 50, exactly two time steps, and targets of spatial period at most two on even indexed rings. No bound on inverse multiplicity for arbitrary output configurations is proved, and no independent mathematical audit has been performed. An earlier presentation of the same evaluated sequence under an equivalent transfer graph or independent-set model may exist beyond the sources inspected; a direct OEIS sequence query was unavailable, and some bibliographic sources were not fully accessible.

## References

1. S. Wolfram, “Statistical mechanics of cellular automata,” *Reviews of Modern Physics* 55 (1983), 601–644. Published July 1, 1983. https://doi.org/10.1103/RevModPhys.55.601
2. E. Jen, “Enumeration of Preimages in Cellular Automata,” *Complex Systems* 3 (1989), 421–456. https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf
3. H. Fukś, “Sequences of Preimages in Elementary Cellular Automata,” *Complex Systems* 14 (2003), 29–43; public preprint https://arxiv.org/abs/1305.6533 (posted May 28, 2013).
