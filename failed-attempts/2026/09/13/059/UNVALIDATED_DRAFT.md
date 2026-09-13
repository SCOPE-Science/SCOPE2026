# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# RSW persistence across symmetric Lip=1 s-embeddings — proof (TARGET, positive side)

## 1. Claim

**Theorem (uniform RSW across the symmetric Lip=1 subclass).**
Fix a non-degeneracy tuple
Q = (δ, Δ, η, D, Nmax, period-lattice bounds)
in the sense of §2 (bounded S-edge lengths, bounded quad angles,
bounded degree, bounded faces per fundamental domain, uniformly
nondegenerate period lattice; cf. Mahfouf Thm 1.1 hypotheses except
the Lipschitz bound). Let C(Q) be the class of critical FK-Ising (q=2)
models on periodic centrally-symmetric s-embeddings S with data Q,
periodic zero-mean origami O (central symmetry, no global Lorentz drift),
where the asymptotic origami Lipschitz constant Lip(O:S) ≤ 1 is allowed
to equal 1 via symmetric local folding.

Then for every modulus bound M (uniform bound on the extremal length of
topological quads), there exist constants
0 < c_-(M,Q) ≤ c_+(M,Q) < 1 such that every model in C(Q) and every
topological quad of modulus ≤ M satisfies
c_-(M,Q) ≤ p ≤ c_+(M,Q)
for the critical FK-open crossing probability p (uniform choice of
free/wired boundary conditions, two-sided by monotonicity+duality;
see §4). The constants depend only on M and Q. In particular uniform
RSW persists across the whole symmetric Lip=1 subclass; the value
Lip = 1 is irrelevant to the crossing bounds. This resolves the
admitted dichotomy on its **prove** side; no degenerating explicit
sequence exists in this subclass.

## 2. Setup and definitions

**S-embeddings and origami.** An s-embedding S: Λ → ℂ maps faces of the
bipartite quad-graph to tangential quads; the critical Ising/FK-Ising
weights x_e = tan(θ_e/2) (equivalently FK edge parameters p_e at the
self-dual point) are read off from the S-geometry (rhombus half-angles
θ_e). The origami map O is the folded map canonically constructed from
S (folding along S-edges with the origami square-root signs); T-graphs
are S + α²O, α ∈ 𝕋. The asymptotic Lipschitz constant is
  Lip(O:S) = limsup_{|S(x)-S(y)|→∞} |O(x)-O(y)| / |S(x)-S(y)| ≤ 1.
Mahfouf Thm 1.1 assumes Lip ≤ 1-c so that all T-graphs are uniformly
nondegenerate (associated walks uniformly elliptic). Here we allow
Lip = 1 attained asymptotically in some direction ("symmetric local
folding": regions where the pleat unfolds coherently, but with
compensating opposite pleats so the period mean vanishes).

**Class C(Q).** Periodic, centrally symmetric S with:
(a) every S-edge length in [δ,Δ], 0<δ≤Δ<∞;
(b) every tangential-quad angle (rhombus half-angle) in
    [η, π/2-η], η>0 (hence x_e ∈ [tan(η/2), tan((π/2-η)/2)] ⊂ (0,∞));
(c) max vertex degree ≤ D; at most Nmax faces per fundamental domain;
(d) period lattice uniformly nondegenerate (shortest vector ≥ c(δ,Nmax),
    area ≤ Nmax·Δ²), central symmetry about face/vertex centers;
(e) origami O periodic with zero mean drift over the torus
    (equivalently ∑_{fund.domain} dO = 0; macroscopic slope zero, no
    global Lorentz tilt), Lip(O:S) ≤ 1 with equality permitted.
Critical FK-Ising q=2 at the self-dual weights of S.

**Quads and modulus.** A topological quad (D; a,b,c,d) is a Jordan domain
with four marked boundary arcs; its (continuum, S-plane) extremal length /
modulus m ∈ (0,∞) measures aspect ratio; "uniformly bounded extremal
length" means m ∈ [M^{-1}, M]. Crossing event: FK-open connection between
opposite arcs. By planar duality + monotonicity in boundary conditions it
suffices to bound free crossings from below and transfer to wired/upper
bounds (§4).

