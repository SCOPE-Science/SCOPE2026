# Independent mathematical audit

## correctness

PASS

For sorted triangle sides a≥b≥c, fixed 0<η<1, the explicitly placed area-η subtriangle with perimeter W=a+ηc+sqrt((1−η)a²+ηb²−η(1−η)c²) provides a universal witness for the maximum contained-perimeter profile. Coordinates u=b−c,v=a−b,w=b+c−a>0 yield an exact nonnegative quadratic identity q²−(u+dv+rw)²=2(1−r)uw+(2/3)(2−η−r)v[2u+(2−η+d)v+(2−η)w], r=sqrt(1−η+η²), d=(2−η+2r)/3. Thus R≥fP+κ(a−c), f=(1+η+r)/3, κ=2(1−f), strict for non-equilateral triangles. Known fixed-triangle theorem proves equality at equilateral. Perimeter monotonicity and (1,1,ε) degeneration prove κ best possible, and compact cone zero-locus proves unique degeneration. Independent SymPy identity and sampled positive-cone computations support the nonnegative remainder proof.

## originality

PASS

Qualified PASS: the exact fixed-triangle optimal perimeter is prior in Ait El Manssour–Fattah–Ftouhi (2026), but its minimization over triangle shapes with a sharp side-spread penalty κ, unique equilateral minimizer and only thin 1:1:0 sharpness are not stated in accessible primary abstract or indexed comparison. Full original primary text was not available; an implication of its stronger explicit formula remains a priority risk, but the new global inequality requires an additional nontrivial cone optimization.

## value

PASS

An optimal stability coefficient measuring the exact penalty for departure from equilateral symmetry and its sole degenerating near-extremizers is a natural refinement of the known optimal-perimeter profile, with a globally sharp inequality over all triangular containers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
