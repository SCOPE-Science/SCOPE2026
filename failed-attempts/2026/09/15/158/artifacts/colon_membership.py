"""Saturation probes: I : m for various generators m.
colon_det gave {1}: I:det = whole ring => det in sqrt(I)?? Actually (I:det^inf)? No:
(I:det) with single det (1-t*det) gives elements f with f*det^k in I for... precisely
I:det^inf cap R = ker(R -> (R/I)_det). Result {1} means (R/I)_det = 0, i.e. det is NILPOTENT mod I,
i.e. det^N in I for some N! Since det is irreducible(?) that would mean det in sqrt(I) but det not in I
(nonzero matrix can have vanishing 3-minors? no wait det is degree 4, gens degree 3).

Check: is det in the radical? That means V(I) = V(I + (det)) = rank<=2 locus entirely, i.e. every
matrix with vanishing 3-minors automatically has det=0?? For 4x4 that's FALSE in general (identity has
3-minors = ... wait identity 3-minors are all 1 or 0? I_3(Id) = (1)! Hmm for symmetric full case rank 4
matrices are NOT in V. But SPARSE identity: diag(1,1,1,1) with zeros: 3-minors: M33=abc=1 != 0. So identity
not in V. Consistent with det nilpotent? No! If det^N in I then V(I) subset V(det). Is that plausible?
V(I) consists of sparse matrices of rank<=2 (need proof) — all have det 0. So YES plausible: V(I) subset V(det)
just says every point of V has det 0, i.e., no rank>=3 point in V. The numeric hunt suggested exactly that!

But wait — (I:det)={1} via 1-t*det trick computes I:det^inf, and =R means det nilpotent mod I.
Hmm, but actually careful: sympy lex GB gave {1}?? That means 1 in (I, 1-t det), i.e., det is... yes, det in sqrt(I).
Hmm, but is that right? sympy might have failed? It returned single poly "1" with no t — meaning GB={1},
ideal is whole ring, so saturation is whole ring. Let me double check with different order and verify the
certificate: find N and cofactor representation det^N in I? Try N=1: is det in I? Reduce det by grevlex GB.

Also note: det^N in I for C4 would be a striking structural fact. For general graphs? The (n-1)-minors
forcing det=0 would mean rank<=n-2 automatically?? That's FALSE for dense symmetric (identity has I_{n-1}=(1)).
But on the sparse locus... hmm, actually for ANY matrix, I_{n-1}=0 minors does NOT imply det=0 in general
(e.g. diag(1,1,1,0)? has minors... M with det 0... take diag(1,1,0,0): 3-minors all 0, det 0. Take diag(1,1,1,1):
3-minors nonzero. A matrix with all 3-minors 0 but det!=0 would have adjugate=0 but det!=0, impossible since
adj(M)*M = det*M... adj=0 => det=0 (as det^{n-1} = det(adj)). CLASSICAL: I_{n-1}(M)=0 entries => adj=0 => det=0
for ANY matrix over a domain! Indeed det(M)^{n-1} = det(adj(M)). So det in sqrt(I_{n-1}) ALWAYS, for any matrix,
with N = n-1: det^{n-1} = det(adj) in I_{n-1} (each term of det(adj) is product of n-1 entries of adj, each in I).
Duh — trivial. So colon_det={1} is expected universally. NOT an obstruction. Good sanity check though.

So the real question remains: is I prime / radical? V = rank<=2 locus (set-theoretically? need: does I_{n-1} cut out
rank<=n-2 set-theoretically on the sparse space? YES universally: V(I_{n-1}) = {rank <= n-2} intersect sparse space,
since rank<=n-2 iff all (n-1)-minors vanish. So V(I) = W_{<=2} = W_2 union W_1 union W_0 (rank strata).
Irreducibility of V = irreducibility of rank<=2 sparse symmetric locus.

So: is {X in Sym_C4 : rank<=2} irreducible? Rank<=2 = image of U(2x4) with 2 constraints, PLUS rank<=1, plus 0.
The map U -> X: U in A^8, constraints u1u3+v1v3... wait constraints are X13=0,X24=0 i.e. two bilinear equations on U=A^8.
Zero set Z in A^8: complete intersection? two bilinear forms. Is Z irreducible? Then image irreducible, but image
might miss rank<=1 boundary? No—image includes all ranks<=2 by symmetric diagonalization (char 0: every symmetric
rank<=2 matrix = U^T U for 2x4 U — over alg closed field yes).

So V(I) irreducible iff Z = {(u,v): u1u3+v1v3=0, u2u4+v2v4=0} ... hmm wait indices: u=(u1..u4) row1, v row2.
constraints: u1u3+v1v3=0 and u2u4+v2v4=0. Each is a quadric cone. Is intersection irreducible? Product structure:
vars split {1,3} and {2,4}: Z = Z13 x_{shared?} ... no: first eq involves u1,u3,v1,v3; second u2,u4,v2,v4. DISJOINT variable
sets! Z = Z13 x Z24 where Z13 = {u1u3+v1v3=0} in A^4, Z24 similarly. Each quadric hypersurface in A^4 is irreducible
(XY+ZW is irreducible quadric). Product of irreducible = irreducible. So Z irreducible, V = image irreducible? Image of
irreducible is irreducible, and V = image (every rank<=2 sym matrix factors). But careful: image is constructible; V = closure
of image? Every rank<=2 symmetric matrix over alg.closed char!=2 is U^TU — yes exact image. So V irreducible as a SET.

So V(I) is IRREDUCIBLE for C4! Then I prime iff I radical. Non-radical? Possible (Ih... symmetric determinantal ideals are
perfect/radical in dense case, but sparse?). Test radicality: find f^n in I with f not in I, or check I:(radical test).
Sympy: try to see if I is radical via... hard. Probe: pick random linear form L, check L^2 in I? Or use Jacobian criterion:
if V irreducible and R/I generically reduced (smooth point exists with Jacobian rank = codim), then I radical? Not quite
need also... if I has embedded components... For unmixed + generically reduced => radical? I is... hmm.

We found smooth rank-2 points with jac rank 3 = codim (8-5). So generically smooth along main component. If I is unmixed
(all associated primes same dim 5), then reduced at generic point => radical. Unmixedness: symmetric sparse determinantal...
Cohen-Macaulay? Unknown.

Practical radicality test: compute (I : f) for candidate f, or test whether Frobenius-like... In char 0: test I : J where J =
Jacobian ideal? If I radical, I : sing... hmm.

Alternative: try to PROVE prime via parametrization kernel = I. Kernel of phi: K[a..s] -> K[u,v], xij=uivj+... on sparse pattern.
ker phi is prime (image domain). I subset ker phi. Show ker phi subset I? Or ker phi subset sqrt(I) + dimension match + ...?
Standard route: show R/I is domain by exhibiting isomorphism to subring of polynomial ring: e.g., localize at a minor/product
and identify.

Concretely: invert D = M_{44} = abc - aq^2 - cp^2 (a principal 3-minor)? On D(s)=D(pqrs)? Hmm.

Better classical approach for dense symmetric submaximal minors (Goto/Kutz): R/I_{n-1} is domain of dim ... via induction:
I_{n-1} : (principal minor) etc. Let's attempt: colon I : D for D = diagonal 3-minor M33... we did I:p: result had 7 polys
vs I's 10 — strictly SMALLER set of generators?? Wait colon should be BIGGER ideal. Got 7 polys spanning... the 7 printed are
a SUBSET of I's generators (missing 3: M00=bcd-br^2-dq^2? Actually missing: bcd-br^2-dq^2? Let's see: colon elts were:
abc-aq^2-cp^2 [M33], abd-bs^2-dp^2 [M22], abr-p^2r+pqs [M23], adq+prs-qs^2 [M12], aqr+cps [M13], bcs+pqr-q^2s [M03],
brs+dpq [M02]. Missing from I: bcd-br^2-dq^2 [M00], acd-ar^2-cs^2 [M11], cdp-pr^2+qrs [M01].
Hmm colon SMALLER?? I:p must CONTAIN I. 7 polys but they might generate a bigger ideal than they appear (fewer polys can
generate bigger ideal). E.g. M00 might be combination. Need ideal membership: is M00 in (colon7)? Or is colon strictly bigger
with new elements not among I's? The 7 are all in I. Is (I:p) = (7 elts) strictly containing I? Check M00 in ideal(7)? If yes,
colon might equal I (p not zerodivisor, good sign for prime/CM). If colon strictly bigger (some h in colon7-ideal not in I),
then p is zerodivisor => I not prime (if also p not nilpotent...). But careful: even if I prime... I:p=I for p not in P.
"""
import sympy as sp

