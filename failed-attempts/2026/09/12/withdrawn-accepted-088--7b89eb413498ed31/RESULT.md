# Disproof of mod-2 self-cup framing value at q2 over Q(sqrt2)

## Context
The admitted target asks for the mod-2 self-linking framing correction at the
unique prime above 2 for F = Q(sqrt2). Let O_F = Z[sqrt2], q2 = (sqrt2),
Y = Spec O_F, V = Y minus {q2}, with mod-2 etale cohomology and Artin-Verdier
trace. Let f in H^1(V, Z/2) be the generator ramified exactly at q2, given by
the Kummer class of the quadratic extension unramified outside q2. Since -1 is
not a square in F, the class [-1] is nonzero and the diagonal self-cup
f cup f = f cup [-1] need not vanish. The stated framing value to test is
trace(f cup f) = 1 in Z/2.

## Definitions
- F = Q(sqrt2), O_F = Z[sqrt2], disc(F) = 8, (2) = (sqrt2)^2.
- q2 = (sqrt2), the unique prime above 2, with norm 2.
- V = Spec O_F minus {q2}; 2 is invertible on V so mu_2 ~= Z/2 and Kummer theory applies.
- a = 2 + sqrt2 = (1+sqrt2)*sqrt2, N(a) = 2, (a) = q2.
- f = Kummer class (a) in H^1(V, Z/2).
- [-1] = Kummer class of -1, nonzero since -1 is not a square in F.
- (a,b) denotes the quaternion algebra class in Br(-)[2]; (a) cup (b) corresponds to [(a,b)].

## Result
The target claim trace(f cup f) = 1 is false. In fact f cup f = f cup [-1] = 0
in H^2(V, Z/2). Hence for every homomorphism out of H^2(V, Z/2), including the
Artin-Verdier trace pairing, the value on f cup f is 0, not 1.

## Proof / Evidence
1. Ring, prime, class number: O_F = Z[sqrt2], disc 8, q2 = (sqrt2) unique above 2.
   Minkowski bound (1/2)sqrt(8) = sqrt2 < 2 gives Cl(O_F) = 1, hence Pic(V) = 0.
2. Units and pinning f: O_F^times = {+-eps^Z} with eps = 1+sqrt2 of norm -1.
   O(V)^times/2 = <-1, eps, sqrt2> ~= (Z/2)^3. Certified sign table at the two real
   embeddings shows [a] with a = 2+sqrt2 is the unique nontrivial class that is
   totally positive and odd at q2; every other odd-at-q2 class is ramified at
   infinity. Since (a) = q2 has odd valuation at q2, F(sqrt(a))/F is ramified
   exactly at q2. Thus f = (a) is uniquely the generator ramified exactly at q2.
   N(a) = 2 is not a square in Q, so a is a nonsquare; -1 < 0 at both embeddings
   so [-1] != 0.
3. Cup identity: for Kummer classes (a) cup (a) = (a) cup (-1), i.e. (a,a) = (a,-1),
   from bilinearity and (a,-a) = 0 (witnessed by zero divisor i+j with i^2=a, j^2=-a).
4. Explicit splitting: with x = 1+sqrt2/2 and y = sqrt2/2 in F,
   x^2+y^2 = (3/2+sqrt2)+(1/2) = 2+sqrt2 = a.
   Since F(i)/F is quadratic, this says N_{F(i)/F}(x+iy) = a, so (a,-1) splits over F.
   Concretely I = [[x,y],[y,-x]], J = [[0,-1],[1,0]] satisfy I^2 = a, J^2 = -1,
   IJ+JI = 0, and {1,I,J,IJ} is an F-basis of M_2(F). The nonzero map
   (a,-1) -> M_2(F) is an isomorphism by simplicity and dimension 4 = 4, so
   [(a,-1)] = 0 in Br(F)[2]. All identities hold by exact rational arithmetic.
5. Descent: Kummer gives H^2(V, mu_2) -> Br(V)[2] with kernel Pic(V)/2 = 0, and
   Br(V) -> Br(F) is injective for regular integral V. Cup products commute with
   restriction, so f cup f maps to 0 in Br(F); by injectivity f cup f = 0 already
   in H^2(V, Z/2). Any trace homomorphism therefore gives 0.
The conclusion is independent of Artin-Verdier trace normalizations because the
class itself vanishes.

## Limitations
Scope is fixed to F = Q(sqrt2), the single-prime complement V = Spec O_F minus q2,
and mod-2 coefficients. No claim is made about other fields, other primes, or other
coefficients. The proof cites standard inputs (Minkowski bound, Dirichlet unit theorem
with explicit minimality check, Kummer sequence, quaternion-algebra facts, Br(X) -> Br(K)
injectivity) plus exact machine-checked identities.

## Reproducibility
Run output/artifacts/verify_selfcup.py with Python 3 using only exact Fraction
arithmetic. It checks discriminant/Minkowski, norms, a = eps*sqrt2, full S-unit sign
table, norm equation, matrix relations I^2=a, J^2=-1, IJ+JI=0, and rank 4 spanning.
Expected output ends with ALL EXACT CHECKS PASSED.

## References
- Artin-Verdier duality origins and extensions (Artin-Mazur, Verdier, Deninger,
  Deninger-Wingberg, Spiess, Bienenfeld, Demarche-Harari, Morin) for general duality
  background; no prior source computes this instance.
- Standard facts used: Minkowski bound, Dirichlet unit theorem, Kummer sequence,
  quaternion algebra bilinearity, (a,-a) = 0 splitting criterion, norm criterion for
  (a,-1), Br(X) -> Br(K) injectivity for regular integral schemes.
- Verification artifact: output/artifacts/verify_selfcup.py.
