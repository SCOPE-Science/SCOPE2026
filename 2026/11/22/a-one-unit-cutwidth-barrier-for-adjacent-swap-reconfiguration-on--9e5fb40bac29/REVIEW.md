# Independent mathematical audit

## correctness

PASS

Count private edges across prefixes with zero, one or two hubs: the widths are a+b, t-a+b+1, and 2t-a-b for U before V. Only a direct adjacent U/V swap changes orientation, and it presents middle widths t+1±(a-b), so it cannot occur at budget t or below. Each orientation is nonempty at t by A^tUVB^t and its mirror; at any lower nonempty budget exchange the two labeled classes and hubs to see that both orientations occur. An adjacent swap changes only the prefix between the swapped entries: BA→AB leaves that cut unchanged outside the hubs and lowers it by two inside; BU→UB and VA→AV bound the new cut by an unchanged neighboring cut minus one. After evacuating the wrong external classes and sorting the middle, UA→AU has new cut a+1≤t and BV→VB has new cut t-b≤t. Same-class label swaps preserve all widths. The passes therefore normalize every feasible order at budget at least t in O(t²) moves. The bridge with h=floor(t/2) has widths bounded by max(2h,t+1,2t-2h)=t+1 in either hub order. The recurrence appends one available symbol and tests the resulting prefix; assigning leaf labels multiplies by (t!)². Independent replay: python3 /workspace/branches/202fc70b-cbfc-4afc-9663-4988e7880669/edgecut_check.py. Its direct edge-cut permutation enumeration and BFS found profiles (1,1)/(16), (16,16)/(296), and (1224,1224)/(13536) at t/t+1 for t=1,2,3; its prefix DP found M_t=1,4,34,160,950,4424 through t=6. The bounded checks corroborate rather than prove the general result. The frozen verifier was inspected, not run. No shortest-path claim is established.

## originality

PASS

The same order-reconfiguration model is established; the finding is the exact connectivity threshold, the obstruction at the tight budget, and the component census on a specific two-hub tree family. Located results do not cover these claims; this is a best-of-knowledge assessment.

## value

PASS

The family is a natural minimal extension of a star with a genuine order-change obstruction. Identifying the exact extra budget, an explicit crossing move, routing inside both orientations, and their exact size adds information neither generic factor-two slack nor a feasibility count gives. The result is limited to unit-weight balanced double stars.

The dated certificate retains the supplied scientific assessment, sources and limitations.
