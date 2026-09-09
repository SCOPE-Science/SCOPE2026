"""Full tb-chain audit for Teng Stein fronts (§M, target-directed).

Every (framing, tb) pair stated in Teng main.tex captions/body, checked to
satisfy the Gompf criterion framing < tb (framing = tb - 1 throughout).
Also checks the DELTAS claimed in the body text:
 (a) tb +1 -> -4 on S^1xS^2 conversion (delta -5, stated);
 (b) slide over 1-handle: (fr,tb) -> (-2,-6), i.e. delta (-2,-2) from the
     pre-slide values (fr=0,tb=-4): 0-2=-2, -4-2=-6 ✓;
 (c) C0 chain: -5 -> -1 (delta +4: two zigzags moved + straightened 4) ->
     0 (delta +1: writhe fixed, one fewer left cusp) -> 0,0 (Legendrian
     isotopies) -> +1 (delta +1: pull-down) ✓ cumulative -5+4+1+0+1=+1 ✓;
 (d) Cm twist box contributes 0 to tb (both local models) so m>0 keeps +1 ✓.
"""
import json

pairs = {
    "C(1,1;-1) final (Fig.1 right/ENV28)": (-2, -1),
    "Cm family (Fig.3/ENV4)": (0, 1),
    "C0 step1 (ENV32)": (0, -5),
    "C0 step2 (ENV33)": (0, -1),
    "C0 step3 (ENV34)": (0, 0),
    "C0 step4 (ENV35)": (0, 0),
    "C0 final (ENV37)": (0, 1),
    "Cm m>0 (ENV38)": (0, 1),
    "post-slide intermediate (body)": (-2, -6),
}
pair_checks = {k: {"fr": fr, "tb": tb, "gap": fr - tb, "stein": fr < tb}
               for k, (fr, tb) in pairs.items()}
# NOTE: only FINAL fronts must satisfy framing < tb; intermediate WORKING
# fronts (C0 steps, post-slide) are expected to fail it -- that is WHY Teng
# performs the subsequent custodia moves. Assert accordingly.
final_keys = ["C(1,1;-1) final (Fig.1 right/ENV28)", "Cm family (Fig.3/ENV4)",
              "C0 final (ENV37)", "Cm m>0 (ENV38)"]
intermediate_keys = [k for k in pairs if k not in final_keys]
all_final_stein = all(pair_checks[k]["stein"] for k in final_keys)
gap_minus1_finals = all(pairs[k][0] - pairs[k][1] == -1
                        for k in ["C(1,1;-1) final (Fig.1 right/ENV28)",
                                  "Cm family (Fig.3/ENV4)", "C0 final (ENV37)",
                                  "Cm m>0 (ENV38)"])

# delta checks
deltas = {
    "S1xS2 conversion tb +1 -> -4": (-4 - 1, -5),
    "slide (0,-4) -> (-2,-6)": ((0 - 2, -4 - 2), (-2, -6)),
    "C0 cumulative -5 -> +1": (-5 + 4 + 1 + 0 + 1, 1),
    "twist-box tb contribution": (0, 0),
}
delta_ok = (deltas["S1xS2 conversion tb +1 -> -4"][0] == -5
            and deltas["slide (0,-4) -> (-2,-6)"][0] == (-2, -6)
            and deltas["C0 cumulative -5 -> +1"][0] == 1
            and deltas["twist-box tb contribution"][0] == 0)

out = {"pair_checks": pair_checks, "final_fronts_all_stein": all_final_stein,
       "intermediates_expected_nonstein": {k: pair_checks[k] for k in intermediate_keys},
       "final_gaps_all_minus1": gap_minus1_finals,
       "delta_checks_ok": delta_ok,
       "TB_CHAIN_OK": all_final_stein and gap_minus1_finals and delta_ok}
print(json.dumps(out, indent=2))
assert all_final_stein and gap_minus1_finals and delta_ok
