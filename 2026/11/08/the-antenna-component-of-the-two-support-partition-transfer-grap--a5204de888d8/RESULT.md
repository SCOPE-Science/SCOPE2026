# The antenna component of the two-support partition-transfer graph

## Finding

Let \(G_n\) be the graph whose vertices are integer partitions of \(n\), with two partitions adjacent when a single unit is moved from one part to another part, or from one part to a newly created part of size one, followed by reordering. Write \(\sigma(\lambda)\) for the number of distinct positive part sizes of \(\lambda\), and let \(G_n^{[2]}\) be the induced graph on partitions with \(\sigma(\lambda)=2\).

**Theorem.** For every integer \(n\geq3\), the connected component of \(G_n^{[2]}\) containing \((n-1,1)\) has precisely the following vertices. Write \(1^q\) and \(2^p\) for repeated parts, and define

\[
\begin{aligned}
H_n&=\{(a,1^{n-a}):2\leq a\leq n-1\},\\
T_n&=\{(n-k,k):1\leq k\leq\lfloor(n-1)/2\rfloor\},\\
U_n&=\{(2^p,1^{n-2p}):1\leq p\leq\lfloor(n-1)/2\rfloor\}.
\end{aligned}
\]

For even \(n\geq4\), the component is \(H_n\cup T_n\cup U_n\). For odd \(n\geq7\), the component is

\[
H_n\cup T_n\cup U_n\cup\left\{\left(\left(\frac{n-1}{2}\right)^2,1\right),\;\left(3,2^{(n-3)/2}\right)\right\}.
\]

For \(n=3,5\), the component is \(H_n\cup T_n\cup U_n\), without additional vertices. Its exact order is

\[
|C_n|=\begin{cases}
1,&n=3,\\
5,&n=5,\\
2n-6,&n\geq4\text{ even},\\
2n-3,&n\geq7\text{ odd}.
\end{cases}
\]

Consequently, **\(G_n^{[2]}\) is connected if and only if \(3\leq n\leq7\)**. For every \(n\geq8\), the vertex \((n-4,2,2)\) lies outside \(C_n\).

## Assumptions and scope

All partitions are **unlabelled integer partitions**, represented as nonincreasing finite lists of positive integers. A transfer must have distinct donor and recipient rows; a newly created recipient row is permitted. Equal resulting partitions are identified, and loops are discarded. All edges are undirected. Only the induced subgraph with *exactly two distinct positive part sizes* is considered; no assertion is made that the full graph \(G_n\) is disconnected.

## Proof

**1. The three framework families form one connected subgraph.** In \(H_n\), shifting one unit from its unique part larger than one into a fresh row connects consecutive hooks. The chain ends at \((n-1,1)\) and \((2,1^{n-2})\). In \(T_n\), shifting a unit from the larger of its two parts to the smaller connects consecutive two-part partitions, beginning at \((n-1,1)\). In \(U_n\), turning a part of size two into two singleton parts connects consecutive members, ending at \((2,1^{n-2})\). Every intermediate partition retains exactly two part sizes. Thus \(H_n\cup T_n\cup U_n\) is connected (the three families overlap at the two indicated hooks).

For odd \(n=2b+1\geq7\), the extra vertex \((b,b,1)\) is adjacent to \((b+1,b)\in T_n\) by moving the singleton into a part of size \(b\). The other extra vertex \((3,2^{b-1})\) is adjacent to \((2^b,1)\in U_n\) by splitting its part of size three into two and one. Therefore the whole displayed set is connected.

**2. It has no edges to any other two-support vertex.** An elementary transfer from a partition with exactly two distinct part sizes can use only the following donor–recipient value pairs (where \(0\) denotes a new row): larger-to-smaller, smaller-to-larger, larger-to-larger when multiplicity permits, smaller-to-smaller when multiplicity permits, and either existing size to zero. For the five named families the exhaustive possible outcomes *that still have exactly two distinct part sizes* are:

| Starting family | Possible destination families within \(G_n^{[2]}\) |
| --- | --- |
| \(H_n\): \((a,1^q)\), \(a\geq2,q\geq1\) | \(H_n\), \(T_n\), or \(U_n\) |
| \(T_n\): \((a,b)\), \(a>b\geq1\) | \(T_n\), \(H_n\), or the extra vertex \((b,b,1)\) when \(a=b+1\) |
| \(U_n\): \((2^p,1^q)\), \(p,q\geq1\) | \(U_n\), \(H_n\), or the extra vertex \((3,2^p)\) when \(q=1\) |
| \((b,b,1)\), \(b\geq3\) | \((b+1,b)\in T_n\), and also \((3,2,2)\) if \(b=3\) |
| \((3,2^p)\), \(p\geq2\) | \((2^{p+1},1)\in U_n\), and also \((3,3,1)\) if \(p=2\) |

