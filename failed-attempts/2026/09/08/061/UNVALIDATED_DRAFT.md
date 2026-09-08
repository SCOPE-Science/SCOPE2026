# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified Jones-collision census of the 11-crossing nonalternating table, with volume separation of two non-mutant classes and a tabulated-A2 non-separation transcript

## Theorem (proved by replayable computation; all data cited or recomputed)

Let K11n1–K11n185 be the Hoste–Thistlethwaite nonalternating 11-crossing
prime knots with KnotAtlas PD presentations P(K) and published Jones
polynomials J_pub(K).

1. **Full Jones recomputation.** The from-scratch pipeline of §2 applied to
   each P(K) returns a polynomial J(K) with
   J(K) = J_pub(K) for all 185 knots (185/185 agreement).
2. **Collision census.** Exactly 15 Jones-equality classes of size ≥ 2 occur:
   14 pairs and one triple, listed in §3. Every other 11n knot is
   Jones-unique within the 11n table (169 distinct Jones values total).
3. **Non-mutant separation by volume (first pair).** The lexicographically
   first colliding pair, K11n11 and K11n112, satisfies
   J(K11n11) = J(K11n112)
     = −q^8+3q^7−6q^6+8q^5−9q^4+10q^3−8q^2+6q−3+q^{−1},
   (recomputed here and equal to both published values), and the two knots
   share the same HOMFLY-PT polynomial (tabled), yet their tabled hyperbolic
   volumes differ, 13.0518 vs 13.3686, and their symmetry types differ
   (Chiral vs Reversible). Hence they are not mutants and are separated by
   volume where Jones and HOMFLY-PT both fail.
4. **Non-mutant separation by volume (triple class).** K11n7, K11n36, K11n44
   all satisfy
   J = −2q^6+5q^5−8q^4+11q^3−11q^2+11q−9+6q^{−1}−3q^{−2}+q^{−3}
   (recomputed and published). K11n36/K11n44 share volume 14.4828 (mutant
   signature), while K11n7 has volume 13.8902, so K11n7 is separated from the
   mutant pair by volume.
5. **Tabulated-A2 non-separation.** In all 7 collision classes where both
   (resp. all) members have tabled KnotAtlas A2 values —
   {34,42}, {35,43}, {36,44}, {39,45}, {40,46}, {41,47}, {151,152} — the
   tabled A2 polynomials are identical within each class (values in §4).
   Hence the A2 invariant, as far as tabled, does not separate any of these
   Jones-equal classes. The remaining classes have at least one member with
   no A2 entry (404 on the Data page), so A2-separation there is undecided.

## 2. Method (from scratch; artifact `jones_pd.py`)

For a PD presentation X[a,b,c,d] per crossing (positions 0–3 in listed
cyclic order):

- (i) Trace the knot as an Eulerian circuit of the 4-regular shadow using
  the strand-through pairing {0,2}/{1,3}; assert the walk closes after 2n
  steps visiting every crossing twice (fails loudly otherwise).
- (ii) Writhe: at each crossing take the oriented over-chord and
  under-chord (entry→exit vectors at angles p·90°) from the traversal and
  set sign = sign of their 2D cross product; w = Σ signs.
- (iii) Kauffman bracket state sum over all 2^n smoothings with a
  union-find loop counter: bit 0 pairs edges (t0,t1)&(t2,t3) with weight A
  (the positional P0 smoothing), bit 1 pairs (t0,t3)&(t2,t1) with weight B;
  each k extra loops contribute (−A²−A⁻²)^k expanded exactly over integers.
- (iv) Normalize by (−A³)^{−w}, substitute A = t^{−1/4}, and assert all
  quarter-exponents are divisible by 4 (integral q-powers); fail otherwise.

Calibration (8 controls, all exact): 3_1, 4_1, 10_22, 10_35 (the documented
same-Jones pair, both returning the identical polynomial), K11n1, K11n2,
K11n34, K11n42. The uniform-P0 A-assignment plus chord-sign writhe is the
unique small-convention choice reproducing all controls; 10_22/10_35
equality is reproduced, not assumed. Full-table check: 185/185 recomputed
Jones equal the published `Data:K11n*/Jones_Polynomial` values (parsed
independently, constants included). Replay: `python3` with only the
standard library; the 185-knot census runs in ~6 s (11 crossings ⇒ 2048
states each); see `jones11n_computed.json` (recomputed values + writhes),
`pd11n.json` (inputs), `dt11n.json`, `volsym_tabled.json`,
`a2cmp_tabled.json` (tabled comparison values with fetch provenance).

## 3. The 15 collision classes (recomputed; each verified against published)

[K11n11, K11n112], [K11n124, K11n166], [K11n132, K11n50],
[K11n148, K11n168], [K11n150, K11n66], [K11n151, K11n152],
[K11n21, K11n4], [K11n28, K11n64], [K11n34, K11n42], [K11n35, K11n43],
[K11n36, K11n44, K11n7] (triple), [K11n39, K11n45], [K11n40, K11n46],
[K11n41, K11n47], [K11n73, K11n74].

