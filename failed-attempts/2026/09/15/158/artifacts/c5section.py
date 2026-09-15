"""Search for reducibility in C5 via parametrization dimension + section.
Plan: parametrize rank<=3 locus: U 3x5, constraints X13=X14=X24=X25=X35=0 (5 quadrics in A^15).
Main component dim = 15 - 5 - dim(O(3))=15-5-3=7? Ambient A^10, codim 3, dim 7. Consistent w/ expected (n-1-minors, codim 3 for symmetric determinantal? dense symmetric I_{n-1} has height 3? For symmetric n x n, I_t has height ... I_{n-1}: height 3? codim = ... for symmetric determinantal: ht(I_t) = C(n-t+2,2)? For t=n-1: C(3,2)=3. Yes codim 3.)

So main component dim 7 in A^10. Extra components would show as other dims.

Direct computational attack on C5: Groebner in 10 vars, 15 quartics — too heavy for sympy lex, maybe grevlex partial OK.
Alternative: numeric monodromy-lite: intersect V with random rational 3-plane (codim 7) -> finite set; compute via homotopy?
sympy nsolve with 10 eqns... 15 gens + 7 linears = overdetermined; pick 10 eqns (7 linears + 3 gens)? misses components where
those 3 gens don't... hmm, better: pick random 3-plane L (7 linear eqns), then solve 7 linears + 3 random combinations? Still
only finds points where... Actually V cap L: substitute linear parametrization (3 params) into 15 gens -> 15 polys in 3 vars,
solve subset and verify. GB in 3 vars feasible!

Do: random integer 3-plane in A^10, substitute, compute GB (3 vars), count solutions (via lex/sturm or eigenvalue), record det values.
Repeat with several planes. If V irreducible deg D, get D points (over CC). Also track: do solutions split into different
"types" (e.g., clusters with different tangent behavior)? For primality this is weak, but for REDUCIBILITY with components of
same dim, monodromy across planes distinguishes: single plane can't prove irreducibility, but rational factorization of section
ideal can suggest.

STRONGER exact idea: work over QQ with the section ideal J = (15 substituted polys) in 3 vars: factor a generator? If J's
radical splits... e.g., if section polynomial factors persistently across MANY random planes into same-degree factors, evidence
of reducibility. If section is irreducible (Eisenstein etc.), evidence for irreducible (though section of irreducible can be reducible).

Even better: use FINITE FIELD point counting! #V(F_p) mod p distinguishes #components/dims via Weil. If V irreducible dim 7,
#V(F_p) = p^7 + O(p^{6.5})... need multiple p. Counting points in A^10 over F_p by brute force impossible (p^10). But random
sampling estimates... noisy.

Alternative PURE THOUGHT route: think about which graphs could FAIL.
- The irrelevant issue: most literature (e.g. "sparse symmetric determinantal ideals" / conditional independence ideals /
  Gaussian graphical models!) — the ideal I_{n-1}(X_G) for maximal minors relates to graphical models? For principal minors
  there's theчка... For (n-1)-minors of sparse symmetric: these are like " tournaments"? Hmm.

- Known result direction: For the generic symmetric matrix, I_{n-1} is prime (Kutz). Sparse versions studied by... 
  Boocher? "Free resolutions..."? Conca, De Negri, Gorla studied symmetric determinantal with zeros? There's work by
  Gorla–Migliore–Nagel on symmetric determinantal ideals? And "sparse determinantal ideals" by Boocher et al (generic matrix
  with zeros)? For the NON-symmetric sparse case (Boocher 2012?), maximal minors form Groebner basis under certain conditions,
  primality for certain zero patterns (e.g., Fettweis?). Hmm.

- Potential counterexample mechanism: if G has a separator... but 2-connected excludes separators of size <=1. Hmm, but for
  SYMMETRIC rank loci, the relevant connectivity might need to be higher! E.g., consider n=6, G = two K4s sharing... that has
  separator of size 2, still 2-connected? Sharing 2 vertices: removing 1 vertex keeps connected. So 2-connected allows
  2-separators. Rank-(n-2)=4 locus with a 2-separator might split?! 

Conjecture to test: n=4 minimal case fully (C4 prime?), then n=5 C5, then 2-separator graphs at n=5,6.

Let me first try the 3-plane section of C5 computationally.
"""
import sympy as sp
import random

a,b,c,d,e,p,q,r,s,t = sp.symbols('a b c d e p q r s t')
vars10 = [a,b,c,d,e,p,q,r,s,t]
M = sp.Matrix([
 [a,p,0,0,t],
 [p,b,q,0,0],
 [0,q,c,r,0],
 [0,0,r,d,s],
 [t,0,0,s,e],
])
gens = []
for di in range(5):
    for dj in range(di,5):
        rr=[x for x in range(5) if x!=di]; cc=[x for x in range(5) if x!=dj]
        gens.append(sp.expand(M.extract(rr,cc).det()))

random.seed(42)
u,v,w = sp.symbols('u v w')
plane = {}
for i,V in enumerate(vars10):
    plane[V] = random.randint(-2,2)*u + random.randint(-2,2)*v + random.randint(-2,2)*w + random.randint(-2,2)
print("plane:", plane)
sub = [sp.expand(g.subs(plane)) for g in gens]
print("num nonzero substituted:", sum(1 for f in sub if f != 0))
for f in sub:
    if f != 0:
        print("  deg", sp.Poly(f,u,v,w).total_degree() if f!=0 else 0, ":", str(f)[:120])
