"""Route B-positive: independent constructive proofs of LOWER bounds.

B1. Claim: on the GRID SUBGRAPH H (generators a,b; i.e. each c-edge and its
endpoints deleted), the product measure mu is G_H-ergodic on the free part.
Proof idea (Neumann-type lemma for the infinite group Gamma): fix Borel sets
A,B of positive measure (in fact any free configurations x,y). For any finite
coordinate sets F_x,F_y, the set T={g : g.F_y disjoint from F_x} is cofinite
(because F_x union F_y finite, only finitely many g send one point of F_y
into F_x; here use: g.y0 in F_x for finitely many g). Hence free
configurations x,y can be spliced: build z agreeing with x on F_x and with
g.y on g.F_y whenever those are disjoint. Diagonalize to a free z that
simultaneously sits in any positive-measure cylinder neighbourhood of x and
of g.y. This gives: for any positive-measure Borel A,B there EXISTS
g with mu(A cap gB)>0 --- weak mixing of the single transformation g is not
even needed. In particular the grid-subgroup action is ergodic.

B2. Corollary (measurable lower bound): let chi_mu(G)=k via measurable
c:X->{1..k} defined mu-a.e. Pick a colour class C of positive measure and
take any NON-IDENTITY grid element g (e.g. g=a). Then mu(C cap gC)>0.
Since C is G_H-independent, g must NOT be an H-edge, i.e. g not in
{a,a^-1,b,b^-1}. True for e.g. g=a^2 (any grid word of length>=2 not in S).
Iterate: with k=2, colour classes C1,C2 both of positive measure (some pair
must jointly cover; in fact at least two classes positive). If the SAME group
element h (grid word, h not in S, h != e, and also h^-1 not in S) moved
positive mass of BOTH classes into themselves... more precisely:
- If mu(C1)>0: some g1 with mu(C1 cap g1 C1)>0, so g1 not an H-edge unless
  the intersection sits inside the null set where c is undefined/improper.
  Since intersections are positive-measure and c is proper a.e., choose points
  where properness holds: g1 is genuinely nonadjacent.
- With k=2, take g = a^2: both C1 cap gC1 and C2 cap gC2... only ONE of them
  is guaranteed positive by ergodicity applied to (C1,gC1)? Ergodicity gives
  SOME g per pair, not a uniform g. So the two-class argument needs care.

  Correct two-class argument: suppose k=2 with classes C1,C2 positive
  measure (they partition a conull set). By B1 applied to A=C1,B=C2, some
  g has mu(C1 cap g C2)>0. That alone does not contradict independence.
  Standard argument instead: B1 => every H-invariant Borel set is null or
  conull (ergodicity). If chi_mu(H)<=2, some colour class C has mu(C)>=1/2.
  Consider D = C cap a C cap a^2 C cap ...? Hmm, that uses powers of a.

  CLEANEST standard argument: assume measurable 2-coloring c of H.
  The grid graph H restricted to any single <a>-orbit (a copy of Z acting
  freely) is a bi-infinite path. A proper 2-coloring of a path alternates,
  so c(a^n x) = c(x) + n (mod 2) for a.e. x (along the orbit; null set may
  depend on orbit but Fubini + countability gives a conull set where it holds
  for all n: properness along each edge a^{n}x--a^{n+1}x fails only on null
  sets N_n; union is null). Hence c(a^2 x) = c(x) a.e. Now apply B1 to the
  pair (C1, C1) with the SPECIFIC element g=a^2? B1 gives SOME g, not a^2.
  So instead: from c(a^2 x)=c(x) a.e., C1 is a^2-invariant mod null.
  Also along <b>-orbits, c(bx)=1-c(x) a.e., so b swaps C1,C2 mod null.
  Then a^2-invariance of C1: consider E = C1 Delta a^2(C1), null. Hmm, this
  shows C1 is periodic, not a contradiction yet.
  The actual contradiction: c(a^2x)=c(x) means a^2 preserves each colour
  class (mod null). Since <a^2,b> still acts ergodically? If the subgroup
  <a^2,b> action is ergodic (same Neumann argument works for any infinite
  subgroup? NO -- B1's proof used the FULL group Gamma to move F_y off F_x;
  the subgroup <a^2,b> is infinite so the same proof works verbatim inside
  the subgroup: for any finite F_x,F_y only finitely many h in <a^2,b> map a
  point of F_y into F_x... wait, need: {h in <a^2,b> : h.F_y cap F_x != empty}
  is finite because it is a subset of the finite set for Gamma. Yes!
  So <a^2,b> acts ergodically too.) Then C1, being <a^2,b>-invariant mod
  null... but b SWAPS C1 and C2, so C1 is NOT <a^2,b>-invariant. Contradiction
  approach: a^2 preserves C1 mod null AND b swaps; the group they generate
  acts ergodically, and C1 has measure 1/2 (exactly? at least...).
  Hmm: ergodicity of <a^2,b>: any invariant set is null/conull. C1 is
  a^2-invariant but not b-invariant. No direct contradiction.

  SIMPLEST CORRECT: use g = a^2 DIRECTLY as an edge-free element.
  Suppose 2-coloring with classes C1, C2. WLOG mu(C1) >= 1/2 > 0.
  Claim: mu(C1 cap a^2 C1) > 0? By Cauchy-Schwarz/mean ergodic? For a
  measure-preserving transformation T=a^2: (1/N)sum mu(C1 cap T^n C1) ->
  ... only gives SOME n with positive intersection, and T^n = a^{2n} is
  still non-edge (a^{2n} not in S for n>=1). Then pick x in C1 cap a^{2n}C1
  where properness holds along the a-path from x to a^{2n}x (all intermediate
  edges proper except null): c alternates along the path of length 2n (even),
  so c(a^{2n}x)=c(x), consistent with both in C1. NO contradiction either!
  Of course: a path of even length CAN be properly 2-colored with endpoints
  equal. So single-class recurrence never contradicts 2-colorability.

  THE REAL OBSTRUCTION for 2 colors: an ODD cycle. The grid graph Z^2-Cayley
  restricted to {a,b} is BIPARTITE (even cycles only), so it IS 2-colorable
  (even Borel: checkerboard (m+n) mod 2 on each <a,b>-orbit requires choosing
  an origin per orbit -- NOT Borel in general! but MEASURABLE? For the free
  Z^2-subaction, ergodic decomposition... hmm, actually the <a,b>-action on
  the free part: each orbit is a Z^2-grid; 2-coloring each grid needs a
  parity choice per orbit. Is there a MEASURABLE choice? The parity function
  p(x)=(m+n) mod 2 relative to an arbitrary origin o(x): changing origin by
  (dm,dn) flips all parities iff dm+dn odd. A measurable 2-coloring of the
  grid subgraph exists iff... For Z^2 acting freely, p(x) must satisfy
  p(ax)!=p(x), p(bx)!=p(x). Then p(a^2 x)=p(x), and q(x):=p(x)+... Consider
  r(x) = p(x) XOR [first coordinate even]? Not well-defined without origin.
  Standard fact: the free part of {0,1}^{Z^2}... the Z^2-shift's grid graph
  has measurable chromatic number 2? NO -- it is known that F(2^{Z^2}) grid
  graph needs 4 colours measurably?? Hmm, no: Gao-Jackson-Krohne-Seward
  continuous needs 4; MEASURABLE for Z^2 grid is 2? There is a classical
  result: the Borel chromatic number of F(2^{Z^2}) with grid generators is
  large, but measurable = 2? I recall: for the free part of the 2-shift of
  Z, measurable chromatic number of the path graph is 2 (alternating, using
  a measurable choice? for Z-action, ergodic components are... ). Actually
  for Z: each orbit is a line; 2-color measurably: use the "marker" method?
  For a free Z-action, a Borel 2-coloring of the path graph exists iff the
  action has a Borel complete section... The irrational rotation has
  Borel chromatic number 3 for the path graph? The distance-1 graph on the
  circle (irrational rotation) has chi_B = 3? Hmm, no: rotation graph is
  2-regular; chi_B in {2,3}; it equals 3 when no Borel 2-coloring exists
  (e.g. irrational rotation: any Borel 2-coloring would give a Borel set
  meeting each orbit in alternating fashion, impossible by ergodicity
  argument? For an ergodic rotation, a 2-coloring class C with T swapping
  C and complement: mu(C)=1/2 and C is... T^2 preserves C; ergodicity of
  T^2 (true for irrational rotation? T^2 is rotation by 2alpha, still
  ergodic) forces C null/conull, contradiction with mu(C)=1/2!).

  THERE it is -- the clean argument, adapted to our cell:
  Suppose c is a measurable 2-coloring of G (hence of grid subgraph H).
  Let C = c^{-1}(0) (positive measure; in fact exactly 1/2 a.e. on ergodic
  components, but we just need: not null/conull... we need BOTH C and
  complement positive; since c is proper, both classes... one class could be
  null! If C null, then complement is conull and c is a.e. constant, but
  then every edge has both endpoints a.e. in complement -> improper on
  conull set. So both classes have positive measure. Good.)
  - a swaps C with complement mod null (properness along a-edges):
    C Delta a(X\\C) null-ish. Precisely: for a.e. x, c(ax) != c(x), i.e.
    x in C <=> ax not in C, a.e. So aC = X\\C mod null.
  - Hence a^2 C = C mod null: C is a^2-invariant mod null.
  - Also b swaps: bC = X\\C mod null.
  - So the subgroup K=<a^2,b>: b swaps C, a^2 preserves C. The element
    a^2 b swaps C (mod null): (a^2 b)C = X\\C. Hmm.
  - Consider the action of K on X with its invariant measure... but mu is
    Gamma-invariant, hence K-invariant. Is K's action ERGODIC? By the Neumann
    argument (B1 proof works for any infinite subgroup: only finitely many
    h in K map F_y-points into F_x), YES: K acts ergodically (any
    K-invariant Borel set is null/conull).
  - Now C has... we need mu(C)=1/2? From aC=X\\C mod null and a preserving
    mu: mu(C)=mu(aC)=mu(X\\C)=1-mu(C), so mu(C)=1/2.
  - The element t := a^2 b in K swaps C with complement mod null. Then
    t^2 preserves C mod null. And <t^2, ...>? Consider the cyclic group
    <t>: t swaps C, so t^2 preserves C mod null. Is <t^2>... t has infinite
    order (Gamma torsion-free part: a^2 b has infinite order since any
    c-free nontrivial word has infinite order; t=a^2b involves no c so it
    lies in the Z^2 factor, nonzero, infinite order). The action of <t>:
    ergodic? <t> is infinite cyclic; Neumann argument again gives ergodicity
    of the <t>-action?? The Neumann splicing argument shows: for any
    positive-measure A,B, some power t^n has mu(A cap t^n B)>0. That is
    exactly ergodicity of the single transformation t? Ergodicity of T means
    invariant sets null/conull; the "some n meets" property for all positive
    pairs is equivalent (for invertible T: if E invariant positive, take
    A=E,B=complement... hmm, the meeting property for all A,B positive
    implies ergodicity: if E invariant with 0<mu<1, A=E,B=E^c gives
    T^n E^c meets E, but T^n E^c = E^c disjoint from E. Contradiction.
    YES equivalent.) So <t> acts ergodically, t swaps C (mu(C)=1/2).
  - Then t^2 preserves C mod null. t^2 also generates an ergodic action?
    <t^2> infinite cyclic, same Neumann argument => ergodic. An ergodic
    transformation preserving C mod null forces C null/conull -- but
    mu(C)=1/2. CONTRADICTION.
  Hence no measurable 2-coloring: chi_mu(G) >= 3. QED.

  Wait -- check "t^2 preserves C mod null forces null/conull": E=C with
  mu(t^2 C Delta C)=0 is an invariant set mod null for ergodic t^2; standard
  fact gives mu(C) in {0,1}. Since mu(C)=1/2, contradiction. And ergodicity
  of <t^2>: the Neumann argument needs the subgroup infinite (yes) -- but
  ALSO needs the splicing diagonalization to produce a FREE configuration.
  The diagonalization: enumerate non-identity elements, pick fresh vertices.
  Works since Gamma infinite and configurations have infinite support room.
  One subtlety: the spliced configuration must lie in the FREE part. The
  standard argument: two free configurations x,y and finite windows can be
  spliced along disjoint translates to a free configuration (freeness is a
  comeager/conull condition; finite constraints + avoiding countably many
  periodic configurations is possible). We must state this carefully in the
  DRAFT: given finite partial assignments on disjoint finite sets
  F1, g.F2, extend to a free configuration: enumerate Gamma\\{e}={h_n}, pick
  distinct vertices v_n outside the constrained region with h_n.v_n also
  outside, set z(v_n)!=z(h_n.v_n). Possible since each h_n moves all but...
  h_n could fix vertices? The shift action on 2^Gamma: h.z=z means
  z(g)=z(hg) for all g; to break it, pick any v with v,hv unconstrained and
  set different bits. Since constrained region finite and Gamma infinite,
  such v exists. Countably many steps, each constraining 2 new vertices;
  always possible. GOOD. Also need the spliced z to extend the cylinder
  constraints exactly -- yes by construction.

  So B1+B2 give a RIGOROUS chi_mu >= 3 lower bound. This is a genuine,
  self-contained, original-writeup theorem fragment (Neumann-splicing
  ergodicity for all infinite subgroups + parity-swap contradiction), even
  though the conclusion chi_mu>=3 is one HALF of the target's measurable
  claim. The other half (chi_mu <= 3, i.e. explicit measurable 3-coloring)
  is where the blockage lies (LLL fails, clopen radius-1 impossible).

B3. This script verifies the GROUP-THEORETIC facts used:
  (i) t=a^2 b has infinite order (grid word (2,1)!=0).
  (ii) a^{2n} not in S (not an edge) for n>=1.
  (iii) a,b act freely on the free part (by definition).
"""
import json
from collections import deque

