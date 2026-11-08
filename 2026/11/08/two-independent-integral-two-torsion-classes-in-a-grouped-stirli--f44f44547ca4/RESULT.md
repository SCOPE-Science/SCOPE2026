# Two independent integral two-torsion classes in a grouped Stirling complex on the complete four-vertex graph

## Finding
Let \(G=K_4\), and give each of three **distinguishable** colors exactly two **indistinguishable within that color** robots. For the grouped Stirling cubical complex \(S_{(2,2,2)}(K_4)\) of Revelli and Scheirer, the complete integral homology is
\[
H_k(S_{(2,2,2)}(K_4);\mathbb Z)\cong
\begin{cases}
\mathbb Z,& k=0,\\
\mathbb Z^{12}\oplus(\mathbb Z/2\mathbb Z)^2,& k=1,\\
\mathbb Z^{71},& k=2,\\
0,& k\ge3.
\end{cases}
\]
The two independent order-two classes in first homology show that this natural grouped configuration complex has genuine integral torsion.

## Assumptions and scope
The complete graph has vertices numbered \(0,1,2,3\), with all six unordered edges oriented from their smaller to larger endpoint. A cubical cell for each color is a choice of two pairwise-disjoint closed vertex/edge supports, with no overlapping endpoints within that color; across colors supports may overlap. Every graph vertex must be occupied by at least one vertex robot. An edge-interior robot does not cover its endpoints. The three colors are ordered and distinguishable, but the two robots within each color are unordered. The total cell dimension is the number of chosen edges. We use the closed cubical model in *Grouped Stirling complexes* (arXiv:2602.09884). These definitions give an honest cellular chain complex, not an approximation to another configuration space.

## Proof
Enumerate the valid configurations, independently choosing each color's two disjoint closed supports, and retain only configurations whose vertex robots cover all four graph vertices. The exhaustive enumeration gives \(c_0=114\), \(c_1=432\), \(c_2=378\), and \(c_j=0\) for \(j\ge3\). In particular, the top dimension is two: three moving edges would leave at most three stationary vertex robots to cover four vertices.

Orient an edge support \(\{a,b\}\), with \(a<b\), from \(a\) to \(b\). Orient product cells by the increasing color order and increasing edge index within each color. The signed cellular boundary of a moving edge is endpoint \(b\) minus endpoint \(a\), with the usual Koszul sign given by the number of earlier moving factors. There are exactly 1,512 nonzero entries in the \(432\)-by-\(378\) matrix \(\partial_2\); a direct check gives \(\partial_1\partial_2=0\).

The supplied executable uses only integral elementary row/column operations. It removes 305 diagonal unit pivots of \(\partial_2\), each by unimodular operations. The remaining \(21\)-by-\(25\) nonzero-support submatrix has all entries divisible by two. After division by two, another exact integer unit-pivot elimination removes two unit pivots and leaves the zero matrix. Hence the integer Smith invariants of \(\partial_2\) are exactly 305 copies of \(1\) and two copies of \(2\): \(\operatorname{rank}\partial_2=307\). This is an integral determination, not a mod-two extrapolation.

The 1-skeleton is connected (independently verified by the executable), so \(\operatorname{rank}\partial_1=114-1=113\). The cokernel of \(\partial_2\) has torsion \((\mathbb Z/2)^2\). Since the image of \(\partial_1\) is free, the exact sequence \(0\to H_1\to\operatorname{coker}\partial_2\to\operatorname{im}\partial_1\to0\) shows this is precisely the torsion of \(H_1\). Its free rank is \(432-307-113=12\). Finally \(H_2=\ker\partial_2\cong\mathbb Z^{378-307}=\mathbb Z^{71}\); there are no higher chain groups.

## Verification
Run `python3 CHECK.py` in the same directory as `grouped_general.py`; only the Python standard library is required. The script independently enumerates every color-cell choice, constructs the signed cubical boundaries, verifies their composition is zero, checks cellular connectivity, performs the exact sparse unimodular reductions, and asserts every reported count and Smith factor. Its recorded deterministic output is `CHECK_OUTPUT.txt`. The proof is a finite exhaustive integer calculation; no claim is made about other graphs or color vectors.

## Relationship to prior work
Revelli–Scheirer introduce the grouped Stirling cubical complexes, establish connectivity for three or more colors, and determine cell counts for certain parameter families. Their homology calculations do not give the integral answer for this triple of quotas on \(K_4\). The present computation adds an exact torsion example, rather than another cell count. Generalized forbidden-collision graph configuration-space results concern related constructions but do not imply this particular restricted-coverage colored cubical calculation.

## Limitations
This is one natural finite object, not a general torsion theorem for all grouped Stirling complexes. No determination of homotopy type, cup product, or symmetry representation is asserted. Its correctness relies on the specified cubical convention and reproducible integral arithmetic; other occupancy conventions produce different complexes.

## References
Revelli, Alessia and Steven Scheirer, *Grouped Stirling complexes*, arXiv:2602.09884, first publicly posted 2026-02-10, https://arxiv.org/abs/2602.09884.
