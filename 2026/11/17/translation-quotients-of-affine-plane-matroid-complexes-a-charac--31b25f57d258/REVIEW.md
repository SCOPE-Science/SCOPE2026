# Independent mathematical audit

## correctness

PASS

K_q is the rank-three affine-plane matroid independence complex: all vertices/pairs and exactly noncollinear triples, hence a connected simply connected 2-dimensional wedge of S2 by matroid shellability. Every nonzero additive translation has prime order p, moves all vertices, and a fixed point of a face requires an invariant face of at most 3 vertices. For p=3 translation 3-orbits are collinear (not faces); for p>3 cannot be within faces; for p=2 each translation fixes q²/2 midpoints of swapped edges. The applicable Armstrong theorem for barycentrically subdivided simplicial actions yields π1(|K_q|/T) = T/<point-fixing translations>, trivial for characteristic two, T=(Z/p)^{2e} for odd characteristic. Count faces using q² vertices, C(q²,2) edges and C(q²,3)-q(q+1)C(q,3) noncollinear triples, and fixed-point Euler for nonzero translations; Burnside gives Euler=1+b_q. Since quotient is 2-dimensional and finite H1 has no free rank, H2 is free of rank b_q; for p=2 simply connected 2-complex is wedge^b S² by Whitehead, not merely rational. Independent exact q=2,3,4,5,7 cover and quotient Euler arithmetic matches the stated b_q, while source affine_check.py uses full orbit-chain Smith normal forms at 2,3,4; finite tests do not replace the arbitrary-field argument.

## originality

PASS

PASS best-of-knowledge. The characteristic-two vs odd-prime quotient fundamental group and exact integral homology for rank-three affine-plane *matroid independence complexes* are not established by generic matroid shellability, general Armstrong orbit fundamental groups, covering-space representation results, or similarly named affine *incidence-graph Rips* quotients.

## value

PASS

This is a uniform natural infinite family with an abrupt characteristic-two homotopy transition caused by fixed edge midpoints. Complete integral H1 torsion for odd characteristic and wedge-of-two-spheres homotopy for even characteristic refine generic rational representations; exact b_q makes the difference quantitative. This is a meaningful structural invariant, not merely a finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