For completeness, the first three rows can be checked directly without any implicit assumption about multiplicities. From \((a,1^q)\), transfers toward a new row or toward its size-\(a\) part stay in the hook family; moving between two ones can give \(U_n\) (if \(a=2\)) or \(T_n\) (if \(q=2\)); moving from \(a\) into a one can give \(U_n\) (if \(a=3\)) or \(T_n\) (if \(q=1\)). All other nontrivial outcomes have at least three positive part sizes. From \((a,b)\), inward and outward transfers between its two existing rows stay in \(T_n\) when they retain two sizes; creating a new one gives \(H_n\) when \(b\in\{1,2\}\), or \((b,b,1)\) precisely when \(a=b+1\). From \((2^p,1^q)\), moving a two into a new row, or moving between two ones, stays in \(U_n\) when the resulting support is two; moving between two twos can give a hook only when \(p=2\); moving a one into a two yields \((3,2^p)\) only when \(q=1\). The fourth and fifth rows follow from the same six donor–recipient choices with sizes \(b,1\) and \(3,2\), respectively. All boundary cases losing a support size are excluded because the graph is induced on support exactly two.

For odd \(n\geq7\), the two exceptional shapes appearing in the first three rows belong to the displayed set, and the final two rows show they introduce no further destinations. For even \(n\), the exceptional odd-size shapes cannot arise; for \(n=5\) the two would-be exceptional partitions are already in \(U_5\) and \(T_5\); and \(n=3\) is checked directly. Hence the displayed connected set is closed under all edges of \(G_n^{[2]}\). It is therefore exactly the component containing \((n-1,1)\).

**3. Count and connectivity.** For \(n\geq4\), \(|H_n|=n-2\) and \(|T_n|=|U_n|=\lfloor(n-1)/2\rfloor\). The only intersections are \(H_n\cap T_n=\{(n-1,1)\}\) and \(H_n\cap U_n=\{(2,1^{n-2})\}\). Consequently the three-family union has order \(n+2\lfloor(n-1)/2\rfloor-4\). For odd \(n\geq7\), the two additional vertices are distinct and outside this union, proving the formula. The \(n=3\) case is a singleton.

For \(n\geq8\), the partition \((n-4,2,2)\) has support exactly two but is not of any listed form: its largest part is at least four, it has three parts, and its smaller parts are both two. Thus the stratum is disconnected. For \(n=3,4,5,6,7\), direct enumeration of partitions with exactly two part sizes gives respectively \(1,2,5,6,11\) vertices, precisely the component sizes already proved. This establishes the claimed exact connectivity threshold. \(\square\)

## Verification

The standalone file `artifacts/verify.py` independently generates all integer partitions for \(3\leq n\leq22\), calculates adjacency from *indexed donor and recipient rows*, and compares it with a distinct-size transfer implementation. It checks the explicit proposed component by breadth-first search, equality with the closed-form shape family, component size, and the disconnection witness. For \(23\leq n\leq150\), it enumerates two-support partitions by the independent integer equation \(pa+qb=n\), checks closure under all allowed transfers, and repeats the component and size checks. The replay prints `VERIFY_OK`. These are finite consistency checks, not a substitute for Step 2 of the general proof.

## Relationship to prior work

Lyudogovskiy's *The Partition Graph as a Growing Discrete Geometric Object* (arXiv:2603.21221, §§2.4–2.6) introduces the hook main chain, the two-part side chain, and its conjugate. *Boundary Framework, Rear Morphology, and Rectangular Ears* (arXiv:2603.24824, §§2–4) studies this boundary and full-graph rectangular-ear neighborhoods. We use the same established partition-transfer adjacency and explicitly distinguish their **full graph** from the present *fixed-support-induced graph*.

The motivating *Support and Support Jumps in the Partition Graph* (arXiv:2604.11837, §§6–8) defines induced support strata, gives component-count data only through \(n=25\), and poses their connectivity as Problem 7.4. It does not state that the support-two component at \((n-1,1)\) is an exactly closed boundary family, does not give the two odd-size additions or the piecewise order, and does not prove the all-size connectivity cutoff. Our theorem supplies these missing assertions without claiming a census of all other components. Earlier partition Gray-code work concerns minimal-change generation of specified partition families, not this exact fixed-support component theorem.

## Limitations

The classification is only of the component containing \((n-1,1)\), *not* of every component or every connected path in \(G_n^{[2]}\). It establishes connectedness of the complete stratum only for the finite small cases and disconnection for larger \(n\); it does not count the other components. It does not concern other support levels, directed transfers, or the connectivity of the unrestricted partition graph. Priority assessment against non-indexed historical work remains provisional, and no independent mathematical audit has occurred.

## References

1. F. B. Lyudogovskiy, *Support and Support Jumps in the Partition Graph*, arXiv:2604.11837v1, first public 2026-04-12, https://arxiv.org/html/2604.11837v1.
2. F. B. Lyudogovskiy, *The Partition Graph as a Growing Discrete Geometric Object*, arXiv:2603.21221v1, first public 2026-03-22, https://arxiv.org/html/2603.21221v1.
3. F. B. Lyudogovskiy, *Boundary Framework, Rear Morphology, and Rectangular Ears in the Partition Graph*, arXiv:2603.24824v1, first public 2026-03-25, https://arxiv.org/abs/2603.24824.
4. C. D. Savage, *Gray code sequences of partitions*, Journal of Algorithms 10 (1989), 577–595 (background on partition transfer generation; no claim that this establishes the present induced-component formula).
