# Better: think structurally. Perhaps I should use the KNOWN Amano construction directly.
# Amano (2007) "Arithmetic of certain non-abelian extensions": for primary pi1,pi2 with (pi1/pi2)_3=(pi2/pi1)_3=1,
# there exist alpha in O_K with N_{K1/K}(alpha)=pi2... Actually the Redei field is obtained from solutions of
#   x^3 + pi1 y^3 + pi1^2 z^3 - 3 pi1 xyz = pi2 * w^3  (homogeneous norm equation!)
# i.e. N(X,Y,Z) = pi2 * W^3 with X,Y,Z,W in O_K — a projective variety. Then theta=(X+Y t+Z t^2)/W has norm pi2.
# My t4 search found N(X,Y,Z)=pi2 exactly (W=1). For Galois-equivariance, Amano shows the extension defined this
# way IS dihedral/Heisenberg Galois over K automatically. So why did the cocycle test fail? Possibly:
# (a) my cocycle condition is wrong (wrong power/convention), or (b) theta must satisfy extra congruence
# (primary / mod-9 condition) for the extension to be Galois with right ramification, or (c) box too small for D.
#
# Actually wait: the Galois closure of K1(cuberoot Th)/K: Gal(K1/K)=<sigma>. sigma extends iff sigma(Th)=Th'*cube
# where Th' is... the conjugates of cuberoot(Th) are cuberoot(sigma^i(Th)). R contains cuberoot(Th); for R/K Galois,
# need cuberoot(sigma(Th)) in R. Since N(Th)=pi2, sigma(Th)*Th... hmm, sigma(Th) = N(Th)/(Th*sigma^2(Th)) = pi2/(Th*sigma^2(Th)).
# cuberoot(sigma(Th)) = cuberoot(pi2)/(cuberoot(Th) cuberoot(sigma^2(Th))). So R contains it iff cuberoot(pi2) in R
# and cuberoot(sigma^2(Th)) in R. cuberoot(pi2)? R=K1(cuberoot Th); pi2=N(Th)=Th*sigma(Th)*sigma^2(Th), so
# cuberoot(pi2)=cuberoot(Th) cuberoot(sigma Th) cuberoot(sigma^2 Th) — circular. The Galois closure is
# K1(cuberoot Th, cuberoot sigma Th) which has degree up to 27 over K... and the Heisenberg extension is a
# SUBFIELD/quotient? Hmm, actually the full Redei extension R contains cuberoot(pi1), cuberoot(pi2) already? No...
#
# Let me step back and recall the actual structure (Amano-Mizusawa-Morishita):
# K=Q(mu_3). K1=K(pi1^{1/3}). R=K1(theta^{1/3}) with N(theta)=pi2. Then R contains K(pi1^{1/3}, pi2^{1/3})? Since
# N(theta)=pi2, pi2^{1/3} = ... theta^{1/3} sigma(theta)^{1/3} sigma^2(theta)^{1/3}, NOT obviously in R.
# The claim in literature: R/K IS Galois with group the Heisenberg group of order 27 (when theta chosen right),
# ramified exactly at pi1,pi2 (and maybe lambda?). The mechanism: R/K Galois requires the cocycle condition;
# Amano proves it can be arranged. The condition might be that theta ≡ 1 mod (3?) or that Th is chosen via the
# specific solution of the norm equation with congruence conditions.
#
# KEY ALTERNATIVE: maybe I have the wrong norm equation orientation. In Redei's original (Q case): for p1,p2 with
# (p1/p2)=1, solve x^2 - p1 y^2 - p2 z^2 + ... hmm that's Hilbert symbol. For cubic: Amano's equation might be
# N(theta)=pi2 with theta in K1 AND theta ≡ ... mod lambda.
#
# PRAGMATIC PIVOT: Instead of building the full Galois closure abstractly, directly construct the Heisenberg
# extension as the GALOIS CLOSURE: R = K1(cuberoot(Th), cuberoot(sigma Th)) — adjoining both cube roots gives
# a Galois extension of K? Gal group: over K1, adjunction of two cube roots: degree up to 9; over K total up to 27.
# Then verify [R:K]=27 computationally (via Frobenius/discriminant methods) and compute Artin symbol of pi3.
# But computing in degree-27 fields explicitly is heavy.
#
# CLEANER PIVOT: use class field theory / ray class group to construct the Heisenberg extension directly?
# Without PARI/Sage, implement ray class group of K modulo pi1*pi2? Hmm, K has class number 1; ray class group
# mod m = (O_K/m)^*/units image. The maximal elementary-abelian-3 extension unramified outside {pi1,pi2,lambda}...
# The Heisenberg extension is NON-abelian over K though (abelian over K1). Construct as: abelian C3xC3 over K1?
# R/K1 should be C3 (Kummer by theta), and K1/K is C3, total Galois group Heisenberg (non-abelian of order 27,
# exponent 3). The non-abelianity comes from sigma acting nontrivially on Gal(R/K1). For R/K to be Galois of
# degree 27, need exactly the cocycle condition.
#
# Let me test MANY theta solutions and check the cocycle condition with a WIDEorable but smarter test:
# Q = sigma(Th)/Th is a cube in K1 iff for every prime q of K1 (test set), the local cubic character is trivial
# in the right sense... equivalently (using Kummer): Q mod P is a cube for all P not dividing 3*Q. Test with
# several split primes of K1. That avoids huge box search. Actually simplest robust test: Q is a cube in K1 iff
# Q = C^3 with C possibly fractional: equivalent to the principal ideal (Q) being a cube ideal AND ... no, need
# unit part too. Use local test at multiple primes: pick rational primes l ≡ 1 mod 3 splitting in K, then in K1?
# This is getting deep. ALTERNATIVE: solve for theta DIRECTLY with the equivariance built in via norm equation
# over the BIQUADRATIC... 
#
# ===== TOTALLY DIFFERENT, RIGOROUS & TRACTABLE ROUTE: Massey product via explicit Galois cohomology =====
# The triple symbol = triple Massey product <chi1,chi2,chi3> in H^2(G_K, F3). Nonvanishing can be witnessed by
# a defining system: cochains evaluated on Frobenius elements — i.e., by unramified-outside-S class group data.
# Concretely (Sharifi/Morishita): with S={pi1,pi2,pi3,lambda}, let chi_i be Kummer characters. A defining system
# for <chi1,chi2,chi3> needs kappa in C^1 with d kappa = chi1 ∪ chi2, i.e., kappa corresponds to theta via Kummer
# (theta solves N=pi2 up to...). Then the Massey value on (sigma, tau) pairs... The representing 2-cocycle
# evaluated at (Frob_pi3, ...) gives the symbol. This is the same theta computation as above.
#
# ===== PRAGMATIC DECISION =====
# The mathematically standard object: Redei extension R = K1(cuberoot theta), claimed Galois over K. If my theta
# gives non-Galois R/K, the FIX per Amano is to choose theta satisfying theta ≡ 1 mod lambda^? (3-adic condition).
# Let me look at it from the units angle: ambiguity in theta is theta' = theta * gamma^3 * epsilon where
# epsilon in O_K1^* (units) with N(epsilon)=1... The cocycle class [sigma(theta)/theta] in K1^*/K1^*3 has norm 1;
# changing theta by gamma^3 doesn't change the class; changing by units/elements of norm... N(theta)=pi2 fixed
# means ambiguity = elements of norm 1 mod cubes. The condition is that this class is trivial. Different W in
# N(X,Y,Z)=pi2 W^3 (W≠1) give DIFFERENT thetas not differing by cubes! So search with W≠1.
# Let me just do a broad search: N(X,Y,Z) = pi2 * W^3 for small nonzero W, collect thetas, test cocycle via LOCAL
# cube tests (fast), and find one passing. Local test: D^3=M solvable mod many primes => use Chebotarev-ish filter.
print("see t12")
