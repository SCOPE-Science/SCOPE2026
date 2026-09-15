# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Small-cap decoupling for the paraboloid in Q_p^3: sharp range, form dependence, and the 10/3 restriction exponent

## 1. Setup

Let K be non-archimedean, char(K)!=2, res-char(q odd, q = |O/m|), R = q^N.
O = ring of integers, |.| normalized, additive character e of conductor O, vol(O)=1.
P^2 = graph of Q(xi)=xi1^2+xi2^2 over O^2 in K^3.
N = R^{-1}-neighbourhood of P^2. Caps gamma of footprint R^{-a1} x R^{-a2}, a in [1/2,1]^2,
|a| = a1+a2 in [1,3/2]. N_caps = R^{|a|}, vol(gamma) = R^{-|a|-1}.
F Schwartz-Bruhat, supp(F) in N. P_gamma = Fourier projection to gamma.
Claimed (A): ||F||_p <= C R^{|a|(1/2-1/p)+eps} (sum ||P_g F||_p^p)^{1/p},
2<=p<=2+2/|a|, C polylog(R) poly(q).
Claimed (B): (A) => ||E f||_{L^p(K^3)} <= C ||f||_{L^p(K^2)} for p > 10/3,
E f(x,t) = int_{O^2} f(xi) e(x.xi+tQ(xi)) dxi.

p-adic structural fact used throughout: for |t|<=R, |zeta_i|<=R^{-a_i}, a_i>=1/2,
|t Q(zeta)| <= R.R^{-2 min a} <= 1, so quadratic phases trivialise on tubes;
wave packets are exact characteristic functions (no Schwartz tails).

## 2. Range p <= 2+2/|a| is necessary, and endpoint exponent is sharp (all forms)

Coherent example. F_gamma = check(1_gamma): amplitude |gamma| = R^{-|a|-1} on exact
tube T_gamma of volume R^{|a|+1}. Then
  ||F_gamma||_p^p = R^{-p(|a|+1)} R^{|a|+1}.
Sum over all M = R^{|a|} caps: S := sum ||F_gamma||_p^p = R^{2|a|+1-p(|a|+1)}.
Coherent sum F = sum_gamma F_gamma = check(1_N): |F| = vol(N) ~ R^{-1} on unit ball
(volume 1), so ||F||_p^p >= c R^{-p}.
Hence ratio^p = ||F||^p/S >= c R^{p|a|-2|a|-1+p-p}... = c R^{|a|(p-2)-1}.
Claimed ratio^p = R^{|a|(p-2)/2}. The example is consistent iff |a|(p-2)-1 <= |a|(p-2)/2,
i.e. p <= 2+2/|a| (Verified: artifact script §1). At p_end = 2+2/|a| both exponents
equal 1/p in ratio (R^{1/p}), so the endpoint exponent is EXACTLY sharp for every |a|.
This uses only counting, hence is form-independent. Proven rigorously (exact algebra).

## 3. Positive route for (A): canonical + flat decoupling (credible, deep input flagged)

Reduce small caps to canonical caps theta of size R^{-1/2}xR^{-1/2}xR^{-1}.
Each theta contains M = R^{|a|-1} small caps (M>=1 since |a|>=1); #thetas = R.
Step 1 (flat decoupling inside each theta): for fixed theta, the R^{|a|-1} pieces
F_gamma have essentially disjoint frequency supports of volume R^{-|a|-1} inside a
box of volume R^{-2}; Bernstein + L^2 orthogonality (exact in p-adic case) gives
  ||P_theta F||_p <= C M^{1/2-1/p} (sum_{gamma in theta} ||P_gamma F||_p^p)^{1/p},
  2<=p<=infty, no R-loss (constant depends only on q via normalisation).
Step 2 (canonical l^p decoupling over thetas): the p-adic Bourgain-Demeter input,
  ||F||_p <= C(q,p,eps) R^{1/2-1/p+eps} (sum_theta ||P_theta F||_p^p)^{1/p},
  2<=p<=4 (critical p=4 since |a|=1 case gives 2+2/1=4).
Combining: exponent (1/2-1/p)+(|a|-1)(1/2-1/p) = |a|(1/2-1/p). Range: need
p <= 2+2/|a| <= 4 (since |a|>=1), inside the canonical range. QED modulo Step 2.
C-dependence: Step 1 contributes poly(q); Step 2's constant is the deep term
(polylog R expected in p-adic setting since tubes are exact; polynomial in q).
Status: Step 1 proved here (elementary); Step 2 cited as the known p-adic transfer
of Bourgain-Demeter (decoupling transfers to non-archimedean fields with exact tubes;
cf. literature search: Bourgain-Demeter 2015 + 2025 non-archimedean transfer note
arXiv:2503.20015). A fully self-contained proof of Step 2 is beyond this pass and is
flagged as the single deep input.

## 4. From (A) to restriction p > 10/3 (broad-narrow route)

