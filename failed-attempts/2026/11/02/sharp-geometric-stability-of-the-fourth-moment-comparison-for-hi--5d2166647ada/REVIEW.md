# Independent mathematical audit

## correctness

PASS

Conditionally expand the square of ||v||²+a²+2<v,X>; the term linear in <v,X> has mean zero. The martingale and Rademacher sum both have second moment equal to the partial sum of squared lengths. The fourth-moment increments therefore differ by 4 E[a²||v||²−<v,X>²], which telescopes. For nonzero v and a, d²=2a²(1−c), giving the exact ratio 2(1+c) of the defect integrand to the weighted squared distance wherever the latter is positive. Orthogonal independent fair steps attain R/D=1/2 and positive angles approaching zero give the limit 1/4. Zero integrands imply radial alignment at every nonzero state; conditional centering gives fair signs on that event, and neither defect nor distance imposes a direction at zero. Zero-length steps contribute nothing. Inspected CHECK.py: quartic moments and transverse term are rational; the angular-distance tests use floats, and the examples are not a proof of the universal statement.

## originality

FAIL

The highlighted defect is the direct quartic fixed-length slack of the cited earlier pointwise comparison, not a new comparison mechanism. The distance constants and equality are immediate sharp consequences of the same slack and one elementary angular identity. The prior paper does not explicitly print the frozen final statement, but no independently substantive addition survives the implication check.

## value

FAIL

The weighted distance is a useful way to teach what loss in the comparison measures, but the frozen claim does not obtain a stability conclusion beyond algebraically rewriting the existing pointwise slack. In particular it does not approximate a martingale by an extremizing process in a path metric or constrain directions at resets. As a standalone result the routine specialization and its elementary endpoint examples do not clear the scientific-value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
