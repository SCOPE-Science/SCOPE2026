# Independent audit — SCOPE-20260913-008

Date: 2026-09-28 (UTC)  

## Disposition: FAILED

### Correctness
The commutative-algebra portion is largely correct: for sl3 the nilpotent cone is the homogeneous complete intersection cut out by the degree-2 and degree-3 basic invariants, so base-changing its Koszul model to the origin produces an exterior cdga on two degree -1 generators; the multiplicity at the vertex is 2·3=6. The naive fiber-product tangent dimensions (8,0,2) and virtual dimension -10 are consistent with that lci model.

The central shifted-symplectic interpretation is not correct. A Lagrangian morphism into [g*/G] is extra structure; in the standard Hamiltonian interpretation it is supplied by a Hamiltonian G-space. The Springer resolution T*(G/B) with its moment map supplies such a Lagrangian map, but the singular image [N/G] is not interchangeable with [T*(G/B)/G] as a Lagrangian source. The filed record defines L1=[N/G] and then attributes to it the Springer Lagrangian structure without constructing or verifying the required nondegenerate isotropic structure.

There is also an internal tangent error in the “resolved model”. At a point of μ^-1(0)=G/B, dμ has rank 3. After quotienting by G, the infinitesimal action g→T(G/B) is surjective with kernel b, so the derived zero-fibre quotient has H^-1≅b (dim 5), H^0=0, H^1≅b* (dim 5), hence virtual dimension -10. The filed (5,3,5) and virtual dimension -7 double-count the base tangent directions.

Finally, the quantity called an “intersection weight” w=χ(Fl3) corrected by an “Euler-log” log(mult/χ) is not tied to a cited standard intersection/DT invariant. The numerical equality mult_0(N)=χ(Fl3)=6 is true, but it does not validate the proposed weight.

### Originality
The valid ingredients (Springer resolution, nilpotent cone complete intersection, flag Euler characteristic, shifted Hamiltonian/Lagrangian formalism) are classical or standard. No independent scientific novelty survives after removing the invalid Lagrangian/weight claims.

### Scientific value
The record contains useful local algebra calculations, but the headline interpretation and resolved comparison are wrong. It should be preserved as a failed attempt rather than published as a validated finding.

### Sources
- P. Safronov, *Symplectic implosion and the Grothendieck–Springer resolution*, DOI 10.1007/s00031-016-9398-1.
- Pantev–Toën–Vaquié–Vezzosi, *Shifted Symplectic Structures*, arXiv:1111.3209.