a, b, c, d, p, q, r, s = sp.symbols('a b c d p q r s')
M = sp.Matrix([
    [a, p, 0, s],
    [p, b, q, 0],
    [0, q, c, r],
    [s, 0, r, d],
])
rows4 = list(range(4))
gens = []
for di in range(4):
    for dj in range(di, 4):
        rr = [x for x in rows4 if x != di]
        cc = [x for x in rows4 if x != dj]
        gens.append(sp.expand(M.extract(rr, cc).det()))

# The 3 "missing" diagonal/offdiag gens:
M00 = sp.expand(b*c*d - b*r**2 - d*q**2)
M11 = sp.expand(a*c*d - a*r**2 - c*s**2)
M01 = sp.expand(c*d*p - p*r**2 + q*r*s)

colon7 = [
    sp.expand(a*b*c - a*q**2 - c*p**2),
    sp.expand(a*b*d - b*s**2 - d*p**2),
    sp.expand(a*b*r - p**2*r + p*q*s),
    sp.expand(a*d*q + p*r*s - q*s**2),
    sp.expand(a*q*r + c*p*s),
    sp.expand(b*c*s + p*q*r - q**2*s),
    sp.expand(b*r*s + d*p*q),
]
# membership: reduce M00 wrt groebner(colon7); if remainder 0 -> M00 in (colon7) -> consistent with colon=I?
G7 = sp.groebner(colon7, a, b, c, d, p, q, r, s, order='grlex')
print("GB of colon7 len:", len(G7.polys))
for cand, name in [(M00, "M00"), (M11, "M11"), (M01, "M01")]:
    red = G7.reduce(cand)
    print(name, "remainder:", str(red[1])[:200] if isinstance(red, tuple) else str(red)[:200])