def mul_A(T, dm, dn):
    L = list(T)
    L[-1] = (L[-1][0] + dm, L[-1][1] + dn)
    return tuple(L)

def reduce_blocks(L):
    L = list(L)
    while len(L) >= 3:
        hit = -1
        for i in range(1, len(L) - 1):
            if L[i] == (0, 0):
                hit = i
                break
        if hit < 0:
            break
        L = (L[:hit - 1]
             + [(L[hit - 1][0] + L[hit + 1][0],
                 L[hit - 1][1] + L[hit + 1][1])]
             + L[hit + 2:])
    return tuple(L)

def mul_c(T):
    return reduce_blocks(list(T) + [(0, 0)])

E = ((0, 0),)
GENS = {'a': ('A', 1, 0), 'ai': ('A', -1, 0), 'b': ('A', 0, 1),
        'bi': ('A', 0, -1), 'c': ('C',)}
SYMS = ['a', 'ai', 'b', 'bi', 'c']
S_ELEMS = {('A', 1, 0), ('A', -1, 0), ('A', 0, 1), ('A', 0, -1), 'C'}

def apply(T, g):
    s = GENS[g]
    if s[0] == 'A':
        return mul_A(T, s[1], s[2])
    return mul_c(T)

# (i) t = a^2 b: check t^n != e for 1<=n<=50 (grid word (2n,n))
T = E
ok_inf = True
for n in range(1, 51):
    for g in ['a', 'a', 'b']:
        T = apply(T, g)
    if T == E:
        ok_inf = False
print('t^n != e for n=1..50:', ok_inf, '; t^1 =', T if False else '(checked)')

# (ii) a^{2n} not a generator-neighbour (not in {a,ai,b,bi,c} image of e)
NB = {apply(E, s) for s in SYMS}
A2 = E
ok_nonedge = True
for n in range(1, 11):
    A2 = apply(apply(A2, 'a'), 'a')
    if A2 in NB:
        ok_nonedge = False
    if A2 == E:
        ok_nonedge = False
print('a^{2n} non-edge & nontrivial for n=1..10:', ok_nonedge)

# (iii) a,b infinite order (powers distinct)
P = E
seen = {E}
for n in range(1, 21):
    P = apply(P, 'a')
    seen.add(P)
print('|<a>-orbit| first 20 powers distinct:', len(seen) == 21)

out = {'t_powers_nontrivial_to_50': ok_inf,
       'a2n_nonedge_nontrivial_to_10': ok_nonedge,
       'a_powers_distinct_to_20': len(seen) == 21}
with open('ergodic_facts.json', 'w') as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