Tabled hyperbolic volumes/symmetries per class (from
`Data:K11n*/HyperbolicVolume`, `Data:K11n*/Symmetry_Type`):
same-volume (mutant-signature) classes: {34,42}: 11.2191; {35,43}: 15.7945;
{36,44}: 14.4828; {39,45}: 12.7511; {40,46}: 15.4047; {41,47}: 13.7623;
{151,152}: 12.4339; {73,74}: 10.4045. Distinct-volume (non-mutant)
collisions: {11: 13.0518 Chiral, 112: 13.3686 Reversible};
{124: 13.6991, 166: 14.1954}; {132: 10.2668, 50: 10.2068};
{148: 15.4617, 168: 15.0132}; {150: 14.7873, 66: 14.4341};
{21: 12.468, 4: 12.5531}; {28: 8.06165, 64: 7.23965};
{7: 13.8902 vs 36/44: 14.4828}.

## 4. Tabled A2 values used in (5) (from `Data:K11n*/QuantumInvariant/A2/1,0`)

K11n34 = K11n42 =
q^18+q^14−q^12−q^10−q^8−2q^6+q^4+3+2q^{−2}+q^{−4}+q^{−6}−q^{−8}−q^{−12};
K11n35 = K11n43 =
3q^{−6}−q^{−8}+4q^{−10}+q^{−12}−2q^{−14}+2q^{−16}−5q^{−18}+q^{−20}−2q^{−22}
+3q^{−26}−2q^{−28}+2q^{−30}−q^{−34};
K11n36 = K11n44 =
q^8−q^6+2q^4−q^2+q^{−2}−3q^{−4}+3q^{−6}−2q^{−8}+3q^{−10}+q^{−12}+2q^{−16}
−2q^{−18}−q^{−22};
K11n39 = K11n45 =
−q^{12}−q^{10}−q^8+q^6+3q^2+3+q^{−2}+2q^{−4}−2q^{−6}−2q^{−10}−q^{−12}
+q^{−14}−q^{−16}+q^{−18};
K11n40 = K11n46 =
−2+2q^{−2}−2q^{−4}+q^{−6}+4q^{−8}+5q^{−12}−q^{−14}+q^{−16}−q^{−18}−4q^{−20}
+q^{−22}−2q^{−24}+q^{−28};
K11n41 = K11n47 =
−q^2+1−q^{−2}+q^{−4}+q^{−6}+q^{−8}+4q^{−10}−q^{−12}+3q^{−14}−2q^{−16}−q^{−18}
−q^{−20}−2q^{−22}+q^{−24}−q^{−26}+q^{−28};
K11n151 = K11n152 =
q^6+q^4+2q^2+q^{−2}−2q^{−4}−2q^{−6}−2q^{−10}+2q^{−12}+2q^{−16}+q^{−18}
−q^{−20}+q^{−22}−q^{−24}.
Single-sided tabled A2 (partner missing, HTTP 404, gap confirmed):
K11n11 =
q^4−1+2q^{−2}−2q^{−4}+q^{−6}+q^{−8}+3q^{−12}−q^{−14}+2q^{−16}−q^{−18}−2q^{−20}
+q^{−22}−q^{−24} (K11n112 missing);
K11n148 =
q^8−2q^6+q^4−2q^2+2q^{−2}−q^{−4}+6q^{−6}−q^{−8}+3q^{−10}−q^{−12}−2q^{−14}
+q^{−16}−2q^{−18}+q^{−20}−q^{−22} (K11n168 missing);
K11n166 =
q^8−q^6+2q^4+1+q^{−2}−3q^{−4}+2q^{−6}−3q^{−8}+2q^{−10}+2q^{−16}−q^{−18}
+q^{−20}−q^{−22} (K11n124 missing).

## 5. Limitations and open part (explicitly not claimed)

- No new A2 (quantum sl3) polynomial is computed here: implementing a
  verified Kuperberg-spider web-resolution recursion was beyond the
  available budget, so the target "first A2 separation certificate" is
  NOT established. The A2 contribution is the certified non-separation
  transcript (5) from tabled values plus confirmed gap pages.
- Volume/symmetry/HOMFLY/A2 comparison values are cited from live KnotAtlas
  Data pages (fetched via action=raw; HTTP 404 = confirmed gap), not
  recomputed; only the Jones equalities are proved twice over (our pipeline
  vs the published table, 185/185).
- The A2-gap scan covered K11n1–139 by live fetch (87 present overall);
  presence/absence for individual knots cited above was each confirmed by a
  direct fetch (200 vs 404).
- The bracket pipeline's A-smoothing/writhe convention is fixed
  empirically by 8 exact controls; it is a verified-correct Jones computer
  on this corpus (185/185), not a general skein-theoretic theorem.
