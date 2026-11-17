# Pendant memory creates a threefold wave clock on dyadic sunlet graphs

## Finding

For each integer \(r\ge2\), put \(n=2^r\), and let \(H_n=C_n\odot K_1\) be the sunlet graph with a cycle vertex and one private leaf at each of the \(n\) cycle sites. Let \(q=2^f\) for any integer \(f\ge1\). On the vector space \(\mathbb F_q^{V(H_n)}\times\mathbb F_q^{V(H_n)}\), evolve by the reversible, two-time-level linear wave
\[
T(u,v)=(Au+v,u),
\]
where \(A\) is open-neighbor adjacency over \(\mathbb F_q\). Write \(P_k\) for the number of labelled states of **least positive temporal period** \(k\) under \(T\), starting at time zero.

The exact permutation order is \(3n\). Every state is periodic immediately. The only nonzero populations of primitive periods are
\[
P_1=1,\qquad P_3=q^4-1,
\]
\[
P_{3\cdot2^j}=q^{4\cdot 2^j}-q^{4\cdot2^{j-1}}
\quad (1\le j\le r),
\]
and \(P_k=0\) at every other positive integer \(k\). Equivalently, for \(0\le j\le r\),
\[
\#\operatorname{Fix}(T^{3\cdot 2^j})=q^{4\cdot2^j},
\]
while the only state fixed by an iterate whose time is not divisible by three is zero. The number of distinct temporal orbits of least period \(k\) is \(P_k/k\).

For example, over \(\mathbb F_2\), the eight-vertex sunlet \(H_4\) has 1 fixed state, 15 primitive period-three states, 240 primitive period-six states, and 65,280 primitive period-twelve states. Their sum is \(2^{16}\).

## Assumptions and scope

The cycle is simple; the restriction \(n\ge4\) avoids the non-simple two-cycle. All vertices are labelled, the pendant leaf at cycle site \(i\) is attached only to that site, and no self-loops occur. There are two independent time layers \((u,v)\), so the state space has dimension \(4n\) over \(\mathbb F_q\). Addition is field addition, not Boolean majority. The field has characteristic two, but it need not be the prime field. The theorem is stated for the dyadic circumference \(n=2^r\), not for arbitrary cycle lengths or odd characteristic.

## Proof

**1. A polynomial module for the adjacency operator.** Index the cycle by \(\mathbb Z/n\mathbb Z\) and set
\[
R=\mathbb F_q[z,z^{-1}]/(z^n-1),\qquad c=z+z^{-1}.
\]
The graph's single-time configuration space is \(R^2\), with the first component giving cycle values and the second giving leaf values. Its adjacency matrix, with entries acting on \(R\), is
\[
A=\begin{pmatrix}c&1\\1&0\end{pmatrix}.
\]
It is invertible: \(A(a,b)=(ca+b,a)\), with inverse \((s,t)\mapsto(t,s+ct)\). Direct multiplication gives the key identity
\[
A^2+cA+I=0,\qquad (A+I)^2=cA.
\]
Because \(n=2^r\) and the field has characteristic two,
\[
z^n-1=(z+1)^n,\qquad c=z^{-1}(z+1)^2.
\]
Multiplication by \(c^a\) on \(R\) therefore has kernel of dimension \(\min(2a,n)\), for any positive integer \(a\). In particular, \(\dim\ker c=2\) and \(c^{n/2}=0\).

**2. Reduce the temporal fixed-space problem to the adjacency kernel.** On the two-time-layer space let \(\mathcal A=\operatorname{diag}(A,A)\). The temporal update \(T\) commutes with \(\mathcal A\), and direct composition yields
\[
T^2+\mathcal A T+I=0.
\]
Thus, in characteristic two,
\[
T^3+I=(T+I)(T^2+T+I)=(T+I)(\mathcal A+I)T.
\]
Both \(T\) and \(T+I\) are invertible. The first is invertible with inverse \((s,t)\mapsto(t,s+At)\). For the second, \(T(u,v)=(u,v)\) forces \(v=u\) and \(Au=0\); invertibility of \(A\) gives the zero vector only. Since the field is finite-dimensional, injectivity gives invertibility.

All factors in the expression for \(T^3+I\) commute. Taking dyadic powers and using the Frobenius identity therefore shows
\[
\ker(T^{3\cdot2^j}+I)=\ker((\mathcal A+I)^{2^j})
\qquad(j\ge0).
\]
The plus sign in these formulas is also subtraction in characteristic two.

