# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Descendant two-contact scattering correspondence for (F1, H + (2H-E)): proof of equality for all admissible classes

## 1. Setup

Let pi: F1 -> P^2 be the blowup at one point, H = pi^*L, E the exceptional
curve. Intersection form in basis (H,E): H^2 = 1, H.E = 0, E^2 = -1.
K_{F1} = pi^*K_{P^2} + E = -3H + E, so -K = 3H - E.

Let D1 have class H (pullback of a line L avoiding the blown-up point) and
D2 have class 2H - E (strict transform of a smooth conic through the
blown-up point meeting L transversely away from it). Then:

- D1 is smooth rational (isomorphic to L).
- D2 is smooth rational (blowup of a smooth conic at one smooth point).
- D1 cap D2 consists of the two transverse L-cap-conic points, both away
  from E, hence two transverse nodes.
- [D1] + [D2] = 3H - E = -K_{F1}, so D = D1 + D2 is anticanonical.
- D1.D2 = H.(2H-E) = 2, D1^2 = 1, D2^2 = 3, K^2 = 8, all as expected.
- (X, D) is a Looijenga pair (rational surface + anticanonical cycle) with
  two components and two nodes.

Admissible classes: beta = aH - kE, a >= 2, 0 <= k <= a.
Write F = H - E (fiber). Then beta = aF + (a-k)E with a >= 0 and a-k >= 0,
a nonnegative combination of the effective generators F, E; hence every
admissible beta is effective, in fact nef (beta.F = a-k >= 0, beta.E = k
>= 0). Contact orders:

- c1 = beta.D1 = a (since H.H = 1, E.H = 0).
- c2 = beta.D2 = (aH-kE).(2H-E) = 2a - k (since E.(2H-E) = +1).
- Both are strictly positive on the subfamily (a >= 2), so the two maximal-
  contact conditions are genuine.
- D.beta = c1 + c2 = 3a - k = c1(X).beta, as required for log Calabi-Yau.

These numerics are verified by `output/artifacts/numerics.py`.

## 2. Key degeneracy: m(beta) = 0 for every admissible beta

Consider genus-0 log stable maps to (X, D) with n = 3 markings: two relative
markings of maximal contact orders c1, c2 and one interior marking with a
point insertion and psi^{m(beta)}.

Log virtual dimension (Gross-Siebert log formula): for a log CY pair,
c1(T_X(-log D)) = c1(X) - [D] = 0, so

  vdim log M_{0,3}(X,D,beta) = (dim X - 3)(1 - g) + n - 1 + c1^log.beta
                             = (2-3)(1) + 3 - 1 + 0 = 2.

Equivalently, by the relative formula,
vdim = -1 + c1(X).beta + n + l - sum(contacts) with l = 0 interior
markings counted separately gives the same value 2 because
sum(contacts) = D.beta = c1(X).beta cancels.

A point insertion has codimension 2. Hence the zero-dimensional condition
is 2 - 2 - m(beta) = 0, i.e.

  m(beta) = 0 for every admissible beta,

uniquely. The script verifies this for all a <= 7 (33 classes) and the
formula is beta-independent, so it holds for all admissible beta by the
closed-form computation above.

Consequences:

(a) The "descendant" invariant Db_beta is in fact primary: psi^0 = 1.
(b) The tropical side has one vertex of valency m + 3 = 3, i.e. an ordinary
    trivalent vertex with the standard (Mikhalkin) multiplicity 1-factor;
    no higher-valency descendant multiplicity appears.
(c) The descendant wall functions, descendant broken lines, and descendant
    multiplicities all specialize to their ordinary counterparts in the
    psi^0 sector. Concretely, any wall decorated by a positive psi power
    cannot contribute to a psi^0 coefficient, and the consistent completion
    projected to descendant order zero is the ordinary Kontsevich-Soibelman
    / Gross-Siebert consistent completion. Hence the "descendant scattering
    coefficient" at beta equals the ordinary scattering/broken-line
    coefficient at beta, and the "descendant tropical count" equals the
    ordinary tropical count with a point constraint.

Therefore the target claim is equivalent, on this subfamily, to the primary
two-contact scattering/tropical correspondence. No specifically descendant
correspondence input is needed beyond this specialization fact.

## 3. Toric model and the two-initial-wall diagram

F1 with its 4-component toric boundary is toric; its boundary sum is
E + (H-E) + H + (H-E) = 3H - E = -K (verified in script). Smoothing two
opposite nodes of the toric boundary merges the four toric divisors into
the two smooth components D1, D2 meeting in the remaining two nodes.
Thus (X, D) admits a toric model in the sense of Gross-Hacking-Keel:
it is obtained from a toric Looijenga pair by smoothing two boundary nodes.

Hence the standard scattering setup applies:

- The dual intersection complex (B, Sigma) with its affine structure with
  singularities has exactly two focus-focus singularities, one per smoothed
  node (the two surviving nodes D1 cap D2 carry no singularity).
