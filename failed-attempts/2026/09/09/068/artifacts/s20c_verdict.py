"""Step 20c (model audit verdict): is D_w = A_w on 0 mod 4 even the right constraint?
C0 = doubly-even [72,35] subcode of putative self-dual C. C0^perp = C + C1 + C2
where C1 = C0^perp \\ C has 2^35 words. The equation D = 2^-35 K C0 is EXACT
(MacWilliams, no assumption). The QUESTION is only what D must look like.
Claim used in s20/s20b: D_w = A_w for w = 0 mod 4, i.e. cosets C1,C2 have NO
weight-0-mod-4 words (their union = shadow, weights 2 mod 4). That holds for a
Type-II C0 *with a Type-I-like neighbor structure*... For Type-II C0 containing 1:
C0^perp / C0 is a 2-dim space? No: dim C0^perp = 37, C0 dim 35, C dim 36 sits
between. C0^perp = C0 + span{a,b}? The coset representatives: C1 = u+C0,
C2 = u+1+C0?? with u in C0^perp \\ C. Weights of u+C0: u has even weight; if u is
singly-even... but C contains ONLY doubly-even words, and C0 subset C. u not in C.
u+C0 for u doubly-even: all words doubly-even -> D_w > A_w possible on 0 mod 4
with NO contradiction. The 0-mod-4 equality D=A requires the cosets to be
singly-even, which needs 1 NOT in C0^perp... but 1 in C (Type II, 8|72) and
C subset C0^perp, so 1 in C0^perp; the coset u+C0 vs u+1+C0 have OPPOSITE parity
classes mod 4? If u doubly-even: u+C0 doubly-even, u+1+C0 singly-even. So
D = A + E + O with E doubly-even part, O singly-even part; D_w = A_w + E_w on
0 mod 4 with E_w >= 0 FREE. Constraint D_w=A_w is WRONG in general (only the
sum over the PAIR is fixed by MW). s20 inconsistency is a MODELING ARTIFACT.
Correct residual: no constraint violated. Record verdict honestly.
Also verify: E_w=0 for all w (i.e., C1 doubly-even-free) would force s20 system;
since system is inconsistent, every codim-1 subcode has doubly-even words outside
C — a structural lemma, NOT an exclusion of C.
"""
import json
import os
HERE = os.path.dirname(os.path.abspath(__file__))
json.dump({"verdict": "s20/s20b inconsistency is a MODELING ARTIFACT: imposed D_w=A_w "
                      "on 0 mod 4 assumes both C0^perp cosets outside C are singly-even, "
                      "which is false in general (one coset is doubly-even when 1 in C0^perp). "
                      "Correct MacWilliams D = 2^-35 K C0 leaves E_w >= 0 free. "
                      "No exclusion of the putative [72,36,16] code follows. "
                      "Structural corollary (lemma): no doubly-even [72,35] subcode of the "
                      "putative code can have both outside-cosets singly-even.",
           "exclusion_claimed": False},
          open(os.path.join(HERE, "s20c_verdict.json"), "w"), indent=1)
print("wrote s20c_verdict.json: NO exclusion — artifact documented")
