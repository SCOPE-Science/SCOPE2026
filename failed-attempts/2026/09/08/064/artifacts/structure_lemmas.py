"""Structural lemmas for putative binary [36,11,13] (exact, no floats).

L1 (even-weight subcode). Let C be a putative [36,11,13]. The parity functional
     p(x) = sum of coordinates (mod 2) restricted to C is either 0 or onto.
     - If p == 0, all weights of C are even; then d >= 14 (odd weights absent).
     - If p is onto, ker(p) is a [36,10,d'] subcode with d' >= 14 (even weights
       of C are >= 14 since odd weights 13 are killed... careful: d' is the min
       over EVEN weights of C, all >= 14 as 13 is odd).
     EITHER WAY: C contains a binary [36,10,d''] subcode with d'' >= 14
     (itself if all-even, else its even subcode).
     Griesmer G(10,14) = 33 <= 36: allowed. G(10,16) = 36 <= 36: even d''=16
     allowed too; d''>=18 needs G(10,18) = 42 > 36, excluded.
     => Lemma: some [36,10,d''] with d'' in {14,16} sits inside C (odd d''
     impossible for an even-weight code).
     NOTE this does not kill; it constrains: BKLC table value d(36,10) is 13
     per the failed-neighbor record (SCOPE-FAIL-20260907-045 targeted [36,10,14]
     as OPEN) — so a [36,10,14] subcode would itself close the neighboring cell!
     Consequence: [36,11,13] => [36,10,14] exists (as even subcode or self) =>
     the (36,11) question IMPLIES the (36,10) question. New reduction link.

L2 (all-even alternative). If C is all-even, then the all-ones vector 1 is in
     C^perp... (standard: C subset 1^perp => 1 in C^perp). Dual is [36,25,d^perp].
     No kill attempted; recorded as structural fork:
       Fork A: C all-even [36,11,>=14] (all weights even, contains ...);
       Fork B: C has odd words, even subcode [36,10,>=14].
     In Fork A, C itself is a [36,11,14] code; G(11,14) = 34 <= 36 allowed.

L3 (residual, from griesmer.py cert). Res w.r.t. any weight-13 word is
     [23,10,d*] with d* >= 7 and d* <= 8 (G(10,9)=25>23). Two subfamilies.
     Residual w.r.t. weight-14 word (if present): [22,10,d*], d*>=7, d*<=8
     (G(10,9)=25>22). Also two subfamilies.

L4 (shortening consistency, BKLC-cited). Shortening C twice at suitable
     coordinates gives [34,9,>=13]; tabled d(34,9) = 13 (closed): consistent,
     no contradiction. Puncturing/shortening to [33,9]: Heijnen forbids [33,9,13]
     but C-shortened descendants have dimension <= 10 with length <= 34, and the
     only forced high-minimum descendant is [34,9,>=13] which exists. No kill.

L5 (Brouwer–van Eijl doubling-type observation, exact count). C has 2048 words;
     average weight of a random nonzero word via shortening identity... recorded
     only as identity, no bound claimed.

All Griesmer numbers recomputed in griesmer.py (exact integer arithmetic).
"""
from math import ceil
import json

def griesmer(k, d):
    return sum(ceil(d / 2 ** i) for i in range(k))

G = {(10, 14): griesmer(10, 14), (10, 16): griesmer(10, 16),
     (10, 18): griesmer(10, 18), (11, 14): griesmer(11, 14),
     (10, 9): griesmer(10, 9), (10, 7): griesmer(10, 7), (10, 8): griesmer(10, 8),
     (11, 13): griesmer(11, 13)}
print(G)
assert G[(10, 14)] == 33 and G[(10, 16)] == 36 and G[(10, 18)] == 42
assert G[(10, 9)] == 25 and G[(11, 13)] == 33 and G[(11, 14)] == 34

doc = {
    "griesmer_values": {str(k): v for k, v in G.items()},
    "L1_even_subcode": "[36,11,13] contains a [36,10,d''] even-weight subcode with d'' in {14,16}; hence [36,11,13]-existence IMPLIES [36,10,14]-existence (neighbor cell).",
    "L2_fork": "Fork A (C all-even): C is [36,11,>=14], G(11,14)=34<=36 allowed. Fork B: even subcode [36,10,>=14].",
    "L3_residual": "Res(wt-13 word)=[23,10,d*], d* in {7,8}; Res(wt-14 word)=[22,10,d*], d* in {7,8}.",
    "L4_shortening": "Two shortenings give [34,9,>=13], consistent with closed d(34,9)=13; Heijnen anchor gives no contradiction. No kill claimed.",
}
with open("cert_structure_lemmas.json", "w") as f:
    json.dump(doc, f, indent=1)
print("wrote cert_structure_lemmas.json")
