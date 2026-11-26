# Independent mathematical audit

## correctness

PASS

For the unsigned incidence M, simplicity and characteristic two give B=MᵀM, and T=MMᵀ is the sum of I+R_a over the generators. These commuting summands square to zero, so T²=0 and B³=0. The group algebra is the truncated square-zero coordinate algebra: T multiplies by t with linear part indexed by c=⊕S. If c≠0, complete t to independent degree-one coordinates. The induced endomorphism is well-defined because augmentation elements square to zero; invertibility on degree one implies generation on the associated graded and hence invertibility of the filtered map. Multiplication by the first coordinate has rank v/2 and equal kernel and image. Connectedness gives H=im M the zero-sum hyperplane (path column sums generate all e_u+e_v) and ker Mᵀ the all-one line in H, so rank B=v−2. For an independent check of the key compression, take a binary linear functional f on vertices with f(c)=1. Then Tf=1 and f∈H since it has 2^(r−1) ones, even for r≥2. Symmetry implies ker T⊂H, so dim T(H)=v/2−1, and Tf=1 gives a further one-dimensional loss under Mᵀ. Thus rank B²=v/2−2. The ranks force (a_3,a_2,a_1)=(v/2−2,2,(s−3)v/2+2), including v=4 where s=2. Kernel-size differences give extinction populations (with exactly one state at time zero). U=I+B has U²=I+B² and U⁴=I, and its fixed subspaces at 1 and 2 give the primitive periods and orbit counts; q is any finite characteristic-two field size. In the excluded K_{4,4} boundary, the rook adjacency squares to zero by J_4²=0. Ran python /workspace/reproductions/check.py 2: direct spans for all 92 connected dimension-three generating sets and full state counts for a square over F_4 and the cube over F_2. The two frozen scripts and captured outputs were inspected, not executed; the recorded 96 complete cases are cumulative across dimensions two and three, and the 200 further cases are sampled. Finite enumeration corroborates, not proves, the all-dimensional statement.

## originality

PASS

Pass for the arbitrary-eligible-cubelike line-graph Jordan/dynamics classification, not for the vertex-Laplacian rank, the cube case, extension of a fixed binary matrix's ranks to characteristic-two fields, or the kernel-to-period counting method separately. Gao–Marx-Kuo–McDonald–Yuen prove exactly the relevant vertex rank under the same nonzero-xor condition. An earlier indexed record already gives the line-graph rank pair, Jordan partition and extinction census for coordinate generators. The noncoordinate edge-space result uses genuinely additional incidence restriction and a position calculation for the all-one line, not just an extension of scalars or a graph-parameter relabelling. No inspected source gives that line-operator compression for the full class.

## value

PASS

The proven rank loss provides an exact edge invariant across arbitrary spanning eligible connection sets, not just a periodic cellular-automaton example on a cube. It classifies sharp extinction and recurrence, exact populations and primitive orbit counts, including the small-dimension and zero-xor boundary distinctions. The known vertex rank is important but describes vertex states, so the edge result is independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
