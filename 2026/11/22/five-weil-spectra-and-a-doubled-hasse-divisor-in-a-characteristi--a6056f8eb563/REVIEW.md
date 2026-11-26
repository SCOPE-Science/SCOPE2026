# Independent mathematical audit

## correctness

PASS

The derivative gives squarefreeness exactly for a²≠4; the degree-ten monic model is genus four with two points at infinity. The inversion quotient has coordinates t=x+x^{-1} and v=y(x+1)/x³, with v²=(t+2)(t⁵−5t³+5t+a), and these generate the fixed field because x solves a quadratic over them. The trivial rotation eigenspace in H¹ vanishes by the genus-zero rotation quotient. The inverse-character eigenspaces are swapped by inversion; Frobenius commutes with both operators, so the determinant on each such pair is the square of the determinant on its inversion-invariants, giving the square Weil numerator via the genus-two quotient. Independent direct counts of C in degrees 1 through 4 reproduce the full squared polynomials: in the five table rows they are (4,114,1084,14314), (24,154,1224,14634), (14,204,1274,13924), (14,164,1334,15124), (4,194,1564,14314). E has 10 rational points. Only the last Q is an elliptic square, and comparing the first two coefficients of Q(T) and Q(−T) distinguishes the ten spectra. The point-count-only assertion in frozen RESULT.md line 38 overstates the original check: C counts in degrees one and two do not by themselves certify the whole degree-eight equality. The cohomological proof establishes it, and independent degree-three and degree-four counts supply the full numeric check here. For the geometric assertion, only diagonal exponents are divisible by five; extraction in (z²+az+1)^5 gives coefficients of z² and z⁴ equal to 5−a² and 5a⁴−3a²−1, paired by reciprocity. For h₂/5, the associated quadratic in a² has nonsquare discriminant 6 and roots in F₁₂₁ of norm 2, a nonsquare in F₁₁. Hence neither root is a square in F₁₂₁ and the quartic is irreducible, giving the degree-four orbit. The h₁ roots ±4 are simple, disjoint from that orbit, and all six roots are smooth parameters. The paired diagonal entries give determinant multiplicity two; rank and stable rank coincide because iteration preserves diagonal support over the perfect geometric field, including with the Cartier scalar roots. Independent replay and counts: /workspace/branches/d785003e-4200-40ab-b131-01a899ecb78f/independent_check.py and independent_check.txt. The uploaded verifier was inspected, not executed.

## originality

PASS

The distinct supported content is the full F₁₁ marked Weil and twist census and its link to the explicit ordinary/nonordinary strata. The family and diagonal Cartier coefficient mechanism are prior, and the characteristic-11 matrix calculation is a specialization of that mechanism, not a new general theorem.

## value

PASS

A complete base-field isogeny and twist census on this natural symmetry pencil distinguishes fibers that a first trace cannot separate and identifies a unique elliptic fourth power. The exact support, multiplicity and Frobenius splitting of the Hasse divisor locate the geometric exceptions and show which lie among the marked arithmetic classes. The value is the combined exact classification, not the routine coefficient formula alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