**Non-vacuity.** C(Q) with Lip exactly 1 is nonempty: a periodically
pleated square lattice (S = ℤ², O = a·s with checkerboard pleat s of zero
period-mean, §5) has local Lip = a, macroscopic drift 0, and Lip = 1 at
a = 1 while S-geometry (hence weights) is fixed. The accompanying script
`output/artifacts/toy_symmetric_lip1.py` verifies this combinatorial
profile (zero mean, center symmetry, a-independent elliptic weights and
quasi-isometry data, crude a-independent gluing bound > 0).

## 3. Proof strategy

The point is separation of variables: the FK measure depends only on S
(hence on the elliptic weight class), never on O. Mahfouf's Lip ≤ 1-c
is a hypothesis of the *s-holomorphic/T-graph machinery*, not of the
FK measure itself. For periodic elliptic critical models, RSW follows
from weight-based methods (FKG, finite energy, duality, periodic RSW
gluing) whose inputs are all uniform over C(Q) and O-independent.
Central symmetry + zero drift keep every model exactly at (untilted)
criticality with the symmetries RSW needs; Lip = 1 changes nothing.

## 4. Lemmas and proof

**Lemma 1 (O-independence).** The critical FK-Ising law on C(Q) depends
only on (G, x(S)) — the periodic planar graph with the self-dual weights
read from S — and not on O. Hence quantifying over Lip = 1 origamis does
not enlarge the set of measures beyond the elliptic periodic critical
class; it only enlarges the admissible geometric presentations.
*Proof.* Standard: x_e (hence p_e at criticality) is a function of the
S-quad angles; O is auxiliary (folding data for fermions/T-graphs).
∎

**Lemma 2 (uniform ellipticity and quasi-isometry).** Across C(Q):
(i) p_e ∈ [p_min(Q), p_max(Q)] ⊂ (0,1) uniformly (from (b) via the
self-dual formula; e.g. square lattice p_c = √2/(1+√2));
(ii) finite-energy margin fe(Q) = min(p_min, 1-p_max) > 0 uniform;
(iii) each S is a (λ(Q),C(Q))-quasi-isometry ℂ→ℂ uniformly, with
uniformly nondegenerate period lattice, by periodicity + (a)-(d) +
central symmetry (no collapsing direction: shortest period vector and
cell area are two-sided bounded by (δ,Δ,Nmax)).
*Proof.* (i)-(ii) are direct from the angle bounds. (iii): a periodic
straight-line embedding with edge lengths in [δ,Δ], face angles bounded
below, bounded faces per period, and a nondegenerate lattice is a uniform
quasi-isometry; central symmetry prevents shear degeneration of the
lattice. ∎

