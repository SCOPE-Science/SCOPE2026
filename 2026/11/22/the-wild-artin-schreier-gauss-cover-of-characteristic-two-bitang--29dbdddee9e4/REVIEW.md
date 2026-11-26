# Independent mathematical audit

## correctness

PASS

The gradient (bX²Z,0,bX³) gives tangent parameter t=X/Z at all smooth points; the lone geometric point with X=0 is [0:a^(1/4):1], singular. In the X=1 chart put z=Z/X=1/t, y=Y/X and u=y²/b. Then u²+u=(a/b²)z⁴+(c/b²)z²+z/b+D. Put α=(a/b²)^(1/4), η=(c/b²)^(1/2)+α. Translating u by α²z²+ηz gives v²+v=D+λz, where λ=1/b+η and λ⁴=Δ/b⁴. The simple pole forbids a trivial Artin–Schreier class and this factor has field k(v). Since dz/dv=1/λ, du/dv=1+η/λ=1/(bλ)≠0, so adjoining y is genuinely purely inseparable of degree two. Perfection gives the resulting field k(v^(1/2)); the argument also works over the algebraic closure, so proves geometric integrality, with no component supported on X=0, and yields the displayed normalized map with the 2/2 degree split. In the separable cover v→t the only candidate ramification lies at v=∞; at w=1/v the nontrivial automorphism sends w to w/(1+w), with displacement of order two, giving lower jump one and different exponent two. Its unique point above zero specializes on the full normalization to the singular point. For each t≠0 including infinity, the line section is a quadratic in the squared coordinate with nonzero linear coefficient, giving two smooth geometric contacts of multiplicity two. On a perfect field the radicial square-root step preserves rationality. The Artin–Schreier trace test applies with z=0 at t=∞; z ranges over all of F_q and the affine trace has q/2 values of each parity. Unsplit roots are exchanged by Frobenius. An independent finite-field replay reconstructed y=√b(s+αz+√η√z), z=(s⁴+s²+D)/λ, and compared all rational smooth points and rational-fibre sizes directly for all 4, 144, 3136, and 57600 allowed tuples at q=2,4,8,16 (replay: /workspace/branches/independent-replays/audit_gauss_points.py). That check does not replace the all-perfect-field proof or independently certify the ramification. Frozen checker read, not executed.

## originality

PASS

The family, concurrence and bitangent geometry are prior. Degree counting, ordinary Artin–Schreier ramification and trace theory, and the aggregate half-split conclusion are not credited as independent novel results. The supported distinct contribution is the explicitly normalized, coefficient-marked Gauss map and its exact line-by-line rational-contact law on the integral locus. The inspected bitangency and four-secant results do not identify the separable factor for this map or give the coefficient/line-dependent trace criterion.

## value

PASS

The concurrent bitangents of this natural quartic family have a marked dual line. The cover determines, over the ground field rather than just geometrically, the residual wild factor and which specific dual lines carry two rational rather than conjugate contacts. Two tuples with the same aggregate contact counts can give different line assignments, so the exact marked coefficient formula answers a question a point-count or a geometric classification does not. Its use is on the integral locus and not a classification of quartic isomorphism classes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
