# Eightfold period collapse for a ternary quadratic lag permutation

## Finding

For every integer \(k\ge2\), consider the bijection of \((\mathbb F_3)^k\)
\[
T_k(w_0,\ldots,w_{k-1})=(w_1,\ldots,w_{k-1},\,w_0+w_{k-1}^2).
\]
The eightfold iterate acquires **no fixed points beyond those already fixed by the fourfold iterate**:
\[
\boxed{\operatorname{Fix}(T_k^{8k})=\operatorname{Fix}(T_k^{4k})\qquad(k\ge2).}
\]
Equivalently, no orbit has least period dividing \(8k\) unless its least period also divides \(4k\). In particular, no orbit of least period exactly \(8k\) exists, and a period-doubling from the \(4k\)-short-period sector is impossible. Combining the equality with the known fourfold count gives, for every \(k\ge2\), the exact cardinality
\[
\boxed{\#\operatorname{Fix}(T_k^{8k})=1+4\sum_{\substack{0\le j\le k\\j\equiv3-k\ ({\rm mod}\ 4)}}\binom{k}{j}.}
\]
The first counts at \(k=2,3,\ldots,11\) are \(9,5,17,41,49,145,257,481,1089,1985\). The arithmetic value of the result is the uniform equality of *sets*, not just the count.

## Assumptions and scope

All coordinates and identities are in \(\mathbb F_3=\{0,1,2\}\). An iterate-fixed state corresponds to a bi-infinite periodic sequence satisfying \(x_n=x_{n-k}+x_{n-1}^2\), where \(x^2=1\) for nonzero \(x\in\mathbb F_3\) and \(x^2=0\) otherwise. We write \(b(x)=1_{x\ne0}\). Period dividing \(8k\) is meant literally, including shorter periods; the result makes no assertion about periods not dividing \(8k\).

To encode a column, index its eight entries by \(t\in\mathbb Z/8\mathbb Z\). Its support mask is the binary word \(B(t)=b(y_t)\); a mask has weight \(\sum_t B(t)\). A mask is encoded as the integer \(\sum_{t=0}^7 2^t B(t)\) in the finite certificate. Cyclically rotating a mask is an operation on the row indices only; no identification of distinct original states is made.

## Proof

**1. Difference equation and admissible supports.** The map is a permutation: its previous first coordinate is recovered from the last output coordinate by subtracting the square of the previous last coordinate, now present in the output. Thus a fixed point of \(T_k^{8k}\) corresponds to a doubly infinite period-\(8k\) solution of
\[
x_n-x_{n-k}=b(x_{n-1}).\]
Write its period as \(k\) columns and eight rows:
\[
y_{j,t}=x_{j+tk},\qquad 0\le j<k,\quad t\in\mathbb Z/8\mathbb Z.
\]
Set \(B_j(t)=b(y_{j,t})\) and \((Dy)_t=y_t-y_{t-1}\). For \(1\le j<k\) the equation becomes \(Dy_j=B_{j-1}\); the wrap relation is
\[
(Dy_0)_t=B_{k-1}(t-1).\]
Summing each equation over the rows gives \(\sum_t B_j(t)=0\pmod3\), since every cyclic row difference sums to zero. Therefore every mask has weight \(0,3,\) or \(6\).

If a mask is zero, the subsequent column must be constant. A nonzero constant has weight eight, which is inadmissible, so the subsequent column is zero. The same observation applies through the wrap relation; hence any zero mask forces the entire periodic state to be zero. Consequently it suffices to examine the 84 nonzero masks of weights three or six.

**2. An exhaustive eight-row mask graph.** Define a finite directed graph \(G\) whose 84 vertices are those masks. Put an arrow \(B\to C\) if some word \(y\in\mathbb F_3^8\) satisfies \(Dy=B\) and has support mask \(C\). Given \(B=(b_0,\ldots,b_7)\), there are **exactly three** solutions, because \(\sum b_t=0\pmod3\):
\[
y_0=a,\qquad y_t=a+\sum_{i=1}^t b_i\pmod3\quad(1\le t<8),\qquad a=0,1,2.
\]
The equation at row zero then follows automatically. For each of these three lifts, calculate its support and retain it precisely when its weight is three or six. This is an exhaustive, exact, finite construction with at most \(84\cdot3=252\) trial lifts. It is independently reproduced in the certificate by examining all \(3^8=6561\) ternary words and computing their cyclic differences.

Both constructions give 84 vertices and 96 distinct arrows. Define the four core masks
\[
\mathcal K=\{119,187,221,238\}.
\]
In each, the four support bits in positions \(0,1,2,3\) repeat in positions \(4,5,6,7\), with exactly three ones in each block. Their complete outgoing adjacency lists, encoded by the above integer convention, are:

| Mask | Outgoing neighbors |
|---|---|
| `119` | `221`, `238` |
| `187` | `119`, `238` |
| `221` | `119`, `187` |
| `238` | `187`, `221` |

There are no edges from \(\mathcal K\) into the other 80 vertices. Within those other 80 vertices **there is no directed walk of length three**: the exhaustive enumeration finds 80 directed walks of length two and verifies that none can be extended one more step inside the exterior. It follows that the only directed cycles of \(G\) lie entirely in \(\mathcal K\). These are explicit finite combinatorial facts, certified by the complete standard-library `verify.py` attached with this result. The certificate checks every candidate arrow by two independent constructions and checks all exterior paths, so no random search or unexamined case is involved.

**3. Why the wrap still forces the core.** Let \(\rho\) rotate an eight-row mask by one row. The defining difference equation commutes with \(\rho\), so \(G\) is equivariant under rotation. The ordinary column transitions form a directed path \(B_0\to B_1\to\cdots\to B_{k-1}\). The wrap relation \(Dy_0=\rho B_{k-1}\) gives \(\rho B_{k-1}\to B_0\), equivalently \(B_{k-1}\to\rho^{-1}B_0\). Thus the complete column sequence is a path from \(B_0\) to \(\rho^{-1}B_0\). Repeating its \(\rho^{-1}\)-rotates eight times produces a genuine directed closed walk in \(G\), since \(\rho^8\) is the identity. Every vertex along a finite directed closed walk lies on a directed cycle; hence every \(B_j\) lies in \(\mathcal K\).

**4. Fourfold period collapse.** Every \(B_j\in\mathcal K\) is four-row periodic and has exactly three nonzero entries in each block of four rows. Its successor \(y_{j+1}\) obeys \(Dy_{j+1}=B_j\) (with a row rotation at the wrap), so
\[
y_{j+1,t+4}-y_{j+1,t}=\sum_{i=1}^4 B_j(t+i)=3=0\quad\text{in }\mathbb F_3.
\]
The same holds at the wrap, because row rotations preserve the four-row support pattern and its weight. Therefore \(y_{j,t+4}=y_{j,t}\) for every column and row. The original period-\(8k\) sequence is in fact period-\(4k\), proving \(T_k^{4k}(w)=w\). The reverse inclusion of fixed sets is automatic.

**5. The known fourfold enumeration.** The displayed cardinality follows from the fourfold period theorem in Finch (2026), which counts one zero state plus \(4\sum_{j\equiv3-k\ ({\rm mod}\ 4)}\binom{k}{j}\) nonzero fixed states. This earlier enumeration is *not* claimed as a new result. Equivalently, each nonzero period-\(4k\) word has one zero per column of four rows; a column transitions its unique zero by one or two positions, and the closing shift imposes the displayed binomial congruence.

## Verification

Run `python3 verify.py` using standard Python 3; it has no third-party dependencies. Its two independent finite-graph constructors agree edge for edge, verify the four core adjacency lists, check that the exterior contains no walk of length three, and establish zero-mask isolation. Separately, direct enumeration of all \(3^k\) states for each \(2\le k\le11\) compares the exact fixed-point sets at the fourth and eighth multiples and checks the known binomial formula. The successful reproduced output is:

```
GRAPH_CERTIFICATE_OK nonzero_masks= 84 edges= 96 exterior_length2_walks= 80 cyclic_masks= [119, 187, 221, 238]
DIRECT_CYCLE_CHECK_OK k=2..11 fixed_counts= [9, 5, 17, 41, 49, 145, 257, 481, 1089, 1985] total_states= 265716
CERTIFIED: Fix(T_k^(8k)) = Fix(T_k^(4k)) for every integer k>=2
```

The direct checks at finitely many lags are consistency tests. The proof for arbitrary \(k\) rests on the exhaustive eight-row mask graph and the rotation/column argument, not on extrapolation from the finite direct counts.

## Relationship to prior work

Finch (2026), Proposition 7 and Theorem 8, proves invertibility and the exact number of fixed points at iterate \(4k\). A published refinement enumerates every primitive orbit whose period divides \(4k\). Neither result establishes that these exhaust **all** points fixed at iterate \(8k\), which is the additional assertion here. Separate published fivefold, sixfold, and sevenfold exclusion results prove that various other multiples admit no nonzero fixed states; they do not compare the two nested fixed sets at multipliers four and eight. In particular, an eight-cycle at \(k=2\) is covered by both fixed sets and does not contradict their equality.

The older Cassaigne–Finch work concerns related quadratic recurrences but does not supply an implication for the specific eightfold equality in the inspected material. Search-based nonidentification is not proof of publication priority; an earlier implicit eightfold statement or an uncatalogued proof remains a residual risk.

## Limitations

The collapse applies only to periods dividing \(8k\). Nonzero orbits of other periods may exist, including longer cycles. The result does not classify the full permutation or assert convergence or asymptotic orbit distribution. The eight-row mask certificate is a finite exhaustive proof component, while the universal conclusion requires the explicit reduction from arbitrary \(k\) to that component. The exact fourfold count is previously established. No independent audit of this new argument has been performed.

## References

1. Steven Finch, *Three Quadratic Recurrences Modulo 3: What We Can Prove and What We Can Guess*, arXiv:2610.34300v1 (first public 2026-10-25), Proposition 7 and Theorem 8, https://arxiv.org/abs/2610.34300 .
2. *Exact primitive short-cycle census for a ternary quadratic recurrence*, published 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-primitive-short-cycle-census-for-a-ternary-quadratic-recur--4fc407051b10 .
3. *A universal five-lag forbidden-period law for a ternary quadratic permutation*, published 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-universal-five-lag-forbidden-period-law-for-a-ternary-quadrati--50d142a68b24 .
4. *Universal sixfold and sevenfold fixed-point exclusion for a ternary quadratic permutation*, published 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-universal-sixfold-and-sevenfold-fixed-point-exclusion-for-a-tern--01cf398f7e75 .
5. Julien Cassaigne and Steven R. Finch, *A Class of 1-Additive Sequences and Quadratic Recurrences*, Experimental Mathematics 4 (1995), 49–60, DOI 10.1080/10586458.1995.10504307.
