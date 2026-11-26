# Independent mathematical audit

## correctness

PASS

The second-derivative determinant of e3 is -4h. Geometric completeness can be checked without relying on finite enumeration: with exactly three nonzero coordinates, h=0 forces their sum to vanish and a supported partial derivative is their nonzero product. With two nonzero coordinates, a missing-coordinate derivative is their product times their sum, so exactly the opposite-coordinate pairs are singular. With one nonzero coordinate all partials vanish. On the torus write h=(product x_i)(S U-4) with S=sum x_i and U=sum 1/x_i. Singularity there implies U=S/x_i^2 for all i, and SU=4; hence all x_i are of the same magnitude up to signs, with precisely a 3-to-1 sign split. In local coordinates u,v,w the leading forms at the three representatives are uv+uw+vw, -u(v+w)-(v-w)^2, and the negative of 2(u^2+v^2-w^2)-(u+v+w)^2. All are nonsingular modulo 5. The projective quartic is integral and normal by isolatedness; the A1 resolution is crepant with H^1(O)=0, so is K3. Every rational node has a smooth split exceptional conic over the finite field, adding q points. Independently enumerating canonical projective representatives over F5 and F5[t]/(t^2+3) reproduced 56 and 826, and the Jacobian enumeration and local ranks reproduced the 14 rank-three rational nodes. The resolved counts are 126 and 1176. The two Frobenius traces are 100 and 550; the second attains 22·25, forcing every squared eigenvalue to be 25 by the Weil bound. The first trace then yields twenty-one +5 and one -5. The K3 Tate theorem in odd characteristic gives the stated ranks over F5 and geometrically, and the trace formula gives both zeta functions.

## originality

FAIL

No exact characteristic-five Cayley zeta entry was found in the checked catalogue, but the prior Cayley Hessian lattice computation plus the general CM theorem for singular K3 surfaces already gives this spectrum. The exact rational model and good-reduction hypothesis can be checked directly, and the prior rational divisor description accounts for all twenty algebraic eigenvalues. The failure is established implication, not inferred priority from a date or an unavailable source.

## value

FAIL

The arithmetic of this classical Hessian is naturally motivated, but the precise Frobenius spectrum here is a specialization of the known CM rule to a model with a known rational rank-twenty divisor lattice and an elementary ordinary-node good-reduction check. Verifying the counts by enumeration is a useful consistency test, not an independent mathematical gain. The record establishes no further projective or arithmetic invariant beyond this implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
