# Independent audit — 2026-09-29

Record: `2026/09/14/035`  
Audited source tree: `7d1f8eff6535ecfdfae5f90ce570b727f669b1d2`  
Disposition: **failed**

## Correctness

The classical dimension/genus calculations and the statement that Hitchin Hamiltonians Poisson-commute are standard and plausible, but the central Melani-Safronov claim uses the wrong shifted-coisotropic degree. In the Melani-Safronov convention an n-shifted coisotropic morphism has an n-shifted Poisson target and induces an (n-1)-shifted Poisson structure on the source; in particular a map to a trivial (n+1)-shifted point recovers n-shifted Poisson structures on the source. Therefore the ordinary 0-shifted Poisson/symplectic structure on the Higgs moduli cannot be encoded by the asserted 0-shifted coisotropic structure over a zero 0-Poisson base in the manner claimed. Moreover standard 'nondegenerate coisotropic' terminology presupposes the relevant nondegenerate shifted-Poisson/Lagrangian compatibility, whereas the record substitutes a custom Hamiltonian anchor determinant over a deliberately degenerate base. The statement that the curve case has Ext^2=0 also conflicts with the scalar H^2 of the unrigidified stable Higgs deformation complex. Thus the advertised shifted-coisotropic theorem is not established by the classical integrable-system observations.

## Originality

The classical Hitchin fibration, spectral correspondence, and singular compactified-Jacobian geometry are established. Because the shifted-coisotropic formulation is invalid as stated, the package does not validate a new derived-geometric theorem whose originality could be credited.

## Scientific value

The dimension checks and nodal critical-locus intuition could support a separately reformulated classical or correctly shifted statement. They do not rescue the record's central 0-shifted Melani-Safronov claim, so the finding is not publishable in its current scientific form.

## Limitations

- This rejection concerns the stated shifted-coisotropic theorem; it does not reject the classical Hitchin-fibration facts used as background.
- A salvage would require reformulating the shift, specifying the precise source/target derived stacks and rigidification, and re-proving the appropriate coisotropic/nondegeneracy conditions from the correct definition.
- The dimension script checks only dimensions, genera, and rough codimensions; it cannot validate the shifted-Poisson/coisotropic formalism.
- No claim is made here about the strongest correct derived reformulation of the Hitchin morphism.

## Sources checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/14/035
- https://arxiv.org/abs/1608.01482
- https://arxiv.org/abs/1704.03201
- https://arxiv.org/abs/1506.03699
