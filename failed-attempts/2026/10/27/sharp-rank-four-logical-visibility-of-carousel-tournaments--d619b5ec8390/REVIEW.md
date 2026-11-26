# Independent mathematical audit

## correctness

PASS

The even vertex sites and odd antipodal gap sites give the half-circle arc relation. With at least one mark pair, the antipodal translation pairs distinct oriented intervals; inserting a new vertex also splits its partner at the translated offset. For r further picks use threshold T_r=2T_{r−1}+2. Equal intervals copy the offset. In unequal large intervals copy any short side exactly (endpoint kind gives the required parity); otherwise there are at least two consecutive admissible positions, one of vertex kind. The remaining gaps meet threshold T_{r−1}, and repeated picks need no insertion. At zero rounds the mark order determines edges and equality. A first pick leaves two intervals of length n−1, so n≥2^q−1 suffices. Finite separation has an independent analytic check: N⁺(a) is a transitive tournament on h=(n−1)/2 vertices. Within that order, the property of having at least s elements has rank at most ceil(log₂(s+1)): choose a pivot and require, in separate conjuncts, enough elements on either side, splitting s−1 as evenly as possible. Relativization to N⁺(a) costs no rank; an outer existential a gives rank at most four for each threshold h≥s, s=1..7. These thresholds separate all eight representatives including n=1. An independent exact recursive type calculation also gave classes (1),(3),(5),(7),(9),(11),(13),(15,17,19). Replay: /workspace/branches/ae8de13d-17e2-4ae0-bbf3-00f292f198b0/independent_rank4.py and independent_rank4_full.txt in the same directory. The supplied verifier was inspected but not executed. The independent finite calculation covers only those ten sizes; the interval lemma accounts for the infinite tail.

## originality

FAIL

The central rank-four classification and uniform all-rank tail are covered for orders ≥3 by the distinct Resultary exact rank-shift theorem, which gives a full all-rank classification. Adding R_1 contributes only the immediate singleton test at rank two, and does not establish a distinct substantive finding.

## value

FAIL

An exact logical resolution threshold for a natural tournament family is worthwhile, but that substantive threshold is already available from the general rank-shift theorem. The extra singleton is an immediate rank-two distinction; the finite recomputation and alternate sufficient tail argument do not establish a further independently useful invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
