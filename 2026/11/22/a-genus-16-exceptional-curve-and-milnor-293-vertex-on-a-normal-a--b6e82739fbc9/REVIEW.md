# Independent mathematical audit

## correctness

PASS

The frozen geometric and numerical assertions check out. The repaired finding in /workspace/repairs/4 also identifies the local resolution with the normalized point blow-up. In the affine vertex chart the strict-transform equation is Q^3=r^3 P. The chart T^3=P, Q=rT is finite over it, and off r=0 its inverse is T=Q/r. At branch directions (P,Q) are analytic parameters by transversality and (T,r) are regular parameters of the new chart. Elsewhere on r=0 the nonzero T derivative and the smooth conic give regular charts. The exceptional fiber is the reduced connected triple cover of the conic and is one-dimensional, so no extra component of the finite smooth chart lies over r=0. The charts are compatible by the weights of r and T; they give the normalization near the fiber. Riemann–Hurwitz at 18 index-3 directions gives genus 16, hence no rational exceptional (-1)-component. The line of the ambient blow-up restricted to the curve is its normal line, giving rho*O(-2) and square -6; independently D^2=4*3 and the 18 simple basepoints subtract 18. The cyclic pushforward on the conic is O⊕O(-6)⊕O(-12), yielding h^1 of the conormal powers as stated, not a formal-neighborhood argument. The cyclic cover and S_Q are normal by the isolated hypersurface singularities criterion; the 18 basepoint exceptionals map onto lines, not into the exceptional divisor of the resolution. Compactly supported Euler additivity gives 70 via fibers of sizes 3,1,0 and affine lines, and subtracting the 12 ordinary cubic-cone contributions from 459-70 gives 293. Running python3 -B /workspace/repairs/4/verify.py verifies the transverse conic and incidences over Q(zeta), normal-bundle arithmetic and both Euler decompositions, not the normalization argument itself.

## originality

PASS

PASS only for the repaired geometric result. The frozen package makes the vertex Milnor number a separate new claim, but the distinct published Milnor-jump record covers it exactly. The correction removes it as novelty, keeps it as a cited consistency check, and focuses on the normalized vertex blow-up and its minimal exceptional curve and normal bundle. The initiating paper's basepoint/conic contraction mechanism is prior and now more explicitly credited. No priority ordering between the two same-date records is inferred from their dates.

## value

PASS

The repaired resolution describes the distinguished, highly singular contraction in the motivating projective abelian model. It distinguishes what the normalized vertex blow-up actually resolves from the mere existence of a birational cyclic-cover model, determines the complete exceptional support and normal bundle, and checks the potentially problematic 18 branch directions. This is a local geometric invariant and concrete construction; the known Milnor computation alone would not carry value as a new result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
