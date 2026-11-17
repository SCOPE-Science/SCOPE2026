# Independent mathematical audit

## correctness

PASS

PASS: exact trihedral formula yields endpoint half-angle tangents bc/[(a+sqrt(a²+b²))(sqrt(a²+b²)+sqrt(a²+b²+c²))] and reversed for opposite endpoint; two middle solid angles equal atan(c/b) and atan(a/b). Holding b and a²+c² fixed, one endpoint decreases and the other increases as a passes c, so their minimum is strictly maximized at a=c. Then t=b/a gives symmetric endpoint F(t)=t/[(1+sqrt(1+t²))(sqrt(1+t²)+sqrt(2+t²))] with F'/F=(sqrt(t²+2)-t²)/[t sqrt(t²+1) sqrt(t²+2)], positive below sqrt2 and negative above. Thus unique upper bound 2atan(√2/(5+3√3)); at a=c=1,b=√2 both middle angles exceed the two matching endpoints, so it is the actual four-vertex maximin. Independent determinant geometry tests on 4000 arbitrary triples corroborated the value 0.2756427992162654 sr. Scope excludes degenerate shapes and general tetrahedra.

## originality

PASS

PASS, qualified: neither Akopyan–Karasev's universal minimum-solid-angle maximization for all tetrahedra (attained by the regular simplex) nor Licht's general shape comparisons evaluate the sharp optimum inside the proper orthoscheme family. The separate sharp μ versus Ω² orthoscheme result does not imply the optimum point or exact Ω*, since fullness itself varies. Checked fixed-shape Schläfli angle-sum theory also distinct. Older mesh literature may hide an equivalent restricted optimization; explicit residual risk.

## value

PASS

PASS: The minimum inward vertex solid angle is a natural tetrahedral mesh-quality invariant. A closed-form all-path maximin together with unique optimizer 1:√2:1 and demonstration that equal legs in all three positions are suboptimal gives a useful exact benchmark for orthoscheme quality and mesh element design. This is a full continuous shape-family classification, not a numerical special point.

The dated certificate retains the supplied scientific assessment, sources and limitations.