**3. Compute every required kernel dimension.** At \(j=0\), the equation \((A+I)(a,b)=0\) is equivalent to \(b=a\) and \(ca=0\). Thus \(\dim\ker(A+I)=2\), and the two time layers give
\[
\dim\ker(T^3+I)=4.
\]
For \(j\ge1\), the adjacency identity implies
\[
(A+I)^{2^j}=c^{2^{j-1}}A^{2^{j-1}}.
\]
Since \(A\) is invertible and commutes with scalar multiplication by \(c\), its factor does not affect the kernel. The two graph components and two time layers produce
\[
\dim\ker(T^{3\cdot2^j}+I)
=4\min(2^j,n).
\]
This agrees with the \(j=0\) calculation. For \(0\le j\le r\), it is \(4\cdot2^j\). At \(j=r\) the kernel is the entire \(4n\)-dimensional state space, proving \(T^{3n}=I\).

**4. Exclude all other primitive periods and count states.** Every least period divides \(3n\). If a nonzero state had period not divisible by three, then its period would divide \(n=2^r\); it would be fixed by a dyadic power of \(T\). But
\[
T^{2^j}+I=(T+I)^{2^j}
\]
is invertible for every \(j\ge0\), so only zero can have a period dividing a power of two. The possible nonzero least periods are therefore precisely among \(3,6,\ldots,3n\). Fixed-space cardinality over \(\mathbb F_q\) is \(q\) to its dimension. Subtracting successive nested fixed-point populations gives the displayed \(P_3\) and \(P_{3\cdot2^j}\) formulas. Every one of these differences is strictly positive, so each listed period occurs; the exact permutation order is \(3n\). Invertibility of \(T\) rules out transient states. This proves all assertions.

## Verification

The standalone programs `check_enumeration.py` and `check_ranks.py` use Python's standard library. Execute them with `python check_enumeration.py` and `python check_ranks.py` from the directory containing these files. Their saved expected outputs are `check_enumeration.txt` and `check_ranks.txt`.

The first program computes full orbits for all \(65{,}536\) binary two-time-layer configurations on \(H_4\), independently checking the exact populations. The second constructs adjacency via explicit neighbor lists (not the first script's cyclic bit shifts), forms the binary temporal operator, computes exact Gaussian-elimination ranks for powers, and checks fixed-space dimensions and the sharp order for \(n=4,8,16,32,64\). Its field-rank tests are over \(\mathbb F_2\); the proof's polynomial-module argument, not extrapolation, establishes the result for every \(\mathbb F_{2^f}\) and all dyadic \(n\).

## Relationship to prior work

Second-order reversible cellular automata and matrix representations were studied by Macfarlane (2004). Steeb and Hardy (2007, especially their reversible construction and wave discretization in equations (23)–(27)) describe the two-time-layer mechanism on one-dimensional rings. Those works motivate the present question; their accessible descriptions do not supply the sunlet-graph orbit census. The sunlet graph itself is a standard graph corona, not a new graph. For comparison, the same wave rule on the undecorated dyadic cycle has exact order \(n\): its temporal operator \(W\) satisfies \(W^2+cW+I=0\), hence \(W^n=I\) because \(c^{n/2}=0\), whereas \(W^{n/2}\ne I\) because \(c^{n/4}\ne0\). Attaching one leaf at every cycle vertex therefore changes the global temporal clock by a factor of three. No claim of a general result for arbitrary coronas or all circumferences is made.

## Limitations

The theorem covers dyadic cycle lengths in characteristic two, and the claimed populations concern the complete labelled state space, not spatial-symmetry equivalence classes. It does not classify periodic points at other circumferences, over odd-characteristic fields, or under nonlinear update rules. An available abstract for Macfarlane (2004) does not establish a whole-document noncoverage claim; its full text could not be inspected, leaving a priority risk. A differently named equivalent in other literature cannot be categorically excluded. Finite computations corroborate, but do not replace, the algebraic proof.

## References

1. A. J. Macfarlane, "Linear reversible second-order cellular automata and their first-order matrix equivalents," *Journal of Physics A* **37** (2004), 10791–10814. DOI: 10.1088/0305-4470/37/45/006. Publisher listing identifies 28 October 2004 as its public publication date.
2. W.-H. Steeb and Y. Hardy, "One-Dimensional Cellular Automata, Conservation Laws and Partial Differential Equations," *Zeitschrift für Naturforschung A* **62** (2007), 569–572. DOI: 10.1515/zna-2007-10-1103.
3. E. W. Weisstein, "Sunlet Graph," *MathWorld*, https://mathworld.wolfram.com/SunletGraph.html (graph definition and nomenclature).
