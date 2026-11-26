# Independent mathematical audit

## correctness

PASS

The nonzero factorizations uv^T with v^Tu=0 have free scalar orbits of size q−1 and all belong to one Jordan class. Fix X=e_1 e_2^T and set a=s_2, b=t_1 for Y=st^T. Then [X,Y]=a e_1 t^T−b s e_2^T and tr(XY)=ab. No nonzero contraction gives rank zero, exactly one gives rank one and square zero, and two give rank two by independence of the two image vectors and two covectors. In the last case span(e_1,s) carries eigenvalues ab,−ab and the two covectors' common kernel complements it, even when the eigenvalues coincide in characteristic two. For fixed a≠0, imposing t_1 and t^Ts=0 imposes two independent scalar conditions, so the count with fixed nonzero ab is q^(2n−3); with b=0 it is q^(n−1)(q^(n−2)−1). The other one-sided count follows by transpose and swapping coordinates 1 and 2. Subtraction from the full class size gives the zero count. The sandwich identities give [C,X]=2ab X and [C,Y]=−2ab Y. If ab≠0, on span(e_1,s) the two generators have opposite off-diagonal entries and C is nonzero diagonal, so they are independent even in characteristic two. In the one-sided case C shares one image or covector line with X and the other with Y; using the distinct lines gives independence. Therefore the span is the stated three-dimensional Lie algebra whenever C≠0; the commuting case reduces to the scalar-multiple test. Normalizing by the full class size gives the stated limits. Independent replay `python3 -B /workspace/review_checks.py 5` enumerated the ambient matrices for (q,n)=(2,2),(3,2),(5,2),(2,3),(3,3), checking rank, trace, eigenspace sizes and Lie span against the proof. The trace in the finding is tr(XY), not the trace of C, which is always zero.

## originality

FAIL

The rank, trace and similarity census for n>=3 is already covered mathematically by an independently indexed, stronger same-day Resultary theorem. The relative posting order of the same-day records is not established. The qualitative odd-characteristic Lie classification also has explicit antecedent coverage in the infinitesimal-transvection literature over algebraically closed fields, with split descent here. Combining that comparison with the rank distribution and the elementary square-zero identity in characteristic two leaves no scientifically distinct exact invariant in the submitted conjunction. This is a failure to establish distinct originality on the combined evidence, not a claim that the entire text or even its exact numerical conjunction appeared in a single earlier-dated paper.

## value

FAIL

The orbit and joint invariant are natural, but after removing the rank-and-trace census covered by the stronger indexed theorem and the known two-transvection Lie cases, the remaining characteristic-two count is the same commuting census relabeled by an immediate double-bracket identity. The direct 2-by-2 boundary and asymptotic division do not independently supply a useful new invariant. No distinct valuable claim suitable for repair was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
