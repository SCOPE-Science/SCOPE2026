# Seven-class wheel coalition partitions and sharp apex repair configurations

## Finding

Define the *singleton repair count* of a non-locating-dominating vertex set \(A\) in a finite simple graph \(G\) as
\[
s_G(A)=|\{w\in V(G)\setminus A:\ A\cup\{w\}\text{ is locating-dominating}\}|.
\]
Let \(H\) be any nonempty finite simple graph, put \(G=K_1\vee H\), let \(h\) be the universal apex, and let \(d=\Delta(H)\). **Apex-local estimate (context from the counting argument of [1]):** every non-locating-dominating \(A\subseteq V(G)\) containing \(h\) satisfies
\[
\boxed{s_G(A)\le2d+2.}
\]
**New uniform sharpness and coalition partitions:** for every integer \(d\ge2\), a connected cone \(G_d\) with \(\Delta(H_d)=d\) and a set \(A_d\ni h\) have \(s_{G_d}(A_d)=2d+2\). The partition consisting of \(A_d\) and its \(2d+2\) singleton-complement classes is a locating-dominating coalition partition, so
\[
\boxed{C_L(G_d)\ge2d+3.}
\]
**New seven-class wheel family:** for every integer \(m\ge10\), the wheel \(W_{m+1}=K_1\vee C_m\) admits an explicit locating-dominating coalition partition of size \(7\), so
\[
\boxed{C_L(W_{m+1})\ge7.}
\]
The paper of Chellali et al. establishes \(C_L(C_m)\le6\) for cycles, so this gives a strict increase for a one-apex extension. The upper estimate above is *not* asserted to be new: it follows from the finer neighborhood-counting step in their Lemma 2.10. The original contribution is the new sharpness construction for every base degree together with the new wheel seven-class family. The result does *not* claim that the wheel bound \(7\) is optimal.

## Assumptions and scope

Graphs are finite, undirected, simple. The base graph \(H\) may be disconnected; its cone \(G=K_1\vee H\) is connected. For a graph \(G\), a set \(D\subseteq V(G)\) is *locating-dominating* (LD) exactly when every vertex outside \(D\) has a nonempty open-neighborhood trace \(N_G(v)\cap D\) and these traces are pairwise distinct. A locating-dominating coalition (LDC) partition has no LD class, but every class has another class whose union with it is LD. The parameter \(C_L(G)\) is the largest number of classes in such a partition. All wheel cycle labels are modulo \(m\).

For sharpness, let \(H_d\) be the disjoint union of two once-subdivided \(d\)-stars. In component \(i\in\{1,2\}\), denote the center by \(c_i\), its adjacent subdivision vertices by \(p_{i,1},\ldots,p_{i,d}\), and the terminal leaves by \(t_{i,1},\ldots,t_{i,d}\). Its only edges are \(c_i p_{i,j}\) and \(p_{i,j}t_{i,j}\). Put \(G_d=K_1\vee H_d\), and select \(A_d=\{h\}\cup\{t_{i,j}:i=1,2,\ 1\le j\le d\}\).

For wheels, label the rim vertices \(0,1,\ldots,m-1\). Set
\[
U=\{1,2,3,6,7,8\},\qquad A=\{h\}\cup (V(C_m)\setminus U).
\]

## Proof

**1. The apex-local inequality.** Since \(h\in A\), all outside vertices are dominated by \(A\). Because \(A\) is not LD, there exist distinct \(u,v\in V(H)\setminus A\) with
\[
N_G(u)\cap A=N_G(v)\cap A.
\]
Fix such a collision. If \(w\in V(H)\setminus(A\cup\{u,v\})\) and \(A\cup\{w\}\) is LD, then the traces of \(u\) and \(v\) must become different. The only new selected vertex is \(w\), so necessarily \(w\) is adjacent in \(H\) to exactly one of \(u,v\). Consequently every singleton repair vertex lies in
\[
\{u,v\}\cup (N_H(u)\mathbin\triangle N_H(v)).
\]
The cardinality of this set is at most \(2+\deg_H(u)+\deg_H(v)\le2d+2\). This proves the inequality for every possible \(A\), including cases with multiple collisions. Notice that this is a necessary condition for repair: we do not presume that every vertex in the displayed set actually repairs \(A\).

**2. Equality and unbounded coalition families.** For \(d\ge2\), the maximum degree of \(H_d\) is \(d\). The outside vertices of \(A_d\) are exactly the two centers and all \(2d\) subdivision vertices. Their traces into \(A_d\) are
\[
N_{G_d}(c_1)\cap A_d=N_{G_d}(c_2)\cap A_d=\{h\},
\quad N_{G_d}(p_{i,j})\cap A_d=\{h,t_{i,j}\}.
\]
The \(2d\) latter traces are all distinct and distinct from \(\{h\}\). Thus the centers are the unique collision. Selecting either center removes one member of that pair. Selecting any subdivision vertex \(p_{i,j}\) makes exactly its center adjacent to a new selected vertex, separating the centers. All other outside traces were already distinct and remain so when a new vertex is selected; domination remains valid. Hence **every** one of the \(2d+2\) outside vertices repairs \(A_d\), proving equality.