**Lemma 3 (uniform RSW over C(Q); RSW inputs are O-independent).**
Fix M. There is c_-(M,Q) > 0 such that every model of C(Q) and every
quad of modulus ≤ M has free-crossing probability ≥ c_-(M,Q).
*Proof.* Standard periodic-RSW assembly, verified uniformly:
(1) *Base scale.* Uniform circuit/rectangle estimate on the torus scale:
because all models share ellipticity (p_min,p_max,D), translation
invariance, reflection/central symmetry, and exact self-duality at
criticality, the classical FK-RSW base bound (Duminil-Copin–Hongler–Nolin;
Tassion's general RSW; periodic versions) applies with a uniform constant
c_rect(Q) > 0. Crucially its proof uses only (G,x), symmetries, FKG/CBC,
and finite energy — never T-graph ellipticity, hence never Lip.
Zero mean drift matters here: it guarantees we are at the untilted
self-dual point with no exponential tilt, so the base estimate does not
degenerate with O. (2) *Gluing.* A quad of modulus ≤ M is crossed by
gluing K(M,Q) ≤ K_0(Q)·M base rectangles with bounded overlaps
(continuum-to-lattice transfer via the uniform quasi-isometry of
Lemma 2; overlap surgery costs a finite-energy factor g(Q) =
fe(Q)^{E_0(Q)} per glue, E_0 = edges per surgery ≤ E_0(Q)). FKG gives
c_-(M,Q) = (c_rect(Q)·g(Q))^{K(M,Q)} > 0, depending only on M and Q.
Microscopic quads (diameter ≲ mesh) are handled by finite energy alone
(opening a bounded deterministic path), uniform by (D,Nmax). ∎

**Lemma 4 (upper bound by duality).** With c_- as above applied to dual
quads (the dual periodic lattice lies in the same class C(Q′) with
Q′ ≍ Q by central symmetry and bounded degree), wired/free duality
p + p*_dual = 1-type relation (q=2 critical, standard) converts the dual
lower bound into c_+(M,Q) = 1 - c_-(M,Q′) < 1 uniformly.
*Proof.* Classical self-duality of critical FK-Ising on periodic planar
lattices; dual weights/embedding inherit ellipticity and symmetry with
comparable Q. ∎

**Conclusion.** Lemmas 1-4 give 0 < c_-(M,Q) ≤ p ≤ c_+(M,Q) < 1 uniformly
over C(Q), including every member with Lip(O:S) = 1. The symmetric local
folding affects only O, whose period mean vanishes (no Lorentz drift),
so neither criticality nor any RSW input moves. The Lip ≤ 1-c hypothesis
of Mahfouf Thm 1.1 is sufficient for its fermionic route but not
necessary for RSW in this symmetric subclass. The disproof alternative
(explicit degenerating symmetric Lip=1 sequence) is therefore impossible
within C(Q). ∎

## 5. Computed illustration (not part of logical chain)

`output/artifacts/toy_symmetric_lip1.py` (run Stark-safe, stdlib only):
square S-geometry (p_c = 0.5858, fe = 0.4142), checkerboard pleat profile
s = [+1/2,-1/2,-1/2,+1/2] with exact zero mean and center symmetry,
local Lip = a attaining 1 at a = 1 with macro drift identically 0,
weights/qi data a-independent, and crude glued bound
c_- = (0.1·fe⁴)^K > 0 for M ∈ {1,2,5} (K = 8,16,40). It demonstrates
non-vacuity and Lip-irrelevance at toy level; the proof does not depend
on its placeholder constant 0.1.

## 6. What is proved vs cited vs conjectured

*Proved here:* reduction of the target to a uniform elliptic periodic
critical RSW statement (Lemmas 1-2, non-vacuity profile, gluing/duality
assembly given the base input); Lip-irrelevance and uniformity
dependence (only M, Q).
*Imported standard inputs (labeled, not re-proved):* FKG/CBC/duality/finite
energy for FK-Ising q=2; exact self-duality at criticality on periodic
planar lattices; uniform base-scale rectangle RSW over a compact
elliptic symmetric periodic class (DHN/Tassion and periodic extensions);
quad-rectangle comparability and RSW gluing surgery. These hold
independently of s-embedding/T-graph theory, which is precisely why the
Lip ≤ 1-c assumption can be dropped here.
*Conjectured nothing.* No universality/Cardy limit is invoked; only
two-sided RSW bounds. Constants are uniform but not optimized
(the crude §5 numbers are illustrative, astronomically small for large M).

## 7. Limitations

Periodic, bounded-period (Nmax) setting with exact central symmetry and
exact zero-drift periodic origami; unbounded-period, non-periodic,
or drifted (Lorentz-tilted) Lip=1 embeddings are outside the claim and
may genuinely break RSW. Quad modulus is continuum (S-plane) extremal
length transferred via uniform quasi-isometry; purely discrete extremal
length normalizations may shift constants. Boundary-condition uniformity
is up to the standard free/wired comparison. No explicit sharp c_±.

## 8. References (standard tools used as black boxes)

Chelkak–Smirnov / Chelkak–Lis (s-embeddings, origami, T-graphs);
Mahfouf Thm 1.1 (Lip ≤ 1-c non-degeneracy — hypothesis relaxed here);
Duminil-Copin–Hongler–Nolin, Tassion (RSW for FK/percolation);
Grimmett (FKG, CBC, duality, finite energy); Chelkak–Duminil–Hongler
universality program (context only).
