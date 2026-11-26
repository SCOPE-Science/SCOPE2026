# Independent mathematical audit

## correctness

PASS

Expanding L=D-A by walk length, the diagonal of L^3 is d^3+2d^2+s, an edge has L^3 entry -(d^2+de+e^2+d+e-1) (the three-edge walks number d+e-1), a distance-two entry is the sum of the three degrees, and a distance-three entry is -1; longer entries vanish. The L^2 entries are respectively d^2+d, -(d+e), 1, and 0. The edge quadratic has positive leading coefficient and negative discriminant, since d^2+de+e^2 >= 3(d+e)^2/4. The diagonal is strictly decreasing by s>=d and 1-z+z^2/2>0. Thus only a diagonal or distance-two entry can go negative at a positive step, proving the closed single interval. The identity with F=I-hL, P=I/3+F/2+F^3/6, leaves diagonal slack at h=1/Delta; equality requires a two-edge path of three vertices of full degree, and attaching leaves to a three-hub path realizes it for every Delta>=2. For the star, substitution at 3/(Delta+2) gives the displayed negative expression: its numerator 4Delta^3+3Delta^2-9Delta-16 is positive at 2 and increasing thereafter. At its smaller center root the row-sum identity gives symmetric center-leaf entries 1/Delta. The leaf-to-leaf cubic c is bounded by 2/[3(Delta+2)^2]<1/Delta (maximum at h=2/(Delta+2)); hence the leaf diagonal is positive there. A full-degree vertex in a nonstar has s>Delta, so its diagonal is strictly negative at the star root. All conclusions are for the completed step; graph work is linear, apart from the stated precision-dependent scalar root work. The finite script was inspected but not executed; no enumeration is needed for the arbitrary-tree proof.

## originality

FAIL

Distinct published Resultary records give the exact positivity formula on all positively weighted bipartite graphs and the exact hub cutoff on all positively weighted stars. The tree-local test is an exact specialization of the first; the full-degree equality motif and unique upper extremizer follow directly from these exact formulas, the forward-Euler identity, and the observation that a full-degree vertex all of whose neighbors are leaves forces a star. This is demonstrable mathematical coverage, not a historical priority finding: the strongest records are catalogued after the frozen date.

## value

PASS

An exact completed-step positivity cutoff on a natural graph class is useful in its own right: it replaces a matrix check with local degree data and decides when the forward-Euler constraint is sharp. The fixed-degree extremal interpretation is meaningful numerically and structurally. This assessment of the mathematics does not make an already covered specialization an independently distinct contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
