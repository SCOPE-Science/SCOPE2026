# Independent mathematical audit

## correctness

PASS

For positive edge lengths closing along five successive 72-degree directions, projection of m_(i+2)-m_i onto the intervening edge gives Δ_i≥g_i=ell_(i+1)−(1−cos72°)(ell_i+ell_(i+2))/2. Explicit weighted sum g0+2g1+2g2+g3 plus the real closure relation equals cos72°(ell0+2ell1+(ell2+ell3)/2+2ell4)≥cos72°L/2. Each cyclic block of four therefore has some g_i≥cos72°L/12; choosing the four indices not containing a hypothetical sole large gap forces two distinct ones. The exact closure example with lengths (1/100,1,b,b,1), b=(299−99sqrt5)/200, has H0=H3>0,H1=H2<0,H4<0, so precisely three nonadjacent pairs intersect and 8 total edges. Fresh SymPy expansion independently checked closure, certificate and all 5 radical signs; 9-edge unrestricted integer witness checked by inspected script. Boundary: closed disks, strictly positive sides, exact 72° exterior turns; quantitative coefficient not asserted optimal.

## originality

PASS

General convex-polygon side-disk graph planarity (Huemer–Pérez-Lantero) only forbids one of five nonadjacent disk pairs at n=5, not two separated pairs; Herrera–Pérez-Lantero treewidth/independent-set results likewise do not force the equiangular numerical threshold. The fixed-angle separation margin and sharp 8-edge witness are not derived by those results.

## value

PASS

The graph of side-diameter disks is a natural geometric proximity object; restricting to an equiangular pentagon forces a genuinely stronger graph-theoretic exclusion than general planarity (8 rather than 9 edges), with an explicit uniform physical separation and a sharp extremal construction. This is not a generic n=5 enumeration or a routine restatement of planarity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