- The initial scattering diagram has exactly two initial walls, one per
  smoothed node, with standard initial functions f_i = 1 + z^{m_i} (times
  the appropriate monomial tracking the exceptional data), i.e. the
  "explicit two-initial-wall" diagram of the claim, truncated to psi^0.
- By the Kontsevich-Soibelman / Gross-Siebert consistency lemma, the
  consistent completion S(D) exists, is unique up to equivalence, and is
  computed order by order with finitely many new walls at each order.
  Coefficient extraction (theta-function / broken-line product) is therefore
  well defined.

## 4. Scattering coefficient = tropical count (wall-crossing side)

This is the established Gross-Hacking-Keel / Gross-Siebert broken-line /
tropical correspondence: for a consistent scattering diagram, the product
of theta functions (broken-line product) at a general basepoint equals the
weighted count of tropical curves (resp. tropical disks) with a point
constraint through that basepoint, with wall-crossing functions recording
the counts. The proof is combinatorial (broken lines glue to tropical
curves and vice versa). It uses no GW input and holds in particular for
the two-wall completion above, in the ordinary (= psi^0) sector. Thus:

  scattering coefficient at beta = ordinary tropical count N^{trop}_beta
  with two unbounded legs of weights c1, c2 and one pointed trivalent
  vertex constrained to a general point P in B_0.

## 5. Log GW invariant = tropical count (correspondence side)

For the primary invariant (m = 0), the equality

  Db_beta = N^{trop}_beta

is the genus-0 toric-model Looijenga correspondence, available via either
of two established routes (we need only one; both apply and agree):

(i) Decomposition + toric vertex: the Abramovich-Chen-Gross-Siebert
    decomposition formula expresses the log virtual class as a sum over
    tropical types; imposing a general point constraint rigidifies the
    tropical type, and the Nishinou-Siebert / Gross-Siebert toric
    correspondence identifies each toric-vertex contribution with its
    tropical multiplicity. Because (X,D) has a toric model, a toric
    degeneration can be chosen so that all vertices contributing to the
    general-point invariant are toric; no exotic vertex contributions occur.

(ii) Frobenius / intrinsic mirror symmetry: the genus-0 Frobenius structure
    conjecture for toric-model Looijenga pairs (proved by Bousseau; in full
    generality by Gross-Siebert intrinsic mirror symmetry) states exactly
    that the theta-function structure constants (broken-line counts) equal
    the punctured/maximal-contact log GW invariants with a point insertion.
    Our Db_beta is (up to the standard relative-vs-punctured dictionary,
    which is an identity at maximal contact) such a 3-point structure
    constant: two incoming boundary directions of weights c1, c2 traced
    against the point class.

Hypotheses checked locally: beta effective and nef (Section 1), contacts
maximal and positive, point constraint general, genus zero, log CY
condition c1^log = 0, toric model exists (Section 3), psi^0 so no
descendant-log refinements needed (Section 2). Hence the cited
correspondence applies to every admissible beta uniformly; there is no
beta-dependent extra hypothesis (no rank, no positivity wall).

## 6. Theorem (target established affirmatively)

For every beta = aH - kE with a >= 2 and 0 <= k <= a, with c1 = a,
c2 = 2a - k and m(beta) = 0 as above,

  Db_beta = (consistent two-wall scattering coefficient at beta)
          = (tropical count with one pointed trivalent vertex),

i.e. the log invariant equals the coefficient prescribed by the consistent
completion of the two-initial-wall descendant scattering diagram (whose
psi^0 sector is the ordinary completion), via tropical correspondence and
wall-crossing. In particular no counterexample beta0 exists in this
subfamily; a rigorous counterexample would contradict the correspondences
invoked, whose hypotheses are verified above.

## 7. Computational verification

`output/artifacts/numerics.py` (run successfully) checks:
D1 + D2 = -K; D1.D2 = 2; toric boundary sum = -K; pa(D2) = 0;
effectiveness/nefness of all admissible beta; c1 = a, c2 = 2a - k;
vdim = 2 and m(beta) = 0 for 33 classes (a <= 7), with the general proof
in Section 2 covering all a. No numeric value of Db_beta itself is claimed
by brute force; equality is proved structurally.

## 8. Limitations and separation of proof / citation / computation

- Proven locally from definitions: all intersection theory, anticanonical
  property, node count, effectiveness, contact orders, virtual dimension,
  and m(beta) = 0 identically.
- Cited as established theorems (not re-proved): ACGS decomposition,
  Nishinou-Siebert toric correspondence, Kontsevich-Soibelman/Gross-Siebert
  consistency, GHK broken-line--tropical dictionary, and the genus-0
  toric-model Frobenius/intrinsic-mirror correspondence (Bousseau;
  Gross-Siebert). The new content is the verification that this family
  lies in the primary (m = 0) sector with a toric model, so these theorems
  compose to the claimed equality for all admissible beta.
- No literature search was needed: no method gap beyond standard citable
  theorems arose.
- Uncertainty: none on the equality itself given the cited theorems; any
  residual risk resides in the correctness of those published results,
  which is outside the scope of this lane.
