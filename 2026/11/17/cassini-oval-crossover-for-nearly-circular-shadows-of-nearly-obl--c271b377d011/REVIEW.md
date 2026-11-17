# Scientific review: Cassini-oval crossover in ellipsoid shadows

## Correctness — PASS

The claim is restricted to \(B>\Delta>0\), fixed \(t>0\), and \(\eta\downarrow0\). The compression of the positive definite squared-semiaxis matrix to the viewing plane gives the projected squared semiaxes. Computing the trace and determinant after removal of the scalar matrix \(BI\) gives the exact discriminant identity (1) in RESULT.md. The near-round event forces transverse squared coordinates to be at most \((1+t)\eta/\Delta\); therefore the rescaled domain is uniformly bounded. The sphere chart has its exact Jacobian, and the limiting algebraic boundary has zero area even at \(t=1\), justifying dominated convergence and conditional uniformity. The two-to-one square map gives the precise factor in Cassini area; radial integration produces the stated elliptic-integral expressions. Differentiation and standard singular asymptotics of the complete elliptic integral establish the logarithmic slope. The checker independently confirms the discriminant and sample integrals. A numerical fit alone would not prove the result.

## Originality — PASS, with explicit coverage boundaries

Binney (1985) and Jones–Basu–Dubinski (2001) already give the general line-of-sight formula for the apparent axis ratio, including the fact that the density of nearly circular projections of a fixed triaxial ellipsoid tends to zero. A previously recorded central-section theorem supplies the fixed-triaxial near-circular coefficient, which by polar duality also covers the fixed-shape shadow coefficient. **Neither this coefficient nor classical circular viewing directions are claimed new.**

The assessed result instead takes both anisotropy and roundness tolerance to zero at the same rate. Fixed-anisotropy asymptotics are nonuniform on that scale. The new statement is the complete elliptic-integral crossover \(\Phi(t)\), the Cassini-region conditional viewing-direction law, and the infinite-slope topology threshold at \(t=1\). Relevant searches of mathematical finding records and scholarly literature did not identify this two-parameter limit. Binney's general formula makes the theorem approachable but does not state the rescaling or perform the singular limit. Stark's original 1977 paper was not inspected in full, and hidden overlap in specialized optics or astrophysics literature remains a priority risk.

## Mathematical value — PASS

Nearly round shadows are a natural shape-inference statistic: a vanishing fixed-triaxial density and a nonvanishing axisymmetric endpoint density are well-known qualitatively, yet provide contradictory extrapolations if both shape anisotropy and observational tolerance are small. The crossover resolves their noncommutation, gives a universal Cassini-oval conditional geometry, and identifies a specific logarithmic nonanalyticity at the merger of the two almost-circular viewing-direction neighborhoods. Its object and invariant are intrinsically motivated by orthographic shadow geometry; the result is not a free-standing unmotivated integral evaluation.

## Limits and closest literature

The theorem is first-order in the simultaneous near-oblate limit, not a uniform finite-anisotropy distribution. Jones–Basu–Dubinski, *Intrinsic Shapes of Molecular Cloud Cores* (2001), Sections 2 and 5; Binney, *Testing for triaxiality with kinematic data* (1985), Section 2 and Figure 1; the prior fixed-ellipsoid central-section asymptotic; classical Cassini ovals. Specialized earlier treatments of the near-axisymmetric optical-axis merger remain possible. No independent audit or mathematical certification has been conducted.

Self-review: passed. Independent audit: not yet performed.
