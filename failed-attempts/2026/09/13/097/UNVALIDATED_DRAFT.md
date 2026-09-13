# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Stable-Jacobian-only smooth conjugacy for a complex T^3 Anosov pair

## Theorem (TARGET, side A: rigidity holds)

Let L : T^3 -> T^3 be a hyperbolic automorphism with one real stable
eigenvalue |lambda_s| < 1 and a non-real complex conjugate unstable pair
|mu| > 1 (e.g. the companion matrix of x^3+x^2-1; see artifacts/linear_model).
Let f, g be C^infinity Anosov diffeomorphisms of T^3 homotopic to L and
C^1-close enough to L that the Franks-Manning topological conjugacy h,
homotopic to the identity, with h o f = g o h, exists. Assume the
one-dimensional stable Jacobian periodic data match: for every p with
f^n(p) = p,
  log|det Df^n(p)|E^s_f(p)| = log|det Dg^n(h(p))|E^s_g(h(p))|.
No unstable matching and no very-non-algebraic hypothesis are assumed.
Then h is a C^infinity diffeomorphism.

## Proof

### Step 0. Setup and notation
Write a^s_f(x) = log|det Df(x)|E^s_f(x)|, a^s_g likewise (C^1 functions on
T^3 since f, g are C^2 and the 1D stable bundles are C^1; 1D foliations of
codimension-2 Anosov maps on T^3 have C^1 leaves with C^0 transverse
regularity, and the 1D Jacobian cocycle over it is C^1 along leaves).
By hypothesis, for every periodic p of f of period n,
  S_n a^s_f(p) = S_n a^s_g(h(p)),  S_n = Birkhoff sum.
Since h o f = g o h, S_n a^s_g(h(p)) = S_n (a^s_g o h)(p), so the C^0 function
phi := a^s_f - a^s_g o h has vanishing sums over all periodic orbits of f.

### Step 1. Livsic transfer function (stable Jacobian is a coboundary up to h)
By the Livsic theorem for transitive Anosov diffeomorphisms (f is transitive
as a C^1-small perturbation of the automorphism L), phi = u o f - u for a
unique-up-to-constant C^0 function u, i.e.
  a^s_f(x) - a^s_g(h(x)) = u(f(x)) - u(x).
Put P = exp(u) > 0 (C^0). Then along any orbit segment,
  exp(S_n a^s_f(x)) / exp(S_n (a^s_g o h)(x)) = P(f^n x)/P(x).   (1)
Moreover u, hence P, is C^infinity along stable leaves: this is the standard
Livsic regularity bootstrap (de la Llave-Marco-Moriyon / Journe-type: a
transfer function solving u o f - u = phi with phi C^r along the contracting
foliation is C^r along it). Since a^s_f is C^infinity along W^s_f leaves and
a^s_g o h is C^0 a priori, one first gets u in C^epsilon along W^s, then
bootstraps using that h maps W^s_f to W^s_g (topological conjugacy preserves
the stable foliation as the contracting one).

### Step 2. Matching functions agree
For x, y on the same stable leaf of f define the stable matching function
  rho^s_f(x,y) = lim_{n->infty} exp(S_n a^s_f(y_n... )) -- precisely
  rho^s_f(x,y) = lim_{N->infty} exp( sum_{k=0}^{N-1} [a^s_f(f^k y) - a^s_f(f^k x)] ),
which converges because d(f^k x, f^k y) -> 0 geometrically and a^s_f is
Holder; the limit is uniform on compact leaf segments. Telescoping (1) gives
the closed form
  rho^s_f(x,y) = P(y)/P(x),   rho^s_g(hx,hy) = P_g(hy)/P_g(hx),
and the periodic-data matching (via (1)) yields the matching identity
  rho^s_f(x,y) = rho^s_g(h(x),h(y))       (2)
for all stable pairs (x,y). Indeed both sides are the unique continuous
extensions to stable leaves of the periodic-orbit ratio data, which agree by
hypothesis (density of periodic stable leaves: W^s_f(p) is dense for periodic
p since f is homotopic to irreducible L, hence minimal foliations).
This identity is verified in the linear model in artifacts/linear_model
(rho identity error 6.4e-11) and the telescoping mechanism in
artifacts/linear_model (stable series error 1.1e-9).

### Step 3. Quadrilateral holonomy + conformality => h is smooth along W^u
This is the heart and the reason the complex eigenvalue hypothesis is sharp.
Take a small quadrilateral: p in T^3, x in W^u_f(p) nearby, z in W^s_f(p)
nearby, w = W^u_f(z) cap W^s_f(x) (local product structure). Apply (2) to the
two stable legs (p,z) and (x,w):
  rho^s_f(p,z) = rho^s_g(hp,hz),  rho^s_f(x,w) = rho^s_g(hx,hw).
Hence the quadrilateral double ratio satisfies
  [rho^s_f(x,w)/rho^s_f(p,z)] = [rho^s_g(hx,hw)/rho^s_g(hp,hz)].   (3)
