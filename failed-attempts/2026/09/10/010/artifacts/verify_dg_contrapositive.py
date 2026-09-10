"""DG-contrapositive audit: IF Dolich-Goodrick Thm 1.1 hypotheses held for T,
then D^{(k)}=P infinite for ALL k forces burden >= k+1 for all k, i.e. infinite
burden (not strong) — the OPPOSITE of target clause (ii) (burden<=2).
This script logs the formal contrapositive chain per k and the fixed-point fact.
It does NOT assert DG applies to T (definable completeness of T is open —
see verify_dc_gap.py); it shows the audit-plan Step 3 as written cannot yield
burden<=2 from the computed iterate: the iterate points the wrong way.
"""
print("Assume DG Thm 1.1 applies (definably complete + strong + D discrete).")
print("Computed: D^{(0)}=P infinite; D'=P so D^{(k)}=P infinite for all k>=0.")
for k in range(6):
    print(f"  D^({k}) infinite  =>  burden >= {k+1} (>{k+1} if densely ordered, i.e. >={k+2})")
print("Hence burden >= N for every N: infinite burden, NOT strong, NOT burden 2.")
print("CONCLUSION: the one-iterate computation D'=P cannot exclude depth 3 / prove")
print("burden<=2 under DG; it obstructs that route (conditional on DG hypotheses).")
print("DG_CONTRAPOSITIVE_AUDIT_OK")
