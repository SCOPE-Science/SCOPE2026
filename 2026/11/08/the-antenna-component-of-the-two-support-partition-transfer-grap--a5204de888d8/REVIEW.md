# Independent mathematical audit

## correctness

PASS

For the repaired result only: the frozen closure table and prose say a singleton entering a size-two row of (2^p,1) yields (3,2^p), which has the wrong total n; the correct result is (3,2^(p−1)). For example (2,2,2,1) becomes (3,2,2) at n=7. When p=1 and there are at least two singleton rows the same donor/recipient type produces the hook (3,1^(q−1)), not listed in the frozen explanatory subcases. At (3,1), the move from size 3 to size 1 gives (2,2), contrary to the frozen blanket statement that other nontrivial outcomes have at least three sizes. A fresh-row move from the larger part of (a,b) gives the equal-largest odd exception only for a=b+1 and b>=2, since b=1,a=2 yields support one. The replacement proof treats all feasible donor/recipient sizes with multiplicity checks and filters loops and support-one/three results. A transfer is reversible by moving a unit back, creating a fresh row if the old donor was a singleton, so enumerating outgoing transfers suffices for undirected closure. From H only H,T,U survive; T gives T,H, or (b,b,1); U gives U,H, or (3,2^(p−1)). The two extra families attach by one edge to their respective chains and are adjacent to each other only for n=7. At n=5 the would-be extras already lie in U_5 and T_5, and n=3 is a singleton. For n>=4 the only intersections of H,T,U are the two different end hooks. Inclusion–exclusion and the two distinct odd added vertices give the stated orders. The witness (n−4,2,2) is two-support outside the closed set for every n>=8; whole-stratum counts for n=3..7 are 1,2,5,6,11. Independent indexed-row BFS with all partitions confirmed the component at n=3..24 and agreed with the value-pair implementation on all support-two vertices at these sizes; feasible value-pair closure was checked through n=250. This preserves the theorem statement but corrects a false exhaustive description in the supporting proof.

## originality

PASS

For the unchanged theorem with its corrected proof: the three full-graph chains and the small-n disconnection data are prior. The claim being credited is the exact induced component, including the odd-size neighbors and its order, and the connectivity cutoff proved for all n. The primary fixed-support source poses the general problem and records small sizes; it does not establish this closure.

## value

PASS

This is a natural distinguished component of the smallest nontrivial support stratum of an established transfer graph. The exact closure and odd exceptions describe which boundary configurations communicate; the order and witness turn a short computational connectivity observation into a sharp theorem for all n in this stratum. The value is not the three known paths or an exhaustive census of every component. Repairing the transfer proof keeps that substantive structural content unchanged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