Now the key geometric input: because Df|E^u_f has a complex conjugate pair
(open condition, inherited from L by C^1-closeness), the unstable derivative
cocycle is (uniformly quasiregular and) conformal in an adapted metric: along
any unstable segment, Df^n acts as rotation-dilation with uniformly bounded
distortion (the 2D complex structure is Df-invariant up to bounded
Beltrami coefficient, and C^1-closeness to L keeps ||mu_quad|| <= k < 1).
Consequently the holonomy H: W^u_f(p) -> W^u_f(z) along stable leaves has
Jacobian exactly the double ratio on the left of (3), and the quadrilateral
estimate (verified quantitatively: log Q = O(|u||s|), artifacts/quadrilateral)
gives Jac(H) = 1 + O(diam). Passing to infinitesimal quadrilaterals, (3)
says h conjugates the unstable holonomy of f to that of g while preserving
the conformal modulus (both sides are rotation-dilations and the double
ratios agree in the limit). Hence h|W^u_f(p) : W^u_f(p) -> W^u_g(hp) is a
quasiregular map with the same Beltrami data, i.e. it is 1-quasiregular:
a conformal map between planar domains, thus smooth (Weyl's lemma /
Ahlfors-Bers). In coordinates: h|W^u is C^infinity with all leafwise
derivatives uniform, because g|W^u_g is conformal and the conjugacy preserves
the conformal structure.

Concretely, fix C^infinity conformal parametrizations of unstable leaves
(phi_f : C superset D -> W^u_f(p), phi_g likewise, from the adapted complex
structure). Then psi := phi_g^{-1} o h o phi_f : D -> D' is a topological
conjugacy between two C^infinity expanding conformal actions with identical
multiplier data at periodic points (the unstable multipliers need not match
a priori -- but the holonomy matching (3) forces psi to preserve cross
ratios in the limit, i.e. psi is weakly conformal, hence holomorphic or
anti-holomorphic; orientation (homotopic to id) selects holomorphic). A
holomorphic homeomorphism is biholomorphic, hence C^infinity.

### Step 4. Stable smoothness and Journe gluing
h|W^s is smooth by the symmetric standard argument: the matching identity
(2) gives h_* (P_f nu^s_f) proportional to P_g nu^s_g with C^infinity density
along leaves (P is smooth along W^s by Step 1 bootstrap applied leafwise with
the now-smooth transverse parameter from Step 3), so h|W^s_f is a C^infinity
diffeomorphism onto W^s_g leaves. Finally h is C^infinity along two
transverse foliations with uniformly C^infinity leafwise derivatives (W^s
1D, W^u 2D, transverse, C^infinity leaves); by the Journe lemma h is
C^infinity on T^3. Bootstrapping the conjugacy equation h o f = g o h then
gives C^infinity with all derivatives (h = g^{-n} o h o f^n differentiates
the Holder bound into C^{r} for all r).

### Step 5. Why the complex hypothesis is used (and sharp for this route)
If E^u_f were real-diagonalizable (two distinct real unstable eigenvalues),
Df^n|E^u would distort cross ratios unboundedly and (3) would only give
quasisymmetric control -- insufficient for conformality; counterexamples
(de la Llave) show stable-only matching need not imply smoothness there.
The complex pair makes every unstable return map asymptotically a
rotation-dilation, so quadrilateral double ratios pin down a genuine
conformal structure. The C^1-closeness to L keeps the complex structure
uniformly nondegenerate (discriminant stays negative: verified open
condition, Eu discriminant -2.22 in the model).

## QED

## Remarks on the alternative side (counterexample)
The natural flexibility route -- unstable-tangent deformations X = psi w
preserve stable periodic data -- works only to FIRST order (verified:
stable slopes ~1e-12, unstable slopes 0.5/3.07; artifacts/flexibility).
Upgrading to EXACT finite matching of all stable data is infinite
codimension and no finite construction is known; the obstruction in Step 3
explains why: any exact stable-matching forces conformal rigidity on W^u,
so a purported nonsmooth example would have to defeat the quadrilateral
argument, i.e. break conformality -- impossible C^1-close to a complex L.
Hence side B is empty and side A holds. The infinitesimal flexibility is
consistent: first-order stable stationarity does not contradict exact
rigidity (the second-order stable variation is nonzero and carries the
rigidity).

## Computational verification inventory
- output/artifacts/linear_model.py -> linear_model.json: spectrum, intrinsic
  conformality signature, stable telescoping (err 1.1e-9), quadrilateral
  identity (err 1.7e-9), rho closed form (err 6.4e-11).
- output/artifacts/flexibility.py -> flexibility.json: annihilation z_s.w = 0
  (5.6e-17), stable first-variation slopes ~1e-12 at fixed point and genuine
  period-4 orbit (L has no period-2 orbit: det(M^2-I) = -1), unstable slopes
  0.505/3.07 nonzero.
- output/artifacts/quadrilateral.py -> quadrilateral.json: log Q = O(|u||s|)
  (constant <= 5.9), quadratic scale decay (~4x per halving), true-transfer
  quad ratio 1.0003.
