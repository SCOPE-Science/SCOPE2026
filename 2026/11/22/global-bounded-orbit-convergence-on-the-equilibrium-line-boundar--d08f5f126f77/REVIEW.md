# Independent mathematical audit

## correctness

PASS

With b=11/10 and a=0, direct differentiation gives (z+by+x-x^2/2)'=-alpha z^2. A bounded maximal forward orbit continues for all time and has a nonempty compact invariant omega-limit set, connected as the intersection of the nested closures of connected orbit tails. For alpha of either nonzero sign, W has a finite limit and is constant on the limit set, which therefore lies in z=0. There y would be constant; if nonzero it makes x affine with nonzero slope and cannot satisfy (x-1)y=0 at all times. The remaining points are equilibria, with W restricted to x-x^2/2, so a level has at most two points and connectedness forces a singleton. For alpha=0, W=K fixes z as a function of x,y and yields the damped scalar second-order equation. Differentiating H_K gives -by^2 and its limit forces y=0; invariance forces z=0, and the same finite-fiber argument applies. For a compactly supported invariant probability, integration of the corresponding Lie derivative is legitimate by invariance and boundedness on the support. Either it forces z=0 or it forces y=0; support invariance again gives the equilibrium line. Every compactly supported probability on that line is invariant. This concerns recurrence, not a claim that every compact invariant set contains only equilibria, nor that all forward orbits are bounded. RESULT.md lines 19–53 and the verification files were inspected; the supplied SymPy script was not executed.

## originality

PASS

The supported distinct part is the nonzero-alpha equilibrium-line convergence and corresponding invariant-measure exclusion, covering both signs. The original Liu–Sang–Wang–Ahmad paper already gives W at a=alpha=0, and its proof entails the zero-alpha bounded-orbit convergence case even though Theorem 2 is stated in terms of chaos. Credit that slice rather than counting the whole line as previously untreated. No statement covering the nonzero-alpha part was identified in the compared sources.

## value

PASS

The equilibrium-line boundary is a natural degeneracy of the motivating jerk family, and even identifying an equilibrium omega-limit set would not by itself prove convergence to a point. The sign-independent nonzero-alpha mechanism and finite-level argument settle that issue and exclude compact nonstationary recurrence for both signs. The result is conditional on boundedness and does not purport to partition basins, but answers a substantive full-boundary dynamical question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