No singleton \(\{w\}\), for any \(w\in V(G_d)\setminus A_d\), is dominating: choose a terminal leaf in the *other* subdivided-star component, which is not adjacent to \(w\). The set \(A_d\) is non-LD, while each \(A_d\cup\{w\}\) is LD. Therefore
\[
\big\{A_d\big\}\cup\big\{\{w\}:w\in V(G_d)\setminus A_d\big\}
\]
is an LDC partition of \(2d+3\) classes, proving the stated lower bound.

**3. Seven classes in every sufficiently long wheel.** Consider the selected set \(A\) and its six outside rim vertices \(U\) from the assumptions. Since \(m\ge10\), the four vertices \(0,4,5,9\) are all selected and distinct. The outside traces are exactly
\[
\begin{aligned}
N(2)\cap A&=N(7)\cap A=\{h\},\\
N(1)\cap A&=\{h,0\},&N(3)\cap A&=\{h,4\},\\
N(6)\cap A&=\{h,5\},&N(8)\cap A&=\{h,9\}.
\end{aligned}
\]
Thus \(A\) dominates and has exactly one collision, between rim vertices \(2\) and \(7\). Adding \(2\) or \(7\) removes one colliding vertex; adding \(1\) or \(3\) creates a new selected neighbor for \(2\) only; adding \(6\) or \(8\) does so for \(7\) only. In every case the remaining outside traces become distinct, so the augmented set is LD. No singleton rim vertex dominates a wheel when \(m\ge10\), since it has only its two rim neighbors and the apex adjacent. Therefore the partition \(\{A,\{1\},\{2\},\{3\},\{6\},\{7\},\{8\}\}\) is LDC. This establishes \(C_L(W_{m+1})\ge7\) uniformly for all \(m\ge10\).

## Verification

Run `python3 verify.py` with Python \(3\). The standard-library verifier implements LD directly from nonempty, pairwise distinct open-neighborhood traces. It exhaustively tests the local partner inequality on every \(33866\) apex-containing subset of all labelled simple base graphs of orders \(1\) through \(5\), tests the sharp construction for \(2\le d\le20\), checks the wheel seven-class witnesses for \(10\le m\le120\), and computes all hub-containing singleton-repair maxima on wheels with \(3\le m\le13\). The replay terminates with `VERIFY_OK`. These finite computations support, rather than replace, the unrestricted arguments in the proof.

## Relationship to prior work

Chellali, Dobrynin, Foucaud, Golmohammadi and Valenzuela-Tripodoro [1] introduce LDC partitions. Their Lemma 2.10 shows that a class of any LDC partition has at most \(2\Delta(G)\) partners and proves sharpness for a cubic example. **Their proof directly yields our upper estimate:** fixing a colliding pair of outside vertices and counting their available closed-neighborhood vertices gives at most \(2+\deg_H(u)+\deg_H(v)\) singleton repairs when the apex is selected. We do **not** claim this bound as new. Our new contributions are (i) explicit *equality for every base maximum degree* \(d\ge2\), with actual LDC partitions of \(2d+3\) classes, and (ii) the explicit seven-class LDC partition for every wheel on \(m+1\) vertices when \(m\ge10\). These statements are not given by the previously published counting proof. We do not assert a global upper bound on \(C_L(G)\) in terms of \(d\).

Their Lemma 3.4 and Proposition 3.7 give \(C_L(C_m)\le6\) and a full cycle classification, but they do not give the cone/wheel construction above. Their Section 6 asks for degree-based bounds on coalition numbers; the cone family contributes a sharp local structural tool in that direction. The definition of locating-domination has earlier roots in Slater [2]. Searches of accessible records for wheel, apex, cone, and singleton-partner formulations did not reveal a stronger statement implying this combined result. Absence of an indexed match is not a proof of historical priority.

## Limitations

The local inequality is a direct consequence of the preceding literature and is used for context rather than claimed as new. It assumes that the selected set contains the unique apex. It does not bound singleton repairs for arbitrary non-LD sets without the apex. The constructed sharp bases \(H_d\) are disconnected although every corresponding cone is connected. The \(7\) for wheels is a proven lower bound, not an exact coalition number for all wheel orders; no characterization of all optimal partitions is claimed. Priority remains conditional on inaccessible or unindexed literature. The scientific review here is same-model only, not independent validation.

## References

[1] M. Chellali, A. A. Dobrynin, F. Foucaud, H. Golmohammadi, and J. C. Valenzuela-Tripodoro, "Locating-dominating coalitions in graphs," arXiv:2602.18760, first posted 2026-02-21, updated version 2026-02-27; especially Lemma 2.10, Lemma 3.4, Proposition 3.7, and Section 6. https://arxiv.org/abs/2602.18760

[2] P. J. Slater, "Domination and location in acyclic graphs," *Networks* **17** (1987), 55–64, DOI:10.1002/net.3230170105.