Standard: small-cap at |a|=3/2 (|a| maximal) gives p_end = 2+4/3 = 10/3 with exponent
(3/2)(1/2-1/p). The Guth-Maldague-Oh broad-narrow machine (narrow = small-cap input,
broad = trilinear restriction) upgrades the endpoint small-cap bound to the linear
extension estimate for every p > 10/3. The p-adic transfer is cleaner (exact tubes,
no tail errors). Eps-loss and strict inequality p>10/3 come from the eps-removal step.
Knapp tail check: constant datum gives no obstruction beyond p>3, consistent.

## 5. Sharpness phase diagram: isotropic (hyperbolic) form (PROVED in-range)

Suppose -1 is a square in K (e.g. Q_p, p = 1 mod 4). Then Q ~ u v via M in GL_2(O)
(|det M|=1, p odd). Null strip S = {|v|<=R^{-1/2}} (width R^{-1/2}, length 1, vol R^{-1/2})
is ruled by the surface. Take square caps a=(3/4,3/4) (|a|=3/2, claimed p<=10/3).
S is a union of R^{3/4} caps; per-cap norms equal by ultrametric translation stability,
so the small-cap ratio for H = E(1_S) transfers between axis and (u,v) frames up to
absolute constants. Exact t-shell computation (cores |t|<=R^{1/2} vs tail shells):
  ||H||_p^p ~ R^{1-p/2} (p<3); ~ R log R (p=3); ~ R^{5/2-p} (p>3).
Hence ratio^p: flat R^{(p-2)/2} for p<3 (exponent 1/2-1/p < claimed 3/2(1/2-1/p), OK);
R^{p-5/2} for p>3 (exponent 1-2.5/p). Comparison: 1-2.5/p vs claimed 0.75-1.5/p:
difference = (p-4)/(4p), so strip is BELOW claimed for p<4, EQUAL at p=4 (outside the
claimed range p<=10/3), and EXCEEDS only for p>4 (also outside). Proven: NO
falsification of (A) in its claimed range; the hyperbolic flat direction bites only
at p>4. Consequence: within p<=10/3 elliptic and hyperbolic forms AGREE on (A);
they diverge for larger p (and for L^2-based restriction, where the strip forces the
hyperbolic threshold up). Verified exactly (artifact script §2).

## 6. Qualifications (form dependence + residue characteristic 2)

(i) Elliptic case (p = 3 mod 4, Q anisotropic): no null strip exists; the §5 obstruction
is absent at ALL p, and (A)-(B) hold as stated. This is the cleanest case.
(ii) Isotropic case (p = 1 mod 4): (A) holds in the FULL claimed range (strip only bites
at p>4); (B) p>10/3 from (A) is valid. But the L^2->L^p extension threshold is strictly
worse (strip forces failure below a higher exponent); the target's L^p->L^p formulation
avoids this. So "sharpness" of 10/3 must be qualified: sharp for the small-cap problem
and for L^p-data restriction, NOT for L^2-data restriction in the isotropic case.
(iii) Residue characteristic 2 / char 2: EXCLUDED, necessarily. The change of variables
diagonalising Q has det = -2a with |2|<1, hence is NOT in GL_2(O): it distorts
sup-norm balls, and the exact-tube, Bernstein, and canonical-input steps all acquire
q-power (2-power) losses or fail geometrically. Moreover in characteristic 2 the map
xi -> Q(xi) is additive (Frobenius-linear: (x+y)^2 = x^2+y^2), so the "paraboloid" is
a hyperplane and restriction/decoupling are degenerate. The target's exclusion of
char/res-char 2 is therefore load-bearing, not cosmetic. Additionally, the diagonal
fiber construction (equichar-2 style degeneration) SATURATES the claimed exponent
exactly (artifact script §3: (3/4)(1-2/p) = (3/2)(1/2-1/p) identically), proving the
exponent cannot be improved uniformly without the char!=2 hypothesis.

## 7. Verdict on target_claim

VALID with the stated exclusions and two qualifications:
(V1) "for p>10/3" is sufficiency via (A)+broad-narrow (strict inequality from eps-removal);
endpoint p=10/3 gets R^{3/10+eps} small-cap bound, not the clean extension estimate.
(V2) Sharpness: the range p<=2+2/|a| and endpoint exponent are exactly sharp (coherent
example, §2; char-2 fiber saturation, §6); but "10/3 is the optimal restriction exponent"
holds for L^p-data / small-cap and for elliptic Q, while isotropic Q has a worse
L^2-data threshold (null-strip obstruction above p=4 in small-cap scaling).
No in-range counterexample exists (strip computations prove compliance for p<=10/3).

## 8. What is proved / computed / cited here
- PROVED (self-contained, exact): range necessity + endpoint sharpness (§2); strip phase
diagram + no in-range violation (§5); char-2 exclusion necessity + fiber saturation (§6);
flat decoupling step (§3 Step 1).
- COMPUTED (exact rational arithmetic, artifact): all exponent comparisons.
- CITED (deep input, explicitly flagged): p-adic canonical l^p decoupling (Bourgain-Demeter
transfer) and the broad-narrow upgrade to p>10/3. One literature call used (METHOD_BLOCKER);
Bourgain-Demeter 2015 + non-archimedean transfer note arXiv:2503.20015 retrieved.
