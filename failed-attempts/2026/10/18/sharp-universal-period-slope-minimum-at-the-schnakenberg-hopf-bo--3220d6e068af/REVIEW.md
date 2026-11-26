# Independent mathematical audit

## correctness

PASS

At fixed 0<s<1, direct differentiation gives the trace mu and determinant s^2 and the stated scaled oscillator. Independently set q=r cos(theta), p=−r sin(theta), with G=q'−p in scaled time. Then r'=cos(theta)G and theta'=1−sin(theta)G/r. Writing c=cos(theta), v=sin(theta), the order-two and order-three parts of G/r are r g2 and r^2 g3 with g2=A c^2−Bcv, g3=C c^3−D c^2v and A,B,C,D as in RESULT.md. At mu=0 the mean cubic radial return term is (3C−AB)/8=−1/(8s^3): the term from varying r in the quadratic radial term integrates to zero because that primitive U has U(0)=U(2pi)=0. In the travel time per turn the linear term averages to zero, as does the term linear in mu; the quadratic coefficient is the mean of v g3+v^2 g2^2+U v g2 with U=A(v−v^3/3)+(B/3)(c^3−1). The three means are −D/8, (A^2+B^2)/16, and (5A^2−B^2)/48. Their sum is (9s^4−5s^2+1)/(24s^4). The linear radial growth has slope 1/(2s) in scaled time, hence along the stable Hopf cycle r^2 is 4s^2 mu to leading order. The analytic remainder can be justified by the analytic signed-section return map, dividing its fixed-point displacement by the initial radius and applying the implicit function theorem in mu. Half return interchanges the two signed section crossings as an analytic involution with derivative −1. In the odd coordinate induced by this involution both mu and the return time are even analytic, and mu has nonzero quadratic coefficient. Thus the remainder is O_s(mu^2). Monotone angle on the small branch makes one turn its least period; physical time divides scaled time by s. The normalized slope simplifies to [1+(3s−1/s)^2]/6, with equality only at 1/sqrt(3). Local nondegenerate supercritical Hopf supplies uniqueness and orbital asymptotic stability. No uniformity in s or global period law is needed. Inspected both frozen scripts without executing them; this independent return calculation is analytical rather than numerical shooting.

## originality

FAIL

Although Liu–Shi–Wang–Feng state only the leading period and evaluate only the real part of c1, their displayed exact homogeneous Hopf data determine its imaginary part by immediate substitution into the standard cubic coefficient formula. On their already matching parameter path the claimed period slope and its minimum then follow mechanically.

## value

FAIL

The slope is a meaningful physical observable, but the particular exact invariant and its minimum follow by retaining the imaginary part of published cubic data on the same unfolding, then completing a square. The independent derivation verifies correctness but does not leave a substantial separate scientific claim here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
