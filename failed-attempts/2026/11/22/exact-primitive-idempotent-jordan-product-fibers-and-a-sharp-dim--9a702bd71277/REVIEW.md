# Independent mathematical audit

## correctness

PASS

The only scalar idempotents are 0 and 1. The nontrivial ones have scalar part 1/2 and vector part x/2 with Q(x)=1; a decomposition into two nonzero orthogonal idempotents cannot use the unit, and two proper parts would sum to scalar 1, so they are primitive. The ordered product determines s=x+y=4w and c=Q(s)/8. The change of variables x=s/2+z, y=s/2-z is a bijection to B(s,z)=0 and Q(z)=1-Q(s)/4. If s=0 the form is the original one; if s is nonisotropic the restriction has determinant D/Q(s); if s is nonzero isotropic, split off a hyperbolic plane of determinant -1 and count q lifts from a dimension-(d-2) form of determinant -D. Character orthogonality with G^2=chi(-1)q gives the stated even and odd signs, including the level zero, and the dimension-zero convention is necessary. Over an odd finite field, a nondegenerate form of dimension at least two represents every nonzero scalar and always represents zero by the zero vector. Thus all paraboloid targets occur at d>=4. In d=3 a nonzero isotropic s leaves a line representing 1 exactly when chi(-D)=1, giving 2q pairs then and none otherwise. The ternary zero level has q^2 vectors; the split d=2 case excludes every nonzero isotropic s. Bounded literal Cartesian-product checks agreed, including all 3,125 targets for each four-dimensional determinant class over F_5 and 24 omitted targets for the nonsplit-sign ternary example. The preserved replay paths are verify_idempotent_products.py and idempotent_output.txt beside RESULT.md; the frozen runs include characteristic-three and F_9 examples, not a universal certificate.

## originality

FAIL

The ordered product count is exactly the ordinary unit-sphere self-convolution at s=4w, not just an analogue. The distinct catalogue result deadda507c3b gives that individual convolution in all even dimensions in its proof. Gogić–Tomašević's earlier Lemma 3.1 directly gives the underlying spin-factor multiplication and perpendicular-space parameterization. Its stated support theorem is over quadratically closed fields, not finite fields; nevertheless the algebraic bijection in its proof uses only invertibility of 2. In odd finite-field dimensions the purported extra counts are then a direct substitution into the classical single-level quadratic representation formula, using the determinant of a perpendicular complement or of a hyperbolic-plane quotient. In particular the remaining ternary condition is exactly representation of 1 by a line of square class -D. The failure concerns equivalent coverage and mechanical implication, not a claim that the earlier article explicitly tabulates the finite-field fibers. No chronological ordering of same-day catalogue findings is inferred.

## value

FAIL

Exact Jordan-product fibers are natural, but the even-dimensional result recasts an existing exact convolution, and the remaining finite-field dimension transition and odd fibers follow directly from the known parameterization by inserting standard quadratic level counts. The anisotropic versus isotropic split changes only the determinant or deletes a hyperbolic plane; the ternary obstruction is the usual square-class test in dimension one. The frozen statement does not establish a distinct nonroutine invariant beyond these implications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
